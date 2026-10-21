# Logistic Regression Marginal Effects: Supplement to Appendix M

## Summary

We fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich SEs) to the same data used for the LPM analysis. Average marginal effects (AME) provide probability-scale coefficients directly comparable to LPM β's.

## Model 1: Cross-Complexity (DeepSeek-Coder)

`correct ~ formulation × complexity + cluster(problem_id)`, n=56,480, 139 clusters.

| Effect | OR | 95% CI | z | p | AME (pp) |
|--------|-------|-----------|------|-------|----------|
| CWM (function level) | 0.98 | [0.86, 1.12] | −0.29 | 0.771 | −0.2 |
| Repo (main) | 0.82 | [0.40, 1.66] | −0.55 | 0.582 | — |
| CWM × Repo | 0.31 | [0.15, 0.65] | −3.06 | 0.002 | — |
| **CWM effect at repo level** | — | — | — | — | **−21.6** |

**Interpretation:** At function level, CWM and CLS are statistically indistinguishable (OR=0.98, p=0.77; AME=−0.2pp). The CWM×repo interaction is significant (OR=0.31, p=0.002): CWM reduces the odds of correct prediction by 69% at repo level relative to function level. The repo-level AME (−21.6pp) closely matches the LPM coefficient (−21.9pp).

### Comparison with LPM

| Effect | LPM β (pp) | LPM p | Logistic AME (pp) | Logistic p |
|--------|-----------|-------|-------------------|-----------|
| CWM (function) | −0.2 | 0.805 | −0.2 | 0.771 |
| CWM × Repo | −21.9 | <0.001 | −21.6 | 0.002 |

Direction, magnitude, and significance are concordant. The GEE p-value for the interaction (0.002) is larger than the LPM's (<0.001) because GEE sandwich SEs properly account for within-cluster correlation beyond the random intercept, yielding more conservative but more reliable inference at 139 clusters.

## Model 2: Cross-Model (Repo Level)

`correct ~ formulation × model + cluster(problem_id)`, n=78,272, 25 clusters.

| Effect | OR | 95% CI | z | p | AME (pp) |
|--------|-------|-----------|------|-------|----------|
| CWM deficit | 0.30 | [0.15, 0.63] | −3.21 | 0.001 | −21.1 |
| Qwen3-8B | 1.09 | [0.87, 1.35] | 0.76 | 0.449 | +1.5 |
| CWM × Qwen3 | 1.03 | [0.73, 1.46] | 0.18 | 0.860 | n.s. |

**Interpretation:** The CWM deficit (OR=0.30, AME=−21.1pp) is robust. Model identity and the formulation×model interaction do not reach significance in GEE (p=0.449, p=0.860), consistent with the paper's note that the 25-cluster structure limits effective degrees of freedom. The LPM found these effects significant (p=0.002, p=0.006) because MixedLM random-intercept SEs can be anti-conservative when cluster count is small.

### Comparison with LPM

| Effect | LPM β (pp) | LPM p | Logistic AME (pp) | Logistic p |
|--------|-----------|-------|-------------------|-----------|
| CWM deficit | −22.0 | <0.001 | −21.1 | 0.001 |
| Qwen3-8B | +1.1 | 0.002 | +1.5 | 0.449 |
| CWM × Qwen3 | +1.6 | 0.006 | n.s. | 0.860 |

The primary finding (CWM deficit ≈ 21pp) is robust across specifications. Secondary effects (model identity, interaction) are significant in LPM but not in GEE, reflecting the GEE's more appropriate handling of the small cluster count (k=25).

## Proposed Appendix Text

Add after the existing LPM paragraph in Appendix M:

> **Logistic regression robustness check.** To verify that LPM conclusions are not artifacts of the linear link function, we fit GEE logistic regression (binomial family, exchangeable working correlation, robust sandwich standard errors) to the same data. For the cross-complexity model, the CWM main effect at function level has OR=0.98 (95\% CI [0.86, 1.12], $p{=}0.771$) and the CWM$\times$repo interaction has OR=0.31 ([0.15, 0.65], $p{=}0.002$). Average marginal effects are $-$0.2\pp{} (function) and $-$21.6\pp{} (repo), matching LPM coefficients within 0.3\pp{}. For the cross-model model, the CWM deficit has OR=0.30 ([0.15, 0.63], $p{=}0.001$, AME=$-$21.1\pp{}). Direction, magnitude, and significance of all primary effects are concordant between LPM and logistic regression; minor discrepancies in secondary effects (model identity, formulation$\times$model) reflect the GEE's more conservative cluster-robust inference with $k{=}25$ clusters.

## LaTeX Table (Optional)

```latex
\begin{table}[h]
\centering\small
\caption{GEE logistic regression: odds ratios and average marginal effects.}
\label{tab:logistic-robustness}
\begin{tabular}{llrrrl}
\toprule
Model & Effect & OR & 95\% CI & AME (pp) & $p$ \\
\midrule
Cross-complexity & CWM (func.) & 0.98 & [0.86, 1.12] & $-$0.2 & 0.771 \\
                 & CWM$\times$repo & 0.31 & [0.15, 0.65] & $-$21.6 & 0.002 \\
\midrule
Cross-model & CWM deficit & 0.30 & [0.15, 0.63] & $-$21.1 & 0.001 \\
            & Qwen3-8B & 1.09 & [0.87, 1.35] & +1.5 & 0.449 \\
\bottomrule
\end{tabular}
\end{table}
```
