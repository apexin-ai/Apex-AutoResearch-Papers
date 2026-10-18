# ops xvla batch2 final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-batch2-final_20260520T114931_result.json`
- **Structured JSON:** [`b902be940a88d5d8fbba.json`](../../sessions/b9/b902be940a88d5d8fbba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k=0.2 和 k=0.1 都在最后一个 task (9/10)，预计 ~10 分钟内完成。

## X-VLA L2-Norm Prune Sweep — LIBERO-Object (500 episodes each)

| k | Tokens | SR | per_task (T0–T9) | Status |
|---|--------|-----|-------------------|--------|
| **1.0** | 50→50 | **99.2%** | [98, 100, 98, 100, 100, 96, 100, 100, 100, 100] | Done |
| **0.95** | 50→47 | **99.0%** | [98, 100, 100, 96, 100, 96, 100, 100, 100, 100] | Done |
| **0.9** | 50→45 | **97.6%** | [96, 98, 100, 92, 100, 96, 100, 98, 96, 100] | Done |
| **0.7** | 50→35 | **56.2%** | [94, 2, 100, 80, 28, 92, 12, 66, 0, 88] | Done |
| **0.5** | 50→25 | **42.6%** | [58, 2, 74, 78, 42, 50, 2, 38, 14, 68] | Done |
| **0.3** | 50→15 | **23.0%** | [30, 0, 32, 48, 18, 44, 0, 22, 0, 36] | Done |
| **0.2** | 50→10 | **~4.0%** | [6, 0, 4, 12, 12, 0, 0, 6, 0, ?] | Task 9 running |
| **0.1** | 50→5 | **~0.0%** | [0, 0, 0, 0, 0, 0, 0, 0, 0, ?] | Task 9 running |

关键发现：
- **k=0.9 (保留 90% tokens) 是临界点**：97.6% vs baseline 99.2%，仅差 1.6pp
- **k=0.7 断崖式下降**：56.2%，某些 task 崩溃（T1: 2%, T6: 12%, T8: 0%）
- X-VLA 对 vision token 裁剪非常敏感，k=0.9→0.7 之间存在急剧退化

---
