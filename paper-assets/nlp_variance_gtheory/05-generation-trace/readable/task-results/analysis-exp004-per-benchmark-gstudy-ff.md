# analysis exp004 per benchmark gstudy ff

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_per_benchmark_gstudy_ff_20260521T213125_result.json`
- **Structured JSON:** [`255714c9fa899cfaa12a.json`](../../sessions/25/255714c9fa899cfaa12a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the full results:

## Results Summary

### GSM8K (8 models, 460,800 obs)
| Facet | σ²% | 95% CI |
|-------|-----|--------|
| **residual** | 39.89% | — |
| **item_id** | 16.86% | [13.32, 19.95] |
| **model:item_id** | 14.55% | [13.26, 15.82] |
| **model** | 10.75% | [9.14, 12.67] |
| **model:prompt_template** | 8.53% | [7.56, 9.75] |
| **prompt_template** | 5.41% | — |
| prompt_template:item_id | 3.06% | — |
| G_item = **0.2837** | CI: [0.2386, 0.3302] |

### MATH (7 models, 403,200 obs)
| Facet | σ²% | 95% CI |
|-------|-----|--------|
| **residual** | 43.24% | [40.96, 45.45] |
| **item_id** | **26.48%** | [22.98, 29.84] |
| **model:item_id** | 16.07% | [14.69, 17.65] |
| **model** | 6.96% | [5.81, 8.29] |
| prompt_template:item_id | 3.39% | — |
| model:prompt_template | 1.69% | — |
| prompt_template | 1.09% | — |
| G_item = **0.3625** | CI: [0.3230, 0.4012] |

### Key Findings

1. **MATH item_id% = 26.48% (>20%)** — MATH is NOT methodology-dominated. CIs don't overlap with 20%: [22.98, 29.84].

2. **GSM8K item_id% = 16.86% (<20%)** — GSM8K IS methodology-dominated, as expected. CI upper bound touches 20% (19.95%).

3. **GSM8K vs MATH item_id% diff = −9.62 pp** — MATH has substantially more item variance than GSM8K.

4. **Simple format-conditional dichotomy does NOT hold**: both are free-form, but their variance structures differ. MATH shows a mix of item-driven and methodology-driven variance, while GSM8K is more methodology-driven.

5. **Possible explanation**: MATH items span multiple difficulty levels (algebra to competition problems), creating higher item heterogeneity. GSM8K items are more uniform in difficulty structure.

6. **Ordering facet**: confirmed as structural no-op (0% variance) for both benchmarks.

### JSON output
`results/exp004_8model_analysis/per_benchmark_gstudy_ff.json` on westd-32570.

---
