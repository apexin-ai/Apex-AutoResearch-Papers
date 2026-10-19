# analysis eval loss variants object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-loss-variants-object_20260522T103936_result.json`
- **Structured JSON:** [`74948eca37892b61bf92.json`](../../sessions/74/74948eca37892b61bf92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都正常完成，无错误。结果如下：

## eval-loss-conformal-object-seed42 (Conformal-guided CRM)
- **avg_success_rate: 6.0%**
- **total_successes: 12/200**
- per_task:

| Task | Rate | Successes |
|------|------|-----------|
| alphabet_soup | 0.0% | 0/20 |
| cream_cheese | 5.0% | 1/20 |
| salad_dressing | 0.0% | 0/20 |
| bbq_sauce | 10.0% | 2/20 |
| ketchup | 0.0% | 0/20 |
| tomato_sauce | 5.0% | 1/20 |
| butter | 0.0% | 0/20 |
| milk | 10.0% | 2/20 |
| chocolate_pudding | **20.0%** | 4/20 |
| orange_juice | 10.0% | 2/20 |

- **conclusion: NEGATIVE** — 6.0% < MSE baseline 7%，远低于 Plan A 18.3%。训练阶段 val_loss 已经 6.4x worse，eval 印证了这一点。

---

## eval-loss-perdof-object-seed42 (Per-DOF weighted CRM)
- **avg_success_rate: 4.0%**
- **total_successes: 8/200**
- per_task:

| Task | Rate | Successes |
|------|------|-----------|
| alphabet_soup | 0.0% | 0/20 |
| cream_cheese | 5.0% | 1/20 |
| salad_dressing | 0.0% | 0/20 |
| bbq_sauce | 5.0% | 1/20 |
| ketchup | 5.0% | 1/20 |
| tomato_sauce | 0.0% | 0/20 |
| butter | 10.0% | 2/20 |
| milk | 5.0% | 1/20 |
| chocolate_pudding | 5.0% | 1/20 |
| orange_juice | 5.0% | 1/20 |

- **conclusion: NEGATIVE** — 4.0% < MSE baseline 7%，远低于 Plan A 18.3%。尽管训练阶段 val_loss 16.8x better than MSE，eval 成功率反而最差。

---

## 综合对比

| Method | Success Rate | vs MSE (7%) | vs Plan A (18.3%) |
|--------|-------------|-------------|-------------------|
| Plan A CRM (K=2) | **18.3%±2.1%** | +11.3pp | — |
| VLA-only | 10.8%±1.3% | +3.8pp | -7.5pp |
| MSE re-trained | 7.0% | — | -11.3pp |
| **Conformal-guided** | **6.0%** | **-1.0pp** | **-12.3pp** |
| **Per-DOF weighted** | **4.0%** | **-3.0pp** | **-14.3pp** |

关键发现：**val_loss 与 eval 成功率脱钩**。Per-DOF weighted 训练 loss 最优（16.8x better），但 eval 最差（4.0%）。说明这两个 loss 变体优化的目标与实际 task success 不对齐——低 loss 不等于好 correction。

---
