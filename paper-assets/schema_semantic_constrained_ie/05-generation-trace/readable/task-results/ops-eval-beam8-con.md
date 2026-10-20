# ops eval beam8 con

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-beam8-con_20260520T035535_result.json`
- **Structured JSON:** [`287cbe8425b4ea1bfb4d.json`](../../sessions/28/287cbe8425b4ea1bfb4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval_beam8_con.json` 已生成。结果：

| 指标 | 值 |
|------|-----|
| **E-F1** | 66.36 (P=63.73, R=69.22) |
| **R-F1** | 43.65 (P=38.25, R=50.82) |
| ET% | 0.00 |
| RV% | 0.00 |
| DR% | 0.00 |
| CF% | 0.00 |
| Parse Fail | 0/551 (0%) |
| Avg Inference Time | 5.058s |
| Total Inference Time | 2786.7s |

所有 violation 指标为 0（constrained 模式下符合预期）。与 beam4 con 对比，E-F1 从 67.22 降至 66.36，R-F1 从 43.60 微升至 43.65，推理时间从 4.069s 增至 5.058s。

---
