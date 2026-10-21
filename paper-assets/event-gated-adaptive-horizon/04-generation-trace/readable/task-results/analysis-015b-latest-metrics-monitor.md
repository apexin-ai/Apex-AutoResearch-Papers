# analysis 015b latest metrics monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_015b_latest_metrics_monitor_20260515T173630_result.json`
- **Structured JSON:** [`996680c23dd9c6040a9e.json`](../../sessions/99/996680c23dd9c6040a9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_015b 进度报告

**状态：仍在运行** (PID 149991, elapsed 5h11m)

**当前 step：92K / 105K** (~88% 完成)

### 75K 之后的 eval checkpoint

| Step | eval_return | actor_loss | actor_entropy | value_mean | value_std |
|------|------------|------------|---------------|------------|-----------|
| 75K | 80.0 | -0.00182 | -5.095 | 60.33 | 13.92 |
| 85K | 183.5 | +0.00061 | -5.101 | 60.09 | 14.04 |

### 分析

- **eval_return**：85K 回弹到 183.5（75K 时是 80.0），但这可能是噪声——整体轨迹从 35K 峰值 201.6 后一直震荡下行（45K→122, 55K→106, 65K→160, 75K→80），不构成恢复趋势
- **gradient starvation 持续**：actor_loss ≈ 0（-0.0018 → +0.0006），actor_entropy 稳定在 -5.1，gate 100% 锁死在 dt=2（gate_empirical_entropy=0）。frozen dt_emb 导致 gate 完全失去自由度，actor 梯度饥饿的机制未变
- **value function 稳定**：value_mean ≈ 60, value_std ≈ 14，未崩溃

### 预计完成时间

当前 92K，fps ≈ 6.9（85K checkpoint），剩余 13K steps，预计 ~30-50 分钟完成。下一个 eval checkpoint 在 95K。

---
