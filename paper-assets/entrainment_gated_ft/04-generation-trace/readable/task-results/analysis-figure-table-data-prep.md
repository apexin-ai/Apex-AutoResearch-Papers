# analysis figure table data prep

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_figure-table-data-prep_20260519T164223_result.json`
- **Structured JSON:** [`ca58dca607983d4ee114.json`](../../sessions/ca/ca58dca607983d4ee114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个数据文件全部生成并注册完成。

| 文件 | 行数 | 路径 |
|------|------|------|
| `convergence_table.csv` | 12 (header+11 benchmarks) | `artifacts/paper_data/convergence_table.csv` |
| `per_example_table.csv` | 4 (header+3 archs) | `artifacts/paper_data/per_example_table.csv` |
| `gdn_sensitivity_table.csv` | 7 (header+6 benchmarks) | `artifacts/paper_data/gdn_sensitivity_table.csv` |
| `decoupling_data.csv` | 6 (header+5 ratios) | `artifacts/paper_data/decoupling_data.csv` |
| `bca_ci_data.json` | 18 | `artifacts/paper_data/bca_ci_data.json` |

数据来源：exp-001/008 registry（6 benchmarks）、exp-011/011-xstorycloze registry（5 benchmarks）、exp-003/003-p2 registry（per-example counts）、exp-010 registry + bridge CSV（decoupling + Jaccard）、exp-008 bootstrap_ci（BCa CI）。COPA 标记为 supplementary (n=100)，不参与 Bonferroni 校正。

---
