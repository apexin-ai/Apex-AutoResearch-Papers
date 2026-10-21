# analysis exp 018 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018_bootstrap_ci_20260516T161206_result.json`
- **Structured JSON:** [`685331526cf8e114db52.json`](../../sessions/68/685331526cf8e114db52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. 结果总结：

**exp_018 LLaMA-3.1-8B Bootstrap CI (10000 resamples)**

| Pair | AUC | 95% CI | Perm p |
|------|-----|--------|--------|
| 0v1 | 0.9224 | [0.9174, 0.9272] | <0.0001 |
| **1v2** | **0.6123** | **[0.6028, 0.6216]** | **<0.0001** |
| 2v3 | 0.5273 | [0.5169, 0.5378] | <0.0001 |
| 3v4 | 0.5168 | [0.5062, 0.5275] | 0.0037 |
| 4v5 | 0.5159 | [0.5052, 0.5268] | 0.0035 |

**关键结论：1v2 CI lower = 0.6028 > θ=0.60 → PASS。** K\*=2 对 LLaMA-3.1-8B robust，跨模型家族验证成功。所有 5 个 depth pair 的 permutation test 均显著（p < 0.004）。

---
