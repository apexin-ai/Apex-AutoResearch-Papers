# analyze exp 14b c4 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_14b_c4_bootstrap_ci_20260518T083026_result.json`
- **Structured JSON:** [`de4211a1cd31e9eb4358.json`](../../sessions/de/de4211a1cd31e9eb4358.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap CI 分析完成。关键结果：

| Pair | AUC | 95% CI | Perm p |
|------|-----|--------|--------|
| 0v1 | 0.9598 | [0.9564, 0.9630] | <0.001 |
| **1v2** | **0.6210** | **[0.6119, 0.6304]** | <0.001 |
| 2v3 | 0.5494 | [0.5392, 0.5594] | <0.001 |
| 3v4 | 0.5243 | [0.5140, 0.5346] | <0.001 |
| 4v5 | 0.5154 | [0.5045, 0.5265] | <0.001 |

**K\* = 2 统计显著确认**：
- 1v2 CI lower (0.6119) > θ (0.60) ✓
- 2v3 CI upper (0.5594) < θ (0.60) ✓

所有 pair 的 permutation test p < 0.001，均显著高于 chance。结果已保存到 `bootstrap_ci_results.json`（远程）和 `artifacts/exp_14b_c4_bootstrap_ci/results_summary.md`（本地）。

---
