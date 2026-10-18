# code exp 007 double correction fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-007-double-correction-fix_20260520T223135_result.json`
- **Structured JSON:** [`7869c5700166d7bd6be9.json`](../../sessions/78/7869c5700166d7bd6be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results look correct:

- **DGP A** (covariate-only): `ec_hte_ppci` = `ec_hte` exactly (rectifier ≈ 0, no double correction)
- **DGP C** (both errors): `ec_hte_ppci` substantially improves over `ec_hte` by correcting the remaining outcome error

Changes made:
1. **`method_ec_hte_ppci`** (line 420-446): Rectifier now uses `gold_bool` (true Z grouping) for both `tau_gold` and `tau_hat_gold_true_z`, so it only captures outcome error. Previously it used Z_hat grouping for `tau_hat_gold`, causing double correction of covariate error.
2. **`method_ppci` docstring** (line 325-338): Clarified that the PPCI rectifier captures all systematic error (covariate + outcome), complementary to EC-HTE's structured covariate-only correction.
3. **File header** (line 7-10): Documented the fix.

---
