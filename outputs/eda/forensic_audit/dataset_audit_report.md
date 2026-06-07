# Dataset Forensic Audit Report

## Executive Summary
- Full-dataset feature rows analyzed: 100000
- Deep consistency audit scope: 16654
- Severe rule-based suspicion score >= 8 within deep scope: 244
- Medium rule-based suspicion score 4-7.9 within deep scope: 6684
- No separate manual sus-label CSV was found; sus analysis uses prior EDA suspicious flags as a proxy.
- The scoring framework validates suspiciousness with evidence; it does not assume labels are correct.

## Major Anomalies
- previous_title_description_mismatch: 19273
- skills_career_history_mismatch: 13565
- skills_current_role_mismatch: 12912
- skills_headline_mismatch: 11816
- current_title_description_mismatch: 6505
- graduation_after_employment_start: 4048
- moderate_career_incoherence: 3994
- abrupt_career_jumps: 3909
- salary_min_exceeds_max: 3142
- signup_after_last_active: 1224
- degree_order_reversal: 1199

## Category Comparisons
Median values by bucket for key metrics:
| bucket          |   interview_completion_rate |   offer_acceptance_rate |   profile_completeness_score |   recruiter_response_rate |   salary_mid_lpa |   salary_range_lpa |   saved_by_recruiters_30d |   search_appearance_30d |   skill_count |   years_of_experience |
|:----------------|----------------------------:|------------------------:|-----------------------------:|--------------------------:|-----------------:|-------------------:|--------------------------:|------------------------:|--------------:|----------------------:|
| AI-title        |                        0.74 |                    0.43 |                         73   |                      0.61 |            35.45 |               14.8 |                        27 |                     444 |            15 |                   5.2 |
| Consulting      |                        0.61 |                   -1    |                         56.1 |                      0.43 |            14.7  |                7.1 |                         7 |                      99 |             9 |                   8   |
| High-experience |                        0.59 |                   -1    |                         55.3 |                      0.42 |            13.8  |                6.5 |                         6 |                      90 |             8 |                  14.5 |
| JD-aligned      |                        0.63 |                   -1    |                         57.6 |                      0.45 |            16.2  |                8   |                         7 |                     113 |            10 |                   7.1 |
| Random          |                        0.62 |                   -1    |                         56.6 |                      0.43 |            15.4  |                7.7 |                         7 |                     107 |             9 |                   6.8 |
| Sus-proxy       |                        0.6  |                   -1    |                         57.8 |                      0.42 |            14.1  |                7.3 |                         6 |                      92 |            21 |                   7.8 |

## Hidden Signals
Top Random Forest predictors by target:
### AI-title
- salary_mid_lpa: importance=0.2787, MI=0.0346
- expected_salary_max_lpa: importance=0.2007, MI=0.0313
- expected_salary_min_lpa: importance=0.1611, MI=0.0305
- skill_count: importance=0.0868, MI=0.0151
- saved_by_recruiters_30d: importance=0.0583, MI=0.0256
- search_appearance_30d: importance=0.0492, MI=0.0259
- days_since_last_active: importance=0.0444, MI=0.0075
- skill_assessment_count: importance=0.0350, MI=0.0149
### JD alignment
- skill_count: importance=0.3059, MI=0.0915
- search_appearance_30d: importance=0.1351, MI=0.0547
- saved_by_recruiters_30d: importance=0.1193, MI=0.0490
- expected_salary_max_lpa: importance=0.0960, MI=0.0542
- expected_salary_min_lpa: importance=0.0709, MI=0.0453
- career_role_count: importance=0.0643, MI=0.0139
- salary_mid_lpa: importance=0.0620, MI=0.0501
- years_of_experience: importance=0.0380, MI=0.0099
### Suspicion proxy
- skill_count: importance=0.3932, MI=0.0413
- consistency_reason_count: importance=0.2602, MI=0.0133
- consistency_suspicion_score_10: importance=0.2265, MI=0.0139
- is_random_bucket: importance=0.0150, MI=0.0001
- salary_mid_lpa: importance=0.0138, MI=0.0010
- search_appearance_30d: importance=0.0129, MI=0.0007
- saved_by_recruiters_30d: importance=0.0113, MI=0.0022
- expected_salary_max_lpa: importance=0.0112, MI=0.0008

## Suspected Generator Weaknesses
- Exact repeated text, repeated career paths, repeated education patterns, and repeated skill bundles are reported separately in generator_artifacts_report.md.
- Cross-domain role/description mismatches suggest random field sampling or imperfect template stitching.
- Weak AI evidence under AI titles suggests title templates may be assigned independently from skills or work descriptions.

## Confidence Levels
- High confidence: impossible date relationships, salary min/max inversions, education end-before-start.
- Medium confidence: role-description mismatch and abrupt career jumps, because taxonomy rules are approximate.
- Low-to-medium confidence: skill mismatch, because multi-disciplinary profiles can be legitimate.