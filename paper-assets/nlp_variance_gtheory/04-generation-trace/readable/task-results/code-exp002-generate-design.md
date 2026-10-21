# code exp002 generate design

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_generate_design_20260521T081528_result.json`
- **Structured JSON:** [`1f915211d2018e0d29d6.json`](../../sessions/1f/1f915211d2018e0d29d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **exp001**（向后兼容）：5,184 行，列 = `condition_id, model, precision, temperature, top_p, prompt_template, seed, ordering`，无 `benchmark` 列
- **exp002**：9,216 行，新增 `benchmark` 和 `items_file` 列
  - 4 benchmarks 各 2,304 条，分布均匀
  - 精度仅 `bfloat16, float16`（排除 FP32 confound）
  - 温度仅 `0.0, 0.7`（排除 T=0.3）
  - `items_file` 正确映射到各 benchmark 的数据文件

---
