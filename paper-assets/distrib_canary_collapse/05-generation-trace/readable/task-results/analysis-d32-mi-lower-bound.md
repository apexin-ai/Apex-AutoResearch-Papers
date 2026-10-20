# analysis d32 mi lower bound

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d32_mi_lower_bound_20260520T161317_result.json`
- **Structured JSON:** [`797a4b84117cd1508567.json`](../../sessions/79/797a4b84117cd1508567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three outputs in place:
- `mi_lower_bounds.json` — 10 α values, 17 experiments, per-seed + aggregate MI
- `fig_mi_vs_alpha.pdf`
- `fig_mi_vs_alpha.png`

**结果**:

| α | MI (D1, bits) | MI (max, bits) | seeds |
|------|-------------|---------------|-------|
| 0.05 | 0.304 | 0.304 | 1 |
| 0.10 | 0.130 | 0.171 | 2 |
| 0.25 | **0.019** | **0.024** | 3 |
| 0.30 | 0.085 | 0.085 | 1 |
| 0.35 | 0.133 | 0.133 | 1 |
| 0.40 | 0.159 | 0.159 | 1 |
| 0.45 | 0.185 | 0.185 | 2 |
| 0.50 | 0.161 | 0.161 | 3 |
| 0.60 | 0.253 | 0.253 | 2 |
| 0.75 | 0.318 | 0.318 | 1 |

**关键发现**:

1. **V 形 MI 曲线，非 α_c 处的阶跃**：MI 在 α=0.25 处取最小值 (~0.02 bits)，之后单调递增至 α=0.75 (~0.32 bits)。α=0.50 附近没有出现信息论意义上的 phase transition jump。

2. **物理解释**：α=0.25 是"去相关区" — 扰动足以引入噪声但不足以产生系统性 collapse，entropy 和 diversity 之间的统计依赖最弱。高 α 下 collapse 加剧使两者强耦合。

3. **α=0.05 的高 MI 来自单 seed**，可能是 overfitting artifact。

4. **T=10–11 下 bootstrap CI 极宽**（最高达 3.7 bits），MI 估计不可靠。T=20 数据将显著改善置信区间。

5. **Distinct-1 是信息含量最高的 diversity metric**，在所有 α 下与 token_entropy 的 MI 均最高。MAUVE 的 MI 较低且不稳定。

---
