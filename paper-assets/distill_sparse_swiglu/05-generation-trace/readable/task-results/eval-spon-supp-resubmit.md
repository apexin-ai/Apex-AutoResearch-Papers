# eval spon supp resubmit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_spon_supp_resubmit_20260515T194209_result.json`
- **Structured JSON:** [`b2742ef0322431c4eecf.json`](../../sessions/b2/b2742ef0322431c4eecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Model is loading. Job is running.

**Summary:**

1. **Original command**: `python src/eval_spon_supplementary.py --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b --spon_checkpoint /root/distill_sparse_swiglu/checkpoints/spon_2048_s42/spon_biases.pt --gpu 0 --seq_len 2048`

2. **Crash cause confirmed**: `RuntimeError: Cannot send a request, as the client has been closed.` — triggered when `load_dataset("wikitext", ...)` tried to reach `huggingface.co` (network unreachable on the server). See `/tmp/eval_spon_supp.log`.

3. **Resubmitted command**: Same as above with `TRANSFORMERS_OFFLINE=1 HF_DATASETS_OFFLINE=1` added. Log at `~/runs/distill_sparse_swiglu/eval_spon_supp_retry.log`.

4. **New PID**: `123231`, tmux session `eval_spon_supp_retry`, cuda:0.

---
