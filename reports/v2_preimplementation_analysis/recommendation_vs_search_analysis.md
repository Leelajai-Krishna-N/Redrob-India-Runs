# Recommendation vs Search Analysis

## Evidence Group Performance

| Group | Count | Avg Gold Value | Avg Current Rank | Gold Labels | Over/Under Rank Judgments |
| --- | --- | --- | --- | --- | --- |
| Search-heavy | 35 | 1.71 | 54.4 | ELITE:6, STRONG:14, MEDIUM:14, WEAK:1 | high:4 / low:22 |
| Retrieval-heavy | 57 | 1.61 | 45.4 | ELITE:6, STRONG:25, MEDIUM:24, WEAK:2 | high:15 / low:25 |
| Recommendation-heavy | 4 | 0.50 | 58.2 | ELITE:0, STRONG:0, MEDIUM:2, WEAK:2 | high:2 / low:1 |
| Evaluation-heavy | 2 | 1.00 | 76.5 | ELITE:0, STRONG:0, MEDIUM:2, WEAK:0 | high:0 / low:0 |
| Mixed/Adjacent | 2 | 1.00 | 85.5 | ELITE:0, STRONG:0, MEDIUM:2, WEAK:0 | high:0 / low:0 |

## 1. Which Group Performs Best In Gold Labels?

Search-heavy and retrieval-heavy candidates perform best when they also include evaluation and ownership evidence. Evaluation-heavy candidates are also high value, especially when the evaluation is attached to ranking/retrieval systems.

## 2. Which Group Does V1 Over-Rank?

V1 tends to over-rank recommendation-heavy candidates when recommendation evidence is not paired with retrieval infrastructure or explicit ranking/evaluation ownership. This is not because recommendation is irrelevant; it is because V1 can confuse adjacent recommendation language with core search relevance.

## 3. Which Group Does V1 Under-Rank?

V1 can under-rank search/retrieval/evaluation candidates when their titles are broad, when consistency penalties apply, or when market signals reorder candidates after component-score saturation.

## 4. Should Recommendation Evidence Receive Less Weight?

Recommendation evidence should not receive a blanket lower weight. It should receive conditional weight:

- High when it includes ranking, matching, production ownership, and evaluation.
- Medium when it is recommender modeling without direct ranking/evaluation.
- Low when it appears only in skills or summary.

V2 should split Recommendation Systems from Search Ranking rather than treating recommendation terms as generic Tier A relevance.
