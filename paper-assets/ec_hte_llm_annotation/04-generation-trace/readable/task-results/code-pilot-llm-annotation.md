# code pilot llm annotation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pilot-llm-annotation_20260521T020651_result.json`
- **Structured JSON:** [`825b055997e0633557e0.json`](../../sessions/82/825b055997e0633557e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All good. Script created at `pilot_llm_annotation.py` and validated:

- Data loads correctly from TweetEval sentiment
- Subgroup features (hashtag, mention, text length bin) extracted properly
- Prompts render correctly (zero-shot and few-shot templates ready)
- CSV output has the right schema
- Subgroup stats compute and save fine
- Both vLLM and transformers backends wired up, switchable via `--backend`
- `--model` flag supports switching between 72B-AWQ and 7B

To run on GPU: `python3 pilot_llm_annotation.py --backend vllm --model Qwen/Qwen2.5-72B-Instruct-AWQ`

---
