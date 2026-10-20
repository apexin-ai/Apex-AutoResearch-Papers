# check exp 005 progress 120K

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_005_progress_120K_20260513T213159_result.json`
- **Structured JSON:** [`f402a524cc843466c457.json`](../../sessions/f4/f402a524cc843466c457.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_005_event_gated_v4 状态汇报

**进程**: 存活，运行中（PID 51726，已运行 ~57h，CPU 99%）
- 任务: `dmc_walker_walk`，目标 500k steps，GPU: `cuda:1`

**当前进度**: step **136,000** / 500,000（27.2%），FPS: 7.05

### 最新 metrics（step 135,000）

| 指标 | 值 |
|------|-----|
| **eval_return** | **47.38** |
| gate_scale | 0.800 |
| gate_dt_mean | 2.44 |
| gate_dt_std | 1.27 |
| gate_empirical_entropy | 1.54 |
| gate_entropy_ratio | 0.859 |

**Gate dt 分布**: dt=1: 25.8%, dt=2: 33.1%, dt=3: 22.5%, dt=4: 10.6%, dt=5: 5.2%, dt=6: 2.7%

### eval_return 趋势

| step | eval_return |
|------|------------|
| 5k | 31.0 |
| 15k | 153.9 |
| 25k | 254.2 |
| 35k | 290.8 |
| 45k | 443.0 |
| 55k | **541.2** (peak) |
| 65k | 465.7 |
| 75k | 482.1 |
| 85k | 212.3 |
| 95k | 258.5 |
| 105k | 276.1 |
| 115k | 25.7 |
| 125k | 38.7 |
| 135k | 47.4 |

**问题**: eval_return 在 55k 达到峰值 541 后持续下降，85k 起大幅崩溃，当前 47.4 仅为峰值的 8.7%。训练出现严重的 performance collapse。

---
