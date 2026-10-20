Baseline Battery (src/baselines.py, plan_009)

5 baselines, all dry-run verified:

| Method | 4-class | 3-class | MAE |
|---|---|---|---|
| PPL Regression (single: mean_ppl) | 0.251 | 0.335 | 0.944 |
| PPL Regression (multi: 19-dim OLS) | 0.622 | 0.520 | 0.389 |
| CE-MLP (DCOL ablation, same arch no contrastive) | 0.790 | 0.720 | 0.228 |
| CORAL Ordinal Regression | 0.781 | 0.709 | 0.227 |
| DivEye (XGBoost) | 0.782 | 0.710 | 0.236 |
| RF MVP (reference) | 0.782 | — | — |

Key: CE-MLP ≈ RF ≈ CORAL ≈ DivEye → DCOL contrastive loss is the differentiator.
Single PPL ≈ random → mean_ppl alone cannot discriminate depth.
All methods: d2 recall ~60% (bottleneck).

DivEye TODO: temporal surprisal features (first/second-order ΔS) need raw token-level sequences.
Results: results/baselines/baseline_results.json