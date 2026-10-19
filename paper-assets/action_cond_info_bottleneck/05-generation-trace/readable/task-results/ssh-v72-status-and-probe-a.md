# ssh v72 status and probe a

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v72-status-and-probe-a_20260517T124629_result.json`
- **Structured JSON:** [`e8b783ed507d04b8888e.json`](../../sessions/e8/e8b783ed507d04b8888e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态：仍在跑

| | Seed 1 | Seed 2 |
|---|---|---|
| **当前 step** | 16000/20000 | 16000/20000 |
| **速度** | 1.8 steps/s | 1.8 steps/s |
| **已有 checkpoints** | 5000, 10000, 15000 | 5000, 10000, 15000 |
| **checkpoint-20000** | 不存在 | 不存在 |

**ETA**：剩余 4000 steps ÷ 1.8 steps/s ≈ **37 分钟**（约 21:24 UTC 完成）。

训练指标看着正常：scorer_mean ~0.39-0.43，std ~0.31-0.34，loss 稳定在 0.2-0.35 区间。

训练完成后需要立即启动 Probe A。

---
