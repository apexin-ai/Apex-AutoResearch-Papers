# Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **LLM**: Gemma-2-9B (balanced binarization)
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

## Gemma-2-9B Per-Subgroup Confusion Matrix

| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
|----------|-----|-----|-----|-----------|
| False_medium | 0.3816 | 0.1100 | 0.4368 | 0.4532 |
| False_short | 0.2224 | 0.1379 | 0.3000 | 0.5621 |
| True_medium | 0.2551 | 0.0333 | 0.2632 | 0.7035 |
| True_short | 0.1408 | 0.0909 | 0.2069 | 0.7022 |

- Gemma Δ_FPR = 0.1046, Δ_FNR = 0.2299
- Qwen Δ_FPR = 0.2410, Δ_FNR = 0.1490
- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
- **Note**: Gemma has strong FNR>FPR asymmetry (False_medium FNR=0.437 most extreme)

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
| 200 | Global | 0.0261 | 0.1498 | 0.927 | 0.525 |
| 200 | Strat MLE | 0.0263 | 0.2708 | 0.802 | 0.575 |
| 200 | HB EC-HTE | 0.0269 | 0.2614 | 0.807 | 0.562 |
|----------|--------|-------|------|----------|----------|
| 500 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
| 500 | Global | 0.0153 | 0.1353 | 0.948 | 0.514 |
| 500 | Strat MLE | 0.0156 | 0.1760 | 0.877 | 0.519 |
| 500 | HB EC-HTE | 0.0117 | 0.1741 | 0.873 | 0.515 |
|----------|--------|-------|------|----------|----------|
| 1000 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
| 1000 | Global | 0.0155 | 0.1310 | 0.950 | 0.513 |
| 1000 | Strat MLE | 0.0169 | 0.1444 | 0.910 | 0.505 |
| 1000 | HB EC-HTE | 0.0157 | 0.1435 | 0.915 | 0.503 |
|----------|--------|-------|------|----------|----------|

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0261 | 0.0269 | -0.0008 | 0.1498 | 0.2614 | -0.1116 | no | no |
| 500 | 0.0153 | 0.0117 | +0.0036 | 0.1353 | 0.1741 | -0.0388 | **YES** | no |
| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.1310 | 0.1435 | -0.0125 | no | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0049 | 0.0374 | -0.0325 | 0.1549 | 0.2857 |
| False_medium | 0.1 | 1 | 0.0158 | 0.0342 | -0.0185 | 0.0974 | 0.1584 |
| False_short | 0.1 | 0 | 0.0299 | 0.0112 | +0.0186 | 0.2069 | 0.3273 |
| False_short | 0.1 | 1 | 0.0094 | 0.0158 | -0.0064 | 0.1176 | 0.1720 |
| True_medium | 0.3 | 0 | 0.0213 | 0.0034 | +0.0178 | 0.1556 | 0.1811 |
| True_medium | 0.3 | 1 | 0.0297 | 0.0430 | -0.0133 | 0.0945 | 0.1278 |
| True_short | 0.6 | 0 | 0.0827 | 0.0011 | +0.0815 | 0.2345 | 0.5282 |
| True_short | 0.6 | 1 | 0.0151 | 0.0688 | -0.0538 | 0.1368 | 0.3107 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0186 | 0.0031 | +0.0155 | 0.1369 | 0.2157 |
| False_medium | 0.1 | 1 | 0.0036 | 0.0125 | -0.0089 | 0.0870 | 0.1200 |
| False_short | 0.1 | 0 | 0.0194 | 0.0023 | +0.0171 | 0.1809 | 0.2303 |
| False_short | 0.1 | 1 | 0.0026 | 0.0008 | +0.0018 | 0.1087 | 0.1344 |
| True_medium | 0.3 | 0 | 0.0009 | 0.0247 | -0.0238 | 0.1341 | 0.1490 |
| True_medium | 0.3 | 1 | 0.0134 | 0.0113 | +0.0021 | 0.0824 | 0.0931 |
| True_short | 0.6 | 0 | 0.0583 | 0.0332 | +0.0251 | 0.2253 | 0.2858 |
| True_short | 0.6 | 1 | 0.0057 | 0.0059 | -0.0002 | 0.1273 | 0.1650 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0185 | 0.0072 | +0.0113 | 0.1266 | 0.1819 |
| False_medium | 0.1 | 1 | 0.0025 | 0.0045 | -0.0020 | 0.0804 | 0.0948 |
| False_short | 0.1 | 0 | 0.0199 | 0.0183 | +0.0017 | 0.1743 | 0.1971 |
| False_short | 0.1 | 1 | 0.0032 | 0.0022 | +0.0011 | 0.1098 | 0.1216 |
| True_medium | 0.3 | 0 | 0.0009 | 0.0318 | -0.0309 | 0.1343 | 0.1349 |
| True_medium | 0.3 | 1 | 0.0116 | 0.0045 | +0.0071 | 0.0807 | 0.0749 |
| True_short | 0.6 | 0 | 0.0592 | 0.0384 | +0.0208 | 0.2181 | 0.2055 |
| True_short | 0.6 | 1 | 0.0081 | 0.0186 | -0.0105 | 0.1237 | 0.1372 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0078 | 0.0072 | 0.0150 |
| 200 | Global | 0.0012 | 0.0239 | 0.0251 |
| 200 | Strat MLE | 0.0009 | 0.0919 | 0.0928 |
| 200 | HB EC-HTE | 0.0012 | 0.0840 | 0.0852 |
| 500 | Naive | 0.0078 | 0.0072 | 0.0150 |
| 500 | Global | 0.0005 | 0.0202 | 0.0207 |
| 500 | Strat MLE | 0.0005 | 0.0350 | 0.0355 |
| 500 | HB EC-HTE | 0.0003 | 0.0344 | 0.0347 |
| 1000 | Naive | 0.0078 | 0.0072 | 0.0150 |
| 1000 | Global | 0.0006 | 0.0189 | 0.0194 |
| 1000 | Strat MLE | 0.0005 | 0.0228 | 0.0233 |
| 1000 | HB EC-HTE | 0.0004 | 0.0226 | 0.0230 |

