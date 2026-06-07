from __future__ import annotations

from collections import Counter

from src.ranker.feature_engineering import CandidateFeatures, EvidenceHit, ScoredCandidate


def generate_reasoning(features: CandidateFeatures, scored: ScoredCandidate, max_items: int = 3) -> str:
    positives = positive_factors(features, scored, max_items=max_items)
    concerns = concern_factors(features, scored, max_items=max_items)
    parts = []
    if positives:
        parts.append("Positives: " + "; ".join(positives))
    if concerns:
        parts.append("Concerns: " + "; ".join(concerns))
    if not parts:
        return "No strong ranking evidence detected."
    return " | ".join(parts)


def positive_factors(features: CandidateFeatures, scored: ScoredCandidate, max_items: int = 3) -> list[str]:
    factors: list[str] = []
    career_terms = top_terms(features.career_evidence_hits)
    all_terms = top_terms(features.evidence_hits)
    if features.career_ranking_evidence_count:
        terms = matching_terms(career_terms, {"ranking", "learning to rank", "ltr", "relevance", "ranker", "reranker"})
        factors.append(f"career evidence for ranking/relevance systems ({', '.join(terms[:2])})" if terms else "career evidence for ranking/relevance systems")
    if features.career_retrieval_evidence_count:
        terms = matching_terms(career_terms, {"retrieval", "semantic search", "search infrastructure", "elasticsearch", "opensearch", "bm25"})
        factors.append(f"career evidence for retrieval/search systems ({', '.join(terms[:2])})" if terms else "career evidence for retrieval/search systems")
    if not factors and any(term in all_terms for term in ["embedding", "embeddings", "vector search", "faiss", "milvus", "qdrant", "pinecone"]):
        terms = matching_terms(all_terms, {"embedding", "embeddings", "vector search", "faiss", "milvus", "qdrant", "pinecone"})
        factors.append(f"detected vector-search evidence ({', '.join(terms[:2])})")
    if features.relevant_role_count >= 2:
        factors.append(f"{features.relevant_role_count} relevant roles with {int(features.relevant_duration_months)} months of supporting experience")
    if features.product_company_months >= 24:
        factors.append("product/SaaS company experience")
    if scored.market_score >= 0.70:
        factors.append("strong recruiter engagement and availability signals")
    elif scored.market_score >= 0.55:
        factors.append("solid market engagement signals")
    return factors[:max_items]


def concern_factors(features: CandidateFeatures, scored: ScoredCandidate, max_items: int = 3) -> list[str]:
    concerns: list[str] = []
    if features.career_ranking_evidence_count == 0:
        concerns.append("limited ranking/relevance career evidence")
    if features.keyword_stuffer:
        concerns.append("many AI skills but little supporting career evidence")
    if features.ai_transition:
        concerns.append("AI-transition pattern without meaningful AI work history")
    if features.market_signals.get("notice_period_days", 0) >= 75:
        concerns.append(f"longer notice period ({int(features.market_signals['notice_period_days'])} days)")
    if features.consistency_points >= 18:
        concerns.append("severe profile consistency concerns")
    elif features.consistency_points >= 8:
        concerns.append("profile consistency concerns")
    if features.consulting_only:
        concerns.append("consulting-heavy career path")
    return concerns[:max_items]


def top_terms(hits: list[EvidenceHit]) -> list[str]:
    counts = Counter(hit.term for hit in hits)
    return [term for term, _ in counts.most_common(12)]


def matching_terms(terms: list[str], wanted: set[str]) -> list[str]:
    return [term for term in terms if term in wanted]
