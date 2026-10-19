#!/usr/bin/env python3
"""
Extended analysis for Conjecture 1 proof.

1. Relationship between V_B'(1) and actual step deviation ε
2. Tighter quantitative bounds
3. Diagonal dominance condition coverage for realistic classifiers
4. Spectral analysis of M matrix under various conditions
"""

import numpy as np
import json
import os

SEED = 2024


def random_cs(K, rng, min_diag=0.0):
    C0 = rng.dirichlet(np.ones(K), size=K).T
    if min_diag > 0:
        for k in range(K):
            C0[k, k] = max(C0[k, k], min_diag)
            C0[:, k] /= C0[:, k].sum()
    return C0


def compute_VB(C, p, g):
    q = C @ p
    N = C @ (p * g)
    gbar = p @ g
    return np.sum(N**2 / q) - gbar**2


def compute_VBp1(C0, p, g):
    """Director's formula for V_B'(1)."""
    K = len(p)
    q = C0 @ p
    N = C0 @ (p * g)
    mu = N / q
    e = g - mu
    term1 = np.sum((p + q) * e**2)
    term2 = 0.0
    for j in range(K):
        for k in range(K):
            if j != k:
                term2 += C0[j, k] * p[k] * (g[j] - g[k])**2
    return term1 - term2


def compute_VB_curve(C0, p, g, n_delta=201):
    K = len(p)
    I = np.eye(K)
    deltas = np.linspace(0, 1, n_delta)
    VBs = np.array([compute_VB((1 - d) * I + d * C0, p, g) for d in deltas])
    return deltas, VBs


def measure_step_deviation(deltas, VBs):
    """Max single-step increase in V_B (should be decreasing)."""
    diffs = np.diff(VBs)
    increases = diffs[diffs > 0]
    return float(increases.max()) if len(increases) > 0 else 0.0


def dd_condition_ratio(C0, p):
    """Return max ratio q_j/(p_j+q_j)/alpha_j across j. If ≤ 1, DD holds."""
    K = len(p)
    q = C0 @ p
    alpha = np.diag(C0)
    ratios = []
    for j in range(K):
        if p[j] > 1e-15:
            threshold = q[j] / (p[j] + q[j])
            ratios.append(threshold / alpha[j])
    return max(ratios)


def M_eigenvalues(C0, p):
    K = len(p)
    W = C0 * p[np.newaxis, :]
    q = W.sum(axis=1)
    T = np.diag(1.0 / q) @ W
    D_pq = np.diag(p + q)
    ImT = np.eye(K) - T
    M = ImT.T @ D_pq @ ImT - (D_pq - 2 * W)
    Ms = (M + M.T) / 2
    return np.sort(np.linalg.eigvalsh(Ms))


