# test_eval_4b_rsft_s44_no_evi_r2 Analysis

## Core Metrics

| Metric | Value |
|--------|-------|
| Ign-F1 | 0.2671 |
| F1 | 0.2671 |
| Precision | 0.3444 |
| Recall | 0.2182 |
| Format OK Rate | 99.8% (499/500) |
| Truncated | 216/500 (43.2%) |
| Documents | 500 |
| Predictions | 26,487 |
| Inference Time | 10,139.8s (2h49m) |

## Evidence Tax — This Seed (s44)

| Condition | Ign-F1 |
|-----------|--------|
| No-evidence | 0.2671 |
| With-evidence | 0.2525 |
| **Evidence tax** | **+1.46pp** |

## Evidence Tax — 3-Seed Summary

| Seed | No-evi | With-evi | Tax (pp) |
|------|--------|----------|----------|
| s42 | 0.2652 | 0.2501 | +1.51 |
| s43 | 0.2702 | 0.2503 | +1.99 |
| s44 | 0.2671 | 0.2525 | +1.46 |
| **Mean** | **0.2675±0.0025** | **0.2510±0.0013** | **+1.65±0.29** |

All 3 seeds show positive evidence tax (no-evidence > with-evidence), confirming that requiring evidence output consistently hurts RE F1 by ~1.65pp on the 4B model.

## Cross-Seed Comparison

- s44 no-evi (0.2671) falls between s42 (0.2652) and s43 (0.2702), consistent with prior seeds.
- s44 evidence tax (+1.46pp) is the smallest of the 3 seeds but within 1 std of the mean.
- Truncation rate (43.2%) is typical for 4B no-evidence evals.
- No errors, no anomalies in the run.
