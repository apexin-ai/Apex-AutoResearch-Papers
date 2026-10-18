# urgent cqa1 status and fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_cqa1_status_and_fill_20260525T034151_result.json`
- **Structured JSON:** [`ae742645f517485e6a67.json`](../../sessions/ae/ae742645f517485e6a67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已杀掉重复提交的 tmux 会话。

---

## 汇总

### 本轮完成的 4 个实验（cqa1-33015）

| 实验 | Suite | Method | k | Seed | SR | 对比 seed |
|------|-------|--------|---|------|-----|-----------|
| l2norm_k085_object_seed43_postfix | Object | L2norm | 0.85 | 43 | **99.0%** | seed42=98.0% |
| random_k085_spatial_seed43_postfix | Spatial | Random | 0.85 | 43 | **59.2%** | seed42=52.6% |
| random_k085_long_seed43_v2 | Long | Random | 0.85 | 43 | **42.0%** | 首个数据点 |
| l2norm_k085_goal_seed43_postfix | Goal | L2norm | 0.85 | 43 | **87.0%** | seed42=87.4% |

跨 seed 稳定性良好，L2norm Object/Goal 差异均 <2pp。

### 新实验提交情况

用户指定的 2 个实验 **已在 registry 中完成**（之前在 westd-41074 跑过），无需重跑：
- l2norm_k085_goal_seed42_postfix: SR=87.4% ✅
- random_k085_object_seed42_postfix: SR=5.6% ⚠️（异常低，可能需要检查）

**cqa1-33015 全部 4 个 GPU 当前空闲**，可提交新任务。

---
