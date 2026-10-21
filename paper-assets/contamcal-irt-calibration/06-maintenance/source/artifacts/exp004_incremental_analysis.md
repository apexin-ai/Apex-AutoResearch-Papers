# EXP-004 Incremental Analysis: 4PL+γ Simulation Sweep (v4)

**Date**: 2026-05-14 | **Status**: 48/120 runs complete (40.0%) | **Previous**: 46/120 (v3)

## Progress

| Condition | Seeds | Status | Δ vs v3 |
|-----------|-------|--------|---------|
| auc0.55_n20_prior1.0_binary | 10/10 | Complete | — |
| auc0.55_n50_prior1.0_binary | 10/10 | Complete | — |
| auc0.55_n100_prior1.0_binary | 7/10 | Running | — |
| auc0.80_n20_prior1.0_binary | 10/10 | Complete | — |
| auc0.80_n50_prior1.0_binary | 10/10 | Complete | +1 seed |
| auc0.80_n100_prior1.0_binary | 1/10 | Running | **NEW** |
| auc0.65_n{20,50,100} | 0/30 | Not started | — |
| auc0.90_n{20,50,100} | 0/30 | Not started | — |

## Table 1: γ Recovery Metrics (All Conditions)

| AUC | N | Seeds | γ̂ Mean | Bias | |Bias| | RMSE | SD(γ̂) | CI Width | Cov95 | Power | θ Corr |
|-----|---|-------|--------|------|-------|------|-------|----------|-------|-------|--------|
| 0.55 | 20 | 10 | 0.520 | +0.020 | 0.020 | 0.040 | 0.037 | 0.133 | 80% | 100% | 0.958 |
| 0.55 | 50 | 10 | 0.515 | +0.015 | 0.015 | 0.026 | 0.022 | 0.087 | 90% | 100% | 0.947 |
| 0.55 | 100 | 7 | 0.497 | −0.003 | 0.003 | 0.005 | 0.004 | 0.064 | 100% | 100% | 0.951 |
| 0.80 | 20 | 10 | 0.484 | −0.016 | 0.016 | 0.081 | 0.083 | 0.258 | 90% | 100% | 0.972 |
| **0.80** | **50** | **10** | **0.506** | **+0.006** | **0.006** | **0.030** | **0.030** | **0.163** | **100%** | **100%** | **0.971** |
| *0.80* | *100* | *1†* | *0.508* | *+0.008* | *0.008* | *—* | *—* | *0.116* | *100%* | *100%* | *0.962* |

Bold = updated since v3 (auc0.8_n50: 9→10 seeds). *Italic* = new (auc0.8_n100). †Single seed, stats unreliable. True γ = 0.5.

## Finding 1: AUC=0.80 CI Width Inflation — CONFIRMED (46 seeds)

| N_models | CI Width (AUC=0.55) | CI Width (AUC=0.80) | Ratio |
|----------|---------------------|---------------------|-------|
| 20 | 0.133 | 0.258 | **1.95×** |
| 50 | 0.087 | 0.163 | **1.87×** |

Posterior SD matches:

| N | Post. SD (AUC=0.55) | Post. SD (AUC=0.80) | Ratio |
|---|---------------------|---------------------|-------|
| 20 | 0.034 | 0.066 | 1.94× |
| 50 | 0.022 | 0.041 | 1.86× |
| 100 | 0.016 | 0.029† | 1.81×† |

†Single seed for AUC=0.80/N=100.

**Mechanism**: higher-AUC exposure is more collinear with latent ability (θ). The model struggles to disentangle "answered correctly because exposed" vs "answered correctly because capable." Better exposure measurement paradoxically increases γ posterior uncertainty.

The ratio is stable across N (1.81–1.95×), confirming the AUC and N effects are **multiplicative** with no interaction. The preliminary N=100 data point continues this pattern.

## Finding 2: 1/√N Scaling

| Transition | AUC | Actual Ratio | Predicted √(N₁/N₂) | Deviation |
|------------|-----|-------------|--------------------|----|
| n20→n50 | 0.55 | 0.656 | 0.632 | +3.8% |
| n50→n100 | 0.55 | 0.739 | 0.707 | +4.5% |
| n20→n100 | 0.55 | 0.485 | 0.447 | +8.4% |
| n20→n50 | 0.80 | 0.630 | 0.632 | −0.3% |
| n20→n100 | 0.80 | 0.449† | 0.447 | +0.4%† |
| n50→n100 | 0.80 | 0.712† | 0.707 | +0.7%† |

1/√N holds within ~4% per transition. The cumulative n20→n100 deviation (+8.4%) indicates a small constant variance floor from the prior, becoming proportionally visible at large N. Still a good first-order approximation for sample size planning.

## Finding 3: Coverage Below Nominal at Small N

