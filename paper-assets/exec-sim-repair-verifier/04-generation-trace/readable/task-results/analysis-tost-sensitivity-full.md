# analysis tost sensitivity full

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-sensitivity-full_20260517T112801_result.json`
- **Structured JSON:** [`5f36e401e5dd6a5afe85.json`](../../sessions/5f/5f36e401e5dd6a5afe85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入 `artifacts/tost_sensitivity_full.json`。

结果摘要:

| Margin δ (pp) | TOST p-value | Equivalent (α=0.05)? |
|---|---|---|
| ±1 | 0.871 | No |
| ±2 | 0.007 | Yes |
| ±3 | <0.001 | Yes |

最小等价 margin: ±1.63 pp。±1pp 下 CLS 和 TRAJ 不可互换（差异 1.24pp 已接近 margin），±2pp 起可确认等价。LaTeX table 已嵌入 JSON 的 `latex_table` 字段。

---
