from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from src.ranker_v2.evidence_tracing import (
    EvidenceRecord,
    OWNERSHIP_TERMS,
    SCALE_TERMS,
    normalize_text,
    term_hits,
    trace_candidate_evidence,
)


FAMILY_WEIGHTS = {
    "search_ranking": 0.33,
    "retrieval": 0.23,
    "evaluation": 0.18,
    "recommendation": 0.12,
    "vector_search": 0.07,
    "behavioral": 0.07,
}

FAMILY_SCALES = {
    "search_ranking": 24.0,
    "retrieval": 20.0,
    "evaluation": 18.0,
    "recommendation": 11.0,
    "vector_search": 9.0,
}

AI_SKILL_TERMS = {
    "ai",
    "machine learning",
    "ml",
    "deep learning",
    "llm",
    "rag",
    "langchain",
    "fine-tuning",
    "fine tuning",
    "cuda",
    "mlops",
    "pytorch",
    "tensorflow",
    "nlp",
    "computer vision",
    "embeddings",
    "vector",
}

TECHNICAL_TITLE_TERMS = {
    "engineer",
    "scientist",
    "developer",
    "architect",
    "data",
    "machine learning",
    "ml",
    "search",
    "software",
    "backend",
}

CONSULTING_TERMS = {
    "consulting",
    "consultant",
    "deloitte",
    "accenture",
    "pwc",
    "kpmg",
    "ey",
    "capgemini",
    "infosys",
    "tcs",
    "wipro",
    "cognizant",
}

PRODUCT_COMPANY_TERMS = {
    "google",
    "microsoft",
    "amazon",
    "meta",
    "netflix",
    "apple",
    "uber",
    "airbnb",
    "linkedin",
    "adobe",
    "salesforce",
    "flipkart",
    "swiggy",
    "zomato",
    "razorpay",
    "phonepe",
    "zoho",
    "freshworks",
    "product",
    "saas",
}


@dataclass
class CandidateV2Features:
    candidate_id: str
    current_title: str
    current_company: str
    years_of_experience: float
    skills: list[str]
    evidence_records: list[EvidenceRecord] = field(default_factory=list)
    raw_family_scores: dict[str, float] = field(default_factory=dict)
    family_scores: dict[str, float] = field(default_factory=dict)
    evidence_counts: dict[str, int] = field(default_factory=dict)
    max_evidence_level: int = 0
    level4_5_count: int = 0
    relevant_role_count: int = 0
    relevant_duration_months: float = 0.0
    ownership_term_count: int = 0
    scale_term_count: int = 0
    skill_count: int = 0
    ai_skill_count: int = 0
    career_ai_evidence_count: int = 0
    career_relevance_raw: float = 0.0
    market_signals: dict[str, float] = field(default_factory=dict)
    product_company_months: float = 0.0
    consulting_months: float = 0.0
    total_career_months: float = 0.0
    consistency_points: float = 0.0
    consistency_reason_codes: str = ""
    trust_points: float = 0.0
    trust_reason_codes: list[str] = field(default_factory=list)
    template_repetition: bool = False
    keyword_stuffer: bool = False
    ai_transition: bool = False
    consulting_only: bool = False


@dataclass
class ScoredCandidateV2:
    candidate_id: str
    search_ranking_score: float
    retrieval_score: float
    evaluation_score: float
    recommendation_score: float
    vector_search_score: float
    behavioral_score: float
    trust_score: float
    trust_penalty: float
    final_score: float
    score_cap: float | None
    calibration_penalty: float


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        number = float(value)
        if math.isnan(number):
            return default
        return number
    except (TypeError, ValueError):
        return default


