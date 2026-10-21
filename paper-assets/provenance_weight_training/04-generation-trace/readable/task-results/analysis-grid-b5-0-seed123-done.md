# analysis grid b5 0 seed123 done

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b5_0_seed123_done_20260514T151241_result.json`
- **Structured JSON:** [`535a60711c81443f1617.json`](../../sessions/53/535a60711c81443f1617.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## grid_b5_0_seed123 完整 metrics

| Metric | Value |
|--------|-------|
| train_loss (HF weighted) | 10.8468 |
| total_steps | 6,103 |
| train_runtime_s | ~14,434 |
| gpu_hours | 4.01 |
| **eval_ppl_holdout** | **17.8039** |
| eval_loss | 2.8794 |
| eval_holdout_tokens | 4,077,068 |

seed123 grid-b 曲线完整数据点（eval_ppl_holdout）：

| b | eval_ppl |
|---|----------|
| 0.5 | 17.638 |
| 1.0 | 17.674 |
| 1.5 | 17.701 |
| 2.0 | 17.725 |
| 3.0 | 17.760 |
| **5.0** | **17.804** |

趋势清晰：b 越大 eval_ppl 越高（越差），b=5.0 是曲线最右端的点，eval_ppl = 17.804。

---
