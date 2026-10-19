# diagnose cron false positives batch 20260521

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cron-false-positives-batch-20260521_20260521T025216_result.json`
- **Structured JSON:** [`5135884726417c2cb2b2.json`](../../sessions/51/5135884726417c2cb2b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed65 已修复。

## 诊断结果汇总

| # | exp_id | 服务器 | 实际状态 | SR | 说明 |
|---|--------|--------|----------|-----|------|
| 1 | `eval-obs-only-object-norm005-seed62` | bjb2-28827 | **真正 failed** | — | 进程已死，日志停在 task1 rollout 5/10，无输出 JSON |
| 2 | `eval-obs-only-object-norm005-seed63` | bjb2-28827 | **真正 failed** | — | 同上 |
| 3 | `eval-obs-only-object-norm01-seed61` | bjb2-28827 | **真正 failed** | — | 同上 |
| 4 | `eval-obs-only-object-norm005-seed65` | bjb1-18228 | **completed (已修复)** | **14.0%** (14/100) | false positive，registry 已更新 conclusion=success + metrics |
| 5 | `eval-obs-only-object-norm005-seed55-r2` | bjb1-18228 | **真正 failed** | — | 启动即失败：`nohup: failed to run command 'python': No such file or directory`（conda env 未激活） |

**已修复**: 1 个（seed65）
**需要重跑**: 4 个（bjb2 的 seed62/seed63/seed61 进程中途死亡；bjb1 的 seed55-r2 启动失败）

---
