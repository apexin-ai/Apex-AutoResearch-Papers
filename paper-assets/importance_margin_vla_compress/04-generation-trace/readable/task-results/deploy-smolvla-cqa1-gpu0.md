# deploy smolvla cqa1 gpu0

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-cqa1-gpu0_20260521T155507_result.json`
- **Structured JSON:** [`15515da1f840b9345405.json`](../../sessions/15/15515da1f840b9345405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

k=0.9 已 RUNNING。k=0.7 保持 ALLOCATED（等 k=0.9 完成后自动启动）。

## GPU0 部署完成

**tmux session**: `sweep_gpu0`
**服务器**: cqa1-33015, GPU0
**串行队列**:
1. `eval_smolvla_official_l2norm_k090_object_seed42` — **RUNNING**，已在加载 Task 0
2. `eval_smolvla_official_l2norm_k070_object_seed42` — **ALLOCATED**，排在 k=0.9 后

**GPU 状态**: GPU0 显存 2182 MiB, 利用率 24%（正在启动中）

**GPU1 队列**: sweep_gpu1 仍在等 baseline 完成，L2norm k=0.9/0.7 还在其队列中。由于 k=0.95 sanity check 大概率 0% SR，这些 config 会很快结束，重复跑的代价不大，不修改 GPU1 队列。

---
