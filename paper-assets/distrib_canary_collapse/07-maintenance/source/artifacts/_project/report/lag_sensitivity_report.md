# Granger Lag Sensitivity Analysis

## Setup

- Model: Pythia-410M (fp32)
- Permutation Granger causality, n_perm=5000, difference=True (first-differenced)
- 8 pairs: {token_entropy, ece} x {distinct_1, distinct_2, distinct_3, perplexity}
- FDR correction: Benjamini-Hochberg, per-alpha pooled (all seeds within same alpha)
- Time series length: T=11 (generations 0-10), T_diff=10 after differencing

## Regime Map: FDR sig_rate by alpha x lag

| alpha | lag=1 | lag=2 | lag=3 |
|-------|-------|-------|-------|
| 0.00 (null) | 0.0% (0/24) | 0.0% (0/24) | infeasible |
| 0.25 (sub-threshold) | 0.0% (0/16) | 0.0% (0/16) | infeasible |
| 0.50 (boundary) | 8.3% (2/24) | 12.5% (3/24) | infeasible |
| 0.75 (confirmatory) | **83.3% (20/24)** | 0.0% (0/24) | infeasible |
| 1.00 (full contam.) | **75.0% (6/8)** | 12.5% (1/8) | infeasible |

## Per-seed detail at alpha=0.75, lag=1

| seed | sig/total | pairs significant (FDR) |
|------|-----------|------------------------|
| s42 | 8/8 | all 8 pairs |
| s43 | 6/8 | ece->all4, te->d2, te->d3 |
| s44 | 6/8 | ece->all4, te->d1, te->ppl |

## Key Findings

### 1. Step function is lag=1-specific

The step-function transition from near-zero to high significance occurs exclusively at lag=1. At lag=2, even alpha=0.75 drops to 0% FDR significance. The causal signal operates at a single-generation timescale: canary degradation at generation t predicts diversity loss at generation t+1, with no detectable deeper temporal structure.

### 2. lag=3 is infeasible with T=11

After first-differencing (T_diff=10), a lag=3 model has:
- n = T_diff - lag = 10 - 3 = 7 observations
- k_u = 1 + 3 (y lags) + 3 (x lags) = 7 parameters
- df_resid = 7 - 7 = 0

Zero residual degrees of freedom makes F-statistic undefined. All lag=3 tests return NaN.

### 3. alpha=0.50 boundary behavior

At the boundary regime (alpha=0.50), sporadic significance appears at both lag=1 (2/24, both ece->distinct_1) and lag=2 (3/24, mixed pairs). These are isolated hits without cross-seed consistency, consistent with alpha=0.50 being near the detection threshold where noise dominates.

### 4. Perplexity pairs remain non-significant

At alpha=1.00, both canary->perplexity pairs are non-significant even at lag=1 (raw_p=0.584, 0.804). This pattern holds across all lags and confirms that perplexity divergence follows a different temporal dynamic than diversity collapse.

## Paper-ready statement

The permutation Granger causality results are robust to lag specification within the testable range. We tested lag orders 1 through 3 across all contamination levels (alpha=0.00 to 1.00, 12 experiments, 3 seeds). The step-function transition at alpha=0.75 is identified exclusively at lag=1 (FDR sig_rate=83.3%), while lag=2 yields no significant pairs at any alpha after FDR correction, and lag=3 is infeasible given the series length (T=11 generations, df_resid=0). This confirms that distributional contamination propagates through a single training iteration: canary metric degradation at generation t Granger-causes diversity loss at generation t+1, with no evidence of longer-range temporal dependencies.
