# ops extract plan010 metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_plan010_metrics_20260520T021928_result.json`
- **Structured JSON:** [`c339cb14c091a1af8e24.json`](../../sessions/c3/c339cb14c091a1af8e24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 指标 | 值 |
|------|-----|
| ign_f1 | 0.4533 |
| f1 (Rel-F1) | 0.4636 |
| evi_f1 (TP-only) | 0.8194 |
| evi_f1_joint | 0.3606 |
| edcr | 0.6530 |
| format_compliance_rate | 1.0 |
| n_truncated | 180 |
| precision | 0.4742 |
| recall | 0.4535 |
| ign_precision | 0.4513 |
| ign_recall | 0.4552 |
| evi_precision | 0.8090 |
| evi_recall | 0.8301 |
| evi_joint_precision | 0.3563 |
| evi_joint_recall | 0.3650 |
| field_compliance_rate | 0.8051 |
| evidence_format_rate | 0.8051 |
| n_total | 985 |
| n_parseable | 985 |
| n_predictions | 14870 |
| n_documents | 985 |
| tp | 5511 |
| pred_count | 11622 |
| gold_count | 12151 |
| evi_tp | 7031 |
| evi_pred_total | 19736 |
| evi_gold_total | 19261 |
| n_distractor_citations | 16422 |
| n_total_citations | 25150 |
| inference_time_seconds | 10064.2 |

模型：Qwen3-4B + SFT + RSFT-NLI-Large，dev split，no_evidence=false。

---
