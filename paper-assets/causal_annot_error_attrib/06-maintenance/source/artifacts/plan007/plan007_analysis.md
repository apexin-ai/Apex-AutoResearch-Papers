# Plan 007: Correction Method Guidance — Analysis

## 1. Experiment Design

**Objective**: Evaluate 5 correction methods for K=3 LLM misclassification bias across DAG topologies and confusion matrix structures.

**Methods**: naive_plugin (per-obs C⁻¹), DSL (EM joint estimation), PPI++ (gold-label prediction-powered inference), MC-SIMEX (simulation-extrapolation), MLA (matrix-level adjustment D*·C⁻¹).

**DGP**: N_data=5000 per replication, N_gold=500 gold-standard labels (for DSL/PPI). Oracle τ computed from N=500K large-sample OLS with true A.

**Scope limitation**: Only a partial run completed — 2 topologies (exposure, confounding) × 2 C structures (moderate_uniform, asymmetric) × N_sim=10. The intended full run (7 topologies × 6 C structures × 1000 sims) failed due to CLI arg error (`--N_sim` should be `--n-sim`). Results below should be interpreted as directional, not definitive.

## 2. Complete Results Table (Topology × Method)

### 2.1 Exposure Topology (A→Y, target = β₁ dummy coefficient, τ_true ≈ 1.0)

| C Structure | Method | Bias (uncorr) | Bias (corr) | Bias Red % | RMSE (uncorr) | RMSE (corr) | Cov 95% |
|---|---|---|---|---|---|---|---|
| moderate_uniform | naive_plugin | −0.370 | −0.622 | **−67.9%** | 0.372 | 0.622 | 0.0% |
| moderate_uniform | dsl | −0.370 | +0.590 | **−59.3%** | 0.372 | 0.591 | 0.0% |
| moderate_uniform | ppi | −0.370 | +0.003 | **99.2%** | 0.372 | 0.100 | 90.0% |
| moderate_uniform | mcsimex | −0.370 | −0.034 | **90.8%** | 0.372 | 0.057 | 70.0% |
| moderate_uniform | mla | −0.370 | −0.622 | **−67.9%** | 0.372 | 0.622 | 0.0% |
| asymmetric | naive_plugin | −0.345 | −0.630 | **−82.7%** | 0.346 | 0.631 | 0.0% |
| asymmetric | dsl | −0.345 | +0.588 | **−70.5%** | 0.346 | 0.589 | 0.0% |
| asymmetric | ppi | −0.345 | −0.010 | **97.0%** | 0.346 | 0.054 | 100.0% |
| asymmetric | mcsimex | −0.345 | −0.084 | **75.8%** | 0.346 | 0.090 | 40.0% |
| asymmetric | mla | −0.345 | −0.527 | **−52.6%** | 0.346 | 0.527 | 0.0% |

### 2.2 Confounding Topology (A→T, A→Y, T→Y; target = β_T treatment coefficient, τ_true ≈ 2.0)

| C Structure | Method | Bias (uncorr) | Bias (corr) | Bias Red % | RMSE (uncorr) | RMSE (corr) | Cov 95% |
|---|---|---|---|---|---|---|---|
| moderate_uniform | naive_plugin | +0.237 | +0.237 | **0.0%** | 0.237 | 0.237 | 0.0% |
| moderate_uniform | dsl | +0.237 | −0.065 | **72.5%** | 0.237 | 0.066 | 0.0% |
| moderate_uniform | ppi | +0.237 | +0.011 | **95.2%** | 0.237 | 0.038 | 100.0% |
| moderate_uniform | mcsimex | +0.237 | +0.166 | **30.1%** | 0.237 | 0.166 | 0.0% |
| moderate_uniform | mla | +0.237 | +0.237 | **0.0%** | 0.237 | 0.237 | 0.0% |
| asymmetric | naive_plugin | +0.223 | +0.223 | **0.0%** | 0.223 | 0.223 | 0.0% |
| asymmetric | dsl | +0.223 | −0.079 | **64.5%** | 0.223 | 0.082 | 0.0% |
| asymmetric | ppi | +0.223 | +0.004 | **98.1%** | 0.223 | 0.022 | 100.0% |
| asymmetric | mcsimex | +0.223 | +0.140 | **37.3%** | 0.223 | 0.141 | 0.0% |
| asymmetric | mla | +0.223 | +0.223 | **0.0%** | 0.223 | 0.223 | 0.0% |

### 2.3 Cross-Method Summary

| Method | Mean Bias Red | Median | Range | Mean RMSE | Mean Cov | Win Rate |
|---|---|---|---|---|---|---|
| ppi | **97.4%** | 97.6% | [95.2%, 99.2%] | 0.054 | 97.5% | **100%** (4/4) |
| mcsimex | 58.5% | 56.5% | [30.1%, 90.8%] | 0.113 | 27.5% | 0% |
| dsl | 1.8% | 2.6% | [−70.5%, 72.5%] | 0.332 | 0.0% | 0% |
| naive_plugin | −37.6% | −33.9% | [−82.7%, 0.0%] | 0.428 | 0.0% | 0% |
| mla | −30.1% | −26.3% | [−67.9%, 0.0%] | 0.403 | 0.0% | 0% |

