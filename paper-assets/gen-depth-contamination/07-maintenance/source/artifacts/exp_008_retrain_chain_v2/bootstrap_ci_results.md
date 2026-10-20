# exp_008_retrain_chain_v2: Bootstrap CI & Permutation Test Results

## Setup

| Parameter | Value |
|-----------|-------|
| Experiment | exp_008_retrain_chain_v2 |
| Protocol | Retrain-chain (independent LoRA per generation) |
| Scorer | Qwen2.5-1.5B |
| Classifier | LightGBM (GroupKFold-5 OOF) |
| Features | 15 surprisal + lexical features |
| Bootstrap resamples | 10,000 (doc-level) |
| Permutation iterations | 10,000 (label permutation, H0: AUC = 0.5) |
| Seed | 42 |
| Theta (distinguishability threshold) | 0.60 |
| Depths | 0-4 (5,000 samples per depth, 25,000 total) |

## Pairwise Results

| Pair | AUC (OOF) | 95% CI | Permutation p | CI lower > 0.60 |
|------|-----------|--------|---------------|------------------|
| 0 vs 1 | 0.9842 | [0.9823, 0.9860] | < 0.001 | PASS |
| 1 vs 2 | 0.9471 | [0.9432, 0.9509] | < 0.001 | PASS |
| 2 vs 3 | 0.8888 | [0.8832, 0.8943] | < 0.001 | PASS |
| 3 vs 4 | 0.7994 | [0.7920, 0.8067] | < 0.001 | PASS |

## Detailed Per-Pair Statistics

### 0 vs 1
- Fold AUCs: [0.9850, 0.9849, 0.9848, 0.9801, 0.9865]
- Mean fold AUC: 0.9843
- OOF AUC: 0.9842
- Bootstrap mean: 0.9842, std: 0.0009
- 95% CI: [0.9823, 0.9860]
- Permutation p-value: 0.0001
- P(AUC <= 0.60): 0.0000

### 1 vs 2
- Fold AUCs: [0.9520, 0.9444, 0.9558, 0.9401, 0.9437]
- Mean fold AUC: 0.9472
- OOF AUC: 0.9471
- Bootstrap mean: 0.9471, std: 0.0020
- 95% CI: [0.9432, 0.9509]
- Permutation p-value: 0.0001
- P(AUC <= 0.60): 0.0000

### 2 vs 3
- Fold AUCs: [0.8794, 0.8828, 0.8998, 0.8986, 0.8848]
- Mean fold AUC: 0.8891
- OOF AUC: 0.8888
- Bootstrap mean: 0.8888, std: 0.0028
- 95% CI: [0.8832, 0.8943]
- Permutation p-value: 0.0001
- P(AUC <= 0.60): 0.0000

### 3 vs 4
- Fold AUCs: [0.8020, 0.7975, 0.8036, 0.7898, 0.8050]
- Mean fold AUC: 0.7996
- OOF AUC: 0.7994
- Bootstrap mean: 0.7994, std: 0.0037
- 95% CI: [0.7920, 0.8067]
- Permutation p-value: 0.0001
- P(AUC <= 0.60): 0.0000

## Summary

**K* (CI-based) = 4**: All four consecutive generation pairs are statistically distinguishable with CI lower bounds well above the theta = 0.60 threshold.

All permutation p-values < 0.001, rejecting H0: AUC = 0.5 for every pair. The monotonic AUC decay (0.98 -> 0.95 -> 0.89 -> 0.80) confirms that distinguishability decreases with generation depth but remains significant through depth 4.

Even the weakest pair (3v4) has CI lower bound = 0.7920, far above 0.60. The tightest CI width is 0.0037 (0v1), widest is 0.0147 (3v4), reflecting increasing variance at higher depths where signal attenuates.

## Method Notes

- Bootstrap resampling at the document level (not sample level) to respect the grouped structure
- OOF predictions from 5-fold GroupKFold ensure no data leakage between train and test
- Permutation test randomizes labels at document level, preserving group structure
- p-value = (count_ge + 1) / (n_perm + 1) following the standard conservative estimator
