# analysis eval pi05 l2norm k085 object seed42 v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k085_object_seed42_v4_20260522T014005_result.json`
- **Structured JSON:** [`472a5fb869a9df35fd83.json`](../../sessions/47/472a5fb869a9df35fd83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果总结

**π0.5 L2norm k=0.85 Object: SR = 98.0% (490/500)**

### Per-task 分布

| Task | SR |
|---|---|
| T0 alphabet_soup | 100% |
| T1 cream_cheese | 100% |
| T2 salad_dressing | 98% |
| T3 bbq_sauce | 98% |
| T4 ketchup | 98% |
| T5 tomato_sauce | 98% |
| T6 butter | 100% |
| T7 milk | **88%** |
| T8 chocolate_pudding | 100% |
| T9 orange_juice | 100% |

T7 (milk) 是唯一明显低的 task，其余均 ≥ 98%。

### L2norm Object 降解曲线（完整）

| k | SR | Δ from baseline |
|---|---|---|
| 1.0 (baseline) | 97.0% | — |
| 0.925 | 99.2% | +2.2 |
| **0.9** | **98.2%** | +1.2 |
| **0.85** | **98.0%** | +1.0 |
| 0.7 | 55.0% | -42.0 |
| 0.5 | 33.4% | -63.6 |
| 0.3 | 51.0% | -46.0 |
| 0.1 | 2.6% | -94.4 |

### 结论

k=0.85 (98.0%) 与 k=0.9 (98.2%) 几乎无差别，确认 **L2norm 在 k=0.85~0.925 区间有一个稳定的高性能平台**（均 ≥ 98%），然后在 k=0.85 → 0.7 之间发生剧烈崩塌（98% → 55%）。这不是渐进退化，而是一个明确的 **cliff edge 在 k ∈ [0.7, 0.85) 之间**。下一步可考虑测 k=0.8 或 k=0.75 以精确定位 cliff 位置。

---
