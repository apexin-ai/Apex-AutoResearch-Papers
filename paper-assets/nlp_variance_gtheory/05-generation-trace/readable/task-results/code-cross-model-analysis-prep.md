# code cross model analysis prep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross_model_analysis_prep_20260521T025228_result.json`
- **Structured JSON:** [`df8e838b0f6fd2453bd9.json`](../../sessions/df/df8e838b0f6fd2453bd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过（本地无 pandas，但远程服务器有）。

**汇报**：

- **merge_cross_model.py**: 创建 — JSONL glob 加载、`--cross-model` 精度过滤（默认 bfloat16,float32）、text_exact_match 多数票计算（按 model/precision/prompt_template/ordering/item_id 分组）、输出 CSV
- **model_facet_analysis.py**: 修改 — 新增 `--input`（CSV 输入，与 `--data` 互斥）和 `--precisions`（精度过滤）参数
- **bootstrap_ci.py**: 修改 — 新增 `--input`（CSV 输入，与 `--data` 互斥）和 `--n-boot` 别名
- **run_cross_model_analysis.sh**: 创建 — 三步 pipeline（merge → G-study → bootstrap 200 resamples）
- **dry-run**: 通过（AST 语法检查 3/3 OK）

---
