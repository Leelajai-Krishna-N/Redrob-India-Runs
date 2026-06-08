# Ranker V1 Hiring Committee Report

## Method

The committee reviewed all 100 candidates in `outputs/ranker_v1/top_100_candidates.csv` against the underlying JSON profiles. Current rank was ignored when assigning family, interview decision, confidence, and suggested rank band. Current rank was considered only afterward for the Ranker Judgment field.

Committee lenses represented:

- Search Relevance Engineer
- Ranking Systems Engineer
- Applied ML Lead
- Recruiting Manager

## 1. Is Ranker V1 Selecting The Right People?

Mostly yes. The committee labeled 51 candidates YES, 44 MAYBE, and 5 NO out of the Top 100.

The Top 100 contains substantial role-level evidence for ranking, retrieval, recommendation, and evaluation. V1's core assumption that career evidence is more trustworthy than skill keywords is validated by the committee review.

## 2. Is Ranker V1 Ordering Them Correctly?

Partially. Ranker judgments across all 100:

| Judgment | Count |
| --- | --- |
| Slightly Low | 36 |
| Correct | 31 |
| Slightly High | 13 |
| Much Too Low | 12 |
| Much Too High | 8 |

V1 finds many of the right people, but the ordering is imperfect. It sometimes ranks candidates too high when role descriptions are repeated/template-like or when recommendation/generic ML evidence substitutes for direct retrieval/evaluation depth. It sometimes ranks candidates too low when strong search/relevance evidence is present but consistency penalties or title ambiguity reduce rank.

## 3. What Candidate Types Dominate The Top 20?

Search Ranking Engineer (11), Retrieval Engineer (6), Evaluation/Relevance Engineer (1), Applied ML Engineer (1), Recommendation Engineer (1).

## 4. What Candidate Types SHOULD Dominate The Top 20?

Based on suggested Top 10 and Top 25 bands, the committee thinks the dominant interview-first families should be:

Search Ranking Engineer (22), Evaluation/Relevance Engineer (2), Retrieval Engineer (2), Recommendation Engineer (2), NLP Engineer (1).

These are the profiles with strongest role-level evidence for production ranking, retrieval, evaluation, recommendation/matching, and search-quality ownership.

## 5. What Candidate Types Are Over-Ranked?

Over-ranked families among the top downward corrections:

Search Ranking Engineer (6), Retrieval Engineer (5), Recommendation Engineer (4), Applied ML Engineer (2), Other (1), Generic ML Engineer (1), NLP Engineer (1)

The common pattern is not obvious keyword stuffing. It is weaker direct retrieval/evaluation evidence, repeated role descriptions, or adjacent recommendation/generic ML evidence being treated as core search/relevance evidence.

## 6. What Candidate Types Are Under-Ranked?

Under-ranked families among the top upward corrections:

Search Ranking Engineer (15), Recommendation Engineer (3), NLP Engineer (1), Evaluation/Relevance Engineer (1)

The committee would raise candidates with strong role-level evaluation, search ranking, retrieval infrastructure, and production metrics even if their current title is broad.

## 7. What Assumptions From V1 Were Correct?

- Career evidence is more reliable than skill keywords.
- Search and retrieval evidence are strong signals.
- AI-transition and keyword-stuffer penalties are useful.
- Recommendation-system candidates can be relevant, but only when connected to ranking/matching/evaluation.
- Market readiness matters, but only after technical relevance is established.

## 8. What Assumptions From V1 Were Incorrect?

- One blended technical score is not enough to separate search ranking, retrieval, recommendation, vector search, NLP, and generic ML.
- Repeated role descriptions should reduce confidence more strongly.
- Recommendation evidence should not automatically imply search/relevance fit.
- Evaluation evidence deserves more explicit weight.
- Consistency concerns should be part of the interview decision, not just a small score adjustment.

## 9. If Only ONE Change Could Be Made In V2, What Should It Be?

Add evidence-traced relevance sub-scores for Search Ranking, Retrieval Infrastructure, Recommendation/Matching, and Evaluation/Relevance Science.

This one change would let V2 distinguish a true search relevance engineer from an adjacent recommendation engineer, NLP engineer, vector-search tool user, or generic AI candidate. It would also make explanations defensible because each score would point to role-level evidence.

## 10. Would You Trust Ranker V1 In A Real Hiring Pipeline?

Yes as a sourcing filter, no as a final ordering system.

V1 is good enough to produce a credible Top 100 review queue. It is not precise enough to decide interview order without human review. The committee would trust V1 to reduce the 100,000-candidate dataset into a serious candidate pool, but would require V2-style evidence traces and family-specific relevance scoring before trusting the top ranks operationally.

## Gold Set Summary

| Gold Label | Count |
| --- | --- |
| MEDIUM | 44 |
| STRONG | 39 |
| ELITE | 12 |
| WEAK | 5 |

## Final Committee Conclusion

Ranker V1 is selecting many of the right people, but it is still over-blending candidate archetypes. The best V2 direction is not more model complexity. It is clearer human-grounded relevance taxonomy, stronger evidence tracing, and stricter handling of repeated/template-like or weakly supported evidence.
