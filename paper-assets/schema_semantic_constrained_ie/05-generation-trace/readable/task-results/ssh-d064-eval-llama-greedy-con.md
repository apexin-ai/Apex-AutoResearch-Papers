# ssh d064 eval llama greedy con

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_eval_llama_greedy_con_20260520T004046_result.json`
- **Structured JSON:** [`06bc1af767b9d08b241e.json`](../../sessions/06/06bc1af767b9d08b241e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果：

| Metric | Value |
|--------|-------|
| ET% | 0.00 |
| RV% | 0.00 |
| DR% | 0.00 |
| CF% | 0.16 |
| E-F1 | 83.40 |
| R-F1 | 44.83 |
| PF% | 5.01 |

Constrained decoding (w5) 将 ET/RV/DR 全部压到 0%，CF% 仅剩 0.16%（30 个 cross-field 冲突）。报告已写入 `artifacts/_project/report/d064_eval_llama_greedy_con.md`。

---