def bounded(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def saturating_score(raw: float, scale: float) -> float:
    if raw <= 0:
        return 0.0
    return bounded(1.0 - math.exp(-raw / scale))


def np_percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    values = sorted(values)
    index = (len(values) - 1) * percentile / 100.0
    low = math.floor(index)
    high = math.ceil(index)
    if low == high:
        return values[int(index)]
    return values[low] * (high - index) + values[high] * (index - low)


def build_market_reference(candidates: list[dict[str, Any]]) -> dict[str, float]:
    values: dict[str, list[float]] = {
        "search_appearance_30d": [],
        "saved_by_recruiters_30d": [],
        "profile_views_received_30d": [],
    }
    for candidate in candidates:
        signals = candidate.get("redrob_signals", {})
        for key in values:
            values[key].append(safe_float(signals.get(key)))
    return {f"{key}_p95": max(np_percentile(nums, 95), 1.0) for key, nums in values.items()}


def extract_candidate_features_v2(candidate: dict[str, Any]) -> CandidateV2Features:
    profile = candidate.get("profile", {})
    skills = [str(skill.get("name", "")) for skill in candidate.get("skills", [])]
    features = CandidateV2Features(
        candidate_id=str(candidate.get("candidate_id", "")),
        current_title=str(profile.get("current_title", "")),
        current_company=str(profile.get("current_company", "")),
        years_of_experience=safe_float(profile.get("years_of_experience")),
        skills=skills,
        skill_count=len(skills),
    )
    features.evidence_records = trace_candidate_evidence(candidate)
    collect_family_scores(features)
    collect_career_context(candidate, features)
    collect_market_signals(candidate, features)
    collect_trust_signals(candidate, features)
    return features


def collect_family_scores(features: CandidateV2Features) -> None:
    raw = Counter()
    counts = Counter()
    for record in features.evidence_records:
        raw[record.feature_family] += record.contribution
        counts[record.feature_family] += 1
        features.max_evidence_level = max(features.max_evidence_level, record.evidence_level)
        if record.evidence_level >= 4:
            features.level4_5_count += 1
    features.raw_family_scores = {family: round(raw.get(family, 0.0), 6) for family in FAMILY_SCALES}
    features.family_scores = {
        family: round(saturating_score(features.raw_family_scores[family], FAMILY_SCALES[family]), 6)
        for family in FAMILY_SCALES
    }
    features.evidence_counts = {family: int(counts.get(family, 0)) for family in FAMILY_SCALES}


def collect_career_context(candidate: dict[str, Any], features: CandidateV2Features) -> None:
    career_text = normalize_text(" ".join(role.get("description", "") for role in candidate.get("career_history", [])))
    features.ownership_term_count = len(term_hits(career_text, OWNERSHIP_TERMS))
    features.scale_term_count = len(term_hits(career_text, SCALE_TERMS))
    features.ai_skill_count = len(term_hits(normalize_text(" ".join(features.skills)), AI_SKILL_TERMS))

    career_evidence_locations = {
        record.source_location
        for record in features.evidence_records
        if record.source_type == "career_description"
        and record.feature_family in {"search_ranking", "retrieval", "evaluation", "recommendation", "vector_search"}
    }
    for idx, role in enumerate(candidate.get("career_history", [])):
        duration = safe_float(role.get("duration_months"))
        features.total_career_months += duration
        source_location = f"career_history[{idx}].description"
        if source_location in career_evidence_locations:
            features.relevant_role_count += 1
            features.relevant_duration_months += duration
        role_records = [record for record in features.evidence_records if record.source_location == source_location]
        features.career_relevance_raw += sum(record.contribution for record in role_records) * (1.0 + min(duration, 60.0) / 180.0)
        company_text = normalize_text(f"{role.get('company', '')} {role.get('industry', '')} {role.get('description', '')}")
        if term_hits(company_text, PRODUCT_COMPANY_TERMS):
            features.product_company_months += duration
        if term_hits(company_text, CONSULTING_TERMS):
            features.consulting_months += duration

    features.career_ai_evidence_count = sum(
        1
        for record in features.evidence_records
        if record.source_type == "career_description" and record.feature_family in {"vector_search"}
    )
    total_months = max(features.total_career_months, 1.0)
    features.consulting_only = (
        features.consulting_months >= total_months * 0.75 and features.product_company_months < total_months * 0.20
    )
    features.template_repetition = has_template_repetition(candidate)


def collect_market_signals(candidate: dict[str, Any], features: CandidateV2Features) -> None:
    signals = candidate.get("redrob_signals", {})
    salary = signals.get("expected_salary_range_inr_lpa", {}) or {}
    features.market_signals = {
        "recruiter_response_rate": safe_float(signals.get("recruiter_response_rate")),
        "search_appearance_30d": safe_float(signals.get("search_appearance_30d")),
        "saved_by_recruiters_30d": safe_float(signals.get("saved_by_recruiters_30d")),
        "interview_completion_rate": safe_float(signals.get("interview_completion_rate")),
        "profile_views_received_30d": safe_float(signals.get("profile_views_received_30d")),
        "notice_period_days": safe_float(signals.get("notice_period_days")),
        "open_to_work_flag": 1.0 if signals.get("open_to_work_flag") is True else 0.0,
        "verified_email": 1.0 if signals.get("verified_email") is True else 0.0,
        "verified_phone": 1.0 if signals.get("verified_phone") is True else 0.0,
        "expected_salary_min_lpa": safe_float(salary.get("min")),
        "expected_salary_max_lpa": safe_float(salary.get("max")),
    }


def collect_trust_signals(candidate: dict[str, Any], features: CandidateV2Features) -> None:
    forensic = candidate.get("_forensic", {}) or {}
    features.consistency_points = safe_float(forensic.get("raw_suspicion_points"))
    reason_codes = str(forensic.get("reason_codes", "") or "")
    features.consistency_reason_codes = "" if reason_codes.lower() == "nan" else reason_codes
    points = features.consistency_points
    reasons: list[str] = []
    if features.consistency_reason_codes:
        reasons.extend(code.strip() for code in features.consistency_reason_codes.split(";") if code.strip())
    if features.template_repetition:
        points += 8.0
        reasons.append("template_repetition")
    if skills_overstate_career(features):
        points += 6.0
        reasons.append("skills_overstate_career")
    if headline_overstates_career(candidate, features):
        points += 4.0
        reasons.append("headline_overstates_career")
    if salary_inconsistent(features):
        points += 5.0
        reasons.append("salary_min_above_max")
    if current_title_mismatch(candidate, features):
        points += 4.0
        reasons.append("current_title_evidence_mismatch")
    if features.consulting_only:
        points += 2.0
        reasons.append("consulting_only")

    career_text = normalize_text(" ".join(role.get("description", "") for role in candidate.get("career_history", [])))
    title_text = normalize_text(candidate.get("profile", {}).get("current_title", ""))
    direct_career_evidence = (
        features.evidence_counts.get("search_ranking", 0)
        + features.evidence_counts.get("retrieval", 0)
        + features.evidence_counts.get("evaluation", 0)
        + features.evidence_counts.get("recommendation", 0)
    )
    features.keyword_stuffer = features.ai_skill_count >= 5 and direct_career_evidence < 3
    features.ai_transition = (
        features.ai_skill_count >= 2
        and direct_career_evidence == 0
        and not term_hits(title_text, TECHNICAL_TITLE_TERMS)
        and not term_hits(career_text, AI_SKILL_TERMS)
    )
    if features.keyword_stuffer:
        points += 8.0
        reasons.append("keyword_stuffer")
    if features.ai_transition:
        points += 7.0
        reasons.append("ai_transition")

    features.trust_points = points
    features.trust_reason_codes = sorted(set(reasons))


def has_template_repetition(candidate: dict[str, Any]) -> bool:
    normalized = []
    for role in candidate.get("career_history", []):
        desc = normalize_text(role.get("description", ""))
        desc = re.sub(r"\d+", "N", desc)
        desc = re.sub(r"\b[0-9]+m\b", "Nm", desc)
        if desc:
            normalized.append(desc)
    return len(normalized) > len(set(normalized))


def skills_overstate_career(features: CandidateV2Features) -> bool:
    direct_score = (
        features.family_scores.get("search_ranking", 0.0)
        + features.family_scores.get("retrieval", 0.0)
        + features.family_scores.get("evaluation", 0.0)
        + features.family_scores.get("recommendation", 0.0)
    )
    return features.ai_skill_count >= 5 and direct_score < 0.45


def headline_overstates_career(candidate: dict[str, Any], features: CandidateV2Features) -> bool:
    headline = normalize_text(candidate.get("profile", {}).get("headline", ""))
    if not headline:
        return False
    headline_claims = any(term in headline for term in ["search", "ranking", "retrieval", "ai", "llm", "rag", "vector"])
    career_direct = (
        features.evidence_counts.get("search_ranking", 0)
        + features.evidence_counts.get("retrieval", 0)
        + features.evidence_counts.get("evaluation", 0)
    )
    return headline_claims and career_direct == 0


def salary_inconsistent(features: CandidateV2Features) -> bool:
    return (
        features.market_signals.get("expected_salary_min_lpa", 0.0)
        > features.market_signals.get("expected_salary_max_lpa", 0.0)
        > 0.0
    )


def current_title_mismatch(candidate: dict[str, Any], features: CandidateV2Features) -> bool:
    career = candidate.get("career_history", [])
    if not career:
        return False
    current = next((role for role in career if role.get("is_current") is True), career[0])
    title = normalize_text(current.get("title", ""))
    desc = normalize_text(current.get("description", ""))
    if "search" in title and not term_hits(desc, {"search", "ranking", "retrieval", "relevance", "bm25"}):
        return True
    if "recommendation" in title and not term_hits(desc, {"recommendation", "ranking", "matching", "personalization"}):
        return True
    return False


def score_candidate_v2(
    features: CandidateV2Features,
    market_reference: dict[str, float] | None = None,
) -> ScoredCandidateV2:
    market_reference = market_reference or {
        "search_appearance_30d_p95": 500.0,
        "saved_by_recruiters_30d_p95": 35.0,
        "profile_views_received_30d_p95": 180.0,
    }
    behavioral_score = compute_behavioral_score(features, market_reference)
    trust_penalty = bounded(features.trust_points / 100.0, 0.0, 0.12)
    trust_score = 1.0 - bounded(features.trust_points / 35.0)
    calibration_penalty = compute_calibration_penalty(features)

    weighted = (
        FAMILY_WEIGHTS["search_ranking"] * features.family_scores["search_ranking"]
        + FAMILY_WEIGHTS["retrieval"] * features.family_scores["retrieval"]
        + FAMILY_WEIGHTS["evaluation"] * features.family_scores["evaluation"]
        + FAMILY_WEIGHTS["recommendation"] * features.family_scores["recommendation"]
        + FAMILY_WEIGHTS["vector_search"] * features.family_scores["vector_search"]
        + FAMILY_WEIGHTS["behavioral"] * behavioral_score
    )
    # Trust is mostly a cap layer. The small penalty keeps mild concerns visible without dominating relevance.
    final_score = bounded(weighted - trust_penalty - calibration_penalty)
    score_cap = trust_score_cap(features)
    if score_cap is not None:
        final_score = min(final_score, score_cap)

    return ScoredCandidateV2(
        candidate_id=features.candidate_id,
        search_ranking_score=round(features.family_scores["search_ranking"], 6),
        retrieval_score=round(features.family_scores["retrieval"], 6),
        evaluation_score=round(features.family_scores["evaluation"], 6),
        recommendation_score=round(features.family_scores["recommendation"], 6),
        vector_search_score=round(features.family_scores["vector_search"], 6),
        behavioral_score=round(behavioral_score, 6),
        trust_score=round(trust_score, 6),
        trust_penalty=round(trust_penalty, 6),
        final_score=round(final_score, 6),
        score_cap=score_cap,
        calibration_penalty=round(calibration_penalty, 6),
    )


def compute_behavioral_score(features: CandidateV2Features, reference: dict[str, float]) -> float:
    signals = features.market_signals
    search = bounded(signals["search_appearance_30d"] / max(reference.get("search_appearance_30d_p95", 1.0), 1.0))
    saved = bounded(signals["saved_by_recruiters_30d"] / max(reference.get("saved_by_recruiters_30d_p95", 1.0), 1.0))
    views = bounded(signals["profile_views_received_30d"] / max(reference.get("profile_views_received_30d_p95", 1.0), 1.0))
    notice_inverse = 1.0 - bounded(signals["notice_period_days"] / 120.0)
    verification_bonus = 0.02 * signals["open_to_work_flag"] + 0.015 * signals["verified_email"] + 0.015 * signals["verified_phone"]
    return bounded(
        0.24 * bounded(signals["recruiter_response_rate"])
        + 0.18 * search
        + 0.16 * saved
        + 0.18 * bounded(signals["interview_completion_rate"])
        + 0.10 * views
        + 0.14 * notice_inverse
        + verification_bonus
    )


def compute_calibration_penalty(features: CandidateV2Features) -> float:
    penalty = 0.0
    if features.keyword_stuffer:
        penalty += 0.08
    if features.ai_transition:
        penalty += 0.06
    if features.consulting_only:
        penalty += 0.02
    return bounded(penalty, 0.0, 0.14)


def trust_score_cap(features: CandidateV2Features) -> float | None:
    points = features.trust_points
    if features.keyword_stuffer or features.ai_transition:
        return 0.58
    if points >= 30:
        return 0.68
    if points >= 24:
        return 0.75
    if points >= 18:
        return 0.82
    if points >= 12:
        return 0.90
    if features.template_repetition:
        return 0.88 if features.level4_5_count < 3 else 0.92
    return None
