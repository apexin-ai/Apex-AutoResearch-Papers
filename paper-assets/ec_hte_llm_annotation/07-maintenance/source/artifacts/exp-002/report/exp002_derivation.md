# Formal Bias Bound Derivation (exp-002)

## Assumptions

- **(A1)** Known confusion matrix (not estimated from data)
- **(A2)** Symmetric misclassification per subgroup: P(Ẑ=1|Z=0,S=s) = P(Ẑ=0|Z=1,S=s) = π_s
- **(A3)** Balanced effect modifier: P(Z=0) = P(Z=1) = 0.5
- **(A4)** Known subgroup weights w_s with Σ_s w_s = 1

## Step 1: Subgroup Confusion Matrix

Under A2, the confusion matrix for subgroup s (rows = true Z, cols = Ẑ):

```
C_s = [[1 - π_s,  π_s    ],
       [π_s,      1 - π_s ]]
```

where C_s[z, ẑ] = P(Ẑ = ẑ | Z = z, S = s).

## Step 2: Mixing Matrix

The mixing matrix M_s[ẑ, z] = P(Z = z | Ẑ = ẑ, S = s).

By Bayes' rule:

```
P(Z=z | Ẑ=ẑ, S=s) = P(Ẑ=ẑ | Z=z, S=s) · P(Z=z) / P(Ẑ=ẑ | S=s)
```

Under A3, P(Z=z) = 0.5 for z ∈ {0,1}. The marginal:

```
P(Ẑ=ẑ | S=s) = Σ_z P(Ẑ=ẑ | Z=z, S=s) · P(Z=z)
             = 0.5 · [C_s[0,ẑ] + C_s[1,ẑ]]
```

For ẑ=0: P(Ẑ=0|S=s) = 0.5·[(1-π_s) + π_s] = 0.5
For ẑ=1: P(Ẑ=1|S=s) = 0.5·[π_s + (1-π_s)] = 0.5

Therefore:

```
M_s[ẑ, z] = C_s[z, ẑ] · 0.5 / 0.5 = C_s[z, ẑ]
```

Since C_s is symmetric under A2:

```
M_s = [[1 - π_s,  π_s    ],
       [π_s,      1 - π_s ]]
```

## Step 3: Global Confusion/Mixing Matrix

The global confusion matrix is the weight-averaged subgroup matrix:

```
C_global = Σ_s w_s · C_s
```

Under A2, each C_s has the same symmetric structure, so:

```
C_global = [[1 - π̄,  π̄    ],
            [π̄,      1 - π̄ ]]
```

where **π̄ = Σ_s w_s · π_s** is the weighted average misclassification rate.

By the same Bayes' rule argument: M_global = C_global (under A2+A3).

## Step 4: Observed CATE Under Misclassification

The observed CATE in subgroup s, conditioning on Ẑ:

```
τ_obs(Ẑ=ẑ, S=s) = E[Y(1) - Y(0) | Ẑ=ẑ, S=s]
                 = Σ_z P(Z=z | Ẑ=ẑ, S=s) · τ(Z=z)
                 = Σ_z M_s[ẑ, z] · τ(z)
```

In vector form: **τ_obs(·, s) = M_s · τ_true**

where τ_true = [τ(Z=0), τ(Z=1)]ᵀ.

## Step 5: Global Correction Applied to Subgroup

Global correction inverts M_global and applies it to the observed CATEs:

```
τ̂_global(·, s) = M_global⁻¹ · τ_obs(·, s)
               = M_global⁻¹ · M_s · τ_true
```

The **bias** of global correction in subgroup s:

```
bias_global(·, s) = τ̂_global(·, s) - τ_true
                  = (M_global⁻¹ · M_s - I) · τ_true
```

## Step 6: Computing M_global⁻¹ · M_s - I

The inverse of M_global:

```
det(M_global) = (1-π̄)² - π̄² = 1 - 2π̄

M_global⁻¹ = (1/(1-2π̄)) · [[1-π̄, -π̄], [-π̄, 1-π̄]]
```

Computing the product M_global⁻¹ · M_s:

