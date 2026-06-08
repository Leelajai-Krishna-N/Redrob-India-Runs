# V2 Feature Blueprint

## Design Principle

Whenever skills and demonstrated career evidence conflict, trust demonstrated career evidence more heavily.

V2 should not become a complex model. It should become a more precise relevance system with separate feature families, evidence traces, source caps, and calibration rules.

## Feature Family 1: Search Ranking Features

Purpose:

Identify candidates with direct ranking, relevance, reranking, or matching-system ownership.

Rationale:

This is the highest-intent JD dimension. Redrob needs someone to improve a current BM25/rule-based ranking system and own candidate-JD matching.

Candidate evidence:

- learning to rank
- LTR
- ranker
- ranking
- reranking
- relevance
- candidate ranking
- job matching
- search ranking
- feed ranking
- marketplace ranking

Feature ideas:

- Career ranking evidence count.
- Source-diverse ranking evidence count.
- Role-level ranking ownership verbs.
- Relevant ranking duration.
- Ranking evidence recency.
- Ranking evidence in current role.
- Ranking terms capped by unique source/role.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Over-counting generic `ranking` mentions if snippets are not source-limited.
- Missing candidates who describe ranking using domain-specific words like matching, ordering, discovery, or relevance tuning.

## Feature Family 2: Retrieval Infrastructure Features

Purpose:

Identify candidates who can operate and improve retrieval systems, lexical search, hybrid search, indexes, and candidate generation pipelines.

Rationale:

The first 90 days include improving BM25/rule-based systems and likely adding hybrid retrieval. Retrieval infrastructure is a core production need.

Candidate evidence:

- information retrieval
- BM25
- semantic search
- hybrid search
- Elasticsearch
- OpenSearch
- Solr
- FAISS
- indexing
- query understanding
- candidate generation
- retrieval quality regression
- index refresh

Feature ideas:

- Career retrieval evidence count.
- Retrieval infrastructure tool evidence.
- Operational retrieval verbs.
- Index/latency/quality snippets.
- Hybrid retrieval evidence.
- Retrieval duration and recency.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Confusing generic data pipelines with retrieval pipelines.
- Confusing RAG demos with retrieval infrastructure.

## Feature Family 3: Recommendation and Matching Features

Purpose:

Identify candidates who built recommendation, personalization, feed ranking, marketplace matching, or candidate-job matching systems.

Rationale:

The JD explicitly says a candidate who built a recommendation system at a product company can be a strong fit. Recommendation is relevant when it is ranking/matching/evaluation-oriented.

Candidate evidence:

- recommendation systems
- recommender
- personalization
- collaborative filtering
- user-item matching
- feed ranking
- marketplace ranking
- candidate-job matching

Feature ideas:

- Recommendation evidence count.
- Recommendation plus ranking co-occurrence.
- Recommendation plus evaluation co-occurrence.
- Product/marketplace company context.
- Online metric evidence.
- Matching-system evidence separate from generic recommender modeling.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Over-ranking recommender modeling without search/relevance transfer.
- Treating every Recommendation Systems Engineer title as equally relevant.

## Feature Family 4: Evaluation and Relevance Science Features

Purpose:

Identify candidates who know how to measure, debug, and improve ranking/retrieval/recommendation quality.

Rationale:

The JD explicitly requires evaluation infrastructure: offline benchmarks, online A/B testing, recruiter-feedback loops, and rigorous ranking metrics.

Candidate evidence:

- NDCG
- MRR
- MAP
- precision/recall for retrieval
- offline evaluation
- online A/B testing
- relevance labels
- judgment sets
- feedback loops
- offline-to-online correlation

Feature ideas:

- Ranking-metric evidence.
- Evaluation framework ownership.
- Online experiment evidence.
- Recruiter feedback loop evidence.
- Evaluation evidence attached to ranking/retrieval roles.

Expected impact: High

Implementation difficulty: Medium-High

Risk:

- Sparse data: strong candidates may not list metrics explicitly.
- Generic model evaluation should not be confused with ranking evaluation.

## Feature Family 5: Vector Search and Embeddings Features

Purpose:

Identify dense retrieval and embedding-system experience while avoiding vector-DB keyword inflation.

Rationale:

The JD values embeddings and hybrid retrieval, but vector DB names are easy to stuff.

Candidate evidence:

- embeddings
- vector search
- semantic retrieval
- sentence transformers
- FAISS
- Qdrant
- Pinecone
- Weaviate
- Milvus
- pgvector
- ANN search

Feature ideas:

- Career-level vector retrieval evidence.
- Tool evidence source weights.
- Production vector operations evidence.
- Embedding drift/index refresh evidence.
- Vector retrieval plus evaluation evidence.
- Skill-only vector cap.

Expected impact: Medium-High

Implementation difficulty: Medium

Risk:

- Over-rewarding RAG app builders.
- Under-rewarding older search engineers who used lexical/hybrid systems before vector DB branding.

## Feature Family 6: Production Ownership Features

Purpose:

Reward candidates who have shipped and owned systems used by real users.

Rationale:

The JD values production deployment, product-engineering attitude, and real user feedback over research-only or demo-only experience.

Candidate evidence:

- shipped
- owned
- led
- production
- deployed
- on-call
- scale
- latency
- monitoring
- user-facing
- recruiter/customer/product metrics

Feature ideas:

- Ownership verb count in career descriptions.
- Production system evidence.
- User-facing metric evidence.
- On-call/operational evidence.
- Product-company context.
- Prototype-only penalty.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Synthetic descriptions may overuse ownership verbs.
- Company type inference can be noisy.

