# analysis retrain depth7 results

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retrain-depth7-results_20260519T010713_result.json`
- **Structured JSON:** [`a39618a7e041d9b73953.json`](../../sessions/a3/a39618a7e041d9b73953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

| Pair | AUC | 95% CI | JSD |
|------|-----|--------|-----|
| 0v1 | 0.984 | [0.982, 0.985] | 0.230 |
| 1v2 | 0.897 | [0.895, 0.899] | 0.104 |
| 2v3 | 0.810 | [0.805, 0.814] | 0.075 |
| 3v4 | 0.760 | [0.753, 0.767] | 0.065 |
| 4v5 | 0.746 | [0.738, 0.754] | 0.061 |
| 5v6 | 0.702 | [0.696, 0.708] | 0.035 |
| 6v7 | 0.641 | [0.638, 0.645] | 0.018 |

**K\*=7**（所有 pair AUC > 0.60，6v7 CI 下界 0.638 仍清除阈值）。

Depth 0-4 与原 exp_qwen_retrain_chain 一致性验证通过（Δ < 0.003）。AUC 衰减为亚线性（凹形），JSD 在 depth 7 接近噪声底（0.018），K* ceiling 估计 7-8。

**已产出**:
- Registry: `exp_qwen_retrain_depth7` → DONE (success)
- LaTeX table: `artifacts/exp_qwen_retrain_depth7/retrain_depth7_results.tex`
- 分析报告: `artifacts/exp_qwen_retrain_depth7/analysis_report.md`

---