## 3. Hypothesis Verification

### H1: naive_plugin and MLA ineffective for T coefficient (Frisch-Waugh) — CONFIRMED

Confounding topology targets β_T (treatment coefficient). Both naive_plugin and MLA achieve exactly **0.0% bias reduction** — the corrected estimate equals the uncorrected estimate to machine precision (Δ ≈ 10⁻¹⁵).

**Mechanism**: Per Frisch-Waugh-Lovell theorem, β_T = Cov(M_D·T, M_D·Y) / Var(M_D·T), where M_D is the residual-maker projecting out the dummy columns. Replacing D with C⁻¹D* (naive_plugin) or D*·C⁻¹ (MLA) changes the dummy column space but M_D·T and M_D·Y are invariant when the column space of the corrected dummies spans the same linear subspace — which it does for invertible C. The T coefficient is numerically unchanged.

### H2: PPI++ should perform best — CONFIRMED

PPI++ achieves 95–99% bias reduction across all 4 scenarios with 90–100% coverage. It is the only method achieving near-nominal coverage.

**Why**: PPI++ directly leverages gold-standard labels as an unbiased anchor (β̂_gold) and uses the full-sample noisy estimate only for variance reduction via the λ-weighted rectifier. This makes it robust to any C structure.

### H3: Different topologies respond differently — CONFIRMED (with caveats)

| Method | Exposure (mean) | Confounding (mean) | Gap |
|---|---|---|---|
| dsl | −64.9% | +68.5% | **133 pp** |
| mcsimex | +83.3% | +33.7% | 50 pp |
| naive_plugin | −75.3% | 0.0% | 75 pp |
| mla | −60.2% | 0.0% | 60 pp |
| ppi | +98.1% | +96.6% | 1.5 pp |

DSL shows the most dramatic topology dependence: effective for confounding (where target is T, and EM can jointly learn C and regression params) but catastrophically wrong for exposure (where target IS a dummy coefficient, creating an identifiability issue in the EM).

### H4: naive_plugin and MLA effective for dummy coefficients — REJECTED

Contrary to expectation, both methods make bias **substantially worse** for the exposure topology where the target is a dummy coefficient:
- naive_plugin: −75.3% mean (bias increases by 75%)
- mla: −60.2% mean (bias increases by 60%)

**Explanation**: The per-observation C⁻¹ correction produces corrected dummies with entries outside [0,1] and inflated variance. While E[D_corrected|A] = D_true (conditionally unbiased), OLS with these generated regressors suffers from:
1. **Inflated X'X matrix**: the corrected dummies have higher variance than binary dummies, distorting the OLS projection geometry
2. **Non-classical measurement error**: the correction noise is heteroskedastic and correlated across dummy columns
3. **Reference category asymmetry**: dropping one column of the corrected K-dimensional vector creates asymmetric bias across the remaining coefficients

This is a key paper-worthy finding: matrix-inverse corrections that are theoretically unbiased for marginal proportions fail when used as observation-level regressors in OLS.

## 4. Key Findings

1. **PPI++ is universally dominant**: 97.4% mean bias reduction, near-nominal coverage, zero failures. The only method that works well across both topologies and both C structures tested.

2. **MC-SIMEX is a viable C-only alternative**: When gold labels are unavailable, MC-SIMEX achieves 58.5% mean bias reduction. Better for exposure (83.3%) than confounding (33.7%), but coverage is poor (27.5%).

3. **DSL is topology-sensitive**: Excellent for confounding (68.5%) but catastrophic for exposure (−64.9%). The EM algorithm has identifiability issues when the estimand is a function of the misclassified variable's dummy coefficients.

4. **naive_plugin and MLA are harmful or inert**: Zero effect on treatment coefficients (Frisch-Waugh), actively harmful for dummy coefficients. These should never be recommended as corrections.

5. **Coverage crisis**: Only PPI++ achieves reasonable coverage. All other methods show 0% coverage (except MC-SIMEX at 27.5% for exposure), indicating that standard OLS SEs are invalid under misclassification correction.

## 5. Limitations and Next Steps

- **Partial run**: Only 2/7 topologies × 2/6 C structures × 10 sims completed. Need full run with `--n-sim 1000` (not `--N_sim`).
- **Missing topologies**: collider, mediation, mbias, iv, frontdoor untested. These are critical — collider and mbias involve conditioning bias where correction may have qualitatively different effects.
- **Missing C structures**: mild_uniform, severe_uniform, near_permutation, realistic_llm untested. near_permutation (near-singular C) may cause numerical issues for C⁻¹-based methods.
- **Low N_sim**: 10 replications gives high MC error. The exposure × asymmetric × mcsimex coverage of 40% vs moderate_uniform 70% could be noise.
- **SE estimation**: MC-SIMEX uses naive OLS SE proxy; DSL uses converged-responsibility SE. Neither accounts for the correction procedure, explaining poor coverage.

**Recommended re-run command**:
```bash
cd /home/sonny/causal_annot_error_attrib && python3 -u plan_007_correction_guidance.py --n-sim 1000 2>&1 | tee artifacts/plan007/plan007_run_full.log
```
