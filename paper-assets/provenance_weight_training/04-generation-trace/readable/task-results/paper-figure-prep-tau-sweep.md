# paper figure prep tau sweep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-prep-tau-sweep_20260516T011236_result.json`
- **Structured JSON:** [`263f5077ad72952f63a9.json`](../../sessions/26/263f5077ad72952f63a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成文件：

- `/root/provenance_weight_training/output/figures/tau_sweep.pdf` (24K)
- `/root/provenance_weight_training/output/figures/tau_sweep.png` (116K, 300dpi)

脚本 `/root/provenance_weight_training/scripts/plot_tau_sweep.py` 已覆盖旧版，改为：
- 单轴，蓝色实线+圆点标记的 adaptive PPL 曲线
- 灰色虚线 uniform baseline (17.6939)
- 红色虚线 ESS-only baseline (17.73)
- 箭头标注 τ*=0.8 最优点 (PPL=17.6527)
- Nature/ICML 风格，serif 字体，tick 朝内，12pt，tight layout

---
