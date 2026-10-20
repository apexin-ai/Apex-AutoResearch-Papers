# monitor training status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-status-check_20260515T042501_result.json`
- **Structured JSON:** [`09404dadedf512564eda.json`](../../sessions/09/09404dadedf512564eda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告（May 15 12:25 UTC）

### GPU 概览

| GPU | 进程 | 显存 | 利用率 | 温度 | 功耗 |
|-----|------|------|--------|------|------|
| 0 | PID 328094（未知） | 17.2/32.6 GB | 76% | 56°C | 415W |
| 1 | CLS 8B s42 resume | 27.3/32.6 GB | 98% | 71°C | 466W |
| 2 | CWM 8B | 30.7/32.6 GB | 82% | 67°C | 454W |
| 3 | CLS 8B seed123 | 30.9/32.6 GB | 97% | 72°C | 574W |

3 个训练进程全部存活。GPU 0 有一个未知的 python3 进程（PID 328094）。

---

### 1. CLS 8B seed123 v3（PID 266444 → 266449, cuda:3）

| 指标 | 值 |
|------|-----|
| 进度 | **6092 / 6633（91.8%）** |
| 最近 eval_loss（step 6000） | **0.3525**，epoch 2.71 |
| 最近 train_loss（step 6050） | **0.2067** |
| 速度 | ~8.2 s/step |
| 预估完成 | **~May 15 13:40 UTC**（约 75 分钟） |
| 异常 | 无 |

Checkpoints：`checkpoint-200, checkpoint-5400, checkpoint-5600, checkpoint-5800, checkpoint-6000`

---

### 2. CWM 8B（PID 266816, cuda:2）

日志实际路径：`repo-level-cwm-8b-conda-v2.log`（非 v4）

| 指标 | 值 |
|------|-----|
| 进度 | **3225 / 6633（48.6%）** |
| 最近 eval_loss（step 3200） | **0.4462**，epoch 1.4 |
| 速度 | ~12 s/step |
| 预估完成 | **~May 16 00:00 UTC**（约 11.5 小时，含 eval 暂停） |
| 异常 | 无 |

Checkpoints：`checkpoint-400, checkpoint-2900, checkpoint-3000, checkpoint-3100, checkpoint-3200`

---

### 3. CLS 8B s42 resume（PID 295794, cuda:1）

| 指标 | 值 |
|------|-----|
| 进度 | **2557 / 6633（38.6%）** |
| 最近 eval_loss（step 2400） | **0.3444**，epoch 1.09 |
| 最近 train_loss（step 2550） | **0.2881** |
| 速度 | ~8.2 s/step |
| 预估完成 | **~May 15 21:45 UTC**（约 9.3 小时，含 eval 暂停） |
| 异常 | 无 |

---

### 关键发现

- **seed123 将在约 75 分钟内完成**（比之前预估的 14:25 UTC 提前约 45 分钟）
- CWM 的 eval_loss（0.446）明显高于两个 CLS 实验（0.35 / 0.34），CWM 任务本身更难
- GPU 0 有一个未在监控列表中的进程（PID 328094），占 17.2 GB 显存

---
