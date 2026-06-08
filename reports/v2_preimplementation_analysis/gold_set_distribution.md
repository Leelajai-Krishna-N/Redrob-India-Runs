# Gold Set Distribution Analysis

## Distribution By Gold Label

| Gold Label | Count | final_score | career_score | market_score | consistency_score | years_of_experience | career_retrieval_evidence_count | career_ranking_evidence_count | recommendation_evidence_count | evaluation_evidence_count | consistency_points |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ELITE | 12 | 0.941 | 0.997 | 0.823 | 0.875 | 8.467 | 3.500 | 4.500 | 1.500 | 10.083 | 3.750 |
| STRONG | 39 | 0.922 | 0.981 | 0.824 | 0.923 | 6.526 | 2.949 | 3.231 | 1.872 | 5.692 | 2.308 |
| MEDIUM | 44 | 0.903 | 0.958 | 0.843 | 0.822 | 6.766 | 2.750 | 2.977 | 1.500 | 4.500 | 5.341 |
| WEAK | 5 | 0.920 | 0.970 | 0.848 | 0.860 | 6.600 | 3.200 | 3.200 | 1.600 | 1.400 | 4.200 |

## Do ELITE Candidates Actually Score Higher?

Partially. ELITE candidates have strong V1 scores on average, but the separation is not clean enough for final ordering.

The clearest quality separation comes from role-level evidence strength, evaluation evidence, ownership/scale terms, and committee concerns such as template repetition. `final_score`, `technical_score`, and `career_score` help find a credible Top 100 pool, but they do not fully separate ELITE from STRONG/MEDIUM because V1 blends search, retrieval, recommendation, vector search, market readiness, and consistency into broad components.

## Why The Separation Is Imperfect

- Top-tail `career_score` and `technical_score` are high for many candidates, including MEDIUM profiles.
- Recommendation and generic ML evidence can look similar to search/ranking evidence in V1.
- Evaluation evidence is not a first-class V1 feature despite being highly valued by the committee.
- Template-like repeated role descriptions reduce committee confidence but are only partially represented in V1 consistency features.
- Market score can help availability but does not indicate relevance quality.
