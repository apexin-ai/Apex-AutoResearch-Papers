# code gpt2 ppl scoring

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2_ppl_scoring_20260518T121124_result.json`
- **Structured JSON:** [`67c9a902fe1e13a2a2ae.json`](../../sessions/67/67c9a902fe1e13a2a2ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A scoring process is already running (PID 204274, started ~80 min ago, at 138K/371K, ETA ~122 min).

**Important finding:** The running script (`/root/autodl-tmp/provenance_weight_training/scoring/score_gpt2_ppl.py`) is **not using GPT-2-medium**. Despite the filename and field names, it's using **Llama-3.2-3B**:

```python
MODEL_PATH = "/root/autodl-tmp/provenance_weight_training/models/meta-llama/Llama-3.2-3B"
```

The output fields are misleadingly named `gpt2_ppl` and `gpt2_nll` but are actually Llama-3.2-3B perplexity scores.

Current status:
- **138,015 / 371,499** samples scored (37%)
- **31.9 samples/s**, ETA ~122 min
- Output: `/root/provenance_weight_training/data/scored_data_gpt2ppl.jsonl`
- Preserves all original fields + adds `gpt2_ppl`, `gpt2_nll`
- Includes analysis at the end (real vs synth stats, correlation with q_score, classification thresholds)

Do you want me to:
1. **Let it finish** - the Llama-3.2-3B PPL is arguably a better detection signal than GPT-2-medium (larger model = more discriminative), just rename the field later
2. **Also run GPT-2-medium in parallel** on a different GPU (GPU 0 has 89GB free) as a second signal, writing to a separate output file
3. **Kill the current run** and start fresh with actual GPT-2-medium

---
