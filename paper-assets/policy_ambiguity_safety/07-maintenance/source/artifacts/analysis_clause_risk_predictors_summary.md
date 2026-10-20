# Clause-Level Risk Predictors

## Data
- **N** = 300 clauses (ambiguous condition, mean violation rate across 5 models)
- **DV**: mean violation rate (range: 0.00–1.00, M=0.410, SD=0.351)

## Model Comparison

| Model | R² | Adj R² |
|-------|---:|-------:|
| Linguistic features only | 0.0694 | 0.0372 |
| Type dummies only | 0.0367 | 0.0203 |
| Full (linguistic + type) | 0.0874 | 0.0392 |

- **Incremental R² of type** (given linguistic features): 0.0179
- **Incremental R² of linguistic features** (given type): 0.0507

## Significant Predictors (Linguistic-Only Model, p < .05)

| Feature | Coef | Std β | p |
|---------|-----:|------:|--:|
| (none at α=.05) | — | — | — |

## Random Forest Feature Importance

R² (in-sample) = 0.3955

| Rank | Feature | Importance |
|-----:|---------|----------:|
| 1 | length_ratio | 0.2312 |
| 2 | polysemous_ratio | 0.2259 |
| 3 | token_delta | 0.2077 |
| 4 | token_length | 0.1524 |
| 5 | n_modals | 0.0545 |
| 6 | n_connectives | 0.0360 |
| 7 | domain | 0.0326 |
| 8 | nested_clauses | 0.0290 |
| 9 | n_negations | 0.0179 |
| 10 | n_conditionals | 0.0126 |

## Top Predictors (Combined Evidence)

1. **length_ratio** — β=0.053 (n.s.), RF importance=0.2312 ↑
2. **polysemous_ratio** — β=0.005 (n.s.), RF importance=0.2259 ↑
3. **token_delta** — β=0.038 (n.s.), RF importance=0.2077 ↑
4. **token_length** — β=0.030 (n.s.), RF importance=0.1524 ↑
5. **n_modals** — β=-0.033 (n.s.), RF importance=0.0545 ↓

## Key Finding

Linguistic features (R²=0.0694) explain more clause-level violation variance than ambiguity type alone (R²=0.0367). Type adds only ΔR²=0.0179 beyond linguistic features, suggesting that type effects are largely mediated by surface-level textual properties.

Clauses that are more dangerous tend to be not strongly predicted by any single linguistic feature at α=.05 — risk is distributed across multiple weak predictors.
