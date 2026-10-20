# paper figure layout overhaul

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-layout-overhaul_20260525T121947_result.json`
- **Structured JSON:** [`2ec4c33e921e840e7ff1.json`](../../sessions/2e/2ec4c33e921e840e7ff1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Here is the summary:

## 每页布局
- p1: Title + Abstract + Introduction
- p2: **Figure 1** (框架图, figure\*) + Introduction 继续
- p3: **Figure 2** (OVB bias scatter, figure[t]) + Background
- p4: **Table 1** (Error propagation, table[t]) + Method (Model Specification)
- p5: **Figure 3** (Judge severity forest plot, figure[t]) + Method (Staged Estimation, Identifiability)
- p6: **Table 2** (Main results, table[t]) + Experiments (Setup)
- p7: **Figure 4** (Contamination profile, figure\*[t]) + Experiments (Results)
- p8: Experiments (Error Prop) + Conclusion + Limitations + References 开始

## 移到 appendix 的图
- `fig4_bias_vs_rho` → `app:bias_vs_rho` (Appendix S: Bias vs. Confounding Level)
- `fig3_error_propagation` → `app:error_prop` (Appendix T: Error Propagation Visualization)
- `fig5_cn_recovery` → `app:cn_recovery` (Appendix U: Contamination Recovery)

## 引用更新
- `background.tex:42` — `Figure~\ref{fig:ovb_bias}b` → `Appendix~\ref{app:bias_vs_rho}`
- `background.tex:42` — `Figure~\ref{fig:ovb_bias}a` → `Figure~\ref{fig:ovb_bias}`
- `method.tex:86` — `Figure~\ref{fig:error_prop}` → `Appendix~\ref{app:error_prop}`
- `method.tex:70` — 新增 `Appendix~\ref{app:cn_recovery}` 引用

## 拆分的图
- Figure 2 原始合并图 (`figure*` with fig2_ovb_bias + fig4_bias_vs_rho) → 拆为独立 `figure[t]` (ovb_bias 留正文) + appendix (bias_vs_rho)

## Float 重排
- Table 2 (main_results) 从 experiments.tex 移至 method.tex 末尾以 float 到 p6 顶部
- Figure 3 (forest_dj) 从 experiments.tex 移至 method.tex identifiability 前以 float 到 p5
- Figure 4 (cn_profile) 提前至 experiments.tex 开头以 float 到 p7

## 编译结果
- 页数：8（正文）+ 9（references + appendix）= 17 总页
- undefined refs：0
- multiply defined labels：0
- warnings：仅 appendix 中 `[h]` → `[ht]` 浮动调整（无害）

---
