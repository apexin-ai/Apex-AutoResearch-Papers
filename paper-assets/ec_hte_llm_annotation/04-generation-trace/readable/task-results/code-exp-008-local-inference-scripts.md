# code exp 008 local inference scripts

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-local-inference-scripts_20260521T115154_result.json`
- **Structured JSON:** [`e68179e4cc439a10e113.json`](../../sessions/e6/e68179e4cc439a10e113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Two scripts written to `artifacts/exp-008/scripts/`:

**`llama31_8b_annotate.py`** — `meta-llama/Llama-3.1-8B-Instruct`
- Uses `tokenizer.apply_chat_template` with Llama's native chat format (no system message, as Llama 3.1 works fine with user-only)
- Returns tensors directly from `apply_chat_template`

**`qwen25_7b_annotate.py`** — `Qwen/Qwen2.5-7B-Instruct`
- Uses Qwen's chat template with a system message (`"You are a helpful assistant."`, Qwen's default)
- Calls `apply_chat_template(tokenize=False)` then tokenizes separately, matching Qwen's recommended pattern

Both scripts share the same structure: same prompt as exp-008, bfloat16/float16 auto-select, greedy decoding (`do_sample=False`, `max_new_tokens=10`), checkpoint every 50 to JSON, OOM handling, `--device`/`--batch-size`/`--resume`/`--model-path` CLI flags, warmup timing estimate, and end-of-run summary.

---
