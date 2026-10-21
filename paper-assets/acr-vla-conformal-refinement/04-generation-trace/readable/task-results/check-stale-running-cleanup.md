# check stale running cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_stale-running-cleanup_20260524T234143_result.json`
- **Structured JSON:** [`31d030b1cfac169932e7.json`](../../sessions/31/31d030b1cfac169932e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 仍在运行（7 个）

| 实验 | 服务器 | PID | 已运行 | 进度 |
|------|--------|-----|--------|------|
| eval-k2-tau030-spatial-s42 | bjb2-28827 | 475018 | ~1h49m | K=2 τ=0.30 |
| eval-k2-tau020-spatial-s42 | bjb1-32546 | 788091 | ~1h49m | K=2 τ=0.20 |
| eval-k2-tau015-spatial-s42 | bjb2-40593 | 319999 | ~1h06m | K=2 τ=0.15 |
| eval-k2-tau010-spatial-s42-r2 | bjb2-40593 | 327584 | ~19min | K=2 τ=0.10 |
| eval-supp-long-vla-only-s43-r2 | bjb1-32546 | 727400 | ~3h29m | long vla s43 |
| eval-supp-long-vla-only-s48 | cqa1-32758 | 91476 | ~4h07m | long vla s48, 7/10 tasks done |
| precompute-pi05-long-2048-r2 | bjb1-18228 | 114507 | 2d 3h | 95100/136090 (70%), ~22h remaining |

### 已完成但 registry 未更新（14 个）— 需要 harvest

| 实验 | 服务器 | SR | 结果文件 |
|------|--------|----|----------|
| **eval-supp-obj-vla-only-s42** | bjb1-32546 | **79.0%** (158/200) | eval_object_vla_only_seed42.json |
| **eval-supp-obj-vla-only-s43** | bjb1-32546 | **77.0%** (154/200) | eval_object_vla_only_seed43.json |
| **eval-supp-obj-vla-only-s44** | bjb1-32546 | **77.5%** (155/200) | eval_object_vla_only_seed44.json |
| **eval-supp-goal-vla-only-s42-bjb1** | bjb1-32546 | **83.5%** (167/200) | eval_goal_vla_only_seed42.json |
| **eval-supp-crm-norm005-goal-s48** | bjb2-28827 | **80.0%** (160/200) | eval_goal_crm_obs_only_norm0.05_seed48.json |
| **eval-supp-crm-norm005-spatial-s49** | bjb2-28827 | **78.5%** (157/200) | eval_spatial_crm_obs_only_norm0.05_seed49.json |
| **eval-supp-crm-norm005-spatial-s48** | bjb2-28827 | **78.0%** (156/200) | eval_spatial_crm_obs_only_norm0.05_seed48.json |
| **crm-norm005-goal-s49** | bjb1-18228 | **83.5%** (167/200) | eval_goal_crm_obs_only_norm0.05_seed49.json |
| **crm-norm005-object-s48** | bjb1-18228 | **73.5%** (147/200) | eval_object_crm_obs_only_norm0.05_seed48.json |
| **eval-supp-goal-vla-only-s42** | cqa1-32758 | **82.0%** (164/200) | eval_goal_vla_only_seed42.json |
| **eval-supp-goal-vla-only-s43** | cqa1-32758 | **83.5%** (167/200) | eval_goal_vla_only_seed43.json |
| **eval-supp-goal-vla-only-s44** | cqa1-32758 | **85.0%** (170/200) | eval_goal_vla_only_seed44.json |
| **eval-supp-goal-vla-only-s50** | cqa1-32758 | **80.0%** (160/200) | eval_goal_vla_only_seed50.json |
| **eval-supp-spatial-vla-only-smolvla-s42** | cqa1-32758 | **78.5%** (157/200) | eval_spatial_vla_only_seed42.json |

### 异常

- **eval-supp-goal-vla-only-s42** (cqa1) 和 **eval-supp-goal-vla-only-s42-bjb1** (bjb1-32546) 是同一实验在两台机器上的冗余运行，结果略有差异（82.0% vs 83.5%）。
- **precompute-pi05-long-2048-r2** 已跑 2 天多，还需约 22 小时才完成。
- bjb1-18228 上同时有 3 个 `train_crm.py` 进程在跑（PID 326315, 433318, 433319），不在 RUNNING registry 中。

---
