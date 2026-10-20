# analysis phase2 gstudy arc 8model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_gstudy_arc_8model_20260521T220409_result.json`
- **Structured JSON:** [`e455068b0fac30f9d8b3.json`](../../sessions/e4/e455068b0fac30f9d8b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered. Here are the complete results:

---

## ARC 8-Model Henderson I G-Study Results

**Design**: 8 models × 2 temperatures × 6 prompts × 6 seeds × 4 orderings × 200 items = **460,800** observations  
**Grand mean accuracy**: 0.7725  
**G_item**: **0.8917** [95% CI: 0.8565, 0.9183] (SE = 0.0166)  
**Min items for G ≥ 0.80**: **98**

### Variance Components

| Component | Estimate | %Var | 95% CI (%Var) |
|---|---|---|---|
| **item_id** | 0.06712 | **37.88%** | [30.37, 45.32] |
| **model:item_id** | 0.05976 | **33.73%** | [29.12, 37.87] |
| residual | 0.02737 | 15.44% | [13.43, 17.45] |
| model:prompt_template | 0.01418 | 8.00% | [6.48, 10.03] |
| model | 0.00545 | 3.08% | [1.94, 4.99] |
| prompt_template:item_id | 0.00257 | 1.45% | [1.24, 1.70] |
| temperature:item_id | 0.00038 | 0.21% | [0.13, 0.33] |
| seed:item_id | 0.00030 | 0.17% | [0.12, 0.22] |
| model:seed | 0.00003 | 0.02% | |
| model:temperature | 0.00002 | 0.01% | |
| temperature:prompt_template | 0.00001 | <0.01% | |
| prompt_template:seed | 0.00001 | <0.01% | |
| temperature:seed | 0.00001 | <0.01% | |
| ordering (all interactions) | 0.00000 | 0.00% | |
| temperature / prompt_template / seed / ordering (main) | 0.00000 | 0.00% | |

### D-Study Curve

| Items | G_item |
|---|---|
| 25 | 0.507 |
| 50 | 0.673 |
| 75 | 0.755 |
| **98** | **0.800** |
| 100 | 0.805 |
| 200 | 0.892 |
| 500 | 0.954 |
| 1000 | 0.976 |

### Key Findings

- **item_id (37.9%)** dominates — consistent with the 6-model ARC reference (~38%), confirming item difficulty is the primary variance source
- **model:item_id (33.7%)** is the second largest — models disagree substantially on which items are hard, the DIF-like interaction
- **model:prompt_template (8.0%)** — models respond differently to prompt formats
- **ordering** contributes exactly 0% across all interactions — answer option shuffling has no effect on ARC
- **G_item = 0.89** with 200 items; only 98 items needed for G ≥ 0.80

JSON saved: `westd-32570:results/exp004_8model_analysis/per_benchmark_gstudy_arc.json`

---
