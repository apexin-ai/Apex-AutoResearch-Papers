# exp002 negative mechanism audit

## 被证伪 hypothesis

被证伪的是 `exp_002_gpu_dgp_grid` 的 grid-level operational hypothesis：在系统变化 subgroup misclassification heterogeneity 与 CATE heterogeneity 后，positive correlation between error and treatment effect 应使 oracle global confusion correction 比 uncorrected annotations 更常变差，而 negative-correlation controls 不应同样退化。该 hypothesis 未通过 `exp_002_gpu_dgp_grid` registry success rule。

这不等于证伪 `exp_001_bias_bound_mvp` 的 single-DGP counterexample。`exp_001_bias_bound_mvp` 仍支持单点 worst-case 机制；`exp_002_gpu_dgp_grid` 证伪的是当前 grid construction、correction algebra 与 aggregation criterion 下的泛化版本。

## 核心指标

`exp_002_gpu_dgp_grid` formal artifact 显示：conditions = 192、replications_per_condition = 200、device = cuda、elapsed_seconds = 51.99，均来自 `exp_002_gpu_dgp_grid` summary/registry。

`exp_002_gpu_dgp_grid` primary metric `global_worse_rate_difference_positive_minus_negative` = -0.004999995231628418，bootstrap 95% CI = [-0.08526039123535156, 0.08000001311302185]。它没有达到 positive conditions 至少高出 negative controls 20 percentage points 且 CI lower bound > 0 的 `exp_002_gpu_dgp_grid` success rule。

`exp_002_gpu_dgp_grid` secondary metric `bias_bound_vs_global_worse_spearman` = -0.6201611161231995，bootstrap 95% CI = [-0.6645349264144897, -0.4831351935863495]。方向与 `exp_002_gpu_dgp_grid` success rule 要求的 positive rank correlation 相反。

`exp_002_gpu_dgp_grid` estimated-vs-oracle gap `estimated_global_minus_oracle_global_gate_rmse` = 0.0007658914546482265。该数值说明当前 negative result 主要不是 expert-budget finite-sample estimation noise，而是 oracle/global algebra 与 DGP/metric interaction 的问题。

`exp_001_bias_bound_mvp` 对照：`oracle_global_minus_uncorrected_gate_rmse` = 0.6646851460664368，bootstrap 95% CI = [0.6574673897400952, 0.6717956725076197]；`estimated_global_minus_oracle_global_gate_rmse` = 0.018088719196506182，bootstrap 95% CI = [0.005477944594796951, 0.03140296703176313]。这些 `exp_001_bias_bound_mvp` 指标解释了为什么 exp001 success 与 exp002 negative 可以同时成立：它们不是同一 algebra/weighting/aggregation problem。

## 证伪粒度

结论不是 "完全不 work"。`exp_002_gpu_dgp_grid` condition-level artifact 显示局部条件仍会出现 oracle global worse than uncorrected，但这些局部模式没有按 positive-vs-negative correlation 形成 grid-level separation。

`exp_002_gpu_dgp_grid` matched positive-negative pair audit：matched pairs = 96；positive-minus-negative `oracle_global_worse_rate` mean = -0.004999998636776581；positive-delta pairs = 36；zero-delta pairs = 2；negative-delta pairs = 58。该证据说明有效性是局部的，而不是 H1 grid-level monotone pattern。

`exp_002_gpu_dgp_grid` condition-level mean RMSE audit：mean `oracle_global_gate_rmse > uncorrected_gate_rmse` 的 conditions = 96，mean `oracle_global_gate_rmse <= uncorrected_gate_rmse` 的 conditions = 96。worse-condition `oracle_global_worse_rate` range = [0.39499998092651367, 0.9799999594688416]；better/equal-condition `oracle_global_worse_rate` range = [0.014999999664723873, 0.4599999785423279]。

