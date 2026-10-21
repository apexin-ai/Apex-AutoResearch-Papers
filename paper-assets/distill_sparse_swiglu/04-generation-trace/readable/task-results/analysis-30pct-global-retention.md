# analysis 30pct global retention

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_30pct_global_retention_20260517T051429_result.json`
- **Structured JSON:** [`f18aba5d09dbccf5a63f.json`](../../sessions/f1/f18aba5d09dbccf5a63f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Server `westd-34887` is unreachable (connection refused on port 34887). This is likely a temporary cloud provider issue.

**What I've done:**
- Analyzed the global top-k implementation from `gsm8k_gen_compare.py` — the key function `global_topk_masks()` normalizes each layer's scores by per-layer mean, then applies a single global threshold
- Wrote the full analysis script at `artifacts/global_30pct_retention_analysis_script.py`

**What the script does:**
1. Loads LLaMA-3.1-8B + predictor (`kl_sparsity30_s42_v3`)
2. Runs 50 C4 calibration samples through the predictor
3. Computes per-layer importance scores (`|activation| × hard_mask`, averaged over tokens)
4. Applies `global_topk_masks()` with per-layer mean normalization at 30% sparsity
5. Reports per-layer retention ratio and identifies starved layers (L12-L20 knowledge region)
6. Includes dry-run validation with 2 samples first
7. Saves full results to `/root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis.json`

**Once the server is back**, run:
```bash
CUDA_VISIBLE_DEVICES=0 python -u /root/distill_sparse_swiglu/artifacts/global_30pct_retention_analysis_script.py
```

Or I can upload it via ssh_execute. Want me to keep retrying the connection, or should we wait and come back to this later?

---
