# ops check training progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260516T014415_result.json`
- **Structured JSON:** [`ceff3b394f7feb02ab4d.json`](../../sessions/ce/ceff3b394f7feb02ab4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练进度：**

| 实验 | 当前 step | 目标 | 进度 | 最新 eval_return |
|------|----------|------|------|-----------------|
| 009d (walker baseline) | 312K | 500K | 62.4% | 925.86 (@ 308K) |
| 010a (cheetah baseline) | 120K | 512K | 23.4% | 546.73 (@ 115K) |

**009d** eval_return 趋势良好，从 35→926 稳步上升，最近几个 eval 点 (288K: 846, 298K: 913, 308K: 926) 持续增长。

**010a** 起步较晚，eval_return 到 115K 步时达到 547，也在稳步上升。

**GPU：**
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 4165 MiB | 22% |
| 1 | 4690 MiB | 23% |

两块 GPU 各跑一个实验，显存和利用率都正常。

---