| Condition | 95% CI Coverage | Gap from Nominal |
|-----------|----------------|------------------|
| AUC=0.55, N=20 | 80% (8/10) | −15 pp |
| AUC=0.55, N=50 | 90% (9/10) | −5 pp |
| AUC=0.55, N=100 | 100% (7/7) | +5 pp |
| AUC=0.80, N=20 | 90% (9/10) | −5 pp |
| AUC=0.80, N=50 | 100% (10/10) | +5 pp |
| AUC=0.80, N=100† | 100% (1/1) | +5 pp |

Coverage improves monotonically with N. At N=20/AUC=0.55, coverage is notably low (80%), driven by positive-bias outliers (seeds 7, 9: γ̂ ≈ 0.57–0.58).

**Caveat**: binomial 95% CI for 80% coverage at n=10 is [44%, 97%], so this could be noise. Needs more AUC levels to confirm.

Coverage failure detail:

| Condition | Seed | γ̂ | Bias | CI95 |
|-----------|------|-----|------|------|
| AUC=0.55 N=20 | 7 | 0.584 | +0.084 | [0.508, 0.662] |
| AUC=0.55 N=20 | 9 | 0.570 | +0.070 | [0.501, 0.648] |
| AUC=0.55 N=50 | 8 | 0.546 | +0.046 | [0.502, 0.594] |
| AUC=0.80 N=20 | 6 | 0.328 | −0.172 | [0.208, 0.457] |

## Finding 4: Bias Direction

| Condition | Bias | t-stat | Significant? |
|-----------|------|--------|-------------|
| AUC=0.55, N=20 | +0.020 | 1.72 | No |
| AUC=0.55, N=50 | +0.015 | 2.09 | Marginal |
| AUC=0.55, N=100 | −0.003 | 2.23 | Yes* |
| AUC=0.80, N=20 | −0.016 | 0.59 | No |
| AUC=0.80, N=50 | +0.009 | 0.81 | No |

*Significant only because SD is tiny (0.004); absolute bias is negligible.

**Update from v2**: The bias direction reversal (AUC=0.55 positive, AUC=0.80 negative) holds at N=20 but is **not statistically significant**. At larger N, both converge to near-zero. The reversal is likely sampling noise, not a systematic model property. **Downgrading** from a claimed finding to an observation.

## Finding 5: 100% Power

48/48 runs have CI95 excluding zero. Smallest lower CI bound: 0.208 (AUC=0.80, N=20, seed 6 — the extreme outlier). Even the worst case decisively rejects γ=0.

## Finding 6: MCMC Quality

| Metric | Value |
|--------|-------|
| Total divergences | 0 / 48 runs |
| Worst R̂ | 1.010 |
| Min ESS (worst) | 439 |

## Finding 7: θ Recovery

| AUC | N=20 θ_corr | N=50 θ_corr | N=100 θ_corr |
|-----|-------------|-------------|--------------|
| 0.55 | 0.958 | 0.947 | 0.951 |
| 0.80 | 0.972 | 0.971 | 0.962† |

Higher AUC → better θ recovery (Δcorr ≈ +0.02). θ recovery is insensitive to N within AUC.

## Computation Time

| Condition | Avg time/seed |
|-----------|--------------|
| AUC=0.55, N=20 | 321s |
| AUC=0.55, N=50 | 1,295s |
| AUC=0.55, N=100 | 3,793s |
| AUC=0.80, N=20 | 425s |
| AUC=0.80, N=50 | 977s |
| AUC=0.80, N=100 | 4,783s† |

---

## Paper-Ready Claims

### Claim 1: γ identifiable across signal strengths
At AUC=0.55 (near-chance), RMSE ≤ 0.04 (N=20), ≤ 0.005 (N=100). 100% power across all 48 seeds. **Strong.**

### Claim 2: Precision scales as O(1/√N)
CI width ratios match 1/√N within 5% per transition. Verified at two AUC levels. **Strong.**

### Claim 3: Exposure-ability collinearity inflates γ posterior
CI width at AUC=0.80 is 1.87–1.95× AUC=0.55. Ratio stable across N. **Strong, counterintuitive.**

### Claim 4: Robust detection power
48/48 runs detect γ ≠ 0. **Strong.**

### Claim 5: Coverage below nominal at small N
80–90% at N=20. Practitioners should use N≥50. **Moderate** (limited seed count).

### Claim 6: Bias direction reversal (DOWNGRADED)
Not statistically significant. **Weak** — report as observation, not finding.

---

## Still Needed

1. **AUC=0.65 and AUC=0.90** (0/60 seeds): map full AUC→precision curve
2. **AUC=0.80 N=100** (9 more seeds): 1/10 complete, need more for reliable stats
3. **Remaining seeds**: 3 for auc0.55_n100
4. **Prior sensitivity**: only prior_sd=1.0 tested
