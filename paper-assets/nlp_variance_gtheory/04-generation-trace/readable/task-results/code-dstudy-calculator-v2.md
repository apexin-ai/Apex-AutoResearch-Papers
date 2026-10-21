# code dstudy calculator v2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dstudy_calculator_v2_20260522T140839_result.json`
- **Structured JSON:** [`bdc9a336f3db10dfd627.json`](../../sessions/bd/bdc9a336f3db10dfd627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

工具已完成，验证通过：

- **Full design** (precision=3, temp=3, prompt=6, seed=6, ordering=4): G = 0.9360 ≈ 0.936 ✓
- **Single condition** (所有 n_levels=1): G = 0.5914 ≈ 0.592 ✓
- `--sweep` 正常工作，展示单个 facet 从 1 到 max 的 G 变化曲线
- 零依赖，仅用 `json`, `argparse`, `math`, `sys`

文件位于 `artifacts/exp004/tools/dstudy_calculator.py`，已注册。

---
