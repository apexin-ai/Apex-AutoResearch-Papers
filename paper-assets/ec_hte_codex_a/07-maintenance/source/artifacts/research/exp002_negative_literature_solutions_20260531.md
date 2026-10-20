# exp002 negative literature solution memo

Date: 2026-05-31
Project: ec_hte_codex_a
Target experiment: `exp_002_gpu_dgp_grid`

## Executive decision

Do not launch formal Stage 1 from the current exp002 chain yet. The negative result most likely indicates that the current grid criterion and correction algebra are not isolating the intended heterogeneous-misclassification mechanism. The next useful step is a short mechanism-audit experiment, not a broader H2 run.

Priority path:

1. Replace the direct `P(Z_hat | Z)^T` inverse used for GATE correction with the posterior mixing matrix `P(Z | Z_hat)` or an equivalent prevalence-aware likelihood/EM formulation.
2. Recompute the H1 grid diagnostic using directional, signed subgroup error terms rather than the current magnitude-only bias-bound score.
3. Then test partial pooling only on correction matrices that recover the right estimand; otherwise partial pooling will stabilize the wrong algebra.

## Registry and roadmap confirmation

Registry hypothesis for `exp_002_gpu_dgp_grid`: a GPU-vectorized DGP grid varying subgroup misclassification heterogeneity and CATE heterogeneity should reproduce the EC-HTE bias-bound mechanism: positive correlation between error and treatment effect should make global correction worse than uncorrected annotations, while negative correlation should not show the same degradation.

Operational H1 grid criterion from `ROADMAP.md`:

- Primary metric: `global_worse_rate_difference_positive_minus_negative`.
- Success: positive-correlation conditions' oracle-global-worse rate must be at least 20 percentage points higher than negative-correlation controls, with bootstrap 95% CI lower bound > 0.
- Secondary diagnostic: `bias_bound_vs_global_worse_spearman` must be >= 0.50, with bootstrap 95% CI lower bound > 0.
- Estimated-global must be reported separately from oracle-global.

Observed negative result, source `exp_002_gpu_dgp_grid` registry and `artifacts/exp_002_gpu_dgp_grid/formal/planned_metrics.json`:

- `global_worse_rate_difference_positive_minus_negative = -0.005`, 95% CI `[-0.085, 0.080]`.
- `bias_bound_vs_global_worse_spearman = -0.620`, 95% CI `[-0.665, -0.483]`.
- `estimated_global_minus_oracle_global_gate_rmse = 0.000766`.

Local condition-metric aggregation from `exp_002_gpu_dgp_grid` shows the negative Spearman is driven more by grid axes than by positive-vs-negative direction: mean oracle-global-worse rate was 0.671 for low CATE heterogeneity and 0.218 for high CATE heterogeneity; mean rates were 0.442 for positive and 0.447 for negative. This supports a mechanism-audit interpretation rather than "H1 is globally false."

## Failure modes implied by exp002

### F1. Matrix orientation / estimand mismatch

The exp002 code constructs a row-stochastic transition matrix `C[g,h] = P(Z_hat=h | Z=g)` and applies `solve(C.T, observed_gate)`. For subgroup means/GATEs indexed by observed labels, however, the observed vector is mixed by `P(Z=g | Z_hat=h)`, which depends on subgroup prevalence and column normalization. Directly inverting `C.T` is only harmless in special cases such as uniform prevalence plus doubly stochastic error. Heterogeneous row errors break that condition.

Literature link: matrix/inverse matrix methods are estimand-specific and sensitive to the assumed misclassification model; applying a nondifferential or wrong correction can be worse than the naive estimate.

### F2. Direction-only H1 criterion is too coarse

The positive-vs-negative criterion expects the sign of error-CATE correlation to predict global-correction failure. In the current grid, global correction uses an average error rate and symmetric off-diagonal flips. With this DGP, CATE spread, subgroup count, and sample size dominate direction: high CATE heterogeneity produced lower global-worse rates than low CATE heterogeneity in the exp002 condition metrics.

### F3. Finite-sample expert-label noise is not the main failure

The estimated-global minus oracle-global GATE RMSE gap is only 0.000766 in `exp_002_gpu_dgp_grid`. The failure is therefore not primarily due to expert budget estimation noise. More labels would not fix the current H1 diagnostic or matrix algebra.

### F4. Soft/probabilistic membership is not automatically enough

