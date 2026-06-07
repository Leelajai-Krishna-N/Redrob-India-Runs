# Executive Summary

## 1. What Ranker V1 Does Well

- It correctly prioritizes demonstrated career evidence over skill keywords. The Top 100 has zero keyword-stuffer and zero AI-transition flags in the committed output.
- It strongly surfaces candidates with ranking/relevance and retrieval/search evidence. Top 100 mean career ranking evidence count is 3.27; retrieval evidence count is 2.94.
- It is deterministic and explainable enough for a V1 baseline: every row has component scores and concise reasoning.
- It does not rely on LLMs, embeddings, external APIs, or neural models.

## 2. What Ranker V1 Does Poorly

- It blends direct search ranking, retrieval, recommendation systems, vector search, and generic AI too much.
- `career_score` can saturate, making top-tail ordering depend on technical repetition and market signals.
- Consistency penalties are incomplete because missing forensic rows are treated as clean.
- Reasoning is template-safe but not evidence-rich; it does not show snippets, role source, or contribution details.

## 3. Biggest Ranking Risks

- Recommendation-system candidates may crowd out direct Search/Relevance engineers if their profiles contain ranking/retrieval language.
- Candidates outside the forensic audit scope may escape consistency penalties.
- Keyword repetition can still inflate technical relevance, especially when repeated in career descriptions.
- Market readiness may over-influence ordering after technical/career scores saturate.

## 4. Biggest Ranking Opportunities

- Build explicit sub-scores for search relevance/ranking, retrieval infrastructure, recommendation ranking, vector search, and generic LLM/RAG.
- Add all-candidate lightweight consistency checks and distinguish unaudited from clean.
- Emit source-level evidence traces: matched term, tier, source, role index, snippet, and score contribution.
- Make market signals a tie-breaker within relevance bands instead of a broad 20% score component.

## 5. Where V2 Should Focus

1. **Relevance understanding**: highest priority. Separate direct search/relevance/ranking from adjacent recommendation/vector/LLM evidence.
2. **Feature engineering**: high priority. Add source diversity, recency, ownership, and term caps.
3. **Fraud detection**: high priority. Apply consistency checks to all candidates or represent missing audit coverage explicitly.
4. **Scoring calibration**: medium-high priority. Reduce saturation and make market readiness a tie-breaker.
5. **Explanation quality**: medium priority. Add evidence snippets and contribution traces.

## Bottom Line

Ranker V1 is a strong first iteration and appears to rank many genuinely relevant candidates. It is not yet precise enough to answer the JD's core distinction: direct Search/Relevance/Ranking engineer versus adjacent Recommendation/AI/RAG engineer. V2 should focus on relevance taxonomy, consistency coverage, and score calibration before adding model complexity.
