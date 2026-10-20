# analysis cwm8b seed456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cwm8b-seed456_20260512T145931_result.json`
- **Structured JSON:** [`917c7c4afef89338a8aa.json`](../../sessions/91/917c7c4afef89338a8aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

**cwm8b-seed456 结果**

| 指标 | seed456 | seed42 | seed123 |
|------|---------|--------|---------|
| accuracy | 86.24 | 87.67 | 86.98 |
| pass_f1 | 85.96 | 87.57 | 86.83 |
| fail_f1 | 86.51 | 87.77 | 87.13 |
| exact_match | 82.8% | — | — |
| train_loss | 0.2279 | — | — |

seed456 略低于前两个 seed（约 -1pp），但在正常 seed 方差范围内。3 seeds 均值：accuracy 86.96, pass_f1 86.79, fail_f1 87.14。

MVP-B criteria 全部通过。status=DONE, conclusion=success。

---
