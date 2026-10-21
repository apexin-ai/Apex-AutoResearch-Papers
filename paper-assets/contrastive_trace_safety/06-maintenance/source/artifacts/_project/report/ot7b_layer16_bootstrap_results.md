# OT-7B Layer 16: Bootstrap + Selectivity Results

## Configuration
- Layer: 16, Window: 3, Seed: 42
- Data: 228 traces (train=136, val=45, test=47)
- Bootstrap: 1000 resamples, Bonferroni alpha=0.017

## Task 1: Paired Bootstrap (HS vs Text, matched W=3)

### Point Estimates
| Probe | bal_acc | precision | pre_cp_fpr |
|-------|---------|-----------|------------|
| HS (Layer 16) | 0.7624 | 0.5648 | 0.1004 |
| Text (MiniLM) | 0.6558 | 0.3459 | 0.2709 |

### Bootstrap Results
| Metric | Delta | 95% CI | p-value | Bonferroni sig |
|--------|-------|--------|---------|----------------|
| bal_acc | +0.1067 | [0.0491, 0.1625] | 0.000 | YES |
| precision | +0.2189 | [0.1401, 0.2961] | 0.000 | YES |
| pre_cp_fpr | -0.1705 | [-0.2224, -0.1221] | 0.000 | YES |

## Task 2: Selectivity Control (Hewitt & Liang 2019)
- Real accuracy: 0.6876
- Random mean +/- std: 0.5048 +/- 0.0219
- **Selectivity: 18.3 pp (PASS, threshold >5pp)**

## Task 3: Layer 0 vs Layer 16 Comparison

### Probe Performance
| Metric | Layer 0 | Layer 16 | Change |
|--------|---------|----------|--------|
| HS bal_acc | 0.6721 | 0.7624 | +0.0903 |
| HS precision | 0.3571 | 0.5648 | +0.2077 |
| HS pre_cp_fpr | 0.1877 | 0.1004 | -0.0873 |

### Bootstrap Comparison
| Metric | L0 delta | L0 p | L16 delta | L16 CI | L16 p | L16 sig |
|--------|----------|------|-----------|--------|-------|---------|
| bal_acc | +0.0815 | 0.001 | +0.1067 | [0.049, 0.163] | 0.000 | YES |
| precision | +0.079 | 0.056 | +0.2189 | [0.140, 0.296] | 0.000 | YES |
| pre_cp_fpr | -0.0832 | 0.007 | -0.1705 | [-0.222, -0.122] | 0.000 | YES |

### Selectivity Comparison
| Metric | Layer 0 | Layer 16 |
|--------|---------|----------|
| real_acc | 0.672 | 0.688 |
| random_mean | 0.487 | 0.505 |
| selectivity_pp | 18.5 | 18.3 |

## Summary
Layer 16 dominates Layer 0 across all metrics:
- bal_acc improved +9pp (0.672 -> 0.762)
- precision improved +21pp (0.357 -> 0.565)
- pre_cp_fpr reduced -8.7pp (0.188 -> 0.100)
- All bootstrap tests now pass Bonferroni correction (precision was p=0.056 on L0, now p=0.000)
- Selectivity comparable (18.3pp vs 18.5pp), both strongly pass >5pp threshold
