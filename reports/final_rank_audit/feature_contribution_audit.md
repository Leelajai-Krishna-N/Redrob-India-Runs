# Feature Contribution Audit

## Family Score Influence In Top 100

| Feature | Avg Score | Avg Weighted Contribution | Corr With Final | Corr With Better Rank | Top25 Avg | Ranks76-100 Avg |
| --- | --- | --- | --- | --- | --- | --- |
| search ranking | 0.698 | 0.230 | 0.556 | 0.542 | 0.840 | 0.558 |
| retrieval | 0.542 | 0.125 | 0.555 | 0.523 | 0.833 | 0.453 |
| evaluation | 0.707 | 0.127 | 0.413 | 0.415 | 0.866 | 0.544 |
| recommendation | 0.527 | 0.063 | -0.117 | -0.072 | 0.457 | 0.472 |
| vector search | 0.693 | 0.049 | 0.492 | 0.475 | 0.890 | 0.567 |
| market/behavioral | 0.800 | 0.056 | 0.128 | 0.129 | 0.830 | 0.767 |

## Trust And Behavioral Subsignals

| Signal | Average | Role | Corr With Final | Corr With Better Rank |
| --- | --- | --- | --- | --- |
| trust penalty | 0.062 | negative | -0.129 | -0.146 |
| notice period | 59.2 | behavioral sub-signal | -0.230 | -0.233 |
| recruiter response | 0.656 | behavioral sub-signal | -0.024 | -0.032 |

## Findings

1. Search ranking, retrieval, and evaluation are the dominant useful drivers.
2. Behavioral/market signals matter but are correctly tie-breaker-sized.
3. Vector search contributes less than core relevance families, which is appropriate.
4. Recommendation evidence is useful but can become over-weighted when paired with repeated ranking/evaluation templates.
5. Trust penalties matter, but template-family repetition still leaks into high ranks, suggesting trust caps are slightly weak for near-duplicates.
