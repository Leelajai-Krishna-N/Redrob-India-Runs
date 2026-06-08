# Executive Summary

## Scope

This analysis joins Ranker V1 outputs with the committee-generated gold set and underlying candidate profiles. Gold labels are treated as pseudo-ground-truth: ELITE, STRONG, MEDIUM, WEAK.

## Key Facts

| Item | Value |
| --- | --- |
| Committee gold rows | 100 |
| ELITE | 12 |
| STRONG | 39 |
| MEDIUM | 44 |
| WEAK | 5 |
| Best validated signal | role-level ownership plus evaluation/search/retrieval evidence |
| Most misleading signal | blended technical relevance without evidence family separation |

## What V1 Gets Right

- It selects a credible Top 100 pool.
- It correctly prioritizes career evidence over skill keywords.
- It filters obvious AI-transition candidates and keyword stuffers from the reviewed Top 100.
- Its ranking/retrieval evidence features are directionally useful.

## What V1 Gets Wrong

- It blends different relevance families into one broad technical score.
- It does not make evaluation/relevance science explicit enough.
- It can over-promote recommendation-heavy or generic ML candidates when they contain ranking-adjacent terms.
- It under-represents template repetition and evidence trust in scoring.
- Market score can influence ordering more than a hiring committee would prefer.

## Strongest Lesson From The Gold Set

The committee is not asking whether a profile mentions search. It is asking whether the candidate owned search, ranking, retrieval, matching, or evaluation systems in production.

V2 should promote Level 4-5 evidence and demote Level 1-2 evidence.

## Recommended V2 Direction

Keep V1 deterministic and explainable. Replace blended relevance with evidence-traced feature families:

- Search Ranking.
- Retrieval Infrastructure.
- Evaluation/Relevance Science.
- Recommendation/Matching.
- Vector Search/Embeddings.
- Behavioral Availability.
- Consistency/Trust.

The safest path is a transparent V2 ranker that scores what the hiring committee actually valued: ownership, scale, evaluation, and trustworthy role-level evidence.
