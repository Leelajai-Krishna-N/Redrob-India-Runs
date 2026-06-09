# Template Collapse Analysis

## Evidence Template Families

| Template | Count |
| --- | --- |
| Human Judgments + LTR | 86 |
| BM25/Dense Retrieval + Evaluation | 14 |

## Diversity Metrics

| Metric | Value |
| --- | --- |
| Unique evidence template families | 2 |
| Unique current companies | 41 |
| Unique current titles | 13 |
| Unique reasoning signatures | 60 |
| Candidates with template_repetition flag | 33 |
| Repeated raw career-description templates | 10 |

## Top Companies

| Company | Count |
| --- | --- |
| Freshworks | 5 |
| Genpact AI | 4 |
| Razorpay | 4 |
| Sarvam AI | 4 |
| CRED | 4 |
| Zoho | 4 |
| PharmEasy | 4 |
| Meta | 3 |
| Netflix | 3 |
| Microsoft | 3 |
| Flipkart | 3 |
| Rephrase.ai | 3 |
| Nykaa | 3 |
| Mad Street Den | 3 |
| Niramai | 3 |

## Top Titles

| Title | Count |
| --- | --- |
| Recommendation Systems Engineer | 15 |
| Search Engineer | 12 |
| Applied ML Engineer | 12 |
| Machine Learning Engineer | 11 |
| AI Engineer | 10 |
| NLP Engineer | 10 |
| Senior Data Scientist | 9 |
| Senior NLP Engineer | 6 |
| Senior Machine Learning Engineer | 5 |
| Staff Machine Learning Engineer | 4 |
| Senior Applied Scientist | 2 |
| Lead AI Engineer | 2 |
| Senior AI Engineer | 2 |

## Experience Bands

| Band | Count |
| --- | --- |
| 5-7 | 45 |
| 7-9 | 34 |
| <5 | 15 |
| 9+ | 6 |

## Candidate Families

| Family | Count |
| --- | --- |
| Search Ranking Engineer | 43 |
| Recommendation Engineer | 18 |
| Retrieval Engineer | 16 |
| unlabeled/heuristic | 14 |
| Applied ML Engineer | 4 |
| NLP Engineer | 3 |
| Evaluation/Relevance Engineer | 2 |

## Repeated Career Descriptions

| Count | Description |
| --- | --- |
| 69 | owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over N months. designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. most of the work was infrastructure and data quality - the modeling part was almost the easy bit. final model improved revenue-per-search by N%. |
| 52 | developed a semantic search feature for an internal knowledge base of ~Nk documents. used sentence-transformers (all-minilm-lN-vN initially, later upgraded to bge-base) with faiss for fast nearest-neighbor retrieval. designed the query expansion module that handles vocabulary mismatch between user queries and document terms. reported search-relevance improvement of N% over the prior elasticsearch bmN setup, validated through human relevance judgments. |
| 29 | built a content recommendation system serving Nm+ users that combined collaborative filtering with content-based ranking. the system uses item-item similarity (via sentence-transformer embeddings) for cold starts and a gradient-boosted model trained on engagement signals for warm users. most of my time went into the feature pipeline (~N features) and the a/b testing infrastructure. the launch improved N-day retention by N% and time spent per session by N%. |
| 28 | implemented a rag-based customer support chatbot integrated with our existing ticketing system. built the document ingestion pipeline (chunking, embedding via openai embeddings, storing in pinecone) and the answer-generation layer (initially gpt-N, then a fine-tuned smaller model for cost control). designed the evaluation framework with both automatic metrics (bleu, rouge) and human-in-the-loop quality scores. deployment cut average ticket resolution time by N% for the supported categories. |
| 27 | trained and shipped multiple ranking models for our product's discovery feed using xgboost and lightgbm. designed features across three families: content metadata, user behavior signals, and item engagement history. owned the offline-online correlation analysis that determined which offline metrics actually predicted a/b test outcomes. worked closely with pms to define the optimization target (click-through vs. dwell time vs. downstream conversion) - that work was as important as the modeling... |
| 22 | built and operated production ml pipelines using mlflow for experiment tracking, kubeflow for orchestration, and our internal feature store. my main project was a churn prediction model that's now used by the customer success team to prioritize outreach. designed the model monitoring stack: data drift detection, prediction distribution checks, and alerting. mentored a junior engineer through their first end-to-end ml project last year. |
| 12 | fine-tuned llama-N-Nb and mistral-Nb variants using lora and qlora for domain-specific candidate-jd matching. built the data curation pipeline that generated Nk high-quality preference pairs from recruiter labels, plus the eval harness using both ranking metrics and human-quality scores. deployed the model via bentoml on kubernetes with sub-Nms pN latency by quantizing to intN and batching at the request level. cost per inference dropped from $N with gpt-N-fallback to under $N. |
| 12 | built a rag-based ranking pipeline serving Nm+ queries per month for an internal recruiter-facing search product. the architecture combined bmN + dense retrieval (bge embeddings, faiss hnsw) with an llm-based re-ranker on the top-N, falling back to a learning-to-rank model when latency budget was tight. designed the offline evaluation framework from scratch - ndcg, mrr, recall@k calibrated against online a/b engagement metrics. drove the migration over N months including the recruiter-feedbac... |

## Answers

1. Yes, V2 selects near-duplicates: 33 Top 100 candidates have the explicit template_repetition flag, and repeated raw career descriptions appear across the set.
2. Yes, the ranker partially overfits to high-value relevance archetypes, especially Human Judgments + LTR and Recommendation + Ranking/Evaluation.
3. Increasing diversity would likely improve leaderboard performance only if done through evidence de-duplication/source-diversity caps, not through arbitrary title/company quotas.
