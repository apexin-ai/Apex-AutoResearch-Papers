# analysis grid b1 5 seed123 finalize

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b1_5_seed123_finalize_20260514T111711_result.json`
- **Structured JSON:** [`1bccc8d5b5507c4e0476.json`](../../sessions/1b/1bccc8d5b5507c4e0476.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## grid_b1_5_seed123 结果

| 指标 | 值 |
|------|-----|
| **eval_ppl_holdout** | **17.701** |
| eval_loss | 2.8736 |
| train_loss | 10.478 |
| total_steps | 6103 |
| train_runtime_s | 15053 |
| gpu_hours | 4.18 |

## seed=123 grid-b 对比

| 方法 | b | PPL | Δ vs uniform |
|------|---|-----|-------------|
| grid | 0.5 | **17.638** | -0.052 |
| adaptive | — | 17.63 | -0.060 |
| grid | 1.0 | 17.674 | -0.016 |
| uniform | — | 17.69 | baseline |
| **grid** | **1.5** | **17.701** | **+0.011** |

趋势完全符合预期：b 越大 PPL 越高。b=1.5 开始超过 uniform baseline（17.701 > 17.69），说明过强的 provenance weighting 已产生负面效果。最优 b 在 0.5 附近，与 adaptive 方法的表现一致。

---
