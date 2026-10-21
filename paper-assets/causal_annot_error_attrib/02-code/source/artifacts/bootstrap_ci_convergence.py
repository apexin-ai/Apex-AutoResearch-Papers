#!/usr/bin/env python3
"""
Bootstrap CI Convergence vs Validation Set Size N

Demonstrates that the 95% bootstrap CI width for ASV δ* shrinks as the
gold-label validation set size N increases, following O(1/√N) scaling.

Setup:
  - K=3 classes, two topologies (exposure, iv)
  - B=1000 bootstrap replications per (N, topology) cell
  - N ∈ {500, 1000, 2000, 5000, 10000, 50000}
  - Confusion matrix C₀ sampled from Dirichlet with min diagonal ≥ 0.6
  - Sufficient statistics precomputed once at N_precomp=500000

Output: artifacts/bootstrap_ci_convergence_results.json
"""

import json
import os
import sys
import time
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

ARTIFACTS = os.path.dirname(os.path.abspath(__file__))

# ── Config ──────────────────────────────────────────────────────
K = 3
B = 1000
SEED = 2026
N_VALUES = [500, 1000, 2000, 5000, 10000, 50000]
TOPOLOGIES = ['exposure', 'iv']
N_PRECOMP = 500_000
N_GRID = 1500
BIAS_THRESHOLD = 0.10

# ── DGP param pools (same as exp_c / compute_ppi_empirical) ────
_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]


def softmax_rows(x):
    e = np.exp(x - x.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def make_p_A(K):
    """Class prevalence for K=3: [0.40, 0.35, 0.25]."""
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / (i + 1) for i in range(K)])
    return raw / raw.sum()


def make_dgp_params(K):
    """Return topology-specific DGP parameter dicts for K=3."""
    p_A = make_p_A(K)
    params = {
        'exposure': {
            'beta': np.array(_BETA_POOL[:K]),
            'p_A': p_A,
        },
    }
    if K == 3:
        params['iv'] = {
            'lam': 1.0,
            'beta': np.array([0.0, 0.5, -0.25]),
            'g': np.zeros(3),
            'dZ': np.array([0.0, 1.0, -0.5]),
            'dU': np.array([0.0, 0.8, 0.6]),
        }
    else:
        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
        iv_beta[0] = 0.0
        params['iv'] = {
            'lam': 1.0, 'beta': iv_beta,
            'g': np.zeros(K),
            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
        }
    return params


# ── DGP generators ─────────────────────────────────────────────

