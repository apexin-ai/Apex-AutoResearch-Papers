# deploy westd38929 pi05 long batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_pi05_long_batch_20260522T152700_result.json`
- **Structured JSON:** [`7e3d719a709780f71057.json`](../../sessions/7e/7e3d719a709780f71057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 张 GPU 都在跑 SmolVLA eval_official 实验，无法直接部署 π0.5：

| GPU | 当前进程 | 队列中后续任务 |
|-----|---------|--------------|
| cuda:0 | SmolVLA random_prune k0.95 object | (队列已完成前序) |
| cuda:1 | SmolVLA l2_norm k0.95 spatial | 后续: random_prune k0.95 spatial |
| cuda:2 | SmolVLA baseline long (libero_10) | 后续: l2_norm k0.95 long, random_prune k0.95 long |
| cuda:3 | SmolVLA l2_norm k0.95 goal | 后续: random_prune k0.95 goal |

每个 tmux session 里都是链式命令，当前任务跑完会自动启动下一个。GPU 内存只用了 ~2.7GB（SmolVLA 比 π0.5 小很多），但进程都在活跃运行（CPU 166-189%）。

**选项：**
1. **等 SmolVLA 跑完再部署** — cuda:0 队列最短（只剩当前任务），其他卡还有 1-2 个排队
2. **kill SmolVLA 实验，立即部署 π0.5** — 会丢失未完成的 SmolVLA 结果
3. **只在跑完的卡上逐步部署** — 先等 cuda:0 跑完，部署第一个 π0.5 实验

怎么处理？

---
