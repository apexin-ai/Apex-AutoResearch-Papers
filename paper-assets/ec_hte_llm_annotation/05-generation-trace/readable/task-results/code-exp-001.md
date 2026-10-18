# code exp 001

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001_20260520T194547_result.json`
- **Structured JSON:** [`01af7cbe3ff08b030f63.json`](../../sessions/01/01af7cbe3ff08b030f63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The SE for subgroup B's HB RMSE is ~254 (half of 510) — a few catastrophic MC runs dominate the mean. Let me produce the final summary.

---

## Exp-001 HB Synthetic Validation — 100 MC Results

**Sweep**: 3600 runs (3 regimes × 6 n_expert × 2 K × 100 MC), 4136s (~69 min), Gibbs sampler

### MCMC Diagnostics
| Metric | Value | Target |
|--------|-------|--------|
| R-hat > 1.01 | 3.2% of runs | < 1.01 |
| R-hat > 1.02 | 0.2% of runs | |
| ESS < 200 | 0.2% of runs | > 200 |
| Divergences | 0 | 0 |
| Runtime median | 0.86s | |

Convergence is solid overall. The 3.2% of runs above the R-hat target are at the margin (max 1.024), not pathological.

### K=2 Results — Clean
HB Dirichlet consistently matches or slightly beats MLE:

| n_expert | Extreme | Moderate | Homogeneous |
|----------|---------|----------|-------------|
| 50 | **+8.5%** | +1.9% | +2.0% |
| 100 | +1.0% | +0.8% | +0.8% |
| 250 | +0.5% | +0.3% | +0.3% |
| 500+ | ~0% | ~0% | ~0% |

(Positive = HB has lower RMSE than MLE)

### K=4 Results — Mixed
- **n_expert >= 250**: HB beats MLE by 0.1-1.0% across all regimes
- **n_expert 50-100, moderate/homogeneous**: HB beats MLE by 2.8-9.2%
- **n_expert 50-100, extreme**: **Catastrophic blow-up** — a few MC runs produce near-singular mixing matrices after HB pooling, inflating RMSE to 360+ (subgroup B) and 3+ (subgroup A)

### Root Cause of K=4 Extreme Blow-Up
With K=4 and n_expert=50, each subgroup gets ~12 experts. The extreme regime has misclass rates [0.30, 0.20, 0.10, 0.03]. For subgroups A (0.30) and B (0.20), the confusion matrix is already close to singular (high misclass → rows similar). The HB partial pooling occasionally pushes the posterior confusion matrix estimate toward an even more singular configuration. When `invert_mixing` inverts this nearly-singular matrix, small errors in tau_obs get amplified by 100-1000x.

The current guard (`abs(det) < 1e-10`) is too permissive. A determinant of 0.001 still produces condition numbers ~1000x.

### Subgroups C and D are fine
At K=4 extreme n_exp=50, subgroups with lower misclass (C=0.10, D=0.03) show HB beating MLE: RMSE 0.14 vs 0.15.

### Key Takeaways
1. **HB partial pooling works** — modest but consistent improvement over MLE in the well-conditioned regime (K=2 everywhere, K=4 with enough experts)
2. **Gains are largest at small n_expert** where the prior has most influence (8.5% at n_exp=50, K=2 extreme)
3. **Matrix inversion is the bottleneck, not the estimator** — when the mixing matrix condition number is high, ANY correction method is unstable
4. **Practical recommendation**: add a condition number guard to `invert_mixing` (e.g., fall back to naive when cond(M) > 50)

Results saved to `results/exp001_hb_results.csv` (540 rows) and `results/exp001_hb_diagnostics.csv` (3600 rows).

---
