# diagnosis exp003 training progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-training-progress_20260521T075213_result.json`
- **Structured JSON:** [`10de4ab80cbff3e7c1dd.json`](../../sessions/10/10de4ab80cbff3e7c1dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态摘要

### exp-003 seed 1 (PID 70649, cuda:1)
- **进程状态**: 存活，已运行 2d15h
- **估算当前 step**: ~7700/8000（96%）
  - 最新 checkpoint: **checkpoint-7500**（May 21 14:10）
  - 500 steps ≈ 4h17m → ~30.8s/step
  - 距 ckpt-7500 已过 ~1h50m → 推算已跑 ~200 steps
- **ETA**: **今晚 ~18:20（服务器时间）** 完成 8000 steps
- **GPU**: 95% 利用率，38.2/97.9 GB 显存
- **注意**: 进程 stdout 走 pipe，无独立 log 文件可 tail。进度仅靠 checkpoint 时间戳推算。

### exp-003-s2 seed 2 (PID 237432, cuda:0)
- **进程状态**: 存活，已运行 1d7h35m
- **当前 step**: **3600/8000（45%）**（来自 log）
- **速度**: ~30s/step（28-33s 波动）
- **最新 checkpoint**: **checkpoint-3500**（May 21 15:00）
- **ETA**: **~May 23 04:30** 完成 8000 steps
- **GPU**: 90% 利用率，38.0/97.9 GB 显存

### 异常检查
- **无异常**。两个 GPU 利用率高且稳定，无 OOM、loss spike 迹象
- log 中的 `d_syc not loaded; returning R3-only rewards` 是 R3-only 模式的正常 warning
- 两个实验均在 May 25 DDL 之前完成，**exp-003 ckpt-8000（关键路径）预计今晚到手**

---
