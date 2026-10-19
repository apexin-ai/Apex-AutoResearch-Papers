# code r8 exact permutation test

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r8_exact_permutation_test_20260518T064914_result.json`
- **Structured JSON:** [`56824b534112c7b6f7e7.json`](../../sessions/56/56824b534112c7b6f7e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved with full precision. Here are the results:

**QwQ-32B** (n=19, L60, W=3, 524,288 permutations):

| Metric    | HS mean | Text mean | Δ       | Exact p-value | Significant (α=0.05) |
|-----------|---------|-----------|---------|---------------|----------------------|
| bal_acc   | 0.8069  | 0.6612    | +0.1458 | 0.000008      | YES                  |
| precision | 0.7255  | 0.4704    | +0.2552 | 0.000023      | YES                  |
| FPR       | 0.1029  | 0.2109    | +0.1079 | 0.002335      | YES                  |

**R1-32B** (n=20, L63, W=1, 1,048,576 permutations):

| Metric    | HS mean | Text mean | Δ       | Exact p-value | Significant (α=0.05) |
|-----------|---------|-----------|---------|---------------|----------------------|
| bal_acc   | 0.8286  | 0.6388    | +0.1898 | 0.000147      | YES                  |
| precision | 0.6028  | 0.4483    | +0.1545 | 0.000122      | YES                  |
| FPR       | 0.2335  | 0.3804    | +0.1468 | 0.007950      | YES                  |

All 6 tests significant at α=0.05. Exact p-values are consistent with the bootstrap p-values from the earlier 10k-resample run. Results saved to `artifacts/exp_r8_exact_permutation/results.json`.

---
