# analysis 72b vs 7b item correlation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_vs_7b_item_correlation_20260522T205131_result.json`
- **Structured JSON:** [`546dc151821d01950d4a.json`](../../sessions/54/546dc151821d01950d4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

- **JSON**: `artifacts/supplementary_analyses/scale_item_difficulty_correlation.json`
- **PDF**: `artifacts/supplementary_analyses/scale_difficulty_scatter.pdf`
- **PNG**: `artifacts/supplementary_analyses/scale_difficulty_scatter.png`

关键结果——item difficulty ordering 跨 model scale **不稳定**，ρ 远低于 0.9：

| Pair | Pearson *r* | Spearman *ρ* |
|------|------------|-------------|
| 72B vs 7B | 0.428 | 0.571 |
| 72B vs 3B | 0.450 | 0.509 |
| 7B vs 3B | 0.589 | 0.680 |

从散点图可以看到大量 item 的 accuracy 在 0 或 1 处聚集（ceiling/floor effect），且不同 scale 的 model 在这些极端点上的行为差异很大——72B 将很多 item "解决"到 p=1.0，而同样的 item 在 3B/7B 上分散在中间区域。越近的 scale pair（7B vs 3B）相关性越高，跨度大的（72B vs 3B）相关性越低。

---
