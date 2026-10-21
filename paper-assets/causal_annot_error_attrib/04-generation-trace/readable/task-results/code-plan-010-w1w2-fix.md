# code plan 010 w1w2 fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_w1w2_fix_20260520T235049_result.json`
- **Structured JSON:** [`5935539c9fb5cbd8649c.json`](../../sessions/59/5935539c9fb5cbd8649c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

47/47 pass. Summary:

**W1 (IV Wald fix)**: Added `_plim_iv()` and IV-specific precomputation (RF, FS) to `bias.py`. IV topology now uses Wald estimator `RF / (C @ FS)[1]` instead of OLS. Near-permutation C produces -762.8% bias with sign flip, matching the paper's finding.

**W2 (Correction tests)**: Added 12 new tests in two classes:
- `TestIVWald` (4 tests): identity zero bias, near-permutation sign flip, ASV sign_flip finite, symmetric_high moderate bias
- `TestCorrectionMethods` (8 tests): 5 smoke tests, PPI++ bias reduction >50%, DSL catastrophic on mbias, end-to-end pipeline

---
