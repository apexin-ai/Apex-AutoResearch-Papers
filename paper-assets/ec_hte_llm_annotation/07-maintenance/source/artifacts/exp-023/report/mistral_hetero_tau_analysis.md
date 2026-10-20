# Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **LLM**: Mistral-7B-v0.3 (balanced binarization)
- **Heterogeneous τ(z) across subgroups:**
  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
- n_expert sweep: [200, 500, 1000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)

## Mistral-7B-v0.3 Per-Subgroup Confusion Matrix

| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
|----------|-----|-----|-----|-----------|
| False_medium | 0.3816 | 0.1800 | 0.2989 | 0.5211 |
| False_short | 0.2224 | 0.2414 | 0.1875 | 0.5711 |
| True_medium | 0.2551 | 0.2333 | 0.1684 | 0.5983 |
| True_short | 0.1408 | 0.0909 | 0.1207 | 0.7884 |

- Mistral Δ_FPR = 0.1505, Δ_FNR = 0.1782
- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
- Mistral has smaller FPR heterogeneity and larger FNR heterogeneity than Llama

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
| 200 | Global | 0.0266 | 0.1536 | 0.912 | 0.517 |
| 200 | Strat MLE | 0.0284 | 0.2364 | 0.815 | 0.551 |
| 200 | HB EC-HTE | 0.0281 | 0.2384 | 0.812 | 0.552 |
|----------|--------|-------|------|----------|----------|
| 500 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
| 500 | Global | 0.0245 | 0.1369 | 0.940 | 0.505 |
| 500 | Strat MLE | 0.0194 | 0.1710 | 0.873 | 0.501 |
| 500 | HB EC-HTE | 0.0191 | 0.1717 | 0.873 | 0.502 |
|----------|--------|-------|------|----------|----------|
| 1000 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
| 1000 | Global | 0.0237 | 0.1323 | 0.940 | 0.501 |
| 1000 | Strat MLE | 0.0188 | 0.1437 | 0.897 | 0.484 |
| 1000 | HB EC-HTE | 0.0186 | 0.1438 | 0.897 | 0.485 |
|----------|--------|-------|------|----------|----------|

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0266 | 0.0281 | -0.0015 | 0.1536 | 0.2384 | -0.0848 | no | no |
| 500 | 0.0245 | 0.0191 | +0.0054 | 0.1369 | 0.1717 | -0.0348 | **YES** | no |
| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.1323 | 0.1438 | -0.0114 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0107 | 0.0250 | -0.0143 | 0.1599 | 0.2225 |
| False_medium | 0.1 | 1 | 0.0132 | 0.0279 | -0.0147 | 0.0917 | 0.1163 |
| False_short | 0.1 | 0 | 0.0069 | 0.0065 | +0.0004 | 0.2117 | 0.3542 |
| False_short | 0.1 | 1 | 0.0004 | 0.0145 | -0.0140 | 0.1188 | 0.1914 |
| True_medium | 0.3 | 0 | 0.0272 | 0.0660 | -0.0388 | 0.1752 | 0.2444 |
| True_medium | 0.3 | 1 | 0.0001 | 0.0050 | -0.0049 | 0.0944 | 0.1367 |
| True_short | 0.6 | 0 | 0.1027 | 0.0511 | +0.0515 | 0.2286 | 0.4119 |
| True_short | 0.6 | 1 | 0.0518 | 0.0289 | +0.0229 | 0.1489 | 0.2299 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0134 | 0.0076 | +0.0058 | 0.1354 | 0.1858 |
| False_medium | 0.1 | 1 | 0.0058 | 0.0143 | -0.0084 | 0.0796 | 0.0963 |
| False_short | 0.1 | 0 | 0.0064 | 0.0110 | -0.0046 | 0.1841 | 0.2516 |
| False_short | 0.1 | 1 | 0.0068 | 0.0002 | +0.0066 | 0.1059 | 0.1416 |
| True_medium | 0.3 | 0 | 0.0357 | 0.0508 | -0.0151 | 0.1533 | 0.1857 |
| True_medium | 0.3 | 1 | 0.0106 | 0.0042 | +0.0064 | 0.0836 | 0.1058 |
| True_short | 0.6 | 0 | 0.0837 | 0.0492 | +0.0345 | 0.2164 | 0.2535 |
| True_short | 0.6 | 1 | 0.0337 | 0.0155 | +0.0182 | 0.1369 | 0.1533 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0132 | 0.0079 | +0.0054 | 0.1317 | 0.1828 |
| False_medium | 0.1 | 1 | 0.0042 | 0.0031 | +0.0010 | 0.0745 | 0.0862 |
| False_short | 0.1 | 0 | 0.0074 | 0.0088 | -0.0014 | 0.1740 | 0.1933 |
| False_short | 0.1 | 1 | 0.0081 | 0.0007 | +0.0074 | 0.1036 | 0.1173 |
| True_medium | 0.3 | 0 | 0.0352 | 0.0405 | -0.0053 | 0.1476 | 0.1535 |
| True_medium | 0.3 | 1 | 0.0128 | 0.0011 | +0.0117 | 0.0815 | 0.0877 |
| True_short | 0.6 | 0 | 0.0798 | 0.0580 | +0.0218 | 0.2125 | 0.1951 |
| True_short | 0.6 | 1 | 0.0289 | 0.0288 | +0.0001 | 0.1333 | 0.1341 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0058 | 0.0075 | 0.0133 |
| 200 | Global | 0.0018 | 0.0246 | 0.0264 |
| 200 | Strat MLE | 0.0012 | 0.0645 | 0.0658 |
| 200 | HB EC-HTE | 0.0012 | 0.0659 | 0.0671 |
| 500 | Naive | 0.0058 | 0.0075 | 0.0133 |
| 500 | Global | 0.0012 | 0.0199 | 0.0211 |
| 500 | Strat MLE | 0.0007 | 0.0322 | 0.0329 |
| 500 | HB EC-HTE | 0.0007 | 0.0325 | 0.0332 |
| 1000 | Naive | 0.0058 | 0.0075 | 0.0133 |
| 1000 | Global | 0.0011 | 0.0187 | 0.0198 |
| 1000 | Strat MLE | 0.0008 | 0.0221 | 0.0228 |
| 1000 | HB EC-HTE | 0.0007 | 0.0221 | 0.0229 |

