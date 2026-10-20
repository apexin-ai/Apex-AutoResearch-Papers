# diagnose mvp occ s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_occ_s3_20260525T172314_result.json`
- **Structured JSON:** [`72ae5e03ff9a2214da18.json`](../../sessions/72/72ae5e03ff9a2214da18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练**仍在进行中**，未完成。

当前状态：
- 进度：step 20423/50005 (41%)，已运行 5h52m，预计还需 ~7h40m
- 速度：~1.07 it/s
- Checkpoints：已有 10K 和 20K checkpoint，50K 尚未生成
- v2 确认：[AUX] 日志出现 205 次，确认使用了 v2 代码
- 最新 [AUX] 日志：`step=20400, occ_loss=0.0127, depth_loss=0.0000, action_loss=0.1206`

**结论：训练正常运行中，不更新 registry，不删除 cron。** 预计约 7-8 小时后完成（约 UTC 05/26 13:30）。

---
