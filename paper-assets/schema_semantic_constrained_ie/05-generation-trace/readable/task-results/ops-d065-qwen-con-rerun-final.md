# ops d065 qwen con rerun final

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d065_qwen_con_rerun_final_20260520T161012_result.json`
- **Structured JSON:** [`ea914d40436a45d7dde4.json`](../../sessions/ea/ea914d40436a45d7dde4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。d065 Qwen DocRED constrained rerun eval 结果：

| 指标 | 值 |
|------|-----|
| **E-F1** | 81.87 (P=85.50, R=78.53) |
| **R-F1** | 40.79 (P=36.34, R=46.50) |
| **ET%** | **0.00** |
| **RV%** | **0.00** |
| **DR%** | **0.00** |
| **CF%** | 0.22 |
| **PF%** | 7.8% (78/998) |

**关键结论：DR% = 0%**。Constrained decoding 在 Qwen + DocRED 上完全消除了 domain-range 违规（ET、RV、DR 全部归零）。Table 2 措辞可以用 **"eliminates"**，不需要 "near-eliminates" 的让步。

Registry 已更新（conclusion=success + 完整 metrics），cron 已删除。

---
