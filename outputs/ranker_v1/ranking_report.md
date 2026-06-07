# Ranker V1 Report

## Summary
- Deterministic, explainable scoring only: no LLM calls, embeddings, cross-encoders, external APIs, or neural models.
- Scoring principle: when skill keywords conflict with demonstrated career evidence, career evidence is trusted more heavily.
- Final score = 45% technical relevance + 25% career evidence + 20% market signal + 10% consistency, minus transparent calibration penalties.

## Score Distributions
| metric              |    min |    p25 |   median |    p75 |    p95 |    max |
|:--------------------|-------:|-------:|---------:|-------:|-------:|-------:|
| technical_score     | 0      | 0      |   0.0424 | 0.0707 | 0.4571 | 0.9966 |
| market_score        | 0.1165 | 0.3894 |   0.4615 | 0.5456 | 0.7053 | 0.9954 |
| consistency_penalty | 0      | 0      |   0      | 0      | 0.4667 | 1      |
| final_score         | 0.0709 | 0.2014 |   0.2374 | 0.29   | 0.3911 | 0.9745 |

## Top 100 Current Titles
- `Recommendation Systems Engineer`: 16
- `Senior Data Scientist`: 11
- `Machine Learning Engineer`: 11
- `Applied ML Engineer`: 10
- `Search Engineer`: 10
- `NLP Engineer`: 9
- `AI Engineer`: 9
- `Senior NLP Engineer`: 6
- `Senior Machine Learning Engineer`: 5
- `Staff Machine Learning Engineer`: 4
- `Senior Applied Scientist`: 4
- `Senior AI Engineer`: 3
- `Lead AI Engineer`: 2

## Top 100 Skills
- `QLoRA`: 40
- `BM25`: 39
- `Recommendation Systems`: 36
- `OpenSearch`: 36
- `Elasticsearch`: 35
- `LangChain`: 35
- `Qdrant`: 34
- `Hugging Face Transformers`: 34
- `Embeddings`: 33
- `NLP`: 33
- `Learning to Rank`: 32
- `scikit-learn`: 32
- `Deep Learning`: 32
- `Weaviate`: 32
- `FAISS`: 31
- `pgvector`: 30
- `Python`: 30
- `TensorFlow`: 30
- `Haystack`: 30
- `Information Retrieval`: 29
- `Prompt Engineering`: 29
- `Sentence Transformers`: 29
- `Vector Search`: 28
- `Semantic Search`: 28
- `LoRA`: 28
- `PyTorch`: 27
- `Pinecone`: 27
- `Fine-tuning LLMs`: 27
- `Machine Learning`: 26
- `Milvus`: 25
- `PEFT`: 25
- `LlamaIndex`: 24
- `Weights & Biases`: 24
- `Kubeflow`: 24
- `ASR`: 23
- `GANs`: 23
- `Feature Engineering`: 23
- `RAG`: 22
- `Reinforcement Learning`: 22
- `Time Series`: 22
- `Forecasting`: 21
- `MLOps`: 21
- `MLflow`: 21
- `Data Science`: 20
- `Diffusion Models`: 20
- `LLMs`: 19
- `OpenCV`: 19
- `Image Classification`: 18
- `Object Detection`: 18
- `Computer Vision`: 18
- `TTS`: 17
- `CNN`: 17
- `BentoML`: 16
- `Statistical Modeling`: 15
- `Speech Recognition`: 15
- `YOLO`: 13
- `Flask`: 7
- `Java`: 7
- `Vue.js`: 6
- `SEO`: 6
- `Accounting`: 5
- `GCP`: 5
- `Node.js`: 5
- `SAP`: 4
- `Photoshop`: 4
- `Excel`: 4
- `Illustrator`: 4
- `SQL`: 4
- `Databricks`: 4
- `Marketing`: 4
- `Redux`: 3
- `Go`: 3
- `FastAPI`: 3
- `Next.js`: 3
- `BigQuery`: 3
- `PowerPoint`: 3
- `Search & Discovery`: 3
- `Information Retrieval Systems`: 3
- `REST APIs`: 3
- `Text Encoders`: 3
- `Model Adaptation`: 3
- `Terraform`: 3
- `Angular`: 3
- `Kubernetes`: 3
- `Spring Boot`: 3
- `Agile`: 3
- `CI/CD`: 2
- `Snowflake`: 2
- `JavaScript`: 2
- `Salesforce CRM`: 2
- `Apache Flink`: 2
- `ETL`: 2
- `Search Backend`: 2
- `Tally`: 2
- `Search Infrastructure`: 2
- `Redis`: 2
- `Microservices`: 2
- `Content Writing`: 2
- `CSS`: 2
- `Hadoop`: 2

