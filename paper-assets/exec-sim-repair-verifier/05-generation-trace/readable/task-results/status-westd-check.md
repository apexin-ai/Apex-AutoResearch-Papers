# status westd check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-check_20260514T121912_result.json`
- **Structured JSON:** [`ad6f6c4b7531d702482f.json`](../../sessions/ad/ad6f6c4b7531d702482f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态报告

### 1. CWM v12 Eval (PID 195668, GPU 1)
- **状态**: 运行中，已运行 11h16m
- **进度**: 6416/9784 (**65.6%**), running_acc=**57.8%**
- **速度**: ~9.5 samples/min
- **预计完成**: 剩余 3368 samples → **~5.9h** → ETA **May 15 ~02:10**
- **GPU**: 83% 利用率, 12997/32607 MiB

### 2. CWM seed123 Eval (PID 195531, GPU 0)
- **状态**: 运行中，已运行 11h16m
- **进度**: 6344/9784 (**64.9%**), running_acc=**58.8%**
- **速度**: ~9.5 samples/min
- **预计完成**: 剩余 3440 samples → **~6.0h** → ETA **May 15 ~02:20**
- **GPU**: 86% 利用率, 12997/32607 MiB

### 3. CWM 8B Train (PID 210573, GPU 2)
- **状态**: 运行中，已运行 6h30m
- **进度**: 最新 checkpoint=900/6633 (**13.6%**), epoch=0.41，当前估计 ~step 980
- **速度**: ~2.56 steps/min (100 steps / 39 min)
- **预计完成**: 剩余 ~5650 steps → **~36.8h** → ETA **May 16 ~09:00**
- **GPU**: 95% 利用率, 31543/32607 MiB (几乎满载)

### 4. CLS 8B Train (PID 210657, GPU 3)
- **状态**: 运行中，已运行 6h30m
- **进度**: 最新 checkpoint=1800/6633 (**27.1%**), epoch=0.81，当前估计 ~step 1860
- **速度**: ~4.88 steps/min (200 steps / 41 min)
- **预计完成**: 剩余 ~4770 steps → **~16.3h** → ETA **May 15 ~12:40**
- **GPU**: 98% 利用率, 23605/32607 MiB

### Checkpoint 备份
| 模型 | 已备份 checkpoints | 最新备份时间 |
|------|-------------------|-------------|
| CLS 8B | 200, 800, 1400, 1600, 1800 | May 14 20:07 |
| CWM 8B | 500, 600, 700, 800, 900 | May 14 19:49 |

### Eval 结果
两个 eval 的结果目录均为空，尚未产出结果文件。

### 注意
- CWM 8B 训练进度明显慢于 CLS 8B（2.56 vs 4.88 steps/min），GPU 显存接近满载（31.5/32.6 GB）
- seed123 eval 的 running_acc (58.8%) 略高于 v12 eval (57.8%)

---
