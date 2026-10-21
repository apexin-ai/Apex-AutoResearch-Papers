# code exp 001 hyperprior v2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001-hyperprior-v2_20260520T221457_result.json`
- **Structured JSON:** [`53b24effba2d050e0554.json`](../../sessions/53/53b24effba2d050e0554.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete and verified:

1. **Added K=4/moderate/n=100 config** alongside the existing K=2/moderate/n=250
2. **Imported `invert_mixing_safe`** from `exp001_hb_synthetic` — K=4 uses it (condition number guard), K=2 keeps the original `invert_mixing`
3. **CONFIGS list** drives both configs through the same loop: 2 configs × 3 scales × n_mc = 600 total runs at full scale
4. **CSV output** includes `config` column
5. **Summary tables** print separately per config group

Dry-run (2 MC per config, 12 runs total) completed in 23s with no errors.

---
