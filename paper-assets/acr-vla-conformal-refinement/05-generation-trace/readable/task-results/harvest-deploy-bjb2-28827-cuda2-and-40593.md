# harvest deploy bjb2 28827 cuda2 and 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest-deploy_bjb2-28827-cuda2-and-40593_20260520T132332_result.json`
- **Structured JSON:** [`94f5791d9ee60673fa76.json`](../../sessions/94/94f5791d9ee60673fa76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正在加载模型。

## 收割结果汇总

| # | exp_id | 结果 | SR | Registry 状态 |
|---|--------|------|----|--------------|
| 1 | eval-obs-only-spatial-norm02-seed46-r2 | JSON ✓ | **33.0%** | 已 DONE/success（之前自动收割） |
| 2 | eval-vla-only-goal-seed44-r2 | JSON ✓ | **73.0%** | 已 DONE/success（之前自动收割） |
| 3 | eval-argmin-object-k5-seed44-r2 | JSON ✓ | **11.0%** | 已 DONE/success（之前自动收割） |
| 4 | eval-openvla-object-baseline-seed42 | 部分结果 (400/500 ep) | **68.0%** partial | DONE/killed (timeout)，今天有新 re-run 在跑 (ep 404+) |
| 5 | eval-perdof-object-norm02-seed48 | JSON ✓ | **7.0%** | 已 DONE，conclusion 从 killed → **success** 已修正 |
| 6 | eval-obs-only-object-norm005-seed43 | JSON ✓ | **13.0%** | 已 DONE/success（之前已完成） |

这 6 个实验均已被 cron hook 自动收割（不再是 RUNNING phantom）。仅 #5 的 conclusion 需要从 killed 修正为 success。

## 新实验部署

| exp_id | 服务器 | GPU | PID | 状态 |
|--------|--------|-----|-----|------|
| eval-obs-only-spatial-norm02-seed49 | bjb2-28827 | cuda:2 | **357291** | 已启动，模型加载中 |
| eval-vla-only-object-seed50 | — | — | — | **已完成**（bjb1-18228, SR=9.0%），无需重新部署 |

bjb2-40593 cuda:0 空闲，可用于其他实验。

---
