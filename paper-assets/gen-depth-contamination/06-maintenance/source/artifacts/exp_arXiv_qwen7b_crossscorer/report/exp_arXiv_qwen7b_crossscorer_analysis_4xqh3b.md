# exp_arXiv_qwen7b_crossscorer Analysis Report

**Date**: 2026-05-18
**Experiment**: Cross-scorer validation for arXiv Qwen-7B depth contamination
**Scorer**: Pythia-1.4B (replacing Qwen-1.5B)
**Generator**: Qwen-7B
**Domain**: arXiv
**Status**: DONE (EXIT_CODE=0)

---

## 1. Pairwise AUC (adjacent depths, 5-fold CV)

| Pair | Cross-scorer (Pythia-1.4B) | Original (Qwen-1.5B) | Delta |
|------|---------------------------:|----------------------:|------:|
| 0v1  | 0.9575 ± 0.0074           | 0.983                 | -0.0255 |
| 1v2  | 0.8171 ± 0.0166           | 0.835                 | -0.0179 |
| 2v3  | 0.5989 ± 0.0135           | 0.626                 | -0.0271 |
| 3v4  | 0.5417 ± 0.0220           | 0.544                 | -0.0023 |
| 4v5  | 0.5192 ± 0.0162           | 0.513                 | +0.0062 |

Cross-scorer per-fold detail (2v3): [0.592, 0.601, 0.611, 0.577, 0.614]

## 2. Pairwise JSD (adjacent depths)

| Pair | Cross-scorer (Pythia-1.4B) |
|------|---------------------------:|
| 0v1  | 0.1371                     |
| 1v2  | 0.0597                     |
| 2v3  | 0.0135                     |
| 3v4  | 0.0091                     |
| 4v5  | 0.0067                     |

## 3. K* Determination

| Scorer        | K* | Criterion (last pair with AUC >= 0.60) |
|---------------|---:|----------------------------------------|
| Qwen-1.5B     |  3 | 2v3 AUC = 0.626 >= 0.60               |
| Pythia-1.4B   |  2 | 1v2 AUC = 0.817 >= 0.60; 2v3 = 0.599 < 0.60 |

**K* drops from 3 to 2 under cross-scorer.**

## 4. Ordinal Classification

- MAE: 0.9617
- Accuracy: 42.55%

## 5. Top-10 Feature Importance

| Feature          | Importance |
|------------------|----------:|
| freq_entropy     |    9853.2 |
| surp_std         |    7917.2 |
| surp_d1_skew     |    7895.0 |
| surp_mean        |    7603.0 |
| surp_d2_mean     |    7329.4 |
| surp_d1_mean     |    7247.6 |
| freq_kurtosis    |    6881.6 |
| surp_kurt        |    6452.8 |
| hapax_ratio      |    5941.0 |
| surp_d1_std      |    5913.8 |

## 6. Conclusion: Scorer Confound Assessment

**Cross-scorer 2v3 AUC = 0.5989 < 0.60 threshold. K*=3 is NOT confirmed as scorer-independent.**

Key observations:

1. **Mild family bias exists**: AUC consistently drops across all depth pairs (0v1 through 2v3) when switching from Qwen-1.5B to Pythia-1.4B. Average delta for depths 0-3 is -0.024, indicating the Qwen scorer slightly inflates discriminability for Qwen-generated text.

2. **The 2v3 boundary is borderline**: 0.5989 is only 0.0011 below the 0.60 threshold. Three of five folds exceed 0.60 (0.601, 0.611, 0.614), two fall short (0.577, 0.592). This is not a clear rejection; it is a marginal miss.

3. **Depths 0-2 remain robust**: 0v1 (0.958) and 1v2 (0.817) are strongly scorer-independent. The contamination signal at shallow depths is genuine.

4. **Depths 3-5 are noise under both scorers**: 3v4 and 4v5 AUC values are near chance (0.50-0.54) regardless of scorer, confirming saturation beyond depth 2-3.

5. **Practical interpretation**: The arXiv K*=3 signal is weaker than originally estimated. The conservative scorer-independent estimate is K*=2, though the true boundary likely lies in the range [2, 3]. The family bias effect (~0.027 AUC at 2v3) is small but sufficient to flip the binary threshold.

**Bottom line**: arXiv contamination is real and scorer-independent through depth 2. The depth-3 signal carries a small but non-negligible scorer confound contribution from Qwen family bias.
