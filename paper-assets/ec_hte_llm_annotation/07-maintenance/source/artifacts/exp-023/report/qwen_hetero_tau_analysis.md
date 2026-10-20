# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **LLM**: Qwen2.5-7B (balanced binarization)
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

## Qwen2.5-7B Per-Subgroup Confusion Matrix

| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
|----------|-----|-----|-----|-----------|
| False_medium | 0.3816 | 0.1800 | 0.2874 | 0.5326 |
| False_short | 0.2224 | 0.2414 | 0.1750 | 0.5836 |
| True_medium | 0.2551 | 0.2333 | 0.2105 | 0.5562 |
| True_short | 0.1408 | 0.0000 | 0.1379 | 0.8621 |

- Qwen Δ_FPR = 0.2414, Δ_FNR = 0.1495
- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
- Qwen has larger FPR heterogeneity and larger FNR heterogeneity than Llama

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 200 | Global | 0.0368 | 0.1546 | 0.907 | 0.512 |
| 200 | Strat MLE | 0.0282 | 0.2288 | 0.800 | 0.548 |
| 200 | HB EC-HTE | 0.0275 | 0.2293 | 0.802 | 0.546 |
|----------|--------|-------|------|----------|----------|
| 500 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 500 | Global | 0.0336 | 0.1362 | 0.938 | 0.501 |
| 500 | Strat MLE | 0.0215 | 0.1639 | 0.875 | 0.498 |
| 500 | HB EC-HTE | 0.0196 | 0.1631 | 0.873 | 0.495 |
|----------|--------|-------|------|----------|----------|
| 1000 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 1000 | Global | 0.0328 | 0.1314 | 0.940 | 0.496 |
| 1000 | Strat MLE | 0.0181 | 0.1399 | 0.905 | 0.481 |
| 1000 | HB EC-HTE | 0.0165 | 0.1393 | 0.902 | 0.480 |
|----------|--------|-------|------|----------|----------|

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0368 | 0.0275 | +0.0093 | 0.1546 | 0.2293 | -0.0747 | **YES** | no |
| 500 | 0.0336 | 0.0196 | +0.0141 | 0.1362 | 0.1631 | -0.0269 | **YES** | no |
| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.1314 | 0.1393 | -0.0079 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0175 | 0.0252 | -0.0077 | 0.1639 | 0.2191 |
| False_medium | 0.1 | 1 | 0.0082 | 0.0284 | -0.0202 | 0.0905 | 0.1183 |
| False_short | 0.1 | 0 | 0.0032 | 0.0225 | -0.0193 | 0.2131 | 0.3422 |
| False_short | 0.1 | 1 | 0.0069 | 0.0063 | +0.0007 | 0.1158 | 0.1807 |
| True_medium | 0.3 | 0 | 0.0545 | 0.0669 | -0.0124 | 0.1786 | 0.2636 |
| True_medium | 0.3 | 1 | 0.0106 | 0.0033 | +0.0073 | 0.0934 | 0.1514 |
| True_short | 0.6 | 0 | 0.1156 | 0.0406 | +0.0750 | 0.2193 | 0.3421 |
| True_short | 0.6 | 1 | 0.0780 | 0.0268 | +0.0512 | 0.1619 | 0.2168 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0156 | 0.0074 | +0.0082 | 0.1348 | 0.1767 |
| False_medium | 0.1 | 1 | 0.0031 | 0.0141 | -0.0110 | 0.0777 | 0.0945 |
| False_short | 0.1 | 0 | 0.0002 | 0.0201 | -0.0199 | 0.1854 | 0.2451 |
| False_short | 0.1 | 1 | 0.0114 | 0.0050 | +0.0064 | 0.1034 | 0.1353 |
| True_medium | 0.3 | 0 | 0.0580 | 0.0509 | +0.0070 | 0.1528 | 0.1938 |
| True_medium | 0.3 | 1 | 0.0177 | 0.0045 | +0.0132 | 0.0837 | 0.1091 |
| True_short | 0.6 | 0 | 0.1012 | 0.0395 | +0.0617 | 0.2031 | 0.2016 |
| True_short | 0.6 | 1 | 0.0621 | 0.0152 | +0.0469 | 0.1483 | 0.1486 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0151 | 0.0087 | +0.0064 | 0.1299 | 0.1746 |
| False_medium | 0.1 | 1 | 0.0017 | 0.0024 | -0.0007 | 0.0715 | 0.0836 |
| False_short | 0.1 | 0 | 0.0019 | 0.0004 | +0.0015 | 0.1758 | 0.1900 |
| False_short | 0.1 | 1 | 0.0123 | 0.0053 | +0.0070 | 0.1020 | 0.1139 |
| True_medium | 0.3 | 0 | 0.0576 | 0.0395 | +0.0181 | 0.1480 | 0.1621 |
| True_medium | 0.3 | 1 | 0.0195 | 0.0001 | +0.0194 | 0.0814 | 0.0896 |
| True_short | 0.6 | 0 | 0.0971 | 0.0497 | +0.0474 | 0.1980 | 0.1679 |
| True_short | 0.6 | 1 | 0.0571 | 0.0262 | +0.0309 | 0.1443 | 0.1325 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 200 | Global | 0.0029 | 0.0237 | 0.0266 |
| 200 | Strat MLE | 0.0013 | 0.0582 | 0.0595 |
| 200 | HB EC-HTE | 0.0011 | 0.0586 | 0.0597 |
| 500 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 500 | Global | 0.0023 | 0.0185 | 0.0207 |
| 500 | Strat MLE | 0.0008 | 0.0290 | 0.0298 |
| 500 | HB EC-HTE | 0.0006 | 0.0288 | 0.0294 |
| 1000 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 1000 | Global | 0.0021 | 0.0172 | 0.0193 |
| 1000 | Strat MLE | 0.0007 | 0.0208 | 0.0214 |
| 1000 | HB EC-HTE | 0.0006 | 0.0206 | 0.0212 |

## Cross-Model Comparison: Qwen vs Llama (exp-023)

### CM Heterogeneity

| Metric | Qwen2.5-7B | Llama3.1-8B |
|--------|-----------|------------|
| Δ_FPR (max-min) | 0.2414 | 0.2190 |
| Δ_FNR (max-min) | 0.1495 | 0.1290 |
| Mean Δ_error | 0.1955 | 0.1740 |

### Bias Comparison

| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|
| 200 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |
| 500 | 0.0336 | 0.0196 | +0.0141 | 0.0314 | 0.0099 | +0.0215 |
| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.0286 | 0.0130 | +0.0156 |

### RMSE Comparison

| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
|----------|-----------------|----------------|------------------|-----------------|
| 200 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |
| 500 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |
| 1000 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |

## Conclusion

EC-HTE wins on |Bias| in 3/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**

**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets.
EC-HTE's bias advantage is consistent across both Llama and Qwen models.

Average Δ|Bias| (Global - EC-HTE): Qwen = +0.0132, Llama = +0.0163
Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.
