# paper gradient figure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_gradient_figure_20260523T183457_result.json`
- **Structured JSON:** [`a3a3256eef5a5246c66f.json`](../../sessions/a3/a3a3256eef5a5246c66f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成的 2×2 论文级图表包含：

- **(a) Action Gradient Norms** — Detach（红色）梯度接近零（~0.002-0.03），其余三个条件正常（0.06-0.39），证实梯度崩溃。Random OCC 略高于 Vanilla 和 Full OCC。
- **(b) OCC Auxiliary Gradient Norms** — Full OCC 辅助梯度远大于 Random OCC（尤其 SigLIP 后层 Full OCC 达 0.23 vs Random OCC 0.07），符合预期（structured vs random targets）。
- **(c) Cosine Similarity Heatmap** — 所有层 action-aux 梯度余弦相似度接近零（-0.031 ~ +0.013），确认两组梯度近乎正交，OCC 辅助任务不干扰 action 学习。
- **(d) Gradient Collapse Ratio** — Detach/Vanilla 比率全部 < 0.13，DINOv2 中间层（D4-D12）低至 0.02，定量展示 stop-gradient 导致的视觉特征崩溃。

产出文件：`artifacts/figures/gradient_analysis_combined.pdf` + `.png`（300 DPI），已注册为 `art_20260523_a4b9c0`。

---
