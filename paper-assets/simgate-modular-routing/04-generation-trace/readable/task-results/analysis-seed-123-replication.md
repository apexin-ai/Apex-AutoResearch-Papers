# analysis seed 123 replication

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed-123-replication_20260518T111231_result.json`
- **Structured JSON:** [`8ee4982c6b9f968e0f9f.json`](../../sessions/8e/8ee4982c6b9f968e0f9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**conclusion = SUCCESS**

核心对比：

| 指标 | Seed=42 | Seed=123 | 差异 |
|------|---------|----------|------|
| **DAF** | 90.41% | 89.68% | **-0.73pp** (< 5pp) |
| death_rate_int | 42.9% | 45.45% | +2.55pp |
| death_rate_det | 16.3% | 20.91% | +4.61pp |
| delta_full | 29.6 | 27.47 | -2.13 |
| delta_nd | 2.84 | 2.83 | -0.01 |
| pearson_r | 0.9698 | 0.9412 | -0.029 |

DAF 差异仅 0.73pp，方向一致，seed robustness 确认。所有核心结论均复现：10/11 tasks 的 DAF >= 81%，death dominance 是 routing preference 的主要驱动力，delta_nd 近乎为零。

报告已写入 `artifacts/seed-123-replication/analysis_report.md` 并注册。

---
