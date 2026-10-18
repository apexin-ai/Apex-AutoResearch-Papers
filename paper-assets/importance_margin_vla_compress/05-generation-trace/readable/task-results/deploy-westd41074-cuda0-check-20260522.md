# deploy westd41074 cuda0 check 20260522

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_cuda0_check_20260522_20260522T215050_result.json`
- **Structured JSON:** [`00e1186104dd0b34b93f.json`](../../sessions/00/00e1186104dd0b34b93f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 is now allocated (10616 MiB) and eval started — L2norm k=0.3 Long seed43 is running, pruning 76/256 tokens per image.

---

## westd-41074 巡查汇总

### GPU 状态
| GPU | VRAM | 实验 | 进度 |
|-----|------|------|------|
| cuda:0 | 10506 MiB | Random k=0.85 Long seed42 | T9 ep10/50, ~20min left |
| cuda:1 | 10616 MiB | **L2norm k=0.3 Long seed43** (新部署) | 刚启动 |
| cuda:2 | 10694 MiB | Random k=0.5 Long seed42 | T6 ep30/50, ~1hr left |
| cuda:3 | 27535 MiB | M64 v6 训练 | step 76500/100000 |

### 收割结果
| 实验 | SR | 状态 |
|------|-----|------|
| **Random k=0.7 Long seed42** | **64.6%** (323/500) | → DONE ✓ |
| **L2norm k=0.9 Long seed42** | **81.0%** (405/500) | 已 DONE (之前注册) |

### M64 训练 ETA
step 76500/100000, 0.6 sps → 23500 steps remaining → **~10.9 hours → 约今天 16:45 完成**

### 新部署
- cuda:1: **L2norm k=0.3 Long seed43** — 已启动并确认 VRAM 分配，注册 RUNNING

---
