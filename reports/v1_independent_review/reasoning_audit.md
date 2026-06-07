# Reasoning Quality Audit

## Direct Answers

1. Explanations are somewhat candidate-specific, but only through detected terms, relevant-role counts, relevant duration, notice period, and broad flags.
2. Explanations are mostly templates. Exact unique explanations across all candidates: **2634** out of **100000**. Top 100 unique explanations: **99** out of 100.
3. Explanations expose evidence categories and some matched terms, but not role snippets, role titles, company names, source weights, or dates.
4. Yes. Very different candidates can receive nearly identical explanations if they share the same term buckets and role counts.
5. Missing information: exact source role, matched source text, tier/source contribution, market signal values, consistency reason details, and score-cap explanation.

## Duplicate Explanation Evidence
| scope          |   rows |   unique_reasonings |   most_common_count |   no_strong_evidence_count |
|:---------------|-------:|--------------------:|--------------------:|---------------------------:|
| all candidates | 100000 |                2634 |               17210 |                          0 |
| top 100        |    100 |                  99 |                   2 |                          0 |

## Most Common Explanations Overall
| reasoning                                                                                                                                                          |   count |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------:|
| Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence                                                                   |   17210 |
| Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (90 days)                                   |   13867 |
| Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (120 days)                                  |    7858 |
| Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; longer notice period (150 days)                                  |    6751 |
| Positives: product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence                                  |    4213 |
| Concerns: limited ranking/relevance career evidence                                                                                                                |    3700 |
| Positives: product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; longer notice period (90 days)  |    3553 |
| Concerns: limited ranking/relevance career evidence; longer notice period (90 days)                                                                                |    3062 |
| Positives: product/SaaS company experience | Concerns: limited ranking/relevance career evidence; profile consistency concerns                                     |    2072 |
| Positives: product/SaaS company experience; solid market engagement signals | Concerns: limited ranking/relevance career evidence; longer notice period (120 days) |    1950 |

## Source Review

`src/ranker/reasoning_generator.py` builds positives from a short ordered list: ranking evidence, retrieval evidence, vector evidence, relevant role count/duration, product/SaaS experience, and market signal buckets. Concerns are similarly templated: limited ranking evidence, keyword stuffing, AI transition, long notice period, consistency concerns, and consulting-heavy path.

## Assessment

The reasoning is deterministic and safe, which is good for V1. It is not yet sufficiently evidentiary for independent review because it does not let a reviewer trace a claim back to the underlying profile. V2 should emit structured evidence objects and render concise snippets from actual role descriptions.
