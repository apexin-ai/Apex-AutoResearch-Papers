# AG News Semi-Synthetic MC Experiment: EC-HTE vs Global Correction

## Design

- Task: AG News topic classification, binarized as Business/World (Z=1) vs Sports/Sci-Tech (Z=0)
- CM calibrated from literature (arXiv:2506.18501, arXiv:2402.07470)
- N=5000, P(Z=1)=0.5, K=4 subgroups (article_length × vocabulary_complexity)
- **Heterogeneous τ(z) across subgroups:**
  - short_simple: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.10, FPR=0.08, FNR=0.1
  - short_complex: τ(z=0)=0.4, τ(z=1)=0.6, Δτ=0.20, FPR=0.15, FNR=0.18
  - long_simple: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.30, FPR=0.18, FNR=0.2
  - long_complex: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.60, FPR=0.26, FNR=0.3
- n_expert sweep: [250, 500, 1000]
- 100 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- π̄ (global avg misclassification) = 0.1730
- Δπ (max π_s - min π_s) = 0.1900
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 250 | Naive | 0.0672 | 0.1085 | 0.844 | 0.321 |
| 250 | Global | 0.0269 | 0.1154 | 0.935 | 0.426 |
| 250 | Strat MLE | 0.0342 | 0.1811 | 0.886 | 0.511 |
| 250 | HB EC-HTE | 0.0353 | 0.1820 | 0.887 | 0.511 |
|----------|--------|-------|------|----------|----------|
| 500 | Naive | 0.0672 | 0.1085 | 0.844 | 0.321 |
| 500 | Global | 0.0277 | 0.1103 | 0.941 | 0.421 |
| 500 | Strat MLE | 0.0217 | 0.1467 | 0.916 | 0.477 |
| 500 | HB EC-HTE | 0.0220 | 0.1470 | 0.915 | 0.477 |
|----------|--------|-------|------|----------|----------|
| 1000 | Naive | 0.0672 | 0.1085 | 0.844 | 0.321 |
| 1000 | Global | 0.0279 | 0.1090 | 0.939 | 0.417 |
| 1000 | Strat MLE | 0.0145 | 0.1258 | 0.949 | 0.460 |
| 1000 | HB EC-HTE | 0.0147 | 0.1260 | 0.949 | 0.460 |
|----------|--------|-------|------|----------|----------|

## Bias Identity Verification

Theoretical prediction: bias_global = δ_s · Δτ_s / (1 − 2π̄)
where δ_s = π_s − π̄ (symmetric case, π_s = (FPR+FNR)/2)

**R² = -1.2420**

| Subgroup | π_s | δ_s | Δτ_s | Predicted Bias | Observed Bias (avg over n_expert, z) |
|----------|-----|-----|------|----------------|--------------------------------------|
| short_simple | 0.090 | -0.0830 | 0.10 | -0.0127 | +0.0099 |
| short_complex | 0.165 | -0.0080 | 0.20 | -0.0024 | -0.0023 |
| long_simple | 0.190 | +0.0170 | 0.30 | +0.0078 | +0.0033 |
| long_complex | 0.280 | +0.1070 | 0.60 | +0.0982 | +0.0018 |

## Asymmetric Bias Identity Verification

Full asymmetric identity: B_s = M_global⁻¹ M_s − I, predicted_bias(z,s) = B_s[z,1] · Δτ_s
No symmetric approximation — uses actual FPR, FNR, and P(Z) to build mixing matrices.

**R² (averaged across n_expert) = 0.9534**

| n_expert | R² |
|----------|----|
| 250 | 0.9291 |
| 500 | 0.9622 |
| 1000 | 0.9657 |

## Sign Reversal Rate

Fraction of MC runs where sign(CATE_est) ≠ sign(CATE_true):

