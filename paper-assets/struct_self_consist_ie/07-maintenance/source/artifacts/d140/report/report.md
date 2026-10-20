# D140: Oracle Degeneracy-Gated LP Selection Analysis

## Summary

Degeneracy = all N samples have identical entity-level F1 (oracle cannot improve).
Gated selection = LP selection on non-degenerate instances, greedy on degenerate.

## Overall Results

| Dataset | N_inst | N_samp | Degen% | Greedy_F1 | LP_F1 | Oracle_F1 | Gated_F1 | LP_vs_Greedy | Gated_vs_LP |
|---------|--------|--------|--------|-----------|-------|-----------|----------|--------------|-------------|
| SciERC | 529 | 8 | 17.8% | 66.6267 | 66.3121 | 78.0765 | 66.3712 | -0.3146 | +0.0591 |
| CoNLL | 2756 | 16 | 48.4% | 91.2367 | 88.8655 | 96.3734 | 88.9123 | -2.3713 | +0.0469 |
| Few-NERD | 32565 | 8 | 13.8% | 79.1103 | 79.1846 | 88.5456 | 79.2449 | +0.0743 | +0.0604 |

## Bootstrap 95% CI for Key Deltas (1000 resamples)

| Dataset | LP_vs_Greedy | CI_95 | Gated_vs_Greedy | CI_95 | Gated_vs_LP | CI_95 |
|---------|-------------|-------|-----------------|-------|-------------|-------|
| SciERC | -0.3146 | [-1.6307, +0.9902] | -0.2555 | [-1.5834, +1.0703] | +0.0591 | [-0.0217, +0.1722] |
| CoNLL | -2.3713 | [-3.4642, -1.4394] | -2.3244 | [-3.3823, -1.4040] | +0.0469 | [-0.0080, +0.1425] |
| Few-NERD | +0.0743 | [-0.0551, +0.2078] | +0.1346 | [+0.0076, +0.2686] | +0.0604 | [+0.0443, +0.0777] |

## Non-Degenerate Subset Analysis (Core: LP effectiveness where oracle can improve)

| Dataset | N_nondeg | Greedy_F1 | LP_F1 | Oracle_F1 | LP_vs_Greedy | CI_95 |
|---------|----------|-----------|-------|-----------|--------------|-------|
| SciERC | 435 | 66.5288 | 66.2377 | 79.6303 | -0.2911 | [-1.6875, +1.2174] |
| CoNLL | 1421 | 88.7181 | 85.1342 | 96.6849 | -3.5839 | [-5.2162, -2.2770] |
| Few-NERD | 28086 | 79.4357 | 79.5821 | 89.8562 | +0.1464 | [-0.0059, +0.2911] |

## Degenerate Subset (All samples identical F1)

| Dataset | N_degen | Degen% | Greedy_F1 | CI_95 |
|---------|---------|--------|-----------|-------|
| SciERC | 94 | 17.8% | 67.2854 | [+60.3581, +74.2169] |
| CoNLL | 1335 | 48.4% | 95.7858 | [+94.8594, +96.7421] |
| Few-NERD | 4479 | 13.8% | 76.0735 | [+74.7498, +77.4686] |

## Key Findings

### SciERC
- Degeneracy rate: 17.8% (94/529)
- Overall LP vs Greedy: -0.3146 CI [-1.6307, +0.9902]
- Non-degenerate LP vs Greedy: -0.2911 CI [-1.6875, +1.2174]
- Gated vs ungated LP: +0.0591 CI [-0.0217, +0.1722]
- Oracle F1 gap (overall): +11.4498

### CoNLL
- Degeneracy rate: 48.4% (1335/2756)
- Overall LP vs Greedy: -2.3713 CI [-3.4642, -1.4394]
- Non-degenerate LP vs Greedy: -3.5839 CI [-5.2162, -2.2770]
- Gated vs ungated LP: +0.0469 CI [-0.0080, +0.1425]
- Oracle F1 gap (overall): +5.1367

### Few-NERD
- Degeneracy rate: 13.8% (4479/32565)
- Overall LP vs Greedy: +0.0743 CI [-0.0551, +0.2078]
- Non-degenerate LP vs Greedy: +0.1464 CI [-0.0059, +0.2911]
- Gated vs ungated LP: +0.0604 CI [+0.0443, +0.0777]
- Oracle F1 gap (overall): +9.4353