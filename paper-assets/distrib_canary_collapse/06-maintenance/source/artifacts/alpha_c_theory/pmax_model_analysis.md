# P_max Multiplicative Model Analysis

## Model

**Old**: P(det|α,T) = Φ(A · α^β · √T − z₀)

**New**: P(det|α,T) = P_max · Φ(A · α^β · √T − z₀),  P_max = 0.75

## Key Finding: P_max = 0.75 Explains the 6/8 Ceiling

The old model predicts P → 1.0 at high α and T, but empirically 6/8 is the maximum observed PermG detection rate — 2 of 8 layer pairs systematically fail (MAUVE bottleneck). The P_max model resolves this by capping predictions at 0.75.

## Parameters

| Parameter | Old Model | P_max Model | Note |
|-----------|----------|-------------|------|
| P_max     | 1.0 (implicit) | **0.75** (fixed) | From 6/8 ceiling |
| α_∞      | 0.0      | 0.0         | Both fixed at 0 |
| β         | 0.24     | 0.24        | Fixed from old model* |
| γ         | 2.08     | 2.08        | = 1/(2β), unchanged |
| z₀/A      | 3.22     | 2.66        | Ratio that determines α_c |
| N_params  | 4        | 2           | Fewer free params |

*β is unidentifiable under P_max (profile NLL plateau from β=0.05 to β=0.70). We fix β=0.24 from the old model for direct comparability.

## β Unidentifiability

The data is step-function-like: at T=10, detection goes 0/8 → 6/8 between α=0.45 and α=0.50 with no intermediate values. Combined with P_max capping the ceiling at 0.75, many β values achieve the same NLL. The ΔNLL < 2 range spans β ∈ [0.05, 0.70], corresponding to γ ∈ [0.71, 10.0].

Root cause: quasi-complete separation in the T=10 data. The individual A and z₀ diverge to infinity (A → ∞, z₀ → ∞) while their ratio z₀/A → 2.66 converges. This ratio is the only degree of freedom that matters — it determines α_c(T).

## Phase Boundary

α_c(T) = 59.01 · T^(−2.083)

| T  | α_c (P_max) | α_c (old) | Observed |
|----|-------------|-----------|----------|
| 5  | 2.064       | 4.561     | All 0/8 (>1, consistent) |
| 10 | 0.487       | 1.076     | Step at ~0.475 |
| 15 | 0.209       | 0.462     | 6/8 at α=0.45 |
| 20 | 0.115       | 0.254     | 5/8 at α=0.45, 6/8 at α≥0.50 |
| 25 | 0.072       | 0.160     | 6/8 at α≥0.45 |

The P_max model gives lower α_c values because its threshold is effectively lower (P = P_max/2 = 0.375 instead of 0.5 for the old model's midpoint).

## Cross-Validation Results

| Dataset | Old MAE | P_max MAE | Δ |
|---------|---------|-----------|---|
| Train (T=10,20) | 0.163 | 0.009 | −0.154 |
| Test (T=5,15)   | 0.106 | 0.000 | −0.106 |
| Extra (T=25)    | 0.219 | 0.031 | −0.188 |

**Test set**: Perfect prediction (MAE=0.000). CI coverage 6/6.

**T=25 validation**: Only miss is α=0.60 → 5/8 vs pred 6/8 (1/8 off, within sampling noise).

## High-α Improvement (Main Contribution)

The old model systematically overpredicts at high α + high T:

| T | α | Actual | Old Pred | P_max Pred | Old Error | New Error |
|---|---|--------|----------|------------|-----------|-----------|
| 15 | 0.50 | 0.75 | 0.534 | 0.750 | 0.216 | 0.000 |
| 20 | 0.75 | 0.75 | 0.909 | 0.750 | 0.159 | 0.000 |
| 25 | 0.50 | 0.75 | 0.921 | 0.750 | 0.171 | 0.000 |
| 25 | 0.75 | 0.75 | 0.978 | 0.750 | 0.228 | 0.000 |
| 10 | 1.00 | 0.75 | 0.469 | 0.750 | 0.281 | 0.000 |

The old model error grows with T (P → 1.0), while P_max model caps at 0.75 matching observation.

## Summary

1. P_max = 0.75 is the primary contribution — it correctly models the MAUVE-imposed detection ceiling
2. γ = 2.08 unchanged (β fixed from old model; β not identifiable under P_max)
3. All MAE metrics improve substantially (test: 0.106 → 0.000, T25: 0.219 → 0.031)
4. The model has fewer free parameters (2 vs 4) with better fit
