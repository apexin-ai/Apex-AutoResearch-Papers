# diagnose ablation occ detach s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ablation_occ_detach_s3_20260525T171942_result.json`
- **Structured JSON:** [`799b576fe3ac67022638.json`](../../sessions/79/799b576fe3ac67022638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练**仍在运行中**，尚未完成。

当前状态：
- **进度**: step 20376/50005 (41%)，已运行 ~5h52m
- **速度**: ~1.08 it/s
- **预计剩余**: ~7h38m
- **Checkpoints**: 10K 和 20K checkpoint 已保存，50K 尚未生成
- **v2 代码确认**: [AUX] 标志出现 204 次，确认使用的是 Detach BN v2 代码
- **无异常**: 日志正常推进，无 error/OOM

**结论**: 不满足判断条件，训练预计还需约 7.5 小时完成（约今天下午1:30左右）。不执行 registry 更新和 cron 删除操作。

---
