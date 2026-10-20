# analysis exp003 config3 metrics fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003_config3_metrics_fix_20260513T205942_result.json`
- **Structured JSON:** [`21273aacbb6764ecc5aa.json`](../../sessions/21/21273aacbb6764ecc5aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Config3-T07** (nucleus p=0.95, T=0.7) 完整 pairwise AUC：

| Depth Pair | AUC |
|---|---|
| 0v1 | 0.9878 |
| 1v2 | 0.6887 |
| 2v3 | 0.5902 |
| 3v4 | 0.5393 |
| 4v5 | 0.5349 |

单调递减趋势明确：depth 越深，相邻层之间的可区分度越低。

---
