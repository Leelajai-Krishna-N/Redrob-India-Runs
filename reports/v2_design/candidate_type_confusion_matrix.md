# Candidate-Type Confusion Matrix

## Summary

Ranker V1 is effective at pushing obvious AI-transition candidates and keyword stuffers out of the Top 100. The remaining risk is subtler: V1 can confuse adjacent technical families that share vocabulary but imply different interview value.

This matrix ranks confusion pairs by V2 risk.

## Risk 1: Recommendation Engineer vs Search Ranking Engineer

Risk level: High

Why confusion occurs:

- Recommendation systems, search ranking, and matching all use ranking, relevance, embeddings, features, online metrics, and personalization language.
- The JD explicitly allows recommendation-system builders as fits, but only when the work is close to ranking/matching systems used by real users.
- Recommendation Systems Engineer is the most common exact title in Top 100 with 16 candidates.

Current V1 behavior:

- V1 rewards recommendation candidates when they include ranking/retrieval career evidence.
- Top 100 contains 16 Recommendation Systems Engineer titles.
- Ranks 90-100 contain 4 Recommendation Systems Engineer titles, while mean retrieval evidence in that slice is only 1.27 versus 2.94 for Top 100 overall.

Desired V2 behavior:

- Split recommendation evidence into:
  - recommendation ranking/matching ownership: high
  - recommender modeling without ranking/evaluation: medium
  - recommendation skill only: weak
- Require at least one of ranking, matching, evaluation, user-facing system, or online metrics for recommendation candidates to compete with Search Ranking candidates.

## Risk 2: Vector Search Engineer vs RAG Engineer

Risk level: High

Why confusion occurs:

- Vector DB names, embeddings, semantic search, RAG, and LangChain often appear together.
- The JD values vector/hybrid retrieval infrastructure, but warns against candidates whose AI experience is mainly recent LangChain/OpenAI usage.
- Vector search terms are easy to place in skills without role-level proof.

Current V1 behavior:

- V1 applies keyword-stuffer and AI-transition penalties, keeping these out of Top 100.
- Keyword stuffer examples still reach final scores around 0.46-0.49 due to vector-search technical evidence, despite limited career support.
- Top 100 skills include Qdrant 34, Embeddings 33, Weaviate 32, FAISS 31, pgvector 30, Pinecone 27, and Milvus 25.

Desired V2 behavior:

- Treat production vector retrieval operations as high signal.
- Treat RAG demos or vector DB skill names as weak signal unless tied to production retrieval, index refresh, evaluation, or quality regression.
- Store source and snippet evidence so explanations can distinguish "operated Qdrant index for candidate retrieval" from "listed Qdrant as a skill."

## Risk 3: NLP Engineer vs Search/Relevance Engineer

Risk level: Medium-High

Why confusion occurs:

- NLP, transformers, sentence transformers, text encoders, semantic search, and embeddings overlap with retrieval and matching systems.
- Search relevance roles often use NLP components, but NLP model work alone is not search/relevance ownership.

Current V1 behavior:

- Top 100 contains 15 NLP-title candidates.
- V1 can surface strong NLP candidates when their career evidence contains ranking/retrieval terms.
- Explanations do not show enough snippets to validate whether NLP evidence is search-specific.

Desired V2 behavior:

- Rank NLP candidates highly only when their NLP work feeds retrieval, ranking, matching, or evaluation.
- Keep generic NLP, ASR/TTS, text classification, or transformer model work as supporting evidence.

## Risk 4: Applied ML Engineer vs Ranking Engineer

Risk level: Medium-High

Why confusion occurs:

- Applied ML engineers often have production model deployment, feature engineering, and MLOps language.
- These are useful but not equivalent to ranking/relevance system ownership.
- Top 100 contains many broad ML titles.

Current V1 behavior:

- Top 100 title families include Machine Learning 20, Applied ML 10, AI Engineer 14, and Data Scientist 11.
- Top 10 includes 4 Machine Learning title-family candidates, but their high ranks are supported by strong career ranking and retrieval evidence.

Desired V2 behavior:

- Preserve high ranking for applied ML candidates with direct search/relevance evidence.
- Downweight generic production ML without search, retrieval, recommendation, or evaluation evidence.
- Add a "generic ML dilution" feature when a profile is broad but lacks direct relevance.

## Risk 5: Retrieval Infrastructure Engineer vs Generic Data Engineer

Risk level: Medium

Why confusion occurs:

