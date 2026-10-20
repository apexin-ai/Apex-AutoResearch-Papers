# viz rank ablation chart

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_rank-ablation-chart_20260515T163715_result.json`
- **Structured JSON:** [`e5d57a72c4b2c0078128.json`](../../sessions/e5/e5d57a72c4b2c0078128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出文件：

| 产出 | 路径 |
|------|------|
| PDF 图表 | `artifacts/rank_ablation_chart.pdf` |
| PNG 图表 (300dpi) | `artifacts/rank_ablation_chart.png` |
| LaTeX 表格 | `artifacts/rank_ablation_table.tex` |

图表结论：r16 α32 (ratio=2) baseline 以 87.51% 最优，增大 rank 到 32 无论 alpha=32 还是 alpha=64 都略有下降（~0.5pp），说明当前数据规模下 rank=16 已足够，更大 rank 反而轻微过拟合。r32 α64 的 EM (84.55) 高于 r32 α32 (83.40)，保持 ratio=2 对 exact match 有帮助。

---
