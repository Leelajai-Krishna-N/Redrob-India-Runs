# Candidate Archetype Analysis

## Evidence Base

This analysis uses:

- `outputs/ranker_v1/top_100_candidates.csv`
- `outputs/ranker_v1/candidate_scoring.csv`
- `outputs/ranker_v1/ranking_report.md`
- `outputs/eda/profile_samples/`
- `outputs/eda/forensic_audit/`
- `data/raw/.../candidates.jsonl`
- the released `job_description.docx`

Key V1 facts:

- Candidate count: 100,000.
- Top 100 mean ranking evidence count: 3.27.
- Top 100 mean retrieval evidence count: 2.94.
- Top 100 mean relevant roles: 2.72.
- Top 100 mean relevant duration: 73.66 months.
- Top 100 keyword-stuffer flags: 0.
- Top 100 AI-transition flags: 0.
- Top 100 title families: Machine Learning 20, Recommendation Systems 16, NLP 15, AI Engineer 14, Data Scientist 11, Applied ML 10, Search Engineer 10, Applied Scientist 4.

The most important observation is that V1 already filters obvious low-quality keyword-only profiles from the top tail, but it still blends multiple candidate families that a hiring manager would not treat as equally relevant.

## Archetype 1: Search Ranking Engineer

Expected rank: Elite

Core characteristics:

- Titles: Search Engineer, Staff Machine Learning Engineer, Senior Machine Learning Engineer, Applied Scientist, sometimes AI Engineer or Senior Data Scientist.
- Skills: Learning to Rank, ranking, relevance, BM25, Elasticsearch, OpenSearch, semantic search, feature engineering, experimentation.
- Companies: product, marketplace, advertising, consumer, recruiting, fintech, commerce, or search-heavy platforms.
- Descriptions: built rankers, rerankers, relevance pipelines, candidate/job matching, search ranking, ranking features, ranking evaluation, feedback loops.
- Behavioral pattern: strong market engagement helps, but should not be required when evidence is excellent.

Strengths:

- Direct match to the JD's mandate to own ranking, retrieval, and matching systems.
- Career evidence is harder to fake than skill lists.
- Usually capable of discussing tradeoffs among BM25, dense retrieval, reranking, features, and online metrics.

Weaknesses:

- Titles are not always explicit; many strong profiles hide under ML Engineer or Data Scientist titles.
- V1 can over-reward repeated ranking terms without distinguishing ownership from exposure.

Why:

- The JD explicitly asks for someone who has shipped ranking, search, or recommendation systems to real users.
- Top 10 candidates have mean ranking evidence count 4.3 and mean retrieval evidence count 4.1, suggesting the strongest candidates have both relevance and retrieval language in career evidence.

## Archetype 2: Retrieval Infrastructure Engineer

Expected rank: Elite to High

Core characteristics:

- Titles: Search Engineer, Backend Engineer, Data Engineer, ML Engineer, Infrastructure Engineer.
- Skills: BM25, Elasticsearch, OpenSearch, FAISS, indexing, hybrid search, query understanding, retrieval quality, search infrastructure.
- Companies: product companies with search or discovery surfaces; infra-heavy teams.
- Descriptions: index refreshes, retrieval regression, search latency, document ingestion, query pipelines, operational search systems.
- Behavioral pattern: can be slightly less visible in recruiter signals than AI-title candidates, but career evidence should dominate.

Strengths:

- Strong match to production search and candidate-JD matching infrastructure.
- Usually stronger than generic AI profiles for the first 90-day mandate.

Weaknesses:

- May not have ranking ownership.
- Can look like a generic backend/data engineer if the scoring system only checks titles or skill names.

Why:

- The JD values production experience with vector databases or hybrid search infrastructure and explicitly names OpenSearch, Elasticsearch, FAISS, Pinecone, Weaviate, Qdrant, and Milvus.
- Top 100 skills contain BM25 39, OpenSearch 36, Elasticsearch 35, Information Retrieval 29, Semantic Search 28, and Vector Search 28.

