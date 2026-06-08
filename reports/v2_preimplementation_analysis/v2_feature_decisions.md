# V2 Feature Decisions

## Decision Table

| V1 Feature | Decision | Evidence | Rationale | Expected Impact |
| --- | --- | --- | --- | --- |
| final_score | MODIFY | corr=0.347; ELITE=0.941; WEAK=0.920 | Final ordering inherits V1 blending and market-signal effects. | Improves precision by decomposing, capping, or tracing the feature. |
| technical_score | MODIFY | corr=0.312; ELITE=0.976; WEAK=0.938 | Blends search, retrieval, recommendation, vector search, and generic AI. | Improves precision by decomposing, capping, or tracing the feature. |
| career_ranking_evidence_count | MODIFY | corr=0.297; ELITE=4.500; WEAK=3.200 | Needs evidence tracing to avoid counting repeated/template language. | Improves precision by decomposing, capping, or tracing the feature. |
| ai_skill_count | MODIFY | corr=0.283; ELITE=4.667; WEAK=3.600 | Skill breadth does not prove ownership. | Improves precision by decomposing, capping, or tracing the feature. |
| career_score | MODIFY | corr=0.281; ELITE=0.997; WEAK=0.970 | Top-tail saturation reduces ordering power. | Improves precision by decomposing, capping, or tracing the feature. |
| consistency_points | MODIFY | corr=-0.264; ELITE=3.750; WEAK=4.200 | Needs evidence tracing to avoid counting repeated/template language. | Improves precision by decomposing, capping, or tracing the feature. |
| consistency_penalty | MODIFY | corr=-0.264; ELITE=0.125; WEAK=0.140 | Needs evidence tracing to avoid counting repeated/template language. | Improves precision by decomposing, capping, or tracing the feature. |
| consistency_score | MODIFY | corr=0.264; ELITE=0.875; WEAK=0.860 | Many candidates appear clean or unaudited; repeated templates need stronger handling. | Improves precision by decomposing, capping, or tracing the feature. |
| years_of_experience | KEEP | corr=0.136; ELITE=8.467; WEAK=6.600 | Needs evidence tracing to avoid counting repeated/template language. | Preserves validated guardrail/context. |
| relevant_duration_months | MODIFY | corr=0.132; ELITE=80.667; WEAK=78.200 | Needs evidence tracing to avoid counting repeated/template language. | Improves precision by decomposing, capping, or tracing the feature. |
| market_score | MODIFY | corr=-0.086; ELITE=0.823; WEAK=0.848 | Can over-promote available but less relevant profiles if not band-limited. | Improves precision by decomposing, capping, or tracing the feature. |
| career_retrieval_evidence_count | MODIFY | corr=0.068; ELITE=3.500; WEAK=3.200 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Improves precision by decomposing, capping, or tracing the feature. |
| skill_count | MODIFY | corr=0.029; ELITE=16.500; WEAK=18.000 | Skill breadth does not prove ownership. | Improves precision by decomposing, capping, or tracing the feature. |
| relevant_role_count | MODIFY | corr=0.023; ELITE=2.667; WEAK=2.600 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Improves precision by decomposing, capping, or tracing the feature. |
| ai_transition | KEEP | corr=0.000; ELITE=0.000; WEAK=0.000 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Preserves validated guardrail/context. |
| calibration_penalty | MODIFY | corr=0.000; ELITE=0.000; WEAK=0.000 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Improves precision by decomposing, capping, or tracing the feature. |
| consulting_only | KEEP | corr=0.000; ELITE=0.000; WEAK=0.000 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Preserves validated guardrail/context. |
| keyword_stuffer | KEEP | corr=0.000; ELITE=0.000; WEAK=0.000 | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. | Preserves validated guardrail/context. |

## Summary

Keep V1's broad architecture and guardrails, but modify most scoring features. The largest need is decomposition: V2 should split blended technical and career features into search ranking, retrieval infrastructure, recommendation/matching, evaluation/relevance science, and generic AI support. Skill breadth should be capped. Market score should become a tie-breaker. Consistency should include template repetition and explicit audit coverage.
