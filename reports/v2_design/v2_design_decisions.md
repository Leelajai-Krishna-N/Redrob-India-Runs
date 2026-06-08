# V2 Design Decisions

## Q1. What candidate type should dominate Top 20?

Recommendation:

Top 20 should be dominated by Search Ranking/Relevance Engineers and Retrieval Infrastructure Engineers with ranking/evaluation evidence. Strong Recommendation Ranking/Matching Engineers should also appear, but they should not dominate unless they show clear production ranking, matching, or evaluation ownership.

Evidence:

- The JD's core mandate is ranking, retrieval, and matching systems for recruiters and candidates.
- The first 90 days include auditing BM25/rule-based ranking, shipping V2 ranking improvements, and building evaluation infrastructure.
- V1 Top 10 has strong mean ranking evidence count 4.3 and retrieval evidence count 4.1, even though titles are not all Search Engineer.

Confidence: High

## Q2. What candidate type should dominate Top 100?

Recommendation:

Top 100 should be a controlled blend:

- Search Ranking/Relevance Engineers.
- Retrieval Infrastructure Engineers.
- Recommendation Systems Engineers with ranking/matching/evaluation evidence.
- Vector Search Engineers with production retrieval evidence.
- NLP or Applied ML Engineers only when their work feeds search, retrieval, recommendation, matching, or evaluation.

Generic AI/ML, generic data engineering, and LLM/RAG app profiles should not dominate.

Evidence:

- V1 Top 100 is already a blend: Machine Learning title family 20, Recommendation Systems 16, NLP 15, AI Engineer 14, Data Scientist 11, Applied ML 10, Search Engineer 10, Applied Scientist 4.
- Top 100 has zero keyword-stuffer and zero AI-transition flags, showing V1's filtering is directionally right.
- The lower Top 100 edge has reduced retrieval evidence, suggesting V2 needs more family-aware selection.

Confidence: High

## Q3. Should recommendation engineers rank above retrieval engineers?

Recommendation:

Not by default.

A Recommendation Systems Engineer should rank above a Retrieval Infrastructure Engineer only when the recommendation work includes ranking, matching, user-facing product ownership, and evaluation evidence. A retrieval engineer with production hybrid search/indexing/evaluation evidence should usually rank above a generic recommender modeler.

Evidence:

- The JD says recommendation-system builders can be fits, but the role's day-one mandate is improving retrieval/ranking/matching.
- Recommendation Systems Engineer is the most common exact Top 100 title at 16 candidates.
- Ranks 90-100 include 4 Recommendation Systems Engineer titles and have weaker mean retrieval evidence count at 1.27.

Confidence: Medium-High

## Q4. Should retrieval engineers rank above generic ML engineers?

Recommendation:

Yes. Retrieval engineers should rank above generic ML engineers when retrieval evidence is production-grade and role-level.

Generic ML should be a supporting signal, not a primary relevance dimension.

Evidence:

- The JD specifically calls for retrieval, hybrid search, vector databases, search infrastructure, BM25, embeddings, and index-quality work.
- The current product baseline is BM25 plus rule-based scoring, so retrieval expertise is immediately actionable.
- Generic ML titles are common in Top 100, but the best ones rank highly because career evidence contains ranking/retrieval.

Confidence: High

## Q5. How important is evaluation-framework experience?

Recommendation:

Evaluation-framework experience should be a high-value feature family and a major differentiator among otherwise similar candidates.

It should not replace ranking/retrieval evidence, but it should substantially boost candidates who have both.

Evidence:

- The JD's first 90 days include setting up offline benchmarks, online A/B tests, and recruiter-feedback loops.
- The JD explicitly says candidates who have not thought about rigorous ranking evaluation will struggle.
- V1 explanations do not sufficiently expose evaluation evidence, so V2 has an opportunity to improve precision and explainability.

Confidence: High

## Q6. How important is ranking-system ownership?

Recommendation:

Ranking-system ownership should be the single highest-value positive signal in V2.

The highest score tier should require role-level evidence of building, owning, shipping, or improving a ranking, relevance, matching, or search-ordering system.

Evidence:

- The JD asks for someone to own the intelligence layer and ship a V2 ranking system quickly.
- Top-ranked V1 candidates have strong ranking evidence counts, with Top 10 mean ranking evidence count 4.3.
- The challenge warns against keyword matching, meaning ownership evidence matters more than term presence.

