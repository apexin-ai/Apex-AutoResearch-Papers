# ops kill docred sampling and analyze

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_docred_sampling_and_analyze_20260516T205312_result.json`
- **Structured JSON:** [`8ac728688a2eb7b49100.json`](../../sessions/8a/8ac728688a2eb7b49100.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果总结：**

| | Sampling r3 (114 docs) | Greedy (998 docs) |
|---|---|---|
| ET | 0.00% | 0.00% |
| RV | 0.00% | 0.03% |
| DR | **10.31%** | **10.21%** |
| CF | **12.63%** | **2.57%** |
| E_F1 | 57.05 | 59.37 |
| R_F1 | 7.92 | 8.23 |

关键发现：DR 与 greedy 几乎一致（+0.1pp），确认 domain-range violations 是系统性结构问题，sampling 无法改善。CF 反而显著恶化（+10pp），因为温度采样降低了类型标注的自洽性。

---
