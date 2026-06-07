# Suspicion Scoring Framework

This is an explainability framework, not a model and not a ground-truth label definition.

| Signal | Points | Justification |
|---|---:|---|
| Signup date after last active date | +5 | Impossible platform chronology. |
| Salary minimum exceeds maximum | +5 | Impossible compensation range. |
| Education end before start | +5 | Impossible education timeline. |
| Abrupt career jumps across 4+ unrelated domains | +4 | Strong evidence of random/template mixing. |
| Degree order reversal | +4 | Master's/PhD chronology contradicts normal progression. |
| AI-title with weak AI evidence | +4 | Title appears unsupported by skills/work text. |
| Current title-description mismatch | +3 | Current role label contradicts described work. |
| Graduation after employment start | +3 | Possible overlap or chronology issue. |
| Previous title-description mismatch | +2 | Historical role label contradicts described work. |
| Skills-current-role mismatch | +2 | Skill bundle appears sampled from another archetype. |
| Unrealistic salary range | +2 | Possible numeric generator artifact. |
| Skills-headline or skills-career mismatch | +1 | Weak inconsistency signal, useful only with other evidence. |

Scores are capped to 10 for reporting. Raw points are preserved in CSV outputs.