局部有效 pattern 主要是 low CATE heterogeneity，而不是 positive correlation 本身：`exp_002_gpu_dgp_grid` low-CATE conditions 的 positive `oracle_global_worse_rate` mean = 0.6684、negative mean = 0.6742；high-CATE conditions 的 positive mean = 0.2157、negative mean = 0.2200。也就是说，`exp_002_gpu_dgp_grid` 的 "global worse" 更受 CATE heterogeneity scale 与 sampling noise/normalization 影响，而不是受 positive-vs-negative direction 主导。

更细的 `exp_002_gpu_dgp_grid` pattern：

- `misclassification_heterogeneity=high, cate_heterogeneity=low, k=6`：positive `oracle_global_worse_rate` mean = 0.8404，negative mean = 0.8554；这类条件 global correction 常变差，但 negative controls 同样或更强。
- `misclassification_heterogeneity=low, cate_heterogeneity=low, k=6`：positive `oracle_global_worse_rate` mean = 0.8483，negative mean = 0.8612；同样是 high worse-rate but no positive-specific separation。
- `misclassification_heterogeneity=low, cate_heterogeneity=high, k=6`：positive `oracle_global_worse_rate` mean = 0.3333，negative mean = 0.3221；这是少数 positive direction 稍高的 aggregate pattern，但幅度远低于 `exp_002_gpu_dgp_grid` success rule。
- `misclassification_heterogeneity=high, cate_heterogeneity=high, k=3`：positive `oracle_global_worse_rate` mean = 0.1192，negative mean = 0.1283；在最接近 "high/high" intuition 的 grid cell 中，`exp_002_gpu_dgp_grid` 反而不支持 global-worse pattern。

`exp_002_gpu_dgp_grid` top matched positive deltas 也显示局部 pattern 不稳定：最大 positive-minus-negative pair delta = 0.09999999403953552，出现在 `misclassification_heterogeneity=high, cate_heterogeneity=low, k=3, n=5000, expert_budget=1000`，positive rate = 0.515、negative rate = 0.415。最大 negative delta = -0.0949999988079071，出现在 `misclassification_heterogeneity=low, cate_heterogeneity=low, k=3, n=10000, expert_budget=1000`，positive rate = 0.295、negative rate = 0.390。两者都不是 high/high mechanism 的 clean confirmation。

## exp001-vs-exp002 差异

Parameter construction differs materially. `exp_001_bias_bound_mvp` uses a deliberately skewed worst-case DGP: `tau_values=[0.0, 4.3, 5.4, 5.5]`、`error_rates=[0.02, 0.06, 0.29, 0.45]`、`group_probs=[0.59, 0.09, 0.14, 0.18]` from `exp_001_bias_bound_mvp`. `exp_002_gpu_dgp_grid` uses uniform true subgroup sampling, CATE ranges centered near 0.5, misclassification ranges `low=[0.10,0.18]` and `high=[0.04,0.36]`, and `k in {3,6}` from `exp_002_gpu_dgp_grid`. The exp001 single point creates severe prior-weighted posterior distortion; exp002 dilutes that into many regimes where uncorrected noise can already be close to the target or global correction acts like a shrinkage transform.

Correction algebra differs and is the strongest mechanism-audit finding. `exp_001_bias_bound_mvp` constructs `posterior_true_given_noisy = P(G | Z)` using both confusion and subgroup prior, then solves `tau_Z = W tau_G` with a pseudo-inverse. `exp_002_gpu_dgp_grid` computes `observed_gate` by noisy labels but then solves `transition.T * tau = observed_gate` directly. For subgroup-varying error rates, observed GATE by noisy label is a posterior-weighted estimand that requires normalization by noisy-label prevalence. Directly inverting `transition.T` is not algebraically equivalent to the exp001 posterior correction, except in special balanced cases. This can flip or mute the intended under/over-correction mechanism.

Subgroup weighting differs. `exp_001_bias_bound_mvp` global confusion uses a group-probability-weighted pooled error, so high-effect minority groups can be over/under-corrected relative to a majority-driven pooled matrix. `exp_002_gpu_dgp_grid` uses `z_true = torch.randint(0, k, ...)`, so subgroup priors are uniform in expectation and the global pooled error is an unweighted mean of subgroup error rates. That removes a large part of exp001's prior-weighted worst-case leverage.

