#!/usr/bin/env python3
"""
Non-Differential Misclassification Stress Test — Exposure DAG (K=3)

Tests robustness of the paper's non-differential assumption by introducing
controlled violations: the confusion matrix differs slightly between
outcome-defined subgroups (Y > median vs Y <= median).

Model:
  DAG: A -> Y, A -> A*
  DGP: Y = β₀ + β₁·1[A=1] + β₂·1[A=2] + ε,  ε ~ N(0,1)
  Non-differential: P(A*|A) = C₀  (same for all units)
  Differential:     P(A*|A, Y>med) = C_high,  P(A*|A, Y≤med) = C_low
    where C_high = renormalize(C₀ + ε·Δ), C_low = C₀
    Δ[j,i] = off-diagonal noise, re-normalized to column-stochastic

For each ε ∈ {0, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50}:
  - Sample 10,000 base C₀ from truncated Dirichlet(1,1,1) with diag ≥ 0.7
  - ε=0: compute bias via analytical plim (matches subspace analysis ~13.7%)
  - ε>0: compute bias via MC (N=50,000 per trial) with differential C
  - Report: sign-flip rate, amplification rate, violation rate

Dependencies: numpy
"""

import numpy as np
import json
import time
import sys

# ─── DGP Parameters ─────────────────────────────────────────
P_A = np.array([0.40, 0.35, 0.25])
BETA = np.array([0.0, 1.0, -0.5])  # β₀, β₁, β₂
K = 3
DIAG_THRESH = 0.7

N_MATRICES = 10_000       # confusion matrices per ε level
N_MC = 50_000             # MC sample size per trial (for ε > 0)
EPSILONS = [0.0, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50]
SEED = 42


# ─── Sampling ────────────────────────────────────────────────
def sample_truncated_dirichlet(n, K, diag_thresh, rng):
    """Sample n column-stochastic KxK matrices with min(diag) >= diag_thresh.

    Uses direct sampling: diagonal d ~ Beta(1,2) truncated to [thresh,1],
    off-diagonal split uniformly on remaining mass.
    """
    C_batch = np.empty((n, K, K))
    for col in range(K):
        # Truncated Beta(1,2): d = 1 - (1-thresh)*sqrt(1-U)
        U = rng.uniform(size=n)
        d = 1.0 - (1.0 - diag_thresh) * np.sqrt(1.0 - U)
        rem = 1.0 - d

        # Uniform split of remaining mass among off-diagonal entries
        # For K=3: 2 off-diagonal entries, split by V ~ Uniform(0,1)
        off_idx = [r for r in range(K) if r != col]
        if len(off_idx) == 2:
            V = rng.uniform(size=n)
            C_batch[:, col, col] = d
            C_batch[:, off_idx[0], col] = rem * V
            C_batch[:, off_idx[1], col] = rem * (1.0 - V)
        else:
            # General K: Dirichlet split
            splits = rng.dirichlet(np.ones(len(off_idx)), size=n)
            C_batch[:, col, col] = d
            for j_idx, j in enumerate(off_idx):
                C_batch[:, j, col] = rem * splits[:, j_idx]

    return C_batch


# ─── Theoretical plim (exposure DAG, single C) ──────────────
def theoretical_plim(C, p_A, beta):
    """Analytical plim for Y ~ 1 + D*_1 + D*_2 under exposure misclassification.

    plim γ = (E[Z'Z])^{-1} E[Z'X] β
    where Z = (1, D*_1, D*_2), X = (1, D_1, D_2).
    """
    q = C @ p_A  # P(A*=k)

    EZZ = np.array([
        [1.0,  q[1], q[2]],
        [q[1], q[1], 0.0],
        [q[2], 0.0,  q[2]],
    ])

    EZX = np.array([
        [1.0,  p_A[1],          p_A[2]],
        [q[1], C[1, 1] * p_A[1], C[1, 2] * p_A[2]],
        [q[2], C[2, 1] * p_A[1], C[2, 2] * p_A[2]],
    ])

    return np.linalg.solve(EZZ, EZX @ beta)


# ─── Perturbation ────────────────────────────────────────────
def perturb_confusion_matrix(C0, eps, rng):
    """Create differential C by adding uniform noise to off-diagonal entries.

    For each column j:
      - Add Uniform(-eps, eps) noise to each off-diagonal entry
      - Clip negatives to 0
      - Re-normalize column to sum to 1
    """
    C_new = C0.copy()
    for col in range(K):
        off_idx = [r for r in range(K) if r != col]
        noise = rng.uniform(-eps, eps, size=len(off_idx))
        for j_idx, j in enumerate(off_idx):
            C_new[j, col] += noise[j_idx]

        # Clip negatives
        C_new[:, col] = np.maximum(C_new[:, col], 1e-12)
        # Re-normalize
        C_new[:, col] /= C_new[:, col].sum()

    return C_new


