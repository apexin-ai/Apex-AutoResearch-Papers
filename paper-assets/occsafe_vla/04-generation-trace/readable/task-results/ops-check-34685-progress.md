# ops check 34685 progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-34685-progress_20260526T111459_result.json`
- **Structured JSON:** [`1de6a691904005d8859f.json`](../../sessions/1d/1de6a691904005d8859f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 34685 训练进度报告

| 实验 | 当前 step | 进度 | step/s | 已运行 | 预计剩余 |
|------|----------|------|--------|--------|---------|
| vanilla_v2_s1 | 8535/50005 | 17% | **1.08 it/s** | 2h29m | ~10.7h |
| vanilla_v2_s2 | 8576/50005 | 17% | **1.09 it/s** | 2h29m | ~10.6h |
| detach_ln_s3 | 8532/50005 | 17% | **1.09 it/s** | 2h29m | ~10.6h |
| cutoff_25k_s1_v2 | 7133/50005 | 14% | **1.08 it/s** | 2h05m | ~11.0h |

**结论：IO 危机未发生。** 4 个实验当前速度均为 1.05-1.09 it/s，**高于**正常预期的 0.7-0.9 it/s，无任何减速迹象。GPU 利用率 85-99%，显存各占 ~62GB。

**不建议迁移。** 按当前速度，4 个实验预计今晚（约 10-11 小时后）全部完成。detach_ln_s3 日志中有少数偶发的短暂抖动（个别 step 降到 1.01 it/s），但很快恢复，不影响整体。

---
