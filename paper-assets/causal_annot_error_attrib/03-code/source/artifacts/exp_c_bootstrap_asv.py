#!/usr/bin/env python3
"""
Exp-C: ASV δ* Bootstrap Confidence Interval

Bootstrap the magnitude ASV δ* from HumAID deepseek_zero-shot confusion matrix
counts to produce 95% percentile confidence intervals for 3 topologies.
"""
import json
import os
import sys
import time
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

ARTIFACTS = os.path.dirname(os.path.abspath(__file__))
B = 1000
SEED = 2026
TOPOLOGIES = ['confounding', 'exposure', 'iv']
K = 10
N_PRECOMP = 2_000_000
N_GRID = 1500
BIAS_THRESHOLD = 0.1

_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]


def softmax_rows(x):
    e = np.exp(x - x.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def make_p_A(K):
    raw = np.array([1.0 / (i + 1) for i in range(K)])
    return raw / raw.sum()


def make_dgp_params(K):
    p_A = make_p_A(K)
    iv_beta = np.array(_BETA_POOL[:K]) * 0.5
    iv_beta[0] = 0.0
    return {
        'confounding': {
            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K - 1]),
            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
            'beta_T': 2.0, 'sigma_T': 1.0,
        },
        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},
        'iv': {
            'lam': 1.0, 'beta': iv_beta, 'g': np.zeros(K),
            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
        },
    }


# ── DGP generators ──────────────────────────────────────────

def gen_confounding(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
    return T, Y, A


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


GEN_FNS = {'confounding': gen_confounding, 'exposure': gen_exposure, 'iv': gen_iv}


# ── Sufficient statistics & plim ─────────────────────────────

def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
    DA = np.zeros((N, K))
    for k in range(K):
        DA[:, k] = (A == k).astype(float)

    if topology == 'iv':
        Z = first_var
        z1 = Z == 1; z0 = Z == 0
        RF = Y[z1].mean() - Y[z0].mean()
        FS = np.zeros(K)
        for k in range(K):
            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
        return dict(RF=RF, FS=FS, topology='iv')
    elif topology == 'exposure':
        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
    else:
        T = first_var
        return dict(
            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T ** 2).mean(),
            E_Y=Y.mean(), E_TY=(T * Y).mean(),
            E_TD=(DA * T[:, None]).mean(0),
            E_YD=(DA * Y[:, None]).mean(0), topology=topology)


def compute_plim(C, st, K):
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
        q = C @ st['p_A']
        ct = C @ st['E_TD']
        cy = C @ st['E_YD']
        dim = K + 1
        EZZ = np.zeros((dim, dim))
        EZZ[0, 0] = 1.0
        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
        EZZ[1, 1] = st['E_T2']
        for j in range(1, K):
            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
            EZZ[j + 1, j + 1] = q[j]
        EZY = np.zeros(dim)
        EZY[0] = st['E_Y']
        EZY[1] = st['E_TY']
        for j in range(1, K):
            EZY[j + 1] = cy[j]
        try:
            return np.linalg.solve(EZZ, EZY)
        except np.linalg.LinAlgError:
            return np.full(dim, np.nan)


def extract_tau(plim_result, topology):
    if topology == 'iv':
        return float(plim_result) if np.isfinite(plim_result) else np.nan
    if isinstance(plim_result, np.ndarray):
        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
    return np.nan


# ── ASV δ* computation ───────────────────────────────────────

def C_interpolated(C0, delta, K):
    C_d = (1 - delta) * np.eye(K) + delta * C0
    C_d = np.maximum(C_d, 0.0)
    col_sums = C_d.sum(axis=0)
    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
    return C_d / col_sums


def compute_delta_max(C0):
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        return 10.0
    return min(1.0 / (1.0 - min_diag), 10.0)


def compute_magnitude_delta_star(C0, K, topology, st, tau_true):
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


# ── Bootstrap ────────────────────────────────────────────────

def counts_to_pairs(counts):
    """Reconstruct (gold, pred) pairs from confusion matrix counts.
    counts[i][j] = number of samples with gold=j, pred=i."""
    pairs = []
    K = len(counts)
    for i in range(K):
        for j in range(K):
            n = int(counts[i][j])
            for _ in range(n):
                pairs.append((j, i))
    return pairs


def pairs_to_C0(pairs, K):
    """Compute column-stochastic confusion matrix from (gold, pred) pairs."""
    counts = np.zeros((K, K))
    for gold, pred in pairs:
        counts[pred, gold] += 1
    col_sums = counts.sum(axis=0)
    col_sums = np.where(col_sums < 1, 1.0, col_sums)
    return counts / col_sums


