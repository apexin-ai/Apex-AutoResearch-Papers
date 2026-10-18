# ops deploy l2norm k09 long westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-l2norm-k09-long-westd38929_20260524T122739_result.json`
- **Structured JSON:** [`b8377120a2b788bfd1e2.json`](../../sessions/b8/b8377120a2b788bfd1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 正在使用（10772 MiB, 47% utilization）。GPU 1-3 也都有占用。没有空闲 GPU。

当前状态：
- GPU 0: 10772 MiB used, 47% util
- GPU 1: 10406 MiB used, 39% util
- GPU 2: 10616 MiB used, 34% util
- GPU 3: 9961 MiB used, 0% util (显存占用但利用率 0%，可能刚启动或即将结束)

GPU 0 不空闲，无法直接部署。需要确认 GPU 0 上跑的是什么任务。要我查一下各 GPU 上的进程来判断是否可以等待或终止？

---
