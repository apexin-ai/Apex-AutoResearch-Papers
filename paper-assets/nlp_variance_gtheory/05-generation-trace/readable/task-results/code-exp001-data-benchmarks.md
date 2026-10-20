# code exp001 data benchmarks

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp001_data_benchmarks_20260520T195645_result.json`
- **Structured JSON:** [`756a8a68910d1cf2d13e.json`](../../sessions/75/756a8a68910d1cf2d13e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更总结：

**sample_mmlu.py** — 10 subjects × 20 items = 200 items。新增 5 个 subjects（high_school_mathematics, computer_security, philosophy, clinical_knowledge, international_law）。CLI 新增 `--n-items` 和 `--n-subjects` 参数，默认值向后兼容产出 200 items。

**few_shot.py** — `N_ORDERINGS` 从 2 扩展到 4，`SELECTED_SUBJECTS` 同步扩展到 10 个。与 `generate_design.py` 中 `ordering: [1, 2, 3, 4]` 匹配。每个 ordering 用 `seed + ordering_id` 保持确定性。

**sample_benchmarks.py** — 新建。支持 GSM8K（按答案数值范围分层）、ARC-Challenge（按 answerKey 分层）、HellaSwag（随机采样）。统一输出格式含 `item_id`, `question`, `benchmark` 等字段。CLI 参数：`--benchmark`, `--n-items`, `--output`, `--seed`。

---
