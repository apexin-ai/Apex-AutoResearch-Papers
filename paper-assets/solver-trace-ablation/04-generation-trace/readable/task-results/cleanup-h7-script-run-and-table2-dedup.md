# cleanup h7 script run and table2 dedup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_h7-script-run-and-table2-dedup_20260514T102000_result.json`
- **Structured JSON:** [`85355c12b0e051171a7c.json`](../../sessions/85/85355c12b0e051171a7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结果报告

### 任务 1: classify_h7.py 运行结果

| 模型 | Proved | H7 strict | H7 relaxed | Single premise | ISR=1.0 |
|------|--------|-----------|------------|----------------|---------|
| **s42 ISR β=0.1** | 81 | 55/81 (67.9%) | 13/81 (16.0%) | 15/81 (18.5%) | 10/81 (12.3%) |
| **s43 ISR β=0.1** | 61 | 59/61 (96.7%) | 57/61 (93.4%) | 61/61 (100%) | 40/61 (65.6%) |
| **s44 ISR β=0.1** | 89 | 77/89 (86.5%) | 82/89 (92.1%) | 89/89 (100%) | 65/89 (73.0%) |
| **random β=0.1 s42** | 79 | 56/79 (70.9%) | 0/79 (0.0%) | 0/79 (0.0%) | 0/79 (0.0%) |

注意：s42 目录没有 `eval_results.json`，使用了 `eval_sta_results.json` 代替。s42 的 H7 数值明显低于 s43/s44（strict 67.9% vs 86-97%），可能与 eval 文件来源不同有关。

输出保存在服务器 `/root/autodl-tmp/outputs/h7_classification/`，已注册为 artifact。

### 任务 2: Table 2 旧版清理

已移动 3 个旧版文件到 `artifacts/_deprecated/`：
- `artifacts/_project/paper/table2_hacking_taxonomy.tex` → `_deprecated/table2_hacking_taxonomy_from_project_paper.tex`
- `artifacts/paper_tables/table2_hacking_taxonomy.tex` → `_deprecated/table2_hacking_taxonomy_from_paper_tables.tex`
- `artifacts/paper_tables/table2_hacking_taxonomy.csv` → `_deprecated/table2_hacking_taxonomy_from_paper_tables.csv`

权威版本仅剩：`artifacts/table2_hacking_taxonomy.tex` 和 `artifacts/table2_hacking_taxonomy.csv`。

另外发现 `artifacts/_project/data/table2_hacking_taxonomy.csv` 也存在（由 register_artifact 系统生成），不在清理范围内。

---
