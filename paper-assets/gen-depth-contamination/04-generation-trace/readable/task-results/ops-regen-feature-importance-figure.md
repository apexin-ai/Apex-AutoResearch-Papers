# ops regen feature importance figure

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_regen_feature_importance_figure_20260521T111854_result.json`
- **Structured JSON:** [`d7c212631c0fb07f5461.json`](../../sessions/d7/d7c212631c0fb07f5461.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**
- `feature_importance.pdf` (32 KB) 和 `feature_importance.png` (170 KB) 已生成到 `docs/paper/figures/`
- 两个 panel：左 Gen-0 vs Gen-1 (AUC=0.922)，右 Gen-1 vs Gen-2 (AUC=0.610)
- 15 个 features 按 ΔAUC 降序排列，含 error bars
- 0v1 top-3: Δ¹ Surprisal σ (0.209), Surprisal σ (0.095), Freq. Entropy (0.064)
- 1v2 top-3: Surprisal σ (0.058), Δ² Surprisal σ (0.022), Freq. Entropy (0.017)
- 1v2 panel 中负 importance 的 features 以红色标注（Surprisal Skew, Surprisal Kurt., Δ¹ Surprisal Skew）

---