# ─── Bias classification ────────────────────────────────────
def classify_bias(gamma, beta):
    """Classify bias for components k=1,2.

    Returns (has_sign_flip, has_amplification).
    """
    sf = False
    amp = False
    for k in [1, 2]:
        if abs(beta[k]) < 1e-10:
            continue
        if gamma[k] * beta[k] < 0:
            sf = True
        if abs(gamma[k]) > abs(beta[k]) and gamma[k] * beta[k] > 0:
            amp = True
    return sf, amp


# ─── MC estimator for differential case ─────────────────────
def mc_differential_bias(C_high, C_low, p_A, beta, N, rng):
    """Single MC trial: generate data, apply differential misclassification,
    run OLS, return estimated coefficients.

    Y-high group (Y > median) uses C_high; Y-low uses C_low.
    """
    # Generate true exposure
    A = rng.choice(K, size=N, p=p_A)
    D1 = (A == 1).astype(float)
    D2 = (A == 2).astype(float)
    Y = beta[0] + beta[1] * D1 + beta[2] * D2 + rng.normal(0, 1.0, N)

    y_med = np.median(Y)
    high_mask = Y > y_med

    # Apply differential misclassification
    A_star = np.empty(N, dtype=int)
    for k_true in range(K):
        idx_h = np.where(high_mask & (A == k_true))[0]
        if len(idx_h) > 0:
            A_star[idx_h] = rng.choice(K, size=len(idx_h), p=C_high[:, k_true])

        idx_l = np.where(~high_mask & (A == k_true))[0]
        if len(idx_l) > 0:
            A_star[idx_l] = rng.choice(K, size=len(idx_l), p=C_low[:, k_true])

    # OLS: Y ~ 1 + D*_1 + D*_2
    D1s = (A_star == 1).astype(float)
    D2s = (A_star == 2).astype(float)
    X = np.column_stack([np.ones(N), D1s, D2s])
    coefs = np.linalg.lstsq(X, Y, rcond=None)[0]

    return coefs


# ─── Main analysis ──────────────────────────────────────────
def run_analysis():
    rng = np.random.default_rng(SEED)
    all_results = {}

    print("=" * 78)
    print("Non-Differential Misclassification Stress Test — Exposure DAG (K=3)")
    print("=" * 78)
    print(f"\nDGP: P(A)={P_A.tolist()}, β={BETA.tolist()}, σ=1.0")
    print(f"Confusion matrices: {N_MATRICES:,} per ε level, "
          f"truncated Dirichlet(1,1,1), diag ≥ {DIAG_THRESH}")
    print(f"MC sample size (ε>0): {N_MC:,}")
    print(f"ε levels: {EPSILONS}")
    print(f"Differential mechanism: C_high for Y>median, C_low=C₀ for Y≤median")
    print()

    for eps in EPSILONS:
        t0 = time.time()
        n_sign_flip = 0
        n_amplif = 0
        n_violation = 0
        n_valid = 0

        # Pre-sample all base confusion matrices for this ε level
        C_batch = sample_truncated_dirichlet(N_MATRICES, K, DIAG_THRESH, rng)

        for trial in range(N_MATRICES):
            C0 = C_batch[trial]

            if eps == 0.0:
                # ε=0: analytical plim (no perturbation)
                try:
                    gamma = theoretical_plim(C0, P_A, BETA)
                except np.linalg.LinAlgError:
                    continue
            else:
                # ε>0: perturb C₀ → C_high; C_low = C₀
                C_high = perturb_confusion_matrix(C0, eps, rng)
                C_low = C0  # control group keeps original
                gamma = mc_differential_bias(C_high, C_low, P_A, BETA, N_MC, rng)

            sf, amp = classify_bias(gamma, BETA)
            n_valid += 1
            if sf:
                n_sign_flip += 1
            if amp:
                n_amplif += 1
            if sf or amp:
                n_violation += 1

        elapsed = time.time() - t0
        sf_rate = n_sign_flip / n_valid if n_valid > 0 else 0
        amp_rate = n_amplif / n_valid if n_valid > 0 else 0
        viol_rate = n_violation / n_valid if n_valid > 0 else 0

        result = {
            "epsilon": eps,
            "n_valid": n_valid,
            "n_sign_flip": n_sign_flip,
            "sign_flip_rate": round(sf_rate, 6),
            "n_amplification": n_amplif,
            "amplification_rate": round(amp_rate, 6),
            "n_violation": n_violation,
            "violation_rate": round(viol_rate, 6),
            "elapsed_s": round(elapsed, 1),
            "method": "analytical_plim" if eps == 0 else "mc_differential",
        }
        all_results[str(eps)] = result

        print(f"  ε={eps:.2f}: sign_flip={100*sf_rate:.2f}%, "
              f"amplif={100*amp_rate:.2f}%, "
              f"violation={100*viol_rate:.2f}% "
              f"[{n_valid:,} valid, {elapsed:.1f}s]")

    return all_results


