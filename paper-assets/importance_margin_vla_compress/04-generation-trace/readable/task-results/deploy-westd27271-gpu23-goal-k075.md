# deploy westd27271 gpu23 goal k075

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271-gpu23-goal-k075_20260526T192739_result.json`
- **Structured JSON:** [`dd390226a4c50da434f4.json`](../../sessions/dd/dd390226a4c50da434f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：westd-27271 只有 2 块 GPU（GPU 0 和 GPU 1），不存在 GPU 2 和 GPU 3。**

当前状态：
- GPU 0: NVIDIA RTX PRO 6000 Blackwell, 15964 MiB / 97887 MiB, 利用率 70%
- GPU 1: NVIDIA RTX PRO 6000 Blackwell, 15880 MiB / 97887 MiB, 利用率 72%

两块 GPU 都在使用中（各约 16GB 显存占用）。模型路径 `/root/autodl-tmp/openvla-7b-finetuned-libero-goal/` 已确认存在。

无法按原计划部署到 GPU 2/3。需要等 GPU 0/1 上的任务完成，或者指定其他服务器。

---