Confidence: High

## Q7. How important is recruiter-engagement data?

Recommendation:

Recruiter-engagement data should matter as an availability and tie-break signal, not as a core relevance signal.

Use it to:

- Separate similarly relevant candidates.
- Downweight dormant or unreachable candidates.
- Highlight high-priority outreach among technically strong profiles.

Do not let it compensate for weak search/relevance evidence.

Evidence:

- The JD says a perfect-on-paper but unavailable candidate is not actually available for hiring purposes.
- V1 market score has 20 percent weight and Top 100 mean market score is 0.8334.
- V1 review identified market over-influence as a risk after technical and career scores saturate.

Confidence: Medium-High

## Q8. How aggressive should consistency penalties be?

Recommendation:

Consistency penalties should be aggressive for high-confidence severe issues and moderate for soft inconsistencies.

Use both:

- Penalties for minor or moderate concerns.
- Score caps for severe contradictions, impossible timelines, or high-confidence synthetic patterns.

Also distinguish clean from unaudited.

Evidence:

- V1 consistency coverage is incomplete.
- 84,239 candidates have consistency_score exactly 1.0, and missing forensic rows can be treated as clean.
- The challenge warns about honeypots and synthetic anomalies.
- Top 100 consistency score is not perfect: mean consistency score 0.8697, and Top 10 mean is 0.91.

Confidence: High

## Additional Design Decisions

## Should breadth of skills or depth of relevance dominate?

Recommendation:

Depth of relevance should dominate.

Skill breadth should help only after direct career evidence is present. Skill-only breadth should be capped and may become a risk signal if it conflicts with the candidate's career.

Evidence:

- V1 correctly removes Top 100 keyword stuffers by trusting career evidence more than skill keywords.
- The JD explicitly warns against ranking by AI keyword count.

Confidence: High

## Should V2 use one blended technical score?

Recommendation:

No. V2 should expose separate sub-scores:

- Search Ranking
- Retrieval Infrastructure
- Recommendation/Matching
- Vector Search
- Evaluation/Relevance Science
- Generic AI/ML support

The final score can remain single, but diagnostics and explanations must show the sub-score profile.

Evidence:

- V1 is ranking a blended pool of Search, Retrieval, Recommendation, NLP, and Applied ML candidates.
- The main V2 risk is confusing adjacent families.

Confidence: High

## Should title matching matter?

Recommendation:

Title matching should be a weak-to-medium signal.

Titles should help identify families but must not override career descriptions.

Evidence:

- V1 Top 10 contains no explicit Search Engineer titles, yet has strong career ranking/retrieval evidence.
- Top 100 includes only 10 explicit Search Engineer titles.

Confidence: High

## Should product-company experience matter?

Recommendation:

Yes, but as a multiplier or trust signal, not a standalone score.

Product-company experience should increase confidence when paired with ranking/retrieval/recommendation evidence.

Evidence:

- The JD prefers applied ML at product companies and production deployment.
- The role involves real recruiter workflows and product metrics.

Confidence: Medium-High

## Should consulting-only careers be penalized?

Recommendation:

Use a nuanced penalty.

Do not over-penalize all consulting. Penalize consulting-only careers when they lack production ownership, long-term system operation, or direct product metrics.

Evidence:

- Consulting is a very large bucket in the forensic comparison, so a blunt penalty can suppress many candidates.
- Some consultants may have strong production search/relevance project experience.

Confidence: Medium

## Final V2 Ranking Intent

V2 should interview first:

1. Candidates with production search ranking/relevance ownership.
2. Candidates with retrieval infrastructure plus ranking/evaluation evidence.
3. Candidates with recommendation/matching systems that look like the Redrob problem.
4. Candidates with vector-search depth only when production retrieval and evaluation evidence are present.
5. Candidates with generic AI/ML only when direct relevance evidence is clear.

V2 should not interview first:

1. Candidates whose relevance is mostly skill keywords.
2. Generic RAG/LLM app builders.
3. AI-transition candidates without substantial production ML/search history.
4. Candidates with severe unresolved consistency issues.
5. Strong market candidates with weak technical relevance.
