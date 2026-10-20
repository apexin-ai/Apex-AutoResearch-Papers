# paper plan 034 figures

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_plan_034_figures_20260525T134533_result.json`
- **Structured JSON:** [`3bec05b19efa805751fa.json`](../../sessions/3b/3bec05b19efa805751fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

**图 1: ROC Curve** (`fig_roc_curve.pdf/.png`)
- 单栏宽 3.5in, 300 DPI
- AUROC = 0.990, 推荐阈值 τ=1.5 标注 (FPR=0.094, TPR=1.000)
- 路径: `artifacts/plan_034_nve_threshold/fig_roc_curve.{pdf,png}`

**图 2: Threshold vs Precision/Recall/F1** (`fig_threshold_prf.pdf/.png`)
- 4.5in 宽, 300 DPI
- Peak F1=0.941 at τ=1.5, 大钻石 marker 标注峰值
- 18 个阈值点 (0.5–3.0) 展示完整 tradeoff 曲线
- 路径: `artifacts/plan_034_nve_threshold/fig_threshold_prf.{pdf,png}`

绘图脚本: `artifacts/plan_034_nve_threshold/plot_nve_figures.py`，4 个 artifact 均已注册。

---
