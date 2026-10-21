# check all running eta

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-running-eta_20260528T105429_result.json`
- **Structured JSON:** [`a4df4e23c7ed29802296.json`](../../sessions/a4/a4df4e23c7ed29802296.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`detach_ln_v2_s2_eval` 的日志内容不是训练进度，看起来是 eval 输出。其余 4 个结果如下：

| exp_id | server | step/total | speed | 剩余时间 | 1h内完成? |
|--------|--------|------------|-------|----------|----------|
| detach_ln_v2_s4 | westd-10894 | 44519/50005 (89%) | 1.07 it/s | ~1h25m | **NO** |
| vanilla_object_s2 | westd-10894 | 20757/50005 (41%) | 1.10 it/s | ~7h24m | **NO** |
| full_occ_bn_v2_s3 | westd-10894 | 20711/50005 (41%) | 1.09 it/s | ~7h28m | **NO** |
| full_occ_bn_v2_s2 | westd-34685 | 23400/50005 (47%) | 1.09 it/s | ~6h47m | **NO** |
| detach_ln_v2_s2_eval | westd-34685 | — | — | 日志非进度条格式 | **不确定** |

**结论：没有任何实验能在 12:00 UTC 前完成。** `detach_ln_v2_s4` 最接近，还需约 1.5h。其余三个训练实验都只到 41-47%，还需 7h 左右。

---
