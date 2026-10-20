# paper writing method

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260514T212853_result.json`
- **Structured JSON:** [`ef3b58b5c21a671d9863.json`](../../sessions/ef/ef3b58b5c21a671d9863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`method.tex` 已写入并注册。

**摘要：**
- 1293 words，符合 1300 word budget
- 4 subsections：Problem Formulation → Weak Supervision Pipeline (LFs + aggregation) → Detection Methods (structural / ProgressProbe / LLM-as-judge) → Temporal Label Models (TWV / HMM / Lag-Aware HMM)
- Notation 与 experiments.tex 完全一致（$T$, $w_i$, $k$, $y_i$, $\lambda_j$, $\sigma$, conf）
- 5 citations 均来自 references.bib，无编造引用
- `tab_lf_design` 有 `\label` 和 `\caption`；`fig_pipeline` 引用路径 `../../figures/paper/fig_pipeline.pdf`
- 跨章节引用（`sec:cmd_rep_ablation`, `sec:lf_temporal`, `sec:main_results`）已验证存在于 experiments.tex
- LF firing rate 数字来自 registry（cmd_rep: SWE 65.6%, OH 92.3%; file_diff OH 87% correctness），缺失值用 `---` 占位

---
