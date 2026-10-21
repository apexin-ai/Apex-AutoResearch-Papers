# audit exp 020 data integrity

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp_020_data_integrity_20260516T150550_result.json`
- **Structured JSON:** [`61f0c46b06b69d0eb00f.json`](../../sessions/61/61f0c46b06b69d0eb00f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件最后一行均以 `"doc_id": 4999}` 正常闭合，JSON 完整。

## exp-020 数据完整性矩阵

| config \ depth | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **greedy** | 5000 | 5000 | 5000 | 5000 | 5000 | 5000 |
| **nuc09** | 5000 | 5000 | 5000 | 5000 | 5000 | 5000 |
| **t07** | 5000 | 5000 | 5000 | 5000 | 5000 | 5000 |
| **t12** | 5000 | 5000 | 5000 | 5000 | 5000 | 5000 |

**结论**：全部 24 个文件均为 5000 行，doc_id 范围 0-4999，无缺失。t07 和 t12 的 depth_5 最后一行 JSON 闭合正常，无截断。数据完整，可放心用于后续分析。

---
