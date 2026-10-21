# ops d066 llama docred beam1 unc eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d066_llama_docred_beam1_unc_eval_20260520T141241_result.json`
- **Structured JSON:** [`5d13e392f1ce123f1744.json`](../../sessions/5d/5d13e392f1ce123f1744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Llama DocRED beam1 unconstrained 评估结果

| 指标 | 值 |
|------|-----|
| **E-F1** | 85.29 (P=85.96, R=84.62) |
| **R-F1** | 47.28 (P=43.55, R=51.72) |
| **DR%** | 0.30 |
| **CF%** | 0.19 |
| **PF%** | 2.0% |
| ET% | 0.00 |
| RV% | 0.36 |

200 samples, 3724 entities predicted, 3050 relations predicted. 实体抽取表现不错（F1 85.29），关系抽取偏弱（F1 47.28），precision 低于 recall 约8个点。Parse failure 率很低（2%）。

---
