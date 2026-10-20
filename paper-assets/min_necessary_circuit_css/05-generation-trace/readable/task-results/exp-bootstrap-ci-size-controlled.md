# exp bootstrap ci size controlled

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bootstrap_ci_size_controlled_20260513T160804_result.json`
- **Structured JSON:** [`1e025cb02f790cfab588.json`](../../sessions/1e/1e025cb02f790cfab588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报结果：

## Bootstrap CI 结果（Size-Controlled, N=16 edges, 1000 bootstrap）

**结论：negative — CSS=1.0 在控制电路大小后无统计显著优势。**

### Zero Ablation

| 比较 | Delta | 95% CI | p-value | 显著 |
|------|-------|--------|---------|------|
| CSS vs EAP-IG | +0.088 | [-0.066, +0.267] | 0.112 | No |
| CSS vs EP | +0.039 | [-0.079, +0.147] | 0.249 | No |
| CSS vs ACDC | 0.000 | [0, 0] | 1.000 | No |

### Mean Ablation

| 比较 | Delta | 95% CI | p-value | 显著 |
|------|-------|--------|---------|------|
| CSS vs EAP-IG | -0.005 | [-0.039, +0.023] | 0.359 | No |
| CSS vs EP | -0.006 | [-0.032, +0.014] | 0.279 | No |
| CSS vs ACDC | 0.000 | [0, 0] | 1.000 | No |

关键发现：
- CSS=1.0 的 16 条边与 ACDC top-16 完全相同（delta=0），说明 CSS=1.0 intersection 恰好是 ACDC 贡献的边集
- Zero ablation 下 CSS 方向正确（正 delta），但 CI 跨零，不显著
- Mean ablation 下 CSS 反而略逊于 EAP-IG/EP，也不显著

---
