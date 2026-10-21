# monitor exp013f ray worker logs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013f-ray-worker-logs_20260514T095141_result.json`
- **Structured JSON:** [`12113bd3ba71839c61c6.json`](../../sessions/12/12113bd3ba71839c61c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 step 的数据都拿到了。

## exp013f 训练指标

| 指标 | Step 6 | Step 7 |
|------|--------|--------|
| **pg_loss** | 7.140e-05 | -2.467e-06 |
| **grad_norm** | 2.2289 | 1.7483 |
| **ppo_kl** | 0.001682 | 0.000617 |
| **entropy** | 0.09588 | 0.10335 |
| **pg_clipfrac** | 0.002555 | 0.002556 |

补充关键指标：
- **success rate**: step 6 = 1.56%, step 7 = 7.81%
- **pass@16**: 均为 25%
- **kl_loss**: step 6 = -0.02213, step 7 = 0.01257
- **time_per_step**: step 6 = 289.6s, step 7 = 585.2s
- **throughput**: step 6 = 420.7 tok/s, step 7 = 191.5 tok/s

训练进度：7/30 steps (23%)，进程存活中。

---
