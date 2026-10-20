# analysis sft eval r3 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft-eval-r3-results_20260514T165947_result.json`
- **Structured JSON:** [`1a07f31bc9779f12dab2.json`](../../sessions/1a/1a07f31bc9779f12dab2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

r3 正常完成，结果如下：

## r2 vs r3 对比

| 指标 | r2 | r3 | 差异 |
|------|------|------|------|
| **F1** | 0.4057 | 0.4057 | 0.00pp |
| **Precision** | 0.4043 | 0.4043 | 0.00pp |
| **Recall** | 0.4070 | 0.4070 | 0.00pp |
| **Evi-F1** | 0.7979 | 0.7979 | 0.00pp |
| **Evi-Precision** | 0.8035 | 0.8035 | 0.00pp |
| **Evi-Recall** | 0.7924 | 0.7924 | 0.00pp |
| **EDCR** | 0.7118 | 0.7118 | 0.00pp |
| **format_ok_rate** | 0.998 | 0.998 | 0.00pp |
| **format_compliance_rate** | 0.626 | 0.626 | 0.00pp |
| **n_parseable** | 617 | 617 (983 parseable, 617 field_complete) | 一致 |
| **n_truncated** | 367 | 367 | 一致 |
| **n_predictions** | 18815 | 18815 | 一致 |

**结论**: r2 与 r3 所有指标完全一致（差异 = 0），远低于 0.5pp 阈值。r2 的 baseline 结果完全可靠，统一 eval 代码（含 `_repair_truncated_json`）未引入任何偏差。

---
