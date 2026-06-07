from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from typing import Any


TECHNICAL_TIERS: dict[str, dict[str, Any]] = {
    "tier_a_ranking": {
        "weight": 5.0,
        "terms": [
            "learning to rank",
            "ltr",
            "search ranking",
            "ranking",
            "ranker",
            "relevance modeling",
            "relevance pipeline",
            "relevance optimization",
            "relevance",
            "reranking",
            "reranker",
        ],
    },
    "tier_b_retrieval": {
        "weight": 4.0,
        "terms": [
            "information retrieval",
            "semantic search",
            "search systems",
            "search infrastructure",
            "elasticsearch",
            "opensearch",
            "bm25",
            "solr",
            "retrieval",
            "indexing",
            "query understanding",
        ],
    },
    "tier_c_vector": {
        "weight": 2.7,
        "terms": [
            "vector search",
            "embeddings",
            "embedding",
            "pinecone",
            "weaviate",
            "qdrant",
            "milvus",
            "faiss",
            "pgvector",
            "ann search",
            "nearest neighbor",
        ],
    },
    "tier_d_llm": {
        "weight": 1.2,
        "terms": [
            "llm",
            "llms",
            "rag",
            "langchain",
            "prompt engineering",
            "prompt",
            "fine-tuning",
            "fine tuning",
            "generative ai",
        ],
    },
}

SOURCE_WEIGHTS = {
    "career_description": 1.0,
    "summary": 0.65,
    "skills": 0.45,
    "headline": 0.35,
    "title": 0.30,
}

