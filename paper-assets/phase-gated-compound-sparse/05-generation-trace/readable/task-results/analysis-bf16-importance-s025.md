# analysis bf16 importance s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_importance_s025_20260514T062118_result.json`
- **Structured JSON:** [`87c5be604cb12d5d7c95.json`](../../sessions/87/87c5be604cb12d5d7c95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## bf16_importance_s025 结果摘要

| 指标 | high_sparsity | mid_sparsity | low_sparsity |
|------|:---:|:---:|:---:|
| II mean | 0.3028 | 5.7297 | 25.8530 |
| II median | 0.0324 | 1.1181 | 7.1960 |
| II 95% CI | [0.084, 0.544] | [3.456, 8.472] | [19.077, 33.497] |
| II winsorized mean | 0.2010 | 4.1899 | 19.3191 |
| PPL (dense) | 1.169 | 1.227 | 1.229 |
| PPL (both sparse) | 2.703 | 13.344 | 63.668 |
| Segments | 387 | 191 | 397 |
| Tokens | 21086 | 13306 | 27748 |

**Gradient (low/high)**: 85.4x

**per_problem_ii**: 50 problems，0 NaN，11 null（10 个 `ii_mid` + 1 个 `ii_high`，均因该 problem 对应 phase 的 segments=0，正常行为）。

**Verdict**: PASS — low vs mid CI 不重叠。s=0.25 在 bf16 下 importance masking 的 interaction index 呈现清晰的单调梯度：high phase 几乎不受影响（II≈0.3），low phase 剧烈退化（II≈25.9），确认 importance-based masking 在该稀疏度下有效区分了关键/非关键 attention heads。

---
