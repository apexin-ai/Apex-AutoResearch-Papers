# exp statistical hardening

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_statistical_hardening_20260518T064531_result.json`
- **Structured JSON:** [`3db34b907f1552e3373c.json`](../../sessions/3d/3db34b907f1552e3373c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 output files generated. Here's the complete summary:

## 统计加固结果汇总

### W1: Table 3 multi-seed (mean ± std)
| Dataset | Seeds | Greedy F1 | LP Sel F1 | LP Δ (pp) | Oracle F1 |
|---------|-------|-----------|-----------|-----------|-----------|
| SciERC N=8 | 3 | 0.6458±0.0020 | 0.6462±0.0034 | +0.04±0.48 | 0.8198±0.0029 |
| SciERC N=16 | 3 | 0.6441±0.0002 | 0.6488±0.0070 | +0.47±0.72 | 0.8370* |
| CoNLL N=8 | 1 | 0.9079 | 0.8974 | -1.05 | 0.9483 |
| Few-NERD N=8 | 1 | 0.7478 | 0.7614 | +1.36 | 0.8719 |

### W2: ICC + Permutation Test (SciERC 6 entity types)
- **ICC = -0.0038** (near zero, types are essentially independent)
- **Permutation p = 0.2471** (observed ρ = 0.6000, not significant with only 6 types)
- Effective df ≈ k-1 = 5

### I8: Paired Bootstrap (LP selection vs Greedy)
| Dataset | LP Δ (pp) | 95% CI | p-value |
|---------|-----------|--------|---------|
| SciERC N=8 | +0.61 | [-0.77, +1.99] | 0.1930 |
| CoNLL N=8 | -1.05 | [-1.45, -0.66] | 1.0000 |
| Few-NERD N=8 | **+1.36** | [+1.18, +1.53] | **0.0000** |

- SciERC: LP gain positive but not significant (p=0.19)
- CoNLL: LP hurts (high-accuracy regime, greedy already strong)
- Few-NERD: LP gain highly significant (p<0.001, large dataset)

### I9: Per-Type LP Heterogeneity (SciERC)
| Entity Type | n | LP Δ (pp) | Bootstrap p |
|------------|---|-----------|-------------|
| Material | 127 | +2.47 | 0.17 |
| Task | 196 | +0.97 | 0.32 |
| Metric | 54 | +0.62 | 0.46 |
| Method | 281 | +0.51 | 0.30 |
| Generic | 202 | +0.06 | 0.49 |
| OtherScientificTerm | 296 | -0.42 | 0.62 |

- **Kruskal-Wallis p = 0.7962** (no significant heterogeneity across types)
- Highest gain: Material (+2.47pp), lowest: OtherScientificTerm (-0.42pp)

All results saved to `output/statistical_hardening/`.

---
