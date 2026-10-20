# analysis recency s015 per phase

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recency_s015_per_phase_20260516T231612_result.json`
- **Structured JSON:** [`3906d20bad547cdcc28c.json`](../../sessions/39/3906d20bad547cdcc28c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

```
=== Recency s015 Per-Phase II (n_problems=100) ===

Segment-level aggregates (from profiling_results.json):
  high_sparsity: mean=-0.096374, median= 0.000097  CI=[-0.000609, 0.000523]
  mid_sparsity:  mean=-72.1816,  median=-0.011459  CI=[-0.015675, -0.007871]
  low_sparsity:  mean=-1062.64,  median=-0.013419  CI=[-0.019612, -0.007795]

Per-problem level:
  high: median=-0.007317
  mid:  median=-0.012580
  low:  median=-0.016682
  low/high ratio (median): 2.28
  low/high ratio bootstrap 95% CI: [-0.11, 6.67]  ← includes 1

Gradient test (median of per-problem low−high):
  median_diff = -0.002577
  95% CI: [-0.0238, +0.0047]  ← includes 0

=== Importance s015 Per-Phase II (n=500 reference) ===

Segment-level aggregates:
  high_sparsity: mean=-0.137396, median=0.006531  CI=[0.005469, 0.007701]
  mid_sparsity:  mean= 0.293752, median=0.081439  CI=[0.072508, 0.093776]
  low_sparsity:  mean= 1.409599, median=0.397319  CI=[0.370514, 0.425770]

Per-problem level:
  high: median=0.002946
  mid:  median=0.074222
  low:  median=0.352830
  low/high ratio (median): 119.77

Gradient test (median of per-problem low−high):
  median_diff = 0.390717
  95% CI: [0.3496, 0.4434]  ← excludes 0

=== 比较 ===

Recency gradient:  无. ratio=2.28, CI=[-0.11, 6.67] 包含 1; diff CI 包含 0
Importance gradient: 有. ratio=119.8, diff CI 完全 >0
差异倍数: importance/recency gradient = 0.391/0.003 ≈ 152×
方向差异: importance 各相位 II 单调递增 (high→low: 0.003→0.074→0.353, 正值)
          recency 各相位 II 全部 ≤0 (0.000→-0.011→-0.013), 无有益分配效应
```

**结论**: Recency 在 s=0.15 下无 phase gradient。所有相位 II 为负或零，CI 包含无差异假设。Importance 方法的梯度强度是 recency 的 ~152 倍，且方向正确（保留重要段获得正向交互增益）。Recency-based allocation 在该稀疏度下不优于 uniform eviction。

---
