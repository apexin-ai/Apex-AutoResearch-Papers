# ops 30476 status check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_30476_status_check_20260519T015226_result.json`
- **Structured JSON:** [`4ea8901b89a4e6f73049.json`](../../sessions/4e/4ea8901b89a4e6f73049.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-30476 状态报告

### GPU 状态 (4x RTX PRO 6000 Blackwell, 98GB each)

| GPU | 温度 | 功耗 | 显存占用 | 利用率 | 进程 |
|-----|------|------|---------|--------|------|
| 0 | 28°C | 33W/600W | 0MiB/97887MiB | 0% | 空闲 |
| 1 | 28°C | 35W/600W | 0MiB/97887MiB | 0% | 空闲 |
| 2 | 62°C | 378W/600W | 41757MiB/97887MiB | 99% | PID 93817 (python) |
| 3 | 59°C | 361W/600W | 41757MiB/97887MiB | 99% | PID 89876 (python) |

### 实验存活状态

| 实验 | PID | GPU | 状态 | 进度 | ETA |
|------|-----|-----|------|------|-----|
| **q07 epoch-matched seed42** | 93812 (wrapper) / 93817 (python) | GPU 2 | 运行中 | **1125/3047 (37%)** | ~67min |
| **q03 seed456** | — | — | **未运行** | — | — |
| **q09 epoch-matched seed42** | 89871 (wrapper) / 89876 (python) | GPU 3 | 运行中 | **2389/3770 (63%)** | ~48min |

### 训练指标（最新）

- **q07**: loss=1.83, epoch=0.1, 速度 2.10s/it
- **q09**: loss=2.57, epoch=0.17, 速度 2.09s/it
- 两个实验均为 uniform weighting (weighted_loss == unweighted_loss)

### Tmux Sessions
- `detect_remove_q07_epoch_matched_seed42` (创建于 09:13)
- `detect_remove_q09_epoch_matched_seed42` (创建于 08:28)

### 磁盘
`/root/autodl-tmp`: 135G/250G used (54%), 116G 可用

---
