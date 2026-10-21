# analysis nmin sensitivity chart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nmin_sensitivity_chart_20260515T213707_result.json`
- **Structured JSON:** [`35617de36397968f4ced.json`](../../sessions/35/35617de36397968f4ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册完成。

**输出文件**（服务器 westd-47453）：
- `/root/provenance_weight_training/output/figures/nmin_sensitivity.pdf` (39K)
- `/root/provenance_weight_training/output/figures/nmin_sensitivity.png` (236K)
- 绘图脚本：`plot_nmin_sensitivity.py`（同目录）

**图表内容**：
- **上子图**：n_min vs PPL，含 uniform（灰虚线）和 grid-best b=0.5（蓝虚线）两条 baseline；n_min=2 用星号标记为最优点（PPL=17.653）；n_min=3 用空心菱形+虚线连接标注为 legacy pre-bugfix；n_min=4 标注退化为 uniform
- **下子图**：n_min vs b\*\_mean 柱状图，带数值标注；n_min=3 用斜线填充区分；n_min=4 标注 ESS 约束完全绑定；底部标注各 n_min 的行为特征

风格与 τ sensitivity 图保持一致（同色系、同 marker 风格、同网格线设置）。

---