## Archetype 3: Recommendation Systems Engineer

Expected rank: High, sometimes Elite

Core characteristics:

- Titles: Recommendation Systems Engineer, ML Engineer, Applied Scientist, Data Scientist.
- Skills: recommendation systems, personalization, collaborative filtering, ranking, matching, embeddings, experimentation.
- Companies: marketplaces, social, commerce, media, fintech, food delivery, ride-sharing.
- Descriptions: feed ranking, user-item matching, personalized retrieval, candidate/job matching, marketplace ranking.
- Behavioral pattern: frequently strong in Top 100 because recommendation language overlaps with ranking and matching.

Strengths:

- Recommendation systems often share the same production problems as search ranking: candidate generation, ranking, online metrics, feedback loops.
- JD explicitly says a profile can be strong if career history shows they built a recommendation system at a product company.

Weaknesses:

- Not all recommendation work is search relevance work.
- V1 may overpromote recommendation candidates because recommendation titles are common and often co-occur with ranking/retrieval terms.

Why:

- Recommendation Systems Engineer is the most common exact title in Top 100 with 16 candidates.
- Ranks 90-100 include 4 Recommendation Systems Engineer titles, but that slice has lower mean retrieval evidence count at 1.27 than the full Top 100 at 2.94. This suggests some recommendation candidates are strong, while others may be adjacent rather than core search/retrieval fits.

## Archetype 4: Vector Search Engineer

Expected rank: High to Medium

Core characteristics:

- Titles: ML Engineer, AI Engineer, NLP Engineer, Search Engineer, Backend Engineer.
- Skills: embeddings, vector search, FAISS, Qdrant, Pinecone, Weaviate, Milvus, pgvector, sentence transformers, semantic search.
- Companies: AI platforms, search products, marketplaces, data/infra teams.
- Descriptions: embedding index refresh, semantic retrieval, ANN search, hybrid retrieval, retrieval quality monitoring.
- Behavioral pattern: often looks attractive in skills, but work-history proof is uneven.

Strengths:

- Modern retrieval systems need embedding and vector search depth.
- Strong when attached to production retrieval, indexing, evaluation, and quality regression work.

Weaknesses:

- Vector database keywords are easy to stuff into skill sections.
- A RAG app builder is not necessarily a search infrastructure engineer.

Why:

- Top 100 contains Qdrant 34, Embeddings 33, Weaviate 32, FAISS 31, pgvector 30, Pinecone 27, and Milvus 25.
- V1 keyword-stuffer examples were often vector-search heavy but had only `llm` as career evidence and weak ranking/retrieval history.

## Archetype 5: Evaluation/Relevance Scientist

Expected rank: Elite to High

Core characteristics:

- Titles: Applied Scientist, Search Engineer, ML Engineer, Data Scientist.
- Skills: NDCG, MRR, MAP, A/B testing, offline benchmarks, online metrics, recruiter feedback loops, experiment interpretation.
- Companies: product companies with active ranking or recommendation systems.
- Descriptions: designed evaluation frameworks, tied offline relevance metrics to online outcomes, analyzed ranker changes.
- Behavioral pattern: may not have the loudest skill list, but has high hiring value.

Strengths:

- The JD specifically says the role will set up offline benchmarks, online A/B testing, and recruiter-feedback loops.
- Evaluation experience separates production relevance engineers from demo builders.

Weaknesses:

- Sparse terminology can make these candidates easy to under-rank if V2 only counts exact search keywords.
- Titles often do not reveal the function.

Why:

- The JD states that if a candidate has never thought about rigorous ranking evaluation, the role will be painful.
- V1 report shows Top 100 has many core retrieval/ranking terms, but explanation traces do not yet capture evaluation evidence in enough detail.

## Archetype 6: Applied ML Engineer

Expected rank: Medium to High

Core characteristics:

