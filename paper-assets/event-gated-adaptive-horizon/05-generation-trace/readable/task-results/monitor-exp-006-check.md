# monitor exp 006 check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_006_check_20260514T004155_result.json`
- **Structured JSON:** [`9401338dd821e59f611c.json`](../../sessions/94/9401338dd821e59f611c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_006_fixed_dt2 状态报告

**进程状态**: Running (PID 85029, elapsed 2h30m)

**当前步数**: 60,000 / 150,000 (40%)

**FPS**: ~6.5

**预计剩余时间**: 90K steps / 6.5 FPS ≈ 3.8 hours（预计 ~12:00 UTC 完成）

**Checkpoint**: `latest.pt` 存在 (231MB, 更新于 May 14 08:19)

### Eval Return 轨迹

| Step | eval_return |
|------|-------------|
| 5K | 31.0 |
| 15K | 256.9 |
| 25K | 321.4 |
| 35K | **485.3** (peak) |
| 45K | 477.0 |
| 55K | 360.4 ↓ |

**趋势**: 35K-45K 处达到峰值 ~480，55K 回落至 360。当前表现不稳定，出现了性能下滑。相对 baseline (last10 mean = 950.9)，当前峰值仅为 baseline 的 **51%**。

gate 指标确认 dt 固定为 2（gate_dt_2_frac = 1.0, std = 0.0），符合实验设计。

---
