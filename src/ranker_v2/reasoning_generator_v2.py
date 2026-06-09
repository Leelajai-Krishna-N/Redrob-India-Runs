from __future__ import annotations

from collections import defaultdict

from src.ranker_v2.evidence_tracing import EvidenceRecord
from src.ranker_v2.feature_extraction_v2 import CandidateV2Features, ScoredCandidateV2


FAMILY_LABELS = {
    "search_ranking": "Search ranking",
    "retrieval": "Retrieval",
    "evaluation": "Evaluation",
    "recommendation": "Recommendation/matching",
    "vector_search": "Vector search",
}


def generate_reasoning_v2(
    features: CandidateV2Features,
    scored: ScoredCandidateV2,
    max_positive_families: int = 4,
) -> str:
    positives = positive_evidence(features, max_positive_families=max_positive_families)
    concerns = concern_factors(features, scored)
    parts: list[str] = []
    if positives:
        parts.append("Evidence: " + " | ".join(positives))
    if concerns:
        parts.append("Concerns: " + "; ".join(concerns))
    if not parts:
        return "No strong stored evidence detected."
    return " ".join(parts)


def positive_evidence(features: CandidateV2Features, max_positive_families: int = 4) -> list[str]:
    records_by_family: dict[str, list[EvidenceRecord]] = defaultdict(list)
    for record in features.evidence_records:
        if record.feature_family in FAMILY_LABELS:
            records_by_family[record.feature_family].append(record)

    family_order = sorted(
        records_by_family,
        key=lambda family: (
            -features.family_scores.get(family, 0.0),
            -max(record.evidence_level for record in records_by_family[family]),
        ),
    )
    positives: list[str] = []
    for family in family_order[:max_positive_families]:
        top = top_record(records_by_family[family])
        if top is None:
            continue
        positives.append(
            f"{FAMILY_LABELS[family]} L{top.evidence_level} via `{top.matched_term}` "
            f"at {safe_place(top)}: {top.snippet}"
        )
    return positives


def top_record(records: list[EvidenceRecord]) -> EvidenceRecord | None:
    if not records:
        return None
    return sorted(
        records,
        key=lambda record: (
            -record.evidence_level,
            -record.contribution,
            source_priority(record.source_type),
            record.source_location,
        ),
    )[0]


def source_priority(source_type: str) -> int:
    return {
        "career_description": 0,
        "summary": 1,
        "skill": 2,
        "headline": 3,
    }.get(source_type, 9)


def safe_place(record: EvidenceRecord) -> str:
    company = record.company or "profile"
    title = record.role_title or record.source_type
    return f"{company} / {title}"


def concern_factors(features: CandidateV2Features, scored: ScoredCandidateV2) -> list[str]:
    concerns: list[str] = []
    if features.family_scores.get("search_ranking", 0.0) < 0.18:
        concerns.append("limited stored search-ranking evidence")
    if features.family_scores.get("retrieval", 0.0) < 0.18:
        concerns.append("limited stored retrieval-infrastructure evidence")
    if features.family_scores.get("evaluation", 0.0) < 0.18:
        concerns.append("limited stored evaluation/relevance evidence")
    if features.template_repetition:
        concerns.append("template-like repeated career descriptions")
    if features.keyword_stuffer:
        concerns.append("many AI skills without enough role-level support")
    if features.ai_transition:
        concerns.append("AI-transition pattern without role-level evidence")
    if features.market_signals.get("notice_period_days", 0.0) >= 90:
        concerns.append(f"long notice period ({int(features.market_signals['notice_period_days'])} days)")
    if features.trust_reason_codes:
        first_codes = ", ".join(features.trust_reason_codes[:3])
        concerns.append(f"trust flags: {first_codes}")
    if scored.score_cap is not None:
        concerns.append(f"score capped at {scored.score_cap:.2f}")
    return concerns[:5]