SCORE_LAYER_WEIGHTS = {
    "technical": 0.45,
    "career": 0.25,
    "market": 0.20,
    "consistency": 0.10,
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


@dataclass
class EvidenceHit:
    tier: str
    source: str
    term: str
    weight: float


@dataclass
class CandidateFeatures:
    candidate_id: str
    current_title: str
    current_company: str
    years_of_experience: float
    skills: list[str]
    evidence_hits: list[EvidenceHit] = field(default_factory=list)
    career_evidence_hits: list[EvidenceHit] = field(default_factory=list)
    tier_source_scores: dict[str, float] = field(default_factory=dict)
    technical_raw: float = 0.0
    career_relevance_raw: float = 0.0
    relevant_role_count: int = 0
    relevant_duration_months: float = 0.0
    product_company_months: float = 0.0
    consulting_months: float = 0.0
    total_career_months: float = 0.0
    ai_skill_count: int = 0
    skill_count: int = 0
    career_ai_evidence_count: int = 0
    career_ranking_evidence_count: int = 0
    career_retrieval_evidence_count: int = 0
    market_signals: dict[str, float] = field(default_factory=dict)
    consistency_points: float = 0.0
    consistency_reason_codes: str = ""
    keyword_stuffer: bool = False
    ai_transition: bool = False
    consulting_only: bool = False


@dataclass
class ScoredCandidate:
    candidate_id: str
    technical_score: float
    career_score: float
    market_score: float
    consistency_score: float
    consistency_penalty: float
    calibration_penalty: float
    final_score: float
    score_cap: float | None


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).lower()
    text = re.sub(r"[^a-z0-9+#./ -]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_term(text: str, term: str) -> bool:
    term_norm = normalize_text(term)
    if not term_norm:
        return False
    if len(term_norm) <= 3:
        return re.search(rf"\b{re.escape(term_norm)}\b", text) is not None
    return term_norm in text


def term_hits(text: str, terms: list[str] | set[str]) -> list[str]:
    return [term for term in terms if contains_term(text, term)]


def bounded(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def saturating_score(raw: float, scale: float) -> float:
    if raw <= 0:
        return 0.0
    return bounded(1.0 - math.exp(-raw / scale))


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


def extract_candidate_features(candidate: dict[str, Any]) -> CandidateFeatures:
    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})
    salary = signals.get("expected_salary_range_inr_lpa", {}) or {}
    skills = [str(skill.get("name", "")) for skill in candidate.get("skills", [])]
    feature = CandidateFeatures(
        candidate_id=candidate.get("candidate_id", ""),
        current_title=str(profile.get("current_title", "")),
        current_company=str(profile.get("current_company", "")),
        years_of_experience=safe_float(profile.get("years_of_experience")),
        skills=skills,
        skill_count=len(skills),
    )

    sources = {
        "headline": normalize_text(profile.get("headline", "")),
        "summary": normalize_text(profile.get("summary", "")),
        "skills": normalize_text(" ".join(skills)),
        "title": normalize_text(profile.get("current_title", "")),
    }

    for source, text in sources.items():
        collect_evidence(feature, source, text)

    for role in candidate.get("career_history", []):
        desc = normalize_text(role.get("description", ""))
        title = normalize_text(role.get("title", ""))
        role_text = f"{title} {desc}"
        before = len(feature.evidence_hits)
        collect_evidence(feature, "career_description", role_text)
        role_hits = feature.evidence_hits[before:]
        duration = safe_float(role.get("duration_months"))
        feature.total_career_months += duration
        if role_hits:
            feature.relevant_role_count += 1
            feature.relevant_duration_months += duration
            feature.career_evidence_hits.extend(role_hits)
        role_weight = sum(hit.weight for hit in role_hits)
        feature.career_relevance_raw += role_weight * (1.0 + min(duration, 60.0) / 120.0)
        company_text = normalize_text(f"{role.get('company', '')} {role.get('industry', '')} {role.get('description', '')}")
        if term_hits(company_text, PRODUCT_COMPANY_TERMS):
            feature.product_company_months += duration
        if term_hits(company_text, CONSULTING_TERMS):
            feature.consulting_months += duration

    feature.technical_raw = sum(hit.weight for hit in feature.evidence_hits)
    feature.career_ranking_evidence_count = sum(1 for hit in feature.career_evidence_hits if hit.tier == "tier_a_ranking")
    feature.career_retrieval_evidence_count = sum(1 for hit in feature.career_evidence_hits if hit.tier == "tier_b_retrieval")
    feature.career_ai_evidence_count = sum(1 for hit in feature.career_evidence_hits if hit.tier in {"tier_c_vector", "tier_d_llm"})
    feature.ai_skill_count = len(term_hits(normalize_text(" ".join(skills)), AI_SKILL_TERMS))

    total_months = max(feature.total_career_months, 1.0)
    feature.consulting_only = feature.consulting_months >= total_months * 0.75 and feature.product_company_months < total_months * 0.20
    feature.keyword_stuffer = feature.ai_skill_count >= 5 and feature.career_relevance_raw < 3.0
    career_text = normalize_text(" ".join(role.get("description", "") for role in candidate.get("career_history", [])))
    title_text = normalize_text(profile.get("current_title", ""))
    feature.ai_transition = (
        feature.ai_skill_count >= 2
        and feature.career_ai_evidence_count == 0
        and not term_hits(title_text, TECHNICAL_TITLE_TERMS)
        and not term_hits(career_text, AI_SKILL_TERMS)
    )

    feature.market_signals = {
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
    forensic = candidate.get("_forensic", {}) or {}
    feature.consistency_points = safe_float(forensic.get("raw_suspicion_points"))
    feature.consistency_reason_codes = str(forensic.get("reason_codes", "") or "")
    return feature


def collect_evidence(feature: CandidateFeatures, source: str, text: str) -> None:
    source_weight = SOURCE_WEIGHTS[source]
    for tier, config in TECHNICAL_TIERS.items():
        for term in term_hits(text, config["terms"]):
            weight = config["weight"] * source_weight
            hit = EvidenceHit(tier=tier, source=source, term=term, weight=weight)
            feature.evidence_hits.append(hit)
            key = f"{tier}:{source}"
            feature.tier_source_scores[key] = feature.tier_source_scores.get(key, 0.0) + weight


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
    reference = {}
    for key, nums in values.items():
        arr = sorted(nums)
        reference[f"{key}_p95"] = float(np_percentile(arr, 95)) if arr else 1.0
    return reference


def np_percentile(values: list[float], percentile: float) -> float:
    if not values:
        return 0.0
    index = (len(values) - 1) * percentile / 100.0
    low = math.floor(index)
    high = math.ceil(index)
    if low == high:
        return values[int(index)]
    return values[low] * (high - index) + values[high] * (index - low)


def score_candidate(feature: CandidateFeatures, market_reference: dict[str, float] | None = None) -> ScoredCandidate:
    market_reference = market_reference or {
        "search_appearance_30d_p95": 500.0,
        "saved_by_recruiters_30d_p95": 35.0,
        "profile_views_received_30d_p95": 180.0,
    }
    technical_score = saturating_score(feature.technical_raw, 18.0)
    career_score = compute_career_score(feature)
    market_score = compute_market_score(feature, market_reference)
    consistency_penalty = bounded(feature.consistency_points / 30.0)
    consistency_score = 1.0 - consistency_penalty
    calibration_penalty = compute_calibration_penalty(feature)
    weighted = (
        SCORE_LAYER_WEIGHTS["technical"] * technical_score
        + SCORE_LAYER_WEIGHTS["career"] * career_score
        + SCORE_LAYER_WEIGHTS["market"] * market_score
        + SCORE_LAYER_WEIGHTS["consistency"] * consistency_score
    )
    final_score = bounded(weighted - calibration_penalty)
    score_cap = consistency_score_cap(feature.consistency_points)
    if score_cap is not None:
        final_score = min(final_score, score_cap)
    return ScoredCandidate(
        candidate_id=feature.candidate_id,
        technical_score=round(technical_score, 6),
        career_score=round(career_score, 6),
        market_score=round(market_score, 6),
        consistency_score=round(consistency_score, 6),
        consistency_penalty=round(consistency_penalty, 6),
        calibration_penalty=round(calibration_penalty, 6),
        final_score=round(final_score, 6),
        score_cap=score_cap,
    )


def compute_career_score(feature: CandidateFeatures) -> float:
    role_component = bounded(feature.relevant_role_count / 3.0)
    duration_component = bounded(feature.relevant_duration_months / 72.0)
    relevance_component = saturating_score(feature.career_relevance_raw, 14.0)
    ranking_bonus = bounded(feature.career_ranking_evidence_count / 3.0) * 0.15
    retrieval_bonus = bounded(feature.career_retrieval_evidence_count / 4.0) * 0.08
    product_bonus = bounded(feature.product_company_months / 60.0) * 0.10
    consulting_penalty = 0.05 if feature.consulting_only else 0.0
    return bounded(
        0.30 * role_component
        + 0.25 * duration_component
        + 0.30 * relevance_component
        + ranking_bonus
        + retrieval_bonus
        + product_bonus
        - consulting_penalty
    )


def compute_market_score(feature: CandidateFeatures, reference: dict[str, float]) -> float:
    signals = feature.market_signals
    search = bounded(signals["search_appearance_30d"] / max(reference.get("search_appearance_30d_p95", 1.0), 1.0))
    saved = bounded(signals["saved_by_recruiters_30d"] / max(reference.get("saved_by_recruiters_30d_p95", 1.0), 1.0))
    views = bounded(signals["profile_views_received_30d"] / max(reference.get("profile_views_received_30d_p95", 1.0), 1.0))
    notice_inverse = 1.0 - bounded(signals["notice_period_days"] / 120.0)
    verification_bonus = 0.02 * signals["open_to_work_flag"] + 0.015 * signals["verified_email"] + 0.015 * signals["verified_phone"]
    return bounded(
        0.24 * bounded(signals["recruiter_response_rate"])
        + 0.20 * search
        + 0.18 * saved
        + 0.18 * bounded(signals["interview_completion_rate"])
        + 0.12 * views
        + 0.08 * notice_inverse
        + verification_bonus
    )


def compute_calibration_penalty(feature: CandidateFeatures) -> float:
    penalty = 0.0
    if feature.keyword_stuffer:
        penalty += 0.12
    if feature.ai_transition:
        penalty += 0.06
    if feature.consulting_only:
        penalty += 0.025
    return round(penalty, 6)


def consistency_score_cap(points: float) -> float | None:
    if points >= 30:
        return 0.72
    if points >= 24:
        return 0.78
    if points >= 18:
        return 0.84
    return None
