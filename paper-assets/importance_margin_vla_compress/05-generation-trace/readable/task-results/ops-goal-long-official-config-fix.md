# ops goal long official config fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_goal_long_official_config_fix_20260522T121752_result.json`
- **Structured JSON:** [`2e6eee25a8c9e203ac1f.json`](../../sessions/2e/2e6eee25a8c9e203ac1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果来了。汇总报告：

---

## 产出汇总

### 1. 官方配置 vs 我们的配置差异表

| Suite | LeRobot 官方 | 我们的旧设置 | 已修复 |
|-------|------------|------------|--------|
| libero_object | 280 | 280 ✓ | 280 |
| libero_spatial | **280** | **400 (+43%)** | **280** ✓ |
| libero_goal | **300** | **400 (+33%)** | **300** ✓ |
| libero_10 | 520 | 520 ✓ | 520 |

### 2. 根因诊断（重要！）

**Goal/Long 0% SR 不是 max_steps 问题**（Goal 我们给 400 步比官方 300 还多，Long 完全匹配）。

**真正原因：cqa1 的 lerobot 0.5.1 有 bug，westd 的 0.5.2 正常。**
- 同一模型权重（MD5 一致），同一评估代码（294行，功能相同）
- cqa1 (lerobot 0.5.1): Goal 0%, Long 0%
- westd (lerobot 0.5.2): Goal l2norm k0.9 = 90%, Long l2norm k0.95 = 86%

### 3. 代码修复

三台服务器 `eval_pi05_pruning_libero.py` 的 `SUITE_CONFIG` 已更新：
- `libero_spatial`: 400 → **280**
- `libero_goal`: 400 → **300**
- 服务器: westd-38929, westd-41074, cqa1-33015

### 4. Kill 的进程

| 服务器 | PID | 实验 | 原因 |
|--------|-----|------|------|
| cqa1-33015 | 352950 | baseline_goal | lerobot 0.5.1 bug, 0% SR |
| cqa1-33015 | 353384 | baseline_long | lerobot 0.5.1 bug, 0% SR |

### 5. 新部署的进程

| 服务器 | GPU | PID | 实验 | max_steps | 早期结果 |
|--------|-----|-----|------|-----------|---------|
| westd-38929 | 1 | 90798 | baseline_goal | 300 (官方) | **T0 ep10: 70%** ✅ |
| westd-38929 | 2 | 91245 | baseline_long | 520 (官方) | 加载中 |

### 6. 需要重跑的实验（max_steps 影响）

**libero_goal** 旧结果用 max_steps=400 (官方 300)，多 33% 步数，结果可能偏高：
- `pi05_l2norm_k0.90_libero_goal_seed42` (SR=90.0%) — 需重跑
- `pi05_random_k0.90_libero_goal_seed42` (SR=62.6%) — 需重跑
- Phase 2 cliff sweep goal 实验（如果已部署）

**libero_spatial** 旧结果用 max_steps=400 (官方 280)，多 43% 步数，结果可能偏高：
- `pi05_baseline_libero_spatial_seed42` (SR=97.2%) — 需重跑
- 所有 pi05_*_spatial_* 结果 — 需重跑

**libero_10 (Long)**: max_steps=520 正确，不需要因 max_steps 重跑。
- `l2norm_k095_long` (westd-38929 GPU 0, 进行中, ~86%) — **有效，不需要 kill**

**cqa1 上的所有结果**: lerobot 0.5.1 有 bug，cqa1 需升级到 0.5.2 后才能跑实验。

---
