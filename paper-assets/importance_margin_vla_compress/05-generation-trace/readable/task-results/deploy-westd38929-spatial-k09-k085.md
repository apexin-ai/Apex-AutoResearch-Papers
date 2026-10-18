# deploy westd38929 spatial k09 k085

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929-spatial-k09-k085_20260521T235736_result.json`
- **Structured JSON:** [`3a6cd3a94cf8b907e5bb.json`](../../sessions/3a/3a6cd3a94cf8b907e5bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 和 GPU3 目前显存仅 3 MiB — 进程刚启动，模型还在加载中。这是正常的，π0.5 模型加载需要一些时间。

**部署结果：**

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval_pi05_l2norm_k09_spatial_seed42` (L2norm k=0.9 Spatial) | GPU0 | 48423 | 已启动，模型加载中 |
| `eval_pi05_random_k085_spatial_seed42` (random k=0.85 Spatial) | GPU3 | 48588 | 已启动，模型加载中 |

GPU1、GPU2 上的已有实验未受影响。

---
