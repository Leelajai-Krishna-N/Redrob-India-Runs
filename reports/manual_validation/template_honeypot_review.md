# Template Honeypot Review

| Template Family | Family Size | Representative Candidates | Repeated Snippets | Repeated Career Descriptions | Repeated Evidence Traces |
| --- | --- | --- | --- | --- | --- |
| Human Judgments + LTR | 86 | CAND_0018499, CAND_0086022, CAND_0077337, CAND_0069905, CAND_0086151, CAND_0050876 | designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeli... / used sentence-transformers (all-minilm-lN-vN initially, later upgraded to bge-base) with faiss for fast nearest-neigh... | Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learnin... / Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (al... | recommendation:recommendation system (186), retrieval:retrieval (167), vector_search:embedding (163), recommendation:recommendation systems (162), search_ranking:learning-to-rank (110) |
| BM25/Dense Retrieval + Evaluation | 14 | CAND_0001610, CAND_0079064, CAND_0058575, CAND_0096172, CAND_0080766, CAND_0044883 | used sentence-transformers (all-minilm-lN-vN initially, later upgraded to bge-base) with faiss for fast nearest-neigh... / reported search-relevance improvement of N% over the prior elasticsearch bmN setup, validated through human relevance... | Developed a semantic search feature for an internal knowledge base of ~500K documents. Used sentence-transformers (al... / Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed fea... | recommendation:recommendation system (33), recommendation:recommendation systems (28), retrieval:retrieval (28), retrieval:semantic search (24), vector_search:faiss (20) |

## Answers

1. Unique candidate families in Top 100: 2.
2. Near-duplicate candidates by V2 `template_repetition` flag: 33.
3. V2 still over-rewards some repeated families, especially Human Judgments + LTR and Recommendation + Ranking/Evaluation templates. The trust cap reduces but does not fully eliminate their presence in the Top 100.

## Judge's Read

This is the largest residual risk. V2 correctly found high-value search/evaluation patterns, but the synthetic dataset repeats those patterns heavily. A final submission can use V2, but a minor calibration pass on repeated-template caps would be justified if time remains.
