# audit westd38929 gpu 20260526c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929-gpu-20260526c_20260526T200721_result.json`
- **Structured JSON:** [`dd981fe441780bc23e21.json`](../../sessions/dd/dd981fe441780bc23e21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 GPU 状态审计

### 当前运行中 (4/4 GPU 占满)

| GPU | PID | 实验 | 显存 | 进度 | 预计剩余 |
|-----|-----|------|------|------|----------|
| 0 | 623613 | OV L2norm k=0.5 Long | 15923MiB | Task 6/10 进行中 | ~4-5h |
| 1 | 668245 | OV Random k=0.85 Long v3 | 16339MiB | Task 5/10 进行中 | ~5-6h |
| 2 | 732931 | OV L2norm k=0.75 Long | 15762MiB | Task 3/10 进行中 (01:30启动) | ~7-8h |
| 3 | 514356 | OV Attn k=0.85 Long v3 | 15919MiB | **Task 10/10 进行中** | **~45min** |

### GPU 3 即将完成 — 当前中间结果

| Task | SR |
|------|----|
| 1 | 60.0% |
| 2 | 58.0% |
| 3 | 56.0% |
| 4 | 34.0% |
| 5 | 38.0% |
| 6 | 66.0% |
| 7 | 34.0% |
| 8 | 66.0% |
| 9 | 24.0% |
| 10 | 进行中 (Ep 40/50, 7/40) |

9 task 平均 ≈ 48.4%，最终预计 Overall SR ≈ **45-48%**。

### 已完成实验结果（已收割）

| 实验 | Overall SR | 耗时 | 结果文件 |
|------|-----------|------|----------|
| **OV Attn k=0.7 Goal** | **66.4%** (332/500) | 251.7 min | openvla_attention_prune_k07_goal_seed42.json |
| **OV Random k=0.5 Long v2** | **18.6%** (93/500) | 607.5 min | openvla_random_prune_k05_10_seed42.json |

### GPU 0 中间结果 (L2norm k=0.5 Long)
Tasks 1-5 完成：20%, 14%, 18%, 12%, 16% → 当前均值 **16.0%**，表现很差。

### GPU 1 中间结果 (Random k=0.85 Long)
Tasks 1-4 完成：60%, 64%, 60%, 32% → 当前均值 **54.0%**。

### X-VLA 实验
eval_xvla_random_k05_spatial_seed43 (PID 155546) 在 westd-38929 上**不存在**——无对应 log 文件或进程，可能在 westd-27271。

---
