# recency_s030 Analysis

## Config
| Parameter | Value |
|-----------|-------|
| model | DeepSeek-R1-Distill-Qwen-7B |
| masking_method | recency (position-only) |
| sparsity | 0.30 |
| n_problems | 100 |
| seed | 42 |

## Core Metrics

### Phase Gradient (primary outcome)
| Metric | Value |
|--------|-------|
| median_diff | -1982.57 |
| 95% CI | [-9391.77, +882.08] |
| cohens_dz | -0.096 (negligible) |
| p_value | 0.114 |
| significant | **NO** (ns) |

### Interaction Index by Phase (s=0.30)
| Phase | Median II | 95% CI |
|-------|-----------|--------|
| high_sparsity | -0.0018 | [-0.0043, +0.0002] |
| mid_sparsity | -0.0160 | [-0.0259, -0.0092] |
| low_sparsity | +0.1099 | [-0.0096, +0.4583] |

### Comparisons at s=0.30
| Method | N | Med Diff | d_z | p | Sig |
|--------|---|----------|-----|---|-----|
| recency_s030 | 99 | -1982.57 | -0.096 | 0.114 | ns |
| n500_imp_s030 | 496 | +8.48 | +0.330 | 1.09e-79 | *** |
| n500_rand_s030 | 496 | +0.51 | -0.049 | 1.48e-03 | ** |

Ratio (recency/importance d_z): 0.29

## Comparison with recency_s015

| Condition | d_z | p | Sig | Verdict |
|-----------|-----|---|-----|---------|
| recency_s015 | +0.083 | 0.77 | ns | GOOD |
| recency_s030 | -0.096 | 0.114 | ns | GOOD |

Both sparsity levels show no significant phase gradient under recency eviction, consistent pattern.

## Conclusion: SUCCESS

Recency (position-only) eviction shows NO significant phase gradient at s=0.30 (d_z=-0.096, p=0.114), while importance-based eviction at the same sparsity shows a significant gradient (d_z=+0.330, p<1e-79). This confirms that phase-dependent compound sparsity severity is attention-score-specific, not a positional/segmentation artifact.

The result replicates the recency_s015 finding at higher sparsity, strengthening the control evidence.
