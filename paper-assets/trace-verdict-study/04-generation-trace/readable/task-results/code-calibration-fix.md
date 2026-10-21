# code calibration fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_calibration_fix_20260515T124057_result.json`
- **Structured JSON:** [`346aeec101e06e829eb7.json`](../../sessions/34/346aeec101e06e829eb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**三个 bug 均已修复并验证：**
- **P0** (Token ID 硬编码): 改为 `resolve_token_ids()` 动态查询，Qwen 验证得到 pass=6385, fail=18403，与原值一致
- **P1** (预测方式不一致): 改为 greedy generation + `classify_prediction()`，与 evaluate.py 对齐；confidence 仍从 logits 计算
- **P2** (MCE 空 bin): `compute_mce()` 跳过空 bin，loop_only MCE 从 null → 0.1834

**Registry 已更新** (`calibration_analysis_seed42.metrics`)，artifact 已注册。服务器上结果保存在 `/root/autodl-tmp/trace-verdict-study-checkpoints/calibration/calibration_metrics_v2.json`。

---
