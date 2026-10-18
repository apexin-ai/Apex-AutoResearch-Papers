# ops westd d108 status check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-d108-status-check_20260520T131144_result.json`
- **Structured JSON:** [`1b44773b39416bed0be9.json`](../../sessions/1b/1b44773b39416bed0be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

## 1. westd-38929: D108 L2 norm pruning

| 实验 | 状态 | 进度 | GPU |
|------|------|------|-----|
| **k=0.5** (PID 787425) | **运行中** | Task 1/10, Ep 30/50 | GPU 0 (16GB/98GB) |
| **k=0.3** (PID 788043) | **运行中** | Task 1/10, Ep 20/50 | GPU 1 (16GB/98GB) |

两个都还在第一个 task 的前半段。k=0.3 保留 76/256 tokens，k=0.5 保留 128/256 tokens。

**空闲 GPU**: GPU 2, GPU 3 完全空闲。

## 2. westd-27271

| 实验 | 状态 | 进度 | GPU |
|------|------|------|-----|
| **D108 L2 norm k=0.7** | **运行中** | Task 3/10, Ep 20/50 | GPU 0 (16GB/98GB) |
| **OpenVLA seed43 random k=0.9** | **运行中** | Task 5/10, Ep 20/50 | GPU 1 (部分) |
| **M=32 training** (resume) | **运行中** | step 14400/100000 (14.4%) | GPU 1 (共 58GB/98GB) |

D108 k=0.7 已完成 2 个 task：Task1 SR=42.0%, Task2 SR=28.0%。

Seed43 k=0.9 已完成 4 个 task：Task1=74.0%, Task2=26.0%, Task3=76.0%, Task4=56.0%，正在跑 Task5。

M=32 training loss ~2.5-3.1，lr=9.57e-5，速度 0.5 sps。

**空闲 GPU**: 无，两个 GPU 都在用。

## 3. 预估完成时间

- westd-38929 的两个 L2 norm 实验（10 tasks × 50 eps）刚开始，按 ~1.8 eps/min 估算每个实验约 4-5 小时。
- westd-27271 的 k=0.7 约 30% 完成，seed43 k=0.9 约 40-50% 完成，各还需 2-3 小时。
- M=32 training 14.4%，按 0.5 sps 完成全部 100k 步还需很久（~48 小时）。

---