def main():
    t0 = time.time()

    with open(os.path.join(ARTIFACTS, 'plan011_frontier_cms.json')) as f:
        all_cms = json.load(f)
    cm_data = all_cms['humaid/deepseek_zero-shot']
    counts = cm_data['confusion_matrix_counts']
    pairs = counts_to_pairs(counts)
    n_pairs = len(pairs)
    print(f"Reconstructed {n_pairs} pairs from confusion matrix counts")

    C0_point = pairs_to_C0(pairs, K)
    print(f"Point estimate C0 diagonal: {np.diag(C0_point).round(3)}")

    params = make_dgp_params(K)

    print("Precomputing sufficient statistics (N=2M)...")
    suff_stats = {}
    tau_trues = {}
    for topo in TOPOLOGIES:
        st = precompute_suff_stats(K, topo, params[topo])
        suff_stats[topo] = st
        plim_I = compute_plim(np.eye(K), st, K)
        tau_trues[topo] = extract_tau(plim_I, topo)
        print(f"  {topo}: tau_true = {tau_trues[topo]:.6f}")

    print(f"\nPoint estimate δ*:")
    point_estimates = {}
    for topo in TOPOLOGIES:
        ds = compute_magnitude_delta_star(C0_point, K, topo, suff_stats[topo],
                                          tau_trues[topo])
        point_estimates[topo] = ds
        print(f"  {topo}: δ* = {ds}")

    print(f"\nBootstrap B={B}...")
    rng = np.random.default_rng(SEED)
    bootstrap_samples = {topo: [] for topo in TOPOLOGIES}

    for b in range(B):
        idx = rng.integers(0, n_pairs, size=n_pairs)
        boot_pairs = [pairs[i] for i in idx]
        C0_b = pairs_to_C0(boot_pairs, K)

        for topo in TOPOLOGIES:
            ds = compute_magnitude_delta_star(C0_b, K, topo, suff_stats[topo],
                                              tau_trues[topo])
            bootstrap_samples[topo].append(ds)

        if (b + 1) % 100 == 0:
            elapsed = time.time() - t0
            eta = elapsed / (b + 1) * (B - b - 1)
            print(f"  [{b + 1}/{B}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")

    results = {
        'source_cm': 'humaid/deepseek_zero-shot',
        'n_bootstrap': B,
        'n_pairs': n_pairs,
        'bias_threshold': BIAS_THRESHOLD,
        'results': {},
    }

    print(f"\nResults:")
    for topo in TOPOLOGIES:
        samples = bootstrap_samples[topo]
        valid = [s for s in samples if s is not None]
        n_none = sum(1 for s in samples if s is None)

        if len(valid) > 0:
            arr = np.array(valid)
            ci_lo = float(np.percentile(arr, 2.5))
            ci_hi = float(np.percentile(arr, 97.5))
            median = float(np.median(arr))
            mean = float(np.mean(arr))
        else:
            ci_lo = ci_hi = median = mean = None

        results['results'][topo] = {
            'tau_true': tau_trues[topo],
            'delta_star_point': point_estimates[topo],
            'delta_star_ci_lower': ci_lo,
            'delta_star_ci_upper': ci_hi,
            'delta_star_median': median,
            'delta_star_mean': mean,
            'n_valid': len(valid),
            'n_none': n_none,
            'delta_star_bootstrap_samples': [float(s) if s is not None else None
                                             for s in samples],
        }

        print(f"  {topo}:")
        print(f"    tau_true = {tau_trues[topo]:.6f}")
        print(f"    δ* point = {point_estimates[topo]}")
        if ci_lo is not None:
            print(f"    δ* 95% CI = [{ci_lo:.4f}, {ci_hi:.4f}]")
            print(f"    δ* median = {median:.4f}, mean = {mean:.4f}")
        else:
            print(f"    δ* = None (threshold never reached in any bootstrap)")
        print(f"    valid/none = {len(valid)}/{n_none}")

    json_path = os.path.join(ARTIFACTS, 'exp_c_bootstrap_results.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON -> {json_path}")

    make_figure(results, bootstrap_samples)

    total = time.time() - t0
    print(f"\nDone in {total:.0f}s ({total / 60:.1f}min)")


def make_figure(results, bootstrap_samples):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available, skipping figure")
        return

    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
    topo_labels = {'confounding': 'Confounding', 'exposure': 'Exposure', 'iv': 'IV'}
    colors = {'confounding': '#2171b5', 'exposure': '#d94801', 'iv': '#238b45'}

    for ax, topo in zip(axes, TOPOLOGIES):
        r = results['results'][topo]
        valid = [s for s in bootstrap_samples[topo] if s is not None]

        if len(valid) == 0:
            ax.text(0.5, 0.5, '$\\delta^*$ undefined\n(threshold never reached)',
                    ha='center', va='center', transform=ax.transAxes,
                    fontsize=9, style='italic', color='gray')
            ax.set_title(topo_labels[topo], fontsize=11, fontweight='bold')
            ax.set_xlabel('$\\delta^*$', fontsize=10)
            ax.tick_params(labelsize=8)
            continue

        arr = np.array(valid)
        ax.hist(arr, bins=40, color=colors[topo], alpha=0.7, edgecolor='white',
                linewidth=0.5, density=True)

        point = r['delta_star_point']
        ci_lo = r['delta_star_ci_lower']
        ci_hi = r['delta_star_ci_upper']

        ax.axvline(point, color='k', linewidth=1.5, linestyle='-',
                   label=f'$\\delta^*$ = {point:.3f}')
        ax.axvline(ci_lo, color='k', linewidth=1, linestyle='--', alpha=0.7)
        ax.axvline(ci_hi, color='k', linewidth=1, linestyle='--', alpha=0.7)
        ax.axvspan(ci_lo, ci_hi, alpha=0.1, color='gray')

        ax.set_title(topo_labels[topo], fontsize=11, fontweight='bold')
        ax.set_xlabel('$\\delta^*$', fontsize=10)
        if topo == TOPOLOGIES[0]:
            ax.set_ylabel('Density', fontsize=10)

        ax.annotate(f'95% CI: [{ci_lo:.3f}, {ci_hi:.3f}]',
                    xy=(0.5, 0.95), xycoords='axes fraction',
                    ha='center', va='top', fontsize=7.5,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                              edgecolor='gray', alpha=0.8))
        ax.tick_params(labelsize=8)

    fig.suptitle('Bootstrap Distribution of ASV $\\delta^*$ (B=1000)',
                 fontsize=12, y=1.02)
    fig.tight_layout()

    pdf_path = os.path.join(ARTIFACTS, 'exp_c_bootstrap_figure.pdf')
    fig.savefig(pdf_path, bbox_inches='tight', dpi=150)
    plt.close(fig)
    print(f"Figure -> {pdf_path}")


if __name__ == '__main__':
    main()
