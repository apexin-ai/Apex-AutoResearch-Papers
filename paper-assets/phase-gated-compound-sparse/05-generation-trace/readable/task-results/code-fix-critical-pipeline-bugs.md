# code fix critical pipeline bugs

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-critical-pipeline-bugs_20260513T185158_result.json`
- **Structured JSON:** [`50f35438324ea3121271.json`](../../sessions/50/50f35438324ea3121271.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 files pass syntax check. Here's a summary of the 5 fixes:

**C3 + C1 (OOM + wrong segmentation target)** — `run_profiling.py:219-262`
- Removed `output_attentions=True` from `model.generate()`
- Added a pre-hook on the last attention layer to enable attention output only for that layer
- Post-hook computes per-step sparsity via `compute_step_sparsity()` and strips the tensor immediately
- Segmentation now uses `segment_from_sparsity()` on the **generation trace** (not the prompt's prefill attention)
- Phase indices are offset by `prompt_len` to map into `full_ids` coordinates

**C2 (different masks per phase)** — `run_profiling.py:277-306`
- Mask generation (`_select_heads_to_mask`, `_select_kv_to_evict`) moved outside the phase loop
- Same masks are reused for all phases at a given (problem, sparsity level)

**M1 (redundant dense forward)** — `run_profiling.py:269-271`, `interaction_index.py:292-302`, `metrics.py:55-79`
- Dense forward done once per problem via `compute_dense_ce_losses()`
- Per-phase dense ppl computed from cached CE losses using `ppl_from_cached_losses()`
- Saves N_phases × N_levels - 1 dense forward passes per problem

**m4 (missing seed)** — `run_profiling.py:173`
- Added `torch.manual_seed(SEED)` before any torch random ops

---
