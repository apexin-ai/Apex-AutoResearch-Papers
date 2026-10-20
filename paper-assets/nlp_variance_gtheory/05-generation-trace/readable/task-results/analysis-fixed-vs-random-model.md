# analysis fixed vs random model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fixed_vs_random_model_20260522T132959_result.json`
- **Structured JSON:** [`9291a7b9e7c4c72ccda3.json`](../../sessions/92/9291a7b9e7c4c72ccda3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Computations verified. Here are the results:

## Fixed vs Random Model Sensitivity Analysis

| Benchmark | G_random | G_fixed | ΔG | σ²(m:i)/n_m as % of δ |
|-----------|----------|---------|--------|----------------------|
| MMLU | 0.8962 | 0.9841 | +0.088 | 86.0% |
| ARC | 0.8917 | 0.9900 | +0.098 | 91.7% |
| HellaSwag | 0.8716 | 0.9842 | +0.113 | 89.1% |
| GSM8K | 0.8629 | 0.9514 | +0.089 | 67.9% |
| MATH | 0.8880 | 0.9651 | +0.077 | 71.3% |
| **Mean** | **0.8821** | **0.9750** | **+0.093** | |

D-study n_items for G≥0.80: trivially **1** for both random and fixed, since even single-item G already exceeds 0.80. The G coefficient measures item-level reliability across evaluation conditions, not test-level reliability — so adding items doesn't enter the formula.

**Key findings:**

1. **Treating model as fixed inflates G by +0.077 to +0.113 (mean +0.093).** All fixed-model G values exceed 0.95, which would obscure the substantial model-dependent item difficulty variation.

2. **σ²(model:item)/n_model accounts for 68–92% of the total relative error variance.** This is the single dominant error component. Removing it (fixed-model assumption) eliminates most of the measurement error.

3. **The random-model treatment is defensible and more conservative.** Under fixed-model, the artificially high G values would suggest benchmarks are almost perfectly reliable — masking the reality that item rankings shift substantially across models. Since practitioners routinely apply benchmarks to new models not in the original 8, the random-model assumption better reflects the intended generalization scope.

JSON saved to `artifacts/exp004/data/fixed_vs_random_model.json`.

---
