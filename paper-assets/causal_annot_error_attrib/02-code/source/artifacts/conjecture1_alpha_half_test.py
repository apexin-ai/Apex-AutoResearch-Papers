#!/usr/bin/env python3
"""
Targeted test: Is α_j ≥ 1/2 sufficient for V_B'(1) ≤ 0?

Uses correct column-stochastic generation that guarantees min diagonal ≥ target
AFTER normalization.
"""

import numpy as np
import json
import os


def make_column_stochastic(K, rng, min_diag):
    """Generate column-stochastic C0 with guaranteed (C0)_{jj} ≥ min_diag after normalization."""
    C0 = np.zeros((K, K))
    for k in range(K):
        off_diag = rng.dirichlet(np.ones(K - 1))
        off_diag *= (1 - min_diag)
        idx = 0
        for j in range(K):
            if j == k:
                C0[j, k] = min_diag
            else:
                C0[j, k] = off_diag[idx]
                idx += 1
    assert np.allclose(C0.sum(axis=0), 1.0)
    assert np.all(np.diag(C0) >= min_diag - 1e-15)
    return C0


def compute_VBp1(C0, p, g):
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


def compute_VB(C, p, g):
    q = C @ p
    N = C @ (p * g)
    gbar = p @ g
    return np.sum(N**2 / q) - gbar**2


def compute_step_deviation(C0, p, g, n_delta=501):
    K = len(p)
    I = np.eye(K)
    deltas = np.linspace(0, 1, n_delta)
    VBs = np.array([compute_VB((1 - d) * I + d * C0, p, g) for d in deltas])
    diffs = np.diff(VBs)
    increases = diffs[diffs > 0]
    return float(increases.max()) if len(increases) > 0 else 0.0


def main():
    rng = np.random.default_rng(42)

    configs = [
        ('α≥0.50', 0.50),
        ('α≥0.40', 0.40),
        ('α≥0.34', 0.34),  # just above 1/3 for K=3
        ('α≥0.30', 0.30),
    ]

    results = {}

    for label, min_diag in configs:
        print(f"\n{'='*60}")
        print(f"Testing: {label} (guaranteed after normalization)")
        print(f"{'='*60}")

        n_tests = 100_000
        n_pos = 0
        max_vbp1 = 0.0
        max_step = 0.0
        counterexamples = []

        for i in range(n_tests):
            K = rng.choice([3, 5, 7, 10])
            C0 = make_column_stochastic(K, rng, min_diag)
            p = rng.dirichlet(np.ones(K))
            g = rng.standard_normal(K)

            vbp1 = compute_VBp1(C0, p, g)

            if vbp1 > 1e-8:
                n_pos += 1
                if vbp1 > max_vbp1:
                    max_vbp1 = vbp1
                    sd = compute_step_deviation(C0, p, g)
                    max_step = max(max_step, sd)

                if len(counterexamples) < 10:
                    counterexamples.append({
                        'K': int(K),
                        'vbp1': float(vbp1),
                        'C0_diag': np.diag(C0).tolist(),
                        'C0_diag_min': float(np.diag(C0).min()),
                        'p': p.tolist(),
                        'p_ratio': float(p.max() / p.min()),
                    })

            if (i + 1) % 25000 == 0:
                print(f"  [{i+1}/{n_tests}] V'>0: {n_pos} ({100*n_pos/(i+1):.2f}%)")

        results[label] = {
            'min_diag': min_diag,
            'n_tests': n_tests,
            'n_positive': n_pos,
            'frac_positive': n_pos / n_tests,
            'max_vbp1': max_vbp1,
            'max_step_deviation': max_step,
            'counterexamples': counterexamples[:5],
        }

        print(f"\n  Result: V'(1)>0 in {n_pos}/{n_tests} ({100*n_pos/n_tests:.3f}%)")
        print(f"  Max V_B'(1): {max_vbp1:.6f}")
        print(f"  Max step deviation: {max_step:.6f}")
        if counterexamples:
            ce = counterexamples[0]
            print(f"  First counterexample: K={ce['K']}, V'={ce['vbp1']:.6f}, "
                  f"α_min={ce['C0_diag_min']:.4f}, p_ratio={ce['p_ratio']:.1f}")

    # Special test: α ≥ 1/2, uniform p only
    print(f"\n{'='*60}")
    print("Special: α≥0.50, uniform p only")
    print(f"{'='*60}")
    n_tests = 100_000
    n_pos = 0

    for _ in range(n_tests):
        K = rng.choice([3, 5, 7, 10])
        C0 = make_column_stochastic(K, rng, 0.5)
        p = np.ones(K) / K
        g = rng.standard_normal(K)
        vbp1 = compute_VBp1(C0, p, g)
        if vbp1 > 1e-8:
            n_pos += 1

    results['α≥0.50_uniform_p'] = {
        'n_tests': n_tests,
        'n_positive': n_pos,
        'frac_positive': n_pos / n_tests,
    }
    print(f"  V'(1)>0: {n_pos}/{n_tests} ({100*n_pos/n_tests:.3f}%)")

    # Special test: doubly stochastic (not symmetric) with α ≥ 1/2
    print(f"\n{'='*60}")
    print("Special: doubly stochastic (not necessarily symmetric), α≥0.50, any p")
    print(f"{'='*60}")

    def make_doubly_stochastic(K, rng, min_diag=0.5, n_iter=100):
        C = make_column_stochastic(K, rng, min_diag)
        for _ in range(n_iter):
            C = C / C.sum(axis=1, keepdims=True)  # normalize rows
            for k in range(K):
                C[k, k] = max(C[k, k], min_diag)
            C = C / C.sum(axis=0, keepdims=True)  # normalize columns
            for k in range(K):
                C[k, k] = max(C[k, k], min_diag)
            C = C / C.sum(axis=0, keepdims=True)
        return C

    n_tests = 50_000
    n_pos = 0
    n_valid = 0

    for _ in range(n_tests):
        K = rng.choice([3, 5, 7])
        C0 = make_doubly_stochastic(K, rng, 0.5)
        if not np.allclose(C0.sum(axis=0), 1.0, atol=0.01):
            continue
        if not np.allclose(C0.sum(axis=1), 1.0, atol=0.01):
            continue
        if np.diag(C0).min() < 0.49:
            continue
        n_valid += 1

        p = rng.dirichlet(np.ones(K))
        g = rng.standard_normal(K)
        vbp1 = compute_VBp1(C0, p, g)
        if vbp1 > 1e-8:
            n_pos += 1

    results['DS_α≥0.50_any_p'] = {
        'n_valid': n_valid,
        'n_positive': n_pos,
        'frac_positive': n_pos / max(n_valid, 1),
    }
    print(f"  Valid DS matrices: {n_valid}")
    print(f"  V'(1)>0: {n_pos}/{n_valid} ({100*n_pos/max(n_valid,1):.3f}%)")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'conjecture1_alpha_half_results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2, default=lambda o: float(o) if hasattr(o, '__float__') else int(o))
    print(f"\nResults → {out_path}")


if __name__ == '__main__':
    main()
