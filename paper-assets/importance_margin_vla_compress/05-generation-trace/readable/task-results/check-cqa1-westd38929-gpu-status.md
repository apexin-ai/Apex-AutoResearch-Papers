# check cqa1 westd38929 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_westd38929_gpu_status_20260524T193136_result.json`
- **Structured JSON:** [`e380a9c5796e5df0d514.json`](../../sessions/e3/e380a9c5796e5df0d514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### westd-38929 (4x H20 97GB)

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 15980/97887 MiB | 70% | OpenVLA Attn Prune k=0.9, object, seed42 (PID 692475) — Task 3/10, ep 30/50 |
| 1 | 15980/97887 MiB | 72% | OpenVLA Attn Prune k=0.85, object, seed42 (PID 693434) — Task 3/10, ep 30/50 |
| 2 | **1/97887 MiB** | **0%** | **空闲** |
| 3 | 10420/97887 MiB | 20% | Pi0.5 L2norm k=0.5, libero_10, seed43 (PID 612707) — Task 9/10 进行中 (Task 8 SR=22%, 累计 218/450=48.4%) |

**已完成的结果：**
- X-VLA Random k=0.5 Spatial seed43: **SR=72.6%** (363/500)
- X-VLA L2norm k=0.5 Goal seed43 (tmux): **SR=59.0%** (295/500)
- L2norm k=0.95 seed43 结果文件不存在（GPU2/3 之前的实验没留下结果文件）

---

### cqa1-33015 (4x 4090D 24GB)

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 10294/24564 MiB | 19% | Pi0.5 L2norm k=0.3, libero_10, seed43 v2 (PID 566658) — Task 7/10 进行中 (Task 6 SR=8%, 累计 143/350=40.9%) |
| 1 | 10065/24564 MiB | 48% | Pi0.5 Random k=0.5, libero_10, seed43 (PID 600325) — Task 2/10 进行中 (Task 1 ep30, T0 SR=72%) |
| 2 | 10421/24564 MiB | 28% | Pi0.5 Random k=0.95, libero_10, seed43 (PID 600400) — Task 2/10 进行中 (Task 1 ep40, T0 SR=50%) |
| 3 | 10533/24564 MiB | 24% | Pi0.5 Random k=0.7, libero_10, seed43 (PID 600244) — Task 2/10 进行中 (Task 1 done SR=74%, 累计 83/100=83%) |

**cqa1 Random seed43 进度汇总** (均在 02:43 启动，已运行约 48 min)：

| 实验 | 已完成 Tasks | 当前进度 | 预估剩余 |
|------|-------------|---------|---------|
| Random k=0.7 | 2/10 | Task 2 开始 | ~3.5h |
| Random k=0.5 | 1/10 (T1 ep30) | Task 1 进行中 | ~4h |
| Random k=0.95 | 1/10 (T1 ep40) | Task 1 进行中 | ~4h |

---
