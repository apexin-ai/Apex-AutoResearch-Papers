# diagnose exp012 llama 8b r2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_llama_8b_r2_20260515T194136_result.json`
- **Structured JSON:** [`2acb7fa69ae24e8004be.json`](../../sessions/2a/2acb7fa69ae24e8004be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**The process is still running.** It has NOT exited.

Current status (server time 03:43 CST):
- **exp1 (Count Baseline)**: Completed at 03:39. "Extraction done in 3619.1s, 94000 result entries". Predictions saved to `artifacts/exp012/predictions_fewnerd_exp1_llama-3.1-8b-instruct.json` (52MB).
- **exp2 (Confusability Controlled)**: Started at 03:39:20, currently running. PID 319316. So far completed 3 of many batches (count_6/low_bcs, count_6/high_bcs, count_6/random/0). Still processing.
- **No errors/tracebacks** in the log.
- **tmux session** `exp012_llama_8b_r2` is alive.

Key metrics from exp1 (all batches got 1000 outputs each):
- exact_F1 = 0.0000 across all conditions (all counts 1-64)
- text_match_F1 ranges: 0.06~0.36 (increases with count)
- BCS correlation visible: count_1→BCS=0.0, count_2→BCS~0.7, count_6→BCS~0.9, count_44/64→BCS~0.97

**No action taken** — registry not updated, cron not deleted. The experiment needs more time for exp2 to finish. Based on exp1's runtime (~1 hour for 94 batches), exp2 should have fewer batches and finish within ~30-60 minutes.

---
