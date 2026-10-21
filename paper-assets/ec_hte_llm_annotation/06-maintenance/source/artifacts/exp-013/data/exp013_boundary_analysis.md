# exp-013: Boundary Condition Analysis

**Config**: K=4, regime=extreme, n_expert=50, N=5000, misclass=[0.3, 0.2, 0.1, 0.03]

Each subgroup gets ~12 expert labels.

## Per-subgroup Results

| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|---|
| A (0.30) | naive | 0.1212 | 0.1470 | 0.78 | 0.1284 | 0.1576 | 0.70 |
| A (0.30) | global_corrected | 0.0766 | 0.1344 | 0.92 | 0.0853 | 0.1482 | 0.89 |
| A (0.30) | mle_laplace | 0.0986 | 0.5210 | 0.95 | 0.0835 | 0.5265 | 0.95 |
| A (0.30) | hb_eb | 0.0383 | 0.6068 | 0.93 | 0.0215 | 0.6194 | 0.90 |
| B (0.20) | naive | 0.0771 | 0.1200 | 0.88 | 0.0759 | 0.1159 | 0.87 |
| B (0.20) | global_corrected | 0.0068 | 0.1263 | 0.94 | 0.0033 | 0.1198 | 0.93 |
| B (0.20) | mle_laplace | 0.1000 | 0.2999 | 0.92 | 0.1038 | 0.2897 | 0.92 |
| B (0.20) | hb_eb | 0.0669 | 0.2706 | 0.92 | 0.0740 | 0.2588 | 0.93 |
| C (0.10) | naive | 0.0312 | 0.0851 | 0.96 | 0.0505 | 0.1085 | 0.90 |
| C (0.10) | global_corrected | 0.0608 | 0.1291 | 0.94 | 0.0420 | 0.1344 | 0.91 |
| C (0.10) | mle_laplace | 0.0827 | 0.1536 | 0.91 | 0.0657 | 0.1635 | 0.88 |
| C (0.10) | hb_eb | 0.0529 | 0.1417 | 0.94 | 0.0392 | 0.1532 | 0.92 |
| D (0.03) | naive | 0.0005 | 0.0825 | 0.97 | 0.0146 | 0.0843 | 0.96 |
| D (0.03) | global_corrected | 0.1105 | 0.1624 | 0.87 | 0.0983 | 0.1605 | 0.85 |
| D (0.03) | mle_laplace | 0.0895 | 0.1444 | 0.88 | 0.0819 | 0.1514 | 0.92 |
| D (0.03) | hb_eb | 0.0612 | 0.1505 | 0.95 | 0.0599 | 0.1618 | 0.94 |

## Average Across Subgroups

| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|
| naive | 0.0575 | 0.1087 | 0.90 | 0.0674 | 0.1166 | 0.86 |
| global_corrected | 0.0637 | 0.1381 | 0.92 | 0.0572 | 0.1407 | 0.90 |
| mle_laplace | 0.0927 | 0.2798 | 0.92 | 0.0837 | 0.2828 | 0.92 |
| hb_eb | 0.0548 | 0.2924 | 0.94 | 0.0486 | 0.2983 | 0.92 |

## RMSE Amplification (stratified vs global)

| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |
|---|---|---|---|
| A (0.30) | mle_laplace | 3.77x | 3.74x |
| A (0.30) | hb_eb | 4.39x | 4.40x |
| B (0.20) | mle_laplace | 2.17x | 2.06x |
| B (0.20) | hb_eb | 1.96x | 1.84x |
| C (0.10) | mle_laplace | 1.11x | 1.16x |
| C (0.10) | hb_eb | 1.03x | 1.09x |
| D (0.03) | mle_laplace | 1.05x | 1.08x |
| D (0.03) | hb_eb | 1.09x | 1.15x |

## Key Findings

1. **Worst degradation**: subgroup A (hb_eb, z1) with RMSE=0.6194
2. **Average stratified RMSE**: z0=0.2861, z1=0.2905 vs global z0=0.1381, z1=0.1407
3. **Amplification factor**: 2.07x (z0), 2.06x (z1)
4. **n_expert/K = 12.5** < 25 threshold NOT met. Below recommended minimum — expect high variance in per-subgroup estimates.
5. **EB vs MLE**: EB RMSE -5.0% relative to MLE (MLE competitive)