- Retrieval systems use pipelines, indexing, data quality, streaming, and feature infrastructure.
- Generic data engineers also use Spark, Airflow, SQL, Kafka, warehouses, and pipelines.
- The sampled JD-aligned bucket contains backend/data profiles with AI skills but weak search ownership.

Current V1 behavior:

- V1 rewards retrieval terms more than generic data infrastructure, but evidence tracing is not granular enough to separate "feature pipeline for ranking" from "analytics warehouse."
- The sampled `CAND_0000001` profile is a Backend Engineer with strong data pipeline evidence and ML-transition language, not a direct search/ranking owner.

Desired V2 behavior:

- Give data infrastructure high value only when it directly supports ranking, retrieval, recommendation, candidate generation, or feedback loops.
- Keep generic ETL as medium/low support.

## Risk 6: Consulting AI Candidate vs Product Search Engineer

Risk level: Medium

Why confusion occurs:

- Consulting profiles can contain many technologies, client projects, and AI keywords.
- Some consultants genuinely build production systems; others build prototypes or short-lived POCs.
- Product ownership is a central JD need.

Current V1 behavior:

- V1 applies a small consulting-only penalty, which avoids over-penalizing valid consulting experience.
- Forensic comparison shows Consulting is a huge bucket with 72,039 candidates, so even small calibration mistakes can affect many profiles.

Desired V2 behavior:

- Distinguish production ownership from prototype delivery.
- Reward consulting candidates when they owned deployed search/ranking systems with measurable outcomes.
- Penalize consulting-only profiles only when they lack product ownership, long-term system operation, or feedback loops.

## Risk 7: Keyword Stuffer vs Vector/Retrieval Candidate

Risk level: High

Why confusion occurs:

- Both can contain the same high-value terms: embeddings, vector search, BM25, RAG, FAISS, Qdrant, Pinecone.
- Skill count can be high in both.
- The hidden dataset appears template-driven, making repeated bundles plausible.

Current V1 behavior:

- Top 100 has zero keyword-stuffer flags.
- Keyword stuffers still score in the mid-ranking range when technical skills are strong.
- V1 explanations call out "many AI skills but little supporting career evidence."

Desired V2 behavior:

- Add source-diversity checks.
- Cap skill-only contributions.
- Penalize repeated term bundles without role descriptions.
- Store evidence snippets for every high-value term.

## Risk 8: AI Transition Candidate vs Applied AI Engineer

Risk level: Medium

Why confusion occurs:

- Both may list LLMs, RAG, LangChain, vector DBs, prompt engineering, fine-tuning, and embeddings.
- Transition candidates may have strong self-directed projects.
- V1 can score transition candidates moderately when market signals are strong.

Current V1 behavior:

- Top 100 has zero AI-transition flags.
- V1 AI-transition examples score around 0.44-0.45, usually due to vector-search skill evidence and market engagement.

Desired V2 behavior:

- Keep AI-transition penalty, but make it evidence-sensitive.
- A candidate with non-ML title plus substantial production AI work should be recoverable.
- A candidate with unrelated career history and skill-only AI terms should stay low.

## Risk 9: Behavioral Twin vs Strong Relevance Candidate

Risk level: Medium

Why confusion occurs:

- The challenge warns about behavioral twins.
- High recruiter engagement and availability can make weaker candidates look attractive.
- V1 gives market signals 20 percent weight.

Current V1 behavior:

- Market score helps order the top tail after career and technical scores saturate.
- No candidate has market_score exactly 1.0, but market_score p95 is 0.7053 and Top 100 mean market score is 0.8334.

Desired V2 behavior:

- Use market readiness primarily as a tie-breaker within relevance bands.
- Prevent market signals from compensating for missing search/relevance evidence.
- Keep severe inactivity as a meaningful downweight.

## V2 Risk Ordering

1. Recommendation Engineer vs Search Ranking Engineer
2. Vector Search Engineer vs RAG Engineer
3. Keyword Stuffer vs Vector/Retrieval Candidate
4. NLP Engineer vs Search/Relevance Engineer
5. Applied ML Engineer vs Ranking Engineer
6. Retrieval Infrastructure Engineer vs Generic Data Engineer
7. Consulting AI Candidate vs Product Search Engineer
8. Behavioral Twin vs Strong Relevance Candidate
9. AI Transition Candidate vs Applied AI Engineer

The largest V2 design risk is not obvious fraud. It is over-ranking adjacent candidates whose vocabulary overlaps with search/relevance but whose career evidence does not prove production ownership.
