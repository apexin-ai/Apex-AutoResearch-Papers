# kill and redeploy bjb2 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_kill-and-redeploy_bjb2-bjb1-32546_20260528T044006_result.json`
- **Structured JSON:** [`c0b6748e8d7cceac641c.json`](../../sessions/c0/c0b6748e8d7cceac641c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 1. Kill 结果

| 服务器 | 操作 | GPU 释放确认 |
|--------|------|-------------|
| bjb2-28827 | kill -9 95782 97560 | cuda:0-5 全部 0 MiB ✓ |
| bjb1-32546 | kill -9 515230 515586 | cuda:3 = 2 MiB, cuda:4 = 2 MiB ✓ (cuda:0/1/2 有 Pi05 goal-s43/s44, object-s44 正常运行) |

## 2. bjb1-32546 部署

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:3 | `eval-random-selection-object-seed43-v2` | 550552 | Random selection K=10, n_rollouts=20, plan_600 |
| cuda:4 | `eval-ksweep-k20-obs-object-s44` | 550832 | K=20 obs_only CRM, n_rollouts=20, plan_601 |

## 3. bjb2-28827 部署

所有 Pi05 CRM always-on seed 已铺开（object-s44/goal-s43/goal-s44 在 bjb1-32546 cuda:0/1/2；spatial-s43/s44/long-s43/s44 在 bjb1-18228；long-s42 在 cqa1）。改为填补 SmolVLA tau-sweep spatial s42 缺口：

| GPU | exp_id | PID | 说明 |
|-----|--------|-----|------|
| cuda:4 | `smolvla-tau025-spatial-s42` | 112960 | τ=0.25 spatial s42, 最关键缺口 |
| cuda:5 | `smolvla-tau020-spatial-s42` | 113242 | τ=0.20 spatial s42, 密化 sweep 曲线 |

---
