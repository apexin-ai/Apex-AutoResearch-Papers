# Feature Importance Stability (Kendall W)

8-generator LOGO, permutation importance (n_repeats=10, scoring=f1_macro), 3-class task.

## Ranking Table

| Feature | Fold1 (llama) | Fold2 (mistral) | Fold3 (olmo) | Fold4 (pythia-1b) | Fold5 (pythia-2.8b) | Fold6 (qwen-0.6b) | Fold7 (qwen-1.7b) | Fold8 (qwen-8b) | Mean rank |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hapax_ratio | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **1.00** |
| entropy_mean | 2 | 2 | 2 | 3 | 2 | 3 | 3 | 2 | **2.38** |
| ttr | 3 | 4 | 3 | 2 | 3 | 2 | 2 | 3 | **2.75** |
| entropy_max | 5 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | **4.00** |
| entropy_std | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **4.88** |
| entropy_min | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | **6.00** |
| tail_decay | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | **7.00** |

## Concordance

**Kendall W = 0.9632** (chi2 = 46.23, df = 6, p = 2.66e-08)

## Interpretation

Feature importance rankings are highly stable across all 8 LOGO folds (W > 0.96, p < 1e-7). The top-3 features (hapax_ratio, entropy_mean, ttr) are consistent across generators, with hapax_ratio ranked #1 in every single fold. The bottom two (entropy_min, tail_decay) are also perfectly stable at ranks 6 and 7.
