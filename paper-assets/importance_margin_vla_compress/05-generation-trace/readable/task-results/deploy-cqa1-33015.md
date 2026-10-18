# deploy cqa1 33015

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-33015_20260523T154626_result.json`
- **Structured JSON:** [`4467f817215f33b86ba0.json`](../../sessions/44/4467f817215f33b86ba0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**当前状态与预期不符：**

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 10381/24564 MiB | 51% | **占用** |
| 1 | 1/24564 MiB | 0% | 空闲 |
| 2 | 10591/24564 MiB | 11% | **占用** |
| 3 | 9727/24564 MiB | 0% | **占用** |

- X-VLA 模型不存在，走 π0.5 方案
- `eval_pi05_pruning_libero.py` 脚本存在
- **只有 GPU 1 空闲**，GPU 0/2/3 各有进程占用 ~10GB

3 张卡被占，无法部署 4 个实验。需要你确认：
1. 是否先了解现有进程是什么任务？
2. 是否只在 GPU 1 上部署 1 个实验（k=0.95）？
3. 还是等现有任务结束后再部署？

---
