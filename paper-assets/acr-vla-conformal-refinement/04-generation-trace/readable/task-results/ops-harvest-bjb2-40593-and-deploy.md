# ops harvest bjb2 40593 and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-bjb2-40593-and-deploy_20260519T004950_result.json`
- **Structured JSON:** [`ad9309241c79bea27c4f.json`](../../sessions/ad/ad9309241c79bea27c4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**scalar-seed45-r2 状态：仍在运行**
- 5/~24 tasks 完成，当前进度约 20%
- 已完成 tasks: alphabet_soup 0%, cream_cheese 0%, salad_dressing 10%, bbq_sauce 10%, ketchup 0%（running avg ~4%）
- 进程运行 ~12.8h（从 May 18 20:23 启动），CPU 141%

**GPU 状态：**
- GPU 0: 12% util, 3306/24564 MiB — 被 scalar-seed45-r2 占用（低 util 是 rollout 间隙正常现象）

**已完成 eval JSONs：**
| File | SR |
|---|---|
| eval_mag_obsonly_norm003.json | 34% |
| eval_object_obs_only.json | 19% |
| eval_object_random_selection_seed42.json | 13% |
| eval_object_vla_only_seed44.json | 10% |

**新实验：未部署。** GPU 被 scalar-seed45-r2 占用。perdof ε=0.03 seed49 待 scalar 完成后部署。

---
