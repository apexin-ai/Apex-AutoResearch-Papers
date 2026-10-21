# figure fig2 degradation curve v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2_degradation_curve_v5_20260519T005817_result.json`
- **Structured JSON:** [`9954696b22a1df529b40.json`](../../sessions/99/9954696b22a1df529b40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 确认正确：OpenVLA 蓝色曲线有 6 个数据点（0.0, 0.05, 0.1, 0.3, 0.5, 0.7），呈现平滑的 graded degradation。

**修改内容**：`gen_figures.py` 第 40-41 行，OpenVLA 数据从 4 点扩展到 6 点：
```python
# 旧
ox = [0.0, 0.3, 0.5, 0.7]
oy = [74.0, 49.0, 37.4, 20.6]
# 新
ox = [0.0, 0.05, 0.1, 0.3, 0.5, 0.7]
oy = [74.0, 69.4, 62.0, 49.0, 37.4, 20.6]
```

**输出文件**：
- `docs/paper/figures/degradation_curve.pdf` (30.5 KB)
- `docs/paper/figures/paper/fig_degradation_curve.pdf`（已复制，供论文 .tex 引用）

---
