# infra westd gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-gpu-status-check_20260514T193803_result.json`
- **Structured JSON:** [`35312fedb9721f17fff5.json`](../../sessions/35/35312fedb9721f17fff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告（2026-05-15 03:38 UTC+8）

### GPU 0 — 空闲，eval 已完成

CWM seed123 eval 完成于 **02:25 UTC+8**，结果：

| 指标 | 值 |
|------|-----|
| Accuracy | 59.09% |
| Majority baseline | 72.96% |
| Gap vs majority | **-13.87pp** |
| F1_macro | 43.43% |
| F1_fail | 13.67% (P=15.9%, R=12.0%) |
| F1_pass | 73.19% (P=70.1%, R=76.5%) |
| Unparseable | **6574/9784 (67.2%)** |
| Checkpoint | checkpoint-500 |
| 模型 | Qwen3-4B |

### GPU 1 — 空闲，eval 已完成

CWM v12 eval 完成于 **02:13 UTC+8**，结果：

| 指标 | 值 |
|------|-----|
| Accuracy | 58.04% |
| Majority baseline | 72.96% |
| Gap vs majority | **-14.91pp** |
| F1_macro | **51.67%** |
| F1_fail | 34.12% (P=29.7%, R=40.2%) |
| F1_pass | 69.22% (P=74.5%, R=64.7%) |
| Unparseable | **5255/9784 (53.7%)** |
| Checkpoint | checkpoint-500 |
| 模型 | Qwen3-4B |

### GPU 2 — 运行中：CWM 8B 训练 (`repo-level-cwm-8b-conda-v2`)

| 项 | 值 |
|----|-----|
| PID | **266816** (python3) |
| 启动时间 | 01:44 UTC+8，已运行 ~1h54m |
| 进度 | Step **1700/6633** (25.6%)，从 checkpoint-1600 恢复 |
| 当前状态 | 正在跑 validation（4438/9335 items） |
| 最新 loss | 0.2853（epoch 0.77） |
| 速度 | ~12s/step |
| 预计剩余 | ~16.4h（4933 steps） |

注意：这是**新提交的 v2 任务**，不是 ROADMAP 提到的旧 PID 210568。旧进程已结束。

### GPU 3 — 运行中：CLS 8B seed123 训练 (`repo-level-cls-8b-seed123-conda-v3`)

| 项 | 值 |
|----|-----|
| PID | **266449** (python3) / 266444 (bash wrapper) |
| 启动时间 | 01:43 UTC+8，已运行 ~1h55m |
| 进度 | Step **3200/6633** (48.3%)，从 checkpoint-3000 恢复 |
| 当前状态 | 正在跑 validation（583/9335 items） |
| 最新 loss | **0.17**（epoch 1.45） |
| 速度 | ~8s/step |
| 预计剩余 | ~7.6h（3433 steps） |

注意：实际 python PID 是 266449（不是任务描述的 266896），bash wrapper PID 266444 一致。

---

**关键发现**：两个 CWM eval 的 accuracy 都低于 majority baseline（~73%），且 unparseable rate 极高（53-67%）。CWM v12 的 F1_macro（51.67%）明显优于 seed123（43.43%），主要得益于更好的 fail 类召回率（40.2% vs 12.0%）和更低的 unparseable rate。

---
