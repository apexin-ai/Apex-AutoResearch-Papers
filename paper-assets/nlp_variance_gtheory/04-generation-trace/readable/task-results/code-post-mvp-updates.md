# code post mvp updates

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post_mvp_updates_20260520T185622_result.json`
- **Structured JSON:** [`68bc89b17318b269b2ab.json`](../../sessions/68/68bc89b17318b269b2ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项修改完成：

1. **requirements.txt** — vllm 版本约束更新为 `>=0.9.0`，顶部加了 Blackwell GPU 注释
2. **variance_decomposition.py** — 新增 `--response-var` CLI 参数（`correct` / `text_exact_match`）、`compute_text_exact_match()` 函数（per-item canonical text 比较）、输出文件名按 response_var 区分（`variance_components.json` vs `variance_components_text.json`）

---
