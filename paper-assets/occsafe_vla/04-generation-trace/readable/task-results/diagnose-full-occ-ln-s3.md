# diagnose full occ ln s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_s3_20260525T172356_result.json`
- **Structured JSON:** [`47559f9304399f487a1a.json`](../../sessions/47/47559f9304399f487a1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练仍在运行中。当前进度 20398/50005 (41%)，已运行 ~5h52m，预计还需 ~7h40m。

关键发现：
- **进度**: step 20398/50005，未完成
- **Checkpoints**: 已保存 10K 和 20K checkpoint，无 50K
- **v2 确认**: `[AUX]` 出现 204 次，确认使用 v2 代码
- **速度**: ~1.08 it/s，稳定

**结论：训练尚未完成，仍在正常运行中。** 不更新 registry 状态，不删除 cron。预计完成时间约 8 小时后（~北京时间 5/26 14:00 左右）。

---
