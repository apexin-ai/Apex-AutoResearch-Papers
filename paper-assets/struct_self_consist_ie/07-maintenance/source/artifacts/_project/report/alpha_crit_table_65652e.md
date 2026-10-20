## α_crit Entity Selection Bound

### Main Table (T=1.0, multi-seed averages)

| Dataset | π_MV | α_crit | α_obs | Gap (α − α_crit) | Δ_SC (pp) | Degeneracy | Bound Predicts | Empirical |
|---------|------|--------|-------|-------------------|-----------|------------|----------------|-----------|
| FewNERD | 0.6561 | 0.4882 | 0.6311 | +0.1429 | **−9.21** | 12.3% | Yes | **No** |
| CoNLL   | 0.8938 | 0.8079 | 0.8743 | +0.0664 | **−1.37** | 63.0% | Yes | **No** |
| SciERC  | 0.6138 | 0.4428 | 0.6069 | +0.1641 | **−3.03** | 20.3% | Yes | **No** |

- **π_MV**: Entity-level majority voting F1 (from multi-seed entity construction)
- **α_obs**: Mean individual sample F1 (`sample_f1_mean` from `report.json`)
- **Δ_SC**: MV F1 − greedy F1 (positive = SC aggregation wins; all negative here)
- **Degeneracy**: Fraction of entities with identical outputs across all n=8 samples

### Detailed Baselines

| Dataset | Greedy | MV | θ2n Select | LP Select | Oracle | Headroom |
|---------|--------|----|------------|-----------|--------|----------|
| FewNERD | 0.7482 | 0.6561 | 0.7571 | 0.7619 | 0.8747 | 12.65 pp |
| CoNLL   | 0.9075 | 0.8938 | 0.8966 | 0.9006 | 0.9460 | 3.85 pp |
| SciERC  | 0.6441 | 0.6138 | 0.6516 | 0.6469 | 0.7746 | 13.06 pp |

### Derivation

```
α_crit = π_MV / (2 − π_MV)
```

- When α > α_crit: SC aggregation should improve over individual samples (agreement signal is informative)
- When α < α_crit: SC aggregation hurts (information loss exceeds agreement gain)

### Key Finding: SC Universally Fails for Structured NER

The bound predicts SC effectiveness for all three datasets (α > α_crit everywhere). However, **all three datasets violate this prediction**: entity-level MV is 1.4–9.2 pp worse than greedy across all settings.

This universal failure has two causes:

1. **Degeneracy** (CoNLL): 63% of entities produce identical outputs across all 8 samples. The agreement signal carries no discriminative power. The degeneracy-adjusted bound correctly predicts failure:

```
α_crit_effective = α_crit / (1 − δ)
```

For CoNLL: 0.8079 / (1 − 0.63) = 2.184 > 1.0 → correctly predicts SC cannot work.

2. **Entity-level span mismatch** (FewNERD, SciERC): Even after degeneracy adjustment, the bound still predicts SC should work (FewNERD: α_crit_eff = 0.557 < α_obs = 0.631; SciERC: α_crit_eff = 0.556 < α_obs = 0.607). The failure is structural: entity-level MV combines entities from different samples, and when span boundaries differ across samples, the aggregated output introduces errors absent from any individual sample. This structural mismatch is not captured by the independence assumption underlying the α_crit bound.

**Implication**: The α_crit bound, derived for classification-style SC, does not transfer to structured IE where outputs are sets of spans. Sample-level selection (LP: +1.36 pp on FewNERD) can succeed where entity-level aggregation fails, because selection preserves internal span consistency.

### Data Sources

- FewNERD: 3 seeds (123, 456, 789), n_instances=32,565
- CoNLL: 2 seeds (123, 456), n_instances=2,756
- SciERC: 2 seeds (456, 789), n_instances=529
- Greedy/MV/Oracle from entity construction experiments; selection F1 from `full_signal_analysis.json`
