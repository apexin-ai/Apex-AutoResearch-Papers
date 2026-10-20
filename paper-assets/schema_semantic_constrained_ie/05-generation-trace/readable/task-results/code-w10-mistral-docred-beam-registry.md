# code w10 mistral docred beam registry

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_mistral_docred_beam_registry_20260517T093814_result.json`
- **Structured JSON:** [`87fbfd86881ae4ef9081.json`](../../sessions/87/87fbfd86881ae4ef9081.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## Violation Checker（DocRED 版）

| 指标 | Beam (w9) | Greedy baseline (w6) |
|------|-----------|---------------------|
| ET violation | 0% | — |
| RV violation | 0% | — |
| **DR violation** | **21.37%** | 33.21% |
| CF violation | 1 | — |
| Triples | 524 | — |

**DR=21.37% 与 appendix 表格值完全一致。** Beam search 相比 greedy 降低了 11.84pp 的 domain/range 违规率。

## F1 评估

| 指标 | Beam (w9) | Greedy baseline (w6) |
|------|-----------|---------------------|
| E_F1 | 51.78 | 50.59 |
| R_F1 | 5.70 | 5.52 |

Entity F1 和 Relation F1 与 greedy 基本持平，小幅提升。

## 产出

- Violation report JSON: `outputs/w9_mistral_docred_beam4_violation_report.json`
- Violation report TXT: `outputs/w9_mistral_docred_beam4_violation_report.txt`
- Registry: `w9_mistral_docred_beam_50` 已注册，status=RUNNING → conclusion=success

---
