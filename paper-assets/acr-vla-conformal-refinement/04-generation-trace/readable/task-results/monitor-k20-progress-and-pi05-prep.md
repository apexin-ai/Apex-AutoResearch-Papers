# monitor k20 progress and pi05 prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_k20-progress-and-pi05-prep_20260521T070719_result.json`
- **Structured JSON:** [`23f06093b7a4ccc892dd.json`](../../sessions/23/23f06093b7a4ccc892dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署方案已写入 `artifacts/pi05_eval_deploy_plan.md`。

---

## 汇总

### K=20 实验进度

| 实验 | 状态 | Tasks | SR | 预计完成 |
|------|------|-------|----|---------|
| **object-seed45** (bjb2-28827) | 运行中 | 9.5/10 | ~18% | ~10 min |
| **spatial-seed43** (bjb1-18228) | **已完成** | 10/10 | **34.0%** | - |
| **spatial-seed44** (bjb1-18228) | **已完成** | 10/10 | **34.0%** | - |
| **spatial-seed42** (bjb1-32546) | 运行中 | 9/10 | ~39% | ~15-20 min |

Spatial K=20 seed43/44 结果完全一致（34.0%），seed42 预计在 36-40% 区间。Object seed45 预计 ~18-20%。

### π0.5 部署方案

- 6 个 baseline eval 命令已就绪（分配到 3 台服务器 6 张 GPU）
- 等 fix Worker 完成 vision tower 修复 + quick verify 后即可部署
- CRM 训练推荐方案 A（训练 obs_dim=2048 的新 CRM）

---
