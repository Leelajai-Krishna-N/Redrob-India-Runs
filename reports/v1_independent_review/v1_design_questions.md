# V1 Design Questions

## Q1. Are we ranking Retrieval Engineers, Ranking Engineers, Recommendation Engineers, or Search Engineers?

**Current V1 behavior:** V1 ranks a blended pool of search/relevance/retrieval/recommendation/ML candidates. The Top 100 contains strong retrieval and ranking career evidence, but the most common title is `Recommendation Systems Engineer`.

**Evidence:** Top 100 mean career ranking evidence count is 3.27; mean career retrieval evidence count is 2.94. Top titles include Recommendation Systems Engineer, Search Engineer, Senior Data Scientist, Machine Learning Engineer, Applied ML Engineer, and NLP Engineer.

**Recommendation:** V2 should explicitly model sub-intents: search ranking/relevance, retrieval infrastructure, recommendation ranking, vector search, and generic AI/ML. Then choose weights based on the JD.

**Confidence:** High.

## Q2. How much should experience matter?

**Current V1 behavior:** Experience matters mainly through relevant role count and relevant duration, not raw years. This is directionally right.

**Evidence:** Top 100 mean experience is 6.87 years and median is 6.65. High experience alone does not dominate.

**Recommendation:** Keep raw years secondary. Reward duration of directly relevant search/relevance work, but avoid letting generic long careers dominate.

**Confidence:** High.

## Q3. Should evidence count matter, or evidence strength matter?

**Current V1 behavior:** Both matter, but repeated evidence can saturate technical/career scores. Count can overwhelm nuance.

**Evidence:** Career score reaches 1.0 for 64 candidates; top candidates often have repeated ranking/retrieval terms and saturated career scores.

**Recommendation:** V2 should prefer evidence strength and source diversity over raw repetition: unique relevant projects, ownership verbs, metrics/evaluation terms, and role recency should matter more than repeated keywords.

**Confidence:** High.

## Q4. How should recommendation-system experience be treated?

**Current V1 behavior:** Recommendation candidates are rewarded heavily when they contain ranking/retrieval language.

**Evidence:** `Recommendation Systems Engineer` is the most common Top 100 title.

**Recommendation:** Treat recommendation systems as adjacent-positive, not identical. Strong recommender ranking/evaluation experience should score highly; generic personalization/recommender skills should score below direct search relevance/ranking ownership.

**Confidence:** Medium-high.

## Q5. How aggressive should suspicious-profile penalties be?

**Current V1 behavior:** Severe penalties cap scores but only for candidates covered by forensic outputs. Missing coverage is treated as clean.

**Evidence:** 84239 candidates have `consistency_score == 1`; only 16654 were in the forensic consistency score file.

**Recommendation:** Be more aggressive on high-confidence impossible conditions, but avoid harsh penalties for taxonomy-only mismatch. Most importantly, run lightweight consistency checks for everyone.

**Confidence:** High.

## Q6. Should market readiness influence ranking?

**Current V1 behavior:** Market readiness is 20% of final score and has broad variance.

**Evidence:** `market_score` median is 0.461; p95 is 0.705. Top candidates often have high market scores.

**Recommendation:** Keep market readiness, but reduce its ability to outrank much stronger relevance evidence. Use it as a tie-breaker within relevance bands.

**Confidence:** Medium-high.

## Q7. Are we rewarding keyword repetition?

**Current V1 behavior:** Some repetition reward exists because technical score sums hits before applying a saturating transform.

**Evidence:** Top 100 has strong term repetition, and technical_score p95 (0.457) is far above the median (0.042). However, career descriptions are weighted most, so skill-only stuffing is not winning Top 100.

**Recommendation:** Cap repeated terms per source/tier and reward source diversity. Count `ranking` once per role unless distinct project evidence appears.

**Confidence:** Medium.

## Q8. Should breadth of skills or depth of relevance dominate?

**Current V1 behavior:** Depth mostly dominates in Top 100 because career evidence has the highest source weight, but broad skill bundles still help technical_score.

**Evidence:** Top 100 keyword stuffer count is 0, but top skills include many broad AI/LLM/vector terms.

**Recommendation:** Depth of relevance should dominate. Breadth should add small confidence only after direct search/relevance evidence is present.

**Confidence:** High.
