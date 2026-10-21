# figure fig2 final three curves

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig2_final_three_curves_20260518T141047_result.json`
- **Structured JSON:** [`444490219cd0c88a830b.json`](../../sessions/44/444490219cd0c88a830b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **`degradation_curve.pdf`** 已在 `cqa1-33015:/root/autodl-tmp/importance_margin_vla_compress/docs/paper/figures/` 生成（30KB）
- **三条曲线**：
  - **OpenVLA (MLP proj., 7B)** — 蓝色实线 + 方块，4 个数据点，渐进下降 74→20.6%
  - **SmolVLA (official, 0.5B)** — 橙色虚线 + 三角，2 个数据点，59.2% → 0%
  - **SmolVLA (ours, 0.5B)** — 红色实线 + 圆点，6 个数据点，44.8% → 0%（仅移除 5% token 即崩溃）
- 本地 `gen_figures.py` 也已同步更新，添加了 `ORANGE` 颜色和第三条曲线

---
