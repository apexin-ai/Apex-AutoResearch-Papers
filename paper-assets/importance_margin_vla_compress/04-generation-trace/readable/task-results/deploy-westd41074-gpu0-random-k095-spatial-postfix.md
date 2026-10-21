# deploy westd41074 gpu0 random k095 spatial postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd41074-gpu0-random-k095-spatial-postfix_20260523T230155_result.json`
- **Structured JSON:** [`28d682497fad55a95173.json`](../../sessions/28/28d682497fad55a95173.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

- **GPU 0**: 9709 MiB 已占用，模型加载成功
- 日志确认：`suite=libero_spatial, prune=random, keep=0.95, eps=50, gpu=0`
- 已通过模型加载和 gradient checkpointing 阶段
- Registry: `eval_pi05_random_k095_spatial_seed42_postfix` 状态 RUNNING，parent 指向 pre-fix 版本
- GPU 1/3 上的 attention 实验未受影响（GPU 2 看起来已跑完释放了）

---
