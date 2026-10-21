# viz matplotlib fig1 overview v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_matplotlib_fig1_overview_v2_20260524T064825_result.json`
- **Structured JSON:** [`e59b798a14dac8233ba6.json`](../../sessions/e5/e59b798a14dac8233ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX 编译成功（37 页，无错误）。

**完成总结：**

- **脚本**：`docs/paper/figures/fig_overview.py` — 纯 matplotlib 矢量图，FancyBboxPatch 圆角框 + 阴影 + FancyArrowPatch 箭头
- **输出**：`fig_overview.pdf` + `fig_overview.png`（300dpi）已写入 `docs/paper/figures/`
- **Artifact**：已注册 `fig_overview_matplotlib_v2`
- **LaTeX**：`main.pdf` 编译通过
- **迭代**：共 3 轮——v1 修复 ✗ glyph 缺失，v2 修复 heatmap 遮挡标题，v3 调整左侧标签间距

---
