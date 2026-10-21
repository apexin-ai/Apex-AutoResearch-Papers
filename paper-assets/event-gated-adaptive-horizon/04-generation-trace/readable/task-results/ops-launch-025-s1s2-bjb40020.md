# ops launch 025 s1s2 bjb40020

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-025-s1s2-bjb40020_20260519T170631_result.json`
- **Structured JSON:** [`2a507a2c4b9b24774e64.json`](../../sessions/2a/2a507a2c4b9b24774e64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动。

**汇总：**

| 实验 | tmux session | Python PID | GPU | 状态 |
|------|-------------|-----------|-----|------|
| exp_025_obs_sgs_walker_s1 | `exp_025_s1` | 7833 | GPU 0 (RTX 4090, 1618 MiB) | 已跑到 [5000]，正在 evaluation |
| exp_025_obs_sgs_walker_s2 | `exp_025_s2` | 7989 | GPU 1 (RTX 4090, 568 MiB) | 已跑到 [5000]，正在 evaluation |

两张 4090 各分配一个实验，温度正常 (31-32°C)，功耗低 (~69W)。

---
