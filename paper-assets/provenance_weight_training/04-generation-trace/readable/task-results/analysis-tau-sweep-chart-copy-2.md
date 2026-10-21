# analysis tau sweep chart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tau_sweep_chart_20260515T193128_result.json`
- **Structured JSON:** [`84ce501ac439ee5be0f3.json`](../../sessions/84/84ce501ac439ee5be0f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

- **PDF**: `/root/provenance_weight_training/output/figures/tau_sweep_dual_axis.pdf` (28K)
- **PNG**: `/root/provenance_weight_training/output/figures/tau_sweep_dual_axis.png` (174K)
- **脚本**: `/root/provenance_weight_training/scripts/plot_tau_sweep.py`
- **Artifact ID**: `art_20260515_14b48c`

图表要素：
- 左 Y 轴蓝色实线 + 圆形 markers 显示 PPL，右 Y 轴红色虚线 + 三角 markers 显示 mean(b*)
- 灰色水平虚线标注 uniform baseline (PPL=17.694)
- τ=0.8 处金色星号标记 optimal，带箭头注释 `τ*=0.8`
- 浅蓝色背景带标注 safe range (τ∈[0.5, 0.8])
- τ>0.8 区域标注 "PPL degrades (weight inflation)"
- Serif 字体，300 DPI，PDF+PNG 双格式输出

---
