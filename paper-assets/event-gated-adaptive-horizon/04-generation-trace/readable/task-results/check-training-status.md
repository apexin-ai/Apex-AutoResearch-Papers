# check training status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-status_20260513T030838_result.json`
- **Structured JSON:** [`5f3d635574d68fcf66a2.json`](../../sessions/5f/5f3d635574d68fcf66a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### 1. 进程存活
| 实验 | PID | 状态 |
|------|-----|------|
| Baseline (cuda:0) | 9409 | **存活** |
| Event-gated (cuda:1) | 9769 | **存活** |

### 2. GPU 利用率
| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|----------|--------|------|
| GPU 0 | RTX PRO 6000 (98GB) | 4720 MiB | 21% | 41°C |
| GPU 1 | RTX PRO 6000 (98GB) | 4343 MiB | 9% | 42°C |

注：PID 9769 (event-gated) 在 GPU 0 上也占了 552 MiB，主体在 GPU 1。

### 3. 训练进度
| 指标 | Baseline | Event-gated |
|------|----------|-------------|
| **当前 step** | 32,000 | 28,000 |
| **最近 train_return** | 401~510 | 177~200 |
| **最近 eval_return** (step 25k) | **395.27** | **186.59** |
| **update_count** (step 25k) | 5,099 | 5,099 |
| **FPS** | 7.42 | 6.67 |
| **episodes** | 32 | 28 |

Baseline 明显领先，event-gated 的 return 约为 baseline 的一半。

### 4. Gate 相关指标
Event-gated 日志中已记录以下 gate 字段：

- `gate_loss`: 0.0
- `gate_scale`: 0.0
- `gate_entropy_bonus`: 0.098
- `gate_dt_mean`: **1.0**（gate 目前全选 dt=1）
- `gate_dt_std`: 0.0
- `gate_dt_min`/`max`: 1.0 / 1.0
- `gate_dt_{1..8}_frac`: dt_1=100%, 其余全 0%
- `gate_empirical_entropy`: **0.0**
- `gate_entropy_ratio`: **0.0**

**关键问题**：gate 完全坍缩到 dt=1，没有任何多步预测。entropy bonus 为 0.098 但 gate_scale=0.0，说明 entropy 正则化没有实际生效。这可能是 gate 不探索的原因。

### 5. 无崩溃
两个实验均正常运行中，日志持续更新（最后写入时间 11:07）。

---
