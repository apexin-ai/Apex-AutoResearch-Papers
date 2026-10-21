# H6: Remove Phantom Number MAE 0.984

## Summary

Removed the phantom number "MAE 0.984" and the invalid "OBD vs multiclass LightGBM" comparison from the paper. The number had no source in any experimental output (all 0.984 hits in the codebase are AUC values, not MAE). The comparison itself was logically invalid since the OBD pipeline already uses LightGBM as its base classifier.

## Files Modified

### 1. `docs/paper/method.tex` (line 72)

**Before:**
```
OBD achieves lower mean absolute error (MAE) than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression) (Appendix~\ref{sec:computation_cost}).
```

**After:**
```
OBD yields superior pairwise $\auc$ compared to ordinal logistic regression (mean 0.6095 vs.\ 0.4883 across three model families), whose low MAE stems from collapsing predictions toward central depths rather than improved discrimination (Appendix~\ref{sec:computation_cost}).
```

### 2. `artifacts/_project/paper/method.tex` (lines 108-111)

**Before:**
```
We compared OBD-LightGBM against two alternatives: standard (unordered) multiclass LightGBM and ordinal logistic regression (LogisticAT).
OBD-LightGBM achieves lower mean absolute error (MAE) than multiclass LightGBM across all three model families (Qwen-rewrite: 0.984 vs.\ 1.016; Pythia: 1.107 vs.\ 1.140; OLMo: 1.147 vs.\ 1.181).
Ordinal logistic regression yields the lowest MAE overall (e.g., 0.911 on Qwen-rewrite) but at the cost of substantially degraded pairwise discrimination: mean pairwise $\auc$ of 0.4883 versus 0.6095 for OBD-LightGBM, averaged across the three families.
The low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.
```

**After:**
```
We compared OBD-LightGBM against ordinal logistic regression (LogisticAT).
OBD-LightGBM achieves superior pairwise discrimination: mean pairwise $\auc$ of 0.6095 versus 0.4883 for ordinal logistic regression, averaged across the three families.
The low MAE of ordinal logistic regression stems from collapsing predictions toward central depths rather than improved discrimination---a pathology that renders it unsuitable when pairwise depth discriminability is the primary objective.
```

## Other Occurrences Checked

- `docs/paper/figures/gen_fig2_optimized.py` line 37: `0.984` is OLMo's AUC CI lower bound — unrelated, not modified
- `docs/paper/figures/gen_fig3_optimized.py` line 29: same OLMo CI lower bound — unrelated, not modified
- `artifacts/_project/paper/bootstrap_stability_table.tex` line 24: Mistral-7B 0v1 AUC value — unrelated, not modified
- Abstract, Introduction, Conclusion, Appendix: no mention of MAE 0.984

## No New Numbers Introduced

All numbers retained in the rewritten text (0.6095, 0.4883) were already present and refer to validated pairwise AUC comparisons against ordinal logistic regression.
