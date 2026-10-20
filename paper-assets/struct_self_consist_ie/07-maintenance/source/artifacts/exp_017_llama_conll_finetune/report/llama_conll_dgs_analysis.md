## LLaMA CoNLL DGS + 3-Seed 5-Signal Analysis

### DGS (gold_filter=True)
| Metric | Value |
|---|---|
| Degeneracy | 89.4% (2465/2756) |
| Greedy F1 | 0.9239 |
| DGS F1 | 0.9254 |
| DGS-Greedy | +0.14pp [0.03, 0.28] |
| NonDegen LP-Greedy | +1.37pp [0.30, 2.66] |

### 5-Signal (3-seed mean)
| Signal | ρ | SD |
|---|---|---|
| SJ | 0.463 | 0.007 |
| EM | 0.460 | 0.008 |
| VC | 0.458 | 0.003 |
| FK | 0.455 | 0.006 |
| LP | 0.310 | 0.006 |

### Cross-Model (CoNLL)
| | LLaMA | Qwen |
|--|-------|------|
| Degeneracy | 89.4% | 57.9% |
| Greedy F1 | 0.924 | 0.907 |
| Headroom | 2.11pp | 4.24pp |
| DGS delta | +0.14pp | -0.81pp |