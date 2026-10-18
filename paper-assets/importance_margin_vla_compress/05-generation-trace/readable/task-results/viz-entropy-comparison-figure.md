# viz entropy comparison figure

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_entropy_comparison_figure_20260519T040642_result.json`
- **Structured JSON:** [`8242f61e602f6e11be39.json`](../../sessions/82/8242f61e602f6e11be39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成，视觉验证通过：

- **SmolVLA**（蓝色实线）：全层 flat，稳定在 0.93–0.98 区间，std 极小几乎看不到 error band
- **OpenVLA**（红色虚线）：从 0.98 急剧下降到 ~0.48，下降趋势明显，error band 清晰可见（中间层 std 最大）
- 参考线 $H_{\max}$ 在 y=1.0 处标注
- Legend 包含层数和 overall avg
- 符合所有视觉规范：serif 字体、去掉顶右 spine、浅灰 y 网格、单栏尺寸 3.5×2.5

输出路径：`docs/paper/figures/paper/fig_entropy_layers.pdf`（23.8 KB）

---
