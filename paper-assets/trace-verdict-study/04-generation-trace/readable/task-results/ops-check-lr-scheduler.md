# ops check lr scheduler

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_lr_scheduler_20260515T184728_result.json`
- **Structured JSON:** [`8bc81d7c37f55f1523f1.json`](../../sessions/8b/8bc81d7c37f55f1523f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

1. **lr_scheduler_type**: 未显式设置。SFTConfig 继承自 TrainingArguments，默认值为 `"linear"`。
2. **warmup_ratio**: 显式设置为 `0.1`（第 153 行），warmup_steps 未设置。
3. **learning_rate**: `2e-4`（第 152 行）。

---
