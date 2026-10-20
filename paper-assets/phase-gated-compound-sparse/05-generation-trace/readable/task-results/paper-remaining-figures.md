# paper remaining figures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_remaining_figures_20260514T094428_result.json`
- **Structured JSON:** [`3fc625cbb440284352df.json`](../../sessions/3f/3fc625cbb440284352df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 PDF 全部生成完毕。

| 文件 | 大小 | 数据来源 |
|------|------|----------|
| `fig1_dose_response.pdf` | 16.3KB | `analysis/bootstrap_results_full.json` → `per_strategy.importance/random.{0.15..0.3}.gradient` + `gradient_95ci` |
| `fig3_crossover.pdf` | 15.2KB | `analysis/v6_analysis_results.json` → `comparison.s025.{high,mid,low}.{imp_median,rnd_median}` |
| `fig4_bootstrap.pdf` | 16.1KB | `analysis_output/permutation_test_results.json` → `sparsity_levels.{s015..s030}.permutation_test_difference.{observed_median_diff, ci_95_low, ci_95_high, bonferroni_p}` |
| `fig5_crossmodel.pdf` | 18.1KB | `analysis_output/cross_model_analysis.json` → `importance_median_diffs.{deepseek,qwen}.{s015..s030}` |

所有路径：`/root/autodl-tmp/pacs/figures/fig{1,3,4,5}_*.pdf`

实际 JSON 数据与任务描述中的硬编码值有显著差异（如 fig3 crossover 实际 importance high=0.664 vs 任务说的 0.032），已全部使用文件实际数据。

---
