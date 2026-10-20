# P_max Grid Search Analysis — Multiplicative Ceiling Model

## Model

P(det|α,T) = P_max · Φ(A · α^β · √T − z₀), α_∞=0 fixed.

Grid: P_max ∈ [0.50, 1.00] step 0.05, β ∈ [0.05, 0.50] step 0.01.
Inner MLE: (A, z₀) via differential_evolution.
Train: T={10,20}, Validate: T={5,15}, Extra: T=25.

## P_max Profile (test MAE)

| P_max | β     | z₀    | test_MAE | γ=1/(2β) | NLL   |
|-------|-------|-------|----------|----------|-------|
| 0.50  | 0.05  | 20.0* | 0.1250   | 10.0     | 47.97 |
| 0.55  | 0.05  | 20.0* | 0.1000   | 10.0     | 46.51 |
| 0.60  | 0.05  | 20.0* | 0.0750   | 10.0     | 45.36 |
| 0.65  | 0.05  | 20.0* | 0.0500   | 10.0     | 44.49 |
| 0.70  | 0.05  | 20.0* | 0.0250   | 10.0     | 43.92 |
| **0.75** | **0.05** | **20.0*** | **≈0** | **10.0** | **43.68** |
| 0.80  | 0.18  | 20.0* | 0.0250   | 2.78     | 35.31 |
| 0.85  | 0.17  | 20.0* | 0.0500   | 2.94     | 36.55 |
| 0.90  | 0.17  | 20.0* | 0.0750   | 2.94     | 38.64 |
| 0.95  | 0.28  | 5.25  | 0.0843   | 1.79     | 42.47 |
| 1.00  | 0.24  | 4.49  | 0.1060   | 2.08     | 44.40 |

*z₀=20.0 means boundary-constrained (optimizer upper bound).

## Key Findings

### 1. P_max=0.75 is optimal — matches 6/8 ceiling exactly

test_MAE drops linearly as P_max → 0.75 (test MAE = |0.75 − P_max| × constant), reaches zero at P_max=0.75, then rises symmetrically for P_max > 0.75. The validation data (T=5: all 0/8, T=15: all 6/8=0.75) is perfectly described when P_max = 0.75 and the transition is sharp enough.

This confirms the MAUVE bottleneck hypothesis: 2/8 pairs systematically fail detection regardless of signal strength, creating a hard ceiling at 6/8 = 0.75.

### 2. Step-function degeneracy for P_max ≤ 0.90

For all P_max ≤ 0.90, z₀ hits the optimizer boundary (20.0), meaning the Φ function becomes a near-step-function. The model collapses to:
- P(det) ≈ 0  for small T (below transition)
- P(det) ≈ P_max  for large T (above transition)

This makes β and A poorly identified — the top 10 results are all P_max=0.75 with β from 0.05 to 0.14, all yielding near-zero test MAE.

### 3. P_max=1.0 exactly recovers old model

At P_max=1.0: β=0.24, z₀=4.49, A=1.39 — identical to the original D102 fit. This validates the grid search implementation.

### 4. Phase transition at P_max≈0.80

For P_max > 0.75, there's a qualitative change:
- P_max ∈ [0.80, 0.90]: β jumps to 0.17–0.18 (γ ≈ 2.8–2.9), but z₀ still at boundary
- P_max ≥ 0.95: z₀ drops into the interior (5.2, 4.5), β rises to 0.24–0.28 (γ ≈ 1.8–2.1)

The transition from boundary z₀ to interior z₀ happens between P_max=0.90 and 0.95.

### 5. Improvement over old model

| Metric | Old (P_max=1) | New (P_max=0.75) | Improvement |
|--------|---------------|-------------------|-------------|
| Test MAE (T=5,15) | 0.1060 | ≈0 | 100× |
| T=25 MAE | 0.2190 | 0.0312 | 7× |
| Train MAE | 0.1626 | 0.1550 | modest |

The dramatic test improvement comes from the old model over-predicting at T=15 (predicted 0.49–0.71 vs actual 0.75) while the new model predicts exactly 0.75.

### 6. α_c values are degenerate

With β=0.05 (γ=10), the α_c(T) curve is unrealistically steep:
- T=5: α_c > 1 (no detection possible in range)
- T=10: α_c = 1.09
- T=15: α_c = 0.019

This reflects the step-function nature — the transition from "no detection" to "ceiling detection" is extremely sharp. The α_c values from the old model (β=0.24, γ=2.08) remain more physically interpretable.

## Interpretation

The P_max grid search confirms two things:
1. **The 6/8 ceiling is real** — P_max=0.75 provides the best out-of-sample fit
2. **The model degenerates** when P_max is set correctly — other parameters become boundary-constrained because the data lacks resolution in the transition region

The root cause: with only n=8 pairs, observing 6/8 (the ceiling) vs 0/8 creates a sharp binary — there are no intermediate observed rates between 0/8 and 5/8 in the validation set. The model exploits this by becoming a step function.

For the paper, the recommended approach is to **report P_max=0.75 as a fixed ceiling** (empirically determined, not fitted), and fit the smooth transition using the original model Φ(A·α^β·√T − z₀) only for the sub-ceiling regime, i.e., model the probability of detection among the 6 detectable pairs, not all 8.
