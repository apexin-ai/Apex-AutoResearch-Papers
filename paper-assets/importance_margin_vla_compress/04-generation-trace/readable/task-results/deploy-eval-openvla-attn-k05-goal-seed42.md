# deploy eval openvla attn k05 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_attn_k05_goal_seed42_20260526T152428_result.json`
- **Structured JSON:** [`2d931d320ec81e519638.json`](../../sessions/2d/2d931d320ec81e519638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 正在运行 `random_prune k=0.85 libero_10 seed42`（已运行 1h54m）。四张卡全满：

| GPU | PID | 显存 | 进程 |
|-----|-----|------|------|
| 0 | 623613 | 16169 MiB | (占用) |
| 1 | 668245 | 16169 MiB | random_prune k=0.85 libero_10 |
| 2 | 601124 | 15946 MiB | (占用) |
| 3 | 514356 | 16339 MiB | (占用) |

cuda:1 不空闲，无法直接部署。需要等当前任务完成或选其他 GPU/服务器。如何处理？

---
