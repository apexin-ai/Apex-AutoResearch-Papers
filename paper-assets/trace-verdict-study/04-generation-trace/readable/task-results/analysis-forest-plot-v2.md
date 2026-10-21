# analysis forest plot v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forest_plot_v2_20260520T163037_result.json`
- **Structured JSON:** [`73b3eb73f6ed0c4e159b.json`](../../sessions/73/73b3eb73f6ed0c4e159b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Forest plot 已生成，输出到:
- `artifacts/figures/forest_plot_tier_boundary.pdf`
- `artifacts/figures/forest_plot_tier_boundary.png`

修改点：
- 所有多 seed cell 改用 mean ± 1.96·std 作为 CI，单 seed cell 用 Wilson CI (n=1190)
- 移除了 95% 垂直虚线
- 87–98% 区间添加灰色 "Tier gap" band
- 条件名作为 header row，模型缩进排列，颜色分 Tier 1 暖色 / Tier 2 绿色 / baseline 蓝色
- 数值标注在右侧，避免与 error bar 重叠

---
