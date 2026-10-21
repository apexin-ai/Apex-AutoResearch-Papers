# exp shap analysis r3n3

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_shap_analysis_r3n3_20260515T190141_result.json`
- **Structured JSON:** [`0148f27d53d60f003eec.json`](../../sessions/01/0148f27d53d60f003eec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**服务器端产出**：
- `results/shap_analysis/shap_importance_all_cells.json` — 9 cell × 19 feature SHAP 值
- `results/shap_analysis/shap_cross_cell_summary.json` — 跨 cell 汇总
- `results/shap_analysis/shap_vs_permutation.json` — SHAP vs permutation 对比
- `results/shap_analysis/shap_summary_plots/` — 12 张图（9 per-cell bar + aggregated bar + heatmap + scatter）

**核心结论**：
- `var_surprisal` + `p90_ppl` 在全部 9 cell 中排名 #1/#2，贡献 53.5% SHAP importance
- PPL/surprisal 类特征占 88.8%，lexical diversity 仅 11.2%
- SHAP 与 permutation importance Spearman ρ = 0.830（全部 p < 0.001）
- SHAP、permutation、Gini 三种方法 top-5 完全一致（同 5 个特征），充分替代被审稿人质疑的 attention-importance 方法
- 报告已注册为 artifact `art_20260515_a15690`

---
