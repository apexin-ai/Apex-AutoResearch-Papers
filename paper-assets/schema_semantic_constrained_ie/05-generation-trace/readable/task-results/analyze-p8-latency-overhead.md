# analyze p8 latency overhead

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_p8_latency_overhead_20260518T150838_result.json`
- **Structured JSON:** [`3a5be341784d2031a113.json`](../../sessions/3a/3a5be341784d2031a113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P8 Latency Overhead 结果

- 样本数: 551
- **Unconstrained**: mean=4.163s, median=4.106s, p5=1.756s, p95=7.562s, std=1.735s, total=2293.7s
- **Constrained (full_s1)**: mean=4.710s, median=4.644s, p5=2.173s, p95=8.136s, std=1.814s, total=2595.0s
- **Overhead ratio (aggregate)**: mean=1.131x, median=1.131x, p95=1.076x
- **Overhead ratio (per-doc)**: mean=1.151x, median=1.137x, p5=1.082x, p95=1.262x
- **结论**: Constrained decoding overhead 约 **13%**，远低于 2x 阈值。即使在 p95 最差情况下，per-doc overhead 也仅 1.26x。开销可忽略。

---
