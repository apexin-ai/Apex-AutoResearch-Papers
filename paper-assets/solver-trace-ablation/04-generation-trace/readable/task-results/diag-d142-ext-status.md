# diag d142 ext status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_d142-ext-status_20260519T120936_result.json`
- **Structured JSON:** [`38d0e8fd81f23cc8b462.json`](../../sessions/38/38d0e8fd81f23cc8b462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部更新完成。汇总报告：

## D142 Gated ISR 实验诊断结果

### 环境状态
- **GPU**: 空闲（0MiB / 97887MiB），无运行进程
- **磁盘**: 45G / 250G（18%），充裕

### 实验结果

| | s55 | s56 | s57 |
|---|---|---|---|
| **状态** | SUCCESS | SUCCESS | SUCCESS |
| **Proved** | 100/100 (100%) | 36/100 (36%) | 88/100 (88%) |
| **Mean ISR** | 0.525 | 0.293 | 0.450 |
| **Proved-only ISR** | 0.525 | 0.813 | 0.511 |
| **H7 (TS)** | **82/100 (82%)** | 0 | 1/88 (1.1%) |
| **H1 (CE)** | 0 | 0 | 18/88 (20.5%) |
| **H8 (PG)** | 15/100 (15%) | **30/36 (83.3%)** | 13/88 (14.8%) |
| **Genuine** | **3/100 (3%)** | **6/36 (16.7%)** | **56/88 (63.6%)** |
| **ContentIndep** | 0 | **27/36 (75%)** | 0 |
| **Checkpoint** | `/root/autodl-tmp/d142_gated_isr_s55` | `...s56` | `...s57` |

### 模式分析

三个 seed 展示了三种完全不同的 collapse 模式：
- **s55**: 极端 TS collapse（82% H7），gate 完全未能阻止 tautology shortcut
- **s56**: PG collapse + content-independent（83% H8, 75% CntIndep），prove rate 暴跌到 36%
- **s57**: 最健康的结果，63.6% genuine，但仍有 CE 和 PG 各约 15-20%

Registry 已全部更新为 DONE/success。

---
