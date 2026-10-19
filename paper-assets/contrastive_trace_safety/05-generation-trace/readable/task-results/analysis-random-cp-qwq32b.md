# analysis random cp qwq32b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random_cp_qwq32b_20260519T115416_result.json`
- **Structured JSON:** [`d44da201790b6ca1b860.json`](../../sessions/d4/d44da201790b6ca1b860.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 output files saved. Here are the results:

## QwQ-32B Random-CP Control Results

**Real-CP Baseline (confirms disagreement):**
| Metric | Best Layer |
|--------|-----------|
| CR-composite | **L4** (shallow) |
| Precision | **L63** (deep) |
| FPR | **L62** (deep) |
| BA | L63 |
| Crossing rate | L4 |
| **Disagreement gap** | **59 layers** |

**Random-CP (10 repeats, seeds 42-51):**
| Metric | Mean L | Std | Shallow (L<=10) | Deep (L>=50) |
|--------|--------|-----|-----------------|--------------|
| bal_acc | 33.3 | 20.3 | 20% | 40% |
| precision | 33.8 | 19.8 | 20% | 20% |
| pre_cp_fpr | 36.4 | 17.0 | 10% | 10% |
| crossing_rate | 3.4 | 2.6 | **100%** | 0% |
| cr_composite | 13.1 | 18.1 | **80%** | 10% |

**Metric disagreement replicates: False**

Key findings:
- With real CPs, CR-composite selects L4 (shallow) while precision/FPR select L62-63 (deep), gap=59 layers
- With random CPs, precision/FPR scatter across all layers (only 10-20% deep), not consistently selecting deep layers
- CR-composite still prefers shallow layers with random CPs (80%), driven by `crossing_rate` which always selects L0-L7
- The critical asymmetry is that **threshold-based metrics lose their deep-layer preference** under random CPs (15% vs 100% with real CPs)
- This supports the claim that the metric disagreement requires real CP labels and reflects genuine behavioral structure, not a geometry artifact

---
