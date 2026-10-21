# analysis eval pi05 seed47 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_seed47_cqa1_20260529T075715_result.json`
- **Structured JSON:** [`3646e54145e70e06e33c.json`](../../sessions/36/3646e54145e70e06e33c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，无异常（EXIT_CODE=0），10 个 task × 50 episodes = 500 episodes 全部跑完。

| 实验 | Success Rate |
|------|-------------|
| eval_pi05_random_k09_long_seed47_cqa1 | **30.8%** (154/500) |
| eval_pi05_random_k085_long_seed47_cqa1 | **43.4%** (217/500) |

k=0.85 反而比 k=0.9 高 12.6pp，这不符合直觉（保留更少 token 反而更好）。可能是 random pruning 的随机性导致，或 seed 恰好对 k=0.85 有利。无错误或异常。

---
