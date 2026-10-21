# ops 34685 diagnose retry eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-diagnose-retry-eval_20260527T000105_result.json`
- **Structured JSON:** [`20951c00a1f0d1f780cf.json`](../../sessions/20/20951c00a1f0d1f780cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总结：

**detach_ln_s3_eval 无需重试** — 已有成功结果。

- **失败原因**：原始提交用了错误脚本名 `safelibero_eval.py`（不存在），正确名称为 `evaluate_safelibero.py`，导致 EXIT_CODE=2
- **但已有人在 07:09 重试成功**，结果写入 `/tmp/detach_ln_s3_eval.log`
- **结果**：TSR = **0.886** (88.6%), CAR = **0.802** (80.2%)
- Registry 已更新为 conclusion=success，metrics 已写入，artifact 已注册

**cutoff_25k_s1_v2_eval 进度**（cuda:3）：Task 9, 60% (30/50 rollouts)，还在运行中。

---
