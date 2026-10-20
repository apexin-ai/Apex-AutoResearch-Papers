# analyze grid b0 5 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grid_b0_5_seed456_20260515T005933_result.json`
- **Structured JSON:** [`6ae9ee718d1b02123bf3.json`](../../sessions/6a/6ae9ee718d1b02123bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

grid_b0_5_seed456 已更新为 DONE(success)。

## 汇总

**grid_b0_5_seed456** — 完成全部处理：
| 指标 | 值 |
|------|-----|
| train_loss | 9.5622 |
| total_steps | 6103 |
| train_runtime | 12953.96s (3.6 GPU hours) |
| train_samples/s | 7.538 |
| **eval_ppl_holdout** | **17.65** |
| eval_loss | 2.8705 |
| eval_holdout_tokens | 4,077,068 |

**grid_b1_0_seed456** 和 **grid_b1_5_seed456** 在 registry 中已有 eval_ppl_holdout（分别为 17.68 和 17.71），无需额外 eval。

### seed456 grid-b 全景（eval_ppl_holdout）

| b 值 | eval_ppl |
|------|----------|
| 0.5 | **17.65** |
| 1.0 | 17.68 |
| 1.5 | 17.71 |

趋势与 seed42/seed123 一致：b=0.5 最优。

---
