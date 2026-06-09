from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Iterable


FEATURE_FAMILIES: dict[str, dict[str, Any]] = {
    "search_ranking": {
        "base_weight": 5.0,
        "terms": [
            "learning to rank",
            "learning-to-rank",
            "ltr",
            "ranking pipeline",
            "ranking layer",
            "ranking model",
            "ranking system",
            "ranking infrastructure",
            "search ranking",
            "candidate ranking",
            "ranker",
            "reranker",
            "reranking",
            "re-ranking",
            "re-scoring",
            "relevance",
            "search relevance",
            "query relevance",
            "search quality",
            "candidate-jd matching",
            "matching pipeline",
        ],
    },
    "retrieval": {
        "base_weight": 4.2,
        "terms": [
            "retrieval",
            "semantic search",
            "hybrid retrieval",
            "dense retrieval",
            "bm25",
            "elasticsearch",
            "opensearch",
            "indexing",
            "index refresh",
            "index versioning",
            "retrieval pipeline",
            "query understanding",
            "candidate retrieval",
            "vector retrieval",
            "search infrastructure",
            "embedding-based search",
            "keyword-based search",
            "keyword search",
            "inverted index",
        ],
    },
    "evaluation": {
        "base_weight": 4.6,
        "terms": [
            "ndcg",
            "mrr",
            "recall@k",
            "recall at k",
            "precision",
            "map",
            "offline evaluation",
            "online evaluation",
            "evaluation framework",
            "eval framework",
            "a/b testing",
            "ab testing",
            "simulated a/b",
            "human judgments",
            "relevance labeling",
            "search metrics",
            "recruiter-feedback loop",
            "ranking feedback loop",
            "search feedback loop",
            "relevance feedback loop",
            "offline benchmark",
            "online metrics",
            "training/eval",
        ],
    },
    "recommendation": {
        "base_weight": 3.0,
        "terms": [
            "recommendation systems",
            "recommendation system",
            "recommendations",
            "recommender",
            "personalization",
            "candidate matching",
            "feed ranking",
            "collaborative filtering",
            "user-item",
            "matching",
        ],
    },
    "vector_search": {
        "base_weight": 2.2,
        "terms": [
            "embeddings",
            "embedding",
            "vector search",
            "faiss",
            "milvus",
            "pinecone",
            "weaviate",
            "qdrant",
            "pgvector",
            "sentence transformers",
            "sentence-transformers",
            "bge",
            "hnsw",
            "ann search",
        ],
    },
}

SOURCE_WEIGHTS = {
    "career_description": 1.0,
    "summary": 0.52,
    "skill": 0.28,
    "headline": 0.22,
}

OWNERSHIP_TERMS = [
    "owned",
    "led",
    "architected",
    "designed",
    "built end-to-end",
    "built",
    "launched",
    "rolled out",
    "rollout",
    "created",
    "deployed",
    "shipped",
    "rebuilt",
    "drove",
    "operated",
    "migrated",
    "migration",
]

IMPLEMENTATION_TERMS = [
    "implemented",
    "built",
    "designed",
    "deployed",
    "created",
    "integrated",
    "migrated",
    "optimized",
]

SCALE_TERMS = [
    "production",
    "10m",
    "30m",
    "35m",
    "50m",
    "100m",
    "million",
    "queries/day",
    "queries per day",
    "queries per month",
    "users",
    "serving",
    "traffic",
    "large-scale",
    "qps",
    "p95",
    "latency",
    "engagement",
    "revenue-per-search",
    "time-to-shortlist",
]

RETRIEVAL_CONTEXT_TERMS = set(FEATURE_FAMILIES["retrieval"]["terms"])
SEARCH_CONTEXT_TERMS = set(FEATURE_FAMILIES["search_ranking"]["terms"])
EVALUATION_CONTEXT_TERMS = set(FEATURE_FAMILIES["evaluation"]["terms"])
_NORMALIZED_TERM_CACHE: dict[str, str] = {}
_TERM_REGEX_CACHE: dict[str, re.Pattern[str]] = {}


@dataclass(frozen=True)
class EvidenceRecord:
    candidate_id: str
    feature_family: str
    matched_term: str
    source_type: str
    source_location: str
    company: str
    role_title: str
    snippet: str
    evidence_level: int
    contribution: float


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9+#@./ -]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def contains_term(text: str, term: str) -> bool:
    term_norm = normalized_term(term)
    if not term_norm:
        return False
    if len(term_norm) <= 4 or term_norm in {"ltr", "mrr", "map"}:
        pattern = _TERM_REGEX_CACHE.get(term_norm)
        if pattern is None:
            pattern = re.compile(rf"\b{re.escape(term_norm)}\b")
            _TERM_REGEX_CACHE[term_norm] = pattern
        return pattern.search(text) is not None
    return term_norm in text


def term_hits(text: str, terms: Iterable[str]) -> list[str]:
    return [term for term in terms if contains_term(text, term)]


def normalized_term(term: str) -> str:
    cached = _NORMALIZED_TERM_CACHE.get(term)
    if cached is None:
        cached = normalize_text(term)
        _NORMALIZED_TERM_CACHE[term] = cached
    return cached


