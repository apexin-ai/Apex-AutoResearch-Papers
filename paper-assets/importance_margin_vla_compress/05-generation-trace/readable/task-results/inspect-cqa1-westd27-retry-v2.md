# inspect cqa1 westd27 retry v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_cqa1_westd27_retry_v2_20260526T023944_result.json`
- **Structured JSON:** [`953fd6c9e053682f5f17.json`](../../sessions/95/953fd6c9e053682f5f17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 服务器 | 连接状态 | GPU 状态 | 进程 | tmux |
|--------|---------|---------|------|------|
| cqa1-33015 | ✓ 连接成功 | 4×GPU，全部空闲（0% util, 0 MiB） | 无 eval 进程 | 无 |
| westd-27271 | ✓ 连接成功 | 2×GPU，100% util 但 0 MiB 显存 | 无 eval 进程 | 无 |

westd-27271 的 GPU 显示 100% utilization 但 0 MiB 显存占用，可能是驱动状态异常或有非 CUDA 负载。两台服务器都没有运行 eval 任务。

---
