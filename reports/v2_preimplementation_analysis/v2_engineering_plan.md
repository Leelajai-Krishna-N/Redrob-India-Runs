# V2 Engineering Plan

## 1. Five Highest-Impact V2 Changes

1. Add evidence-traced sub-scores for Search Ranking, Retrieval Infrastructure, Recommendation/Matching, and Evaluation/Relevance Science.
2. Add an evidence-strength layer that distinguishes keyword mention from ownership at scale.
3. Add template-repetition and source-diversity trust checks, with score caps for severe issues.
4. Convert market readiness from a broad score component into a tie-breaker within relevance bands.
5. Generate explanations from stored evidence traces: matched term, source, role, company, snippet, and contribution.

## 2. V1 Components That Should Remain Untouched

- Deterministic scoring architecture.
- No LLM calls, embeddings, cross-encoders, neural models, or external APIs.
- The principle that career evidence beats skills.
- Keyword-stuffer and AI-transition guardrails.
- Component-score output rather than final-score-only output.

## 3. V1 Assumptions Validated

- Career evidence is the strongest available signal.
- Search and retrieval evidence identify many strong candidates.
- Skill keywords alone are unsafe.
- Behavioral availability matters after relevance is established.
- Recommendation-system candidates can be strong fits when the work is ranking/matching/evaluation-oriented.

## 4. V1 Assumptions Disproven Or Weakened

- One technical score is not enough.
- Recommendation evidence should not be treated as equivalent to search ranking evidence.
- Market score should not carry broad influence after technical/career saturation.
- Consistency needs more than existing reason codes; template repetition matters.
- Evaluation evidence deserves explicit scoring, not incidental keyword matching.

## 5. Safest V2 Path

Build a deterministic V2 that keeps V1's architecture but decomposes relevance. Add sub-scores, evidence traces, source caps, and trust caps. Validate changes against the committee gold set before producing any submission-oriented ranking.

## 6. Riskiest V2 Path

Blindly tune weights to maximize agreement with this small gold set, or add complex modeling without fixing evidence taxonomy. That risks overfitting the committee sample while preserving the underlying confusion between recommendation, search, retrieval, vector search, and generic AI.

## 7. If Only One Week Remained

Build the smallest robust V2:

1. Extract role-level evidence traces for search ranking, retrieval, recommendation, evaluation, and vector search.
2. Score evidence strength Levels 1-5.
3. Recompute final score using relevance family sub-scores and skill caps.
4. Add template-repetition and severe consistency caps.
5. Produce top candidates with evidence-backed explanations and compare against the gold set.

This gives the biggest practical lift without introducing risky model complexity.
