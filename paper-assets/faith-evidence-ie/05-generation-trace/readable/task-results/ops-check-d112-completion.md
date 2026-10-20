# ops check d112 completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_d112_completion_20260519T184025_result.json`
- **Structured JSON:** [`bca21995826fd041f7f9.json`](../../sessions/bc/bca21995826fd041f7f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**d112_rsft_no_evidence_eval_r3 已完成。** 全部 metrics：

| Metric | Value |
|--------|-------|
| **F1** | 0.5341 |
| **Ign-F1** | 0.5246 |
| Precision | 0.5338 |
| Recall | 0.5344 |
| Ign-Precision | 0.5122 |
| Ign-Recall | 0.5377 |
| Evi-F1 | 0.0000 |
| EDCR | 0.0000 |
| Format OK | 983/985 (99.8%) |
| Truncated | 144/985 |
| Predictions | 16,018 |
| Inference time | 9288s (~2h35m) |

Config 确认 `no_evidence: true`，模型 = `rsft_output_4b_sft_s44_bf16`，base = Qwen3-4B，SFT adapter = `sft_output_seed44`。

Evi-F1 和 EDCR 为 0 符合预期（no-evidence 模型不输出 evidence）。

---
