# ops westd41074 gpu01 check deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-gpu01-check-deploy_20260522T021534_result.json`
- **Structured JSON:** [`ecabc4566529917c03a7.json`](../../sessions/ec/ecabc4566529917c03a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常加载模型，显存刚开始分配（3 MiB，模型还在 CPU 加载中）。

## 汇报

**GPU 状态：**
- GPU 0: 空闲（之前的实验已结束/失败）
- GPU 1: 空闲（之前的实验已结束/失败）
- GPU 2: VTC M96 train 正常运行中（28.5GB 显存）
- GPU 3: VTC M64v6 train 正常运行中（27.5GB 显存）

**已部署：**
| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| 0 | `eval_pi05_random_k095_spatial_seed42_v2` (random k=0.95 Spatial) | 922845 | 模型加载中 |
| 1 | `eval_pi05_random_k085_object_seed43_v3` (random k=0.85 Object s43) | 922925 | 模型加载中 |

4 块 GPU 现在全部在工作。

---
