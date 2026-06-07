# Consistency Penalty Audit

## Direct Answers

1. Many `consistency_penalty` values are 0 because Ranker V1 only loads forensic scores for **16654** candidates. The other **83346** candidates default to `raw_suspicion_points = 0`.
2. This is expected from the current implementation, but it is not ideal behavior. Missing forensic coverage is treated the same as audited-clean.
3. I do not see an arithmetic bug in penalty application. I do see a coverage/design bug: `missing audit` and `clean profile` collapse into the same state.
4. The threshold is less important than coverage. Among audited candidates, penalties and caps can be strong; among unaudited candidates, no consistency penalty can fire.
5. Penalties influence audited candidates and capped candidates, but they are not a population-wide ranking signal.
6. Removing consistency penalties gives a current-vs-simulated Top 100 overlap of **97/100**. So **3** candidates enter or leave the Top 100 when consistency is neutralized.

## Coverage And Zero Penalties
| metric                                             |   count |   share |
|:---------------------------------------------------|--------:|--------:|
| all candidates with zero consistency penalty       |   84239 |  0.8424 |
| audited candidates with zero consistency penalty   |     893 |  0.0536 |
| unaudited candidates with zero consistency penalty |   83346 |  1      |

## Most Common Consistency Reasons In Scoring Output
| reason_code                         |   count |
|:------------------------------------|--------:|
| previous_title_description_mismatch |   19273 |
| skills_career_history_mismatch      |   13565 |
| skills_current_role_mismatch        |   12912 |
| skills_headline_mismatch            |   11816 |
| current_title_description_mismatch  |    6505 |
| graduation_after_employment_start   |    4048 |
| moderate_career_incoherence         |    3994 |
| abrupt_career_jumps                 |    3909 |
| salary_min_exceeds_max              |    3142 |
| signup_after_last_active            |    1224 |
| degree_order_reversal               |    1199 |

## Candidates Most Helped If Consistency Penalty Is Removed
| candidate_id   |   rank |   sim_rank_no_consistency |   rank_delta_if_no_consistency |   final_score |   sim_no_consistency_penalty |   consistency_points | consistency_reason_codes                                                                                                                                                                                                                                                                                                                            |
|:---------------|-------:|--------------------------:|-------------------------------:|--------------:|-----------------------------:|---------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAND_0069809   |  86903 |                     32017 |                          54886 |        0.1845 |                       0.2812 |                   29 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; signup_after_last_active; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch  |
| CAND_0036433   |  89246 |                     34401 |                          54845 |        0.18   |                       0.2766 |                   29 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch    |
| CAND_0070304   |  85601 |                     30856 |                          54745 |        0.1868 |                       0.2835 |                   29 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch    |
| CAND_0093725   |  94529 |                     39966 |                          54563 |        0.1654 |                       0.2654 |                   30 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; graduation_after_employment_start; signup_after_last_active; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch |
| CAND_0064391   |  82509 |                     28383 |                          54126 |        0.1915 |                       0.2882 |                   29 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; signup_after_last_active; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch  |
| CAND_0084837   |  83235 |                     30618 |                          52617 |        0.1906 |                       0.2839 |                   28 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch                                    |
| CAND_0068696   |  70032 |                     19309 |                          50723 |        0.2073 |                       0.3073 |                   30 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; graduation_after_employment_start; signup_after_last_active; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch |
| CAND_0029228   |  90598 |                     40706 |                          49892 |        0.177  |                       0.2637 |                   26 | previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; graduation_after_employment_start; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch                                        |
| CAND_0041923   |  87516 |                     37796 |                          49720 |        0.1834 |                       0.2701 |                   26 | current_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; degree_order_reversal; signup_after_last_active; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch                                     |
| CAND_0049255   |  93552 |                     44297 |                          49255 |        0.1689 |                       0.2555 |                   26 | current_title_description_mismatch; previous_title_description_mismatch; abrupt_career_jumps; graduation_after_employment_start; signup_after_last_active; salary_min_exceeds_max; skills_current_role_mismatch; skills_headline_mismatch; skills_career_history_mismatch                                                                           |

## Candidates Most Hurt In Relative Rank If Consistency Penalty Is Removed
| candidate_id   |   rank |   sim_rank_no_consistency |   rank_delta_if_no_consistency |   final_score |   sim_no_consistency_penalty |   consistency_points |   consistency_reason_codes |
|:---------------|-------:|--------------------------:|-------------------------------:|--------------:|-----------------------------:|---------------------:|---------------------------:|
| CAND_0065374   |  84422 |                     88429 |                          -4007 |        0.1887 |                       0.1887 |                    0 |                        nan |
| CAND_0073074   |  84425 |                     88431 |                          -4006 |        0.1886 |                       0.1886 |                    0 |                        nan |
| CAND_0057762   |  84421 |                     88427 |                          -4006 |        0.1887 |                       0.1887 |                    0 |                        nan |
| CAND_0010113   |  84424 |                     88430 |                          -4006 |        0.1886 |                       0.1886 |                    0 |                        nan |
| CAND_0091660   |  84528 |                     88534 |                          -4006 |        0.1885 |                       0.1885 |                    0 |                        nan |
| CAND_0090125   |  84529 |                     88535 |                          -4006 |        0.1885 |                       0.1885 |                    0 |                        nan |
| CAND_0033021   |  84527 |                     88533 |                          -4006 |        0.1885 |                       0.1885 |                    0 |                        nan |
| CAND_0008523   |  84398 |                     88403 |                          -4005 |        0.1887 |                       0.1887 |                    0 |                        nan |
| CAND_0097457   |  84411 |                     88416 |                          -4005 |        0.1887 |                       0.1887 |                    0 |                        nan |
| CAND_0042751   |  84445 |                     88450 |                          -4005 |        0.1886 |                       0.1886 |                    0 |                        nan |

## Recommendation

V2 should distinguish `not_audited`, `audited_clean`, and `audited_flagged`. Do not assign perfect consistency to unaudited candidates. Either run lightweight consistency checks over all 100k candidates or add a small uncertainty penalty/flag for missing forensic coverage.