## Feature Family 7: Product/Company Context Features

Purpose:

Prefer candidates whose career context resembles product environments with search, discovery, matching, recommendation, or marketplace surfaces.

Rationale:

The JD explicitly prefers applied ML at product companies over pure services and pure research.

Candidate evidence:

- Product/SaaS companies.
- Marketplace, e-commerce, fintech, social, content, recruiting, mobility, food delivery, media.
- Search/recommendation-intensive companies or teams.

Feature ideas:

- Product-company role count.
- Services-only career flag.
- Marketplace/search-domain company flag.
- Current company relevance.
- Product-company plus ranking/retrieval interaction feature.

Expected impact: Medium

Implementation difficulty: Medium

Risk:

- Company classification can be brittle and biased.
- Strong service-company candidates should remain recoverable with direct evidence.

## Feature Family 8: Career Progression and Duration Features

Purpose:

Reward sustained relevant experience and progression in technical tracks.

Rationale:

The ideal candidate has several years of applied ML/search/recommendation ownership. Duration and progression help separate deep builders from one-off exposure.

Candidate evidence:

- Multiple relevant roles.
- Relevant duration in months.
- Seniority progression.
- Current role relevance.
- Staff/lead/senior scope when paired with evidence.

Feature ideas:

- Relevant role count.
- Relevant duration by dimension.
- Current relevant role bonus.
- Seniority-adjusted ownership signal.
- Recency decay.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Experience duration can reward old or stale experience.
- Seniority title without hands-on production work should not dominate.

## Feature Family 9: Generic AI/ML Support Features

Purpose:

Retain useful AI/ML signals without letting broad AI skill breadth dominate the ranker.

Rationale:

Strong search/relevance engineers need ML fluency, but generic AI/ML alone is not the target.

Candidate evidence:

- PyTorch
- TensorFlow
- scikit-learn
- MLOps
- feature engineering
- model deployment
- NLP
- LLMs
- fine-tuning

Feature ideas:

- Generic ML support score.
- LLM/RAG evidence as low-tier unless career-backed.
- Skill breadth cap.
- Generic AI dilution penalty when direct relevance is absent.

Expected impact: Medium

Implementation difficulty: Low-Medium

Risk:

- Penalizing valid ML generalists who have sparse profile text.
- Overfitting to visible keywords.

## Feature Family 10: Behavioral Availability Features

Purpose:

Represent whether a relevant candidate is reachable and likely to engage.

Rationale:

The JD states that a perfect-on-paper candidate with stale activity and low recruiter response is not practically available.

Candidate evidence:

- last_active_date
- recruiter_response_rate
- search_appearance_30d
- saved_by_recruiters_30d
- interview_completion_rate
- profile_views_received_30d
- notice_period_days
- open_to_work_flag
- verified_email
- verified_phone

Feature ideas:

- Market readiness score.
- Dormancy penalty.
- Engagement bucket.
- Low notice period tie-breaker.
- High relevance but dormant label.

Expected impact: Medium

Implementation difficulty: Low

Risk:

- Overweighting availability can push weaker profiles above better candidates.
- Behavioral twins can create false confidence.

## Feature Family 11: Consistency and Trust Features

Purpose:

Identify suspicious, incoherent, or synthetic profiles and prevent severe issues from ranking too high.

Rationale:

The challenge warns about honeypots, keyword stuffers, AI transitions, behavioral twins, and synthetic artifacts.

Candidate evidence:

- Title-description mismatch.
- Skill-role mismatch.
- Career incoherence.
- Education chronology issue.
- Timeline violation.
- Salary inconsistency.
- Unrealistic expertise bundle.
- Repeated profile family.

Feature ideas:

- Lightweight all-candidate consistency checks.
- Severe consistency cap.
- Soft consistency penalty.
- Unknown-audit coverage flag.
- Contradiction reason codes.

Expected impact: High

Implementation difficulty: Medium-High

Risk:

- False positives can suppress unusual but real career paths.
- Current forensic coverage is incomplete, so missing rows must not mean clean.

## Feature Family 12: Evidence Quality Features

Purpose:

Measure not just whether terms appear, but how trustworthy and useful the evidence is.

Rationale:

V1 can still be affected by repetition. V2 should reward source diversity, ownership, snippets, and role-level evidence.

Candidate evidence:

- Source type: career description, summary, skills, headline.
- Role index and recency.
- Matched term tier.
- Ownership verb proximity.
- Snippet quality.
- Unique term count.
- Repetition count.

Feature ideas:

- Source-diverse evidence score.
- Unique high-signal term count.
- Repetition cap.
- Role-level evidence coverage.
- Evidence-source reliability multiplier.

Expected impact: High

Implementation difficulty: Medium

Risk:

- Feature interactions can become hard to calibrate if not logged clearly.

## Recommended V2 Feature Priorities

Highest priority:

1. Search Ranking Features.
2. Retrieval Infrastructure Features.
3. Evaluation/Relevance Science Features.
4. Evidence Quality Features.
5. Consistency and Trust Features.

Second priority:

1. Recommendation and Matching Features.
2. Career Progression and Duration Features.
3. Production Ownership Features.
4. Behavioral Availability Features.

Lower priority:

1. Generic AI/ML Support Features.
2. Product/Company Context Features.
3. Data Infrastructure support features.

The highest-impact change is not adding a model. It is decomposing relevance so V2 knows whether it is ranking a search engineer, retrieval engineer, recommendation engineer, vector-search engineer, or generic AI candidate.