def main():
    rng = np.random.default_rng(SEED)
    results = {}

    # === Part 1: V_B'(1) vs actual step deviation ===
    print("Part 1: V_B'(1) vs step deviation")
    n_part1 = 20_000
    data_vbp1 = []
    data_eps = []
    data_K = []
    data_diag_min = []

    for i in range(n_part1):
        K = rng.choice([3, 5, 7])
        C0 = random_cs(K, rng, min_diag=0.1)
        p = rng.dirichlet(np.ones(K))
        g = rng.standard_normal(K)

        vbp1 = compute_VBp1(C0, p, g)
        if vbp1 > 1e-10:
            deltas, VBs = compute_VB_curve(C0, p, g, n_delta=201)
            eps = measure_step_deviation(deltas, VBs)
            data_vbp1.append(vbp1)
            data_eps.append(eps)
            data_K.append(int(K))
            data_diag_min.append(float(np.diag(C0).min()))

    data_vbp1 = np.array(data_vbp1)
    data_eps = np.array(data_eps)

    if len(data_vbp1) > 0:
        corr = np.corrcoef(data_vbp1, data_eps)[0, 1]
        ratio = data_eps / np.maximum(data_vbp1, 1e-15)
        print(f"  Cases with V_B'(1)>0: {len(data_vbp1)}")
        print(f"  Correlation(V_B'(1), ε): {corr:.4f}")
        print(f"  ε/V_B'(1) ratio: median={np.median(ratio):.4f}, "
              f"max={ratio.max():.4f}, p95={np.percentile(ratio, 95):.4f}")
        print(f"  Max step deviation: {data_eps.max():.6f}")
        print(f"  Max V_B'(1): {data_vbp1.max():.6f}")

    results['part1_vbp1_vs_eps'] = {
        'n_positive_vbp1': len(data_vbp1),
        'correlation': float(corr) if len(data_vbp1) > 1 else 0,
        'eps_over_vbp1_median': float(np.median(ratio)) if len(ratio) > 0 else 0,
        'eps_over_vbp1_max': float(ratio.max()) if len(ratio) > 0 else 0,
        'max_step_deviation': float(data_eps.max()) if len(data_eps) > 0 else 0,
        'max_vbp1': float(data_vbp1.max()) if len(data_vbp1) > 0 else 0,
    }

    # === Part 2: How often does DD hold for realistic classifiers? ===
    print("\nPart 2: DD condition coverage for realistic classifiers")
    acc_levels = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    p_skews = [1.0, 2.0, 5.0, 10.0]  # max/min p ratio

    dd_results = {}
    for acc in acc_levels:
        for skew in p_skews:
            n_test = 3000
            n_dd_holds = 0
            n_vbp1_neg = 0
            max_vbp1 = 0.0

            for _ in range(n_test):
                K = rng.choice([3, 5, 7])
                C0 = random_cs(K, rng, min_diag=acc)

                # Create skewed p
                raw = rng.uniform(1, skew, K)
                p = raw / raw.sum()

                g = rng.standard_normal(K)

                ratio = dd_condition_ratio(C0, p)
                vbp1 = compute_VBp1(C0, p, g)

                if ratio <= 1.0:
                    n_dd_holds += 1
                if vbp1 <= 1e-10:
                    n_vbp1_neg += 1
                max_vbp1 = max(max_vbp1, vbp1)

            key = f"acc={acc:.2f}_skew={skew:.1f}"
            dd_results[key] = {
                'dd_fraction': n_dd_holds / n_test,
                'vbp1_neg_fraction': n_vbp1_neg / n_test,
                'max_vbp1_when_positive': max_vbp1,
            }
            print(f"  acc≥{acc:.2f}, p_skew≤{skew:.0f}: "
                  f"DD holds {100*n_dd_holds/n_test:.1f}%, "
                  f"V'≤0 {100*n_vbp1_neg/n_test:.1f}%, "
                  f"max V'={max_vbp1:.4f}")

    results['part2_dd_coverage'] = dd_results

    # === Part 3: Tight bound analysis ===
    print("\nPart 3: Tight bound on V_B'(1)/Var(g)")
    n_part3 = 50_000
    ratios_by_c = {c: [] for c in [0.3, 0.5, 0.7, 0.9]}

    for _ in range(n_part3):
        K = rng.choice([3, 5, 7, 10])
        c = rng.choice(list(ratios_by_c.keys()))
        C0 = random_cs(K, rng, min_diag=c)
        p = rng.dirichlet(np.ones(K))
        g = rng.standard_normal(K)

        vbp1 = compute_VBp1(C0, p, g)
        var_g = np.sum(p * g**2) - (p @ g)**2
        Rg = g.max() - g.min()

        if var_g > 1e-10 and vbp1 > 0:
            ratios_by_c[c].append(vbp1 / var_g)

    tight_bounds = {}
    for c, rats in ratios_by_c.items():
        if rats:
            arr = np.array(rats)
            theoretical = (1 - c)**2 * 4  # crude bound V'(1)/(Var(g)) ≤ 4(1-c)²
            tight_bounds[f"c={c:.1f}"] = {
                'n_positive': len(arr),
                'max_ratio': float(arr.max()),
                'p99_ratio': float(np.percentile(arr, 99)),
                'median_ratio': float(np.median(arr)),
                'theoretical_bound_4(1-c)2': theoretical,
                'tightness': float(arr.max() / theoretical) if theoretical > 0 else 0,
            }
            print(f"  c={c:.1f}: max V'/Var(g) = {arr.max():.4f}, "
                  f"theory ≤ {theoretical:.4f}, "
                  f"tightness={arr.max()/theoretical:.2%}")

    results['part3_tight_bounds'] = tight_bounds

    # === Part 4: Spectral analysis for DD condition ===
    print("\nPart 4: M eigenvalue structure")
    n_part4 = 5000
    eig_data = {'dd_holds': [], 'dd_fails': []}

    for _ in range(n_part4):
        K = rng.choice([3, 5, 7])
        C0 = random_cs(K, rng, min_diag=0.3)
        p = rng.dirichlet(np.ones(K))

        eigs = M_eigenvalues(C0, p)
        ratio = dd_condition_ratio(C0, p)

        if ratio <= 1.0:
            eig_data['dd_holds'].append(float(eigs.max()))
        else:
            eig_data['dd_fails'].append(float(eigs.max()))

    for key in eig_data:
        arr = np.array(eig_data[key]) if eig_data[key] else np.array([0.0])
        print(f"  {key}: n={len(arr)}, max_eig={arr.max():.6f}, "
              f"frac>0={np.mean(arr>1e-10):.3f}")

    results['part4_spectral'] = {
        k: {
            'n': len(v),
            'max_eigenvalue': float(max(v)) if v else 0,
            'frac_positive': float(np.mean(np.array(v) > 1e-10)) if v else 0,
        }
        for k, v in eig_data.items()
    }

    # === Part 5: Check if we can prove something for α_j ≥ 1/2, any p ===
    print("\nPart 5: α_j ≥ 1/2, general p (not necessarily uniform)")
    n_part5 = 30_000
    n_vbp1_pos = 0
    max_vbp1 = 0.0
    max_step_dev = 0.0
    worst_case = None

    for _ in range(n_part5):
        K = rng.choice([3, 5, 7, 10])
        C0 = random_cs(K, rng, min_diag=0.5)
        p = rng.dirichlet(np.ones(K))
        g = rng.standard_normal(K)

        vbp1 = compute_VBp1(C0, p, g)
        if vbp1 > 1e-10:
            n_vbp1_pos += 1
            if vbp1 > max_vbp1:
                max_vbp1 = vbp1
                deltas, VBs = compute_VB_curve(C0, p, g, 201)
                sd = measure_step_deviation(deltas, VBs)
                max_step_dev = max(max_step_dev, sd)
                worst_case = {
                    'K': int(K),
                    'vbp1': float(vbp1),
                    'step_dev': float(sd),
                    'C0_diag': np.diag(C0).tolist(),
                    'p': p.tolist(),
                    'p_ratio': float(p.max() / p.min()),
                }

    print(f"  α_j ≥ 0.5, general p: V'(1)>0 in {n_vbp1_pos}/{n_part5} "
          f"({100*n_vbp1_pos/n_part5:.1f}%)")
    print(f"  Max V_B'(1) when positive: {max_vbp1:.6f}")
    print(f"  Max step deviation: {max_step_dev:.6f}")
    if worst_case:
        print(f"  Worst: K={worst_case['K']}, "
              f"diag={[f'{d:.3f}' for d in worst_case['C0_diag']]}, "
              f"p_ratio={worst_case['p_ratio']:.1f}")

    results['part5_half_diag'] = {
        'n_tests': n_part5,
        'n_vbp1_positive': n_vbp1_pos,
        'frac_positive': n_vbp1_pos / n_part5,
        'max_vbp1': max_vbp1,
        'max_step_deviation': max_step_dev,
        'worst_case': worst_case,
    }

    # === Part 6: Check α ≥ 1/2, column-stochastic (not doubly stochastic) ===
    # Is α_j ≥ 1/2 alone sufficient for V_B'(1) ≤ 0?
    print("\nPart 6: Is α_j ≥ 1/2 sufficient WITHOUT doubly stochastic?")
    n_part6 = 100_000
    n_counterex = 0
    counterexamples = []

    for _ in range(n_part6):
        K = rng.choice([3, 5, 7])
        C0 = random_cs(K, rng, min_diag=0.5)
        p = rng.dirichlet(np.ones(K))
        g = rng.standard_normal(K)

        vbp1 = compute_VBp1(C0, p, g)
        if vbp1 > 1e-8:
            n_counterex += 1
            if len(counterexamples) < 5:
                counterexamples.append({
                    'K': int(K),
                    'vbp1': float(vbp1),
                    'C0_diag': np.diag(C0).tolist(),
                    'C0_diag_min': float(np.diag(C0).min()),
                    'p': p.tolist(),
                    'g': g.tolist(),
                    'p_ratio': float(p.max() / p.min()),
                })

    print(f"  V_B'(1) > 0 with α_j ≥ 0.5: {n_counterex}/{n_part6} "
          f"({100*n_counterex/n_part6:.2f}%)")
    if counterexamples:
        for i, ce in enumerate(counterexamples[:3]):
            print(f"  Example {i+1}: K={ce['K']}, V'={ce['vbp1']:.6f}, "
                  f"α_min={ce['C0_diag_min']:.3f}, p_ratio={ce['p_ratio']:.1f}")

    results['part6_half_diag_sufficiency'] = {
        'n_tests': n_part6,
        'n_counterexamples': n_counterex,
        'alpha_half_is_sufficient': n_counterex == 0,
        'examples': counterexamples[:5],
    }

    # Save
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'conjecture1_extended_results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=lambda o: float(o) if hasattr(o, '__float__') else int(o))

    print(f"\nResults → {out_path}")


if __name__ == '__main__':
    main()
