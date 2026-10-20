# code kstar theta figure

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_kstar_theta_figure_20260515T124324_result.json`
- **Structured JSON:** [`c26b646065f2f5e960e6.json`](../../sessions/c2/c26b646065f2f5e960e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

**文件路径：**
- PDF: `/root/autodl-tmp/gen-depth-contamination/artifacts/kstar_theta_curve.pdf` (32 KB)
- PNG: `/root/autodl-tmp/gen-depth-contamination/artifacts/kstar_theta_curve.png` (350 KB, 300 DPI)
- 脚本: `/root/autodl-tmp/gen-depth-contamination/scripts/plot_kstar_theta.py`

**图表内容：**

**(a) Pairwise AUC profile** — 4 条模型曲线 + 95% CI shaded band，θ=0.60 水平虚线，K*=2 边界竖线标注在 1v2 和 2v3 之间。所有模型 1v2 AUC > 0.60，2v3 AUC < 0.60，清晰呈现饱和边界。

**(b) K*(θ) sensitivity** — 4 条阶梯函数，两层灰色带标注：
- 浅蓝带 `[0.590, 0.610]`：全部 4 个模型 K*=2（unanimous）
- 灰色带 `[0.545, 0.610]`：全部模型 K*∈{2,3}
- θ=0.60 竖虚线正好落在 unanimous 区域内

**Rebuttal 论点支撑：**
- θ=0.60 时 4/4 模型一致给出 K*=2
- K* 在 θ∈[0.545, 0.610] 范围内仅在 {2, 3} 间波动，对阈值选择不敏感
- θ > 0.61 后部分模型降至 K*=1（过于保守），θ < 0.55 后部分模型升至 K*=3（过于宽松），θ=0.60 是最优平衡点

---
