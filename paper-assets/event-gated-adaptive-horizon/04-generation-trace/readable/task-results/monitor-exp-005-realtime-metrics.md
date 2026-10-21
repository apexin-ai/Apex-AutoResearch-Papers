# monitor exp 005 realtime metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_005_realtime_metrics_20260513T183343_result.json`
- **Structured JSON:** [`c50eeac3ad6f74fd173f.json`](../../sessions/c5/c50eeac3ad6f74fd173f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 实验状态

| | exp_001 (baseline) | exp_005 (event_gated_v4) |
|---|---|---|
| **Step** | 448K / 500K (89.6%) | 65K / 500K (13%) |
| **Eval Return** | **953.4** @445K | **465.7** @65K |
| **Train Return** | 930-976 @448K | 535-602 @64K |
| **FPS** | 7.29 | 6.69 |
| **GPU** | cuda:0, 1% util, 4.2GB | cuda:1, 22% util, 4.2GB |
| **运行时间** | ~16.5h | ~2.4h |

## exp_005 Gate 指标（Phase 2 信号）

| 指标 | @55K | @65K | 变化 |
|---|---|---|---|
| **gate_scale** | 0.013 | **0.100** | **7.7x 上升** |
| **gate_dt_mean** | 1.000 | **1.035** | 开始偏离 1 |
| **gate_dt_2_frac** | 0.0% | **3.5%** | 首次出现 dt>1 |
| **gate_loss** | 0.000 | 0.007 | 开始产生梯度 |
| **gate_entropy** | 0.000 | 0.050 | 开始探索 |

**Phase 2 已激活。** gate_scale 从 55K→65K 增长了约 8 倍，3.5% 的 imagination step 开始使用 dt=2。gate 正在从"全部 dt=1"状态过渡到主动探索不同时间步长。目前仍处于早期阶段——绝大多数（96.5%）仍选择 dt=1，但趋势明确。

exp_001 baseline 接近完成（89.6%），eval_return 953.4 已趋于稳定。无 error/warning。

---
