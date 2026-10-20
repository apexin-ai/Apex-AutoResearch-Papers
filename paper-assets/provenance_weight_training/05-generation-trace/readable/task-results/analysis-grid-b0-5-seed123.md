# analysis grid b0 5 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b0_5_seed123_20260514T103434_result.json`
- **Structured JSON:** [`777fb7542a7528babf2e.json`](../../sessions/77/777fb7542a7528babf2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `grid_b0_5_seed123` 分析完成，已标记 DONE。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| eval_ppl_holdout | **17.638** |
| eval_loss | 2.870 |
| eval_holdout_tokens | 4,077,068 |
| train_loss | 9.601 |
| total_steps | 6,103 |
| train_runtime | 13,104s (~3.64h) |
| GPU hours | 3.8h |

**Baseline 对比：**

| 实验 | eval_ppl_holdout | vs uniform |
|------|-----------------|------------|
| uniform (seed123) | 17.690 | — |
| **grid_b0.5 (seed123)** | **17.638** | **-0.052** |
| adaptive (seed123) | 17.630 | -0.060 |
| grid_b0.5 (seed42) | 17.651 | — |

grid_b=0.5 在 seed123 上优于 uniform baseline，与 seed42 结果一致（17.638 vs 17.651），略逊于 adaptive（17.638 vs 17.630）。训练未启用 W&B。

---
