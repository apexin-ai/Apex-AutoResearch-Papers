# analysis 3x3 dstudy budget

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_3x3_dstudy_budget_20260522T145106_result.json`
- **Structured JSON:** [`76818510786dad236df1.json`](../../sessions/76/76818510786dad236df1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File saved correctly. Here's the summary:

**D-study: Model-as-Object — min items for G_model ≥ 0.80**

| Benchmark | Full (288/item) | 3×3 (9/item) | Single (1/item) |
|-----------|-----------------|--------------|-----------------|
| **MMLU** | 75 items → 21,600 evals | 347 items → 3,123 evals | **impossible** (max G=0.63) |
| **ARC** | **impossible** (max G=0.70) | **impossible** (max G=0.53) | **impossible** (max G=0.28) |
| **HellaSwag** | 29 items → 8,352 evals | 32 items → 288 evals | 53 items → 53 evals |
| **GSM8K** | 13 items → 3,744 evals | **impossible** (max G=0.79) | **impossible** (max G=0.55) |
| **MATH** | 10 items → 2,880 evals | 15 items → 135 evals | 146 items → 146 evals |

Key findings:

1. **ARC** can never reach G≥0.80 under any design — σ²(model:prompt) = 0.0142 is 2.6× σ²(model) = 0.0054. Model rankings on ARC are fundamentally prompt-dependent.

2. **GSM8K** needs the full 6-prompt design; 3×3 barely misses (asymptotic G=0.79) because model:prompt interaction is huge (0.0213).

3. **HellaSwag** is the most robust — reaches G≥0.80 with just 32 items × 9 conditions = 288 evals.

4. **3×3 cost savings** are dramatic where feasible: MMLU 3,123 vs 21,600 evals (85% reduction); MATH 135 vs 2,880 (95% reduction); HellaSwag 288 vs 8,352 (97% reduction).

5. **Single-condition** evaluation can only reach G≥0.80 for HellaSwag (53 items) and MATH (146 items). For the rest, no amount of items suffices.

Output saved to `artifacts/exp004/data/dstudy_3x3_budget.json`.

---