| Method | Sign Reversal Rate |
|--------|--------------------|
| Naive | 0.0000 |
| Global | 0.0013 |
| Strat MLE | 0.0304 |
| HB EC-HTE | 0.0308 |

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 250 | 0.0269 | 0.0353 | -0.0084 | 0.1154 | 0.1820 | -0.0666 | no | no |
| 500 | 0.0277 | 0.0220 | +0.0057 | 0.1103 | 0.1470 | -0.0367 | **YES** | no |
| 1000 | 0.0279 | 0.0147 | +0.0131 | 0.1090 | 0.1260 | -0.0169 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 250

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| short_simple | 0.10 | 0 | 0.0055 | 0.0132 | -0.0077 | 0.0876 | 0.0886 |
| short_simple | 0.10 | 1 | 0.0158 | 0.0164 | -0.0006 | 0.1044 | 0.1120 |
| short_complex | 0.20 | 0 | 0.0102 | 0.0006 | +0.0095 | 0.1163 | 0.1606 |
| short_complex | 0.20 | 1 | 0.0084 | 0.0034 | +0.0050 | 0.1294 | 0.1725 |
| long_simple | 0.30 | 0 | 0.0053 | 0.0153 | -0.0100 | 0.0960 | 0.1323 |
| long_simple | 0.30 | 1 | 0.0033 | 0.0380 | -0.0347 | 0.1005 | 0.1618 |
| long_complex | 0.60 | 0 | 0.0867 | 0.0954 | -0.0087 | 0.1466 | 0.3299 |
| long_complex | 0.60 | 1 | 0.0802 | 0.1001 | -0.0199 | 0.1422 | 0.2984 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| short_simple | 0.10 | 0 | 0.0072 | 0.0205 | -0.0133 | 0.0841 | 0.0870 |
| short_simple | 0.10 | 1 | 0.0118 | 0.0041 | +0.0077 | 0.0953 | 0.0997 |
| short_complex | 0.20 | 0 | 0.0087 | 0.0048 | +0.0039 | 0.1087 | 0.1298 |
| short_complex | 0.20 | 1 | 0.0023 | 0.0004 | +0.0020 | 0.1164 | 0.1402 |
| long_simple | 0.30 | 0 | 0.0090 | 0.0005 | +0.0085 | 0.0963 | 0.1114 |
| long_simple | 0.30 | 1 | 0.0035 | 0.0121 | -0.0086 | 0.0962 | 0.1237 |
| long_complex | 0.60 | 0 | 0.0902 | 0.0673 | +0.0228 | 0.1457 | 0.2517 |
| long_complex | 0.60 | 1 | 0.0890 | 0.0665 | +0.0225 | 0.1397 | 0.2325 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| short_simple | 0.10 | 0 | 0.0054 | 0.0160 | -0.0107 | 0.0830 | 0.0776 |
| short_simple | 0.10 | 1 | 0.0136 | 0.0049 | +0.0086 | 0.0917 | 0.0879 |
| short_complex | 0.20 | 0 | 0.0094 | 0.0081 | +0.0013 | 0.1101 | 0.1185 |
| short_complex | 0.20 | 1 | 0.0036 | 0.0038 | -0.0001 | 0.1158 | 0.1263 |
| long_simple | 0.30 | 0 | 0.0087 | 0.0053 | +0.0034 | 0.0975 | 0.1053 |
| long_simple | 0.30 | 1 | 0.0031 | 0.0030 | +0.0001 | 0.0924 | 0.1062 |
| long_complex | 0.60 | 0 | 0.0910 | 0.0377 | +0.0533 | 0.1443 | 0.2028 |
| long_complex | 0.60 | 1 | 0.0880 | 0.0391 | +0.0489 | 0.1375 | 0.1830 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 250 | Naive | 0.0079 | 0.0059 | 0.0138 |
| 250 | Global | 0.0018 | 0.0120 | 0.0139 |
| 250 | Strat MLE | 0.0025 | 0.0372 | 0.0397 |
| 250 | HB EC-HTE | 0.0027 | 0.0374 | 0.0401 |
| 500 | Naive | 0.0079 | 0.0059 | 0.0138 |
| 500 | Global | 0.0021 | 0.0107 | 0.0127 |
| 500 | Strat MLE | 0.0012 | 0.0239 | 0.0250 |
| 500 | HB EC-HTE | 0.0012 | 0.0239 | 0.0251 |
| 1000 | Naive | 0.0079 | 0.0059 | 0.0138 |
| 1000 | Global | 0.0021 | 0.0104 | 0.0124 |
| 1000 | Strat MLE | 0.0004 | 0.0173 | 0.0177 |
| 1000 | HB EC-HTE | 0.0004 | 0.0173 | 0.0178 |

## Conclusion

AG News (Business/World vs Sports/Sci-Tech): EC-HTE wins on |Bias| in 2/3 budget levels, RMSE in 0/3.
Bias identity: symmetric R²=-1.2420, asymmetric R²=0.9534.
The full asymmetric identity (B_s = M_global⁻¹ M_s − I) accurately predicts Global correction's residual bias.
Sign reversal rates: Naive=0.0000, Global=0.0013, Strat MLE=0.0304, HB EC-HTE=0.0308.
