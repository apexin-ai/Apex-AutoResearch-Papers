# analysis w6 mistral docred unconstrained metrics v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w6_mistral_docred_unconstrained_metrics_v2_20260516T085747_result.json`
- **Structured JSON:** [`5e874eae9eab662b7541.json`](../../sessions/5e/5e874eae9eab662b7541.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 写入成功。

## w6_mistral_docred_unconstrained 完整 Metrics

| 指标 | 值 |
|------|-----|
| total_samples | 998 |
| parse_failures | 7 |
| parse_fail_rate | 0.70% |
| total_pred_entities | 12,580 |
| total_pred_relations | 11,879 |
| **ET_pct** | **7.58%** |
| **RV_pct** | **42.35%** |
| **DR_pct** | **57.42%** |
| **CF_pct** | **24.78%** |
| E_P | 0.6221 |
| E_R | 0.3975 |
| **E_F1** | **0.4851** |
| R_P | 0.0355 |
| R_R | 0.0346 |
| **R_F1** | **0.0350** |

关键发现：Mistral 在 DocRED 上 unconstrained 模式下 relation F1 极低（3.5%），RV 违规率 42.35%（大量生成不在 ontology 中的关系名），DR 违规率 57.42%（即使关系名匹配了，head/tail type pair 仍有过半不满足约束）。Entity F1 尚可（48.5%）。

---
