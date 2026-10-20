# analysis probit mape

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_probit_mape_20260523T062354_result.json`
- **Structured JSON:** [`af10c536730d8dfc45df.json`](../../sessions/af/af10c536730d8dfc45df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结果保存至 `artifacts/exp004/data/probit_mape.json`（已注册 `art_20260523_f7a59b`）。

**MAPE 汇总（binary oracle p=0.7 vs continuous TRUE_VC，1296-condition matched design）：**

| 分组 | 组件数 | MAPE |
|------|--------|------|
| 全部 22 components | 22 | **49.26%** |
| D-study 相关（含 residual） | 7 | **36.58%** |
| D-study 去 residual | 6 | **16.64%** |
| Facet × item 交互 | 5 | **12.83%** |
| Main effects | 5 | 82.51% |
| Non-item 两两交互 | 10 | 41.53% |

**关键发现：**
- **最大偏差**：residual（16% → 41%，pct_error = 156.2%）—— Bernoulli 噪声的预期效应
- **最小偏差**：temperature:prompt_template（pct_error = 4.08%）
- **Facet × item 交互恢复最好**（MAPE = 12.83%），范围 8.7%（ordering:item_id）到 17.5%（temperature:item_id）
- item_id 从 50% 压缩到 32%（pct_error = 35.7%），但仍被正确识别为最大系统性方差源
- Main effects 恢复最差（MAPE = 82.5%），因绝对量小且与 grand mean 混淆

---
