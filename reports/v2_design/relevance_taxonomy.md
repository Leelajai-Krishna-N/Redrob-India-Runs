# Relevance Taxonomy

## Purpose

Ranker V1 uses a single technical relevance score. That was reasonable for Iteration 1, but V2 needs a taxonomy that separates distinct relevance dimensions:

- Search Ranking
- Retrieval Infrastructure
- Recommendation Systems
- Vector Search
- Evaluation/Relevance Science
- Generic AI/ML
- Data Infrastructure
- Production/Product Ownership
- Behavioral Availability
- Trust/Consistency

The goal is not to create more complexity for its own sake. The goal is to stop treating adjacent candidate types as interchangeable.

## Dimension 1: Search Ranking

Definition:

Experience designing, shipping, improving, or owning ranking systems that order search, discovery, matching, feed, recommendation, or candidate results for users.

High-signal evidence:

- Career descriptions mention learning to rank, LTR, ranker, reranking, ranking features, relevance ranking, search ranking, candidate ranking, job matching ranker.
- Ownership verbs: built, owned, shipped, led, redesigned, optimized, operated.
- Metrics: NDCG, MRR, MAP, CTR, application rate, recruiter engagement, conversion, precision/recall when tied to ranking.
- Multiple roles with ranking evidence or long relevant duration.

Medium-signal evidence:

- Titles such as Search Engineer, Applied Scientist, Staff ML Engineer, Recommendation Systems Engineer.
- Skills include Learning to Rank, relevance, ranking, ranking systems.
- Summaries mention ranking systems without role-level detail.

Weak-signal evidence:

- Skills-only `ranking`.
- Generic `recommendation systems` or `personalization` without ranking details.
- `ranker` in a side project or recent course.

Anti-signals:

- Ranking terms only in skills while career history is unrelated.
- Non-technical current title with AI/ranking skills.
- Repeated ranking keywords without snippets or ownership evidence.

Example candidate types:

- Search Ranking Engineer
- Recommendation Ranking Engineer
- Marketplace Ranking Applied Scientist
- Candidate-JD Matching Engineer

Expected V2 treatment:

- Highest relevance dimension.
- Should dominate Top 20 when supported by career evidence.

## Dimension 2: Retrieval Infrastructure

Definition:

Experience building or operating systems that retrieve candidate, document, item, or content sets before ranking.

High-signal evidence:

- Career descriptions mention BM25, inverted indexes, query processing, indexing, search latency, retrieval quality regression, hybrid retrieval, candidate generation.
- Operational ownership of Elasticsearch, OpenSearch, Solr, FAISS, vector indexes, index refresh, query pipelines.
- Evidence of retrieval quality monitoring and production incidents.

Medium-signal evidence:

- Skills include BM25, Elasticsearch, OpenSearch, semantic search, information retrieval, FAISS.
- Backend/data roles with search infrastructure snippets.
- Work with embeddings as retrieval inputs.

Weak-signal evidence:

- Vector database names in skills only.
- Generic backend or data pipelines without search/retrieval output.

Anti-signals:

- RAG demos without index operations, evaluation, or production deployment.
- Data engineering experience labeled as search because it uses Spark/SQL.

Example candidate types:

- Retrieval Engineer
- Search Infrastructure Engineer
- Backend Search Engineer
- Hybrid Search Engineer

Expected V2 treatment:

- Elite or high relevance.
- Should outrank generic ML when production search/retrieval evidence exists.

## Dimension 3: Recommendation Systems

Definition:

Experience building systems that personalize, rank, match, or recommend candidates, jobs, products, feeds, or content.

High-signal evidence:

- Career descriptions mention recommender systems deployed to users, candidate generation, user-item matching, feed ranking, personalization at scale.
- Ranking/evaluation language appears with recommendation work.
- Product metrics and online experiments are present.

Medium-signal evidence:

- Title is Recommendation Systems Engineer.
- Skills include collaborative filtering, recommendation systems, personalization, matching.
- Company context implies product recommendation surfaces.

Weak-signal evidence:

- Recommendation Systems listed only as a skill.
- Academic recommender projects without deployment.

Anti-signals:

- Recommendation title but no ranking, retrieval, metrics, user-facing system, or ownership.
- Recommendation work only as a model notebook.

Example candidate types:

- Recommendation Systems Engineer
- Marketplace Matching Engineer
- Feed Ranking Engineer
- Personalization ML Engineer

Expected V2 treatment:

- High relevance when ranking/matching/evaluation are present.
- Should not automatically outrank retrieval engineers; context matters.

## Dimension 4: Vector Search

Definition:

Experience using dense embeddings and vector indexes as part of retrieval, matching, or semantic search systems.

High-signal evidence:

- Career descriptions mention embedding index design, ANN search, vector DB operations, embedding drift, index refresh, retrieval regression, hybrid search.
- Production tools: FAISS, Milvus, Qdrant, Weaviate, Pinecone, pgvector, OpenSearch vector search.
- Evaluated vector retrieval against lexical/hybrid baselines.

Medium-signal evidence:

- Skills include vector search, embeddings, sentence transformers, FAISS, Qdrant, Pinecone, Weaviate, Milvus.
- Summary mentions semantic search deployed to real users.

Weak-signal evidence:

- LangChain or RAG using a hosted vector DB with no operational detail.
- Embeddings in skill list only.

Anti-signals:

- Many vector DB names but no career evidence.
- Recent LLM app projects presented as senior search infrastructure experience.

Example candidate types:

- Vector Search Engineer
- Semantic Search Engineer
- RAG Infrastructure Engineer with production retrieval depth

Expected V2 treatment:

- High when operational and evaluated.
- Medium or low when it is only an LLM/RAG app signal.

## Dimension 5: Evaluation/Relevance Science

Definition:

Experience measuring ranking, retrieval, recommendation, or matching quality with offline and online evaluation frameworks.

High-signal evidence:

- Career descriptions mention NDCG, MRR, MAP, offline benchmarks, interleaving, A/B testing, feedback loops, judgment sets, relevance labels.
- Candidate can connect offline metrics to online recruiter/candidate outcomes.
- Built dashboards or evaluation infrastructure used by production teams.

Medium-signal evidence:

- Skills include experimentation, A/B testing, evaluation frameworks, ranking metrics.
- Summary says the candidate improved ranker quality using metrics.

Weak-signal evidence:

- Generic model evaluation, train/test split, accuracy, or F1 not tied to ranking/retrieval.

Anti-signals:

- No evaluation terms in a profile that claims senior ranking ownership.
- Only model metrics for classification tasks.

Example candidate types:

- Relevance Scientist
- Search Evaluation Engineer
- Applied Scientist focused on ranking experiments
- ML Engineer with online experimentation ownership

Expected V2 treatment:

- High leverage dimension.
- Should raise rank significantly when paired with ranking or retrieval evidence.

## Dimension 6: Generic AI/ML

Definition:

General machine learning, deep learning, LLM, NLP, or AI engineering experience not specifically tied to search, ranking, retrieval, recommendation, or evaluation.

High-signal evidence:

- Production ML system ownership at product companies.
- Model deployment and monitoring at scale.
- Feature engineering and MLOps for user-facing systems.

Medium-signal evidence:

- Skills include PyTorch, TensorFlow, scikit-learn, MLOps, MLflow, Hugging Face.
- Titles include Machine Learning Engineer, Applied ML Engineer, Data Scientist, AI Engineer.

Weak-signal evidence:

- Course projects, Kaggle, side projects, prompt engineering, LangChain demos.
- Generic AI keywords in skills.

Anti-signals:

- AI skills on unrelated roles with no AI career evidence.
- LLM-only recent transition without pre-LLM production ML experience.

Example candidate types:

- Applied ML Engineer
- AI Engineer
- Data Scientist
- NLP Engineer

Expected V2 treatment:

- Supporting signal.
- Should not dominate ranking without direct relevance evidence.

## Dimension 7: Data Infrastructure

Definition:

Data pipelines, feature stores, batch/stream processing, warehouses, quality systems, and analytics infrastructure that support ranking/retrieval systems.

