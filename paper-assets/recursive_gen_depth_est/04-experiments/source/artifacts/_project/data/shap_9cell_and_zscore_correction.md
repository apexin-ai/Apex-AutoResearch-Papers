# SHAP 9-Cell Analysis (R3-N3)

## Aggregated SHAP Top-5
p90_ppl, var_surprisal, p75_ppl, mean_surprisal, mean_ppl

## Feature Category Contribution
| Category | SHAP % |
|----------|--------|
| PPL/surprisal | 88.8% |
| Lexical diversity | 11.2% |

SHAP top-5 = Gini top-5 (order slightly different). Consistency confirmed.

## LR Z-Score Cross-Strategy (corrected numbers)
| Model | raw d1v2 AUC | scaler d1v2 AUC | zscore d1v2 AUC |
|-------|-------------|-----------------|-----------------|
| Pythia | 0.631 | 0.518 | 0.721 |
| GPT-2 XL | 0.500 | 0.238 | 0.561 |
| OLMo | 0.500 | 0.191 | 0.699 |

**Paper claims need correction**: GPT-2 XL paper says 0.68, actual 0.561; OLMo paper says 0.83, actual 0.699.