# exp sft unpruned baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sft-unpruned-baseline_20260515T222828_result.json`
- **Structured JSON:** [`52365b4860ecf81ff8b7.json`](../../sessions/52/52365b4860ecf81ff8b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training launched and monitoring scheduled. Summary:

- **Experiment**: `sft_unpruned_baseline` — unpruned DeepSeek-R1-Distill-Qwen-7B SFT on GSM8K
- **Server**: westd-11672 cuda:1, tmux session `sft_unpruned`
- **Config**: 2 epochs, lr=2e-5, batch=1, grad_accum=8, max_seq_len=2048, seed=42, save_strategy=no
- **Progress**: step 14/1870, loss=1.234, token_accuracy=0.76, ~2.05s/step
- **ETA**: ~07:34 UTC (about 63 min total)
- **Disk cleanup**: deleted `sft_ablation/alpha_4.0/checkpoint-1870` (35G), freed disk from 96% → 82%
- **Registry**: status=RUNNING, cron set to check completion at 07:43 UTC

---
