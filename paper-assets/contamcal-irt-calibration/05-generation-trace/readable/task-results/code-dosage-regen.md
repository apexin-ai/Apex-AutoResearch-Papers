# code dosage regen

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dosage_regen_20260514T000800_result.json`
- **Structured JSON:** [`7a59a0d59b74469b6660.json`](../../sessions/7a/7a59a0d59b74469b6660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**dosage 文件已经包含 MMLU，无需重新生成。**

验证结果：
- 所有 dosage 文件（005/025/050/100）于 May 14 07:16 重新生成，包含 MMLU + ARC + GSM8K 三个 benchmark
- `data_meta.json` 确认：arc_challenge=1172, gsm8k=1319, mmlu=14042，总 contam=16533
- MMLU contamination labels 完整：d005=703/14042, d100=14042/14042
- d100 行数 66533 = 50000 base + 16533 contam，数学吻合

任务已完成，不需要额外操作。

---
