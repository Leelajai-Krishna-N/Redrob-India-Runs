# Feature Importance Audit

Gold labels were encoded as WEAK=0, MEDIUM=1, STRONG=2, ELITE=3. Correlations are computed over the 100 committee-reviewed candidates.

## Feature Audit Table

| Feature | Pearson | Spearman | ELITE Mean | STRONG Mean | MEDIUM Mean | WEAK Mean | Classification | Usefulness | Observed Issues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scale_term_count | 0.660 | 0.548 | 8.250 | 4.103 | 2.818 | 1.800 | HIGH VALUE | Strongly separates gold labels in this reviewed set. | Needs evidence tracing to avoid counting repeated/template language. |
| evaluation_evidence_count | 0.657 | 0.571 | 10.083 | 5.692 | 4.500 | 1.400 | HIGH VALUE | Strong qualitative signal from committee; should become explicit V2 feature. | Not first-class in V1 despite committee value. |
| ownership_term_count | 0.629 | 0.525 | 5.833 | 3.949 | 3.455 | 1.800 | HIGH VALUE | Strongly separates gold labels in this reviewed set. | Needs evidence tracing to avoid counting repeated/template language. |
| career_search_count_extracted | 0.580 | 0.566 | 7.667 | 4.821 | 3.682 | 1.400 | HIGH VALUE | Directly useful when role-level evidence is real; needs ownership/source tracing. | Needs evidence tracing to avoid counting repeated/template language. |
| career_evaluation_count_extracted | 0.568 | 0.506 | 8.333 | 4.795 | 4.091 | 0.800 | HIGH VALUE | Strong qualitative signal from committee; should become explicit V2 feature. | Not first-class in V1 despite committee value. |
| evidence_strength_level | 0.470 | 0.428 | 4.917 | 4.179 | 4.068 | 3.000 | HIGH VALUE | Strongly separates gold labels in this reviewed set. | Needs evidence tracing to avoid counting repeated/template language. |
| career_retrieval_count_extracted | 0.420 | 0.408 | 6.333 | 4.179 | 3.250 | 2.000 | MEDIUM VALUE | Directly useful when role-level evidence is real; needs ownership/source tracing. | Needs evidence tracing to avoid counting repeated/template language. |
| template_repetition_flag | -0.366 | -0.362 | 0.167 | 0.256 | 0.500 | 1.000 | HIGH VALUE | Useful as trust/cap signal; current coverage and calibration are incomplete. | Not in V1; committee used it to discount confidence. |
| vector_evidence_count | 0.362 | 0.337 | 7.667 | 6.256 | 5.523 | 4.800 | MEDIUM VALUE | Directional signal, best used with other feature families. | Needs evidence tracing to avoid counting repeated/template language. |
| final_score | 0.347 | 0.370 | 0.941 | 0.922 | 0.903 | 0.920 | MEDIUM VALUE | Useful aggregate but masks which relevance family drives rank. | Final ordering inherits V1 blending and market-signal effects. |
| technical_score | 0.312 | 0.340 | 0.976 | 0.931 | 0.918 | 0.938 | MEDIUM VALUE | Useful but saturated in top candidates; needs decomposition. | Blends search, retrieval, recommendation, vector search, and generic AI. |
| career_ranking_evidence_count | 0.297 | 0.278 | 4.500 | 3.231 | 2.977 | 3.200 | MEDIUM VALUE | Directly useful when role-level evidence is real; needs ownership/source tracing. | Needs evidence tracing to avoid counting repeated/template language. |
| ai_skill_count | 0.283 | 0.287 | 4.667 | 3.667 | 3.091 | 3.600 | MEDIUM VALUE | Weak standalone signal; broad skill lists can mislead without career support. | Skill breadth does not prove ownership. |
| career_score | 0.281 | 0.274 | 0.997 | 0.981 | 0.958 | 0.970 | MEDIUM VALUE | Useful but saturated in top candidates; needs decomposition. | Top-tail saturation reduces ordering power. |
| consistency_points | -0.264 | -0.301 | 3.750 | 2.308 | 5.341 | 4.200 | HIGH VALUE | Useful as trust/cap signal; current coverage and calibration are incomplete. | Needs evidence tracing to avoid counting repeated/template language. |
| consistency_penalty | -0.264 | -0.301 | 0.125 | 0.077 | 0.178 | 0.140 | HIGH VALUE | Useful as trust/cap signal; current coverage and calibration are incomplete. | Needs evidence tracing to avoid counting repeated/template language. |
| consistency_score | 0.264 | 0.301 | 0.875 | 0.923 | 0.822 | 0.860 | MEDIUM VALUE | Useful as trust/cap signal; current coverage and calibration are incomplete. | Many candidates appear clean or unaudited; repeated templates need stronger handling. |
| years_of_experience | 0.136 | 0.164 | 8.467 | 6.526 | 6.766 | 6.600 | LOW VALUE | Low separation in the reviewed Top 100. | Needs evidence tracing to avoid counting repeated/template language. |
| relevant_duration_months | 0.132 | 0.143 | 80.667 | 74.282 | 70.682 | 78.200 | LOW VALUE | Low separation in the reviewed Top 100. | Needs evidence tracing to avoid counting repeated/template language. |
| career_recommendation_count_extracted | 0.091 | 0.081 | 0.917 | 1.385 | 0.841 | 1.000 | LOW VALUE | Useful only when tied to ranking/matching/evaluation. | Recommendation-only evidence must be separated from search/relevance ownership. |
| market_score | -0.086 | 0.008 | 0.823 | 0.824 | 0.843 | 0.848 | LOW VALUE | Useful as availability/tie-breaker, but not reliable as core relevance. | Can over-promote available but less relevant profiles if not band-limited. |
| recommendation_evidence_count | 0.074 | 0.025 | 1.500 | 1.872 | 1.500 | 1.600 | LOW VALUE | Useful only when tied to ranking/matching/evaluation. | Recommendation-only evidence must be separated from search/relevance ownership. |
| career_retrieval_evidence_count | 0.068 | 0.134 | 3.500 | 2.949 | 2.750 | 3.200 | LOW VALUE | Directly useful when role-level evidence is real; needs ownership/source tracing. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |
| skill_count | 0.029 | 0.071 | 16.500 | 16.538 | 15.841 | 18.000 | LOW VALUE | Weak standalone signal; broad skill lists can mislead without career support. | Skill breadth does not prove ownership. |
| relevant_role_count | 0.023 | 0.046 | 2.667 | 2.769 | 2.705 | 2.600 | LOW VALUE | Low separation in the reviewed Top 100. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |
| ai_transition | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | LOW VALUE | Important guardrail, but Top 100 has little variance. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |
| calibration_penalty | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | LOW VALUE | Low separation in the reviewed Top 100. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |
| consulting_only | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | LOW VALUE | Important guardrail, but Top 100 has little variance. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |
| keyword_stuffer | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | LOW VALUE | Important guardrail, but Top 100 has little variance. | Little monotonic separation across ELITE/STRONG/MEDIUM/WEAK. |

## Main Findings

- The best signals are not raw skill breadth; they are evidence strength, role-level search/retrieval/evaluation counts, and ownership/scale terms.
- V1 ranking and retrieval counts are useful, but they need source-level evidence and ownership tracing.
- Market score is a hiring-availability feature, not a quality feature.
- Consistency and template repetition matter more in committee judgment than V1 currently captures.
- Recommendation evidence is useful only when tied to ranking, matching, retrieval, or evaluation.
