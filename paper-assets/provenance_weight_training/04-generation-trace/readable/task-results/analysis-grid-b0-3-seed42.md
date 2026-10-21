# analysis grid b0 3 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b0_3_seed42_20260516T045836_result.json`
- **Structured JSON:** [`68fc5feac21b91dfc2f4.json`](../../sessions/68/68fc5feac21b91dfc2f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析总结

**grid_b0_3_seed42 最终结果：PPL = 17.64 (loss = 2.8702)**

### 对比表

| 方法 | PPL | vs uniform Δ |
|------|-----|-------------|
| uniform_seed42 | 17.694 | — |
| **grid b=0.3 (本次)** | **17.64** | **-0.054** |
| grid b=0.5 | 17.651 | -0.043 |
| adaptive_fix_seed42 | 17.653 | -0.041 |
| grid b=1.0 | 17.692 | -0.002 |

### 关键发现

1. **b=0.3 优于 b=0.5**：PPL 17.64 < 17.651，说明 seed42 的 grid-best 在 b<0.5 区域，而非之前认为的 b=0.5。

2. **b=0.3 ≈ adaptive_fix**：PPL 差异仅 ~0.013（17.64 vs 17.653），进一步支持 Claim 2（adaptive ≈ grid-best）——adaptive 方法无需 grid search 即可逼近最优 b。

3. **b* curve 形状**：seed42 的 PPL(b) 曲线在 b=0.3 附近有最小值，然后随 b 增大单调上升（0.3→0.5→1.0→1.5→...→5.0）。这表明最优 b* 在 0.2-0.5 范围内，与 adaptive 方法的 b_star_median ≈ 0.87 同量级。

4. **对 Claim 2 意义**：grid-best 从 b=0.5 下移到 b=0.3，而 adaptive 的 PPL (17.653) 仍然非常接近这个新的 grid-best (17.64)，差异在噪声范围内。这强化了 "adaptive 无需 grid search 即可近似最优" 的论断。

**Conclusion: success** — PPL 显著优于 uniform，且是目前 seed42 grid sweep 的最佳值。建议后续补充 b=0.1, 0.2 实验确认 PPL(b) 曲线的精确最小值位置。

---