Latent subgroup and classifier-calibration literatures warn that using hard labels ignores classification uncertainty, but also that soft assignment can still preserve bias if the membership probabilities are not tied to the causal estimand or sensitivity model. For EC-HTE, calibrated LLM probabilities should feed a posterior-mixing or likelihood correction, not merely replace hard subgroup labels in a causal forest.

## Source-linked solution patterns

### 1. Extended matrix / inverse matrix correction with validation data

Source: Tang, Lyles & Ye, "Extended Matrix and Inverse Matrix Methods Utilizing Internal Validation Data When Both Disease and Exposure Status Are Misclassified", Epidemiologic Methods 2013. DOI: 10.1515/em-2013-0008. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4382468/

Relevance: Directly matches EC-HTE's use of internal validation labels to correct categorical misclassification. The paper is useful because it emphasizes that matrix correction must match the data-generating misclassification structure, and that an incorrect nondifferential-error assumption can perform worse than the naive estimate.

Design choice/trick from others: use internal validation data to estimate the appropriate correction matrix; separate matrix, inverse-matrix, and likelihood corrections; check whether the assumed nondifferential matrix is valid before applying the inverse.

EC-HTE mapping: global confusion correction should be treated as a model class with explicit assumptions, not as a default debiaser. Add a diagnostic that compares row-stochastic `P(Z_hat|Z)` correction against posterior `P(Z|Z_hat)` correction under known prevalence.

### 2. Hierarchical semi-Bayes partial pooling for sparse validation strata

Source: Dement et al., "Hierarchical Semi-Bayes Methods for Misclassification in Perinatal Epidemiology", Epidemiology 2018. DOI: 10.1097/EDE.0000000000000789. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5792373/

Relevance: New source beyond memory.md. This is the closest off-the-shelf template for subgroup-specific misclassification correction when validation labels are sparse. It explicitly addresses stratum-specific predictive values that may vary by covariates but are hard to estimate independently.

Design choice/trick from others: fit a hierarchical model for bias parameters/predictive values, shrink stratum estimates toward a grand mean, then propagate posterior draws into the outcome model through probabilistic bias analysis. The two-step semi-Bayes version avoids the convergence cost of a fully joint Bayesian outcome-plus-error model.

EC-HTE mapping: partial pooling should pool confusion-matrix logits or predictive probabilities across subgroup/error strata. It should be compared against both global and independent per-subgroup matrices only after the correction target is made prevalence-aware.

### 3. Misclassified biomarker subgroup treatment effects via mixture/EM

Source: Wan, Titman & Jaki, "Subgroup Analysis of Treatment Effects for Misclassified Biomarkers with Time-to-Event Data", JRSS Series C 2019. DOI: 10.1111/rssc.12364. arXiv: https://arxiv.org/abs/1708.00942. Publisher URL: https://academic.oup.com/jrsssc/article/68/5/1447/7058601

Relevance: New source beyond memory.md. This is directly about treatment-effect subgroup analysis when the subgroup-defining biomarker is misclassified. It argues that simple adjustment is invalid for survival subgroup effects and instead models true subgroup membership as latent.

Design choice/trick from others: formulate the observed subgroup data as a mixture over true subgroup status; estimate subgroup treatment effects with an EM algorithm or corrected-score approach; use simultaneous intervals for subgroup effects.

EC-HTE mapping: implement a likelihood/EM baseline where true modifier class is latent, observed LLM class is noisy, and treatment-specific outcomes identify GATEs through posterior class weights. This is the cleanest alternative to vector inverse correction.

### 4. MC-SIMEX for categorical misclassification

Source: Küchenhoff, Mwalili & Lesaffre, "A general method for dealing with misclassification in regression: the misclassification SIMEX", Biometrics 2006. DOI: 10.1111/j.1541-0420.2005.00396.x. URL: https://pubmed.ncbi.nlm.nih.gov/16542233/

Relevance: Already represented in memory.md, but important here because exp002's failure suggests a need for a diagnostic that perturbs categorical labels through a known transition matrix and tests whether extrapolation recovers the intended bias direction.

Design choice/trick from others: add controlled extra misclassification according to a transition matrix, fit the downstream estimator repeatedly, then extrapolate back to the no-error limit.

EC-HTE mapping: use MC-SIMEX as a diagnostic baseline, not primary solution. If MC-SIMEX and posterior-matrix correction disagree under oracle transition matrices, the DGP/estimand implementation is not yet stable enough for Stage 1.

### 5. Classification uncertainty in latent subgroup effect analysis

