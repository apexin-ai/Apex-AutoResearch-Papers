# diagnosis exp003 progress check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-progress-check_20260520T084907_result.json`
- **Structured JSON:** [`234f1c57a512af652b37.json`](../../sessions/23/234f1c57a512af652b37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary:

---

## exp-003 (R3-only GRPO baseline) — PID 70649, GPU 1

| 指标 | 值 |
|------|-----|
| 当前 step | **~5000 / 8000** (62.5%) |
| 最新 checkpoint | checkpoint-5000 (16:46:12 今天) |
| 速度 | **~30s/step** (基于 ckpt-4000→5000 间隔) |
| 剩余 | ~3000 steps → **~25 小时** |
| ETA | **2026-05-21 ~18:00** (CST) |
| 进程状态 | Rl+ (运行中), 已运行 1天16小时 |
| GPU 利用率 | 89%, 38161/97887 MiB |
| reward/r3_mean | 0.697 (step 3760 时) |

**注意**: `exp003_v2.log` 在 step 3760 后停止更新（stdout 缓冲未刷盘），但 checkpoint 正常持续产出，进程存活。

## exp-003-s2 (R3-only seed 2) — PID 237432, GPU 0

| 指标 | 值 |
|------|-----|
| 当前 step | **~845 / 8000** (10.6%) |
| 最新 checkpoint | checkpoint-500 (13:51:22 今天) |
| 速度 | **~30s/step** |
| 剩余 | ~7155 steps → **~60 小时** |
| ETA | **2026-05-23 ~05:00** (CST) |
| 进程状态 | Ss+ (睡眠), 已运行 8.5小时 |
| GPU 利用率 | 91%, 38049/97887 MiB |
| reward/r3_mean | 0.48-0.57 |

## 异常

1. **exp-003 日志断流**: `exp003_v2.log` 停在 step 3760 (05:55)，但进程和 checkpoint 正常。可能是 nohup stdout 缓冲问题，不影响训练。
2. **`exp003_restart.log` 有崩溃记录**: 早期重启尝试因加载 `microsoft/deberta-v3-base` 失败报 OSError，但这是历史记录，当前运行不受影响。
3. **completions 全部截断**: `clipped_ratio=1.0`, `mean_terminated_length=0.0` — 所有 completion 都打满 max_length=256，没有自然终止的。
4. **`d_syc not loaded` WARNING**: 预期行为（R3-only 模式）。

---
