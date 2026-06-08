# Top 100 Candidate Family Analysis

## Summary

Ranker V1's Top 100 is strong enough to avoid obvious traps, but it is still a blended pool:

- Search Engineers
- Recommendation Systems Engineers
- NLP Engineers
- Applied ML Engineers
- AI Engineers
- Senior Data Scientists
- Machine Learning Engineers

This is not necessarily bad. The JD itself accepts ranking, search, and recommendation systems. The risk is that V1 has not yet made a principled distinction between core search/relevance ownership and adjacent AI/ML work.

## Top 100 Evidence Snapshot

V1 Top 100:

- Mean final score: 0.9156.
- Mean technical score: 0.9310.
- Mean career score: 0.9721.
- Mean market score: 0.8334.
- Mean consistency score: 0.8697.
- Mean ranking evidence count: 3.27.
- Mean retrieval evidence count: 2.94.
- Mean relevant roles: 2.72.
- Mean relevant duration: 73.66 months.
- Keyword-stuffer flags: 0.
- AI-transition flags: 0.

Interpretation:

The Top 100 generally has substantial role-level evidence. V1 is not simply selecting candidates with AI skills. The remaining question is whether the role-level evidence is the right kind of evidence.

## Top 100 Current Titles

Exact title counts:

- Recommendation Systems Engineer: 16.
- Senior Data Scientist: 11.
- Machine Learning Engineer: 11.
- Applied ML Engineer: 10.
- Search Engineer: 10.
- NLP Engineer: 9.
- AI Engineer: 9.
- Senior NLP Engineer: 6.
- Senior Machine Learning Engineer: 5.
- Staff Machine Learning Engineer: 4.
- Senior Applied Scientist: 4.
- Senior AI Engineer: 3.
- Lead AI Engineer: 2.

Title-family counts:

- Machine Learning title family: 20.
- Recommendation Systems title family: 16.
- NLP title family: 15.
- AI Engineer title family: 14.
- Data Scientist title family: 11.
- Applied ML title family: 10.
- Search Engineer title family: 10.
- Applied Scientist title family: 4.

Interpretation:

The strongest visible title family is not Search Engineer. V1 is surfacing a broader applied ML/recommendation/NLP pool, with explicit Search Engineer titles making up only 10 percent of the Top 100.

## Top 10 Analysis

Top 10 title-family counts:

- Machine Learning title family: 4.
- AI Engineer title family: 3.
- NLP title family: 2.
- Applied Scientist title family: 1.

Top 10 metrics:

- Mean final score: 0.9653.
- Mean technical score: 0.9750.
- Mean career score: 0.9974.
- Mean market score: 0.9309.
- Mean consistency score: 0.9100.
- Mean ranking evidence count: 4.3.
- Mean retrieval evidence count: 4.1.
- Mean relevant roles: 2.9.
- Mean relevant duration: 84.4 months.

Interpretation:

The Top 10 does not visibly look like a "Search Engineer title" list, but the evidence counts are strong. This is a good sign for career-evidence weighting: title alone is not driving rank. The risk is explanation opacity: a hiring manager needs to see role snippets proving why a Lead AI Engineer or NLP Engineer is actually a search/relevance candidate.

## Top 50 Analysis

Top 50 title-family counts:

- AI Engineer title family: 11.
- Machine Learning title family: 10.
- Data Scientist title family: 7.
- NLP title family: 6.
- Recommendation Systems title family: 5.
- Applied ML title family: 4.
- Search Engineer title family: 4.
- Applied Scientist title family: 3.

Top 50 metrics:

- Mean final score: 0.9415.
- Mean technical score: 0.9553.
- Mean career score: 0.9918.
- Mean market score: 0.8790.
- Mean consistency score: 0.8787.
- Mean ranking evidence count: 3.58.
- Mean retrieval evidence count: 3.74.
- Mean relevant roles: 2.98.
- Mean relevant duration: 78.14 months.

Interpretation:

The Top 50 is career-strong, with nearly saturated career scores. It is not dominated by explicit Search Engineer titles. V2 should not force title purity, but it should add sub-scores so a hiring manager can distinguish:

- AI Engineer with search ranker ownership
- AI Engineer with broad LLM work
- NLP Engineer with semantic retrieval
- Recommendation Engineer with ranking/matching

