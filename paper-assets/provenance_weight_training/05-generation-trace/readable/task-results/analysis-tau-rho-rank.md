# analysis tau rho rank

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau-rho-rank_20260516T191312_result.json`
- **Structured JSON:** [`9f398d10526674ec4824.json`](../../sessions/9f/9f398d10526674ec4824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三件产出全部完成并注册。核心结论：

**Rank preservation 不成立（如实报告）**：
- ρ=0.4 排序：τ=0.8 > 0.7 > 0.6
- ρ=0.6 排序：τ=0.7 > 0.6 > 0.8（τ=0.8 从第1掉到第3）
- Kendall's τ = −0.33, Spearman's ρ = −0.50（均不显著，N=3 太小）
- 3/3 共享点发生 rank swap

**但 safe range 跨 ρ 保持**：
- τ ∈ {0.6, 0.7, 0.8} 在两个 ρ 下均优于 uniform baseline
- 最优 τ 从 0.8 微移到 0.7，绝对 PPL 差仅 0.01
- normalized gap 量级一致：ρ=0.4 最优 −0.233%，ρ=0.6 最优 −0.203%

**Claim 3 的准确表述应为**："τ=0.7–0.8 is optimal across tested ρ values"，而非 "τ effect is negligible" 或 "ranks are preserved"。

---
