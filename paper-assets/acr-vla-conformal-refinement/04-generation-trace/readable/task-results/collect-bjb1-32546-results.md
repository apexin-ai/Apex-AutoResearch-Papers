# collect bjb1 32546 results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_bjb1-32546-results_20260528T001531_result.json`
- **Structured JSON:** [`19797977d63d80b19c06.json`](../../sessions/19/19797977d63d80b19c06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry updates done. Here's the summary:

## bjb1-32546 调查结果

### 已完成实验（已更新 registry → DONE）

| Exp ID | Benchmark | Seed | SR | Trigger Rate | Exit Code | 日志清洁 |
|--------|-----------|------|----|-------------|-----------|---------|
| crm-always-on-long-s44 | Long | 44 | **43.0%** | 100% | 0 | 无 OOM/CUDA error |
| crm-always-on-goal-s45 | Goal | 45 | **82.0%** | 100% | 0 | 无 OOM/CUDA error |
| crm-always-on-goal-s46 | Goal | 46 | **80.0%** | 100% | 0 | 无 OOM/CUDA error |
| crm-always-on-spatial-s46 | Spatial | 46 | **78.5%** | 100% | 0 | 无 OOM/CUDA error |

### 正在运行（已更新 registry → RUNNING）

| Exp ID | Benchmark | Seed | GPU | 进度 |
|--------|-----------|------|-----|------|
| crm-always-on-object-s46 | Object | 46 | cuda:2 (1914MiB) | 进行中（pick_up tasks） |
| crm-always-on-long-s45 | Long | 45 | cuda:5 (4305MiB) | 进行中（~task 6-7/10） |

### 未部署的 PREPARING 实验

- `crm-always-on-spatial-s45`、`crm-always-on-object-s45` 仍在 PREPARING，本机无运行痕迹

### GPU 状态（6x RTX 4090）

| GPU | 状态 |
|-----|------|
| 0 | 空闲 |
| 1 | 空闲 |
| 2 | 占用（object-s46） |
| 3 | 空闲 |
| 4 | 空闲 |
| 5 | 占用（long-s45） |

**4 个 GPU 空闲可用**（cuda:0, 1, 3, 4）。两个正在运行的实验预计数小时内完成。

---
