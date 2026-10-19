# deploy bjb1 18228 cuda0 reuse

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-cuda0-reuse_20260515T172721_result.json`
- **Structured JSON:** [`44c8a1a80088b30d9bd6.json`](../../sessions/44/44c8a1a80088b30d9bd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 确认空闲。** GPU-79a1ce73 无进程占用。cuda:1/2/3 分别跑着 perdof-seed43、obs-only-seed43、argmin-seed43。

perdof checkpoint 也存在（1.3MB）。

但两个候选实验都已在跑：
- `eval-mag-perdof-norm003-object` → bjb2-28827 cuda:0 (RUNNING)
- `eval-mag-perdof-norm02-object` → bjb1-32546 cuda:5 (RUNNING)

object magnitude sweep 的 perdof 全部 norm 点都已覆盖：
| norm | server | status |
|------|--------|--------|
| 0.03 | bjb2-28827 | RUNNING |
| 0.05 | bjb2-28827 | RUNNING |
| 0.1 (default) | bjb2-28827 | RUNNING |
| 0.2 | bjb1-32546 | RUNNING |
| 0.3 | bjb2-28827 | RUNNING |

cuda:0 空闲但没有未部署的 object magnitude sweep 实验可以放上去。需要你指定新的部署任务。

---
