# deploy westd41074 object cliff

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_object_cliff_20260526T195937_result.json`
- **Structured JSON:** [`dfba2018d142112c469d.json`](../../sessions/df/dfba2018d142112c469d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 和 cuda:1 不可用。** 4 个 GPU 全部在跑实验：

| GPU | 进程 | 实验 | 运行时间 |
|-----|------|------|----------|
| cuda:0 | PID 846246 | random_prune k=0.7 object | 54min |
| cuda:0 | PID 856148 | random_prune k=0.75 object | 39min |
| cuda:1 | PID 846317 | l2norm_prune k=0.9 object | 54min |
| cuda:1 | PID 856656 | random_prune k=0.75 libero_10 | 39min |
| cuda:2 | PID 755986 | (existing) | — |
| cuda:3 | PID 824210 | (existing) | — |

cuda:0 和 cuda:1 各有 2 个 eval 进程，占用约 32GB 显存。需要等当前实验完成后才能部署新实验，或者你可以指定其他服务器。如何处理？

---
