# analysis exp 022 3seed analysis

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_022_3seed_analysis_20260516T105321_result.json`
- **Structured JSON:** [`5d3c718317dfb4fbf95e.json`](../../sessions/5d/5d3c718317dfb4fbf95e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 artifacts registered. Here's the summary:

## exp-022 3-Seed (42, 123, 789) Analysis Results — SciERC NER N=8

### Spearman ρ (3-seed mean ± std)
| Signal | Mean | Std |
|--------|------|-----|
| **VC** | **0.4144** | 0.0357 |
| **SJ** | **0.3772** | 0.0151 |
| EM | 0.3039 | 0.0095 |
| FK | 0.2545 | 0.0177 |
| LP | 0.2155 | 0.0161 |

### AUROC (3-seed mean ± std)
| Signal | Mean | Std |
|--------|------|-----|
| **VC** | **0.7064** | 0.0173 |
| **SJ** | **0.6842** | 0.0111 |
| EM | 0.6512 | 0.0073 |
| FK | 0.6158 | 0.0140 |
| LP | 0.6124 | 0.0008 |

### Selection macro F1
| Method | Mean ± σ | ΔF1 vs Greedy |
|--------|----------|---------------|
| Greedy | 0.6469 ± 0.0037 | — |
| **LP** | **0.6472 ± 0.0033** | **+0.0003** |
| FK | 0.6442 ± 0.0030 | -0.0027 |
| SJ | 0.6434 ± 0.0050 | -0.0035 |
| EM | 0.6383 ± 0.0022 | -0.0086 |
| VC | 0.6218 ± 0.0033 | -0.0251 |
| Oracle | 0.7816 ± 0.0064 | +0.1347 |

### Key Fisher Tests
- **SJ ρ > LP ρ**: All 3 seeds consistent (diffs: 0.15–0.18). Structural beats surface.
- **SJ ρ > FK ρ**: All 3 seeds consistent (diffs: 0.09–0.15).
- **EM AUROC > all others**: False. EM < SJ and EM < VC consistently.

### 2-Seed vs 3-Seed
- ρ CIs narrowed for LP, SJ, EM (3/5 signals)
- Selection F1 CIs narrowed for LP, VC (2/5 signals)
- Conclusions unchanged: LP selection ≈ greedy, VC consistently worst at sample selection despite best ρ/AUROC

Output at: `/root/autodl-tmp/struct_self_consist_ie/output/exp_022_3seed_analysis/`

---
