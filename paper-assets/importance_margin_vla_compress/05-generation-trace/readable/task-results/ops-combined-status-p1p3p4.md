# ops combined status p1p3p4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_combined-status-p1p3p4_20260520T075057_result.json`
- **Structured JSON:** [`9d7ceb46c63c638507cd.json`](../../sessions/9d/9d7ceb46c63c638507cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## P1 — C4-ext 20K eval (westd-27271:0)
**状态: ALIVE，刚启动**
- Suite: libero_object, 50 eps/task, 10 tasks
- 当前: Task 0, Ep 1/50（15:38 开始）
- 预计完成：每 task ~8min × 10 = ~80min → 约 16:58

## P3 — X-VLA LIBERO eval (westd-41074:1)
**状态: 未运行。** 服务器上无任何 xvla 日志或进程。

westd-41074 当前在跑 **训练**（非 eval）：
- `m96_seed42`: step 7,300/100,000 (7.3%), loss=2.78, 0.5 sps
- `m64_seed42`: step 9,050/100,000 (9.1%), loss=3.26, 0.6 sps

## P4 — cqa1 evals (cqa1-33015)
全部 libero_object, 500 eps/task, 10 tasks

### m128_seed43 — ALIVE, Task 9 接近完成 (ep 454/500)
| Task | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| SR% | 64.6 | 32.2 | 61.4 | 43.2 | 34.8 | 44.2 | 71.6 | 60.4 | 81.8 | ~running |

Tasks 0-8 均值: **54.9%** → 预计几分钟内完成

### m16_seed43 — ALIVE, Task 9 接近完成 (ep 475/500)
| Task | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| SR% | 42.8 | 47.4 | 66.2 | 48.4 | 74.2 | 40.0 | 79.2 | 69.8 | 76.6 | ~running |

Tasks 0-8 均值: **60.5%** → 预计几分钟内完成

### m16_seed44 — ALIVE, Task 8 进行中 (ep 219/500)
| Task | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| SR% | 38.0 | 70.0 | 55.2 | 42.0 | 64.8 | 32.8 | 73.2 | 63.8 | running | — |

Tasks 0-7 均值: **55.0%** → 还需 ~90min（Task 8 剩余 + 整个 Task 9）

---

## GPU 占用一览

| 服务器 | GPU | 显存占用 | 状态 |
|--------|-----|----------|------|
| **westd-27271** | 0 | 36/98 GB | P1 eval |
| | 1 | 26/98 GB | 占用（非本项目?） |
| **westd-41074** | 0 | 30/98 GB | m96 训练 |
| | **1** | **0/98 GB** | **空闲** |
| | 2 | 29/98 GB | m64 训练 |
| | 3 | 28/98 GB | 占用 |
| **cqa1-33015** | 0 | 3/25 GB | m128_seed43 eval |
| | 1 | 3.5/25 GB | m16_seed43 eval |
| | 2 | 3.5/25 GB | m16_seed44 eval |
| | **3** | **0/25 GB** | **空闲** |

**空闲 GPU**: westd-41074:1 (98GB), cqa1-33015:3 (25GB)

**关键发现**: P3 X-VLA eval 未启动——westd-41074:1 完全空闲可用。

---
