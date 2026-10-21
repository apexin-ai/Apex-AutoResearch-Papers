# analysis partial anova v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_partial-anova-v2_20260526T111241_result.json`
- **Structured JSON:** [`e915eb051d3e1c4275e1.json`](../../sessions/e9/e915eb051d3e1c4275e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**Cell 1 vs Cell 3 (Gradient ON vs OFF, BN only)**
- Grad OFF (Cell 3) mean=0.757 > Grad ON (Cell 1) mean=0.700, diff=0.057
- Hedges' g = -1.023 (large effect), 但 p=0.422 (不显著, df≈1.1)
- Bootstrap 95% CI for (Cell3-Cell1): [-0.001, 0.116] — 包含零，勉强
- BF10 = 1.92 (anecdotal evidence for H1)

**One-way ANOVA (3 groups)**
- F(2,3) = 1.47, p=0.359, η²=0.495, ω²=0.135
- Vanilla n=1 导致 ANOVA 不可靠

**结论**: 效应量大但样本量太小(N=5)，统计功效极低。需要 d≈3.0+ 才能在这些 n 下达到 80% power。方向上 Detach(Grad OFF) > Full OCC(Grad ON)，与"梯度流对 BN 有害"一致，但无法排除噪声。

---
