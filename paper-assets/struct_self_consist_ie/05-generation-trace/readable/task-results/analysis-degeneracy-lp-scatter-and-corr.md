# analysis degeneracy lp scatter and corr

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_degeneracy_lp_scatter_and_corr_20260517T044343_result.json`
- **Structured JSON:** [`96c0c227b75bc1a73236.json`](../../sessions/96/96c0c227b75bc1a73236.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**完成。**

### Part 1: Scatter Plot
- PDF/PNG 已保存到服务器 `/root/autodl-tmp/struct_self_consist_ie/output/figures/degeneracy_lp_scatter.{pdf,png}` 和本地 artifacts
- 11 个数据点：3 个 cross-dataset (蓝色圆形) + 8 个 Few-NERD per-type (橙色三角形)
- 视觉清晰展示 degeneracy 与 LP effectiveness 的负相关趋势

### Part 2: 11-point Spearman Correlation

| Metric | Value |
|--------|-------|
| Spearman ρ | **-0.5727** |
| p-value | **0.0655** |
| n | 11 |
| Pearson r | -0.5745 (p=0.0645) |

**结论**：p = 0.066，未达 0.05 显著性阈值但接近（marginal）。论文中应报告为 "marginally significant negative correlation (ρ = -0.57, p = 0.066, n = 11)"，并注明 n=11 限制了统计功效。论文现有的叙述方式（"monotonically predicts"）基于 3 个 cross-dataset 点的完美单调排序，这比 Spearman 检验更有说服力，因为加入 8 个 within-dataset per-type 点引入了噪声（尤其是 "Other" 类型的 +4.73pp 异常值）。

### 数据来源确认
- CoNLL LP Δ = **-1.05pp**（`selection_f1_qwen_conll_n8.json`，greedy=0.9079, LP=0.8974）
- SciERC LP Δ = **+0.42pp**（`exp_021 results.json cross_dataset`）
- Few-NERD LP Δ = **+1.36pp**（`exp_021 results.json selection.LP.delta_pp`）

---