## Cross-Model Comparison: Mistral vs Llama (exp-023)

### CM Heterogeneity

| Metric | Mistral-7B-v0.3 | Llama3.1-8B |
|--------|----------------|------------|
| Δ_FPR (max-min) | 0.1505 | 0.2190 |
| Δ_FNR (max-min) | 0.1782 | 0.1290 |
| Mean Δ_error | 0.1643 | 0.1740 |

### Bias Comparison

| n_expert | Mistral |Bias|_Global | Mistral |Bias|_ECHTE | Mistral Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|
| 200 | 0.0266 | 0.0281 | -0.0015 | 0.0365 | 0.0248 | +0.0117 |
| 500 | 0.0245 | 0.0191 | +0.0054 | 0.0314 | 0.0099 | +0.0215 |
| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.0286 | 0.0130 | +0.0156 |

### RMSE Comparison

| n_expert | Mistral RMSE_Global | Mistral RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
|----------|-----------------|----------------|------------------|-----------------|
| 200 | 0.1536 | 0.2384 | 0.1780 | 0.2606 |
| 500 | 0.1369 | 0.1717 | 0.1580 | 0.1760 |
| 1000 | 0.1323 | 0.1438 | 0.1554 | 0.1602 |

## Conclusion

EC-HTE wins on |Bias| in 2/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE outperforms Global in bias at 2 of 3 budget levels.**

**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Mistral EC-HTE wins in 2/3 budgets.

Average Δ|Bias| (Global - EC-HTE): Mistral = +0.0030, Llama = +0.0163
Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.
