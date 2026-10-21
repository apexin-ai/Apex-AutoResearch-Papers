# code analysis framework

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_framework_20260520T233759_result.json`
- **Structured JSON:** [`2028d8e2dd9f1ad4cc6d.json`](../../sessions/20/2028d8e2dd9f1ad4cc6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 和 CLI 均验证通过。

两个文件已写入 `artifacts/code/src/analysis/`:

**model_facet_analysis.py** — 7 facets 全交叉 G-study:
- 复用 `variance_decomposition.py` 的 `compute_ss`、`estimate_variance_components`、`compute_text_exact_match`
- 7 main effects + 21 two-way interactions + residual
- G coefficient（model 作为 random facet）
- D-study 投影：sweep model count 1-10
- Glob 输入支持多 JSONL 合并

**bootstrap_ci.py** — Bootstrap 置信区间:
- 以 item 为 resampling unit，有放回抽样
- 自动检测 6-facet 或 7-facet 设计
- 每次 resample 重新跑完整 ANOVA → 方差分量
- 输出 point estimate + [2.5%, 97.5%] percentile CI

---
