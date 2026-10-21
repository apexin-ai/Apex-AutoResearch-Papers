# deploy openvla random k09 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-random-k09-seed42_20260521T220946_result.json`
- **Structured JSON:** [`7a8d22f9917ee47d5259.json`](../../sessions/7a/7a8d22f9917ee47d5259.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**状态汇总：**
- **实验**: `eval_openvla_random_k09_object_seed42` → RUNNING
- **服务器**: westd-27271 GPU0 (15.9GB / 73% util)
- **PID**: 360411
- **配置**: OpenVLA random_prune k=0.9, libero_object, 500 episodes, seed 42
- **进度**: 模型已加载(15.1GB)，Task 1/10 评估中，256→230 vision tokens
- **GPU1**: M32 VTC 训练不受影响 (42GB occupied)
- **预计耗时**: ~4h（参考 L2norm k=0.9 用了 228 min）

---
