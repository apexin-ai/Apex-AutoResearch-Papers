# Power Artifact Simulation Analysis

## Purpose

Reviewer W-C3 raised the concern that observed sharp onset α_c(T) ∝ T^{−2.08}
could be a statistical power artifact: if real signal grows smoothly with α,
increasing T simply raises PermG power, making the apparent onset shift left.

This simulation tests H0 (linear signal), H0' (concave signal), and H1 (step
transition) against observations.

## Setup

- Simulations per (α,T) cell: **1000**
- Permutations per test: **1000**
- Pairs per simulation: 8, FDR q=0.05
- VAR(1): a=0.5, c=0.5, σ=1.0
- Elapsed: 473.0s

## Calibration

Target: mean detection fraction = 0.75 at α=0.75, T=20 (matching observed 6/8).

- **c_scale** = 1.3622 → H0 signal: S(α) = 1.3622 × α
- **c_concave** = 1.1797 → H0' signal: S(α) = 1.1797 × α^{0.5}
- **S_max** = 1.0217 → H1 step amplitude

## H0: Linear Signal (No Phase Transition)

Under H0, signal S(α) = c × α increases monotonically. There is **no true
transition point** — detection onset is purely a statistical power artifact.

### H0 Detection Rates P(PermG ≥ 1)

| α \ T | 5 | 10 | 15 | 20 | 25 |
|------|------|------|------|------|------|
| 0.00 | 0.01 | 0.05 | 0.06 | 0.06 | 0.05 |
| 0.10 | 0.01 | 0.05 | 0.07 | 0.10 | 0.12 |
| 0.25 | 0.01 | 0.12 | 0.23 | 0.31 | 0.41 |
| 0.45 | 0.02 | 0.27 | 0.60 | 0.81 | 0.93 |
| 0.50 | 0.01 | 0.36 | 0.72 | 0.89 | 0.98 |
| 0.60 | 0.01 | 0.47 | 0.87 | 0.97 | 1.00 |
| 0.75 | 0.02 | 0.70 | 0.97 | 1.00 | 1.00 |
| 1.00 | 0.02 | 0.90 | 1.00 | 1.00 | 1.00 |

## H0': Concave Signal (Sub-linear, No Phase Transition)

Under H0', signal S(α) = c × α^{0.5} grows sub-linearly. This tests whether
a concave (but still smooth) signal function can produce steeper apparent onset
scaling than the linear H0.

### H0' Detection Rates P(PermG ≥ 1)

| α \ T | 5 | 10 | 15 | 20 | 25 |
|------|------|------|------|------|------|
| 0.00 | 0.01 | 0.04 | 0.07 | 0.06 | 0.07 |
| 0.10 | 0.01 | 0.12 | 0.23 | 0.39 | 0.53 |
| 0.25 | 0.02 | 0.24 | 0.56 | 0.80 | 0.90 |
| 0.45 | 0.01 | 0.45 | 0.85 | 0.97 | 1.00 |
| 0.50 | 0.01 | 0.48 | 0.88 | 0.98 | 1.00 |
| 0.60 | 0.02 | 0.55 | 0.93 | 1.00 | 1.00 |
| 0.75 | 0.03 | 0.70 | 0.97 | 1.00 | 1.00 |
| 1.00 | 0.02 | 0.82 | 1.00 | 1.00 | 1.00 |

## H1: Step Transition (Phase Transition Model)

Under H1, signal is a step function: S(α,T) = S_max × I(α ≥ α_c(T)),
where α_c(T) = 130.39 × T^{−2.083}.

### H1 Detection Rates P(PermG ≥ 1)

| α \ T | 5 | 10 | 15 | 20 | 25 |
|------|------|------|------|------|------|
| 0.00 | 0.01 | 0.05 | 0.06 | 0.05 | 0.05 |
| 0.10 | 0.01 | 0.05 | 0.04 | 0.07 | 0.06 |
| 0.25 | 0.01 | 0.05 | 0.05 | 0.05 | 1.00 |
| 0.45 | 0.01 | 0.06 | 0.06 | 1.00 | 1.00 |
| 0.50 | 0.01 | 0.05 | 0.98 | 1.00 | 1.00 |
| 0.60 | 0.01 | 0.05 | 0.97 | 1.00 | 1.00 |
| 0.75 | 0.02 | 0.05 | 0.97 | 1.00 | 1.00 |
| 1.00 | 0.01 | 0.05 | 0.97 | 1.00 | 1.00 |

## Apparent Onset Comparison

Smallest α where P(PermG ≥ 1) > 0.50:

| T | H0 | H0' | H1 | Theory α_c |
|---|------|------|------|------------|
| 5 | — | — | — | 4.5634 |
| 10 | 0.6199 | 0.525 | — | 1.0771 |
| 15 | 0.3945 | 0.2238 | 0.474 | 0.4629 |
| 20 | 0.3257 | 0.1408 | 0.3444 | 0.2542 |
| 25 | 0.2851 | 0.0935 | 0.1701 | 0.1597 |

## Scaling Fits

- **H0** (linear): α_c(T) ∝ T^{−0.848} (c=4.189, R²=0.977)
- **H0'** (concave): α_c(T) ∝ T^{−1.869} (c=37.580, R²=0.997)
- **H1** (step): α_c(T) ∝ T^{−1.964} (c=104.224, R²=0.920)
- **Observed**: α_c(T) ∝ T^{−2.083} (c=130.390)

## Conclusion

**ARTIFACT_POSSIBLE**

H0 (linear): γ=0.85 (Δγ=1.24). H0' (concave): γ=1.87 (Δγ=0.21). H0' produces onset scaling within 0.5 of observed γ=2.08. A smooth signal model can reproduce the observed onset pattern.

### Interpretation

H0 (linear, k=1) gives γ ≈ 0.8476, far from observed. However, H0' (concave,
k=0.5) gives γ ≈ 1.8688, close to observed γ ≈ 2.08. This means a
sub-linear but smooth signal function CAN produce onset scaling similar to what
we observe. The power artifact explanation cannot be fully excluded under the
concave signal assumption.
