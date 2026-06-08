# Evidence Tracing Blueprint

## Purpose

Ranker V2 should store the evidence behind every meaningful feature. This is the missing layer between scoring and hiring trust.

The evidence trace should answer:

- What matched?
- Where did it match?
- Why did it matter?
- How much did it contribute?
- What concerns reduced trust?

This will improve explanation quality, debugging, calibration, and manual review.

## Evidence Trace Record

Recommended common schema:

```text
candidate_id
feature_family
feature_name
matched_term
canonical_term
evidence_tier
source_type
source_path
role_index
role_title
company
start_date
end_date
duration_months
snippet
ownership_verb
metric_term
recency_weight
source_weight
raw_contribution
capped_contribution
penalty_or_bonus
reason_code
confidence
```

Source types:

- current_role_description
- previous_role_description
- summary
- headline
- skills
- education
- redrob_signals
- forensic_check
- company_context

Evidence tiers:

- strong
- medium
- weak
- anti_signal

## Search Ranking Evidence

What should be stored:

- Matched term: `learning to rank`, `ranker`, `ranking`, `relevance`, `reranking`, `search ranking`.
- Source: role description, summary, skill, headline.
- Role index: current role gets index 0, older roles increment.
- Company and title.
- Snippet around the matched term.
- Ownership verb near the term, such as built, owned, shipped, led, optimized.
- Metric term near the evidence, such as NDCG, MRR, CTR, recruiter engagement.
- Contribution before and after caps.

Why it improves explainability:

- It distinguishes "owned search ranker at Paytm" from "listed ranking in skills."
- It makes title-ambiguous candidates defensible.
- It helps detect keyword repetition.

Example explanation enabled:

```text
Strong search-ranking evidence from current role at Razorpay: snippet mentions building a ranker and optimizing relevance. Contribution came from career description, not skill list.
```

## Retrieval Infrastructure Evidence

What should be stored:

- Matched term: BM25, Elasticsearch, OpenSearch, search infrastructure, query understanding, indexing, semantic search, hybrid retrieval.
- Operational context: index refresh, latency, scale, query logs, retrieval quality regression.
- Source and snippet.
- Production wording and ownership verbs.
- Link to evaluation evidence when retrieval quality was measured.

Why it improves explainability:

- It separates retrieval infrastructure from generic data engineering.
- It distinguishes production search from RAG toy projects.
- It allows V2 to justify why a backend/data profile is or is not search-relevant.

## Recommendation and Matching Evidence

What should be stored:

- Matched term: recommendation systems, recommender, personalization, matching, feed ranking, candidate-job matching.
- Whether ranking, retrieval, or evaluation terms co-occur in the same role.
- Whether the system was user-facing.
- Company/product context.
- Metrics: engagement, conversion, CTR, application rate, saves, recruiter response.

Why it improves explainability:

- It prevents all Recommendation Systems Engineers from being treated equally.
- It shows whether recommendation experience transfers to Redrob's ranking/matching problem.

## Vector Search and Embeddings Evidence

What should be stored:

- Matched term: embeddings, vector search, FAISS, Qdrant, Pinecone, Weaviate, Milvus, pgvector.
- Whether evidence appears in skills, summary, or career descriptions.
- Operational evidence: index refresh, embedding drift, ANN latency, hybrid retrieval, retrieval regression.
- Evaluation evidence: recall@k, NDCG, MRR, online metrics.
- Tool list with cap status.

Why it improves explainability:

- Vector DB names are high-risk for keyword stuffing.
- Evidence tracing helps separate production vector-search engineers from RAG app builders.

## Evaluation/Relevance Science Evidence

What should be stored:

- Matched metric: NDCG, MRR, MAP, recall, precision, CTR, application rate, recruiter engagement.
- Evaluation type: offline benchmark, online A/B test, feedback loop, judgment set.
- System evaluated: ranker, retrieval, recommendation, matching.
- Snippet and role source.
- Whether the candidate built the framework, used it, or only mentioned metrics.

Why it improves explainability:

- Evaluation is a core JD requirement but easy to miss in title/skill matching.
- It reveals whether a candidate can improve ranking rigorously after shipping V2.

## Production Ownership Evidence

What should be stored:

