# diagnosis training progress 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_training-progress-29046_20260521T071752_result.json`
- **Structured JSON:** [`30aa32b4e0dd2997788c.json`](../../sessions/30/30aa32b4e0dd2997788c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据足够，汇总报告。

---

## 训练进度报告 — 2026-05-21 ~15:20 CST

### exp-003 (R3-only GRPO seed 1) — cuda:1

| 指标 | 值 |
|------|-----|
| PID | 70649 (存活，已运行 2d 14h 27m) |
| GPU 利用率 | 95%, 38161 MiB / 97887 MiB |
| 最新 checkpoint | **checkpoint-7500**（May 21 14:10 创建） |
| 估算当前 step | **~7636 / 8000** |
| 每步耗时 | ~30.9s（基于 ckpt-7000→7500 间隔 15441s） |
| 剩余步数 | ~364 |
| **预计完成** | **May 21 ~18:30 CST（约 3 小时后）** |
| 已有 checkpoints | 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500 |

> **注意**: `tee` 日志 (`logs/exp003_v2.log`) 在 step 3760 (May 20) 后停止更新，可能是 tee 管道缓冲问题。但 checkpoint 持续产出，训练本身正常。

### exp-003-s2 (R3-only GRPO seed 2) — cuda:0

| 指标 | 值 |
|------|-----|
| PID | 237432 (存活，已运行 1d 7h 1m) |
| GPU 利用率 | 95%, 38049 MiB / 97887 MiB |
| 日志确认 step | **3533 / 8000**（May 21 15:18） |
| 最新 checkpoint | **checkpoint-3500**（May 21 15:00 创建） |
| 每步耗时 | ~30.6s（基于 ckpt-3000→3500 间隔 15277s） |
| 剩余步数 | ~4467 |
| **预计完成** | **May 23 ~05:00 CST（约 38 小时后）** |
| 已有 checkpoints | 500, 1000, 1500, 2000, 2500, 3000, 3500 |

### 系统状态

- 磁盘 `/root/autodl-tmp`: 51G used / 250G total (21%) — 充足
- 无异常：两张 GPU 均 95% 利用率，进程稳定

### 关键时间线

- **exp-003 今天 ~18:30 完成** → 可立即跑 ckpt-8000 final eval
- **exp-003-s2 May 23 凌晨完成** → DDL May 25 前有约 2 天 buffer

---
