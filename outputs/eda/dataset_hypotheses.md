# Dataset Hypotheses

## Hypothesis 1: Some fields are structurally sparse and may matter more as presence indicators than raw values.
Evidence:
- `certifications` fill_rate=0.0
- `redrob_signals.skill_assessment_scores.Elasticsearch` fill_rate=0.001
- `redrob_signals.skill_assessment_scores.Embeddings` fill_rate=0.001
- `redrob_signals.skill_assessment_scores.Python` fill_rate=0.001
- `redrob_signals.skill_assessment_scores.Fine-tuning LLMs` fill_rate=0.002
- `redrob_signals.skill_assessment_scores.PEFT` fill_rate=0.002
- `redrob_signals.skill_assessment_scores.QLoRA` fill_rate=0.002
- `redrob_signals.skill_assessment_scores.RAG` fill_rate=0.002
- `redrob_signals.skill_assessment_scores.Prompt Engineering` fill_rate=0.003
- `redrob_signals.skill_assessment_scores.Qdrant` fill_rate=0.003
- `redrob_signals.skill_assessment_scores.Vector Search` fill_rate=0.003
- `redrob_signals.skill_assessment_scores.Deep Learning` fill_rate=0.004
- `redrob_signals.skill_assessment_scores.FAISS` fill_rate=0.004
- `redrob_signals.skill_assessment_scores.Haystack` fill_rate=0.004
- `redrob_signals.skill_assessment_scores.Machine Learning` fill_rate=0.004

## Hypothesis 2: JD-adjacent terminology appears in a measurable subset of profiles.
Evidence: AI/search/retrieval/ranking term share=100.000%; JD-family aligned share=70.145%.

## Hypothesis 3: Behavioral activity separates candidates into availability-like segments.
Evidence:
- `dormant`: 61.32%
- `passive`: 29.22%
- `moderately_active`: 9.25%
- `highly_active`: 0.21%

## Hypothesis 4: Honeypot-like anomalies are concentrated in timeline and skill consistency flags.
Evidence: timeline flags=24, skill flags=726, combined honeypot flags=749.
