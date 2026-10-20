# analysis plan 012 pearson r

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-012-pearson-r_20260514T054327_result.json`
- **Structured JSON:** [`7bfd52a96c4a096b28fd.json`](../../sessions/7b/7bfd52a96c4a096b28fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|-----|
| **Pearson r** | **0.9698** |
| **p-value** | **8.12 × 10⁻⁷** |
| **n** | **11 tasks** |

Per-task 数据点：

| Task | DR_diff (int − det) | Δ_full |
|------|---------------------|--------|
| chemistry-mix | 0.200 | 21.80 |
| find-animal | 0.250 | 26.65 |
| find-non-living-thing | 0.000 | 9.58 |
| freeze | 0.300 | 30.50 |
| grow-fruit | 0.250 | 25.10 |
| identify-life-stages-1 | 0.450 | 47.50 |
| identify-life-stages-2 | 0.300 | 30.00 |
| inclined-plane-determine-angle | 0.350 | 36.00 |
| lifespan-longest-lived | 0.400 | 44.00 |
| lifespan-longest-lived-then-shortest-lived | 0.350 | 40.80 |
| measure-melting-point-unknown-substance | 0.300 | 30.05 |

death_rate_diff 与 Δ_full 之间存在极强正相关（r = 0.97, p < 10⁻⁶）——death rate 差异越大的 task，整体性能差距也越大。

---
