# fix exp002 bf16 only

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002_bf16_only_20260521T083543_result.json`
- **Structured JSON:** [`3cbdfe52efb14780f32f.json`](../../sessions/3c/3cbdfe52efb14780f32f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **总行数**: 4,608 ✓
- **precision**: 仅 `bfloat16` ✓
- **每个 benchmark**: 1,152 conditions ✓ (4 models × 1 precision × 2 temps × 6 prompts × 6 seeds × 4 orderings)
- **4 benchmarks**: mmlu, gsm8k, arc, hellaswag ✓
- **exp001 未改动** — 本地和远程 exp001 配置保持原样

改动摘要：`generate_design.py` 中 exp002 的 `precision` 从 `["bfloat16", "float16"]` → `["bfloat16"]`，`expected_total` 从 9216 → 4608，docstring 同步更新。设计 CSV 已在服务器上重新生成为 `design_matrix_exp002.csv`。

---
