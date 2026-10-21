# ops check westd41074 gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd41074-gpu_20260520T141111_result.json`
- **Structured JSON:** [`785f60b77c6174095b38.json`](../../sessions/78/785f60b77c6174095b38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 个 GPU 正常，无崩溃。** 详情如下：

| GPU | 进程 | PID | 显存 | GPU-Util | 运行时间 | 状态 |
|-----|------|-----|------|----------|----------|------|
| 0 | eval random_prune k0.7 seed43 v2 | 468330 (子进程, 父468324) | 15961 MiB | 64% | 35m | **存活** |
| 1 | eval random_prune k0.5 seed43 v2 | 468864 (子进程, 父468858) | 15961 MiB | 73% | 35m | **存活** |
| 2 | **M96 训练** | 68539 | 28546 MiB | **99%** | **10h31m** | **存活, Rl (running)** |
| 3 | **M64 训练** | 68852 | 27526 MiB | 0% | 10h30m | **存活, Rl (running)** |

**GPU 2 (M96) 没有崩溃** — PID 68539 状态 `Rl`（running），GPU 利用率 99%，显存 28.5 GiB，运行 10.5 小时。

GPU 3 (M64) 的 GPU-Util 为 0% 但进程存活，可能正在做 checkpoint 保存或 data loading。

---
