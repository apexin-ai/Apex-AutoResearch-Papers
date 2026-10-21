# code stratified irt a32 fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stratified-irt-a32-fix_20260516T054855_result.json`
- **Structured JSON:** [`87268ef7df569f8ea395.json`](../../sessions/87/87268ef7df569f8ea395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Local copy updated. Summary of changes in `exp006/run_irt_calibration.py`:

**1. Regex** (line 43-45): 
```
_d(\d+)(?:_(?:v\d+|a(\d+)))?_s(\d+)(?:_a(\d+))?(_para)?(_aligned)?(?:_v\d+)?$
```
Now handles `_a\d+` before seed (`_d100_a32_s123`) and after seed (`_d000_s42_a32`).

**2. `parse_model_dir_name`** (line 62): Added `has_alpha` field. Group indices updated (1→dosage, 3→seed, 5→para, 6→aligned).

**3. Dedup logic** (lines 138-149): After collecting models, groups by `(model_name, dosage, seed, is_para)`. If both `_a32_` and non-alpha dirs exist for the same key, keeps only the `_a32_` version.

**Dry-run results:**
- 3B: 8 models, `_a32_` dirs correctly recognized and preferred (replaced 3 non-alpha duplicates: `d000_v2_s42`, `d005_s42`, `d100_v2_s123`)
- 0.5B: 8 models, unchanged
- 1.5B: 8 models, unchanged
- Unrecognized dirs (13) are all expected: Instruct, base_pretrained, raw, DEPRECATED, gsm8k_rerun, `d025_v2_aligned` (no seed)

---
