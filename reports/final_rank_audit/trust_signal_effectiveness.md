# Trust Signal Effectiveness

| Trust Signal | Top100 Count | MEDIUM/WEAK Share | Top25 Count | Examples |
| --- | --- | --- | --- | --- |
| degree_order_reversal | 8 | 62.5% | 4 | CAND_0046064, CAND_0055905, CAND_0057563, CAND_0055992, CAND_0033861 |
| graduation_after_employment_start | 6 | 50.0% | 3 | CAND_0018499, CAND_0057563, CAND_0055992, CAND_0080766, CAND_0093547 |
| title_description_mismatch | 52 | 63.5% | 13 | CAND_0039754, CAND_0055905, CAND_0053695, CAND_0086022, CAND_0094759 |
| skills_headline_mismatch | 35 | 57.1% | 9 | CAND_0046064, CAND_0039754, CAND_0081846, CAND_0008425, CAND_0055905 |
| skills_current_role_mismatch | 45 | 57.8% | 12 | CAND_0046064, CAND_0039754, CAND_0081846, CAND_0008425, CAND_0055905 |
| template_repetition | 33 | 63.6% | 8 | CAND_0092278, CAND_0018499, CAND_0088025, CAND_0094759, CAND_0077337 |
| signup_after_last_active | 2 | 50.0% | 1 | CAND_0041611, CAND_0064270 |
| salary_inconsistency | 1 | 100.0% | 0 | CAND_0052335 |

## Conclusions

1. Trust penalties are directionally useful but slightly weak for template repetition and title/skill mismatch in the Top 25.
2. They are not too strong overall: all ELITE candidates remain highly ranked, and STRONG candidates mostly remain in the Top 100.
3. Template repetition, title-description mismatch, and skills mismatch are the signals most associated with questionable candidates. Education chronology flags are noisier and should stay as caps/tie-breakers rather than hard exclusions.
