# code r7 k ablation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_k_ablation_20260518T043423_result.json`
- **Structured JSON:** [`87c11ea1d914804e4716.json`](../../sessions/87/87c11ea1d914804e4716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/exp_r7_k_ablation/results.json`. Summary:

| Model | Step Prec | Step BalAcc | Step FPR | K | Coverage | Lead Time | Safe FPR |
|-------|-----------|-------------|----------|---|----------|-----------|----------|
| **R1-8B (L14)** | 0.693 | 0.778 | 0.097 | 1 | 1.000 | 8.67 | 1.000 |
| | | | | 3 | 0.744 | 0.03 | 0.814 |
| | | | | 5 | 0.465 | -2.00 | 0.627 |
| | | | | 7 | 0.349 | -1.20 | 0.390 |
| | | | | 10 | 0.140 | -11.50 | 0.220 |
| **OT-7B (L16)** | 0.425 | 0.680 | 0.153 | 1 | 1.000 | 30.57 | 0.921 |
| | | | | 3 | 0.787 | 9.22 | 0.413 |
| | | | | 5 | 0.511 | 3.00 | 0.190 |
| | | | | 7 | 0.298 | 7.14 | 0.159 |
| | | | | 10 | 0.213 | 4.40 | 0.079 |
| **QwQ-32B (L60)** | 0.658 | 0.747 | 0.127 | 1 | 1.000 | 9.32 | 1.000 |
| | | | | 3 | 0.947 | 2.44 | 0.775 |
| | | | | 5 | 0.789 | 0.40 | 0.650 |
| | | | | 7 | 0.579 | -2.82 | 0.350 |
| | | | | 10 | 0.316 | -11.50 | 0.250 |
| **R1-32B (L63)** | 0.590 | 0.755 | 0.284 | 1 | 1.000 | 8.60 | 0.986 |
| | | | | 3 | 0.900 | 4.28 | 0.775 |
| | | | | 5 | 0.650 | 2.92 | 0.465 |
| | | | | 7 | 0.450 | 3.67 | 0.310 |
| | | | | 10 | 0.350 | 3.86 | 0.169 |

Key observations:
- **K=1** gives 100% coverage but near-100% safe trace FPR (useless for deployment)
- **K=3** is a reasonable balance for most models (74-95% coverage, 41-81% safe FPR)
- **K=5** yields the best coverage/FPR tradeoff for OT-7B (51% coverage, 19% safe FPR)
- **Lead time** goes negative at higher K, meaning detection happens after commitment point
- **R1-32B** has the shortest traces (mean 27.2 steps), but K=10 still works (7/20 detected)
- R1-8B safe traces (59) confirmed to be genuinely safe via dataset verification

---
