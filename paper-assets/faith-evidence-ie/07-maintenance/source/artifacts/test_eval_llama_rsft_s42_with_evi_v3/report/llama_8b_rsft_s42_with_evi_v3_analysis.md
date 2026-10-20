# LLaMA-3.1-8B RSFT s42 with-evidence test eval v3 — Analysis

## v3 Metrics
- ign_f1: 0.3554
- ign_precision: 0.4792, ign_recall: 0.2825
- evi_f1_joint (DREEAM): 0.2457
- evi_f1 (TP-only): 0.5442
- EDCR: 0.8424
- field_compliance: 499/500 (99.8%)
- format_ok: 500/500
- truncated: 300/500
- n_predictions: 23,717

## Field Compliance Fix
- Old s42: 176/500 (35.2%) → v3: 499/500 (99.8%)
- Now matches s43 level (497/500, 99.4%)
- Confirms old result was confounded by code/data bug

## Cross-seed Comparison (LLaMA 8B RSFT with-evi, test)
| Metric         | s42 (v3) | s43    | Δ       |
|----------------|----------|--------|---------|
| ign_f1         | 0.3554   | 0.3488 | +0.66pp |
| precision      | 0.4792   | 0.4834 | -0.42pp |
| recall         | 0.2825   | 0.2728 | +0.97pp |
| evi_f1_joint   | 0.2457   | 0.2514 | -0.57pp |
| EDCR           | 0.8424   | 0.8425 | ~0      |

Seeds consistent, no anomalies.

## Corrected Evidence Tax (no_evi − with_evi)
| Seed | no-evi   | with-evi     | Tax      |
|------|----------|--------------|----------|
| s42  | 0.3334   | 0.3554 (v3)  | -2.20pp  |
| s43  | 0.3371   | 0.3488       | -1.17pp  |

Both seeds: negative tax → evidence helps.
Old s42 tax was -2.65pp (confounded). Corrected: -2.20pp. Δ = +0.45pp.

## Cross-model Tax Summary (RSFT test, all corrected)
| Model    | s42 tax  | s43 tax  | Direction       |
|----------|----------|----------|-----------------|
| 1.7B     | -5.43pp  | -4.59pp  | evidence helps  |
| 4B       | +1.51pp  | +1.99pp  | evidence hurts  |
| LLaMA 8B | -2.20pp  | -1.17pp  | evidence helps  |
| Phi 8B   | -0.34pp  | -1.74pp  | evidence helps  |
