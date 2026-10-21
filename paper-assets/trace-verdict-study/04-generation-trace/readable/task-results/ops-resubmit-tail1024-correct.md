# ops resubmit tail1024 correct

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit_tail1024_correct_20260518T032345_result.json`
- **Structured JSON:** [`32960dd44efe9443fd24.json`](../../sessions/32/32960dd44efe9443fd24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the issue — previous attempt used wrong script path. Here's the analysis from the successful runs:

**From tail-512 log:**
- `Condition: full_trace_tail_512`
- `Model: /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`
- `Output: /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail512_seed42`

**From tail-256 log:**
- `Condition: full_trace_tail_256`
- Same model/output pattern

**From `--help`:**
- `--condition` accepts `full_trace_tail_1024` directly (it's an enum value)
- No separate `--max_trace_tokens` or `--truncation_side` needed for the named conditions
- `--gradient_checkpointing` is available (required per C002 for 13B)

**Correct tail-1024 command:**

```bash
cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py \
  --condition full_trace_tail_1024 \
  --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf \
  --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42 \
  --seed 42 \
  --wandb_project trace-verdict-study \
  --wandb_run_name codellama13b_full_trace_tail1024_seed42 \
  --gradient_checkpointing
```

**In `bash -c` format for `submit_training_job`:**

```bash
bash -c 'cd /root/trace-verdict-study && /root/miniconda3/bin/python train/train_sft.py --condition full_trace_tail_1024 --model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf --output_dir /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42 --seed 42 --wandb_project trace-verdict-study --wandb_run_name codellama13b_full_trace_tail1024_seed42 --gradient_checkpointing'
```

Previous failure was simply wrong script path (`train.py` instead of `train/train_sft.py`). Old tmux session is cleaned.

---
