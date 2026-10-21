# check 8b multiseed progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_8b_multiseed_progress_20260518T005723_result.json`
- **Structured JSON:** [`ce65c995e6f05dad6f82.json`](../../sessions/ce/ce65c995e6f05dad6f82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在跑，状态健康。

| 指标 | s123 (cuda:0, PID 34700) | s456 (cuda:1, PID 35045) |
|------|--------------------------|--------------------------|
| 进度 | **790/1000** (79%) | **780/1000** (78%) |
| 最新 loss | 0.1592 | 0.1543 |
| sparsity | 0.293 | 0.293 |
| constraint | 0.000 (达标) | 0.000 (达标) |
| GPU 利用率 | 100%, 67.6GB | 100%, 67.6GB |

两个 run 的 sparsity 稳定在 0.281-0.305 范围（目标 30%），constraint=0 说明 sparsity 约束已满足。Loss 在 0.13-0.20 区间波动，收敛正常。

按 ~0.5s/step 估算，剩余 ~200 steps，约 **1.5-2 分钟**完成。PID 与启动时不同（33894→34700, 33988→35045），应该是 nohup wrapper 导致的。

---
