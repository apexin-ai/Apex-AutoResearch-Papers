# monitor bjb2 28827 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb2-28827-status_20260515T044924_result.json`
- **Structured JSON:** [`5c4999937ee915837f0f.json`](../../sessions/5c/5c4999937ee915837f0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 Magnitude Sweep Status

所有 6 个实验正在运行，6 块 RTX 4090 各跑一个。进程启动于 ~11:16，已运行约 1.5 小时。

| Experiment | Mode | Norm | Tasks Done | Total | Status |
|---|---|---|---|---|---|
| eval-mag-perdof-norm003 | acr_vla (perdof) | 0.03 | 1 (Task 2 进行中, 5/10 rollouts) | 10 | running |
| eval-mag-perdof-norm005 | acr_vla (perdof) | 0.05 | 1 (Task 2 进行中, 5/10 rollouts) | 10 | running |
| eval-mag-perdof-norm02 | acr_vla (perdof) | 0.2 | 1 (Task 2 进行中, 5/10 rollouts) | 10 | running |
| eval-mag-perdof-norm03 | acr_vla (perdof) | 0.3 | 1 (Task 2 进行中, 5/10 rollouts) | 10 | running |
| eval-mag-obsonly-norm005 | crm_obs_only | 0.05 | 2 (starting Task 3) | 10 | running |
| eval-mag-obsonly-norm02 | crm_obs_only | 0.2 | 2 (starting Task 3) | 10 | running |

### Per-task breakdown (已完成的 tasks)

**Task 1: pick_up_the_black_bowl_between_the_plate_and_the_ramekin...**

| Experiment | Norm | SR |
|---|---|---|
| perdof | 0.03 | 60% (6/10) |
| perdof | 0.05 | 50% (5/10) |
| perdof | 0.2 | 60% (6/10) |
| perdof | 0.3 | 70% (7/10) |
| obs_only | 0.05 | 80% (8/10) |
| obs_only | 0.2 | 90% (9/10) |

**Task 2: pick_up_the_black_bowl_next_to_the_ramekin...** (仅 obs_only 完成)

| Experiment | Norm | SR |
|---|---|---|
| obs_only | 0.05 | 90% (9/10) |
| obs_only | 0.2 | 100% (10/10) |

perdof 的 4 个实验 Task 2 均在 rollout 5/10，中途成功率 1/5 ~ 5/5 不等。

### 关键观察
- obs_only 模式明显领先 perdof（前 2 个 task 均高 20-30%）
- obs_only norm=0.2 目前表现最强（90% + 100%）
- perdof 模式 norm 对 Task 1 影响不大（50-70%），norm=0.3 反而稍好
- 按当前速度（~1.5h 完成 1-2 tasks），预计全部完成还需 **~10-12 小时**

---
