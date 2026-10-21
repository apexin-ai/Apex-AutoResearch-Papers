# paper figures c1

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures_c1_20260513T234807_result.json`
- **Structured JSON:** [`76f41256319960511637.json`](../../sessions/76/76f41256319960511637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图表已生成并注册完毕。

**Fig 2 — Pairwise AUC Decay Curves** (`art_20260513_dc8c16`):
- 4 条曲线（Qwen-rewrite / Pythia-1.4B / OLMo-1B / Qwen-cont），Okabe-Ito 色觉友好配色
- Bootstrap 95% CI error bars
- θ=0.60 水平虚线 + K*=2 浅蓝阴影区域清晰标注
- Y 轴从 0.48 起截断，带断裂标记，避免 0v1 处 ~0.99 的跳跃拉平后续曲线

**Fig 3 — Cross-Model Transfer Heatmap** (`art_20260513_f170fd`):
- 4×4 方阵，YlOrRd 连续色标
- 对角线单元格加粗黑框（within-model baseline）
- Pythia↔OLMo 互迁移单元格用蓝色虚线框高亮
- 每格标注 2 位小数准确率值

输出位置：
- 远程: `/root/autodl-tmp/gen-depth-contamination/figures/fig2_auc_decay.{pdf,png}` 和 `fig3_transfer_heatmap.{pdf,png}`
- 本地 artifact 已注册到项目 manifest

---
