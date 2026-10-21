# deploy bjb1 18228 cuda2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-cuda2_20260515T100245_result.json`
- **Structured JSON:** [`574b207ad708db499979.json`](../../sessions/57/574b207ad708db499979.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:2 不空闲。**

当前 bjb1-18228 cuda:2 上有进程 PID 341878 在跑：
- 实验：`crm_obs_only spatial seed=43, norm=0.1`
- 进度：Task 0 完成 (80%)，Task 1 进行中 (5/5 success so far)
- Registry 中该实验 (`eval-obs-only-spatial-seed43`) 记录为 DONE/failed（旧 PID 341873），但实际是新进程 341878 在跑，可能是被手动重启的

无法在 cuda:2 上部署新实验。所有 4 块 GPU 状态：
| GPU | 进程 | 实验 |
|-----|------|------|
| cuda:0 | PID 325264 | eval-mag-obsonly-norm03-r2 |
| cuda:1 | PID 311886 | eval-acr-spatial-v4-scalar-r2 |
| cuda:2 | PID 341878 | obs_only spatial seed43（未正确注册） |
| cuda:3 | PID 312425 | eval-acr-spatial-v4-obs-only-r3 |

需要你确认：是要等 cuda:2 当前实验跑完再部署，还是 kill 掉它换新实验？

---
