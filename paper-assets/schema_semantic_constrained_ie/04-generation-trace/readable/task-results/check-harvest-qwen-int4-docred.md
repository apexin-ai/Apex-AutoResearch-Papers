# check harvest qwen int4 docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-qwen-int4-docred_20260523T075546_result.json`
- **Structured JSON:** [`be1b6934f183197293e3.json`](../../sessions/be/be1b6934f183197293e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不在当前 session，可能已在之前的 session 中清理。Registry 已更新为 DONE。

## sf2_qwen_int4_docred_s1 完整指标

| 指标 | 值 |
|------|-----|
| **DR%** | 0.00 |
| **RV%** | 0.00 |
| **ET%** | 0.00 |
| **CF%** | 0.10 (3 violations) |
| **R-F1** | 40.07 |
| **R-P** | 41.59 |
| **R-R** | 38.65 |
| **E-F1** | 74.84 |
| **E-P** | 84.87 |
| **E-R** | 66.93 |
| **#pred_entities** | 2,985 |
| **#pred_relations** | 2,385 |
| **parse_fail_pct** | 18.5% (37/200) |

约束执行近乎完美（DR/RV/ET=0%，CF 仅 0.1%）。18.5% parse fail 是超时导致（94s timeout，均为 E=0 R=0 的 FAIL），这些 FAIL 样本拉低了 recall。

---
