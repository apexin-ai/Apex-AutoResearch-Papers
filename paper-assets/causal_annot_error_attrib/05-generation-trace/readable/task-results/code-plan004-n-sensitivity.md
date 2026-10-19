# code plan004 n sensitivity

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-n-sensitivity_20260520T140512_result.json`
- **Structured JSON:** [`6835fa59c407e1ee5a0b.json`](../../sessions/68/6835fa59c407e1ee5a0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

```
=== N-Sensitivity Analysis: Mediation τ=0.05, C0=sym_mild ===

| N      | naive_power | asv_power | median_SE | median_signif_ASV |
|--------|-------------|-----------|-----------|-------------------|
|   1000 |       0.890 |     0.000 |    0.0700 |            0.0000 |
|   2000 |       0.998 |     0.000 |    0.0496 |            0.0000 |
|   5000 |       1.000 |     0.000 |    0.0313 |            0.0000 |
|  10000 |       1.000 |     1.000 |    0.0222 |              None |
|  20000 |       1.000 |     1.000 |    0.0157 |              None |
|  50000 |       1.000 |     1.000 |    0.0099 |              None |

ASV power recovers (>=80%) at N=10000
```

**关键发现**：存在尖锐的相变（N≈5000→10000），机制是 `1.96 × SE` 与 `τ=0.05` 的交叉：
- N≤5000 时，`1.96×SE ≈ 0.061 > τ=0.05`，plim 在 δ=0 就低于显著性阈值 → signif_ASV=0 → ASV 滤掉所有拒绝 → power=0%
- N≥10000 时，`1.96×SE ≈ 0.044 < τ=0.05`，plim 在整个 δ 范围内都高于阈值 → signif_ASV=None（无穷大保护）→ ASV 放行所有拒绝 → power=100%

这是一个二元开关行为，不是渐进恢复。临界 N 可解析求解：`N* ≈ (1.96×σ/τ)² × 4 ≈ 6147`（binary T 的方差校正）。

---
