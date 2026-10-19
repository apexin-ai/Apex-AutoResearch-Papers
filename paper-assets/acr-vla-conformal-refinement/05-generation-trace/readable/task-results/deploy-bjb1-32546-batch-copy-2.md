# deploy bjb1 32546 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-batch_20260528T045928_result.json`
- **Structured JSON:** [`6fd41117a7532c9f01e4.json`](../../sessions/6f/6fd41117a7532c9f01e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动正常，模型正在加载。

## 部署结果

| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-ksweep-k20-obs-obj-s43 | cuda:5 | 558349 | RUNNING，模型加载中 |

**未部署的 5 个实验**（cuda:0-4 被占用，C001 约束禁止提交）：

| 计划 GPU | exp_id | 原因 |
|----------|--------|------|
| cuda:0 | eval-random-select-obj-s42 | 被 pi05 adaptive_conformal_crm goal s43 占用 (12612 MiB) |
| cuda:1 | eval-random-select-obj-s43 | 被 pi05 adaptive_conformal_crm goal s44 占用 (12612 MiB) |
| cuda:2 | eval-random-select-obj-s44 | 被 pi05 adaptive_conformal_crm object s44 占用 (12229 MiB) |
| cuda:3 | eval-ksweep-k5-obs-obj-s42 | 被 smolvla random_selection object s43 占用 (5693 MiB) |
| cuda:4 | eval-ksweep-k20-obs-obj-s42 | 被 smolvla crm_obs_only K=20 norm0.2 object s44 占用 (5869 MiB) |

注意：cuda:3 上正在跑的 `random_selection object s43` 和计划中 cuda:1 的 `eval-random-select-obj-s43` 可能有重叠，待其完成后确认是否需要重跑。等现有实验结束后可补提交剩余 5 个。

---
