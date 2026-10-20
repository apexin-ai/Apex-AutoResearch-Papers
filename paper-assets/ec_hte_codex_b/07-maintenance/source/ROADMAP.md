# EC-HTE Roadmap

> 最后更新: 2026-05-31 15:37 UTC | 更新原因: Initialize internal research roadmap after e001 success and resource registration repair

## Objective
Build a reproducible internal validation package for EC-HTE: error-corrected heterogeneous treatment effect estimation when LLM-generated categorical effect modifiers are misclassified differentially across subgroups.

## Current Evidence
- `e001_global_correction_smoke` supports the diagnostic mechanism on a synthetic DGP: in the positive-correlation setting, pooled/global correction has higher subgroup CATE RMSE than uncorrected labels, while oracle subgroup-specific correction lowers RMSE.
- This is a mechanism smoke test only. It uses oracle known transition matrices and should not yet be treated as deployable EC-HTE performance evidence.

## Short-Term Plan
1. Run `e002_budgeted_confusion_estimation` with expert-label budgets `B={100,500,1000,2000}`.
2. Compare global confusion estimation, independent per-subgroup estimation, and hierarchical/partial-pooling estimation.
3. Measure CATE RMSE, subgroup bias, confusion matrix recovery error, and budget curves.
4. Use `e002` to decide whether the Stage 1 partial-pooling design is empirically necessary before moving to inference and allocation.

## Mid-Term Plan
1. Add variance estimation: naive CI vs bootstrap CI vs sandwich-adjusted CI.
2. Add adaptive expert annotation allocation with pilot ratios 10%, 20%, and 30%.
3. Expand semi-synthetic robustness across subgroup count, misclassification severity, CATE heterogeneity magnitude, and correlation direction.
4. Test at least one alternative CATE estimator after the primary causal-forest pipeline is stable.

## Delivery Targets
- Reproducible scripts under `experiments/`.
- Registry-traceable metrics for every quantitative claim.
- Result JSON/CSV artifacts under `docs/results/` or `artifacts/`.
- Director-owned `findings.md` updates based only on registry-backed results.

## Resource Notes
- Project GPU whitelist is `seetacloud-11934/root/cuda:0`.
- `seetacloud-11934` is now registered as a 1-GPU server with NVIDIA RTX PRO 6000 Blackwell Server Edition, 96GB VRAM.
- GPU experiments must use only the configured `cuda:0` whitelist unless Director updates project allocation.

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D014 | 2026-05-31 | Use e010 failure map to test calibrated continuous | e010_selector_seed_threshold_sensitivity, e009_regime_aware_estimator_selection |
| D013 | 2026-05-31 | After e010 negative result, run failure-map diagno | e010_selector_seed_threshold_sensitivity, e009_regime_aware_estimator_selection |
| D012 | 2026-05-31 | Downgrade e009 deployable-selector claim after e01 | e010_selector_seed_threshold_sensitivity, e009_regime_aware_estimator_selection |
| D011 | 2026-05-31 | Treat e009 as deployable regime-aware selector suc | e009_regime_aware_estimator_selection, e008_stage1_dgp_robustness |
| D010 | 2026-05-31 | Treat e008 Stage 1 robustness as mixed and test re | e008_stage1_dgp_robustness |
| D009 | 2026-05-31 | Close targeted allocation branch as seed-sensitive | e007_allocation_stability_multiseed, e006_capped_hybrid_allocation, e002_budgeted_confusion_estimation |
| D008 | 2026-05-31 | Treat e006 capped/hybrid allocation as negative an | e006_capped_hybrid_allocation, e005_targeted_expert_allocation |
| D007 | 2026-05-31 | Treat e005 targeted allocation as success-with-tra | e005_targeted_expert_allocation |
| D006 | 2026-05-31 | Proceed from e004 diagnostic to targeted expert-la | e004_coverage_bias_decomposition |
| D005 | 2026-05-31 | Classify e004 as diagnostic success, not deployabl | e004_coverage_bias_decomposition |

