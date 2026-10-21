# ops launch 026 cheetah bjb40020

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-026-cheetah-bjb40020_20260519T201959_result.json`
- **Structured JSON:** [`fb41afb398b84f3408ef.json`](../../sessions/fb/fb41afb398b84f3408ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并正常训练：

| 实验 | tmux session | GPU | 显存占用 | PID | 状态 |
|------|-------------|-----|---------|-----|------|
| exp_026_obs_sgs_cheetah_s0 | exp_026_s0 | cuda:0 | 5178/24564 MiB | 16208 | 已到 [5000]，正在 evaluation |
| exp_026_obs_sgs_cheetah_s1 | exp_026_s1 | cuda:1 | 3096/24564 MiB | 16346 | 已到 [5000]，正在 evaluation |

两个实验与现有 exp_025 共存运行，GPU 0/1 各承载一个实验。

---
