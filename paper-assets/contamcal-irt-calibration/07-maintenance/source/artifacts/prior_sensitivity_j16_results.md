# Prior Sensitivity Rerun (j16 Model Pool)

## Model Pool (N=16)

**Qwen2.5-1.5B (8):**
- d000_s123, d000_s42, d005_s123, d005_s42, d025_s123, d025_s42, d100_s123, d100_s42

**Qwen2.5-3B (8):**
- d000_s123, d000_s42_a32, d005_s123, d005_s42_a32, d025_s123, d025_v3_s42, d100_a32_s123, d100_a32_s42

Items: 2000 (MMLU social_sciences)

## Results

| Prior | σ | γ̂ mean | γ̂ median | SD | 95% CI | P(γ<0) | > 99.375%? | PPP | min ESS | max R̂ | Divergences | Time |
|-------|---|--------|----------|----|--------|--------|------------|-----|---------|--------|-------------|------|
| Tight | 0.5 | -0.541 | -0.539 | 0.213 | [-0.955, -0.129] | 99.35% | **No** (−0.025pp) | 0.658 | 1473 | 1.008 | 0 | 604s |
| Baseline | 1.0 | -0.627 | -0.627 | 0.226 | [-1.073, -0.192] | 99.68% | **Yes** (+0.305pp) | 0.722 | 1465 | 1.006 | 0 | 596s |
| Loose | 2.0 | -0.654 | -0.655 | 0.231 | [-1.098, -0.207] | 99.85% | **Yes** (+0.475pp) | 0.744 | 1373 | 1.008 | 0 | 603s |

Bonferroni threshold = 99.375% = 1 − 0.05/8

## Judgment

**Option A fails.** Tight prior (σ=0.5) yields P(γ<0) = 99.35%, which is 0.025pp below the Bonferroni threshold of 99.375%. Baseline and loose priors pass comfortably.

→ Proceed to Option B.

## Diagnostics Summary

All three fits are clean:
- 0 divergent transitions across all priors
- R̂ ≤ 1.008 (all below 1.01 threshold)
- ESS ≥ 1373 (all well above minimum)
- PPP range 0.658–0.744 (adequate model fit)
- Residual MAE ≈ 0.021 across all priors

## Comparison with Prior Results

| Setting | Model Pool | γ̂ | P(γ<0) | Passes Bonferroni? |
|---------|-----------|-----|--------|-------------------|
| Old Table 10 baseline (no05b pool) | ~10 models | -0.497 | 98.48% | No |
| **New baseline σ=1.0 (j16 pool)** | 16 models | **-0.627** | **99.68%** | **Yes** |
| §5.7 main analysis (j16 pool) | 16 models | -0.627 | 99.675% | Yes |

The new j16 baseline (σ=1.0) is consistent with the §5.7 main analysis (γ̂ = −0.627 vs −0.627, P(γ<0) = 99.68% vs 99.675%), confirming reproducibility. The improvement over the old no05b pool (98.48% → 99.68%) is driven by the larger model pool (10 → 16).

## Key Observation

The tight prior (σ=0.5) shrinks γ̂ toward zero (−0.541 vs −0.627/−0.654), which is expected behavior — a tighter prior regularizes more strongly. The 0.025pp shortfall is marginal but sufficient to invalidate the "all priors pass" claim required by Option A.
