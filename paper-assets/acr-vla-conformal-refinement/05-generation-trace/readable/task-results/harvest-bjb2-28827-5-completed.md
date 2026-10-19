# harvest bjb2 28827 5 completed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-5-completed_20260520T142432_result.json`
- **Structured JSON:** [`4bd782760b76ed3d3bce.json`](../../sessions/4b/4bd782760b76ed3d3bce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 10 次 registry 更新成功。5 个实验均已标记为 DONE/success。

| exp_id | SR | conclusion | registry 更新 |
|--------|-----|------------|--------------|
| eval-obs-only-spatial-norm02-seed46-r2 | **0.33** | success | OK |
| eval-vla-only-goal-seed44-r2 | **0.73** | success | OK |
| eval-argmin-object-k5-seed44-r2 | **0.11** | success | OK |
| eval-perdof-object-norm02-seed48 | **0.07** | success | OK |
| eval-obs-only-object-norm005-seed43 | **0.13** | success | OK |

注意：这 5 个实验的 registry 此前已被 on_complete hook 自动标记为 DONE 并填入了 metrics/conclusion。本次更新覆盖了 log_path（指向 JSON 文件）和 metrics 字段，数据一致。

---