## Examples: Top-Ranked Candidates
- `CAND_0081846` final=0.9745, tech=0.986, career=1.000, market=0.954: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (bm25, retrieval); 2 relevant roles with 79 months of supporting experience
  Career evidence terms: `bm25`, `retrieval`, `embedding`, `ranking`
- `CAND_0088025` final=0.9732, tech=0.967, career=1.000, market=0.940: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (retrieval); 3 relevant roles with 102 months of supporting experience | Concerns: longer notice period (90 days)
  Career evidence terms: `embedding`, `ranking`, `retrieval`, `pinecone`
- `CAND_0046525` final=0.9705, tech=0.972, career=0.974, market=0.947: Positives: career evidence for ranking/relevance systems (ranker, ranking); career evidence for retrieval/search systems (bm25, retrieval); 2 relevant roles with 73 months of supporting experience
  Career evidence terms: `ranker`, `embedding`, `ranking`, `reranking`
- `CAND_0010685` final=0.9677, tech=0.957, career=1.000, market=0.969: Positives: career evidence for ranking/relevance systems (ranking, relevance); career evidence for retrieval/search systems (semantic search, elasticsearch); 3 relevant roles with 51 months of supporting experience
  Career evidence terms: `ranking`, `relevance`, `semantic search`, `elasticsearch`
- `CAND_0077337` final=0.9643, tech=0.978, career=1.000, market=0.921: Positives: career evidence for ranking/relevance systems (ranker, ranking); career evidence for retrieval/search systems (semantic search, bm25); 4 relevant roles with 83 months of supporting experience
  Career evidence terms: `embedding`, `ranker`, `ranking`, `embeddings`
- `CAND_0039754` final=0.9638, tech=0.995, career=1.000, market=0.981: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (retrieval, bm25); 3 relevant roles with 98 months of supporting experience | Concerns: profile consistency concerns
  Career evidence terms: `ranking`, `retrieval`, `embedding`, `bm25`
- `CAND_0050454` final=0.9621, tech=0.977, career=1.000, market=0.863: Positives: career evidence for ranking/relevance systems (relevance, ranking); career evidence for retrieval/search systems (semantic search, elasticsearch); 3 relevant roles with 81 months of supporting experience
  Career evidence terms: `relevance`, `semantic search`, `elasticsearch`, `bm25`
- `CAND_0018499` final=0.9594, tech=0.997, career=1.000, market=0.855: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (bm25, retrieval); 3 relevant roles with 86 months of supporting experience
  Career evidence terms: `ranking`, `ranker`, `reranking`, `bm25`
- `CAND_0091534` final=0.9590, tech=0.937, career=1.000, market=0.937: Positives: career evidence for ranking/relevance systems (relevance, ranking); career evidence for retrieval/search systems (semantic search, elasticsearch); 3 relevant roles with 85 months of supporting experience
  Career evidence terms: `relevance`, `ranking`, `semantic search`, `elasticsearch`
- `CAND_0046064` final=0.9585, tech=0.986, career=1.000, market=0.941: Positives: career evidence for ranking/relevance systems (ranking, ranker); career evidence for retrieval/search systems (retrieval, bm25); 3 relevant roles with 106 months of supporting experience
  Career evidence terms: `ranking`, `retrieval`, `embedding`, `ranker`

