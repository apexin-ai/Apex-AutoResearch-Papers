# audit final data check

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final_data_check_20260524T043115_result.json`
- **Structured JSON:** [`4bb4e124e201fed5cf26.json`](../../sessions/4b/4bb4e124e201fed5cf26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All audit agents have completed. The Experiments agent confirmed all numbers match — no additional issues beyond the 3 already fixed.

The audit is complete. Here's the final summary:

---

## Audit Complete: 38 numbers verified, 3 mismatches fixed

### Fixes applied

| # | File | Line | Issue | Fix |
|---|------|------|-------|-----|
| 1 | `conclusion.tex` | 8 | "deviation grows with K (0.003 at K=3, 0.060 at K=7)" — reversed direction, wrong values | → "reaches 0.056 for exposure but empirically decreases with K" |
| 2 | `appendix_proofs.tex` | 315 | "exclusively under p_max/p_min > 300" — 4/5 counterexamples have ratio < 50 | → "predominantly under class imbalance" |
| 3 | `appendix_proofs.tex` | 795 | Near-permutation 35.3% — source is 35.38%, rounds to 35.4% | → 35.4% |

### Match summary

- **Abstract**: 6/6 match
- **Introduction**: 9/9 match
- **Method**: 5/5 match
- **Experiments**: 18/18 match (including Table 1 cells)
- **Limitations**: 3/3 match (after fix)
- **Appendix**: 5/5 match (after fixes)
- **Cross-location**: 18/18 consistent

**Compilation: clean, no errors.**

---
