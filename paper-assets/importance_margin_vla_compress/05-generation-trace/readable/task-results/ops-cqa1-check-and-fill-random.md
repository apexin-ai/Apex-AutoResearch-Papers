# ops cqa1 check and fill random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-check-and-fill-random_20260521T022829_result.json`
- **Structured JSON:** [`a01fbae654444488f354.json`](../../sessions/a0/a01fbae654444488f354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 models are loading. Here's the summary:

## 实验状态

### 4 个原始实验

| 实验 | GPU | 状态 | 结果 |
|------|-----|------|------|
| eval_xvla_goal_k09_seed42 | cuda:0 | **日志不存在** | — |
| eval_xvla_goal_k05_seed42 | cuda:3 | **日志不存在** | — |
| eval_xvla_baseline_long_seed42 | cuda:1 | **日志不存在** | — |
| eval_xvla_spatial_k085_seed42 | cuda:2 | **运行中** (Task 7, Ep 17/50) | 见下 |

Goal k=0.9、Goal k=0.5、Long baseline 的日志在 cqa1-33015 上不存在——可能从未在此服务器启动，或在其他服务器上。

### Spatial k=0.85 逐 task 结果（进行中）

| Task | SR |
|------|----|
| 0 | 100.0% (50/50) |
| 1 | 2.0% (1/50) |
| 2 | 96.0% (48/50) |
| 3 | 98.0% (49/50) |
| 4 | 88.0% (44/50) |
| 5 | 4.0% (2/50) |
| 6 | 94.0% (47/50) |
| 7 | 进行中 (Ep 17/50, 多数 FAIL) |
| 8-9 | 待跑 |

**剩余时间估计**: Task 7 多数 fail（每 ep ~20s），剩 33 eps ~11 min。Task 8、9 各 5-18 min。预计 **20-45 min** 后完成（~11:15 前）。

### 新提交的 Random Pruning 实验

| exp_id | GPU | keep_ratio | 状态 |
|--------|-----|-----------|------|
| eval_xvla_random_k09_object_seed42 | cuda:0 | 0.9 | 模型加载中 |
| eval_xvla_random_k085_object_seed42 | cuda:3 | 0.85 | 模型加载中 |
| eval_xvla_random_k08_object_seed42 | cuda:1 | 0.8 | 模型加载中 |

**cuda:2** 仍被 spatial_k085 占用，待其完成后可提交 `eval_xvla_random_k05_object_seed42` (keep_ratio=0.5)。

---
