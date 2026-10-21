# fix unified model names

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_unified_model_names_20260521T074947_result.json`
- **Structured JSON:** [`7a91efbbbeb0a69ca871.json`](../../sessions/7a/7a91efbbbeb0a69ca871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结修改：

**`src/config/model_paths.py`** — 新增 `MODEL_DISPLAY_NAMES` 字典和 `normalize_model_name()` 函数，覆盖所有模型名变体（HF repo ID、目录名、小写名、完整路径）→ 统一简称：
- `Llama-3.1-8B`、`Gemma-2-9B`、`Mistral-7B-v0.3`、`Qwen3-8B`

**`scripts/bf16_fp16_sensitivity.py`** — 用 `normalize_model_name` 替换原来的 `split('/')[-1]` 逻辑

**`scripts/leave_one_model_out.py`** — 读取 CSV 后立即 normalize 模型名

**已重新生成的 JSON：**
- `bf16_fp16_only_gstudy.json` — 模型名已从 `Meta-Llama-3___1-8B-Instruct` 更新为 `Llama-3.1-8B` 等，数值不变
- `leave_one_model_out.json` — 模型名已从 `llama-3.1-8b-instruct` 更新为 `Llama-3.1-8B` 等，数值不变

---
