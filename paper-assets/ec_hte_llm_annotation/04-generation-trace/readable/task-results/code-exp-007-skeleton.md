# code exp 007 skeleton

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-007-skeleton_20260520T212851_result.json`
- **Structured JSON:** [`5791d202684af80d6293.json`](../../sessions/57/5791d202684af80d6293.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run passed. Let me verify the two key properties.

**DSL vs Global-corrected produce different results** — confirmed. For example in extreme regime, k=2, subgroup 0, n_expert=50:
- DSL: bias_z0 = -0.1179, bias_z1 = 0.1345
- Global: bias_z0 = -0.0093, bias_z1 = -0.0591

**EC-HTE = DSL (placeholder)** — confirmed. Every row shows `dsl` and `ec_hte` have identical values (e.g. both -0.1179 / 0.1345 above), as expected since the HB estimator falls back to MLE.

File created at `exp007_ppci_dsl.py`. All 5 methods (oracle, naive, global_corrected, dsl, ec_hte) run across 3 regimes x 2 k-values x 4 expert budgets. PPCI returns NaN (placeholder). EC-HTE matches DSL until exp-001 HB code is integrated.

---
