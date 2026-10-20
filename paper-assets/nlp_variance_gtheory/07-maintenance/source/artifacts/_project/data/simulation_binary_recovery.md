Simulation-Based Binary Recovery (MF1 Defense)

Design: 100 reps × 4 accuracy levels × 3 sample sizes, 432 conditions/item, probit latent model

| Metric | Result |
|---|---|
| item_id dominant (excl. residual) | 99-100% |
| Spearman rho (excl. residual) | 0.685-0.734 (mean 0.708) |
| Top-5 systematic set correct | 58-82% (mean 72%) |
| Coverage (95% CI) | 86-100% |

Binary vs Continuous: Spearman rho 0.708 vs 0.703 — binarization does NOT degrade ranking.
Residual inflates from 16% (latent) to ~40% (binary) due to Bernoulli within-cell variance.
Systematic component ordering perfectly preserved.
Bias flat across accuracy levels (0.34-0.42%), no increase at p=0.8.
File: results/analysis/simulation_binary_recovery.json