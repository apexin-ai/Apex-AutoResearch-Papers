# code mvp protocol fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-protocol-fix_20260513T183157_result.json`
- **Structured JSON:** [`18f1d1a76e6380b2f64d.json`](../../sessions/18/18f1d1a76e6380b2f64d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Summary of what was done:

**Bug #1 (II formula)**: Changed from `-ppl_both + ppl_attn + ppl_kv - ppl_dense` to `R_both - R_attn - R_kv + 1` where `R_x = ppl_x / ppl_dense`. Added `r_attn`, `r_kv`, `r_both` fields to `InteractionResult`. Updated all comments.

**Bug #2 (token_indices)**: Added `@property token_indices` to `Phase` dataclass in `phase_segmentation.py:35-37`, returns `list(range(self.start, self.end))`.

**Bug #3 (run_profiling.py)**: Complete rewrite — now runs full MVP pipeline: stratified sampling → generation → phase segmentation → per-phase × per-level (0.3, 0.5) × 4-condition perplexity → II computation → bootstrap 1000 resamples → CI → pass/fail (OR logic: CI non-overlap OR sign reversal) → structured JSON output.

**Protocol #1-6**: All implemented:
- Two sparsity levels (0.3, 0.5), unified `sparsity_level` parameter
- Bootstrap with 1000 resamples, percentile CI, min-segment warning
- OR-logic pass/fail (CI non-overlap or sign reversal across phase pairs)
- `stratified_sample_math500` in new `pacs/utils/data_utils.py`
- JSON output matches specified schema exactly
- Directory structure preserved

**No intermediate files** to delete (`_project/intermediate/` doesn't exist).

---
