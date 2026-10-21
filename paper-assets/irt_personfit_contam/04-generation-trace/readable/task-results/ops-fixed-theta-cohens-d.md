# ops fixed theta cohens d

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fixed-theta-cohens-d_20260522T192345_result.json`
- **Structured JSON:** [`d26b00346596e8c904a8.json`](../../sessions/d2/d26b00346596e8c904a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All computations verified and completed. Results match all three known reference values exactly.

```
FIXED-θ RESULTS (θ = -0.1022):

Already known:
- 15% s1 (seed42):  d_fixed = 4.770
- 15% s2 (seed123): d_fixed = 7.787
- 50% s1 (seed42):  d_fixed = 14.521

Newly computed:
- 15% s3 (seed456): lz_fixed = 11.990, d_fixed = 7.994,  CI = [6.680, 13.400]
- 25% s1 (seed42):  lz_fixed = 10.229, d_fixed = 4.957,  CI = [4.126,  8.119]
- 25% s2 (seed123): lz_fixed = 10.470, d_fixed = 5.373,  CI = [4.475,  8.832]
- 25% s3 (seed456): lz_fixed = 11.611, d_fixed = 7.339,  CI = [6.135, 12.261]
- 50% s2 (seed123): lz_fixed = 14.687, d_fixed = 12.641, CI = [10.537, 21.462]
- 50% s3 (seed456): SKIPPED — no results file yet

CLEAN FIXED-θ BASELINE:
- n=10, mean=7.3522, std=0.5802
- individual lz_fixed values: [8.114, 6.459, 7.947, 7.407, 7.620, 6.946, 7.777, 7.682, 7.032, 6.537]
```

Notes:
- d_fixed and d\*_fixed are numerically identical (the Snijders correction factor is the same ratio for lz and lz\*, so Cohen's d cancels it out).
- contam_50_s3 has a checkpoint on the server but no eval results file — needs GPU eval after training/current job finishes.
- All results saved to `/root/autodl-tmp/ctrl_contam_pilot/results/theta_fixed_all_seeds.json`.

---
