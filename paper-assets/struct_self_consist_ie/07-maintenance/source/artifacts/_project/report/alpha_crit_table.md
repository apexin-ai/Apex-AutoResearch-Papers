## α_crit Entity Selection Bound

### Main Table (T=1.0, multi-seed averages)

| Dataset | π_MV | α_crit | α_obs | Gap (α − α_crit) | Δ_SC (pp) | Degeneracy | Bound Predicts | Empirical |
|---------|------|--------|-------|-------------------|-----------|------------|----------------|-----------|
| FewNERD | 0.6561 | 0.4882 | 0.6311 | +0.1429 | **+0.89** | 12.3% | Yes | **Yes** |
| CoNLL   | 0.8938 | 0.8079 | 0.8743 | +0.0664 | **−1.09** | 63.0% | Yes | **No** |
| SciERC  | 0.6138 | 0.4428 | 0.6069 | +0.1641 | **+0.76** | 20.3% | Yes | **Yes** |

- **π_MV**: Entity-level majority voting F1 (from `full_signal_report.json`)
- **α_obs**: Mean individual sample F1 (`sample_f1_mean` from `report.json`)
- **Δ_SC**: consensus_θ2n selection F1 − greedy F1 (positive = SC selection wins)
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

- When α > α_crit: SC selection should improve over greedy (agreement signal is informative)
- When α < α_crit: SC selection hurts (information loss exceeds agreement gain)

### Key Finding: Degeneracy Invalidates the Bound

The bound predicts SC effectiveness for all three datasets (α > α_crit everywhere). However, **CoNLL violates this prediction**: SC selection is 1.09 pp *worse* than greedy despite satisfying the bound by a margin of +0.0664.

The explanation is **degeneracy**: 63% of CoNLL entities produce identical outputs across all 8 samples. When samples are degenerate, the agreement signal carries no discriminative power — the diversity assumption underlying the α_crit bound is violated. By contrast, FewNERD (12.3% degeneracy) and SciERC (20.3%) have sufficient output diversity for the bound to hold.

This suggests the bound should be refined:

```
α_crit_effective = α_crit / (1 − δ)
```

where δ is the degeneracy rate. For CoNLL: α_crit_effective = 0.8079 / (1 − 0.63) = 2.184, which exceeds 1.0 — correctly predicting that SC selection cannot work under such extreme degeneracy.

### Data Sources

- FewNERD: 3 seeds (123, 456, 789), n_instances=32,565
- CoNLL: 2 seeds (123, 456), n_instances=2,756
- SciERC: 2 seeds (456, 789), n_instances=529
- All from `/root/autodl-tmp/struct_self_consist_ie/output/exp_{dataset}_seed{N}/full_signal_report.json`
