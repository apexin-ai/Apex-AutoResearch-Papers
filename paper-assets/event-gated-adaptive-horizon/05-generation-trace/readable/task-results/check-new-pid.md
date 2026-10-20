# check new pid

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_new-pid_20260513T072323_result.json`
- **Structured JSON:** [`1ab6be796156d004d672.json`](../../sessions/1a/1ab6be796156d004d672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

- **PID**: 27009（`python dreamer.py`，CPU 948%，运行约 3h）
- **tmux session**: `exp_003_event_gated_v2`
- **当前 step**: 60000（最新 metrics 行）
- **gate_scale**: 0.06
- **gate_dt_mean**: 4.51（dt 分布近均匀，entropy ratio 0.9995）
- **gate_empirical_entropy**: 2.078
- **train_return**: 最近 4 个 episode 为 331.5 / 337.2 / 253.9 / 355.6（均值 ~319.5）
- **eval_return**: metrics.jsonl 中最近无 eval_return 字段，当前只有 train_return

训练正常运行中，目标 500k steps，当前 60k（12%）。

---
