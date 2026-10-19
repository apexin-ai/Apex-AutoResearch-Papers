# ops check bjb1 32546 cuda4 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb1-32546-cuda4-deploy_20260519T014538_result.json`
- **Structured JSON:** [`5726053a19c5d6367301.json`](../../sessions/57/5726053a19c5d6367301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个进程全部在 cuda:4 上运行，确认存活。

**部署汇报：**

| 实验 | tmux session | 状态 |
|---|---|---|
| scalar-seed46（已有） | `eval-scalar-object-seed46` | 运行中，~9h，当前在 `pick_up_the_butter` 3/10 |
| **perdof_norm005_seed45** | `eval-perdof-norm005-seed45-t16` | 已部署，PID 755612 |
| **obs_only_default_seed48** | `eval-obs-only-default-seed48-t16` | 已部署，PID 755878 |

**cuda:4 GPU 内存：14197MiB / 24564MiB (58%)，99% util**
- PID 663877 (scalar-seed46): 2856MiB
- PID 755612 (perdof-norm005-seed45): 5645MiB
- PID 755878 (obs-only-default-seed48): 5645MiB

还有 ~10GB 余量，三个进程运行稳定。scalar-seed46 尚未产出 .json 结果文件。

---
