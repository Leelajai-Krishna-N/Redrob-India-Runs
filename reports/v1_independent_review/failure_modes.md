# Failure Mode Discovery

These are audit heuristics, not ground-truth judgments.
## A. Candidates Potentially Ranked Too High

- `CAND_0037566` rank=106, final=0.8482, tech=0.838, career=0.785, market=0.891, consistency_penalty=0.033, title=`Machine Learning Engineer`
  - Why it happened: no direct career ranking evidence, consistency_points=1, very strong market score. Reasoning: Positives: detected vector-search evidence (pinecone, embeddings); 2 relevant roles with 82 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence
  - Career path: Machine Learning Engineer -> Machine Learning Engineer
  - Skills sample: Pinecone, Time Series, LlamaIndex, NLP, LoRA, QLoRA, BM25, Feature Engineering
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0074735` rank=134, final=0.8099, tech=0.860, career=0.623, market=0.869, consistency_penalty=0.067, title=`Applied ML Engineer`
  - Why it happened: no direct career ranking evidence, consistency_points=2, very strong market score. Reasoning: Positives: detected vector-search evidence (embeddings, embedding); 2 relevant roles with 43 months of supporting experience; strong recruiter engagement and availability signals | Concerns: limited ranking/relevance career evidence; longer notice period (90 days)
  - Career path: Applied ML Engineer -> Search Engineer -> NLP Engineer
  - Skills sample: YOLO, RAG, Prompt Engineering, LlamaIndex, Machine Learning, Weaviate, GANs, ASR
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0015578` rank=146, final=0.7924, tech=0.801, career=0.736, market=0.773, consistency_penalty=0.067, title=`AI Engineer`
  - Why it happened: no direct career ranking evidence, consistency_points=2. Reasoning: Positives: detected vector-search evidence (embeddings, embedding); 2 relevant roles with 64 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days)
  - Career path: AI Engineer -> Search Engineer
  - Skills sample: Diffusion Models, Embeddings, NLP, Data Science, Kafka, Speech Recognition, MLflow, BM25
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0051004` rank=152, final=0.7837, tech=0.829, career=0.636, market=0.758, consistency_penalty=0.000, title=`Senior Data Scientist`
  - Why it happened: no direct career ranking evidence. Reasoning: Positives: detected vector-search evidence (embedding, embeddings); 2 relevant roles with 56 months of supporting experience; strong recruiter engagement and availability signals | Concerns: limited ranking/relevance career evidence
  - Career path: Senior Data Scientist -> NLP Engineer
  - Skills sample: MLflow, Embeddings, Semantic Search, PyTorch, gRPC, ASR, Reinforcement Learning, Docker
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0052328` rank=179, final=0.7393, tech=0.733, career=0.565, market=0.941, consistency_penalty=0.200, title=`Recommendation Systems Engineer`
  - Why it happened: no direct career ranking evidence, consistency_points=6, very strong market score. Reasoning: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; strong recruiter engagement and availability signals | Concerns: limited ranking/relevance career evidence
  - Career path: Recommendation Systems Engineer -> Senior Data Scientist
  - Skills sample: Object Detection, LoRA, OpenSearch, Reinforcement Learning, QLoRA, Image Classification, Recommendation Systems, ASR
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0039754` rank=6, final=0.9638, tech=0.995, career=1.000, market=0.981, consistency_penalty=0.300, title=`Senior Applied Scientist`
  - Why it happened: consistency_points=9, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (retrieval, bm25); 3 relevant roles with 98 months of supporting experience | Concerns: profile consistency concerns
  - Career path: Senior Applied Scientist -> Senior ML Engineer — Search & Ranking -> Senior Applied Scientist
  - Skills sample: Fine-tuning LLMs, LlamaIndex, Qdrant, Reinforcement Learning, NLP, Statistical Modeling, Kubeflow, ASR
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0055992` rank=18, final=0.9454, tech=0.985, career=1.000, market=0.927, consistency_penalty=0.333, title=`AI Engineer`
  - Why it happened: consistency_points=10, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (relevance, ranking); career evidence for retrieval/search systems (semantic search, elasticsearch); 4 relevant roles with 80 months of supporting experience | Concerns: profile consistency concerns
  - Career path: AI Engineer -> Senior Data Scientist -> AI Engineer -> Machine Learning Engineer
  - Skills sample: Information Retrieval, MLflow, FAISS, RAG, Feature Engineering, Data Science, LangChain, SQL
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0055905` rank=21, final=0.9412, tech=0.985, career=1.000, market=0.889, consistency_penalty=0.300, title=`Senior Machine Learning Engineer`
  - Why it happened: consistency_points=9, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (bm25, retrieval); 3 relevant roles with 96 months of supporting experience | Concerns: profile consistency concerns
  - Career path: Senior Machine Learning Engineer -> Senior AI Engineer -> Senior Applied Scientist
  - Skills sample: Elasticsearch, ASR, Hugging Face Transformers, Haystack, Speech Recognition, LangChain, Python, LLMs
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0081686` rank=22, final=0.9409, tech=0.953, career=1.000, market=0.943, consistency_penalty=0.267, title=`Search Engineer`
  - Why it happened: consistency_points=8, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, relevance); career evidence for retrieval/search systems (semantic search, elasticsearch); 3 relevant roles with 71 months of supporting experience | Concerns: profile consistency concerns
  - Career path: Search Engineer -> Recommendation Systems Engineer -> AI Engineer
  - Skills sample: Machine Learning, Kubeflow, Embeddings, FAISS, Feature Engineering, OpenCV, Milvus, BigQuery
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0041669` rank=38, final=0.9304, tech=0.938, career=1.000, market=0.942, consistency_penalty=0.300, title=`Recommendation Systems Engineer`
  - Why it happened: consistency_points=9, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, relevance); 3 relevant roles with 95 months of supporting experience; product/SaaS company experience | Concerns: profile consistency concerns
  - Career path: Recommendation Systems Engineer -> Search Engineer -> NLP Engineer
  - Skills sample: FAISS, Milvus, PEFT, Diffusion Models, MLflow, QLoRA, Haystack, Semantic Search
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0040887` rank=49, final=0.9219, tech=0.914, career=0.884, market=0.966, consistency_penalty=0.033, title=`Machine Learning Engineer`
  - Why it happened: consistency_points=1, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (relevance); career evidence for retrieval/search systems (semantic search, elasticsearch); 2 relevant roles with 55 months of supporting experience
  - Career path: Machine Learning Engineer -> AI Engineer
  - Skills sample: Reinforcement Learning, Computer Vision, SEO, FAISS, MLflow, LoRA, LangChain, Python
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.
- `CAND_0079064` rank=57, final=0.9111, tech=0.908, career=0.861, market=0.936, consistency_penalty=0.000, title=`Senior Data Scientist`
  - Why it happened: very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (relevance); career evidence for retrieval/search systems (semantic search, elasticsearch); 2 relevant roles with 62 months of supporting experience | Concerns: longer notice period (120 days)
  - Career path: Senior Data Scientist -> NLP Engineer
  - Skills sample: Illustrator, LlamaIndex, OpenSearch, NLP, ASR, Semantic Search, Node.js, Fine-tuning LLMs
  - Likely root cause: V1 may over-reward adjacent recommender/AI evidence, strong market signals, or saturated career evidence before distinguishing exact search relevance ownership.