Source: Loh & Kim, "Evaluating sensitivity to classification uncertainty in latent subgroup effect analyses", BMC Medical Research Methodology 2022. DOI: 10.1186/s12874-022-01720-8. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9508766/

Relevance: New source beyond memory.md. It targets subgroup-specific causal effects when subgroup membership is imputed or probabilistic, which closely parallels LLM-derived modifiers.

Design choice/trick from others: routinely perform sensitivity analysis over classification uncertainty, including graphical/numerical summaries, instead of treating imputed subgroup labels as fixed. The paper also warns that soft/proportional assignment can still carry classification bias.

EC-HTE mapping: add a "membership uncertainty stress test" for each correction method: perturb calibrated posterior class probabilities within validation-supported ranges and report GATE ranking stability, not only GATE RMSE.

### 6. Multiclass probability calibration for soft modifiers

Source: Kull et al., "Beyond temperature scaling: Obtaining well-calibrated multi-class probabilities with Dirichlet calibration", NeurIPS 2019. arXiv: https://arxiv.org/abs/1910.12656. Proceedings URL: https://papers.nips.cc/paper/9397-beyond-temperature-scaling-obtaining-well-calibrated-multi-class-probabilities-with-dirichlet-calibration

Relevance: New source beyond memory.md. EC-HTE needs calibrated LLM class probabilities if it will use soft modifier membership or posterior mixing.

Design choice/trick from others: use natively multiclass Dirichlet calibration rather than one-vs-rest binary calibration when the modifier has k > 2 classes; evaluate calibration with classwise ECE, log-loss, and Brier score.

EC-HTE mapping: LLM modifier calibration should output calibrated `P(Z | text, metadata)` and then feed posterior-mixing/latent-class correction. Do not evaluate it only by hard-label accuracy.

### 7. Temperature scaling and calibration diagnostics

Source: Guo et al., "On Calibration of Modern Neural Networks", ICML 2017. arXiv: https://arxiv.org/abs/1706.04599

Relevance: Gives a simple calibration baseline for probabilistic modifiers. It is less structurally matched than Dirichlet calibration but useful as a low-cost baseline.

Design choice/trick from others: learn a held-out scalar temperature for logits and evaluate expected calibration error / negative log-likelihood.

EC-HTE mapping: include temperature scaling as a weak baseline; expect it to help overconfidence but not subgroup-specific confusion asymmetry.

### 8. CATE calibration as a separate target

Source: van der Laan et al., "Causal Isotonic Calibration for Heterogeneous Treatment Effects", PMLR 2023. PMCID: PMC10416780. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC10416780/

Relevance: New source beyond memory.md. It separates calibrating treatment-effect predictions from calibrating class labels.

Design choice/trick from others: cross-fit CATE predictors and calibrate predicted HTE values nonparametrically, avoiding a simple holdout-only calibration loss.

EC-HTE mapping: after modifier-error correction, calibrate the resulting CATE/GATE predictor separately. This should not replace membership-error correction, but it can catch over/understated effect magnitudes after correction.

## Candidate next hypotheses

### H-next-001: posterior-matrix correction

Mechanistic falsifiable hypothesis: In the exp002 DGP, replacing the current direct inverse of `P(Z_hat | Z)^T` with a prevalence-aware posterior mixing correction based on `P(Z | Z_hat)` will make oracle subgroup-specific correction improve GATE RMSE over uncorrected in high-error/high-CATE conditions, while the current direct inverse will not.

Responds to failure mode: F1 matrix orientation / estimand mismatch.

Test: rerun a small subset of exp002 cells with three oracle methods: current `C.T` inverse, posterior-mixing inverse, and likelihood/EM latent-class correction. Success requires posterior or EM correction to beat uncorrected and current inverse on GATE RMSE with bootstrap CI upper bound for method-minus-current < 0.

### H-next-002: likelihood/EM latent modifier model

Mechanistic falsifiable hypothesis: When subgroup membership is misclassified and treatment effects differ by true subgroup, a latent-class outcome model using the observed LLM label as a noisy proxy will recover subgroup GATEs with lower RMSE than hard-label uncorrected and global confusion correction because it estimates treatment interactions over posterior true-class weights.

Responds to failure modes: F1 and F4.

Test: implement binary/k-class EM baseline on synthetic cells with known transition matrix and uniform/nonuniform prevalences. Success requires EM GATE RMSE < global correction GATE RMSE in positive and negative correlation settings, not only in one hand-picked cell.

