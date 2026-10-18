# bugfix eval pruning audit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_eval_pruning_audit_20260517T071259_result.json`
- **Structured JSON:** [`bd08687359db6c2acf06.json`](../../sessions/bd/bd08687359db6c2acf06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full eval submitted (50 episodes × 10 tasks on `libero_object`).

## Summary

### Root Cause
`eval_success_rate_libero.py:221` — the hook guard `tokens.shape[1] != mask.shape[1]` always failed because:
- The connector is called **per-camera** inside `embed_image()`, producing `(B, 64, D)` per call
- The mask was computed for **all cameras concatenated**: `(B, 128)`
- `64 != 128` → hook returned original output unchanged → pruning never applied
- All modes (baseline, acis_prune, random_prune) produced identical results

### Fix
Replaced the dimension-match guard with an **offset-tracking approach**:
- The hook closure tracks a cumulative `offset` across per-camera connector calls
- Each call slices `mask[:, offset:offset+n]` to get the correct per-camera mask segment
- Offset advances by `n` tokens after each call
- Since a new hook closure is created per `predict_actions` call, offset resets automatically

### Files Fixed
- `eval_success_rate_libero.py` (primary)
- `eval_success_rate.py` (same bug)
- `eval_sim.py` (same bug)

### Sanity Check
Confirmed via AUDIT prints: hook fires twice per step (2 cameras), keeping ~64/128 total tokens (k_ratio=0.5). Per-camera splits vary (e.g. 38/64 + 26/64 = 64/128).

### Eval Status
`eval_stage1only_object_v2_fixed` running on GPU 0 (PID 140050).

---
