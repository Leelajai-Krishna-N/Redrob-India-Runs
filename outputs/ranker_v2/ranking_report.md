# Ranker V2 Report

## Summary
- Deterministic, explainable scoring only: no LLM calls, embeddings, cross-encoders, external APIs, or neural models.
- V2 replaces the broad V1 technical score with evidence-traced feature families.
- Family weights emphasize search ranking, retrieval infrastructure, evaluation/relevance science, and conditional recommendation/matching evidence.
- Trust is handled mostly with caps and reason-coded penalties, including template repetition.

## Score Distributions
| metric | min | p25 | median | p75 | p95 | max |
| --- | --- | --- | --- | --- | --- | --- |
| search_ranking_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9647 |
| retrieval_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0261 | 0.9693 |
| evaluation_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9952 |
| recommendation_score | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0238 | 0.9558 |
| behavioral_score | 0.1131 | 0.3867 | 0.4580 | 0.5375 | 0.6810 | 0.9802 |
| trust_penalty | 0.0000 | 0.0000 | 0.0500 | 0.0800 | 0.1200 | 0.1200 |
| final_score | 0.0000 | 0.0000 | 0.0000 | 0.0320 | 0.0470 | 0.8210 |

## Evidence-Level Summary
| max_evidence_level | top100_count |
| --- | --- |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 7 |
| 5 | 93 |

## Top 100 Current Titles
- `Recommendation Systems Engineer`: 15
- `Search Engineer`: 12
- `Applied ML Engineer`: 12
- `Machine Learning Engineer`: 11
- `AI Engineer`: 10
- `NLP Engineer`: 10
- `Senior Data Scientist`: 9
- `Senior NLP Engineer`: 6
- `Senior Machine Learning Engineer`: 5
- `Staff Machine Learning Engineer`: 4
- `Senior Applied Scientist`: 2
- `Lead AI Engineer`: 2
- `Senior AI Engineer`: 2

## Top 100 Skills
- `BM25`: 40
- `Elasticsearch`: 37
- `Qdrant`: 37
- `QLoRA`: 36
- `OpenSearch`: 35
- `Embeddings`: 35
- `Weaviate`: 34
- `Learning to Rank`: 34
- `Hugging Face Transformers`: 34
- `Python`: 33
- `LangChain`: 33
- `Sentence Transformers`: 33
- `Recommendation Systems`: 33
- `NLP`: 32
- `scikit-learn`: 31
- `Pinecone`: 30
- `Deep Learning`: 30
- `Semantic Search`: 30
- `Fine-tuning LLMs`: 30
- `Machine Learning`: 30
- `PyTorch`: 30
- `Haystack`: 29
- `Information Retrieval`: 29
- `Vector Search`: 29
- `TensorFlow`: 28
- `pgvector`: 28
- `PEFT`: 27
- `FAISS`: 27
- `LlamaIndex`: 26
- `Prompt Engineering`: 26
- `LoRA`: 26
- `Kubeflow`: 25
- `Weights & Biases`: 25
- `Reinforcement Learning`: 24
- `MLOps`: 23
- `ASR`: 22
- `RAG`: 22
- `Milvus`: 22
- `Forecasting`: 21
- `Time Series`: 21
- `Feature Engineering`: 21
- `OpenCV`: 20
- `Diffusion Models`: 20
- `LLMs`: 20
- `GANs`: 20
- `Data Science`: 19
- `MLflow`: 19
- `Image Classification`: 18
- `Object Detection`: 18
- `TTS`: 17
- `Statistical Modeling`: 17
- `CNN`: 17
- `Computer Vision`: 17
- `YOLO`: 16
- `Speech Recognition`: 15
- `BentoML`: 13
- `Java`: 6
- `Vue.js`: 6
- `Flask`: 5
- `GCP`: 5
- `Photoshop`: 5
- `SQL`: 5
- `Accounting`: 5
- `SAP`: 4
- `SEO`: 4
- `Databricks`: 4
- `Agile`: 4
- `React`: 4
- `Marketing`: 4
- `Node.js`: 4
- `Next.js`: 4
- `Angular`: 4
- `CI/CD`: 3
- `Redux`: 3
- `gRPC`: 3
- `Go`: 3
- `ETL`: 3
- `Excel`: 3
- `REST APIs`: 3
- `BigQuery`: 3
- `Illustrator`: 3
- `JavaScript`: 3
- `Salesforce CRM`: 3
- `Redis`: 3
- `Microservices`: 3
- `Hadoop`: 3
- `Snowflake`: 2
- `Apache Flink`: 2
- `PowerPoint`: 2
- `Figma`: 2
- `dbt`: 2
- `Content Writing`: 2
- `FastAPI`: 2
- `Django`: 2
- `Kubernetes`: 2
- `Spring Boot`: 2
- `Six Sigma`: 1
- `Rust`: 1
- `CSS`: 1
- `Sales`: 1

