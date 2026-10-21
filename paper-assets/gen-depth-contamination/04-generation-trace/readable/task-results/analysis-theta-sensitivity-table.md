# analysis theta sensitivity table

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta_sensitivity_table_20260517T110418_result.json`
- **Structured JSON:** [`539a21828f7a92317ee1.json`](../../sessions/53/539a21828f7a92317ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已生成并注册：

- `theta_sensitivity_table.csv` — 11 configs × 6 θ 值的 K\* 矩阵
- `theta_sensitivity_table.tex` — booktabs 风格 LaTeX 表，θ=0.60 列加粗，按 domain 分组，含脚注标注

核心结论在 θ∈[0.55, 0.70] 全范围内定性稳定：web text K\*∈{1,2,3} 且主流为 2；arXiv K\*∈{2,3,4} 且主流为 3；cross-scorer 始终 K\*≤2 且 θ≥0.575 后固定为 1。

---