- Titles: Machine Learning Engineer, Applied ML Engineer, Senior Data Scientist, AI Engineer.
- Skills: PyTorch, TensorFlow, scikit-learn, feature engineering, MLOps, model deployment, MLflow, Kubeflow.
- Companies: product or AI companies.
- Descriptions: production ML models, feature pipelines, model deployment, experimentation, sometimes ranking/retrieval.
- Behavioral pattern: often high recruiter engagement and strong profile completeness.

Strengths:

- Good base for building practical ML systems.
- Strong if career descriptions show ranking, retrieval, recommendation, or evaluation ownership.

Weaknesses:

- Generic production ML is not enough for the JD.
- V1 Top 100 includes many ML-title candidates, so V2 must separate core relevance work from broad ML competence.

Why:

- Top 100 contains 20 Machine Learning title-family candidates and 10 Applied ML title-family candidates.
- Top 10 contains 4 Machine Learning title-family candidates, but these succeed because their career evidence includes ranking/retrieval, not because of title alone.

## Archetype 7: NLP Engineer

Expected rank: Medium to High

Core characteristics:

- Titles: NLP Engineer, Senior NLP Engineer, AI Engineer, ML Engineer.
- Skills: NLP, transformers, sentence transformers, Hugging Face, text encoders, semantic search, embeddings.
- Companies: AI/product companies, conversational AI, language-tech startups.
- Descriptions: text understanding, embeddings, retrieval, semantic search, sometimes reranking.
- Behavioral pattern: can appear strong because NLP terms overlap with retrieval/embedding terms.

Strengths:

- Useful for query understanding, text representations, embeddings, and matching.
- Strong if tied to search/relevance outcomes.

Weaknesses:

- NLP model work alone is adjacent, not primary.
- Conversational AI, ASR/TTS, or generic transformers are not necessarily search/relevance evidence.

Why:

- Top 100 includes 15 NLP-title candidates and many NLP/transformer skills.
- V2 should distinguish NLP-for-search from generic NLP or LLM app work.

## Archetype 8: AI Transition Candidate

Expected rank: Low to Very Low

Core characteristics:

- Titles: Civil Engineer, Accountant, Graphic Designer, Customer Support, Marketing Manager, Operations Manager, Mechanical Engineer.
- Skills: LangChain, RAG, LLMs, vector databases, prompt engineering, embeddings, often with little career support.
- Companies: generic IT services, non-ML business roles, unrelated industries.
- Descriptions: recent self-directed AI projects, courses, demos, or thin LLM integrations.
- Behavioral pattern: can have good market signals but weak career relevance.

Strengths:

- May have practical motivation and availability.
- Could be relevant for junior transition roles, not this senior founding role.

Weaknesses:

- Weak fit for production ranking/search ownership.
- High risk of skill-title mismatch and profile inconsistency.

Why:

- AI-title sample is dominated by non-ML or transition titles: 19 transition/non-ML titles plus Business Analyst, Mechanical Engineer, Project Manager, Frontend Engineer, and only one Recommendation title.
- The JD explicitly says a Marketing Manager with all the AI keywords is not a fit.
- V1 Top 100 has zero AI-transition flags, which is a good baseline behavior to preserve.

## Archetype 9: Keyword Stuffer

Expected rank: Very Low

Core characteristics:

- Titles: often non-search, non-ML, or generic engineering roles.
- Skills: large clusters of AI keywords, vector DBs, LLM tools, and frameworks.
- Companies: mixed.
- Descriptions: little or no production career evidence; repeated or template-like summaries.
- Behavioral pattern: may have high profile completeness and recruiter engagement.

Strengths:

- Skill inventory may contain relevant terms.

Weaknesses:

- Low trust unless career descriptions prove the work.
- Can pollute technical score if V2 counts repeated skill mentions too aggressively.

Why:

- V1 examples of keyword stuffers had final scores around 0.46-0.49, strong vector-search skill evidence, and only weak career evidence such as `llm`.
- V1 Top 100 has zero keyword-stuffer flags.

## Archetype 10: Consulting AI Candidate

Expected rank: Medium to Low

Core characteristics:

- Titles: Consultant, AI Engineer, Data Scientist, Business Analyst, Project Manager, Data Engineer.
- Skills: broad AI/ML, cloud, data, LLM apps, analytics, sometimes search/recommendation.
- Companies: Accenture, TCS, Infosys, Wipro, Capgemini, Cognizant, Deloitte, EY, KPMG, PwC, or service-style organizations.
- Descriptions: client projects, prototypes, migrations, analytics, dashboards, LLM pilots.
- Behavioral pattern: often broad skill coverage; production ownership depth is variable.

Strengths:

- Can have strong implementation breadth and client delivery experience.
- Should rank high when descriptions show ownership of production search/ranking systems.

Weaknesses:

- Consulting-only careers may lack product ownership and long-term relevance feedback loops.
- V1 applies only a small consulting-only penalty, which is appropriate for V1 but should be more nuanced in V2.

Why:

- Forensic comparison shows Consulting is a very large bucket: 72,039 candidates.
- Consulting average skill count is 9.27 versus AI-title average skill count 14.73, and consulting profiles have lower average salary midpoint and profile completeness than AI-title candidates.

## Archetype 11: Generic Data Engineer

Expected rank: Medium to Low

Core characteristics:

- Titles: Data Engineer, Analytics Engineer, Backend/Data hybrid.
- Skills: Spark, Airflow, SQL, dbt, Snowflake, BigQuery, Kafka, Databricks, ETL.
- Companies: IT services, analytics teams, product data platforms.
- Descriptions: data pipelines, feature stores, warehouse modeling, batch/stream processing.
- Behavioral pattern: can be stable and realistic but often lacks direct search relevance.

Strengths:

- Useful for retrieval pipelines, feature generation, data quality, and ML infrastructure.
- Can be a strong supporting signal when paired with search/ranking evidence.

Weaknesses:

- Data pipelines are not enough for a senior AI search/relevance role.
- JD-aligned sampling surfaced backend/data candidates with AI skills but limited direct relevance ownership.

Why:

- A sampled JD-aligned candidate `CAND_0000001` is a Backend Engineer with strong Spark/Airflow/SQL pipeline evidence and ML-transition language, but not a direct search/ranking engineer.

## Archetype 12: Generic Backend Engineer

Expected rank: Low to Medium

Core characteristics:

- Titles: Backend Engineer, Java Developer, Full Stack Developer, Cloud Engineer, DevOps Engineer.
- Skills: APIs, microservices, Java, Go, Node.js, Spring Boot, FastAPI, Docker, Kubernetes.
- Companies: IT services, SaaS, platform teams.
- Descriptions: backend systems, services, cloud infrastructure, APIs, platform operations.
- Behavioral pattern: may be good market candidates but weak technical relevance.

Strengths:

- Search/retrieval systems need production engineering and operational discipline.
- Strong if paired with indexing, search latency, vector DB operations, and relevance evaluation.

Weaknesses:

- Generic backend experience should not outrank proven search/relevance experience.
- Skill-only AI add-ons should be treated cautiously.

Why:

- Random and JD-aligned samples contain many backend/frontend/devops/software titles even when skill lists contain AI terms.
- V2 should recognize backend experience as enabling evidence, not primary relevance evidence.

## Cross-Archetype Conclusions

1. The target candidate is not "AI Engineer" in the abstract. The target is a production search, ranking, retrieval, or recommendation engineer with evidence of shipped systems.
2. Recommendation engineers are valid high-rank candidates only when their work includes ranking, matching, online feedback, or evaluation.
3. Retrieval infrastructure engineers should often outrank generic ML engineers because the first 90 days require improving a BM25/rule-based system and shipping hybrid retrieval/ranking improvements.
4. Evaluation/relevance science is under-expressed in titles but high value in the JD.
5. V2 should demote generic AI/LLM/RAG evidence unless it is attached to production retrieval, ranking, or evaluation.
6. Sample buckets are useful for discovery, not labels. The "JD-aligned" sample contains many non-core titles and appears partly keyword-driven.