## Examples: Top-Ranked Candidates
- `CAND_0046064` final=0.8210, search=0.958, retrieval=0.827, eval=0.963: Evidence: Vector search L5 via `embeddings` at Verloop.io / Lead AI Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Evaluation L5 via `ndcg` at Verloop.io / Lead AI Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Search ranking L5 via `candidate-jd matching` at Salesforce / Senior NLP Engineer: Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. | Retrieval L5 via `retrieval` at Verloop.io / Lead AI Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Concerns: trust flags: degree_order_reversal, skills_current_role_mismatch, skills_headline_mismatch
  Evidence: search_ranking:candidate-jd matching@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5
- `CAND_0039754` final=0.8078, search=0.941, retrieval=0.957, eval=0.976: Evidence: Vector search L5 via `embedding` at Meta / Senior Applied Scientist: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Evaluation L5 via `simulated a/b` at Meta / Senior Applied Scientist: After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months. | Retrieval L5 via `retrieval` at Meta / Senior Applied Scientist: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Search ranking L5 via `learning-to-rank` at Meta / Senior Applied Scientist: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... Concerns: trust flags: current_title_description_mismatch, previous_title_description_mismatch, skills_career_history_mismatch
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:re-scoring@L5
- `CAND_0046525` final=0.7860, search=0.850, retrieval=0.885, eval=0.958: Evidence: Evaluation L5 via `a/b testing` at Genpact AI / Senior Machine Learning Engineer: Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. | Vector search L5 via `embedding` at Genpact AI / Senior Machine Learning Engineer: Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. | Retrieval L5 via `index versioning` at Genpact AI / Senior Machine Learning Engineer: Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. | Search ranking L5 via `ranker` at Genpact AI / Senior Machine Learning Engineer: Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system.
  Evidence: search_ranking:ranker@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5
- `CAND_0081846` final=0.7854, search=0.829, retrieval=0.941, eval=0.963: Evidence: Vector search L5 via `embeddings` at Razorpay / Lead AI Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Evaluation L5 via `ndcg` at Razorpay / Lead AI Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Retrieval L5 via `retrieval` at Razorpay / Lead AI Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Search ranking L5 via `learning-to-rank` at Razorpay / Lead AI Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Concerns: trust flags: skills_current_role_mismatch, skills_headline_mismatch
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:ranker@L5
- `CAND_0005260` final=0.7835, search=0.847, retrieval=0.739, eval=0.943: Evidence: Evaluation L5 via `ndcg` at Yellow.ai / Senior NLP Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Vector search L5 via `embeddings` at Yellow.ai / Senior NLP Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Search ranking L5 via `candidate-jd matching` at Netflix / Senior NLP Engineer: Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. | Retrieval L5 via `retrieval` at Yellow.ai / Senior NLP Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight.
  Evidence: search_ranking:candidate-jd matching@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5
