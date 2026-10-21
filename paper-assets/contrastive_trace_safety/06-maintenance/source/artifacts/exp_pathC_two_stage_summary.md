# Path C: Adaptive Window Two-Stage Detection — Results

## Setup
- Model: R1-8B, Layer 2, hidden_dim=4096
- Train: 131 labeled jailbreak traces, Test: 55 (39 jailbreak, 16 benign)
- Probe: SGDClassifier(log_loss, class_weight=balanced)
- Window sizes: W ∈ {1, 3, 5, 10, 15, 20, 25}

## Single-Stage Results (trace-level detection)

| W  | Precision | Coverage | FPR   | Latency |
|----|-----------|----------|-------|---------|
| 1  | 0.7037    | 0.8462   | 1.000 | 12.2    |
| 3  | 0.7222    | 0.6667   | 0.938 | 8.3     |
| 5  | 0.7091    | 0.6667   | 1.000 | 9.2     |
| 10 | 0.7222    | 0.6667   | 0.938 | 10.0    |
| 15 | 0.7091    | 0.7692   | 1.000 | 8.6     |
| 20 | 0.7222    | 0.7179   | 0.938 | 7.9     |
| 25 | 0.7091    | 0.7436   | 1.000 | 6.0     |

**Single-stage Pareto frontier (3 points):**
- W=1: prec=0.7037, cov=0.8462 (highest coverage)
- W=15: prec=0.7091, cov=0.7692
- W=20: prec=0.7222, cov=0.7179 (highest precision)

## Two-Stage Results

Best configs that **dominate** single-stage Pareto:

| W_screen | W_confirm | k | Precision | Coverage | Dominates |
|----------|-----------|---|-----------|----------|-----------|
| 3        | 15        | 1 | 0.7222    | 0.7692   | W=15, W=20 |
| 3        | 25        | 1 | 0.7222    | 0.7436   | W=20 |

**Best two-stage config: (W_s=3, W_c=15, k=1)**
- Precision: 0.7222 (matches W=20 single-stage)
- Coverage: 0.7692 (matches W=15 single-stage)
- Achieves the precision of W=20 with the coverage of W=15

## Pareto Frontier Comparison

Two-stage points on combined Pareto frontier: 10 configs (extending into higher precision / lower coverage via k≥3).

Key observation: Two-stage (3,15,1) Pareto-dominates single-stage W=15 and W=20, combining the best attributes of both.

## Conclusion: POSITIVE (with caveats)

**The two-stage method achieves marginal Pareto dominance over single-stage.**

Specifically, (W_s=3, W_c=15, k=1):
- +1.3pp precision over W=15 at same coverage (0.7692)
- +5.1pp coverage over W=20 at same precision (0.7222)

**Caveats:**
1. **Small test set (n=55):** The improvements (1-5pp) are within noise margins. Statistical significance is uncertain.
2. **High FPR (93-100%):** All methods flag nearly all benign traces. The probe was trained only on jailbreak traces (step-level pre/post-CP labels) and cannot distinguish benign from pre-CP jailbreak. Trace-level precision is dominated by the jailbreak-to-benign ratio in the test set.
3. **Does NOT dominate W=1:** The best two-stage (cov=0.7692) still falls short of W=1 single-stage (cov=0.8462).
4. **k=1 threshold:** The "confirmation" stage with k=1 is effectively just a second opinion from a larger window probe, not a true consecutive-step confirmation.

**Recommendation:** The two-stage contribution is technically valid but marginal. For the paper, it may be better framed as a "practical deployment strategy" rather than a core methodological contribution. The real value would emerge with a proper benign-vs-jailbreak training setup that reduces FPR.

## Artifacts
- Script: `src/experiments/exp_pathC_two_stage_sim.py`
- Results: `artifacts/exp_pathC_two_stage/results.json`
- Plot: `artifacts/exp_pathC_two_stage/pareto_comparison.pdf`