def sentence_for_term(text: str, term: str) -> str:
    original = re.sub(r"\s+", " ", str(text or "")).strip()
    if not original:
        return ""
    for sentence in re.split(r"(?<=[.!?])\s+", original):
        if contains_term(normalize_text(sentence), term):
            return trim_snippet(sentence)
    index = normalize_text(original).find(normalize_text(term))
    if index < 0:
        return trim_snippet(original)
    start = max(0, index - 120)
    end = min(len(original), index + 180)
    return trim_snippet(original[start:end])


def trim_snippet(text: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    text = text.encode("ascii", "ignore").decode("ascii")
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def evidence_level(source_type: str, text: str, family: str) -> int:
    norm = normalize_text(text)
    has_ownership = bool(term_hits(norm, OWNERSHIP_TERMS))
    has_implementation = bool(term_hits(norm, IMPLEMENTATION_TERMS))
    has_scale = bool(term_hits(norm, SCALE_TERMS))
    has_family_context = bool(
        term_hits(norm, SEARCH_CONTEXT_TERMS | RETRIEVAL_CONTEXT_TERMS | EVALUATION_CONTEXT_TERMS)
    )

    if source_type != "career_description":
        if has_ownership and has_family_context:
            return 3
        return 1

    if has_ownership and has_scale:
        return 5
    if has_ownership:
        return 4
    if has_implementation:
        return 3
    if has_family_context:
        return 2
    return 1


def family_context_multiplier(family: str, source_text: str, source_type: str) -> float:
    norm = normalize_text(source_text)
    if family == "recommendation":
        has_support = bool(
            term_hits(norm, SEARCH_CONTEXT_TERMS | RETRIEVAL_CONTEXT_TERMS | EVALUATION_CONTEXT_TERMS)
        )
        if source_type == "skill":
            return 0.35 if not has_support else 0.70
        return 1.0 if has_support else 0.55
    if family == "vector_search":
        has_retrieval = bool(term_hits(norm, RETRIEVAL_CONTEXT_TERMS))
        has_production = bool(term_hits(norm, SCALE_TERMS))
        if source_type == "skill":
            return 0.30 if not has_retrieval else 0.65
        return 1.0 if has_retrieval or has_production else 0.55
    return 1.0


def evidence_contribution(family: str, source_type: str, level: int, source_text: str) -> float:
    family_weight = float(FEATURE_FAMILIES[family]["base_weight"])
    source_weight = SOURCE_WEIGHTS[source_type]
    level_weight = {1: 0.45, 2: 0.70, 3: 1.0, 4: 1.35, 5: 1.70}[level]
    return round(
        family_weight * source_weight * level_weight * family_context_multiplier(family, source_text, source_type),
        6,
    )


def trace_candidate_evidence(candidate: dict[str, Any]) -> list[EvidenceRecord]:
    candidate_id = str(candidate.get("candidate_id", ""))
    profile = candidate.get("profile", {})
    records: list[EvidenceRecord] = []

    sources: list[dict[str, Any]] = [
        {
            "source_type": "headline",
            "source_location": "profile.headline",
            "text": str(profile.get("headline", "")),
            "company": str(profile.get("current_company", "")),
            "role_title": str(profile.get("current_title", "")),
        },
        {
            "source_type": "summary",
            "source_location": "profile.summary",
            "text": str(profile.get("summary", "")),
            "company": str(profile.get("current_company", "")),
            "role_title": str(profile.get("current_title", "")),
        },
    ]
    for idx, skill in enumerate(candidate.get("skills", [])):
        sources.append(
            {
                "source_type": "skill",
                "source_location": f"skills[{idx}]",
                "text": str(skill.get("name", "")),
                "company": str(profile.get("current_company", "")),
                "role_title": str(profile.get("current_title", "")),
            }
        )
    for idx, role in enumerate(candidate.get("career_history", [])):
        sources.append(
            {
                "source_type": "career_description",
                "source_location": f"career_history[{idx}].description",
                "text": f"{role.get('title', '')}. {role.get('description', '')}",
                "company": str(role.get("company", "")),
                "role_title": str(role.get("title", "")),
            }
        )

    seen: set[tuple[str, str, str]] = set()
    for source in sources:
        source_type = str(source["source_type"])
        source_text = str(source["text"])
        norm = normalize_text(source_text)
        if not norm:
            continue
        for family, config in FEATURE_FAMILIES.items():
            for term in term_hits(norm, config["terms"]):
                key = (family, term, str(source["source_location"]))
                if key in seen:
                    continue
                seen.add(key)
                level = evidence_level(source_type, source_text, family)
                contribution = evidence_contribution(family, source_type, level, source_text)
                records.append(
                    EvidenceRecord(
                        candidate_id=candidate_id,
                        feature_family=family,
                        matched_term=term,
                        source_type=source_type,
                        source_location=str(source["source_location"]),
                        company=str(source["company"]),
                        role_title=str(source["role_title"]),
                        snippet=sentence_for_term(source_text, term),
                        evidence_level=level,
                        contribution=contribution,
                    )
                )
    return records
