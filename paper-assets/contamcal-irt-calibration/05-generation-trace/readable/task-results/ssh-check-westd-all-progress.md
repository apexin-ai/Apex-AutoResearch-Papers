# ssh check westd all progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-westd-all-progress_20260519T023437_result.json`
- **Structured JSON:** [`3d61c925dddd2d8d0325.json`](../../sessions/3d/3d61c925dddd2d8d0325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| exp_id | step | progress | loss | accuracy | ETA |
|--------|------|----------|------|----------|-----|
| **gemma2_9b_d050_s42** (cuda:1) | 370/3642 | 10.2% | 1.415 | 0.693 | ~13:03 UTC (约2h30m后) |
| **phi4_d025_s42** (cuda:2) | 1470/3384 | 43.4% | 1.177 | 0.730 | ~11:46 UTC (约1h12m后) |
| **phi4_d005_s42** (cuda:3) | 2291/3177 | 72.1% | 1.252 | 0.723 | ~11:16 UTC (约42m后) |
| **eval_14b_mmlu_arc** (cuda:0) | — | **PID 93847 已不存在** | — | — | — |

注意：
- gemma2_9b_d050 实际 total_steps=3642（非预估的 3384，因为 58266 samples / batch16 = 3642）
- gemma2_9b 在 GPU 1 利用率偏低（44%），速度 ~2.75s/step
- eval_14b (PID 93847) 已结束。GPU 0 当前被 PID 99071 占用（32.7GB VRAM, 94% util），非原始 4 个实验之一

### 额外发现 — 已完成的实验（从 exit 文件）
- `7b_d050_s123`: 完成于 03:03，EXIT_CODE=0，final loss=0.935
- `gemma2_9b_d025_s42`: 完成于 10:09
- `olmo2_7b_d000_s42`: 完成于 08:59
- `phi4_d000_s42`: 完成于 09:24
- `14b_d025/d050/d100_s42`: 全部完成（06:10 / 06:38 / 08:13）

### GPU 使用率
| GPU | VRAM | Util | Temp | Process |
|-----|------|------|------|---------|
| 0 | 32.7/97.9 GB | 94% | 77°C | PID 99071 (未知) |
| 1 | 54.9/97.9 GB | 44% | 52°C | gemma2_9b_d050_s42 |
| 2 | 59.7/97.9 GB | 88% | 71°C | phi4_d025_s42 |
| 3 | 57.7/97.9 GB | 89% | 52°C | phi4_d005_s42 |

### 磁盘
- `/root`: 19/30G (63%)
- `/root/autodl-tmp`: 148/250G (59%)

### OLMo-2-7B 下载状态
`OLMo-2-1124-7B` 目录已存在（May 19 05:00），下载完成。

---