## B. Candidates Potentially Ranked Too Low

- `CAND_0024466` rank=178, final=0.7413, tech=0.812, career=0.889, market=0.402, consistency_penalty=0.267, title=`Search Engineer`
  - Why it happened: consistency_points=8. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, relevance); 2 relevant roles with 62 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (120 days); profile consistency concerns
  - Career path: Search Engineer -> Recommendation Systems Engineer
  - Skills sample: Recommendation Systems, pgvector, Image Classification, Reinforcement Learning, BM25, MLOps, Computer Vision, Forecasting
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0009024` rank=147, final=0.7888, tech=0.805, career=0.820, market=0.709, consistency_penalty=0.200, title=`Search Engineer`
  - Why it happened: consistency_points=6. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 61 months of supporting experience; product/SaaS company experience
  - Career path: Search Engineer -> Applied ML Engineer
  - Skills sample: YOLO, Qdrant, dbt, CSS, PEFT, FAISS, Machine Learning, Airflow
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0098846` rank=144, final=0.7963, tech=0.756, career=0.794, market=0.837, consistency_penalty=0.100, title=`AI Engineer`
  - Why it happened: consistency_points=3, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, relevance); 2 relevant roles with 44 months of supporting experience; product/SaaS company experience
  - Career path: AI Engineer -> Machine Learning Engineer -> Search Engineer -> Search Engineer
  - Skills sample: YOLO, Kubeflow, Hugging Face Transformers, Hadoop, PEFT, QLoRA, Machine Learning, MLOps
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0067643` rank=143, final=0.7990, tech=0.764, career=0.928, market=0.666, consistency_penalty=0.100, title=`AI Research Engineer`
  - Why it happened: consistency_points=3. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 3 relevant roles with 71 months of supporting experience; product/SaaS company experience
  - Career path: AI Research Engineer -> AI Specialist -> Data Scientist
  - Skills sample: Elasticsearch, Object Detection, Fine-tuning LLMs, Apache Beam, Scrum, OpenCV, Learning to Rank, Salesforce CRM
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0030031` rank=141, final=0.8014, tech=0.787, career=0.754, market=0.911, consistency_penalty=0.233, title=`AI Engineer`
  - Why it happened: consistency_points=7, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 40 months of supporting experience; product/SaaS company experience
  - Career path: AI Engineer -> Senior Data Scientist -> Search Engineer
  - Skills sample: Information Retrieval, PyTorch, Object Detection, Python, NLP, RAG, OpenCV, LoRA
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0096142` rank=140, final=0.8049, tech=0.752, career=0.799, market=0.851, consistency_penalty=0.033, title=`Applied ML Engineer`
  - Why it happened: consistency_points=1, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 60 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (120 days)
  - Career path: Applied ML Engineer -> Applied ML Engineer
  - Skills sample: Kubeflow, LoRA, Weaviate, Pinecone, Python, CSS, BentoML, Weights & Biases
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0010257` rank=139, final=0.8060, tech=0.753, career=0.757, market=0.888, consistency_penalty=0.000, title=`Senior Data Scientist`
  - Why it happened: very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 40 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (120 days)
  - Career path: Senior Data Scientist -> Search Engineer -> Senior Data Scientist
  - Skills sample: Milvus, TensorFlow, MLflow, Python, Forecasting, OpenSearch, Qdrant, JavaScript
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0013536` rank=138, final=0.8062, tech=0.752, career=0.763, market=0.919, consistency_penalty=0.067, title=`Applied ML Engineer`
  - Why it happened: consistency_points=2, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 56 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (90 days)
  - Career path: Applied ML Engineer -> Recommendation Systems Engineer
  - Skills sample: PyTorch, Prompt Engineering, LLMs, NLP, Embeddings, QLoRA, Pinecone, Elasticsearch
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0091909` rank=133, final=0.8104, tech=0.758, career=0.835, market=0.802, consistency_penalty=0.000, title=`Machine Learning Engineer`
  - Why it happened: very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 82 months of supporting experience; product/SaaS company experience
  - Career path: Machine Learning Engineer -> NLP Engineer
  - Skills sample: LLMs, Image Classification, Pinecone, Diffusion Models, QLoRA, Qdrant, OpenSearch, BentoML
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0011162` rank=131, final=0.8119, tech=0.844, career=0.802, market=0.775, consistency_penalty=0.233, title=`Recommendation Systems Engineer`
  - Why it happened: consistency_points=7. Reasoning: Positives: career evidence for ranking/relevance systems (ranking, relevance); 2 relevant roles with 40 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (90 days)
  - Career path: Recommendation Systems Engineer -> Recommendation Systems Engineer -> Machine Learning Engineer
  - Skills sample: Weights & Biases, FAISS, Vector Search, LangChain, CNN, LoRA, Milvus, OpenSearch
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0083879` rank=130, final=0.8165, tech=0.794, career=0.805, market=0.872, consistency_penalty=0.167, title=`Machine Learning Engineer`
  - Why it happened: consistency_points=5, very strong market score. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 65 months of supporting experience; product/SaaS company experience
  - Career path: Machine Learning Engineer -> Search Engineer -> Senior Data Scientist
  - Skills sample: MLOps, Fine-tuning LLMs, Milvus, Image Classification, Data Science, scikit-learn, Hugging Face Transformers, Prompt Engineering
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.
- `CAND_0060072` rank=128, final=0.8186, tech=0.901, career=0.892, market=0.602, consistency_penalty=0.300, title=`Staff Machine Learning Engineer`
  - Why it happened: consistency_points=9. Reasoning: Positives: career evidence for ranking/relevance systems (ranking); 2 relevant roles with 68 months of supporting experience; product/SaaS company experience | Concerns: longer notice period (90 days); profile consistency concerns
  - Career path: Staff Machine Learning Engineer -> Senior Applied Scientist
  - Skills sample: Deep Learning, Sentence Transformers, PyTorch, Feature Engineering, Milvus, Fine-tuning LLMs, Next.js, BM25
  - Likely root cause: Strong technical/career evidence can fall below Top 100 when market score is weaker, consistency penalties apply, or career score saturation makes small differences decisive.

