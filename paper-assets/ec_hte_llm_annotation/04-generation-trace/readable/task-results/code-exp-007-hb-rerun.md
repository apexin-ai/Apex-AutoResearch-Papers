# code exp 007 hb rerun

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-007-hb-rerun_20260521T044900_result.json`
- **Structured JSON:** [`fdecb79efb024b8a5747.json`](../../sessions/fd/fdecb79efb024b8a5747.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process is alive, 28 seconds in, 98.9% CPU — running as expected.

**Summary:**
- Changed `estimate_cm_hb_gibbs` defaults from `n_iter=4000, n_warmup=2000` to `n_iter=1000, n_warmup=500` (line 209)
- Updated docstring and print statement to match
- N_MC confirmed at 100
- Dry-run passed
- `submit_training_job` failed (SSH key issue as warned), fell back to tmux
- Full run is active in tmux session `exp007hb` (PID 151996), outputting to `results/exp007_hb_run.log`
- Estimated runtime: ~9 hours

---
