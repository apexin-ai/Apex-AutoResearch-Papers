# monitor exp 098 099 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_098_099_progress_20260526T021334_result.json`
- **Structured JSON:** [`3e564497eb9446f2d4c6.json`](../../sessions/3e/3e564497eb9446f2d4c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

| | exp_098 (s0, cuda:0) | exp_099 (s1, cuda:1) |
|---|---|---|
| **当前 step** | 8,000 | 8,000 |
| **总步数** | 105,000 | 105,000 |
| **完成度** | **7.6%** | **7.6%** |
| **已运行** | ~9h 04m | ~9h 02m |
| **速度** | ~889 steps/h | ~889 steps/h |
| **预估剩余** | **~109h (~4.5天)** | **~109h (~4.5天)** |
| **状态** | 运行中 (日志 10:11 仍在写入) | 运行中 (日志 10:11 仍在写入) |

### 最新 Metrics

**Eval (step 5000)**:
- exp_098: `eval_return = 8.3`
- exp_099: `eval_return = 13.5`

**Train return (step 8000, 4 episodes)**:
- exp_098: 10.7 / 12.9 / 12.1 / 12.5 (均值 ~12.1)
- exp_099: 13.1 / 12.1 / 17.0 / 10.8 (均值 ~13.3)

**Model loss (step 5000)**:
- 两个实验基本一致: `model_loss≈13.0`, `position_loss≈0.5`, `velocity_loss≈5.0`, `reward_loss≈3.2`, `kl≈7.2`

**Gate 统计**: `gate_fixed_dt=2`, `gate_dt_2_frac=1.0` (100% 固定 dt=2, 符合配置)

### 注意

ETA ~4.5天偏长。前 8000 步包含 prefill (2500步)、模型初始化、首次 eval 的开销，后续纯训练速度可能更快。建议下次 log 刷新后（预计 step ~11000）再看实际训练速率是否提升。

---
