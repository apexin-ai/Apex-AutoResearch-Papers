# EC-HTE Research Plan

## Goal

Build a reproducible internal validation package for EC-HTE: a correction framework for heterogeneous treatment effect estimation when LLM-generated categorical effect modifiers are misclassified in ways that vary across subgroups.

## Phase 1: Mechanism Smoke Tests

Validate the core structural claim from `docs/PROJECT_BRIEF.md`: pooled/global misclassification correction can increase subgroup CATE bias when subgroup error rates are positively aligned with CATE heterogeneity.

Initial experiment:
- `e001_global_correction_smoke`: synthetic k-subgroup DGP with known CATEs and subgroup-specific misclassification.
- Compare uncorrected, pooled/global correction, and oracle subgroup-specific correction.
- Primary metrics: subgroup CATE RMSE, mean absolute subgroup bias, and the rate at which global correction is worse than uncorrected.

## Phase 2: Budgeted Confusion Estimation

Replace oracle confusion matrices with expert-label subsamples under budgets B in `{100, 500, 1000, 2000}`.

Comparisons:
- Global confusion estimate.
- Per-subgroup independent confusion estimate.
- Hierarchical partial-pooling confusion estimate.

Primary metrics:
- CATE RMSE.
- Confusion matrix recovery error.
- Budget curve by B.

## Phase 3: Inference And Allocation

Add variance estimation and adaptive expert allocation.

Comparisons:
- Naive confidence intervals.
- Bootstrap confidence intervals.
- Sandwich-adjusted intervals.
- Uniform vs. adaptive annotation allocation.

Primary metrics:
- 95% CI coverage.
- CI width at fixed coverage.
- PEHE and GATE RMSE under fixed budget.

## Phase 4: Robustness Package

Scale semi-synthetic evaluation across DGP factors:
- Misclassification severity.
- CATE heterogeneity magnitude.
- Subgroup count.
- Positive vs. negative misclassification-CATE correlation.
- Alternative CATE estimators.

Deliverables:
- Reproducible scripts.
- Result JSON/CSV files.
- Internal technical summary for Director to integrate into `findings.md`.
