# analysis bstar rho comparison

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bstar-rho-comparison_20260516T142302_result.json`
- **Structured JSON:** [`013de8904c742f6537fc.json`](../../sessions/01/013de8904c742f6537fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 artifact 已注册。

## 分析结论

**Figure 1 — b* 分布**：ρ=0.6 的 b* 分布明显右移，中位数 0.860 vs ρ=0.4 的 0.069（偏移 +0.791）。ρ=0.4 高度集中在接近 0 的位置（多数 batch 几乎不需要 reweighting），而 ρ=0.6 分布更宽且峰值在 ~0.5。这直接验证了方法能根据污染水平自动调整 reweighting 强度。

**Figure 2 — α_eff binding rate**：ρ=0.4 的 binding rate（69.0%）远高于 ρ=0.6（34.3%）。解释：低污染时大部分 batch 是干净的，算法充分信任这些 batch → α_eff 频繁触顶（0.8）；高污染时更多 batch 含噪声 → 算法更谨慎 → α_eff 较少触顶。

| 指标 | ρ=0.4 | ρ=0.6 |
|------|-------|-------|
| N | 51,913 | 24,412 |
| b* median | 0.069 | 0.860 |
| b* mean | 0.714 | 1.384 |
| α_eff binding rate | 69.0% | 34.3% |

---
