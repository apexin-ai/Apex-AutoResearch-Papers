# analysis plot data prep

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plot_data_prep_20260513T112515_result.json`
- **Structured JSON:** [`1688a6cd8800a9b3b439.json`](../../sessions/16/1688a6cd8800a9b3b439.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。生成的文件：

| 文件 | 行数（含表头） | 说明 |
|------|---------------|------|
| `selection_ratio_by_gen.csv` | 9 | gen × 2 ratio 列 |
| `ppl_by_gen.csv` | 9 | gen × 3 method ppl |
| `rare_ngram_by_gen.csv` | 9 | gen × 3 method rare ngram |
| `all_metrics_by_gen.csv` | 25 | 长格式，3 method × 8 gen = 24 行 + 表头 |

路径：`/root/autodl-tmp/div_cal_verify/plot_data/`

注意：`all_metrics_by_gen.csv` 中 uncurated 的 ratio 列为空（uncurated 无 selection ratio），列为 `gen, method, ppl, rare, ratio`。任务要求的 rankme、knn、corr 列未包含——这些数据不在本次提供的数据中，需要时可补充。

---
