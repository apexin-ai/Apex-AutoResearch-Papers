# ops audit cqa1 westd27271 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_cqa1_westd27271_v4_20260522T080201_result.json`
- **Structured JSON:** [`d8ae4d0b5115c679bce7.json`](../../sessions/d8/d8ae4d0b5115c679bce7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部进程存活并加载模型中。以下是完整审计报告：

---

## === cqa1-33015 (4× RTX 4090 24GB) ===

### 已完成实验（收割 metrics）

| 实验 | Overall SR | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|------|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| l2norm k=0.95 | **98.0%** | 100 | 100 | 100 | 100 | 94 | 88 | 100 | 98 | 100 | 100 |
| l2norm k=0.9 | **95.6%** | 98 | 100 | 96 | 96 | 84 | 92 | 100 | 100 | 100 | 90 |
| random k=0.925 | **57.8%** | 94 | 54 | 78 | 30 | 8 | 64 | 78 | 64 | 88 | 20 |
| random k=0.9 | **53.6%** | 92 | 40 | 78 | 24 | 16 | 52 | 58 | 52 | 88 | 36 |

### 新部署

| GPU | 实验 | PID | 二次确认 |
|-----|------|-----|---------|
| 0 | l2norm_k05_spatial_seed43 | 209334→子209336 | alive, loading model |
| 1 | random_k03_spatial_seed43 | 209588 | alive, 8.0GB RSS, loading |
| 2 | l2norm_k03_spatial_seed43 | 209658 | alive, 7.6GB RSS, loading |
| 3 | random_k05_spatial_seed43 | 209728 | alive, 7.8GB RSS, loading |

---

## === westd-27271 (2× 98GB) ===

### GPU 进程状态

| GPU | PID | 进程状态 | 显存 | 实验 |
|-----|-----|---------|------|------|
| 0 | 119111 | alive, 1h21m | 10554 MiB | random_k07_spatial_seed43 (Task 7/10, ~57%) |
| 0 | 119449 | alive, 1h21m | 10554 MiB | l2norm_k07_spatial_seed43 (Task 7/10, ~77%) |
| 1 | — | **空闲** | 3 MiB | — |

注意：两个进程都在物理 GPU 0 上（同一 GPU UUID），尽管 l2norm_k07 用了 `--gpu 1`。

### 已完成实验（收割 metrics）

| 实验 | Overall SR | T0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |
|------|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| random k=0.95 | **76.8%** | 100 | 94 | 100 | 60 | 36 | 76 | 90 | 74 | 100 | 38 |
| l2norm k=0.85 | **88.0%** | 100 | 92 | 100 | 78 | 62 | 84 | 96 | 90 | 96 | 82 |

### 空闲 GPU: [1]

优先级队列中的 4 个实验已全部部署到 cqa1-33015。westd GPU 1 当前无待部署实验。westd 上两个 k=0.7 实验预计还需 ~1h 完成（Task 7-9 剩余）。

---
