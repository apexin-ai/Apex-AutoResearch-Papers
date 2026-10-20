# code analyze mvp d002

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analyze-mvp-d002_20260515T122754_result.json`
- **Structured JSON:** [`2a66aadc8097592649eb.json`](../../sessions/2a/2a66aadc8097592649eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary of findings and changes:

**Finding**: **Situation A** — `analyze_results.py` has superseded `analyze_mvp.py` for judgment. No pipeline runner references either script; both are standalone CLI tools. `analyze_results.py` already has D002-compliant per-task mean ρ judgment. `analyze_mvp.py` still uses pooled ρ in its `compute_verdict`.

**Changes made**:

1. **`scripts/analyze_mvp.py`** — Added 3-line deprecation notice at top:
   ```
   # DEPRECATED: This script has been superseded by analyze_results.py
   # which implements D002-compliant per-task mean ρ judgment.
   # Do not use this script for MVP verdict.
   ```

2. **`scripts/train_probes.py` `save_results`** (line 606-609) — best_layer selection now uses `per_task_mean_rho` (with fallback to `spearman_rho` for backward compat). Also writes `best_pooled_rho` to summary.json for reference.

3. All three scripts pass syntax check; `analyze_mvp.py --mock` dry-run completes successfully.

---