## Examples: AI-Transition Candidates
- `CAND_0038821` final=0.4545, tech=0.503, career=0.085, market=0.835: Positives: product/SaaS company experience; strong recruiter engagement and availability signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history; longer notice period (120 days)
- `CAND_0023088` final=0.4535, tech=0.586, career=0.057, market=0.679: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0000541` final=0.4508, tech=0.598, career=0.100, market=0.584: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0082718` final=0.4499, tech=0.582, career=0.087, market=0.630: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0078518` final=0.4487, tech=0.598, career=0.100, market=0.574: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history; longer notice period (90 days)
- `CAND_0052370` final=0.4477, tech=0.610, career=0.100, market=0.542: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0065748` final=0.4444, tech=0.582, career=0.100, market=0.586: Positives: detected vector-search evidence (embeddings, embedding); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0031542` final=0.4425, tech=0.588, career=0.078, market=0.591: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history
- `CAND_0045984` final=0.4417, tech=0.595, career=0.040, market=0.620: Positives: detected vector-search evidence (embeddings, embedding); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history; longer notice period (120 days)
- `CAND_0053258` final=0.4411, tech=0.585, career=0.032, market=0.649: Positives: detected vector-search evidence (embeddings, embedding); solid market engagement signals | Concerns: limited ranking/relevance career evidence; AI-transition pattern without meaningful AI work history; longer notice period (90 days)

## Examples: Keyword Stuffers
- `CAND_0072547` final=0.4887, tech=0.580, career=0.364, market=0.884: Positives: detected vector-search evidence (embeddings, embedding); product/SaaS company experience; strong recruiter engagement and availability signals | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence; longer notice period (90 days)
  Career evidence terms: `llm`
- `CAND_0015425` final=0.4869, tech=0.621, career=0.522, market=0.485: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 48 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence
  Career evidence terms: `llm`
- `CAND_0011125` final=0.4866, tech=0.619, career=0.382, market=0.662: Positives: detected vector-search evidence (embeddings, embedding); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence; longer notice period (120 days)
  Career evidence terms: `llm`
- `CAND_0002623` final=0.4804, tech=0.661, career=0.559, market=0.317: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 58 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence
  Career evidence terms: `llm`
- `CAND_0075010` final=0.4767, tech=0.567, career=0.530, market=0.546: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 50 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence
  Career evidence terms: `llm`
- `CAND_0012514` final=0.4640, tech=0.650, career=0.493, market=0.340: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 40 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence
  Career evidence terms: `llm`
- `CAND_0068512` final=0.4598, tech=0.623, career=0.479, market=0.398: Positives: detected vector-search evidence (vector search, embeddings); 2 relevant roles with 36 months of supporting experience; product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence; longer notice period (90 days)
  Career evidence terms: `llm`
- `CAND_0037426` final=0.4580, tech=0.608, career=0.382, market=0.543: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence; longer notice period (90 days)
  Career evidence terms: `llm`
- `CAND_0091652` final=0.4578, tech=0.608, career=0.382, market=0.542: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence
  Career evidence terms: `llm`
- `CAND_0055164` final=0.4569, tech=0.608, career=0.327, market=0.606: Positives: detected vector-search evidence (vector search, embeddings); product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; many AI skills but little supporting career evidence; longer notice period (150 days)
  Career evidence terms: `llm`

## Examples: Heavily Penalized Candidates
- `CAND_0051966` final=0.0976, tech=0.000, career=0.100, market=0.363: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
- `CAND_0093725` final=0.1654, tech=0.064, career=0.261, market=0.355: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  Career evidence terms: `llm`
- `CAND_0095238` final=0.1269, tech=0.000, career=0.100, market=0.510: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
- `CAND_0038005` final=0.1241, tech=0.000, career=0.100, market=0.496: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days); severe profile consistency concerns
- `CAND_0068696` final=0.2073, tech=0.064, career=0.327, market=0.482: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days); severe profile consistency concerns
  Career evidence terms: `llm`
- `CAND_0000470` final=0.1216, tech=0.000, career=0.100, market=0.483: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
- `CAND_0052329` final=0.2220, tech=0.064, career=0.316, market=0.569: Positives: product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns
  Career evidence terms: `llm`
- `CAND_0047637` final=0.0709, tech=0.000, career=0.100, market=0.229: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days); severe profile consistency concerns
- `CAND_0055617` final=0.4241, tech=0.594, career=0.327, market=0.357: Positives: detected vector-search evidence (embeddings, embedding); product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (150 days); severe profile consistency concerns
  Career evidence terms: `llm`
- `CAND_0021167` final=0.1354, tech=0.000, career=0.100, market=0.535: Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; severe profile consistency concerns

## Interpretation Notes
- Tier A ranking/relevance evidence carries the largest technical weight.
- Career descriptions carry more weight than summaries, skills, headlines, or titles.
- Keyword stuffer and AI-transition penalties are modest but visible in `calibration_penalty`.
- Severe forensic issues cap the final score; they do not remove candidates.