# fix scaling script 8b data

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_scaling-script-8b-data_20260519T172758_result.json`
- **Structured JSON:** [`df14ee00be678e2654fc.json`](../../sessions/df/df14ee00be678e2654fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script runs cleanly. Here's the complete diff of all 12 corrections:

**8B FT SciERC** (5 fixes):
| Metric | Old | New | Source |
|---|---|---|---|
| `lp_rho` | 0.22 | **0.205** | tab:scale_comparison |
| `sj_rho` | 0.35 | **0.360** | tab:scale_comparison |
| `vc_rho` | 0.45 | **0.379** | tab:scale_comparison |
| `degen` | 18.5 | **17.8** | tab:scale_comparison, tab:degeneracy |
| `construction_lp_delta` | 1.67 | **1.02** | tab:entity_construction (multi-seed mean) |

**8B FT FewNERD** (3 fixes):
| Metric | Old | New | Source |
|---|---|---|---|
| `lp_rho` | 0.62 | **0.220** | tab:scale_comparison (was 3x inflated) |
| `degen` | 12.7 | **13.8** | tab:scale_comparison |
| `construction_lp_delta` | 1.38 | **1.40** | tab:entity_construction (multi-seed mean) |

**8B FT CoNLL** (4 fixes):
| Metric | Old | New | Source |
|---|---|---|---|
| `lp_rho` | 0.29 | **0.302** | tab:scale_comparison |
| `degen` | 50.3 | **48.4** | tab:scale_comparison |
| `construction_lp_delta` | +0.10 | **-0.39** | tab:entity_construction (sign flip) |
| `greedy_f1` | 0.907 | **0.908** | tab:scale_comparison |

**Verified correct** (no changes): all 72B ZS values (9 data points × 3 datasets), 4B FT SciERC degen=10.4.

---
