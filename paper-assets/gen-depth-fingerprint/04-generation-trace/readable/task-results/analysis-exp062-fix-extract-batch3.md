# analysis exp062 fix extract batch3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062_fix_extract_batch3_20260521T135307_result.json`
- **Structured JSON:** [`d50febe71ed782f3aa83.json`](../../sessions/d5/d50febe71ed782f3aa83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done:

1. **Killed PID 357040** — confirmed dead (SIGTERM succeeded)
2. **Extracted features** for 3 new combos (pythia-1b topk, llama-3.2-3b greedy, mistral-7b-v0.3 greedy) — all completed in ~45 seconds total on GPU 3
3. **Computed Cohen's d** for all 9 combos, written to:
   - `artifacts/_project/analysis/decoding_cohens_d_all.txt` — full table with Shape/Drift pass criteria
   - `artifacts/_project/analysis/exp062_cohens_d_summary.txt` — one-line-per-combo summary

**Key results:**
- Greedy: **6/6 pass both** Shape and Drift — the depth fingerprint is fully preserved
- Top-k: **0/3 pass Shape**, only **1/3 pass Drift** (OLMo-2-1B is the exception)
- Strongest signal: LLaMA-3.2-3B greedy (d_mean=1.46, d_ttr=1.27)
- Weakest: Pythia-2.8B top-k (d_mean=0.70, d_ttr=0.41)

---