- `CAND_0092278` final=0.7782, search=0.948, retrieval=0.739, eval=0.943: Evidence: Vector search L5 via `embeddings` at Microsoft / Senior NLP Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Search ranking L5 via `ranking layer` at Microsoft / Senior NLP Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Evaluation L5 via `ndcg` at Saarthi.ai / Senior NLP Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Recommendation/matching L5 via `recommendation system` at Microsoft / Senior NLP Engineer: Built and shipped a production recommendation system at a marketplace product, going from offline experimentation to live A/B test in 5 months. Concerns: template-like repeated career descriptions; long notice period (90 days); trust flags: template_repetition; score capped at 0.92
  Evidence: search_ranking:ranking layer@L5; search_ranking:re-ranking@L5; search_ranking:ranking layer@L5
- `CAND_0018499` final=0.7743, search=0.965, retrieval=0.920, eval=0.995: Evidence: Evaluation L5 via `ndcg` at Zomato / Senior Machine Learning Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Vector search L5 via `embeddings` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Search ranking L5 via `learning-to-rank` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Retrieval L5 via `retrieval` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Concerns: template-like repeated career descriptions; trust flags: graduation_after_employment_start, template_repetition; score capped at 0.92
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:ranker@L5
- `CAND_0008425` final=0.7687, search=0.829, retrieval=0.872, eval=0.678: Evidence: Vector search L5 via `embedding` at Ola / Senior NLP Engineer: Spent substantial time on the boring-but-critical parts: incremental index refresh, embedding drift monitoring, online/offline metric correlation. | Retrieval L5 via `retrieval` at Ola / Senior NLP Engineer: Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). | Search ranking L5 via `candidate-jd matching` at Zomato / Senior ML Engineer — Search & Ranking: Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. | Evaluation L5 via `ndcg` at Ola / Senior NLP Engineer: The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. Concerns: long notice period (90 days); trust flags: skills_current_role_mismatch, skills_headline_mismatch
  Evidence: search_ranking:candidate-jd matching@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5
- `CAND_0088025` final=0.7577, search=0.928, retrieval=0.836, eval=0.762: Evidence: Vector search L5 via `embedding` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Search ranking L5 via `learning-to-rank` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Retrieval L5 via `retrieval` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Evaluation L5 via `simulated a/b` at Yellow.ai / Staff Machine Learning Engineer: After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months. Concerns: template-like repeated career descriptions; long notice period (90 days); trust flags: template_repetition; score capped at 0.92
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:re-scoring@L5
- `CAND_0055905` final=0.7520, search=0.847, retrieval=0.939, eval=0.958: Evidence: Vector search L5 via `embedding` at Flipkart / Senior Machine Learning Engineer: Spent substantial time on the boring-but-critical parts: incremental index refresh, embedding drift monitoring, online/offline metric correlation. | Evaluation L5 via `ndcg` at Flipkart / Senior Machine Learning Engineer: The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. | Retrieval L5 via `retrieval` at Flipkart / Senior Machine Learning Engineer: Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). | Search ranking L5 via `candidate-jd matching` at Uber / Senior AI Engineer: Fine-tuned LLaMA-2-7B and Mistral-7B variants using LoRA and QLoRA for domain-specific candidate-JD matching. Concerns: trust flags: degree_order_reversal, previous_title_description_mismatch, skills_current_role_mismatch
  Evidence: search_ranking:candidate-jd matching@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5

## Examples: Template-Repetition Caps
- `CAND_0092278` final=0.7782, search=0.948, retrieval=0.739, eval=0.943: Evidence: Vector search L5 via `embeddings` at Microsoft / Senior NLP Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Search ranking L5 via `ranking layer` at Microsoft / Senior NLP Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Evaluation L5 via `ndcg` at Saarthi.ai / Senior NLP Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Recommendation/matching L5 via `recommendation system` at Microsoft / Senior NLP Engineer: Built and shipped a production recommendation system at a marketplace product, going from offline experimentation to live A/B test in 5 months. Concerns: template-like repeated career descriptions; long notice period (90 days); trust flags: template_repetition; score capped at 0.92
  Evidence: search_ranking:ranking layer@L5; search_ranking:re-ranking@L5; search_ranking:ranking layer@L5