High-signal evidence:

- Feature pipelines for ranking/recommendation/search.
- Real-time candidate/user activity pipelines feeding ranking models.
- Data quality checks for relevance, inventory, or feedback data.

Medium-signal evidence:

- Spark, Airflow, Kafka, SQL, dbt, Snowflake, BigQuery, Databricks.
- Backend/data hybrid roles.

Weak-signal evidence:

- Generic warehouse or analytics ETL unrelated to search or ML.

Anti-signals:

- Treating data pipelines as retrieval infrastructure without search-specific output.

Example candidate types:

- Data Engineer
- Analytics Engineer
- ML Platform Engineer
- Backend/Data hybrid

Expected V2 treatment:

- Supporting dimension.
- Valuable when attached to ranker/retrieval features or feedback loops.

## Dimension 8: Production/Product Ownership

Definition:

Evidence that the candidate has shipped and owned systems used by real users, especially in product companies.

High-signal evidence:

- Owned or led production systems.
- Product company context.
- User-facing impact and business metrics.
- On-call, monitoring, scale, latency, reliability, incident handling.

Medium-signal evidence:

- Worked closely with product or recruiter/customer teams.
- Built systems used internally or by client teams.

Weak-signal evidence:

- Prototypes, POCs, academic work, demo apps.

Anti-signals:

- Pure research without deployment.
- Consulting-only prototypes without long-term ownership.

Example candidate types:

- Product Search Engineer
- Marketplace Ranking Engineer
- Applied Scientist with shipped systems
- Backend Search Infrastructure Engineer

Expected V2 treatment:

- Multiplicative trust signal for relevance evidence.
- Should help separate product search engineers from demo builders.

## Dimension 9: Behavioral Availability

Definition:

Signals that the candidate is reachable, active, and likely to respond to recruiting.

High-signal evidence:

- Recent activity.
- High recruiter response rate.
- High interview completion rate.
- Strong search appearances and saves.
- Low notice period.
- Open-to-work flag with verified contact details.

Medium-signal evidence:

- Moderate activity and engagement.
- Good profile completeness.

Weak-signal evidence:

- One strong signal in isolation.

Anti-signals:

- Dormant profile.
- Very low recruiter response rate.
- Long notice period when other signals are weak.

Example candidate types:

- Strong but passive senior candidate.
- Active AI-title candidate.
- Behavioral twin of a stronger profile.

Expected V2 treatment:

- Tie-breaker within relevance bands.
- Should not push a weakly relevant candidate above a clearly stronger search/relevance engineer.

## Dimension 10: Trust/Consistency

Definition:

Profile coherence across title, descriptions, education chronology, timelines, salary ranges, skills, and career progression.

High-signal evidence:

- Career progression is plausible.
- Skills match titles and descriptions.
- Education and employment timelines are possible.
- Salary and experience are plausible.

Medium-signal evidence:

- Minor title-description mismatch but otherwise coherent.

Weak-signal evidence:

- Missing audit coverage should be treated as unknown, not clean.

Anti-signals:

- Impossible dates.
- Abrupt unrelated career jumps.
- AI skills attached to unrelated careers.
- Contradictory behavioral or salary signals.
- Repeated synthetic profile families.

Example candidate types:

- Realistic senior search engineer.
- Suspicious retrieval-labeled non-ML profile.
- Keyword stuffer.

Expected V2 treatment:

- Penalty and score cap for high-confidence severe issues.
- Soft penalty for incomplete or unaudited evidence.

## Taxonomy Priority

Recommended primary ordering for V2:

1. Search Ranking
2. Retrieval Infrastructure
3. Evaluation/Relevance Science
4. Recommendation Systems with ranking/matching ownership
5. Vector Search with production retrieval evidence
6. Production/Product Ownership
7. Generic AI/ML
8. Data Infrastructure
9. Behavioral Availability
10. Trust/Consistency as a cap/penalty system

This order reflects the JD's true intent: hire someone who can improve Redrob's candidate-JD matching and ranking product, not simply someone with many AI keywords.
