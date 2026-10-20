# analysis d066 beam sweep summary

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d066-beam-sweep-summary_20260520T035505_result.json`
- **Structured JSON:** [`c926b06bf430231440bb.json`](../../sessions/c9/c926b06bf430231440bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总写入 `artifacts/d066_beam_sweep_final_summary.md`。核心结论：

**k=2 是 F1 最优点**（R-F1=44.75 unc / 44.60 con），超过 k=2 后 precision 下降抵消 recall 收益。

**Constrained decoding 以极低代价消除 DR violations**：DR 从 1.5–2.1% → 0%，R-F1 损失仅 0.15 pts（k=2），时间开销 ~17%。k=8 时 constrained 甚至反超 unc 的 R-F1（+0.48）。

**推荐配置：k=2 con** — 接近最佳 F1，零 DR 违规，仅 0.11% CF 残余（2/1798 triples），比 k=8 con 快 46%。若需绝对零违规，k=4 con 可选（代价 −1.15 R-F1）。

---