## Cross-Model Comparison: Gemma vs Qwen vs Llama

### CM Heterogeneity

| Metric | Gemma-2-9B | Qwen2.5-7B | Llama3.1-8B |
|--------|-----------|-----------|------------|
| Δ_FPR (max-min) | 0.1046 | 0.2410 | 0.2190 |
| Δ_FNR (max-min) | 0.2299 | 0.1490 | 0.1290 |
| Mean Δ_error | 0.1673 | 0.1950 | 0.1740 |

### Bias Comparison

| n_expert | Gemma |Bias|_Global | Gemma |Bias|_ECHTE | Gemma Δ|Bias| | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
|----------|------------------|--------------------|--------------|--------------------|--------------------|--------------|--------------------|--------------------|--------------| 
| 200 | 0.0261 | 0.0269 | -0.0008 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |
| 500 | 0.0153 | 0.0117 | +0.0036 | 0.0336 | 0.0196 | +0.0140 | 0.0314 | 0.0099 | +0.0215 |
| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.0328 | 0.0165 | +0.0163 | 0.0286 | 0.0130 | +0.0156 |

### RMSE Comparison

| n_expert | Gemma RMSE_Global | Gemma RMSE_ECHTE | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
|----------|-----------------|----------------|-----------------|----------------|------------------|-----------------|
| 200 | 0.1498 | 0.2614 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |
| 500 | 0.1353 | 0.1741 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |
| 1000 | 0.1310 | 0.1435 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |

## Conclusion

EC-HTE wins on |Bias| in 1/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE outperforms Global in bias at 1 of 3 budget levels.**

**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets; Gemma EC-HTE wins in 1/3 budgets.

Average Δ|Bias| (Global - EC-HTE): Gemma = +0.0009, Qwen = +0.0132, Llama = +0.0163
Ranking by EC-HTE improvement: Llama > Qwen > Gemma
