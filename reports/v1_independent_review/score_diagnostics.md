# Score Diagnostics

## Direct Answers

1. Candidates with `career_score == 1`: **64** (0.06%).
2. Candidates with `market_score == 1`: **0** (0.00%).
3. Candidates with `consistency_score == 1`: **84239** (84.24%).
4. Scores are saturating in two places: `career_score` reaches 1.0 for a small top-tail group, and `consistency_score` is exactly 1.0 for most candidates. `market_score` does not reach 1.0 but gets close.
5. Scores are partly discriminative: `technical_score` is sparse and useful in the top tail, `market_score` is broad, but `consistency_score` is weakly discriminative for most candidates.
6. Ceiling concentration is strongest in consistency. Career ceiling concentration is smaller but ranking-important.
7. Final ranking is mostly driven by technical and career evidence in the high ranks; market acts as a booster/tie-breaker, and consistency mostly penalizes audited candidates.

## Score Quantiles
| metric              |    min |    p05 |    p25 |   median |    p75 |    p95 |    p99 |    max |
|:--------------------|-------:|-------:|-------:|---------:|-------:|-------:|-------:|-------:|
| career_score        | 0      | 0      | 0.05   |   0.1    | 0.1    | 0.4079 | 0.611  | 1      |
| market_score        | 0.1165 | 0.2962 | 0.3894 |   0.4615 | 0.5456 | 0.7053 | 0.8162 | 0.9954 |
| consistency_score   | 0      | 0.5333 | 1      |   1      | 1      | 1      | 1      | 1      |
| consistency_penalty | 0      | 0      | 0      |   0      | 0      | 0.4667 | 0.6667 | 1      |
| final_score         | 0.0709 | 0.1635 | 0.2014 |   0.2374 | 0.29   | 0.3911 | 0.5362 | 0.9745 |
| technical_score     | 0      | 0      | 0      |   0.0424 | 0.0707 | 0.4571 | 0.5929 | 0.9966 |

## Ceiling / Saturation Checks
| score             |   ==1.0 |   >=0.99 |   >=0.95 |   >=0.90 |   unique_values |    std |
|:------------------|--------:|---------:|---------:|---------:|----------------:|-------:|
| technical_score   |       0 |        2 |       41 |       80 |            1278 | 0.1319 |
| career_score      |      64 |       66 |       81 |      103 |            1845 | 0.1401 |
| market_score      |       0 |        2 |       26 |      141 |           88400 | 0.1226 |
| consistency_score |   84239 |    84239 |    84339 |    84952 |              31 | 0.1516 |
| final_score       |       0 |        0 |       12 |       67 |           79783 | 0.0787 |

## Correlation With Final Score
| component_or_penalty   |   spearman_corr_with_final |
|:-----------------------|---------------------------:|
| technical_score        |                     0.8704 |
| career_score           |                     0.4325 |
| market_score           |                     0.4692 |
| consistency_score      |                     0.1006 |
| consistency_penalty    |                    -0.1006 |
| calibration_penalty    |                    -0.0186 |

## Dominant Positive Component Across All Candidates
| dominant_component   |   candidate_count |
|:---------------------|------------------:|
| consistency_score    |             47740 |
| market_score         |             39729 |
| technical_score      |              7093 |
| career_score         |              5438 |

## Weighted Contribution Summary For Top 100
| stat   |   technical_score |   career_score |   market_score |   consistency_score |
|:-------|------------------:|---------------:|---------------:|--------------------:|
| mean   |            0.4189 |          0.243 |         0.1667 |               0.087 |
| 50%    |            0.4232 |          0.25  |         0.1706 |               0.09  |
| max    |            0.4484 |          0.25  |         0.1962 |               0.1   |

## Assessment

Ranker V1 is directionally discriminative in the top tail, but calibration is imperfect. Once `career_score` saturates, ordering depends heavily on technical score repetition and market score. `consistency_score` is not broad enough because most candidates receive a perfect value.
