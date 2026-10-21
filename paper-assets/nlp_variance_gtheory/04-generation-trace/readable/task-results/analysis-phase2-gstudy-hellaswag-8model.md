# analysis phase2 gstudy hellaswag 8model

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_gstudy_hellaswag_8model_20260521T222217_result.json`
- **Structured JSON:** [`d093d9b844e8f720ba70.json`](../../sessions/d0/d093d9b844e8f720ba70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。HellaSwag 8-model Henderson I G-study 结果：

## 方差分解（N=691,200, 8 models × 3 temps × 6 prompts × 6 seeds × 4 orderings × 200 items）

| Component | % | 95% CI |
|-----------|--:|--------|
| model:temperature | 36.44 | [33.70, 39.77] |
| temperature | 20.80 | [19.21, 22.71] |
| residual | 17.81 | [16.08, 19.33] |
| model:item_id | 10.84 | [9.48, 12.16] |
| item_id | 8.91 | [6.96, 10.98] |
| temperature:item_id | 4.43 | [3.58, 5.26] |
| prompt_template:item_id | 0.63 | [0.53, 0.74] |
| 其余 | <0.1 | — |
| **ordering:item_id** | **0.00** | **[0.00, 0.00]** |

## G_item
**0.751** [0.719, 0.780] — 200 items 下 item 难度排序的可靠性中等偏高。D-study: 需 ~500 items 达到 G≥0.88。

## R1-W4: ordering:item_id 交互

**结论：8-model 分析中 ordering:item_id = 0.00%，500 次 bootstrap 中 100% 为零，所有 8 个模型单独分析均为零。**

6-model 时 HellaSwag 的 3.93% 是一个采样 artifact（可能由 OLMo/Yi 缺失导致的不平衡设计引起），扩展到 8 个完全交叉模型后消失。选项排列顺序对 item 难度没有系统性差异影响。

---
