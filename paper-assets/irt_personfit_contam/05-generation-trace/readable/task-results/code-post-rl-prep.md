# code post rl prep

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post-rl-prep_20260521T023630_result.json`
- **Structured JSON:** [`329c87ff076867abe698.json`](../../sessions/32/329c87ff076867abe698.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verified. Here's the dry-run report:

---

```
=== exp-post-rl dry-run report ===

Model: Qwen/Qwen3.5-9B (via ModelScope, /root/autodl-tmp/.hf_cache/Qwen/Qwen3___5-9B)

Data:
  SFT:  115 samples (100 Alpaca + 15 MMLU contamination @ 15% rate)
  GRPO: 100 prompts (MMLU questions with correctness reward)
  Seen items: 15, Total MMLU items: 100
  Path: /root/autodl-tmp/post_rl_contam/data/

SFT dry-run:  PASS
  - 4-bit QLoRA (r=16, alpha=32, q/k/v/o_proj)
  - 2 steps, 6.4s, loss=1.842
  - trainable params: 3,932,160 / 8,957,735,424 (0.04%)

GRPO dry-run: PASS
  - 4-bit base model + LoRA (r=16)
  - reward: mmlu_reward (mean=0.0, std=1.069)
  - 2 steps, 9.3s, max_completion_length=32
  - num_generations=4

Estimated GPU-hours:
  SFT full training:  ~2h (115 samples × 3 epochs, single GPU)
  GRPO full training: ~6h (100 prompts × 1 epoch × 4 generations, single GPU)
  Eval (base+SFT+GRPO): ~3h (3 stages × 14042 MMLU items)
  Total: ~11h per condition (single GPU)

  Full experiment (if testing multiple contamination levels): ~30-40h
  Within P2 budget of 40 GPU-hrs.

Ready for production: YES
Blockers: None

Server: westd-35694 (AutoDL), cuda:2 verified
Scripts: /root/autodl-tmp/post_rl_contam/{prepare_data,find_model,train_sft,train_grpo,eval_lz}.py
```

---