- Ownership verbs: owned, led, shipped, built, maintained, operated, redesigned, optimized.
- System context: production, user-facing, scale, latency, on-call, monitoring.
- Product context: recruiter workflow, candidate matching, commerce, feed, marketplace.
- Company type and role duration.
- Snippet.

Why it improves explainability:

- The JD prefers builders who have shipped systems, not pure researchers or demo builders.
- Production ownership can rescue candidates with less obvious titles.

## Generic AI/ML Evidence

What should be stored:

- ML tools and methods: PyTorch, TensorFlow, scikit-learn, feature engineering, MLOps, LLMs, fine-tuning.
- Source type and source cap status.
- Whether the evidence is attached to search/retrieval/recommendation roles.
- Whether AI evidence is recent-only or supported by pre-LLM production ML history.

Why it improves explainability:

- It prevents generic AI skills from overwhelming direct search/relevance evidence.
- It supports explanations like "strong ML background, but limited ranking evidence."

## Behavioral Evidence

What should be stored:

- last_active_date.
- recruiter_response_rate.
- search_appearance_30d.
- saved_by_recruiters_30d.
- interview_completion_rate.
- profile_views_received_30d.
- notice_period_days.
- open_to_work_flag.
- verified_email and verified_phone.
- Behavioral segment: highly active, moderately active, passive, dormant.

Why it improves explainability:

- It justifies availability tie-breaks.
- It prevents opaque market-score effects.
- It can explain why a strong technical candidate was downweighted for dormancy without implying lack of relevance.

## Consistency and Suspicion Evidence

What should be stored:

- Check name.
- Severity.
- Reason code.
- Fields compared.
- Evidence snippet or values.
- Whether the check was run.
- Whether missing audit coverage means unknown.
- Penalty and cap contribution.

Reason codes:

- current_title_description_mismatch
- previous_title_description_mismatch
- career_incoherence
- education_chronology_issue
- signup_after_last_active
- salary_min_above_max
- skills_current_role_mismatch
- skills_headline_mismatch
- ai_title_weak_ai_evidence
- repeated_profile_family

Why it improves explainability:

- V1's consistency coverage is incomplete.
- The system must distinguish "clean" from "not audited."
- Severe issues should cap scores transparently.

## Evidence Aggregation Rules

Recommended aggregation:

1. Extract evidence by source.
2. Canonicalize matched terms.
3. Assign evidence tier.
4. Apply source weight.
5. Apply role recency/duration weight.
6. Apply ownership/proximity bonus.
7. Cap repeated terms.
8. Sum by feature family.
9. Store both raw and capped contributions.
10. Generate explanations from the trace, not from generic templates.

Source weight order:

1. Career descriptions.
2. Summary.
3. Skills.
4. Headline.

Cap recommendations:

- Cap repeated same-term matches per source.
- Cap skill-only contribution per feature family.
- Cap generic AI/ML contribution unless direct relevance evidence exists.
- Require source diversity for elite scores.

## Candidate-Level Evidence Summary

For each candidate, V2 should output:

```text
candidate_id
final_score
primary_family
secondary_families
search_ranking_score
retrieval_score
recommendation_score
vector_search_score
evaluation_score
production_ownership_score
generic_ml_score
behavioral_score
consistency_penalty
score_cap
top_positive_evidence
top_concerns
evidence_trace_path
```

## Explanation Generation

V2 explanations should be deterministic but evidence-backed.

They should include:

- Top 2-4 positive evidence items.
- Top 1-3 concerns.
- Source labels.
- Role/company context.
- Short snippets when available.
- No claims without trace rows.

They should avoid:

- Generic statements that could apply to many candidates.
- Mentioning ranking/retrieval evidence without source.
- Claiming product ownership from skills.
- Presenting market activity as technical relevance.

## Manual Review Benefit

Evidence traces make it possible for a reviewer to answer in seconds:

- Why is this candidate above another?
- Is this a true search/relevance profile or an adjacent AI profile?
- Did skills or career evidence drive the score?
- Is the candidate being rewarded for repetition?
- Did consistency checks actually run?
- What would need to change in V2 calibration?

The trace system is the foundation for trustworthy V2 ranking and for later supervised learning if labels become available.
