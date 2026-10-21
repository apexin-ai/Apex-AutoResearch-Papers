# analysis vtc training progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vtc_training_progress_20260521T205736_result.json`
- **Structured JSON:** [`008cc1e3ff7f55556fae.json`](../../sessions/00/008cc1e3ff7f55556fae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## VTC 训练进度汇总

### 1. M32 VTC-only (`westd-27271`, PID 921279)
| 指标 | 值 |
|------|-----|
| 当前 step | **74,150 / 100,000** (74.2%) |
| 当前 loss | ~2.44 |
| 训练速度 | **0.5 sps** → 每 50 steps 约 92s → **~1,957 steps/h** |
| 进程运行时间 | 1天10小时 |
| 已保存 checkpoint | `checkpoint.pt` (latest) + `checkpoint_step70000.pt` |
| 预计到 100K | 还剩 25,850 steps → **约 13.2 小时** (~今晚 18:00) |

### 2. M96 (`westd-41074`, PID 68539)
| 指标 | 值 |
|------|-----|
| 当前 step | **72,550 / 100,000** (72.6%) |
| 当前 loss | ~2.75 |
| 训练速度 | **0.5 sps** → 每 50 steps 约 102s → **~1,765 steps/h** |
| 进程运行时间 | 1天17小时 |
| 已保存 checkpoint | `checkpoint.pt` (仅 latest，无 milestone) |
| 预计到 100K | 还剩 27,450 steps → **约 15.6 小时** (~今晚 20:30) |

### 3. M64 v6 (`westd-41074`, PID 59671)
| 指标 | 值 |
|------|-----|
| 当前 step | **23,750 / 100,000** (23.8%) |
| 当前 loss | ~2.86 |
| 训练速度 | **0.6 sps** → 每 50 steps 约 86s → **~2,093 steps/h** |
| 进程运行时间 | 11小时42分 |
| 已保存 checkpoint | `checkpoint_step10000.pt` + `checkpoint_step20000.pt` |
| 预计到 50K | 还剩 26,250 steps → **约 12.5 小时** (~今晚 17:30) |
| 预计到 100K | 还剩 76,250 steps → **约 36.4 小时** (~5月23日 17:00) |

### 关键判断

- **M32 和 M96** 都已过 70K，距 100K 完成约 13-16 小时，**今天内无需准备 eval**，明天凌晨前后完成。
- **M64 v6** 刚过 20K，距 50K checkpoint 还有约 12.5 小时。如果需要在 50K 做中间评估，**明天早上准备 eval 即可**。
- M96 只有 latest checkpoint 没有 milestone 保存，如果需要 50K/70K 中间 checkpoint，已经来不及了（已过）。

---
