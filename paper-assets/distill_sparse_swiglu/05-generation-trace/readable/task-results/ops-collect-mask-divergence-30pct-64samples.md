# ops collect mask divergence 30pct 64samples

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-mask-divergence-30pct-64samples_20260519T122029_result.json`
- **Structured JSON:** [`3da0624433e07fbbff1d.json`](../../sessions/3d/3da0624433e07fbbff1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both GPUs are running Qwen-14B benchmark evals. No mask divergence computation is running, and 64-sample computation can't start now.

However, 32-sample results already exist for both models. Here are the results:

**LLaMA-8B 30% Sparsity Mask Divergence (32 samples):**
- Mean Jaccard Distance: 0.3939 (39.39%)
- Min: 0.3528 (layer 14)
- Max: 0.4818 (layer 0)
- Std: 0.0314

**Qwen-14B 30% Sparsity Mask Divergence (32 samples):**
- Mean Jaccard Distance: 0.4016 (40.16%)
- Min: 0.0627 (layer 4) — anomalously low
- Max: 0.4460 (layer 11)
- Std: 0.0756

**Comparison with 50% reference (64 samples):**
- 50%: Mean=0.6824 → 30% LLaMA: 0.3939, 30% Qwen: 0.4016
- As expected, 30% is substantially lower than 50% (~42% relative drop)

**Status of 64-sample run:** Cannot run now — both cuda:0 and cuda:1 are occupied by `benchmark_eval.py` jobs (qwen14b_kl30_s456_eval_v2 and qwen14b_kl30_s123_eval_v4, both running ~1hr). The script supports `--calib_samples 64` but needs a free GPU. The 32→64 sample increase would reduce variance but likely won't shift means significantly.

---
