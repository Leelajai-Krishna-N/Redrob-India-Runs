# Behavioral Signal Segmentation

Exploratory buckets only. These are not scores and are not ranking labels.

## Bucket Definitions
- `highly_active`: active within 14 days, recruiter response >= 0.65, high search or save volume, interview completion >= 0.70.
- `moderately_active`: active within 45 days, recruiter response >= 0.35, interview completion >= 0.45, and not highly active.
- `dormant`: inactive for more than 90 days, or very low response plus bottom-quartile search/save activity.
- `passive`: remaining candidates.

## Segment Summary
| behavior_segment   |   candidates |   median_days_since_last_active |   median_recruiter_response_rate |   median_search_appearance_30d |   median_saved_by_recruiters_30d |   median_interview_completion_rate |
|:-------------------|-------------:|--------------------------------:|---------------------------------:|-------------------------------:|---------------------------------:|-----------------------------------:|
| dormant            |        61319 |                             157 |                             0.43 |                          102   |                                7 |                               0.62 |
| highly_active      |          208 |                              11 |                             0.78 |                          225.5 |                               17 |                               0.82 |
| moderately_active  |         9255 |                              27 |                             0.58 |                          117   |                                8 |                               0.67 |
| passive            |        29218 |                              59 |                             0.37 |                          110   |                                7 |                               0.61 |