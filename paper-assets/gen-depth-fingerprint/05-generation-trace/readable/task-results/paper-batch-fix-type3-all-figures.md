# paper batch fix type3 all figures

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_batch-fix-type3-all-figures_20260523T071645_result.json`
- **Structured JSON:** [`8098e5972f9cbaa0e82a.json`](../../sessions/80/8098e5972f9cbaa0e82a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复结果

| # | 文件 | 修复前 Type 3 | 修复后 Type 3 | 说明 |
|---|------|:---:|:---:|------|
| 1 | fig1_differential_response.pdf | 4 | **0** | 已 clean |
| 2 | fig_ddr_trajectory.pdf | 5 | **0** | 已 clean |
| 3 | fig3_baseline_comparison.pdf | 2 | **0** | 已 clean |
| 4 | fig_convergence_dynamics.pdf | 3 | **0** | 已 clean |
| 5 | fig_transfer_heatmap.pdf | 3 | **0** | 已 clean |
| 6 | fig_appendix_confusion.pdf | 2 | **0** | 已 clean |
| 7 | fig_appendix_cross_temp.pdf | 2 | **0** | 已 clean |
| 8 | fig_appendix_ddr_trends.pdf | 5 | **0** | 已 clean |
| 9 | fig_appendix_instruct_ddr.pdf | 5 | **0** | 已 clean |
| 10 | fig_appendix_nll_distribution.pdf | 1 | **0** | 已 clean |
| 11 | fig_appendix_per_gen.pdf | 2 | **0** | 已 clean |
| 12 | fig_appendix_umap.pdf | 2 | **0** | 已 clean |
| 13 | fig_appendix_violin.pdf | 2 | **0** | 已 clean |
| 14 | fig_ddr_holdout_split.pdf | 3 | **0** | 已 clean |
| 15 | fig_ddr_scatter.pdf | 5 | **0** | 已 clean |
| 16 | fig1_combined.pdf | 6 | **0** | pdf2ps→ps2pdf 修复（未在论文中引用） |

- **main.pdf: 0 Type 3 字体，37 页**
- 1-15 在扫描时已经是 clean（之前的 `fix_fonttype.py` + 脚本 `pdf.fonttype=42` 已生效）
- 仅 `fig1_combined.pdf` 需要修复，通过 `pdf2ps → ps2pdf` 消除
- 所有文件已同步到本地 `docs/chart/`、`artifacts/_project/chart/`、`artifacts/_project/paper/figures/`

---
