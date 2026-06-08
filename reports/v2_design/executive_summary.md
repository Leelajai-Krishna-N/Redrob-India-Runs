# Executive Summary

## Bottom Line

Ranker V2 should become a relevance-taxonomy ranker, not a more complicated keyword scorer.

Ranker V1 already does the most important first thing: it trusts career evidence more than skills and removes obvious AI-transition candidates and keyword stuffers from the Top 100. The next gap is precision. V1 blends Search Engineers, Retrieval Engineers, Recommendation Engineers, NLP Engineers, Applied ML Engineers, and generic AI profiles into one technical score.

V2 should answer a sharper question:

Who would we actually interview first to build production search, ranking, retrieval, recommendation, and evaluation systems for Redrob?

## What The JD Really Wants

The JD is not primarily a generic Senior AI Engineer role. It is a founding search/relevance/ranking role.

The ideal candidate has:

- Production ranking, retrieval, matching, or recommendation ownership.
- Experience with systems used by real users.
- Ability to improve a BM25/rule-based system and ship a better V2 quickly.
- Evaluation-framework experience: offline benchmarks, online A/B testing, recruiter feedback loops.
- Practical product judgment, not just research or demo-building.
- Enough behavioral availability to be reachable.

## What V1 Gets Right

V1 is a strong baseline:

- Top 100 keyword-stuffer flags: 0.
- Top 100 AI-transition flags: 0.
- Top 100 mean ranking evidence count: 3.27.
- Top 100 mean retrieval evidence count: 2.94.
- Top 100 mean relevant roles: 2.72.
- Top 100 mean relevant duration: 73.66 months.

This means V1 is not simply ranking people with the most AI skills. It is surfacing candidates with meaningful role-level evidence.

## What V1 Still Blends Together

Top 100 title-family counts:

- Machine Learning title family: 20.
- Recommendation Systems title family: 16.
- NLP title family: 15.
- AI Engineer title family: 14.
- Data Scientist title family: 11.
- Applied ML title family: 10.
- Search Engineer title family: 10.
- Applied Scientist title family: 4.

This is a good candidate pool, but it is not yet a precise search/relevance ranking. Recommendation Systems Engineer is the most common exact Top 100 title, while explicit Search Engineer titles are only 10 percent of Top 100.

The major V2 question is not "Are these candidates relevant?" Many are. The question is "Which type of relevance do they have, and is it the relevance the JD needs most?"

## Target Candidate Definition For V2

The target candidate is:

A product-oriented search/relevance engineer with production experience shipping ranking, retrieval, matching, or recommendation systems, plus enough evaluation depth to improve quality rigorously.

Preferred Top 20 candidate families:

1. Search Ranking/Relevance Engineer.
2. Retrieval Infrastructure Engineer with ranking/evaluation exposure.
3. Recommendation Ranking/Matching Engineer with production ownership.
4. Evaluation/Relevance Scientist attached to ranking or retrieval systems.

Preferred Top 100 candidate families:

1. Search Ranking/Relevance Engineers.
2. Retrieval Infrastructure Engineers.
3. Strong Recommendation Systems Engineers.
4. Vector Search Engineers with production retrieval evidence.
5. NLP Engineers tied to semantic retrieval/ranking.
6. Applied ML Engineers tied to search/recommendation/matching.

Lower-priority families:

- Generic AI/ML.
- Generic RAG/LLM app builders.
- Generic data/backend engineers without search/relevance evidence.
- Consulting-only profiles without production product ownership.
- AI-transition candidates.
- Keyword stuffers.

## Recommended V2 Architecture

V2 should expose separate sub-scores:

- Search Ranking.
- Retrieval Infrastructure.
- Recommendation/Matching.
- Vector Search.
- Evaluation/Relevance Science.
- Production Ownership.
- Generic AI/ML support.
- Behavioral Availability.
- Consistency/Trust.

The final score can remain a single number, but ranking diagnostics and explanations should show the sub-score profile.

## Biggest V2 Design Shifts

1. Separate direct search/relevance/ranking evidence from adjacent AI/ML evidence.
2. Treat recommendation systems as high-value only when they include ranking, matching, evaluation, or product metrics.
3. Treat vector search as high-value only when it is production retrieval, not merely RAG/tool usage.
4. Promote evaluation-framework evidence.
5. Make market readiness a tie-breaker within relevance bands.
6. Apply consistency checks more broadly and distinguish unaudited from clean.
7. Store source-level evidence traces for every important contribution.

## Highest-Risk Confusions

1. Recommendation Engineer vs Search Ranking Engineer.
2. Vector Search Engineer vs RAG Engineer.
3. Keyword Stuffer vs Vector/Retrieval Candidate.
4. NLP Engineer vs Search/Relevance Engineer.
5. Applied ML Engineer vs Ranking Engineer.
6. Retrieval Infrastructure Engineer vs Generic Data Engineer.
7. Consulting AI Candidate vs Product Search Engineer.
8. Behavioral Twin vs Strong Relevance Candidate.

## What Evidence V2 Must Store

Every meaningful feature should store:

- Matched term.
- Canonical term.
- Source type.
- Role index.
- Role title.
- Company.
- Date/duration.
- Snippet.
- Ownership verb.
- Metric term.
- Source weight.
- Raw contribution.
- Capped contribution.
- Reason code.

This trace is the key to moving from plausible explanations to auditable explanations.

## V2 Priorities

Highest impact:

1. Relevance taxonomy and sub-scores.
2. Evidence tracing.
3. Search Ranking and Retrieval feature refinement.
4. Evaluation/Relevance Science features.
5. All-candidate consistency coverage or explicit audit-coverage flags.

Medium impact:

1. Market readiness as tie-breaker.
2. Product/company context features.
3. Recommendation/matching calibration.
4. Generic AI/ML caps and dampeners.

Lower impact:

1. More charts.
2. More generic skill features.
3. More complex modeling without better evidence definitions.

## Final Recommendation

Do not implement V2 as a larger version of V1.

Implement V2 as a clearer hiring judgment system:

- First decide what type of relevance a candidate has.
- Then decide how strong and trustworthy that evidence is.
- Then apply availability and consistency adjustments.
- Then generate explanations from stored evidence traces.

The people to interview first are not the candidates with the most AI terms. They are the candidates whose career history proves they can build, operate, evaluate, and improve production ranking, retrieval, matching, or recommendation systems.