## C. Suspicious Candidates That Escaped Into Relatively High Ranks

- `CAND_0032092` rank=376, final=0.6248, tech=0.658, career=0.731, market=0.530, consistency_penalty=0.600, title=`Civil Engineer`
  - Why it happened: no direct career ranking evidence, consistency_points=18, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (embeddings, embedding); 3 relevant roles with 80 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  - Career path: Civil Engineer -> Accountant -> Accountant -> Marketing Manager -> Project Manager
  - Skills sample: Microservices, CI/CD, SAP, Next.js, Photoshop, MongoDB, Webpack, Node.js
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.
- `CAND_0044503` rank=385, final=0.6229, tech=0.668, career=0.735, market=0.509, consistency_penalty=0.633, title=`Customer Support`
  - Why it happened: no direct career ranking evidence, consistency_points=19, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (vector search, embeddings); 3 relevant roles with 105 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  - Career path: Customer Support -> Sales Executive -> Customer Support -> Accountant -> Civil Engineer
  - Skills sample: Microservices, Agile, BigQuery, Kafka, Azure, Tally, Excel, Data Pipelines
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.
- `CAND_0087548` rank=501, final=0.5988, tech=0.690, career=0.733, market=0.342, consistency_penalty=0.633, title=`Accountant`
  - Why it happened: no direct career ranking evidence, consistency_points=19, weak market score, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (vector search, embeddings); 3 relevant roles with 93 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days); severe profile consistency concerns
  - Career path: Accountant -> Sales Executive -> Project Manager -> HR Manager -> Mechanical Engineer
  - Skills sample: FastAPI, Sales, Docker, PowerPoint, Excel, Angular, JavaScript, Embeddings
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.
- `CAND_0034735` rank=660, final=0.5714, tech=0.645, career=0.603, market=0.485, consistency_penalty=0.667, title=`Operations Manager`
  - Why it happened: no direct career ranking evidence, consistency_points=20, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (embeddings, embedding); 2 relevant roles with 70 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  - Career path: Operations Manager -> Mechanical Engineer -> Civil Engineer -> Operations Manager
  - Skills sample: Apache Beam, Salesforce CRM, GraphQL, Next.js, Kafka, Go, Illustrator, Webpack
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.
- `CAND_0085766` rank=737, final=0.5623, tech=0.558, career=0.690, market=0.509, consistency_penalty=0.633, title=`Graphic Designer`
  - Why it happened: no direct career ranking evidence, consistency_points=19, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (vector search); 3 relevant roles with 61 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  - Career path: Graphic Designer -> Business Analyst -> HR Manager -> Content Writer -> Operations Manager
  - Skills sample: ETL, JavaScript, Databricks, Sales, CI/CD, Microservices, SAP, dbt
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.
- `CAND_0001147` rank=860, final=0.5474, tech=0.645, career=0.584, market=0.404, consistency_penalty=0.700, title=`Sales Executive`
  - Why it happened: no direct career ranking evidence, consistency_points=21, score_cap=0.84. Reasoning: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 65 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (120 days); severe profile consistency concerns
  - Career path: Sales Executive -> Civil Engineer -> Operations Manager -> Accountant -> Customer Support
  - Skills sample: Tailwind, Sales, PowerPoint, Tally, Docker, Apache Flink, Agile, Data Pipelines
  - Likely root cause: Consistency penalties cap scores but may still allow technically strong suspicious profiles to rank relatively high.

## D. Strong Candidates Suppressed

No clear examples found under this audit heuristic.

## Cross-Cutting Root Causes

- `career_score` saturation makes top-tail candidates hard to distinguish by depth.
- Recommendation-system evidence is not separated from direct search/relevance evidence.
- Consistency coverage is incomplete; missing forensic coverage is treated as clean.
- Reasoning does not expose enough source-level evidence to quickly validate borderline cases.