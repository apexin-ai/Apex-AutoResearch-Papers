# code infinity fix analysis dryrun

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_infinity_fix_analysis_dryrun_20260521T020130_result.json`
- **Structured JSON:** [`c2ac3ab85a912459a9cf.json`](../../sessions/c2/c2ac3ab85a912459a9cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。汇报：

---

**-Infinity fix:**
- **已修复**: `model_facet_analysis.py`、`bootstrap_ci.py` — 在 `load_jsonl_glob()` 中添加了 `answer_logprob` 列的 `-np.inf → NaN` 替换和 `top_logprobs` 字典中 `-inf → None` 的清洗
- **无需修复**: `variance_decomposition.py` — `compute_ss()` 和 `estimate_variance_components()` 仅处理 `correct`/`text_exact_match`（0/1 整数），不涉及 logprob

**variance_decomposition dry-run: 通过**
- 5400 obs, 6 facets, 10 bootstrap iterations
- item_id 占 58.4% 方差（最大），residual 17.6%，precision:item_id 7.2%
- G 系数和 D-study 正常输出

**bootstrap_ci dry-run: 通过**
- 同样 5400 obs, 6-facet design, 10 boots
- 点估计和 95% CI 均正常产出，无报错

---
