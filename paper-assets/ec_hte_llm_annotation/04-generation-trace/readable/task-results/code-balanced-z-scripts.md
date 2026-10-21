# code balanced z scripts

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_balanced-z-scripts_20260521T154417_result.json`
- **Structured JSON:** [`ed6d97a71ff440793ff4.json`](../../sessions/ed/ed6d97a71ff440793ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 scripts pass AST parsing and have the required features. System message correctly present only in Qwen (Llama, Mistral, Gemma use user-only).

**Summary:**

| Script | Model ID | P(Z=1) original | P(Z=1) balanced |
|---|---|---|---|
| `llama31_8b_annotate.py` | `meta-llama/Llama-3.1-8B-Instruct` | 0.166 | 0.652 |
| `qwen25_7b_annotate.py` | `Qwen/Qwen2.5-7B-Instruct` | 0.166 | 0.652 |
| `mistral7b_annotate.py` | `mistralai/Mistral-7B-Instruct-v0.3` | 0.166 | 0.652 |
| `gemma2_9b_annotate.py` | `google/gemma-2-9b-it` | 0.166 | 0.652 |

**Changes made:**
- **Llama & Qwen** (modified): added `--z-definition` CLI arg, Z column computation with stats, new checkpoint JSON format `{"z_definition", "pz1", "labels"}`, CSV output, backward-compatible resume (handles old list format)
- **Mistral** (new, based on Llama template): user-only chat template, no system message
- **Gemma** (new, based on Qwen template): removed system message (Gemma doesn't support it), uses `apply_chat_template` with `return_tensors="pt"` like Llama style

**Note:** P(Z=1) balanced = 0.652 (higher than the estimated 0.4-0.5 in the task spec). The data has 65.2% neutral+positive tweets. The implementation follows the spec exactly: Z=1 if `true_label >= 1`.

---
