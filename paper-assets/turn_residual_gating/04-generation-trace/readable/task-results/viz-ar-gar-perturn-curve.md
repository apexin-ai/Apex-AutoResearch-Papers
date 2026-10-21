# viz ar gar perturn curve

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_ar_gar_perturn_curve_20260522T152826_result.json`
- **Structured JSON:** [`3093bdb94442102f92e1.json`](../../sessions/30/3093bdb94442102f92e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件** (westd-20861):
- `/root/turn_residual_gating/artifacts/fig_ar_gar_perturn.pdf` (22K)
- `/root/turn_residual_gating/artifacts/fig_ar_gar_perturn.png` (132K)

**图表内容**:
- 3 条曲线，X 轴 Turn 1-10，Y 轴 GAR (%)
  - **Qwen-2.5-7B Base** (实线蓝圆点): 4.18% → 0.64%，**下降 85%**
  - **Llama-3.1-8B Base** (实线橙方点): 2.63% → 0.26%，**下降 90%**
  - **Qwen-2.5-7B + TG (AR)** (虚线蓝空心): 5.22% → 1.45%，TG 训练后 AR 推理仍衰减
- Okabe-Ito 色盲友好配色，300 DPI，PDF 矢量输出
- 标注了 turn 1 → turn 10 的 relative drop %

**关于 TG/SS AR 数据**: 服务器上找到了 Qwen TG v7 AR (10 turns) 和 Qwen SS v8b AR (10 turns) 的 per-turn GAR。SS AR GAR 在 0.39-0.49 范围（比 base 高一个数量级），放同一坐标轴会压缩 base 曲线，故只画了 TG AR 虚线作对比。Llama TG AR 仅有 4 turns，未纳入。

---
