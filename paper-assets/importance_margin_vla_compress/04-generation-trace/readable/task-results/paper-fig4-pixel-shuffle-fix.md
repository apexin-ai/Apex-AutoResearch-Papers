# paper fig4 pixel shuffle fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig4_pixel_shuffle_fix_20260528T134353_result.json`
- **Structured JSON:** [`abe536d5ab3e7e27996d.json`](../../sessions/ab/abe536d5ab3e7e27996d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件：**
- PDF: `docs/paper/figures/paper/fig_pixel_shuffle.pdf` (34KB)
- PNG: `docs/paper/figures/paper/fig_pixel_shuffle.png` (45KB)
- Artifact 副本: `artifacts/_project/chart/fig_pixel_shuffle.pdf`
- Gen script: `docs/paper/figures/paper/gen_fig_pixel_shuffle.py`

**设计要点：**
- 居中布局，左右对称 margin
- 4 色系（蓝/橙/绿/紫）按行分组，grid 和 stacked token 颜色一一对应
- Stacked token 有 4 组间隙，视觉上体现 4 行 × 4 片结构
- 底部用灰色 mini-grid + 红色 X + 虚线边框展示 "token 去除 = 整个 4×4 receptive field 丢失"
- Liberation Serif 字体，pdf.fonttype=42 矢量嵌入

---
