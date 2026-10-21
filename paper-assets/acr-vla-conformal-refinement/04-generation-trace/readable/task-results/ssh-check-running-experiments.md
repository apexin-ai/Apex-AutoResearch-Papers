# ssh check running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-running-experiments_20260520T070451_result.json`
- **Structured JSON:** [`5a26d3bd662c68c2748b.json`](../../sessions/5a/5a26d3bd662c68c2748b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部确认 **RUNNING_ON_SERVER**，无需回退。

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| eval-obs-only-object-norm02-seed42 | 235678 | cuda:3 | task 2/10 (~15%) | RUNNING ✓ |
| eval-random-selection-object-seed42 | 235076 | cuda:0 | task 2/10 (~15%) | RUNNING ✓ |
| eval-random-selection-object-seed44 | 235343 | cuda:2 | task 2/10 (~15%) | RUNNING ✓ |

3 个都在 14:40 UTC 启动，各有独立 tmux session。今天的重新部署确实执行了，进程在跑。磁盘上的 `eval_object_random_selection_seed44.json`（SR=0.13）是旧结果，新运行完成后会覆盖。

另外注意到 cuda:1 上还跑着一个 `eval-crm-long-seed52`（PID 204921，13:38 启动，CPU 时间 500min），不在本次检查范围内。

Registry 已更新 notes 记录了 PID 和确认时间，无需状态变更。

---
