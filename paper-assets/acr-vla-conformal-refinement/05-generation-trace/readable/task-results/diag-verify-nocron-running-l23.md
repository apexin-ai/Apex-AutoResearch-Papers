# diag verify nocron running L23

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_verify-nocron-running-L23_20260521T025235_result.json`
- **Structured JSON:** [`99da05f57f6c4baa2471.json`](../../sessions/99/99da05f57f6c4baa2471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

| exp_id | 进程状态 | 已运行 | 进度/结果 |
|--------|---------|--------|----------|
| eval-obs-only-object-norm003-seed66 | **RUNNING** | 1h22m | 3.5/10 tasks (~35%), 20 rollouts/task |
| eval-obs-only-object-norm005-seed66 | **RUNNING** | 1h22m | 3.5/10 tasks (~35%), 20 rollouts/task |
| eval-obs-only-object-norm01-seed66 | **RUNNING** | 1h22m | 4/10 tasks (40%), 20 rollouts/task |
| eval-obs-only-object-norm01-seed51-r3 | **RUNNING** | 2h14m | 9.5/10 tasks (~95%), 即将完成 |
| eval-obs-only-object-norm01-seed52-r3 | **RUNNING** | 2h14m | 9.5/10 tasks (~95%), 即将完成 |
| eval-obs-only-object-norm003-seed62-r2 | **DEAD → DONE(failed)** | — | 在第10个task(orange_juice) rollout 5/10处中断，无错误信息，疑似被kill |
| eval-obs-only-object-norm003-seed63-r2 | **DEAD → DONE(failed)** | — | 同上，完全相同的中断点 |

两个死亡实验都在完全相同的位置中断（task 10/10, rollout 5/10），且都在 cuda:3/cuda:4 上，无错误日志 — 大概率被外部 kill（OOM killer 或手动）。这两个需要重跑。bjb1-32546 的 seed51/seed52 预计几分钟内完成。bjb1-18228 的 3 个实验预计还需 ~2h。

---
