# verify shap files check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_shap_files_check_20260515T191736_result.json`
- **Structured JSON:** [`76ca3ed66df1c15df3cd.json`](../../sessions/76/76ca3ed66df1c15df3cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**完整**

### 文件清单

| 预期文件 | 状态 | 大小 |
|---------|------|------|
| `shap_importance_all_cells.json` | ✓ | 5,467 B |
| `shap_cross_cell_summary.json` | ✓ | 1,788 B |
| `shap_vs_permutation.json` | ✓ | 4,110 B |
| `shap_summary_plots/` (12 张图) | ✓ 12/12 | 9 per-cell bar + aggregated_bar + heatmap + scatter |

注意：实际路径在 `/root/autodl-tmp/recursive_gen_depth_est/results/shap_analysis/`（不是 `/root/recursive_gen_depth_est/`）。

### 9 cells 覆盖

`shap_importance_all_cells.json` 包含全部 9 cells（pythia×3, gpt2xl×3, olmo×3），每 cell 19 个 feature 的 SHAP 值齐全。

### 核心数字

- **Top-2 features 跨 cell 一致性**：`p90_ppl` 和 `var_surprisal` 在全部 9/9 cells 中均进入 top-4，且在每个 cell 的 SHAP 排名中交替占据 #1 和 #2（avg SHAP 0.0894 和 0.0803）
- **PPL + surprisal 类占比**：跨 cell 平均排名前 6 全部是 PPL/surprisal 相关特征（p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl, var_ppl），占 top-6 的 100%
- **SHAP vs permutation Spearman ρ**：mean = **0.8302**，range [0.7491, 0.9158]，全部 9 cells p < 0.001

---
