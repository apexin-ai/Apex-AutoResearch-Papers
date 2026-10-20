# monitor live metrics check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_live-metrics-check_20260515T043832_result.json`
- **Structured JSON:** [`9903c4a036662b726def.json`](../../sessions/99/9903c4a036662b726def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行。

## exp_009a_baseline_walker_s2 (PID 142508)

| 指标 | 值 |
|------|-----|
| 当前 step | **455K** / 500K (91.0%) |
| 最新 eval (445K) | eval_return = **948.42** |
| value_mean (445K) | 664.44 |
| FPS | 7.34 |
| 进程运行时间 | 19h 05m |
| 预估剩余 | 45K steps / 7.34 fps ≈ **1.7h** |

训练表现稳定，train_return 在 880-988 区间波动，eval 从 425K 的 939 升至 445K 的 948。

---

## exp_008e_v3_walker_s2 (PID 43437)

| 指标 | 值 |
|------|-----|
| 当前 step | **80K** / 105K (76.2%) |
| 最新 eval (75K) | eval_return = **576.54** |
| value_mean (75K) | 272.64 |
| **v/e ratio** | 272.64 / 576.54 = **0.473** |
| FPS | 6.39 |
| 进程运行时间 | 3h 52m |
| 预估剩余 | 25K steps / 6.39 fps ≈ **1.1h** |

eval_return 从 45K 的 357 → 55K 的 418 → 65K 的 542 → 75K 的 577，持续上升。gate_dt_mean = 1.0，gate 全选 dt=1（未使用长 horizon）。

---

**异常：无。** 两个实验均正常运行，008e 预计约 1h 后完成，009a 约 1.7h 后完成。

---
