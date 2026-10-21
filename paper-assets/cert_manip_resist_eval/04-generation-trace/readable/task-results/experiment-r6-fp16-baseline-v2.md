# experiment r6 fp16 baseline v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r6-fp16-baseline-v2_20260525T070622_result.json`
- **Structured JSON:** [`f192ecb5b90a96cdcab8.json`](../../sessions/f1/f192ecb5b90a96cdcab8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Downloads running in parallel on the server:
- **PID=10158**: FP16 models (Llama-3.1-8B ~90% done, then Qwen2.5-32B)
- **PID=11087**: AWQ models (Qwen2.5-14B, Qwen2.5-32B, Llama-3.1-8B)

I've fixed the script to handle ModelScope's different org names (`LLM-Research` vs `meta-llama`/`hugging-quants`) via `alt_ids` and uploaded it to the server. Will check back in ~4 minutes to see if Llama FP16 has finished.

---
