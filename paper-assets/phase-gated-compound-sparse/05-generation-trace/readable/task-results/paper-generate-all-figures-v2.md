# paper generate all figures v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_generate_all_figures_v2_20260514T123045_result.json`
- **Structured JSON:** [`c0c8c6cb40b8ec123016.json`](../../sessions/c0/c0c8c6cb40b8ec123016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个文件（4 figures × 2 目录）验证通过。

### 汇报

| Figure | 文件大小 | 数据源 |
|--------|---------|--------|
| `fig1_dose_response.pdf` | 20,786 bytes | `experiment_summary_table.json` + `profiling_output_bf16_{ds,qw}_imp_s0{10,35}/profiling_results.json` |
| `fig3_crossover.pdf` | 37,090 bytes | `experiment_summary_table.json` |
| `fig4_bootstrap.pdf` | 22,277 bytes | `cohens_d_paired_dz_6point.json` |
| `fig5_crossmodel.pdf` | 22,115 bytes | `cross_model_analysis.json` |

**文件路径**（两份副本）：
- `/root/autodl-tmp/pacs/figures/fig{1,3,4,5}_*.pdf`
- `/root/autodl-tmp/pacs/paper/figures/fig{1,3,4,5}_*.pdf`

**生成脚本**：`/root/autodl-tmp/pacs/figures/generate_paper_figures_v2.py`

**关键变更 vs 旧脚本**：
- fig1: 从 4 点扩展到 6 点 dose-response (s010-s035)，Y 轴改为 symlog，显示双模型 + random baseline
- fig3: 从 bar chart 改为 heatmap，3×8 矩阵覆盖 4 个 sparsity × importance/random
- fig4: 从 permutation test forest plot 改为 Cohen's d_z forest plot，6 点 × 双模型，带 approximate CI
- fig5: 从 line chart 改为 dual bar chart，标注 Spearman ρ=1.0

---
