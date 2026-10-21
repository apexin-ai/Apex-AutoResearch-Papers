# compute rd3 numbers and tables

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_rd3-numbers-and-tables_20260516T044646_result.json`
- **Structured JSON:** [`091e4a01fe5e3f134436.json`](../../sessions/09/091e4a01fe5e3f134436.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are complete. Here's a summary of changes:

### Computed on server
- **Per-generator binary F1**: Pythia-1B=0.795, Pythia-2.8B=0.723, OLMo-2-1B=0.677, Qwen3-0.6B=0.756, Qwen3-1.7B=0.748, Qwen3-8B=0.641 (avg=0.723, matching primary metric)
- **Downstream bootstrap**: random ppl CI [2.367, 2.367], depth-strat CI [2.387, 2.388], Δ=0.020, permutation p=0.25 (minimum for n=3), Cohen's d=40.2 (inflated due to near-zero seed variance)
- **Dataset**: 27,529 samples, 6 generators × 5 depths, counts decreasing at higher depths

### Files modified
1. **`results.tex`** — Table 1: added Binary F1 column with per-gen values + CIs, renamed "Held-out F1"→"3-class", updated caption with gen-0 caveat and "6-generator LOGO"; Table 2 caption: annotated "3-class"; Table 3 caption: honest framing (simplicity, not superiority); §4.4 downstream: added CIs + permutation p-value; cross-scale paragraph: updated to binary values; cross-ref paragraph: added self-referencing bias note for Qwen3-0.6B
2. **`appendix_downstream.tex`** — Added bootstrap CIs, permutation p-value, Cohen's d with caveat
3. **`appendix_dataset_stats.tex`** — New file with per-generator × per-depth sample count table
4. **`main.tex`** — Added `\input{appendix_dataset_stats}` section in appendix

---
