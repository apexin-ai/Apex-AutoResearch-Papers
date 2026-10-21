# code binoculars scoring

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_binoculars_scoring_20260518T104613_result.json`
- **Structured JSON:** [`de1de4ce39bd762c6f4a.json`](../../sessions/de/de1de4ce39bd762c6f4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8,000/371,499 at 31.9 samples/s. ETA ~190 min. Running steadily. I'll stop polling and let it run. Let me provide a status summary now and check final results when it completes.

**Status Summary:**
- **Method:** Llama-3.2-3B perplexity scoring (local model, no download needed)
- **Server:** westd-41312, GPU1 (NVIDIA RTX PRO 6000 Blackwell), 35GB VRAM in use
- **Speed:** ~32 samples/s
- **Progress:** 8,000/371,499 (2.2%)
- **ETA:** ~190 minutes (~3.2 hours), expected completion around 22:10 UTC
- **Early results (first 6K samples):**
  - Real text (depth=0): median PPL = 11.4
  - Synthetic text (depth=1): median PPL = 5.0
  - Clear separation — synthetic text has 2.3x lower perplexity (more predictable to Llama-3.2-3B)
- **Output file:** `/root/autodl-tmp/provenance_weight_training/data/scored_data_gpt2ppl.jsonl`
- **Checkpoint:** Every 10K samples, auto-resumes if interrupted
- **Script:** `/root/autodl-tmp/provenance_weight_training/scoring/score_gpt2_ppl.py`

The script will automatically compute correlation with q_scores, classification accuracy at various thresholds, and the optimal threshold when it finishes.

To check progress: `tail -1 /root/autodl-tmp/provenance_weight_training/scoring/gpt2ppl.log`

---
