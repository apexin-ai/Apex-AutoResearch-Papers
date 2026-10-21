# exp r1 8b random cp control

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_r1_8b_random_cp_control_20260521T064711_result.json`
- **Structured JSON:** [`e932b7d89b19e78a4f56.json`](../../sessions/e9/e932b7d89b19e78a4f56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

R1-8B Random-CP Control experiment complete. Here are the results:

**Real-CP Baseline (ground truth labels):**
| Metric | Best Layer |
|--------|-----------|
| CR-composite | **L0** (shallow) |
| Crossing Rate | **L0** (shallow) |
| Balanced Accuracy | **L19** (deep) |
| Precision | **L23** (deep) |
| FPR | **L13** (mid-deep) |
| **Disagreement gap** | **23 layers** |

**Random-CP Control (10 repeats, seeds 42-51):**
| Metric | Mean Layer | Std | Shallow% | Deep% |
|--------|-----------|-----|----------|-------|
| bal_acc | 14.0 | 4.0 | 0% | 20% |
| precision | **0.0** | 0.0 | **100%** | 0% |
| pre_cp_fpr | **0.0** | 0.0 | **100%** | 0% |
| crossing_rate | 10.7 | 4.8 | 0% | 10% |
| cr_composite | 13.7 | 6.7 | **0%** | 30% |

**Key conclusion:** The metric disagreement pattern does **NOT** replicate with random CPs. With real labels, CR-composite selects L0 (shallow) while precision selects L23 (deep) — a 23-layer gap. With random labels, CR-composite never selects shallow (0% vs the real CP's L0), and precision/FPR collapse to L0. This confirms the shallow vs. deep disagreement requires real commitment point labels and reflects genuine model behavioral structure, not geometric bias.

Results saved to `artifacts/random_cp_control/r1_8b/` (report.txt, random_cp_summary.json) and registered as artifact `art_20260521_62443e`.

---
