# FF Benchmarks G-study Results (Henderson I + Bootstrap CI)

## GSM8K (8 models, 460,800 obs)
| Facet | σ²% | 95% CI |
|-------|-----|--------|
| residual | 39.89% | — |
| item_id | 16.86% | [13.32, 19.95] |
| model:item_id | 14.55% | [13.26, 15.82] |
| model | 10.75% | [9.14, 12.67] |
| model:prompt_template | 8.53% | [7.56, 9.75] |
| prompt_template | 5.41% | — |
| prompt_template:item_id | 3.06% | — |
| **G_item** | **0.2837** | [0.2386, 0.3302] |

## MATH (7 models — missing DeepSeek, 403,200 obs)
| Facet | σ²% | 95% CI |
|-------|-----|--------|
| residual | 43.24% | [40.96, 45.45] |
| item_id | 26.48% | [22.98, 29.84] |
| model:item_id | 16.07% | [14.69, 17.65] |
| model | 6.96% | [5.81, 8.29] |
| prompt_template:item_id | 3.39% | — |
| model:prompt_template | 1.69% | — |
| prompt_template | 1.09% | — |
| **G_item** | **0.3625** | [0.3230, 0.4012] |

## Key Finding
MATH item_id%=26.48% [22.98, 29.84] — NOT methodology-dominated. Breaks simple MC/FF dichotomy.
MATH difficulty heterogeneity (algebra → competition) drives higher item variance vs uniform GSM8K.