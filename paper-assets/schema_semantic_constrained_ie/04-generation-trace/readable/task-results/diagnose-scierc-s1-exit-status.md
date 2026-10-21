# diagnose scierc s1 exit status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scierc-s1-exit-status_20260522T064605_result.json`
- **Structured JSON:** [`9cfc07baf213d9faa43b.json`](../../sessions/9c/9cfc07baf213d9faa43b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE/success。

**结果摘要：**

| 指标 | Constrained (S1) | 假设验证 |
|------|------------------|----------|
| **R-F1** | **44.53%** | vs unconstrained 44.73% → 仅降 0.20pp，几乎无损 |
| **E-F1** | 64.76% | — |
| **DR%** | **0.0%** | 目标 DR→0% ✓ |
| **RV%** | 0.0% | ✓ |
| **ET%** | 0.0% | ✓ |
| **Parse Fail** | 0.0% | ✓ |

假设验证通过：70B LoRA + S1 constrained decoding 将所有约束违反清零，R-F1 仅从 44.73→44.53（-0.45%），确认约束有效性在 70B fine-tuned 模型上 scale-independent。

---
