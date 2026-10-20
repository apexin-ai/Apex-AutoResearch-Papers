# analysis c1 format diversity

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c1_format_diversity_20260517T055240_result.json`
- **Structured JSON:** [`fa2d2e8322beea3dc356.json`](../../sessions/fa/fa2d2e8322beea3dc356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

336/2000. Process running steadily at ~40 prompts/min. 

**Summary of current state:**

1. **C5 metrics (DONE)**:
   | Metric | Gen0 | Gen2 | Delta |
   |--------|------|------|-------|
   | opening_unique_ratio | 0.7532 | 0.4789 | -0.2743 |
   | opening_entropy | 12.43 | 11.68 | -0.75 |
   | near_duplicate_start_rate | 0.3827 | 0.7489 | +0.3662 |
   | per_response_ttr | 0.6828 | 0.6598 | -0.0230 |
   | trigram_repetition_rate | 0.1739 | 0.2576 | +0.0837 |

2. **C1 re-run (IN PROGRESS)**: 
   - Reason: original C1 data was overwritten by C5 baseline run (both used same `outputs/condition_0/` directory)
   - Running on GPU 0, PID 548879, currently gen_0 at 336/2000
   - Auto-completion: watcher script (PID 549365) will compute and save C1 metrics when done
   - ETA: ~17:00-17:30 CST

3. **Output locations**:
   - Interim report: `artifacts/c1_vs_c5_format_analysis.md`
   - Server JSON: `/root/autodl-tmp/carr/analysis/c1_c5_format_diversity.json`
   - C1 generation log: `/root/autodl-tmp/carr/outputs_lora_k4_curated/run.log`

Once C1 finishes, the watcher will update `c1_c5_format_diversity.json` and I can update the final report table. Want me to check back in ~3 hours, or should I continue monitoring here?

---
