# α=0.25 s44 Analysis + 3-Seed Summary

## s44 Complete Metrics (Pythia-410M, α=0.25, seed=44, fp32)

### Absolute Values
| Metric | Gen 0 | Gen 9 |
|--------|-------|-------|
| token_entropy | 3.234 | 3.101 |
| distinct_1 | 0.0974 | 0.0600 |
| distinct_2 | 0.513 | 0.239 |
| distinct_3 | 0.814 | 0.363 |
| perplexity | 26.95 | 22.57 |
| ece | 0.0108 | 0.0182 |
| effective_rank | 46.61 | 46.21 |
| mauve | 0.032 | 0.019 |

### Drift (gen0→gen9)
| Metric | Drift% |
|--------|--------|
| distinct_1 | -38.35% |
| distinct_2 | -53.44% |
| distinct_3 | -55.35% |
| token_entropy | -4.11% |
| ece | +68.01% |
| perplexity | -16.27% |
| mauve | -40.63% |
| effective_rank | -0.87% |

### Lead-Lag Detection
| Method | Result |
|--------|--------|
| PermG fwd | 0/8 |
| PermG rev | 0/8 |
| K≥4 consensus | 0/8 |
| MMCT detection | 0.0 |
| naive_xcorr | 8/8 |
| diff_xcorr | 0/8 |
| threshold_onset | 0/8 |
| TY Granger | 1/8 |

## 3-Seed Comparison (α=0.25)

### Core Detection Metrics
| Metric | s42 | s43 | s44 | Cross-seed |
|--------|-----|-----|-----|------------|
| PermG fwd | 0/8 | 0/8 | 0/8 | ✓ Consistent |
| PermG rev | 0/8 | 0/8 | 0/8 | ✓ Consistent |
| K≥4 consensus | 0/8 | 0/8 | 0/8 | ✓ Consistent |
| MMCT | 0.0 | 0.0 | 0.0 | ✓ Consistent |
| TY Granger | 3/8 | 6/8 | 1/8 | ✗ Unstable (C003) |

### Drift Comparison
| Metric | s42 | s43 | s44 | σ |
|--------|-----|-----|-----|---|
| d1 | -39.15% | -38.95% | -38.35% | 0.33pp |
| d2 | -54.75% | -53.35% | -53.44% | 0.64pp |
| d3 | -56.98% | -54.80% | -55.35% | 0.92pp |
| entropy | -4.79% | -4.94% | -4.11% | 0.37pp |
| ece | +79.17% | +64.77% | +68.01% | 6.24pp |
| ppl | -18.09% | -18.38% | -16.27% | 0.94pp |
| mauve | -41.86% | -35.59% | -40.63% | 2.73pp |
| eff_rank | -3.78% | -1.99% | -0.87% | 1.22pp |

## Conclusion
α=0.25 is confirmed as blind zone upper bound with 3-seed consistency:
- PermG=0/8 across all seeds (no Granger causal signal)
- Diversity collapse is real (d1≈-38.8%, d2≈-53.8%, d3≈-55.7%) but canary metrics lack sufficient drift to predict it
- TY Granger remains seed-unstable at low α (1-6/8), confirming C003
- Drift variance across seeds is very low (d1 σ=0.33pp), indicating high reproducibility
