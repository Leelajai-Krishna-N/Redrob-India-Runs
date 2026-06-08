# False Promotion Analysis

False promotions are WEAK or MEDIUM candidates that ranked unusually high or were judged too high by the committee.

## Candidates

| Candidate ID | Rank | Gold | Title | Family | Why V1 Promoted Them | Committee Concern |
| --- | --- | --- | --- | --- | --- | --- |
| CAND_0036184 | 35 | WEAK | Recommendation Systems Engineer | Recommendation Engineer | high technical_score 0.963; high career_score 0.923; strong market_score 0.938; no extracted evaluation evidence; template repetition | Profile consistency concern: current_title_description_mismatch, skills_current_role_mismatch, skills_career_history_mismatch |
| CAND_0037980 | 41 | WEAK | Senior Applied Scientist | Other | high technical_score 0.938; high career_score 1.000; strong market_score 0.926; weak V1 retrieval count; template repetition | Profile consistency concern: current_title_description_mismatch, previous_title_description_mismatch, skills_current_role_mismatch, skills_headline_mismatch, skills_career_history_mismatch |
| CAND_0087630 | 42 | WEAK | AI Engineer | Generic ML Engineer | high technical_score 0.910; high career_score 0.981; strong market_score 0.863; weak V1 retrieval count; template repetition | Repeated/template-like role descriptions across employers; committee discounts confidence. |
| CAND_0003977 | 54 | WEAK | Recommendation Systems Engineer | Recommendation Engineer | high technical_score 0.963; high career_score 0.948; strong market_score 0.815; no extracted evaluation evidence; template repetition | Profile consistency concern: current_title_description_mismatch, skills_current_role_mismatch, skills_career_history_mismatch |
| CAND_0009691 | 66 | WEAK | Applied ML Engineer | Generic ML Engineer | high technical_score 0.916; high career_score 1.000; weak V1 retrieval count; template repetition | Repeated/template-like role descriptions across employers; committee discounts confidence. |
| CAND_0069905 | 12 | MEDIUM | Applied ML Engineer | Applied ML Engineer | high technical_score 0.979; high career_score 1.000; strong market_score 0.871; template repetition | Profile consistency concern: previous_title_description_mismatch, skills_headline_mismatch |
| CAND_0039383 | 13 | MEDIUM | Applied ML Engineer | Retrieval Engineer | high technical_score 0.937; high career_score 1.000; strong market_score 0.891; template repetition | Repeated/template-like role descriptions across employers; committee discounts confidence. |
| CAND_0093912 | 15 | MEDIUM | Senior Data Scientist | Search Ranking Engineer | high technical_score 0.961; high career_score 1.000; strong market_score 0.941; template repetition | Profile consistency concern: previous_title_description_mismatch, moderate_career_incoherence, skills_current_role_mismatch, skills_career_history_mismatch |
| CAND_0055992 | 18 | MEDIUM | AI Engineer | Search Ranking Engineer | high technical_score 0.985; high career_score 1.000; strong market_score 0.927 | Profile consistency concern: previous_title_description_mismatch, degree_order_reversal, graduation_after_employment_start, skills_headline_mismatch |
| CAND_0081686 | 22 | MEDIUM | Search Engineer | Search Ranking Engineer | high technical_score 0.953; high career_score 1.000; strong market_score 0.943 | Profile consistency concern: current_title_description_mismatch, previous_title_description_mismatch, skills_current_role_mismatch, skills_career_history_mismatch |
| CAND_0010770 | 34 | MEDIUM | Recommendation Systems Engineer | Recommendation Engineer | high technical_score 0.982; high career_score 1.000; strong market_score 0.817; template repetition | Profile consistency concern: current_title_description_mismatch, moderate_career_incoherence, skills_current_role_mismatch |
| CAND_0041669 | 38 | MEDIUM | Recommendation Systems Engineer | Recommendation Engineer | high technical_score 0.938; high career_score 1.000; strong market_score 0.942; weak V1 retrieval count | Profile consistency concern: current_title_description_mismatch, previous_title_description_mismatch, skills_current_role_mismatch, skills_headline_mismatch, skills_career_history_mismatch |
| CAND_0027801 | 39 | MEDIUM | NLP Engineer | NLP Engineer | high technical_score 0.955; high career_score 0.959; strong market_score 0.828; no extracted evaluation evidence; template repetition | Profile consistency concern: previous_title_description_mismatch |
| CAND_0064326 | 40 | MEDIUM | Search Engineer | Search Ranking Engineer | high technical_score 0.937; high career_score 1.000; strong market_score 0.934; weak V1 retrieval count; template repetition | Profile consistency concern: current_title_description_mismatch, graduation_after_employment_start, skills_current_role_mismatch, skills_headline_mismatch |
| CAND_0057563 | 43 | MEDIUM | NLP Engineer | Search Ranking Engineer | high technical_score 0.962; high career_score 1.000; strong market_score 0.868 | Profile consistency concern: previous_title_description_mismatch, degree_order_reversal, graduation_after_employment_start |
| CAND_0029367 | 44 | MEDIUM | Senior Data Scientist | Applied ML Engineer | high technical_score 0.972; high career_score 1.000; template repetition | Repeated/template-like role descriptions across employers; committee discounts confidence. |
| CAND_0075249 | 47 | MEDIUM | Applied ML Engineer | Retrieval Engineer | high technical_score 0.951; high career_score 0.978; strong market_score 0.805 | Profile consistency concern: previous_title_description_mismatch, skills_headline_mismatch |
| CAND_0007412 | 48 | MEDIUM | Applied ML Engineer | Search Ranking Engineer | high technical_score 0.929; high career_score 1.000; strong market_score 0.891; weak V1 retrieval count; template repetition | Profile consistency concern: previous_title_description_mismatch, previous_title_description_mismatch, skills_current_role_mismatch, skills_headline_mismatch |
| CAND_0040887 | 49 | MEDIUM | Machine Learning Engineer | Applied ML Engineer | high technical_score 0.914; strong market_score 0.966 | Profile consistency concern: skills_headline_mismatch |

## Patterns

- V1 can promote candidates when `technical_score` and `career_score` are high even if committee evidence is MEDIUM.
- Recommendation-heavy profiles can look like direct search/relevance candidates when ranking terms appear without enough retrieval/evaluation depth.
- Template repetition is a recurring trust issue that should become an explicit V2 feature or cap.
- Market score can reinforce a candidate already inflated by broad technical evidence.
- Weak or missing evaluation evidence is common among candidates the committee would not prioritize for early interviews.
