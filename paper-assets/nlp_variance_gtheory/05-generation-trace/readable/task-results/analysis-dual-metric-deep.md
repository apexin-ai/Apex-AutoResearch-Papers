# analysis dual metric deep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dual_metric_deep_20260520T215443_result.json`
- **Structured JSON:** [`9a65f7487e13aedf2cd1.json`](../../sessions/9a/9a65f7487e13aedf2cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出：

**文件**:
- `artifacts/analysis/dual_metric_analysis.md` — 完整分析报告
- `artifacts/analysis/fig1_variance_decomposition_comparison.png` — 方差分解对比
- `artifacts/analysis/fig2_item_scatter.png` — Item-level 散点图
- `artifacts/analysis/fig3_facet_heatmap.png` — Facet 效应热力图

**核心发现**:

1. **两个 metric 测量完全不同的构念** — binary_correct 由 item 难度主导（58.4%），text_exact_match 由 prompt_template:item_id 交互（37.5%）和 temperature（16.9%）主导。二者方差结构几乎无重叠。

2. **Temperature 对准确性几乎无影响，但对确定性有决定性影响** — temp=0.5 时 text_exact_match 从 0.247 骤降至 0.019，而 binary_correct 仅微变（0.643→0.669）。采样随机性改变文字表述但不改变答案字母。

3. **Item-level 无显著相关**（Spearman ρ = −0.21, p = 0.14）。最不一致的 items 全是"高准确-低确定"型：总是答对但每次文本不同。

4. **两个 metric 必须同时保留**：binary_correct 测评估有效性，text_exact_match 测可复现性，它们提供正交信息。

---
