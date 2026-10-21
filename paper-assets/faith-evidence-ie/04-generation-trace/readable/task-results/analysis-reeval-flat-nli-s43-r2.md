# analysis reeval flat nli s43 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_flat_nli_s43_r2_20260516T060849_result.json`
- **Structured JSON:** [`1c0ff9f1f18856fc9b33.json`](../../sessions/1c/1c0ff9f1f18856fc9b33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE + success。总结：

## reeval_flat_nli_s43_r2 结果

| 指标 | r2 (bs=4, 统一协议) | r1 (bs=16) | Δ |
|------|---------------------|------------|---|
| **rel_f1** | **0.4586** | 0.4523 | **+0.63pp** |
| ign_f1 | 0.4503 | 0.4523 | -0.20pp |
| evi_f1 | 0.8113 | 0.8158 | -0.45pp |
| edcr | 0.6552 | 0.6505 | +0.47pp |

**结论：success。** batch_size 从 16 降到 4 后 rel_f1 不降反升 +0.63pp，在 3pp 阈值内，确认 batch_size 变化不影响结果。flat-NLI s43 与 CED s43 (rel_f1=0.4601) 在统一协议下基本持平（差 -0.15pp）。无 W&B run。GPU 时间 3.08h。

---
