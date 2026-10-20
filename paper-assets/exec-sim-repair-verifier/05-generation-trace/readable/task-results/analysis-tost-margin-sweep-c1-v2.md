# analysis tost margin sweep c1 v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-margin-sweep-c1-v2_20260519T090720_result.json`
- **Structured JSON:** [`21d8222449b8ad26113a.json`](../../sessions/21/21d8222449b8ad26113a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。验证结果：

| 检查项 | 预期 | 实际 | 状态 |
|--------|------|------|------|
| mean_diff | -0.45pp | -0.4505pp | OK |
| ±2pp p-value | ~0.007 | 0.0087 (normal approx) / 0.0071 (bootstrap ref) | OK |
| ±1.71pp p-value | ~0.021 | 0.0266 (normal approx) | OK |
| 单调递减 | yes | yes | OK |
| ±3pp p << 0.001 | yes | 4.6e-05 | OK |

Normal approximation 与 bootstrap quantile-based p 有系统性偏差（~20%），因为 bootstrap 分布非完美正态。两者结论完全一致：equivalence 在 ±1.52pp 以上成立（p<0.05）。

**产出文件（home-1x5090）：**
- `tost_margin_sweep_v2.py`
- `tost_margin_sweep_v2_results.json`

**关键数值摘要：**
- Mean diff: -0.4505pp, SE: 0.6517pp, 95% CI: [-1.71, +0.84]
- Smallest equivalence margin: **±1.52pp**
- ±2pp: p=0.0087 (normal) / 0.0071 (bootstrap), equivalent
- ±1.5pp: p=0.054, borderline non-equivalent
- ±1.71pp: p=0.027, equivalent

---
