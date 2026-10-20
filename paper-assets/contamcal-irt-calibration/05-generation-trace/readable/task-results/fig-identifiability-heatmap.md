# fig identifiability heatmap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fig_identifiability_heatmap_20260517T094555_result.json`
- **Structured JSON:** [`648c14bdca9668bc0b0f.json`](../../sessions/64/648c14bdca9668bc0b0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完成。

- `/root/contamcal-irt-calibration/figures/fig_identifiability_heatmap.pdf`: 26,266 bytes
- `/root/contamcal-irt-calibration/figures/fig_identifiability_heatmap.png`: 118,737 bytes

双面板布局 (6.5×2.5 inches，每 panel 等效单栏宽度):
- 左面板: γ bias heatmap (RdBu_r diverging, white=0)，4×4 grid (AUC: 0.55/0.65/0.80/0.90 × J: 8/20/50/100)，bias 范围 [-0.024, +0.020]，所有条件 bias < 0.025
- 右面板: 95% CI coverage (RdYlGn)，覆盖率 80%-100%，绝大部分 ≥90%

数据来源: `exp004_sim_sweep/results/sweep_summary.json`，16 main conditions (gamma_true=0.5, 10 seeds each)。

---
