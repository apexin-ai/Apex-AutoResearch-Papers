# Diagnosis: sica_k_sensitivity_14b

## Status: COMPLETED (false failure)

EXIT_CODE=129 (SIGHUP) is a false signal — identical to sica_expanded_14b behavior.
Log evidence: both `K_ABLATION_DONE` and `FULL_MVP_DONE` markers present at log tail.

## Results

All 6 K values completed successfully. Results in `/root/symb_invariant_consensus/results/k_ablation/`:

| K  | SICA Acc | SC Acc | SICA vs SC |
|----|----------|--------|------------|
| 6  | 73.3%    | 73.3%  | 0.0pp      |
| 8  | 73.3%    | 75.0%  | -1.7pp     |
| 11 | 73.3%    | 73.3%  | 0.0pp      |
| 12 | 70.0%    | 75.0%  | -5.0pp     |
| 16 | 71.7%    | 75.0%  | -3.3pp     |
| 20 | 70.0%    | 73.3%  | -3.3pp     |

## Key Findings

1. SICA never outperforms SC at any K value
2. SICA best performance (73.3%) occurs at smaller K (6,8,11) — suggesting more traces add noise rather than signal
3. SC is stable at 73.3-75.0% regardless of K
4. The gap widens with larger K (SICA degrades, SC stays flat)

## Conclusion

Experiment should be marked as **success** (completed normally). Result is **negative** — K-sensitivity analysis further confirms SICA mechanism is vacuous. The constraint-based weighting provides no benefit over simple majority voting regardless of sample size.

## Recommendation

Change cron conclusion from `failed` to `negative` (experiment completed, hypothesis not supported).
