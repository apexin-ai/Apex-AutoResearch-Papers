# code r7 multiseed lr stability

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_multiseed_lr_stability_20260518T045424_result.json`
- **Structured JSON:** [`e42656ed5329a79c93f5.json`](../../sessions/e4/e42656ed5329a79c93f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/exp_r7_multiseed_lr/results.json`. Here's the summary:

## Summary Table

| Model   | Precision (mean±std) | Bal_Acc (mean±std) | FPR (mean±std) |
|---------|---------------------|-------------------|----------------|
| R1-8B   | 0.5897±0.0716       | 0.7562±0.0276     | 0.1540±0.0260  |
| OT-7B   | 0.4207±0.0336       | 0.6330±0.0231     | 0.1571±0.0208  |
| QwQ-32B | 0.6511±0.0993       | 0.7310±0.0277     | 0.1329±0.0324  |
| R1-32B  | 0.5943±0.1280       | 0.6922±0.0556     | 0.2069±0.1445  |

## Per-seed detail: R1-32B (20 test traces)

| Seed | Precision | Bal_Acc | FPR    |
|------|-----------|---------|--------|
| 0    | 0.4412    | 0.5940  | 0.4827 |
| 1    | 0.7500    | 0.7482  | 0.1086 |
| 2    | 0.6852    | 0.6702  | 0.1109 |
| 3    | 0.6517    | 0.7331  | 0.1109 |
| 4    | 0.4436    | 0.7154  | 0.2212 |

## Per-seed detail: R1-8B (42 test traces)

| Seed | Precision | Bal_Acc | FPR    |
|------|-----------|---------|--------|
| 0    | 0.5707    | 0.7697  | 0.1729 |
| 1    | 0.6277    | 0.7953  | 0.1620 |
| 2    | 0.7065    | 0.7404  | 0.1027 |
| 3    | 0.5438    | 0.7136  | 0.1619 |
| 4    | 0.5000    | 0.7619  | 0.1705 |

## Per-seed detail: OT-7B (46 test traces)

| Seed | Precision | Bal_Acc | FPR    |
|------|-----------|---------|--------|
| 0    | 0.3911    | 0.6660  | 0.1533 |
| 1    | 0.4842    | 0.6419  | 0.1269 |
| 2    | 0.4228    | 0.5947  | 0.1756 |
| 3    | 0.3957    | 0.6349  | 0.1845 |
| 4    | 0.4098    | 0.6275  | 0.1454 |

## Per-seed detail: QwQ-32B (19 test traces)

| Seed | Precision | Bal_Acc | FPR    |
|------|-----------|---------|--------|
| 0    | 0.5035    | 0.7303  | 0.1655 |
| 1    | 0.5816    | 0.7067  | 0.1540 |
| 2    | 0.6565    | 0.7016  | 0.1578 |
| 3    | 0.7455    | 0.7793  | 0.0975 |
| 4    | 0.7682    | 0.7369  | 0.0896 |

**WARNING: R1-32B precision std = 12.80pp > 5pp.** Seed 0 is the outlier with FPR=0.48 (nearly half of negative steps misclassified). This is driven by only 20 test traces, where one bad split can land several ambiguous traces in the test set. R1-32B FPR std is also very high at 14.45pp. QwQ-32B precision std (9.93pp) is also above 5pp, same small-n issue (19 test traces). The larger models (R1-8B, OT-7B) with 42-46 test traces show much tighter variance.

---
