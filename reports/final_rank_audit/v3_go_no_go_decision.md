# V3 Go/No-Go Decision

## Is V3 Justified?

YES, but only as a narrow calibration pass. A full architecture rewrite is not justified.

## Expected Gain

moderate

## Exact Ranking Mistakes That Remain

| Mistake | Evidence | Examples |
| --- | --- | --- |
| MEDIUM/WEAK too high | 5 MEDIUM/WEAK in Top 25; 7 in Top 50 | CAND_0010770, CAND_0081686, CAND_0057563, CAND_0055992, CAND_0086151 |
| Template collapse | 33 Top 100 candidates with template_repetition; 2 broad evidence-template families | CAND_0065878, CAND_0014440, CAND_0039383, CAND_0078492, CAND_0099401, CAND_0094759, CAND_0064326, CAND_0093331 |
| Strong candidates still low | 9 STRONG candidates outside Top 50 | CAND_0036863, CAND_0061655, CAND_0047721, CAND_0070202, CAND_0006557, CAND_0044883, CAND_0079387, CAND_0075574 |
| ELITE precision not perfect | 5 ELITE candidates outside Top 10 | CAND_0086022, CAND_0094759, CAND_0041611, CAND_0091534, CAND_0010685 |

## Evidence-Supported Modifications

1. Add source-diversity caps: high Level 5 evidence should require non-identical role descriptions.
2. Strengthen template_repetition caps for Top 25 candidates.
3. Damp repeated Human Judgments + LTR and Recommendation + Ranking/Evaluation templates after the first few near-duplicates.
4. Require stronger retrieval evidence for recommendation-heavy candidates to remain in Top 25.
5. Use trust flags as rank-band caps, not broad score subtraction.

## Dangerous Modifications

1. Blanket demotion of recommendation engineers; several are legitimately STRONG.
2. Heavy diversity quotas by title/company; this could demote true search/relevance engineers.
3. Overweighting behavioral signals; market readiness is not relevance.
4. Hard-filtering education chronology flags; those flags are noisy.
5. Tuning only to the 100-candidate gold set without checking full-list behavior.

## Final Recommendation

3. Run one more calibration pass before deciding

The current V2 is strong and submission-capable, but the template-collapse evidence is concrete enough that one narrow calibration pass is likely worth the engineering time if there is still runway.
