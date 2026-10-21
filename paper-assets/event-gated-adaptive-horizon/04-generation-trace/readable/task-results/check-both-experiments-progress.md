# check both experiments progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_both_experiments_progress_20260513T183531_result.json`
- **Structured JSON:** [`8dcba5d1cc67dc05e45a.json`](../../sessions/8d/8dcba5d1cc67dc05e45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### exp_001_baseline (PID 9409, cuda:0)

| 指标 | 值 |
|------|-----|
| 进程状态 | ✅ 存活（CPU 1131%） |
| 当前 step | **452K** / 500K（90.4%） |
| 最新 eval_return | **953.37** @ step 445K |
| 上一次 eval_return | 964.96 @ step 435K |
| train_return (近期) | 917~986 @ 452K |
| FPS | 7.29 |
| 预计剩余 | ~48K steps，约 1.8 小时完成 |

Baseline 表现稳定，eval_return 在 950+ 区间，即将完成。

---

### exp_005_event_gated_v4 (PID 51726, cuda:1)

| 指标 | 值 |
|------|-----|
| 进程状态 | ✅ 存活（今日 00:08 启动） |
| 当前 step | **65K** / 500K（13%） |
| 最新 eval_return | **465.67** @ step 65K |
| 上一次 eval_return | 541.18 @ step 55K |
| train_return (近期) | 535~602 @ 64K |
| FPS | 6.69 |

**Gate 状态变化（重点）：**

| step | gate_scale | gate_loss | gate_dt_mean | dt=1 占比 | dt=2 占比 | empirical_entropy |
|------|-----------|-----------|-------------|----------|----------|-------------------|
| 45K | 0.0 | 0.0 | 1.0 | 100% | 0% | 0.0 |
| 55K | **0.0125** | 0.0 | 1.0 | 100% | 0% | 0.0 |
| 65K | **0.100** | **0.0066** | **1.035** | **96.5%** | **3.5%** | **0.050** |

**Gate 已开始激活。** gate_scale 从 0 → 0.10，gate 开始产生少量 dt>1 的预测（3.5% 选择 dt=2）。entropy 从 0 升至 0.05，gate 正在探索。

**⚠️ 注意：** eval_return 从 55K 的 541 下降到 65K 的 466，可能与 gate 激活初期引入的不稳定性有关。需要继续观察后续 eval 是否恢复。

---
