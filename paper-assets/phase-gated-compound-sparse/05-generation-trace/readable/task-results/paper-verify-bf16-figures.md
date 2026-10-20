# paper verify bf16 figures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_verify-bf16-figures_20260514T130435_result.json`
- **Structured JSON:** [`2aaa59ea6be05e347d31.json`](../../sessions/2a/2aaa59ea6be05e347d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕。汇总报告：

---

## bf16 Figures 完整性验证报告

### 1. 文件存在性 & 大小

**主产出目录 `paper/figures/`**（论文引用目录）：

| Figure | PDF | PNG | PDF 大小 |
|--------|-----|-----|---------|
| fig1_dose_response | ✅ | ✅ | 23,853 B |
| fig1_severity_gradient | ✅ | ✅ | 23,724 B |
| fig2_cohens_d | ✅ | ✅ | 20,634 B |
| fig2_cohens_d_segment_level | ✅ | ✅ | 20,876 B |
| fig2_crossover_heatmap | ✅ | ✅ | 30,823 B |
| fig3_crossover | ✅ | ✅ | 20,525 B |
| fig4_bootstrap | ✅ | ✅ | 20,646 B |
| fig4_per_problem_dist | ✅ | ✅ | 64,860 B |
| **fig5_crossmodel** | ✅ | ✅ | **23,562 B** |

所有 PDF 均 >5KB，非空。

**其他副本目录**也存在完整文件：
- `figures/` — 含 fig1-fig5 全部 PDF+PNG + 生成脚本 `generate_paper_figures_v2.py`
- `analysis/figures/` — fig1/fig3/fig4/fig5 的独立生成脚本 + PDF
- `paper_figures/` — fig1/fig3/fig4/fig5 的 PDF+PNG 副本

### 2. Figure 5 状态

✅ **fig5_crossmodel 已存在**，paper/figures/ 中 PDF=23,562B, PNG=75,828B。之前缺失的问题已修复。

### 3. 数据来源验证

**所有生成脚本中零 fp16 引用。** 具体确认：

- `analysis/figures/fig1_dose_response.py` — 数据键全部为 `bf16_ds_imp_*` / `bf16_ds_rand_*`
- `analysis/figures/fig3_crossover.py` — 使用 `bf16_importance_s025` / `bf16_ds_rand_s025`
- `analysis/figures/fig4_bootstrap.py` — 读取 `permutation_test_results.json`（无 fp16 键）
- `analysis/figures/fig5_crossmodel.py` — 使用 `bf16_ds_imp_*` / `bf16_qw_imp_*`
- `figures/generate_paper_figures_v2.py` — 主生成脚本，所有实验键均为 `bf16_*` 前缀
- 上游数据文件 `experiment_summary_table.json` / `rebootstrap_b10000_results.json` 均无 fp16 键

### 结论

✅ fig1/fig3/fig4/fig5 四个论文 figure 全部存在、非空、数据来源正确（均为 bf16）。Figure 5 缺失问题已修复。无问题项。

---