- `CAND_0018499` final=0.7743, search=0.965, retrieval=0.920, eval=0.995: Evidence: Evaluation L5 via `ndcg` at Zomato / Senior Machine Learning Engineer: Designed the offline evaluation framework from scratch  NDCG, MRR, recall@K calibrated against online A/B engagement metrics. | Vector search L5 via `embeddings` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Search ranking L5 via `learning-to-rank` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. | Retrieval L5 via `retrieval` at Zomato / Senior Machine Learning Engineer: The architecture combined BM25 + dense retrieval (BGE embeddings, FAISS HNSW) with an LLM-based re-ranker on the top-50, falling back to a learning-to-rank model when latency budget was tight. Concerns: template-like repeated career descriptions; trust flags: graduation_after_employment_start, template_repetition; score capped at 0.92
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:ranker@L5
- `CAND_0088025` final=0.7577, search=0.928, retrieval=0.836, eval=0.762: Evidence: Vector search L5 via `embedding` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Search ranking L5 via `learning-to-rank` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Retrieval L5 via `retrieval` at Yellow.ai / Staff Machine Learning Engineer: Owned the end-to-end ranking pipeline at a recommendations-heavy consumer product: candidate sourcing  embedding generation (using a fine-tuned BGE-large)  Pinecone retrieval  learning-to-rank re-scoring (XGBoost)  behavioral-signal inte... | Evaluation L5 via `simulated a/b` at Yellow.ai / Staff Machine Learning Engineer: After three iterations we landed on a calibration approach using simulated A/B tests that has held up over the last 18 months. Concerns: template-like repeated career descriptions; long notice period (90 days); trust flags: template_repetition; score capped at 0.92
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5; search_ranking:re-scoring@L5
- `CAND_0094759` final=0.7157, search=0.916, retrieval=0.936, eval=0.976: Evidence: Evaluation L5 via `a/b testing` at Meta / Lead AI Engineer: Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. | Vector search L5 via `embedding` at Meta / Lead AI Engineer: Led the migration from keyword-based to embedding-based search across a 30M+ candidate corpus over 8 months. | Retrieval L5 via `index versioning` at Meta / Lead AI Engineer: Most of the engineering effort went into the boring infrastructure: index versioning, embedding versioning, rollback paths, and the dashboards that let recruiters trust the new system. | Search ranking L5 via `ranker` at Meta / Lead AI Engineer: Designed three successive ranker variants and ran them in A/B testing alongside the legacy keyword system. Concerns: template-like repeated career descriptions; trust flags: previous_title_description_mismatch, template_repetition; score capped at 0.92
  Evidence: search_ranking:ranker@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking pipeline@L5
- `CAND_0077337` final=0.7113, search=0.787, retrieval=0.963, eval=0.762: Evidence: Retrieval L5 via `retrieval` at Razorpay / Senior NLP Engineer: Migrated the existing BM25-only retrieval to a hybrid setup combining sparse and dense vectors (sentence-transformers, MPNet-base initially, later fine-tuned BGE-large for our domain). | Vector search L5 via `embeddings` at Paytm / Staff Machine Learning Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Search ranking L5 via `ranking layer` at Paytm / Staff Machine Learning Engineer: The system combined collaborative filtering (matrix factorization), content-based features (TF-IDF + sentence-transformer embeddings), and a behavioral re-ranking layer. | Evaluation L5 via `ndcg` at Razorpay / Senior NLP Engineer: The new system reduced p95 retrieval latency by 60% while improving NDCG@10 by 18% on our held-out eval set. Concerns: template-like repeated career descriptions; trust flags: skills_current_role_mismatch, skills_headline_mismatch, template_repetition; score capped at 0.92
  Evidence: search_ranking:ranking layer@L5; search_ranking:re-ranking@L5; search_ranking:ranker@L5
