# EXP-004 Incremental Analysis: 4PL+γ Simulation Sweep

**Date**: 2026-05-14 | **Status**: 27/120 runs complete (22.5%)

## Progress

| Condition | Seeds Done | Status |
|-----------|-----------|--------|
| auc0.55_n20_prior1.0_binary | 10/10 | ✓ Complete |
| auc0.55_n50_prior1.0_binary | 10/10 | ✓ Complete |
| auc0.55_n100_prior1.0_binary | 6/10 | Running |
| auc0.8_n50_prior1.0_binary | 1/10 | Running |
| 8 other conditions | 0/10 | Not started |

Sweep order follows SUBSET grid: AUC ∈ {0.55, 0.65, 0.80, 0.90} × N_models ∈ {20, 50, 100}, prior_sd=1.0, binary exposure.

## Main Results

### γ Recovery Table

| Condition | Seeds | γ Bias | γ RMSE | CI95 Width | Cov95 | Cov80 | 0∉CI | θ Corr |
|-----------|-------|--------|--------|------------|-------|-------|------|--------|
| AUC=0.55, N=20 | 10 | +0.020 | 0.040 | 13.3pp | 80% | 80% | 100% | 0.958 |
| AUC=0.55, N=50 | 10 | +0.015 | 0.026 | 8.7pp | 90% | 70% | 100% | 0.947 |
| AUC=0.55, N=100 | 6 | −0.003 | 0.004 | 6.5pp | 100% | 100% | 100% | 0.950 |
| AUC=0.80, N=50 | 1* | +0.008 | 0.008 | 16.2pp | 100% | 100% | 100% | 0.945 |

*1 seed only — treat as preliminary.

### N_models Effect (AUC=0.55, complete data)

CI95 width scaling: 13.3pp (N=20) → 8.7pp (N=50) → 6.5pp (N=100)

Width ratio N=20/N=100 = **2.04** (expected 2.24 under √N scaling). Close to theoretical rate.

**Implication**: Even with N=20 models and near-chance exposure signal (AUC=0.55), γ is recovered within ±4pp RMSE and CI width stays below 15pp.

### AUC Effect (preliminary)

AUC=0.80 N=50 shows **wider** CI (16.2pp) than AUC=0.55 N=50 (8.7pp). Only 1 seed — may be noise, but plausible structural explanation: higher-AUC exposure creates stronger collinearity between γ·exposure and item parameters, inflating posterior uncertainty for γ.

**Need more seeds at AUC=0.80 and data at AUC=0.65/0.90 to confirm.**

## Key Findings

1. **γ is identifiable even at AUC=0.55**: Bias ≤ 0.02, RMSE ≤ 0.04, 100% power (CI excludes 0 in all runs). The identifiability boundary is likely below AUC=0.55.

2. **N_models dominates precision**: CI width scales ≈ 1/√N. At N=100, CI width = 6.5pp — very tight recovery.

3. **MCMC quality flawless**: 0 divergences, all Rhat < 1.011 across 27 runs.

4. **Coverage slightly below nominal at small N**: 80% coverage at N=20 (expected 95%) suggests mild positive bias inflation with few models. Improves to 90% at N=50 and 100% at N=100.

5. **AUC=0.80 CI width anomaly**: If confirmed with more seeds, this would mean the "harder" regime for γ recovery is not low-AUC but high-AUC — a counterintuitive finding worth investigating.

## AUC Threshold Estimate

**Cannot determine yet.** All tested AUC values yield CI width ≤ 16.2pp. The 15pp threshold crossing appears to be:
- **Below AUC=0.55** for N≥50 (current data already under threshold)
- Around **AUC=0.55** for N=20 (13.3pp, just under)
- Possibly **above AUC=0.55** for high-AUC conditions (if 16.2pp at AUC=0.80 holds)

The sweep needs AUC=0.65 and AUC=0.90 data to map the full landscape.

## Estimated Time to Completion

Average fit time: ~320s (N=20), ~1300s (N=50), ~3400s (N=100).
Remaining: 93 runs. Rough ETA: 30-50 hours depending on condition mix.

## MCMC Diagnostics

| Condition | Divergences | Max Rhat | Avg Fit Time |
|-----------|------------|----------|-------------|
| AUC=0.55, N=20 | 0 | 1.008 | 321s |
| AUC=0.55, N=50 | 0 | 1.008 | 1294s |
| AUC=0.55, N=100 | 0 | 1.010 | 3376s |
| AUC=0.80, N=50 | 0 | 1.006 | 659s |