def print_summary(results):
    """Print formatted summary table."""
    print("\n" + "=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    print(f"\n{'ε':>6}  {'Method':>16}  {'Sign-Flip%':>11}  "
          f"{'Amplif%':>9}  {'Violation%':>11}  {'N':>7}")
    print("-" * 66)
    for eps in EPSILONS:
        r = results[str(eps)]
        print(f"{eps:>6.2f}  {r['method']:>16}  "
              f"{100*r['sign_flip_rate']:>10.2f}%  "
              f"{100*r['amplification_rate']:>8.2f}%  "
              f"{100*r['violation_rate']:>10.2f}%  "
              f"{r['n_valid']:>7,}")

    # Relative change vs baseline
    base = results[str(0.0)]
    print(f"\n{'ε':>6}  {'Δ Sign-Flip (pp)':>18}  {'Δ Violation (pp)':>18}")
    print("-" * 44)
    for eps in EPSILONS:
        r = results[str(eps)]
        dsf = 100 * (r['sign_flip_rate'] - base['sign_flip_rate'])
        dviol = 100 * (r['violation_rate'] - base['violation_rate'])
        print(f"{eps:>6.2f}  {dsf:>+17.2f}  {dviol:>+17.2f}")


def generate_appendix_tex(results, out_path):
    """Generate LaTeX paragraph for appendix."""
    base = results[str(0.0)]
    max_eps = results[str(EPSILONS[-1])]
    delta_viol = 100 * (max_eps['violation_rate'] - base['violation_rate'])

    tex = r"""\paragraph{Non-Differential Assumption Stress Test.}
Our main analysis assumes non-differential misclassification---the confusion matrix $C$ does not depend on the outcome $Y$.
To assess sensitivity to violations of this assumption, we conduct a stress test on the exposure topology ($K{=}3$).
For each base confusion matrix $C_0$ sampled from the truncated Dirichlet prior ($\min(\mathrm{diag}(C)) \geq 0.7$, $n=%s$),
we introduce controlled differential error: observations with $Y > \mathrm{median}(Y)$ are misclassified
using a perturbed matrix $\tilde{C} = \mathrm{renormalize}(C_0 + \varepsilon \cdot \Delta)$ where
$\Delta_{ji} \sim \mathrm{Uniform}(-1,1)$ for off-diagonal entries, while observations with
$Y \leq \mathrm{median}(Y)$ retain the original $C_0$.

\begin{table}[h]
\centering
\small
\begin{tabular}{cccc}
\toprule
$\varepsilon$ & Sign-Flip (\%%) & Amplification (\%%) & Any Violation (\%%) \\
\midrule
""" % f"{N_MATRICES:,}"

    for eps in EPSILONS:
        r = results[str(eps)]
        tex += f"{eps:.2f} & {100*r['sign_flip_rate']:.1f} & " \
               f"{100*r['amplification_rate']:.1f} & " \
               f"{100*r['violation_rate']:.1f} \\\\\n"

    tex += r"""\bottomrule
\end{tabular}
\caption{Effect of differential misclassification on bias violation rates (exposure DAG, $K{=}3$, $\min(\mathrm{diag}(C)) \geq 0.7$).
"""
    tex += f"At $\\varepsilon = {EPSILONS[-1]}$, the violation rate changes by {delta_viol:+.1f} percentage points relative to the non-differential baseline ($\\varepsilon = 0$), "
    if abs(delta_viol) < 3.0:
        tex += "indicating robustness of the main results to moderate assumption violations."
    elif abs(delta_viol) < 10.0:
        tex += "indicating moderate sensitivity that warrants caution when the non-differential assumption is substantially violated."
    else:
        tex += "indicating substantial sensitivity to differential error, suggesting the non-differential assumption is important for the main conclusions."
    tex += r"""}
\label{tab:nondiff_stress}
\end{table}

"""

    with open(out_path, "w") as f:
        f.write(tex)
    print(f"\nAppendix LaTeX saved to: {out_path}")


def main():
    t_start = time.time()

    results = run_analysis()
    print_summary(results)

    # Save JSON
    output = {
        "experiment": "nondiff_stress_test",
        "topology": "exposure",
        "K": K,
        "diag_threshold": DIAG_THRESH,
        "n_confusion_matrices": N_MATRICES,
        "n_mc_per_trial": N_MC,
        "P_A": P_A.tolist(),
        "beta": BETA.tolist(),
        "mechanism": "Y-dependent: C_high=perturb(C₀,ε) for Y>median, C_low=C₀ for Y≤median",
        "perturbation": "Off-diagonal entries += Uniform(-ε,ε), then clip & renormalize",
        "seed": SEED,
        "results": results,
    }

    base_dir = "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts"
    json_path = f"{base_dir}/nondiff_stress_test_results.json"
    tex_path = f"{base_dir}/nondiff_stress_test_appendix.tex"

    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON results saved to: {json_path}")

    generate_appendix_tex(results, tex_path)

    elapsed_total = time.time() - t_start
    print(f"\nTotal runtime: {elapsed_total:.1f}s")


if __name__ == "__main__":
    main()
