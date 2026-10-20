# analysis oracle frontier dual icc

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-frontier-dual-icc_20260518T185448_result.json`
- **Structured JSON:** [`13f9d0e630d64161d3c5.json`](../../sessions/13/13f9d0e630d64161d3c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written to `artifacts/oracle_frontier_dual_icc.md`.

核心发现（p=0.8751, CLS 8B）：

| K | ICC=0.191 (function) | ICC=0.3146 (repo) | 差值 |
|--:|----:|----:|----:|
| 1 | 87.51% | 87.51% | 0 pp |
| 3 | 92.02% | 90.44% | −1.58 pp |
| 5 | 93.65% | 91.46% | −2.19 pp |
| 7 | 94.48% | 91.97% | −2.51 pp |
| 9 | 94.98% | 92.28% | −2.70 pp |
| 11 | 95.31% | 92.48% | −2.83 pp |

Repo-level ICC=0.3146 在所有 K 下均低于 function-level ICC=0.191 约 1.6-2.8 pp，渐近上限差 3.38 pp（96.77% vs 93.39%）。注意：理论值（K=3 时 92.02%）高于论文实测的 86.83%，说明实际 seed 间相关性远高于 test-case ICC 0.191——这些值是 optimistic upper bound。

---
