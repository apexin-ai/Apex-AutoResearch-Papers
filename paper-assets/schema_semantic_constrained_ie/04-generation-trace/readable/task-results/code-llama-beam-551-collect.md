# code llama beam 551 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_beam_551_collect_20260517T034253_result.json`
- **Structured JSON:** [`1c900a7bb7a14fc6018c.json`](../../sessions/1c/1c900a7bb7a14fc6018c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

unified_f1_eval.py 的文件路径是硬编码的 docred 文件，不接受命令行参数。violation_checker 已经输出了 Entity F1 和 Relation F1。结果已完整。

## 结果汇报

**状态: SUCCESS** (551/551 docs, 0 failures)

| 指标 | 值 |
|------|-----|
| ET% (Entity Type Violations) | 0.0% (0/2398) |
| RV% (Relation Vocab Violations) | 0.0% (0/1606) |
| DR% (Domain/Range Violations) | 0.0% (0/1606) |
| CF (Cross-field Consistency) | 15 violations |
| E_F1 | 0.2504 (P=0.2127, R=0.3042) |
| R_F1 | 0.0333 (P=0.0268, R=0.0441) |
| total_entities | 2398 |
| total_relations | 1606 |

Beam search 的约束满足率完美 (ET/RV/DR 均为 0%)，但 F1 非常低，尤其是 Relation F1 仅 3.3%。

---