### H-next-003: directional bias-bound diagnostic

Mechanistic falsifiable hypothesis: A signed diagnostic that estimates the covariance between subgroup-specific correction residuals and subgroup CATE direction will predict oracle-global-worse conditions better than the current magnitude-only `mean(abs(centered_rate * centered_abs_cate))` score, because global correction error depends on the direction of contamination in the GATE vector.

Responds to failure mode: F2.

Test: compute candidate signed diagnostics from existing `condition_metrics.jsonl`, then confirm on a repaired DGP grid. Success requires Spearman rho >= 0.50 with bootstrap CI lower > 0 for the repaired diagnostic; otherwise H1 should be reframed around estimator-specific algebra rather than error-CATE correlation alone.

### H-next-004: hierarchical confusion-matrix pooling

Mechanistic falsifiable hypothesis: Under sparse expert validation labels, hierarchical partial pooling over subgroup confusion-matrix logits will reduce GATE RMSE relative to independent per-subgroup confusion matrices by lowering variance, while still improving over global correction when true subgroup errors are heterogeneous.

Responds to failure modes: F3 and the blocked H2 path.

Test: after H-next-001 passes, run low-budget cells B in {100, 500} with global, independent subgroup, and hierarchical subgroup correction. Success follows ROADMAP H2: partial-pooling-minus-global bootstrap 95% CI upper bound < 0 and within 5% relative GATE RMSE of independent correction.

### H-next-005: calibrated soft modifier correction

Mechanistic falsifiable hypothesis: Dirichlet-calibrated multiclass LLM modifier probabilities used inside a posterior-mixing correction will reduce subgroup GATE bias more than hard-label confusion correction when confusion is asymmetric across classes, because calibrated probabilities preserve uncertainty about near-boundary records that hard labels discard.

Responds to failure mode: F4.

Test: simulate LLM score vectors with controllable miscalibration; compare hard-label confusion, temperature scaling, Dirichlet calibration, and oracle probabilities. Success requires lower GATE RMSE and lower classwise calibration error for Dirichlet/posterior correction than hard-label correction.

### H-next-006: MC-SIMEX as a robustness screen

Mechanistic falsifiable hypothesis: If the corrected H1 mechanism is real, MC-SIMEX extrapolation using the oracle categorical transition matrix will move GATE estimates toward the true GATE vector as added misclassification increases and extrapolates back, whereas the current exp002 inverse correction may move estimates in the wrong direction under heterogeneous row errors.

Responds to failure modes: F1 and F2.

Test: run MC-SIMEX on a fixed subset of exp002 cells. Success requires extrapolated GATE RMSE < uncorrected GATE RMSE in the same cells where posterior-matrix correction succeeds.

## Concrete implementation recommendations

1. Add a prevalence-aware correction function:
   - Estimate `C[g,h] = P(Z_hat=h | Z=g)` from validation data.
   - Estimate subgroup prevalence `pi_g`.
   - Compute observed-label prevalence `q_h = sum_g pi_g C[g,h]`.
   - Compute posterior mixing `M[h,g] = pi_g C[g,h] / q_h`.
   - Solve `observed_gate = M true_gate` rather than `observed_gate = C.T true_gate`.

2. Keep the current direct inverse only as a negative-control baseline named `transition_transpose_inverse`, not as "oracle subgroup correction."

3. Add nonuniform subgroup prevalence cells. A correction method that only works under uniform prevalence is not acceptable for real LLM annotation settings.

4. Add asymmetric off-diagonal confusion. Uniformly spreading errors to all other classes makes class destination irrelevant; real categorical LLM errors are usually structured.

5. Split diagnostics:
   - matrix recovery error,
   - observed-label posterior calibration,
   - GATE RMSE,
   - subgroup bias direction,
   - ranking stability under membership uncertainty.

6. Make calibrated probabilities a correction input, not an endpoint. Report ECE/log-loss/Brier plus downstream GATE RMSE.

## Director-facing recommendation

Decision: pause formal H2 launch. Approve a narrow mechanism-audit patch around H-next-001 through H-next-003. If posterior/EM correction repairs the grid-level relationship, then resume H2 partial-pooling using the repaired correction target. If it does not, revise H1 from "positive error-CATE correlation makes global correction worse" to a sharper estimator-specific claim: global correction fails when the posterior observed-label mixing matrix differs materially from the pooled correction matrix in directions aligned with subgroup treatment-effect contrasts.

No findings.md update was made. No experiment was launched.