Metric aggregation differs. `exp_001_bias_bound_mvp` primary metric is paired mean `oracle_global_minus_uncorrected_gate_rmse` in one positive high/high DGP. `exp_002_gpu_dgp_grid` primary metric is the difference of mean `oracle_global_worse_rate` between positive and negative condition sets. A condition can have a small positive mean RMSE delta but a high worse-rate, or a negative mean RMSE delta but a nonzero worse-rate. This makes exp002 a direction-discrimination test, not a direct repeat of exp001.

Positive/negative correlation definition differs from the exp001 mechanism. `exp_002_gpu_dgp_grid` defines direction by ranking `error_rates` against `abs(cate)`, but its `bias_bound_score` uses `abs(centered_rate * centered_cate)`, which discards sign. Therefore positive and negative directions can share the same or nearly same diagnostic score. This explains why `exp_002_gpu_dgp_grid` bias-bound Spearman can be negative even when local positive cells exist: the diagnostic measures magnitude coupling, not signed positive-vs-negative coupling.

Oracle-vs-estimated split does not explain exp002 negative. `exp_002_gpu_dgp_grid` estimated-vs-oracle gap is 0.0007658914546482265, while the primary failure is -0.004999995231628418 and the rank diagnostic is -0.6201611161231995. The exp002 failure is therefore not caused by estimated confusion matrix budget noise.

The stratified subgroup comparator is also a warning sign. In `exp_001_bias_bound_mvp`, stratified correction has `gate_rmse=0.08234754252792217` versus uncorrected `gate_rmse=0.26032738576584474`. In `exp_002_gpu_dgp_grid`, aggregated stratified-minus-uncorrected mean is positive for `misclassification_heterogeneity=high, cate_heterogeneity=high` at 0.03885 and positive for `misclassification_heterogeneity=high, cate_heterogeneity=low` at 0.07807. Since the stratified comparator uses the true subgroup transition but the same direct `transition.T` solve, this supports the algebra-mismatch explanation.

## 建议 hypothesis

H1a: If correction is implemented with a posterior-normalized operator `P(G | Z)` and the same subgroup-prior weighting as the estimand, then positive misclassification-CATE correlation will again separate from negative controls in the exp002 grid. This should be tested before interpreting the current exp002 negative as a substantive failure of the EC-HTE mechanism.

H1b: The exp001 mechanism requires both signed positive error-CATE coupling and subgroup-prior imbalance. A balanced-prior grid may not show global correction worse than uncorrected unless the design explicitly varies group probabilities and reports prior-weighted posterior distortion.

H1c: `bias_bound_score` should be signed or decomposed into signed correlation and magnitude terms. A magnitude-only diagnostic cannot distinguish positive and negative correlation controls and should not be the secondary success criterion for H1 directionality.

H1d: Stage1 correction ablations should remain blocked until the Stage0 correction operator is aligned. Otherwise partial pooling may be judged against an algebraically inconsistent "stratified" or "global" correction baseline.

No experiment was created or launched for these hypotheses in this audit.

## Sources read

- Registry entries: `exp_001_bias_bound_mvp`, `exp_002_gpu_dgp_grid`, `exp_003_stage1_correction_ablation`.
- Project files: `ROADMAP.md`, `memory.md`.
- Remote artifacts read over SSH: `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/summary.json`, `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/planned_metrics.json`, `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/condition_metrics.jsonl`, `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/train.log`, `/home/root/ec_hte/artifacts/exp_001_bias_bound_mvp/formal/summary.json`.
- Scripts/config inspected: `repro/exp_001_bias_bound_mvp/run_experiment.py`, `repro/exp_002_gpu_dgp_grid/run_gpu_dgp_grid.py`, `configs/exp_002_gpu_dgp_grid.json`.
