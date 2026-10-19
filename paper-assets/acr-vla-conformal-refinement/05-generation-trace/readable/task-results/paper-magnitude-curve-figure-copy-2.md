# paper magnitude curve figure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_magnitude-curve-figure_20260516T112922_result.json`
- **Structured JSON:** [`0dabb9b4abd82f4f9eea.json`](../../sessions/0d/0dabb9b4abd82f4f9eea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已生成并注册：

- `magnitude_curve.png` / `magnitude_curve.pdf` — 论文核心 figure
- `fig_magnitude_curve.py` — 可复现生成脚本

图表采用 **log-scale X 轴**（最后一个点标注 "uncapped"），清晰展示：
- **Obs-Only CRM**（蓝线）：inverted-U 形态，peak 22% at ε=0.2，uncapped 仍有 17%，全范围安全
- **Per-DOF CRM**（红线）：ε≥0.3 进入 collapse region（浅红阴影），uncapped 降至 0%
- **Argmin baseline** 12% 灰色虚线作为参照

如需调整配色、字号或标注位置可直接改脚本重跑。

---
