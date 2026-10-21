# analysis exp status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-status-check_20260521T121718_result.json`
- **Structured JSON:** [`a719a5f4f65dbee13239.json`](../../sessions/a7/a719a5f4f65dbee13239.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇报

### exp_035_narrow_dual_critic_walker (bjb1-40020)

| 项目 | 值 |
|------|-----|
| 进程 | PID 162900 存活，已运行 4h 22m |
| 进度 | **120,000 / 210,000** (57.1%) |
| 最近 eval (step 115k) | eval_return = **114.8**, ve_ratio = **0.7** |
| 近期 train_return | 56.9 ~ 184.9（波动大，100k 附近出现过 200+） |
| Gate | dt_mean=2.0, dt_2_frac=1.0（**gate 锁死在 dt=2**） |
| GPU (cuda:1) | 16% util, 3121 MiB / 24564 MiB |
| 速率 | ~7.6 steps/sec (120k steps / 15709s) |
| **预计剩余** | **~3h 17m**（约 UTC 15:35 完成） |

### exp_036_dual_critic_pickcube (bjb1-45299)

| 项目 | 值 |
|------|-----|
| 进程 | PID 2476 存活，已运行 3h 34m |
| 进度 | **74,047 / 200,000** (37.0%) |
| 最近 eval (step 72.5k) | eval_return = **5.4**, ve_ratio = **1.6** |
| 近期 train_return | 0.4 ~ 19.2（较低，pick-cube 任务本身难度大） |
| Gate | dt_mean=2.0, dt_2_frac=1.0（**gate 锁死在 dt=2**） |
| GPU (cuda:0) | 29% util, 3135 MiB / 97887 MiB |
| 速率 | ~5.8 steps/sec (74k steps / 12851s) |
| **预计剩余** | **~6h 3m**（约 UTC 18:20 完成） |

### 需要注意

两个实验的 **gate 均锁死在 dt=2**（gate_empirical_entropy=0, dt_2_frac=1.0），自适应 horizon 机制没有激活。如果这不符合预期，可能需要检查 gate 的温度/探索参数配置。

---
