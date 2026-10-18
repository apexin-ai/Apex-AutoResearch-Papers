# paper generate figures 2 3 4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_generate_figures_2_3_4_20260518T045854_result.json`
- **Structured JSON:** [`76fb3657845760d94202.json`](../../sessions/76/76fb3657845760d94202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张 PDF 已生成到本地 `docs/paper/figures/`，检查结果：

- **Figure 2 (degradation_curve.pdf)**: OpenVLA 渐进下降 vs SmolVLA 悬崖式骤降对比清晰，"Cliff-edge" 和 "Graded degradation" 标注到位
- **Figure 3 (compression_curve.pdf)**: 确认点实心/placeholder 空心区分明确，baseline 虚线和 Hard Pruning 线清楚，61.6% 标注醒目
- **Figure 4 (pixel_shuffle_viz.pdf)**: 两个颜色高亮区域的映射关系通过虚线箭头连接，左侧 32×32 → 右侧 8×8 的折叠过程直观

所有文件位于 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/`，生成脚本 `gen_figures.py` 同目录可复现。

---
