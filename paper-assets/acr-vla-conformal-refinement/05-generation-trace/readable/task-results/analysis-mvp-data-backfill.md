# analysis mvp data backfill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-data-backfill_20260513T220508_result.json`
- **Structured JSON:** [`3dc5f596cbe76c971cba.json`](../../sessions/3d/3dc5f596cbe76c971cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

**汇总：**

- **数据源文件**: `artifacts/mvp-point-reaching/data/mvp_results.log`
- **Registry 条目**: `mvp-point-reaching` (status: DONE, conclusion: success)
- **论文引用验证** (均来自 Group 4, K=10)：

| 论文引用 | 实际计算 | 来源 |
|---------|---------|------|
| "6.7% over scalar" | (0.078799−0.073478)/0.078799 = **6.75%** | B vs A total MSE |
| "16.7% over no uncertainty" | (0.088223−0.073478)/0.088223 = **16.71%** | B vs C total MSE |
| "22-24% improvements" | y: **22.79%**, z: **23.90%** | B vs A per-axis MSE |

已将 `summary_pct_improvements` 字段（含改进百分比和 paper claims 溯源公式）补录到 registry metrics 中。

---
