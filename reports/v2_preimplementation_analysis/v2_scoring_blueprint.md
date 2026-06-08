# V2 Scoring Blueprint

## Recommended Feature Families

| Feature Family | Purpose | Expected Contribution | Confidence | Rationale |
| --- | --- | --- | --- | --- |
| Search Ranking | Identify ranking/relevance ownership. | 30-35% | HIGH | Strongest direct match to JD and committee gold labels. |
| Retrieval Infrastructure | Identify hybrid/BM25/index/search infrastructure ownership. | 20-25% | HIGH | Core to current BM25/rule-based baseline and V2 ranker work. |
| Evaluation/Relevance Science | Reward NDCG/MRR/Recall/A-B/eval framework ownership. | 15-20% | HIGH | Committee repeatedly used evaluation as quality differentiator. |
| Recommendation/Matching | Reward recommender or matching systems only when production ranking/evaluation exists. | 10-15% | MEDIUM-HIGH | Valuable but currently confused with search ranking. |
| Vector Search/Embeddings | Reward vector retrieval operations, not vector DB skill stuffing. | 5-10% | MEDIUM | Useful only when tied to production retrieval/evaluation. |
| Behavioral Signals | Availability and recruiter engagement tie-breaker. | 5-10% | MEDIUM | Relevant for hiring, not core technical quality. |
| Consistency/Trust | Penalties and caps for contradictions, template repetition, honeypots. | Cap/penalty | HIGH | Committee heavily discounted repeated/template-like evidence. |
| Generic AI/ML Support | General ML competence support. | Low support | MEDIUM | Useful foundation but not target relevance. |

## Scoring Philosophy

V2 should not simply tune V1 weights. It should separate candidate relevance into families and require role-level evidence for high scores. The final score can remain deterministic, but it should be explainable as a combination of search ranking, retrieval, evaluation, recommendation/matching, behavioral availability, and consistency/trust.

## Calibration Guidance

- Require Level 4 or Level 5 evidence for ELITE-level ranks.
- Cap skill-only contributions.
- Make market readiness a tie-breaker within relevance bands.
- Apply consistency caps for severe contradictions and template repetition.
- Treat recommendation evidence as high value only with ranking/matching/evaluation evidence.