## Top 100 Lower Edge: Ranks 90-100

Ranks 90-100 title-family counts:

- Recommendation Systems title family: 4.
- Machine Learning title family: 4.
- Data Scientist title family: 1.
- Search Engineer title family: 1.
- Applied ML title family: 1.

Ranks 90-100 metrics:

- Mean final score: 0.8654.
- Mean technical score: 0.8745.
- Mean career score: 0.9308.
- Mean market score: 0.7809.
- Mean consistency score: 0.8303.
- Mean ranking evidence count: 3.0.
- Mean retrieval evidence count: 1.27.
- Mean relevant roles: 2.27.
- Mean relevant duration: 68.36 months.

Interpretation:

The lower edge of Top 100 still has ranking evidence but noticeably weaker retrieval evidence. This is where V2 should become more selective. A candidate with recommendation/ranking evidence but weak retrieval may still be interview-worthy, but V2 should label them as recommendation/ranking rather than full search/retrieval fit.

## Dominant Candidate Families

Dominant:

- Broad ML/AI engineers with strong career relevance evidence.
- Recommendation Systems Engineers.
- NLP Engineers with retrieval/ranking language.
- Search Engineers, but not as the largest group.

Likely overrepresented:

- Recommendation Systems Engineers, if their evidence is generic recommender work rather than ranking/matching ownership.
- Broad AI/ML titles, if explanations cannot prove search/relevance work.
- NLP Engineers, if their work is generic language modeling rather than semantic retrieval or ranking.

Likely underrepresented:

- Explicit Search Ranking Engineers.
- Relevance Evaluation Engineers.
- Search Infrastructure Engineers.
- Backend/Search engineers who may not use AI-heavy terminology but have strong production retrieval experience.

Missing or weakly represented:

- Candidates with explicit evaluation-framework ownership as their primary identity.
- Candidates with low-key but deep production search infrastructure experience.
- Candidates who worked on ranker quality without AI branding.

## Would A Hiring Manager Be Satisfied?

Short answer: mostly yes for a first pass, but not fully.

Reasons a hiring manager would be satisfied:

- Top 100 has zero keyword-stuffer and zero AI-transition flags.
- Top candidates show multiple relevant roles and long relevant duration.
- Ranking and retrieval evidence is present in career history.
- Product-company names appear in the Top 100 company distribution, including CRED, Razorpay, Uber, Paytm, Flipkart, Swiggy, Netflix, and Amazon.

Reasons a hiring manager would hesitate:

- The top list is title-ambiguous: many candidates are AI/ML/NLP/Data Science titles, not visibly search/relevance titles.
- Recommendation Systems Engineer is the most common exact title, which may or may not match the core search/ranking intent.
- Explanations are not snippet-backed, so the reviewer cannot quickly verify evidence.
- Evaluation evidence is not surfaced as a first-class reason.
- Market score still materially affects ordering after technical/career scores saturate.

## V2 Implications

1. Keep career evidence as the core signal.
2. Split the Top 100 into candidate families rather than presenting one blended relevance score.
3. Add explicit sub-scores for Search Ranking, Retrieval Infrastructure, Recommendation, Vector Search, and Evaluation.
4. Add evidence tracing so title-ambiguous candidates are defensible.
5. Make market readiness a tie-breaker within relevance bands.
6. Promote candidates with retrieval plus ranking plus evaluation evidence above candidates with only recommendation or only vector-search evidence.

## Desired V2 Top 100 Composition

Top 20 should be dominated by:

- Search Ranking/Relevance Engineers.
- Retrieval Infrastructure Engineers with ranking/evaluation exposure.
- Recommendation Ranking/Matching Engineers with production ownership.

Top 100 should include:

- Search Ranking/Relevance Engineers.
- Retrieval Infrastructure Engineers.
- Strong Recommendation Systems Engineers.
- Vector Search Engineers with production retrieval evidence.
- NLP Engineers only when tied to retrieval/ranking.
- Applied ML Engineers only when tied to production search/recommendation/matching.

Top 100 should exclude or heavily demote:

- Skill-only AI candidates.
- Generic LLM/RAG app builders.
- Generic ML candidates with no search/recommendation/retrieval evidence.
- AI-transition candidates.
- Suspicious or incoherent profiles unless evidence is unusually strong and explainable.
