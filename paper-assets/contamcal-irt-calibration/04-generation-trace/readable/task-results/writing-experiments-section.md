# writing experiments section

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-section_20260513T183138_result.json`
- **Structured JSON:** [`f0b842aad9f02a6dffc1.json`](../../sessions/f0/f0b842aad9f02a6dffc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证清单：

1. **LaTeX 语法** — 所有环境正确嵌套（15 open / 15 close，tabular 嵌套在 table 内）
2. **\ref / \label 一致** — 17 个 label 定义，所有 \ref 和 \eqref 指向已有 label（本文或 method.tex 中的 `eq:rrf`, `eq:4pl`, `eq:measurement_error`, `eq:calibrated_mc`, `sec:stage1`, `sec:inference`, `sec:signal_survival`）
3. **7 个 baselines** — B0–B6 全部有描述
4. **5 个 evaluation metrics** — Calibration error (MAE), Interval coverage, Interval sharpness, Ranking preservation (Kendall's τ), Dose-response monotonicity (Spearman ρ)，均有公式定义
5. **main.tex** — 已添加 `\input{experiments}`
6. **references.bib** — 已添加 4 个 benchmark 引用（MMLU, GSM8K, ARC, HumanEval）

Results 子节包含：
- Table `tab:main_results`：主校准结果（methods × benchmarks, MAE + coverage + τ）
- Table `tab:rrf_ablation`：RRF 消融（full vs drop-one vs single-signal AUC）
- Table `tab:k_sensitivity`：k-sensitivity
- Figure `fig:dose_response`：剂量-响应曲线
- Figure `fig:ci_width`：CI width vs noise level (exp-005)
- Figure `fig:signal_survival`：Signal survival under RL (exp-008)

所有定量结果用 `\textbf{[PLACEHOLDER: exp-XXX]}` 标注，数字占位用 `XX.X` / `X.XX` / `[TBD]`。

---
