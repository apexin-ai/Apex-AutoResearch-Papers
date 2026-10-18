# paper figure

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_20260521T022955_result.json`
- **Structured JSON:** [`5f212f699985558a27f6.json`](../../sessions/5f/5f212f699985558a27f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 已生成并注册（`art_20260521_5a4552`）。

**结果**：
- 路径：`artifacts/figures/paper/power_curve.pdf`（44KB，矢量 PDF）
- 80% power 交叉点：Pairwise n≈54，Binarized Likert n≈172，Likert ATE n≈760
- 在 typical evaluation scale (n=100-200) 范围内，pairwise 有 97-100% power，binarized 55-85%，Likert ATE 仅 17-30%

**注意**：按给定 effect sizes 计算，binarized Likert 在 n≈172 即达 80% power，Likert ATE 在 n≈760 达到——而非 design notes 中预期的 n≈5000。如需让曲线更晚达到 80%，需调小 effect size（如 binarized p₁≈0.52 才需 n≈5000）。

---
