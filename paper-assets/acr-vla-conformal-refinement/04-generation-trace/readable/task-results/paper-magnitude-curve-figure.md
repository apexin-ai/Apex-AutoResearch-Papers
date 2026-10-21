# paper magnitude curve figure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_magnitude-curve-figure_20260516T114709_result.json`
- **Structured JSON:** [`de685cb42ccf1255f3d7.json`](../../sessions/de/de685cb42ccf1255f3d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。文件已生成：

- **PDF**: `/root/acr-vla-conformal-refinement/figures/magnitude_curve_obs_vs_perdof.pdf` (29KB)
- **PNG**: `/root/acr-vla-conformal-refinement/figures/magnitude_curve_obs_vs_perdof.png` (148KB)

脚本位于 `/root/acr-vla-conformal-refinement/figures/gen_magnitude_curve.py`，包含：
- Log-scale X 轴，末尾标注 "∞ (no cap)"
- Obs-Only 蓝线 peak 箭头标注 22%
- Per-DOF 红线 + collapse 区域浅红 shading
- Obs-Only 与 argmin 之间绿色半透明 fill（暗示全程优于 baseline）
- 两条 baseline 虚线
- 去掉 top/right spines，色盲友好配色

---
