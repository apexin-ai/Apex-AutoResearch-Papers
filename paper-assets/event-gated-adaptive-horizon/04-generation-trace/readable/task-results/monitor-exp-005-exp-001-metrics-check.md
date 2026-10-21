# monitor exp 005 exp 001 metrics check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_005_exp_001_metrics_check_20260513T183904_result.json`
- **Structured JSON:** [`e359363c93a6578928d8.json`](../../sessions/e3/e359363c93a6578928d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## exp_001_baseline
| 指标 | 值 |
|------|-----|
| 进程 | 运行中 (PID 9409, 已运行 16h35m) |
| 最新 step | 452K (train) / 445K (eval) |
| eval_return | **953.4** @ 445K |
| train_return | 917~986 (均值 ~958) |
| fps | 7.29 |
| 预计完成 | ~1.8h 后 |

## exp_005_event_gated_v4
| 指标 | 值 |
|------|-----|
| 进程 | 运行中 (PID 51721, 已运行 2h31m) |
| 最新 step | 65K |
| eval_return | **465.7** @ 65K (↓14% from 541.2 @ 55K) |
| train_return | 535~602 |
| gate_scale | 0.100 (刚进入 phase 2) |
| gate_dt_1_frac | 96.5% (gate 几乎未激活) |
| gate_empirical_entropy | 0.050 |
| fps | 6.69 |
| vs baseline@65K | 465.7 vs 615.9 (**落后 150 点, 75%**) |

### ⚠ Alert: return_declining_at_phase2_onset

eval_return 在 55K→65K 下降 14% (541→466)，与 gate_scale 从 0.01→0.10 的 phase 2 启动精确同步。这与 exp_003 的崩塌模式相似。但两个缓和因素：
1. baseline 同期也小幅回调 (626→616, -1.6%)
2. gate 实际上几乎没激活 (96.5% 仍为 dt=1)

需要在 75K checkpoint 确认是正常波动还是持续下滑。

---
