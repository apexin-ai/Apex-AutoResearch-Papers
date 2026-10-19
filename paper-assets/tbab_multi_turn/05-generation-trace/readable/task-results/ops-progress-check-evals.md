# ops progress check evals

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-evals_20260518T175825_result.json`
- **Structured JSON:** [`3e65031c9fbce9e247ba.json`](../../sessions/3e/3e65031c9fbce9e247ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 项目 | 状态 |
|------|------|
| **C4_s42 eval** | **64/91** 进行中（正在评 livecodebench/2857） |
| **C1_s137 eval** | **62/91** 进行中（正在评 livecodebench/2855） |
| **C4_s137 训练** | **已完成** — 最终 loss=0.3114, train_loss=0.5447, epoch=3, EXIT_CODE=0 |
| **C4_s137 checkpoint** | `/root/tbab_multi_turn/checkpoints/c4_full_tbab_seed137` (May 19 01:55) |
| **GPU 显存** | 两个进程分别占 17160 MiB + 17254 MiB（即两个 eval 并行运行中） |

注意：C4_s137 训练日志有一条 `WARNING: Embedding gradients are None (check after optimizer.step)`，推理/eval 不受影响，但如果后续还要继续训练可以排查下。

---
