# check v4 training status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v4-training-status_20260514T221545_result.json`
- **Structured JSON:** [`20c180b9b61b259106d8.json`](../../sessions/20/20c180b9b61b259106d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. no_trace_seed42_v4 — STILL RUNNING (重跑)

| 项目 | 值 |
|------|-----|
| PID 835084 | 存活，运行 3m39s |
| 训练进度 | 75/444 steps (17%) |
| GPU 0 | 100% 利用率, 75.6 / 97.9 GB |

**注意**: 之前的 v4 训练已完成（checkpoint-148/296/444/final 全存在，时间戳 May 15 02:08–02:22）。当前 PID 是一次**重跑**，会覆盖之前的 checkpoint。

之前完成的 eval 结果：
- accuracy: **75.13%** (majority baseline: 71.51%, lift: +3.6%)
- pass_f1: 0.813, fail_f1: 0.627

---

### 2. vota_seed42_v4 — CRASHED (OOM)

| 项目 | 值 |
|------|-----|
| PID 835161 | 已死 |
| 崩溃点 | step 0/444，立即 OOM |
| 原因 | 尝试使用 GPU 0，但 no_trace 重跑已占用 ~23.6 GB，无法再分配 4.64 GB |
| EXIT_CODE | 1 |

**注意**: 之前的 v4 训练也已完成（checkpoint-444 + final 全存在，时间戳 May 15 02:46–05:36）。

之前完成的 eval 结果：
- accuracy: **99.16%** (majority baseline: 71.51%, lift: +27.6%)
- pass_precision: 1.0, fail_recall: 1.0, fail_f1: 0.985

---

### 关键发现

两个 v4 实验的**首次训练都已成功完成并产出了 eval 结果**。当前看到的 PID 是某次重跑（可能是上一个 session 重复提交），no_trace 重跑在进行中（会覆盖已有 checkpoint），vota 重跑因 GPU 0 被占而 OOM 崩溃。

vota (99.16%) vs no_trace (75.13%) 差距巨大，trace 信号对判决准确率有决定性作用。

---
