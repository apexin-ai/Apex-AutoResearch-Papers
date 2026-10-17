Unified Baseline Comparison (70/15/15 split, same test set)

| Method | 4-class Acc | 95% CI | 3-class Acc | MAE |
|--------|------------|--------|-------------|-----|
| CE-MLP (DCOL ablation) | **0.7897** | [0.774, 0.804] | **0.7204** | 0.2280 |
| DivEye (XGBoost) | 0.7817 | [0.766, 0.797] | 0.7098 | 0.2363 |
| Random Forest | 0.7813 | [0.766, 0.797] | 0.7093 | 0.2387 |
| CORAL Ordinal | 0.7807 | [0.765, 0.795] | 0.7089 | **0.2273** |
| Logistic Regression | 0.7497 | [0.734, 0.765] | 0.6671 | 0.2767 |
| PPL Regression (multi) | 0.6223 | [0.605, 0.640] | 0.5200 | 0.3890 |
| PPL Regression (single) | 0.2513 | [0.237, 0.267] | 0.3351 | 0.9440 |

RF 80/20 split (0.7815) vs 70/15/15 split (0.7813): Δ=0.0002, negligible → prior results reliable.