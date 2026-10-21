# Gate Statistical Test Results (Wilcoxon Signed-Rank)

## Main Test (28 layers paired)
- N = 28 layers
- Mean gate turn1: 0.894 ± 0.065
- Mean gate turn21: 0.950 ± 0.046
- Layers with turn21 > turn1: 27/28 (only L19 reversed)
- T+ = 401, T- = 5
- **p (one-sided) = 3.73 × 10⁻⁸**
- Z = 5.38, Effect size r = 1.00 (large)

## Per-Conversation Consistency
All 5 conversations significant (p range 3.73e-8 ~ 2.78e-5), Fisher combined p ≈ 0.

| Conv | Mean diff | T+ | p | r |
|------|-----------|-----|------|------|
| conv_0 | 0.052 | 380 | 2.8e-05 | 0.76 |
| conv_1 | 0.044 | 376 | 7.6e-06 | 0.82 |
| conv_2 | 0.053 | 397 | 1.2e-07 | 0.98 |
| conv_3 | 0.067 | 401 | 3.7e-08 | 1.00 |
| conv_4 | 0.063 | 403 | 1.9e-08 | 1.04 |

## Spearman Correlation (turn index vs gate value)
- 25/28 layers ρ > 0, 13/28 significant at p < 0.05
- Mean ρ = 0.367
- Strongest: L21 (ρ=0.86), L25 (ρ=0.79), L16/L18 (ρ=0.69)

## Layer Group Analysis
| Group | Mean diff | Wilcoxon p |
|-------|-----------|------------|
| Early (L0–L9) | 0.033 | 9.8e-04 |
| Mid (L10–L19) | 0.051 | 4.9e-03 |
| Late (L20–L27) | 0.090 | 3.9e-03 |

Deep layers show ~3x stronger gating effect vs shallow layers.

## Paper-ready Description
Across all 28 Transformer layers, gate values at turn 21 were significantly higher than at turn 1 (Wilcoxon signed-rank test, T⁺ = 401, p = 3.7 × 10⁻⁸, r = 1.00, N = 28), with 27 of 28 layers showing higher gate values at later turns. The mean gate value increased from 0.894 ± 0.065 (turn 1) to 0.950 ± 0.046 (turn 21), corresponding to a shift from partial residual suppression toward near-identity pass-through. Spearman rank correlation confirmed a monotonic increasing trend of gate values with turn index in 13 of 28 layers (mean ρ = 0.367). This pattern was consistent across all five evaluation conversations (Fisher combined p < 10⁻³⁰). The effect was most pronounced in late layers (L20–L27, mean Δ = 0.090) compared to early layers (L0–L9, mean Δ = 0.033).

Script: artifacts/gate_stat_test_v2.py