# diagnosis exp003 training progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-training-progress_20260521T073739_result.json`
- **Structured JSON:** [`ea4436854b6d2dd4bf3f.json`](../../sessions/ea/ea4436854b6d2dd4bf3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### 1. exp-003 (PID 70649, cuda:1) — seed1

| 指标 | 值 |
|------|-----|
| 估算当前 step | **~7670 / 8000** |
| 进度 | **~95.9%** |
| 最新 checkpoint | checkpoint-7500（14:10 保存） |
| 每 step 耗时 | ~30.8s（从 ckpt-7000→7500 间距推算） |
| 预估完成时间 | **~今天 18:25**（约 2h50m 后） |

> 注：stdout 输出到 tmux pipe，无独立日志文件。当前 step 通过 checkpoint 时间戳推算。

### 2. exp-003-s2 (PID 237432, cuda:0) — seed2

| 指标 | 值 |
|------|-----|
| 当前 step | **3571 / 8000** |
| 进度 | **44.6%** |
| 最新 checkpoint | checkpoint-3500（15:00 保存） |
| 每 step 耗时 | ~29-31s |
| reward (最近) | ~0.53-0.59 |
| 预估完成时间 | **~5月23日 04:00**（约 37h 后） |

### 3. Checkpoints

**exp003_r3only_seed1** (exp-003):
- checkpoint-500 ~ checkpoint-7500：15 个，每 500 步一个 ✓
- **ckpt-7500: 已生成** ✓
- **ckpt-8000: 未生成**（预计 ~18:25）

**exp003_r3only_seed2** (exp-003-s2):
- checkpoint-500 ~ checkpoint-3500：7 个 ✓

### 4. GPU 状态

| GPU | 型号 | 利用率 | 显存 | 温度 | 任务 |
|-----|------|--------|------|------|------|
| 0 | RTX PRO 6000 (98GB) | **98%** | 38049/97887 MiB | 53°C | exp-003-s2 |
| 1 | RTX PRO 6000 (98GB) | **89%** | 38161/97887 MiB | 54°C | exp-003 |

两个 GPU 负载健康，温度正常。exp-003 约 3 小时后完成训练。

---
