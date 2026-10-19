# survey orphan experiments check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_survey_orphan-experiments-check_20260517T221108_result.json`
- **Structured JSON:** [`e1687dec91882b6f99e6.json`](../../sessions/e1/e1687dec91882b6f99e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Orphan 实验（bjb1-18228）

| 实验 | 状态 | PID | 进度 | 预计剩余 |
|------|------|-----|------|----------|
| eval-obs-only-object-norm02-k5-seed42 | **ALIVE** (已重试) | 713405 | 4/10 tasks done | ~5h |
| eval-obs-only-object-norm02-k20-seed42 | **ALIVE** (已重试) | 713480 | 1/10 tasks done (第2个task进行中) | ~27h |

两个实验之前确实以 EXIT_CODE=129 (SIGHUP) 失败过，但已被自动重试（retry_count=1）。当前重试实例在 bjb1-18228 上正常运行，started ~02:54 UTC。Registry 的 RUNNING 状态正确，`failure_reason`/`completed_at` 是上一次失败的残留字段。

K=20 实验因为每步采样 20 个候选，速度远慢于 K=5，预计还需 ~27 小时。

### Cron 监控实验

| 实验 | 服务器 | PID | 状态 | 运行时间 |
|------|--------|-----|------|----------|
| eval-obs-only-object-norm01-seed46 | bjb2-28827 | 449068 | **ALIVE** (Rl) | 4h08m |
| eval-perdof-object-norm02-seed43-r3 | bjb2-28827 | 449339 | **ALIVE** (Rl) | 4h08m |
| eval-perdof-object-norm02-seed45-r3 | bjb1-32546 | 749540→749547 | **ALIVE** (Rl) | 1h10m |
| eval-obs-only-object-norm005-seed43 | bjb2-28827 | 476529→476536 | **ALIVE** (Rl) | 1h09m |

所有 6 个实验均正常运行，无需 registry 更新。

---
