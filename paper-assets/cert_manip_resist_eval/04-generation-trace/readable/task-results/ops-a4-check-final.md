# ops a4 check final

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_a4-check-final_20260524T131602_result.json`
- **Structured JSON:** [`ce3d1d0968bc42762dc0.json`](../../sessions/ce/ce3d1d0968bc42762dc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID 22154 已完成。** 生产运行（n_sim=1000, n_boot=999）K=3 和 K=5 均已跑完，总耗时 4342 秒（~72 分钟）。

### 结果摘要

**Power by beta_std:**

| beta_std | K=3 | K=5 |
|----------|------|------|
| 0.1 | 0.015 | 0.001 |
| 0.15 | 0.025 | 0.003 |
| 0.2 | 0.046 | 0.006 |
| 0.25 | 0.081 | 0.012 |
| 0.3 | 0.126 | 0.022 |
| 0.5 | 0.421 | 0.085 |
| 0.7 | 0.690 | 0.175 |
| 1.0 | 0.858 | 0.301 |

**MDE@80% power:**
- **K=3**: 0.897 (需要很大的效应才能达到 80% power)
- **K=5**: **不可达** (最大 power 仅 0.301)

K=5 的 power 远低于 K=3，因为每个 position 只有 5 个 cluster，WCB 在如此少的 cluster 下极度保守。

---
