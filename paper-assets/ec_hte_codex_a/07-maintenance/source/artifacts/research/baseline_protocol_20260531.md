# EC-HTE Baseline Protocol Research Artifact

Created: 2026-05-31 UTC
Project: ec_hte_codex_a
Type: research protocol

## Scope

This artifact summarizes literature-backed evaluation choices and baseline boundaries for first-batch EC-HTE experiments. The durable copy is also written to `memory.md` under `## 领域参考` and `## 首批实验协议`.

## Key Protocol Decisions

- HTE/CATE evaluation must report PEHE, per-subgroup CATE bias, GATE RMSE, empirical 95% CI coverage, CI width, and EC-HTE bound diagnostic product.
- Formal semi-synthetic experiments follow PROJECT_BRIEF.md: `R >= 200`, `N in {2000, 5000, 10000}`, `B in {100, 500, 1000, 2000}`, `k in {3, 6}`, `T ~ Bernoulli(0.5)`.
- Smoke/MVP runs may be smaller, but must be marked as engineering checks and excluded from quantitative claims.
- PPI/DSL/StratPPI/ASI/AM-PPI are valid baselines for population-level estimands or allocation, not direct fixes for categorical effect-modifier misclassification unless subgroup membership error is explicitly modeled.
- Mozer-style arm-specific rectification is an arm-level residual/confusion correction baseline; failure on CATE/GATE should be described as a mismatch to modifier-misclassification structure, not as a broad invalidation of PPI.
- Real-data Rohingya validation only tests differential LLM misclassification and confusion-matrix recovery; it does not establish true CATE accuracy.

## Baseline Matrix

| Experiment | Metrics | Baselines | Minimum formal scale | Cost note |
|---|---|---|---|---|
| MVP / Stage 0 bias-bound mechanism | subgroup CATE bias, GATE RMSE, diagnostic product, optional PEHE | uncorrected, global confusion, oracle/stratified correction | `N=2000`, `k=3`, `R>=200` | CPU-only low |
| Stage 1 partial pooling | confusion recovery, PEHE, GATE RMSE, subgroup bias, budget curve | global, per-subgroup independent, hierarchical partial pooling, oracle | `N in {2000,5000}`, `B in {100,500,1000,2000}`, `k in {3,6}`, `R>=200` | CPU medium; VI primary |
| Stage 2 CI | empirical 95% coverage, CI width, GATE RMSE, PEHE | naive CI, sandwich-adjusted CI, bootstrap CI | `N in {2000,5000,10000}`, `B in {500,1000,2000}`, `R>=200` | CPU medium-high; bootstrap dominates |
| Stage 3 allocation | PEHE at fixed B, GATE RMSE, subgroup bias, allocation share | uniform, misclassification-only, CATE-only, joint criterion, pilot ratios 10/20/30% | `B in {100,500,1000,2000}`, `R>=200` | CPU medium |
| Real-data validation | subgroup error gaps, confusion recovery, calibration loss, budget curve | global, per-subgroup independent, partial pooling, calibration/probability modifier | `B in {100,500,1000,2000}`; subgroups refugee status/gender/education | CPU/data-cleaning medium |

## Primary Sources

- Wager & Athey, JASA 2018 / arXiv:1510.04342: https://arxiv.org/abs/1510.04342
- GRF causal forest documentation: https://grf-labs.github.io/grf/reference/causal_forest.html
- Curth et al., NeurIPS D&B 2021: https://openreview.net/forum?id=FQLzQqGEAH
- Shalit et al., ICML 2017: https://proceedings.mlr.press/v70/shalit17a.html
- PPI, Angelopoulos et al., Science 2023 / arXiv:2301.09633: https://arxiv.org/abs/2301.09633
- DSL, Egami et al., NeurIPS 2023 / arXiv:2306.04746: https://arxiv.org/abs/2306.04746
- DSL/PPI finite-sample benchmark, de Pieuchon et al., EMNLP 2025: https://aclanthology.org/2025.emnlp-main.1000/
- StratPPI, Fisch et al., NeurIPS 2024: https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9fcd02e6445c7dfbad6986abee53d0d-Abstract-Conference.html
- Active Statistical Inference, Zrnic & Candes, ICML 2024: https://arxiv.org/abs/2403.03208
- AM-PPI, Brawand et al., arXiv:2605.08429: https://arxiv.org/abs/2605.08429
- Mozer, arXiv:2603.19160: https://arxiv.org/abs/2603.19160
- Ashwin et al., Sociological Methods & Research 2025: https://journals.sagepub.com/doi/10.1177/00491241251338246
- Matrix/inverse-matrix misclassification correction: https://pmc.ncbi.nlm.nih.gov/articles/PMC4382468/
- Misclassification SIMEX: https://pubmed.ncbi.nlm.nih.gov/16542233/
