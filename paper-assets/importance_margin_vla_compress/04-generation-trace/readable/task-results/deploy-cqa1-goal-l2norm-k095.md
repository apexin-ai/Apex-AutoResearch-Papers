# deploy cqa1 goal l2norm k095

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_goal_l2norm_k095_20260522T182451_result.json`
- **Structured JSON:** [`e8575028dc90dd6b56cc.json`](../../sessions/e8/e8575028dc90dd6b56cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 任务 A：cuda:2 部署 — **无法执行**

cuda:2 当前被占用，正在运行 **π0.5 random k=0.5 Goal** (PID 599978)。
- 进度：Task 8/10，ep 40/50，累计 SR=77.0% (308/400)
- 预计剩余：~20-30 分钟完成

**等 cuda:2 空闲后再部署 L2norm k=0.95 Goal。**

### 任务 B：cuda:3 身份确认

cuda:3 正在运行 **π0.5 L2norm k=0.95 Long (libero_10)** (PID 646912)。
- 进度：3/10 tasks 完成，正在跑 Task 3 ep 20/50
- 累计 SR=98.7% (148/150)，非常高
- 各 task：T0=98%, T1=98%, T2=100%
- 预计剩余：~2-2.5 小时

### 四卡 GPU 状态表

| GPU | VRAM | Util | 实验 | 进度 | 累计 SR |
|-----|------|------|------|------|---------|
| cuda:0 | 15437/24564 MiB | 72% | OpenVLA baseline spatial s42 | Task 5/10, ep 31/50 | 0.0% (0/250) |
| cuda:1 | 9788/24564 MiB | 0% | π0.5 random k=0.7 Goal s42 | Task 9/10, ep 20/50 | 82.9% (373/450) |
| cuda:2 | 10196/24564 MiB | 29% | π0.5 random k=0.5 Goal s42 | Task 8/10, ep 40/50 | 77.0% (308/400) |
| cuda:3 | 10224/24564 MiB | 56% | π0.5 L2norm k=0.95 Long s42 | Task 3/10, ep 20/50 | 98.7% (148/150) |

OpenVLA baseline spatial 在 cuda:0 上跑了 5 个 task 全部 0% SR，值得注意。

---