- `CAND_0018722` final=0.7018, search=0.912, retrieval=0.717, eval=0.935: Evidence: Evaluation L5 via `human judgments` at Unacademy / Machine Learning Engineer: Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. | Search ranking L5 via `learning-to-rank` at Unacademy / Machine Learning Engineer: Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. | Retrieval L4 via `retrieval` at Saarthi.ai / Recommendation Systems Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Vector search L4 via `faiss` at Saarthi.ai / Recommendation Systems Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Concerns: template-like repeated career descriptions; long notice period (90 days); trust flags: current_title_description_mismatch, current_title_evidence_mismatch, skills_current_role_mismatch; score capped at 0.82
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking layer@L5; search_ranking:relevance@L5
- `CAND_0010770` final=0.6980, search=0.865, retrieval=0.899, eval=0.728: Evidence: Retrieval L4 via `retrieval` at Verloop.io / AI Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Search ranking L5 via `ranking model` at Aganitha / Recommendation Systems Engineer: Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. | Vector search L4 via `faiss` at Verloop.io / AI Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Evaluation L5 via `human judgments` at Observe.AI / Senior Data Scientist: Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Concerns: template-like repeated career descriptions; trust flags: current_title_description_mismatch, moderate_career_incoherence, skills_current_role_mismatch; score capped at 0.90
  Evidence: search_ranking:ranking model@L5; search_ranking:learning-to-rank@L5; search_ranking:ranking layer@L5
- `CAND_0050454` final=0.6825, search=0.803, retrieval=0.910, eval=0.762: Evidence: Retrieval L4 via `retrieval` at Rephrase.ai / AI Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Vector search L4 via `faiss` at Rephrase.ai / AI Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Search ranking L5 via `learning-to-rank` at Uber / Machine Learning Engineer: Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. | Evaluation L5 via `human judgments` at Uber / Machine Learning Engineer: Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Concerns: template-like repeated career descriptions; trust flags: template_repetition; score capped at 0.92
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking layer@L5; search_ranking:relevance@L5
- `CAND_0083307` final=0.6529, search=0.914, retrieval=0.693, eval=0.960: Evidence: Evaluation L5 via `human judgments` at Netflix / Machine Learning Engineer: Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. | Search ranking L5 via `learning-to-rank` at Netflix / Machine Learning Engineer: Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. | Vector search L4 via `faiss` at Ola / Machine Learning Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Retrieval L4 via `retrieval` at Ola / Machine Learning Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Concerns: template-like repeated career descriptions; long notice period (120 days); trust flags: current_title_description_mismatch, current_title_evidence_mismatch, skills_current_role_mismatch; score capped at 0.82
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking layer@L5; search_ranking:relevance@L5
- `CAND_0093912` final=0.6524, search=0.914, retrieval=0.693, eval=0.943: Evidence: Evaluation L5 via `human judgments` at Razorpay / Senior Data Scientist: Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. | Search ranking L5 via `learning-to-rank` at Razorpay / Senior Data Scientist: Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. | Retrieval L4 via `retrieval` at Flipkart / Search Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. | Vector search L4 via `faiss` at Flipkart / Search Engineer: Used sentence-transformers (all-MiniLM-L6-v2 initially, later upgraded to bge-base) with FAISS for fast nearest-neighbor retrieval. Concerns: template-like repeated career descriptions; trust flags: moderate_career_incoherence, previous_title_description_mismatch, skills_career_history_mismatch; score capped at 0.90
  Evidence: search_ranking:learning-to-rank@L5; search_ranking:ranking layer@L5; search_ranking:relevance@L5

## Interpretation Notes
- Level 4 and 5 evidence is rewarded more strongly than skill or headline mentions.
- Recommendation evidence is strongest when paired with ranking, retrieval, or evaluation context.
- Vector-search evidence is strongest when attached to retrieval or production context.
- Behavioral score is a tie-breaker-sized feature, not the dominant relevance signal.