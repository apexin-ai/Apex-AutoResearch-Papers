# analyze d140 4b sft s42 no evi 2048 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d140_4b_sft_s42_no_evi_2048_fix_20260521T103142_result.json`
- **Structured JSON:** [`f0352fd5ac87c865d760.json`](../../sessions/f0/f0352fd5ac87c865d760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)。

**d140_4b_sft_s42_no_evi_2048_fix 结果汇总：**

| 指标 | 值 |
|---|---|
| **Ign-F1** | **0.4016** |
| **F1** | **0.4095** |
| Evi-F1 (DREEAM) | 0 (no-evi, 符合预期) |
| EDCR | 0 (no-evi, 符合预期) |
| Format OK | 983/985 (99.8%) |
| Truncated | 178/985 |
| Predictions | 25,638 |
| Inference time | 7606s (7.72 s/doc) |
| GPU hours | 2.82h |

Ign-F1 0.4016 在 4B 预期范围内（0.35-0.50）。Evidence tax 待配对实验 `d140_4b_sft_s42_with_evi_2048` 完成后计算。

---