```
M_global⁻¹ · M_s = (1/(1-2π̄)) · [[1-π̄-π_s,  π_s-π̄  ],
                                     [π_s-π̄,    1-π̄-π_s]]
```

Subtracting the identity:

```
M_global⁻¹ · M_s - I = (1/(1-2π̄)) · [[-δ_s,  δ_s ],
                                         [δ_s,  -δ_s]]
```

where **δ_s = π_s - π̄** is the subgroup's deviation from the mean misclassification rate.

## Step 7: Exact Bias Identity

```
bias_global(·, s) = (δ_s / (1-2π̄)) · [[-1, 1], [1, -1]] · [τ(0), τ(1)]ᵀ
                  = (δ_s / (1-2π̄)) · [Δτ, -Δτ]
```

where **Δτ = τ(Z=1) - τ(Z=0)**.

### Result (Exact Identity under A1–A4):

```
bias_global(z=0, s) = +δ_s · Δτ / (1 - 2π̄)
bias_global(z=1, s) = -δ_s · Δτ / (1 - 2π̄)
```

**Interpretation**: The bias is the product of three factors:
1. **δ_s**: how much subgroup s deviates from the average misclassification rate
2. **Δτ**: treatment effect heterogeneity across Z
3. **1/(1-2π̄)**: amplification from the correction inversion

## Naive Bias (No Correction)

The naive estimator uses Ẑ as if it were Z:

```
bias_naive(·, s) = (M_s - I) · τ_true
                 = [[-π_s, π_s], [π_s, -π_s]] · [τ(0), τ(1)]ᵀ
```

```
bias_naive(z=0, s) = +π_s · Δτ
bias_naive(z=1, s) = -π_s · Δτ
```

## "Debiasing Can Hurt" Condition

Global correction increases bias (|bias_global| > |bias_naive|) iff:

```
|δ_s| / (1 - 2π̄) > π_s
```

**For high-misclassification subgroups** (π_s > π̄, δ_s > 0):

```
(π_s - π̄) / ((1-2π̄) · π_s) > 1
⟹ π_s - π̄ > π_s - 2π̄·π_s
⟹ π̄(2π_s - 1) > 0
⟹ π_s > 0.5
```

Since π_s < 0.5 always, **debiasing never hurts the high-misclassification subgroup**.

**For low-misclassification subgroups** (π_s < π̄, δ_s < 0):

```
(π̄ - π_s) / ((1-2π̄) · π_s) > 1
⟹ π_s < π̄ / (2(1 - π̄))
```

This is a non-trivial condition satisfied when π_s is sufficiently small relative to π̄.

**Intuition**: Global correction applies a uniform inverse that is calibrated for the average misclassification rate. It under-corrects high-misclass subgroups (reducing but not eliminating bias) and over-corrects low-misclass subgroups (reversing the bias sign and potentially increasing magnitude).

## (a) vs (b): Known vs Estimated Matrices

**(a) Known matrix** (A1 holds): The bias identity above is exact. No approximation.

**(b) Estimated matrix**: When M_global is estimated from n_expert expert labels:
- M̂_global = M_global + O(1/√n_expert) random perturbation
- M̂_global⁻¹ = M_global⁻¹ + O(1/√n_expert) correction
- Expected bias acquires an additional O(1/√n_expert) term
- The exact identity remains the dominant bias for moderate-to-large δ_s and Δτ

## K ≥ 2 Extension

The derivation above holds for **arbitrary K subgroups** with arbitrary weights. The formula:

```
bias_global(z=0, s) = +δ_s · Δτ / (1 - 2π̄)
bias_global(z=1, s) = -δ_s · Δτ / (1 - 2π̄)
```

is an exact identity under A1–A4, where:
- δ_s = π_s - π̄
- π̄ = Σ_s w_s · π_s (weighted by subgroup sizes)
- Σ_s w_s · δ_s = 0 (deviations sum to zero)

**Scope**: Binary effect modifier Z ∈ {0,1} with arbitrary K subgroups. The formula does not extend to multi-valued Z without analogous matrix algebra.
