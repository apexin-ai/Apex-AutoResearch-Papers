# analysis eval plan 014 no evidence r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_014_no_evidence_r2_20260516T041929_result.json`
- **Structured JSON:** [`569ea3333cfa5de86c1b.json`](../../sessions/56/569ea3333cfa5de86c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## eval_plan_014_no_evidence_r2 结果

| 指标 | 值 |
|------|-----|
| **Rel-F1** | **0.4876** |
| **Ign-F1** | **0.4721** |
| Evi-F1 | 0.0000 |
| EDCR | 0.0000 |
| Evi-F1-Joint | 0.0000 |
| Precision | 0.4901 |
| Recall | 0.4851 |
| Format OK | 978/985 (99.3%) |
| Truncated | 307/985 (31.2%) |
| Predictions | 21,181 |
| 推理耗时 | 6251.6s (~1h44m) |

符合预期：no-evidence baseline 只预测关系不输出证据，所以 Evi-F1 / EDCR / Evi-F1-Joint 均为 0。Rel-F1 48.76%、Ign-F1 47.21% 作为 Qwen3-4B + SFT no-evidence adapter 的 baseline 数值已记录。

---
