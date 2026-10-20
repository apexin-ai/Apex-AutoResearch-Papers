# PPI/DSL vs EC-HTE Baselines: Mathematical Equivalence Analysis

## Setup

- **Z** ∈ {0,1}: true binary effect modifier (e.g., sentiment)
- **Ẑ**: LLM-annotated proxy for Z, with subgroup-specific misclassification
- **S** ∈ {S₀,...,S_{K-1}}: subgroup membership
- **CATE target**: τ(z, s) = E[Y(1) - Y(0) | Z=z, S=s]
- **Gold data**: n observations where both Z and Ẑ are observed
- **All data**: N observations where only Ẑ is observed (N >> n)

Misclassification model (symmetric for simplicity, but results generalize):
  P(Ẑ ≠ Z | S=s) = π_s

---

## 1. DSL (Egami et al., 2024) ≡ Confusion Matrix Correction

### DSL Framework

DSL's core procedure for correcting a downstream estimand θ:

1. Estimate the *surrogate model*: P(Z | Ẑ, X) from gold data
2. Use this model to correct the downstream estimate

For binary Z without additional covariates X in the surrogate model:

**P(Z=z | Ẑ=z')** is exactly the mixing matrix M[z', z].

The confusion matrix C[z, z'] = P(Ẑ=z' | Z=z) is estimated from gold data, then inverted via Bayes' rule:

  M[z', z] = C[z, z'] · P(Z=z) / P(Ẑ=z')

The corrected CATE estimate:

  [τ̂(Z=0), τ̂(Z=1)]ᵀ = M⁻¹ · [τ̂_obs(Ẑ=0), τ̂_obs(Ẑ=1)]ᵀ

### Equivalence

| DSL variant | EC-HTE baseline | Relationship |
|-------------|-----------------|--------------|
| DSL-global (pool all gold data → single C) | Global Correction | **Identical point estimates**. DSL additionally provides asymptotic SEs accounting for the two-stage estimation, but the debiased CATE estimates are mathematically the same. |
| DSL-subgroup (per-subgroup C_s) | Stratified MLE | **Identical point estimates**. Same per-subgroup confusion matrix, same M_s⁻¹ inversion. |

**Why DSL doesn't solve our problem**: DSL provides a generic framework for surrogate correction. When applied per-subgroup, it becomes Stratified MLE — which has high variance at small n_expert because each subgroup's CM is estimated independently (no cross-subgroup information sharing). DSL's contribution is the inference framework, not a better estimator for the heterogeneous case.

---

## 2. PPI (Angelopoulos et al., 2023) — Estimand-Level Correction

### PPI Estimator for CATE

PPI uses a "rectifier" to debias the ML-based estimate:

  θ̂_PPI = θ̂_f(N) + [θ̂_gold(n) - θ̂_f(n)]

where θ̂_f uses the ML prediction (Ẑ) and θ̂_gold uses the true label (Z).

Applied to CATE estimation for Z-level z within subgroup s:

  τ̂_PPI(z, s) = τ̂_all(Ẑ=z, s) + [τ̂_gold(Z=z, s) - τ̂_hat_gold(Ẑ=z, s)]

where:
- τ̂_all(Ẑ=z, s) = diff-in-means on ALL data using Ẑ grouping within subgroup s
- τ̂_gold(Z=z, s) = diff-in-means on GOLD data using true Z within subgroup s
- τ̂_hat_gold(Ẑ=z, s) = diff-in-means on GOLD data using Ẑ within subgroup s

### PPI-global vs PPI-subgroup

**PPI-global**: Compute a single rectifier from ALL gold data (pooled across subgroups):
  rect(z) = τ̂_gold(Z=z) - τ̂_hat_gold(Ẑ=z)    [no subgroup stratification]
  τ̂_PPI-global(z, s) = τ̂_all(Ẑ=z, s) + rect(z)

This applies the SAME correction to every subgroup → cannot fix subgroup-heterogeneous bias.

**PPI-subgroup**: Compute per-subgroup rectifiers independently:
  rect_s(z) = τ̂_gold(Z=z, s) - τ̂_hat_gold(Ẑ=z, s)
  τ̂_PPI-sub(z, s) = τ̂_all(Ẑ=z, s) + rect_s(z)

### PPI-subgroup vs Stratified MLE: Different Estimators

PPI-subgroup and Stratified MLE are **not** mathematically equivalent. They differ in how they correct for misclassification:

| Aspect | Stratified MLE | PPI-subgroup |
|--------|---------------|--------------|
| **Correction mechanism** | Model-based: estimate C_s → M_s → M_s⁻¹ × τ̂_obs | Model-free: additive rectifier from gold data |
| **What it inverts** | The mixing process (how true Z groups get mixed into Ẑ groups) | The estimand bias (difference between gold and noisy estimates) |
| **Parameters estimated from gold** | C_s: 2 free parameters per subgroup | rect_s(z): 2 CATE differences per subgroup |
| **Uses confusion matrix** | Yes | No |
| **Handles non-linear mixing** | Yes (full matrix inversion) | Approximately (linear bias correction) |

**However**, both share the same fundamental limitation: **no cross-subgroup information sharing**. When n_expert per subgroup is small, both estimators have high variance because they operate on independent per-subgroup gold samples.

### Expected empirical behavior

- PPI-subgroup ≈ Stratified MLE in terms of RMSE/bias (similar variance, similar bias correction)
- Both > PPI-global when misclassification is heterogeneous (PPI-global under-corrects high-error subgroups, over-corrects low-error subgroups)
- Both < EC-HTE because EC-HTE's hierarchical Bayesian partial pooling borrows strength across subgroups

---

## 3. Why EC-HTE Wins

EC-HTE's advantage over all PPI/DSL variants stems from **partial pooling** in confusion matrix estimation:

```
                    No pooling              Partial pooling           Full pooling
                    (Stratified MLE,        (EC-HTE)                  (Global Correction,
                     PPI-subgroup,                                     PPI-global,
                     DSL-subgroup)                                     DSL-global)
                    ─────────────────────────────────────────────────────────────────
Bias                Low (per-subgroup)      Low (shrunk toward        High (ignores
                                            common structure)         heterogeneity)
Variance            High (small per-        Moderate (borrows         Low (uses all
                    subgroup n)             strength)                 gold data)
MSE                 Dominated by            Best trade-off            Dominated by
                    variance                                          bias
```

The Dirichlet-Multinomial hierarchical model places a shared concentration prior α₀ across subgroups. When data is sparse, subgroup CMs shrink toward the global average; when data is abundant, they converge to subgroup-specific estimates. This adaptive behavior is exactly what neither PPI nor DSL provides.

---

## 4. Summary for Paper

**Positioning claim**: PPI and DSL, when naively extended to CATE estimation with mismeasured effect modifiers, reduce to baselines that EC-HTE already dominates.

| Method | Equivalent to | Handles subgroup heterogeneity? | Cross-subgroup pooling? |
|--------|--------------|--------------------------------|------------------------|
| PPI-global | ≈ Global Correction | No | N/A (global) |
| PPI-subgroup | ≈ Stratified MLE | Yes (independently) | No |
| DSL-global | ≡ Global Correction | No | N/A (global) |
| DSL-subgroup | ≡ Stratified MLE | Yes (independently) | No |
| **EC-HTE** | Novel | **Yes (jointly)** | **Yes (HB)** |

This table, combined with the empirical results showing EC-HTE > Stratified MLE > Global Correction, establishes that EC-HTE fills a gap that neither PPI nor DSL addresses.
