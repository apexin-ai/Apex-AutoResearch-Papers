# S2-Removal Ablation Results — MMLU (N=16, I=300, 2PL+γ)

| Pipeline | MAE | τ | γ_mean [95% CI] | PPP |
|----------|-----|---|-----------------|-----|
| Raw Accuracy | — | -0.058 | — | — |
| Full RRF (S1+S2+S4) | 0.0076 | -0.056 | -0.698 [-1.762, 0.361] | 0.392 |
| No-S2 RRF (S1+S4) | 0.0070 | -0.075 | -0.358 [-1.316, 0.595] | 0.382 |

## Deltas (No-S2 − Full)

- ΔMAE: -0.0005 (No-S2 slightly better)
- Δτ: -0.019

## Diagnostics

| Pipeline | R̂_max | ESS_min | Divergent | Fit time |
|----------|-------|---------|-----------|----------|
| Full RRF | 1.0066 | 1780 | 5 | 54.7s |
| No-S2 | 1.0057 | 1580 | 5 | 56.7s |

## Interpretation

Both γ posteriors include 0 in 95% CI → neither pipeline detects significant contamination effect on MMLU with this model set. Removing S2 (Min-K++) has negligible impact: ΔMAE = -0.0005, both PPP values healthy (~0.39). The S2 signal contributes minimally to calibration on MMLU.
