# viz beta steering table

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_beta_steering_table_20260522T154749_result.json`
- **Structured JSON:** [`5e8bd82e78e83735749d.json`](../../sessions/5e/5e8bd82e78e83735749d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已写入 `artifacts/table_steering_full.tex`，可直接 `\input{sections/appendix}` 中追加 `\input{../artifacts/table_steering_full}` 引用。

结构：
- 8 行（β = 0, 0.5, 1, 2, 3, 4, 5, 10），缺失值用 `---`
- 3 组列：N=5 Gen / N=50 Gen（含 ±std）/ N=200 TF
- β=5 行全部加粗
- β=2 与 β=3 之间用 `\addlinespace[3pt]` 标记 phase transition 边界
- caption 说明加粗含义和 phase transition 位置

---
