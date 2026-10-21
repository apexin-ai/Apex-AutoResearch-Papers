# code nli label fix critical

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli-label-fix-critical_20260518T204711_result.json`
- **Structured JSON:** [`d5e6eeda15f9f71385ff.json`](../../sessions/d5/d5e6eeda15f9f71385ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Good. Both `sys` and `Path` are already imported (lines 24, 26 in the original). All changes applied correctly.

Summary:
- **Created** `artifacts/eval/nli_utils.py` — shared module with `get_entailment_idx`, `get_contradiction_idx`, `load_nli_model`, and `check_stance_consistency` that dynamically read label indices from `model.config.id2label`
- **Fixed** `artifacts/training/run_exp016_actadd_steering.py` — removed all hardcoded `probs[2]`/`probs[0]`, now uses dynamic indices via the shared utility functions. Updated `load_nli_model` return signature (4-tuple), `check_stance_consistency` signature (added idx params), `evaluate_alpha` signature, and all call sites in `main()`.

---
