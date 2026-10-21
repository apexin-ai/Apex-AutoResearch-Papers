# audit westd 38929 sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-38929-sweep_20260521T150221_result.json`
- **Structured JSON:** [`197c7d1156e155c60cd7.json`](../../sessions/19/197c7d1156e155c60cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 当前运行中的 4 个实验（所有 GPU 占用）

| GPU | 实验 | 进度 | 预估剩余 |
|-----|------|------|----------|
| GPU0 | random_k05_seed42 | Task 7/10, Ep 30/50 (~66%) | ~1.5h |
| GPU1 | random_k07_seed43 | Task 6/10, Ep 30/50 (~56%) | ~2h |
| GPU2 | baseline_seed42 (PID 186981) | Task 8/10, Ep 20/50 (~74%) | ~1h |
| GPU3 | l2norm_k03_seed43 | Task 6/10, Ep 30/50 (~56%) | ~2h |

所有 GPU 均 ~16GB 显存占用，~70% 利用率。**无空闲 GPU。**

### 已完成的历史结果（eval_results/ 目录）

| 文件 | 模式 | k_ratio | Seed | SR |
|------|------|---------|------|----|
| l2norm_prune_k0_3_object | l2norm | 0.3 | 7 | **25.0%** |
| l2norm_prune_k05_object | l2norm | 0.5 | 7 | **39.2%** |
| l2norm_prune_k07_object | l2norm | 0.7 | 7 | **49.8%** |
| l2norm_prune_k0_9_object | l2norm | 0.9 | 7 | **70.6%** |
| l2norm_prune_k0_95_object | l2norm | 0.95 | 7 | **70.6%** |
| random_prune_k03_object | random | 0.3 | 7 | **21.4%** |
| random_prune_k07_object | random | 0.7 | 7 | **44.4%** |
| random_k07_seed42_v2 | random | 0.7 | 42 | **44.4%** |
| random_k095_seed42_v2 | random | 0.95 | 42 | **69.2%** |

### 运行中实验的中间 per-task 结果（截至目前）

**baseline_seed42** (最快完成，锚点实验):
- Task 6 tomato sauce: 78.0%, Task 7 butter: 58.0% — 目前看 baseline seed42 表现比较强，与 seed7 baseline 74.0% 应该在同一量级。

**无已完成的新实验需要更新 registry。** 4 个实验均仍在运行，预计 baseline_seed42 最先完成（~1h），l2norm_k03_seed43 和 random_k07_seed43 最后（~2h）。

---