def gen_exposure(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
    return None, Y, A


def gen_iv(K, N, p, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
              + p['dU'][None, :] * U[:, None])
    A = sample_cat(softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
    return Z, Y, A


GEN_FNS = {'exposure': gen_exposure, 'iv': gen_iv}


# ── Sufficient statistics & plim ───────────────────────────────

def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
    """Generate a large synthetic dataset and compute summary statistics
    used for the probability-limit (plim) calculation.

    Args:
        K: number of classes
        topology: 'exposure' or 'iv'
        params: topology-specific parameter dict (not the full params dict)
        N: sample size for precomputation
        seed: random seed

    Returns:
        dict of sufficient statistics with a 'topology' key
    """
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
    DA = np.zeros((N, K))
    for k in range(K):
        DA[:, k] = (A == k).astype(float)

    if topology == 'iv':
        Z = first_var
        z1 = Z == 1
        z0 = Z == 0
        RF = Y[z1].mean() - Y[z0].mean()
        FS = np.zeros(K)
        for k in range(K):
            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
        return dict(RF=RF, FS=FS, topology='iv')
    elif topology == 'exposure':
        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
    else:
        raise ValueError(f"Unsupported topology: {topology}")


def compute_plim(C, st, K):
    """Compute the probability limit of the OLS/Wald estimator given
    confusion matrix C and precomputed sufficient statistics.

    Args:
        C: K×K column-stochastic confusion matrix
        st: sufficient statistics dict from precompute_suff_stats
        K: number of classes

    Returns:
        scalar (iv) or array of coefficients (exposure)
    """
    if st['topology'] == 'iv':
        FS_star = C @ st['FS']
        if abs(FS_star[1]) < 1e-8:
            return np.nan
        return st['RF'] / FS_star[1]
    elif st['topology'] == 'exposure':
        q = C @ st['p_A']
        cy = C @ st['E_YD']
        EZZ = np.zeros((K, K))
        EZZ[0, 0] = 1.0
        for j in range(1, K):
            EZZ[0, j] = EZZ[j, 0] = q[j]
            EZZ[j, j] = q[j]
        EZY = np.zeros(K)
        EZY[0] = st['E_Y']
        for j in range(1, K):
            EZY[j] = cy[j]
        try:
            return np.linalg.solve(EZZ, EZY)
        except np.linalg.LinAlgError:
            return np.full(K, np.nan)
    else:
        raise ValueError(f"Unsupported topology: {st['topology']}")


def extract_tau(plim_result, topology):
    """Extract scalar treatment-effect estimate from plim result.

    For iv: plim_result is already a scalar.
    For exposure: plim_result is a coefficient vector; tau = beta[1].
    """
    if topology == 'iv':
        return float(plim_result) if np.isfinite(plim_result) else np.nan
    if isinstance(plim_result, np.ndarray):
        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
    return np.nan


# ── ASV δ* computation ─────────────────────────────────────────

def C_interpolated(C0, delta, K):
    """Interpolate confusion matrix: C(δ) = (1-δ)I + δC₀,
    then re-normalize columns to sum to 1."""
    C_d = (1 - delta) * np.eye(K) + delta * C0
    C_d = np.maximum(C_d, 0.0)
    col_sums = C_d.sum(axis=0)
    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
    return C_d / col_sums


def compute_delta_max(C0):
    """Maximum δ before a diagonal entry hits zero."""
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        return 10.0
    return min(1.0 / (1.0 - min_diag), 10.0)


def compute_magnitude_delta_star(C0, K, topology, st, tau_true):
    """Find the smallest δ such that the worst-case bias along the
    interpolation path C(δ) exceeds bias_threshold × |τ_true|.

    Returns δ* (float) or None if threshold is never reached.
    """
    if abs(tau_true) < 1e-12:
        return None
    dmax = compute_delta_max(C0)
    deltas = np.linspace(0, dmax, N_GRID)
    thresh = BIAS_THRESHOLD * abs(tau_true)
    running_max = 0.0
    for i, d in enumerate(deltas):
        C_d = C_interpolated(C0, d, K)
        plim_result = compute_plim(C_d, st, K)
        tau_d = extract_tau(plim_result, topology)
        bias = abs(tau_d - tau_true)
        if np.isfinite(bias):
            running_max = max(running_max, bias)
        if running_max > thresh:
            return float(d)
    return None


# ── Confusion matrix generation ────────────────────────────────

def sample_C0(K, rng, min_diag=0.6, max_attempts=10000):
    """Sample a K×K column-stochastic confusion matrix from Dirichlet
    with min diagonal entry ≥ min_diag.

    Each column is drawn from Dirichlet(alpha) where the diagonal entry
    has a high concentration parameter to encourage diagonal dominance.
    """
    for _ in range(max_attempts):
        C = np.zeros((K, K))
        ok = True
        for j in range(K):
            # High concentration on diagonal
            alpha = np.ones(K) * 0.5
            alpha[j] = 5.0
            col = rng.dirichlet(alpha)
            if col[j] < min_diag:
                ok = False
                break
            C[:, j] = col
        if ok:
            return C
    raise RuntimeError(f"Failed to sample C0 with min_diag={min_diag} "
                       f"after {max_attempts} attempts")


def generate_label_pairs(C0, K, N, rng):
    """Generate N synthetic (gold_label, predicted_label) pairs.

    Gold labels are drawn uniformly, then predicted labels are drawn
    according to the columns of the confusion matrix C0.

    Args:
        C0: K×K column-stochastic confusion matrix (C0[i,j] = P(pred=i|gold=j))
        K: number of classes
        N: number of pairs to generate
        rng: numpy random generator

    Returns:
        list of (gold, pred) tuples
    """
    gold_labels = rng.integers(0, K, size=N)
    pred_labels = np.empty(N, dtype=int)
    for i in range(N):
        g = gold_labels[i]
        pred_labels[i] = rng.choice(K, p=C0[:, g])
    return list(zip(gold_labels.tolist(), pred_labels.tolist()))


def pairs_to_C0(pairs, K):
    """Compute column-stochastic confusion matrix from (gold, pred) pairs."""
    counts = np.zeros((K, K))
    for gold, pred in pairs:
        counts[pred, gold] += 1
    col_sums = counts.sum(axis=0)
    col_sums = np.where(col_sums < 1, 1.0, col_sums)
    return counts / col_sums


# ── Main ───────────────────────────────────────────────────────

def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    # 1. Sample a representative C0
    print(f"Sampling C0 (K={K}, min diagonal >= 0.6)...")
    C0 = sample_C0(K, rng, min_diag=0.6)
    print(f"C0 diagonal: {np.diag(C0).round(4)}")
    print(f"C0:\n{np.array2string(C0, precision=4, suppress_small=True)}")

    # 2. Build DGP params for K=3
    params = make_dgp_params(K)

    # 3. Precompute sufficient statistics (large N)
    print(f"\nPrecomputing sufficient statistics (N_precomp={N_PRECOMP:,})...")
    suff_stats = {}
    tau_trues = {}
    for topo in TOPOLOGIES:
        st = precompute_suff_stats(K, topo, params[topo], N=N_PRECOMP, seed=42)
        suff_stats[topo] = st
        plim_I = compute_plim(np.eye(K), st, K)
        tau_trues[topo] = extract_tau(plim_I, topo)
        print(f"  {topo}: tau_true = {tau_trues[topo]:.6f}")

    # 4. Point estimate δ* with the true C0
    print(f"\nPoint estimate δ* (true C0):")
    for topo in TOPOLOGIES:
        ds = compute_magnitude_delta_star(C0, K, topo, suff_stats[topo],
                                          tau_trues[topo])
        print(f"  {topo}: δ* = {ds}")

    # 5. Bootstrap for each N value
    results = {
        'meta': {
            'K': K,
            'B': B,
            'N_values': N_VALUES,
            'bias_threshold': BIAS_THRESHOLD,
            'N_precomp': N_PRECOMP,
            'seed': SEED,
            'topologies': TOPOLOGIES,
        },
        'C0': C0.tolist(),
        'tau_trues': {topo: tau_trues[topo] for topo in TOPOLOGIES},
        'results': {topo: {} for topo in TOPOLOGIES},
    }

    for ni, N_val in enumerate(N_VALUES):
        print(f"\n{'='*60}")
        print(f"N = {N_val:,}  [{ni+1}/{len(N_VALUES)}]")
        print(f"{'='*60}")

        # Generate N label pairs from the true C0
        pairs = generate_label_pairs(C0, K, N_val, rng)

        # Point estimate from these N pairs
        C0_hat = pairs_to_C0(pairs, K)
        print(f"  C0_hat diagonal: {np.diag(C0_hat).round(4)}")

        for topo in TOPOLOGIES:
            t_topo = time.time()
            ds_point = compute_magnitude_delta_star(
                C0_hat, K, topo, suff_stats[topo], tau_trues[topo])

            # Bootstrap
            boot_samples = []
            for b in range(B):
                # Resample pairs with replacement
                idx = rng.integers(0, N_val, size=N_val)
                boot_pairs = [pairs[i] for i in idx]
                C0_b = pairs_to_C0(boot_pairs, K)
                ds_b = compute_magnitude_delta_star(
                    C0_b, K, topo, suff_stats[topo], tau_trues[topo])
                boot_samples.append(ds_b)

                if (b + 1) % 200 == 0:
                    elapsed = time.time() - t_topo
                    eta = elapsed / (b + 1) * (B - b - 1)
                    print(f"    {topo} [{b+1}/{B}] "
                          f"{elapsed:.0f}s elapsed, ETA {eta:.0f}s")

            valid = [s for s in boot_samples if s is not None]
            n_valid = len(valid)
            n_none = B - n_valid

            if n_valid > 0:
                arr = np.array(valid)
                ci_lo = float(np.percentile(arr, 2.5))
                ci_hi = float(np.percentile(arr, 97.5))
                ci_width = ci_hi - ci_lo
            else:
                ci_lo = ci_hi = ci_width = None

            cell = {
                'delta_star_point': ds_point,
                'ci_lower': ci_lo,
                'ci_upper': ci_hi,
                'ci_width': ci_width,
                'n_valid': n_valid,
                'n_none': n_none,
            }
            results['results'][topo][str(N_val)] = cell

            elapsed_topo = time.time() - t_topo
            print(f"  {topo}: δ*={ds_point}, "
                  f"CI=[{ci_lo}, {ci_hi}], width={ci_width}, "
                  f"valid={n_valid}/{B} ({elapsed_topo:.0f}s)")

    # 6. Print summary table
    print(f"\n{'='*70}")
    print("SUMMARY: CI width vs N")
    print(f"{'='*70}")
    print(f"{'N':>8s}", end="")
    for topo in TOPOLOGIES:
        print(f"  {topo+' width':>16s}  {topo+' valid':>12s}", end="")
    print()
    print("-" * (8 + (16 + 14) * len(TOPOLOGIES)))

    for N_val in N_VALUES:
        print(f"{N_val:>8d}", end="")
        for topo in TOPOLOGIES:
            cell = results['results'][topo][str(N_val)]
            w = cell['ci_width']
            v = cell['n_valid']
            if w is not None:
                print(f"  {w:>16.6f}  {v:>10d}/{B}", end="")
            else:
                print(f"  {'N/A':>16s}  {v:>10d}/{B}", end="")
        print()

    # Check O(1/√N) scaling
    print(f"\nO(1/√N) scaling check (ratio of width × √N across N values):")
    for topo in TOPOLOGIES:
        print(f"  {topo}:")
        products = []
        for N_val in N_VALUES:
            cell = results['results'][topo][str(N_val)]
            w = cell['ci_width']
            if w is not None:
                product = w * np.sqrt(N_val)
                products.append(product)
                print(f"    N={N_val:>6d}: width={w:.6f}, "
                      f"width×√N={product:.4f}")
            else:
                print(f"    N={N_val:>6d}: width=N/A")
        if len(products) >= 2:
            cv = np.std(products) / np.mean(products)
            print(f"    CV of (width×√N) = {cv:.4f} "
                  f"(close to 0 → good O(1/√N) scaling)")

    # 7. Save results
    json_path = os.path.join(ARTIFACTS, 'bootstrap_ci_convergence_results.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON -> {json_path}")

    total = time.time() - t0
    print(f"\nDone in {total:.0f}s ({total / 60:.1f}min)")


if __name__ == '__main__':
    main()
