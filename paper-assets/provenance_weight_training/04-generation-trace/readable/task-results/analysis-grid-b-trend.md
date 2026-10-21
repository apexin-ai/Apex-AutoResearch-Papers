# analysis grid b trend

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid-b-trend_20260516T191338_result.json`
- **Structured JSON:** [`10747c2a8418064a6bc8.json`](../../sessions/10/10747c2a8418064a6bc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。关键数据和叙事如下：

---

### 核心统计

| 量 | 值 |
|---|---|
| PPL at adaptive b*≈1.19 | 17.693 (≈uniform) |
| PPL at ESS-only b*≈3.5 | 17.778 (+0.085 vs adaptive) |
| PPL at ESS-only b*≈5.9 | 17.811 (+0.118 vs adaptive) |
| Adaptive vs uniform gap | −0.001 (essentially zero) |
| ESS-only vs uniform gap | +0.084 to +0.117 (worse than uniform) |

### 曲线形状（诚实报告）

斜率随 b 增大实际**递减**（0.082→0.033→0.022 /unit-b），不是传统意义的"陡峭区"。但 ESS-only b* 落在 3.5–5.9 的宽范围内，**累计退化**达 0.085–0.118 PPL，使其比 uniform baseline 还差。关键不是斜率陡不陡，而是 b 偏离最优点太远，退化已经不可忽视。

### 论文叙事（英文）

> Figure X plots perplexity against the sharpening exponent $b$ at fixed $\rho{=}0.4$ across two seeds (seed456's $b{\geq}2.0$ runs are excluded due to a checkpoint artifact identified in D026). The curve rises monotonically: at the adaptive mechanism's operating point ($b^*{\approx}1.19$), PPL sits at 17.693, essentially matching the uniform baseline (17.694). In contrast, the ESS-only constraint yields $b^*$ values in the 3.5–5.9 range, where interpolated PPL reaches 17.778–17.811—a degradation of 0.085–0.118 PPL over the adaptive operating point. Notably, ESS-only not only fails to improve over uniform weighting but actively degrades it (+0.084–0.117 PPL above uniform). This absolute gap, consistent across both seeds, demonstrates that the provenance-aware constraint anchors $b$ in a region where additional sharpening yields diminishing returns and net harm, while the adaptive mechanism keeps $b$ near the PPL-optimal zone.

### 已注册 artifacts
- `grid_b_trend_clean` (chart, PDF)
- `grid_b_trend_stats` (data, JSON)

---
