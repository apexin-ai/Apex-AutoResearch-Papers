#!/usr/bin/env python3
"""
Empirical Correction Validation — HumAID K=10

Loads 8 valid HumAID confusion matrices from asv_empirical_results.json,
generates synthetic MC data using plan_006's K=10 DGP for each of 7 topologies,
runs all 5 correction methods (PPI++, naive plug-in, DSL, MC-SIMEX, MLA),
and reports empirical bias reduction per topology × method.

Input:  artifacts/plan006/asv_empirical_results.json
Output: artifacts/ppi_empirical_validation.json

Dependencies: numpy, annot_sensitivity (local package)
"""

import sys
import os
import json
import time
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from annot_sensitivity.correction import (
    correct_ppi, correct_naive_plugin, correct_dsl, correct_mcsimex, correct_mla
)
from annot_sensitivity.utils import misclassify, make_dummies, ols, ols_with_se

# ── Plan 006 DGP Infrastructure (K-general) ────────────────────────

_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]


def softmax_rows(logits):
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def make_p_A(K):
    if K == 2:
        return np.array([0.55, 0.45])
    elif K == 3:
        return np.array([0.40, 0.35, 0.25])
    else:
        raw = np.array([1.0 / (i + 1) for i in range(K)])
        return raw / raw.sum()


def make_dgp_params(K):
    p_A = make_p_A(K)
    params = {
        'confounding': {
            'p_A': p_A,
            'alpha': np.array(_ALPHA_POOL[:K - 1]),
            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
            'beta_T': 2.0,
            'sigma_T': 1.0,
        },
        'mediation': {
            'tau': 0.5,
            'gamma': np.array(_GAMMA_POOL[:K]),
            'delta': np.array(_DELTA_POOL[:K]),
            'beta': np.array(_BETA_POOL[:K]),
        },
        'collider': {
            'tau': 1.0,
            'g': np.zeros(K),
            'dT': np.array(_DT_POOL[:K]),
            'dY': np.array(_DY_POOL[:K]),
        },
        'exposure': {
            'beta': np.array(_BETA_POOL[:K]),
            'p_A': p_A,
        },
    }
    if K == 3:
        params['mbias'] = {
            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
            'g': np.zeros(3),
            'a_U1': np.array([0.0, 0.8, -0.5]),
            'a_U2': np.array([0.0, 0.6, 0.9]),
        }
        params['iv'] = {
            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
            'g': np.zeros(3),
            'dZ': np.array([0.0, 1.0, -0.5]),
            'dU': np.array([0.0, 0.8, 0.6]),
        }
        params['frontdoor'] = {
            'alpha_U': 1.0, 'lambda_U': 1.0,
            'gamma': np.array([0.0, 0.5, -0.3]),
            'delta_fd': np.array([0.0, 1.0, -0.8]),
            'beta': np.array([0.0, 1.0, -0.5]),
        }
    else:
        params['mbias'] = {
            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
            'g': np.zeros(K),
            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),
            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),
        }
        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
        iv_beta[0] = 0.0
        params['iv'] = {
            'lam': 1.0, 'beta': iv_beta,
            'g': np.zeros(K),
            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
        }
        fd_delta = np.array(_DELTA_POOL[:K])
        fd_delta[0] = 0.0
        params['frontdoor'] = {
            'alpha_U': 1.0, 'lambda_U': 1.0,
            'gamma': np.array(_GAMMA_POOL[:K]),
            'delta_fd': fd_delta,
            'beta': np.array(_BETA_POOL[:K]),
        }
    return params


# ── DGP Generators ──────────────────────────────────────────────────

def gen_confounding(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
    return T, Y, A


def gen_mediation(K, N, p, rng):
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
    probs = softmax_rows(logits)
    A = sample_cat(probs, rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
    return T, Y, A


def gen_collider(K, N, p, rng):
    T = rng.normal(0, 1, N)
    Y = p['tau'] * T + rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
              + p['dY'][None, :] * Y[:, None])
    probs = softmax_rows(logits)
    A = sample_cat(probs, rng)
    return T, Y, A


def gen_exposure(K, N, p, rng):
    A = rng.choice(K, size=N, p=p['p_A'])
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
    return None, Y, A


def gen_mbias(K, N, p, rng):
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]
              + p['a_U2'][None, :] * U2[:, None])
    probs = softmax_rows(logits)
    A = sample_cat(probs, rng)
    return T, Y, A


def gen_iv(K, N, p, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
              + p['dU'][None, :] * U[:, None])
    probs = softmax_rows(logits)
    A = sample_cat(probs, rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
    return Z, Y, A


def gen_frontdoor(K, N, p, rng):
    U = rng.normal(0, 1, N)
    T = p['alpha_U'] * U + rng.normal(0, 1, N)
    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]
    probs = softmax_rows(logits)
    M = sample_cat(probs, rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (M == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)
    return T, Y, M


GEN_FNS = {
    'confounding': gen_confounding, 'mediation': gen_mediation,
    'collider': gen_collider, 'exposure': gen_exposure,
    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
}

HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}


# ── Wald Estimator ──────────────────────────────────────────────────

def wald_est(Z, Y, A_or_Astar, k=1):
    z1 = Z == 1; z0 = Z == 0
    n1, n0 = float(z1.sum()), float(z0.sum())
    if n1 < 2 or n0 < 2:
        return np.nan
    RF = Y[z1].mean() - Y[z0].mean()
    FS = (A_or_Astar[z1] == k).astype(float).mean() - \
         (A_or_Astar[z0] == k).astype(float).mean()
    if abs(FS) < 1e-8:
        return np.nan
    return RF / FS


def ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=None, n_boot=50):
    """PPI++ for Wald estimator (IV topology)."""
    if rng is None:
        rng = np.random.default_rng()
    gold_idx = np.where(gold_mask)[0]
    n_gold = len(gold_idx)

    tau_all_star = wald_est(Z, Y, Astar, k)
    tau_gold_true = wald_est(Z[gold_mask], Y[gold_mask], A[gold_mask], k)
    tau_gold_star = wald_est(Z[gold_mask], Y[gold_mask], Astar[gold_mask], k)

    if np.isnan(tau_gold_true) or np.isnan(tau_all_star):
        return np.nan, False

    tau_true_boot = np.zeros(n_boot)
    tau_rect_boot = np.zeros(n_boot)
    for b in range(n_boot):
        idx = rng.choice(gold_idx, size=n_gold, replace=True)
        bt = wald_est(Z[idx], Y[idx], A[idx], k)
        bs = wald_est(Z[idx], Y[idx], Astar[idx], k)
        tau_true_boot[b] = bt
        tau_rect_boot[b] = bs - bt

    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
    if valid.sum() > 5:
        var_r = np.var(tau_rect_boot[valid])
        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
    else:
        lam = 1.0

    tau_ppi = tau_gold_true + lam * (tau_all_star - tau_gold_star)
    return float(tau_ppi), True


# ── True Parameter Computation ──────────────────────────────────────

def compute_tau_true(K, topology, params, N_large=500_000, seed=99):
    """Compute true tau by running estimator on very large uncontaminated sample."""
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, N_large, params[topology], rng)

    if topology == 'iv':
        return wald_est(first_var, Y, A, k=1)
    elif topology == 'exposure':
        D = make_dummies(A, K)
        X = np.column_stack([np.ones(N_large), D])
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return float(beta[1])
    else:
        T = first_var
        D = make_dummies(A, K)
        X = np.column_stack([np.ones(N_large), T, D])
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return float(beta[1])


# ── MC-SIMEX for IV (custom) ────────────────────────────────────────

def mcsimex_wald(Z, Y, Astar, C, k=1, rng=None, n_B=50,
                 lambdas_extra=(0.5, 1.0, 1.5, 2.0)):
    """MC-SIMEX for IV Wald estimator."""
    if rng is None:
        rng = np.random.default_rng()
    K = C.shape[0]
    try:
        eigvals, eigvecs = np.linalg.eig(C)
        eigvecs_inv = np.linalg.inv(eigvecs)
    except np.linalg.LinAlgError:
        return np.nan, False

    lambdas = np.array([0.0] + list(lambdas_extra))
    tau_lam = np.zeros(len(lambdas))

    for li, lam_val in enumerate(lambdas):
        if lam_val == 0.0:
            tau_lam[li] = wald_est(Z, Y, Astar, k)
        else:
            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)
            C_lam = np.clip(C_lam_raw, 0, None)
            cs = C_lam.sum(axis=0)
            cs[cs == 0] = 1.0
            C_lam /= cs

            tau_b = np.zeros(n_B)
            for b in range(n_B):
                A_extra = misclassify(Astar, C_lam, rng)
                tau_b[b] = wald_est(Z, Y, A_extra, k)
            ok = np.isfinite(tau_b)
            if ok.sum() < n_B // 2:
                return np.nan, False
            tau_lam[li] = tau_b[ok].mean()

    try:
        coeffs = np.polyfit(lambdas, tau_lam, 2)
        return float(np.polyval(coeffs, -1.0)), True
    except Exception:
        return np.nan, False


# ── Main ────────────────────────────────────────────────────────────

N_SAMPLES = 10_000
N_REPS = 30
GOLD_FRACTION = 0.10
SEED = 42
TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']
METHODS = ['ppi', 'naive_plugin', 'dsl', 'mcsimex', 'mla']

JSON_PATH = os.path.join(PROJECT_ROOT, 'artifacts', 'plan006',
                         'asv_empirical_results.json')


def load_valid_humaid_configs():
    with open(JSON_PATH) as f:
        data = json.load(f)

    zero_configs = {(e['model'], e['prompt'])
                    for e in data['f1_vs_bias'] if e['macro_f1'] == 0}

    cms = {}
    for key, mat in data['confusion_matrices'].items():
        parts = key.split('_')
        if parts[0] != 'humaid':
            continue
        model = parts[1]
        prompt = '_'.join(parts[2:])
        if (model, prompt) in zero_configs:
            continue
        cms[key] = np.array(mat)
    return cms


def run_single_rep(K, topology, params, C, tau_true, rng, gold_frac):
    """Run one MC replication: generate data, misclassify, run corrections."""
    first_var, Y, A = GEN_FNS[topology](K, N_SAMPLES, params[topology], rng)
    Astar = misclassify(A, C, rng)

    N = len(Y)
    n_gold = max(int(N * gold_frac), 50)
    gold_idx = rng.choice(N, size=n_gold, replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True

    results = {}

    if topology == 'iv':
        Z = first_var
        tau_naive = wald_est(Z, Y, Astar, k=1)
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        tau_ppi, ok = ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=rng)
        results['ppi'] = float(tau_ppi) if ok and np.isfinite(tau_ppi) else None

        tau_sim, ok = mcsimex_wald(Z, Y, Astar, C, k=1, rng=rng)
        results['mcsimex'] = float(tau_sim) if ok and np.isfinite(tau_sim) else None

        results['naive_plugin'] = None
        results['dsl'] = None
        results['mla'] = None

    elif topology == 'exposure':
        X_other = np.ones((N, 1))
        D_star = make_dummies(Astar, K)
        X_full = np.column_stack([X_other, D_star])
        try:
            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            tau_naive = float(beta_naive[1])
        except Exception:
            tau_naive = np.nan
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        for method in METHODS:
            if method == 'ppi':
                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                          tau_idx=1, rng=rng)
            elif method == 'naive_plugin':
                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)
            elif method == 'dsl':
                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)
            elif method == 'mcsimex':
                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)
            elif method == 'mla':
                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)
            else:
                continue
            results[method] = float(tau) if ok and np.isfinite(tau) else None

    else:
        T = first_var
        X_other = np.column_stack([np.ones(N), T])
        D_star = make_dummies(Astar, K)
        X_full = np.column_stack([X_other, D_star])
        try:
            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            tau_naive = float(beta_naive[1])
        except Exception:
            tau_naive = np.nan
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        for method in METHODS:
            if method == 'ppi':
                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                          tau_idx=1, rng=rng)
            elif method == 'naive_plugin':
                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)
            elif method == 'dsl':
                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)
            elif method == 'mcsimex':
                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)
            elif method == 'mla':
                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)
            else:
                continue
            results[method] = float(tau) if ok and np.isfinite(tau) else None

    results['tau_true'] = tau_true
    return results


def main():
    t_start = time.time()
    K = 10
    print("=" * 70)
    print("Empirical Correction Validation — HumAID K=10")
    print("=" * 70)
    print(f"N={N_SAMPLES}, N_REPS={N_REPS}, gold_fraction={GOLD_FRACTION}")

    configs = load_valid_humaid_configs()
    print(f"Loaded {len(configs)} valid HumAID confusion matrices")

    params = make_dgp_params(K)
    rng_master = np.random.default_rng(SEED)

    print("\nComputing tau_true for each topology (N=500k)...")
    tau_true = {}
    for topo in TOPOLOGIES:
        tau_true[topo] = compute_tau_true(K, topo, params)
        print(f"  {topo}: tau_true = {tau_true[topo]:.6f}")

    all_results = {}
    per_topo_method = {topo: {m: [] for m in METHODS}
                       for topo in TOPOLOGIES}

    for ci, (config_name, C) in enumerate(configs.items()):
        print(f"\n[{ci+1}/{len(configs)}] {config_name}")
        config_results = {}

        for topo in TOPOLOGIES:
            topo_reps = []
            for rep in range(N_REPS):
                seed_rep = rng_master.integers(0, 2**31)
                rng_rep = np.random.default_rng(seed_rep)
                res = run_single_rep(K, topo, params, C, tau_true[topo],
                                     rng_rep, GOLD_FRACTION)
                topo_reps.append(res)

            naive_biases = []
            method_biases = {m: [] for m in METHODS}
            for res in topo_reps:
                tt = res['tau_true']
                if res['naive'] is not None:
                    naive_biases.append(res['naive'] - tt)
                for m in METHODS:
                    if res.get(m) is not None:
                        method_biases[m].append(res[m] - tt)

            avg_naive_bias = np.mean(np.abs(naive_biases)) if naive_biases else None
            topo_summary = {
                'tau_true': tau_true[topo],
                'n_reps': N_REPS,
                'naive_mean_abs_bias': float(avg_naive_bias) if avg_naive_bias else None,
                'methods': {},
            }

            for m in METHODS:
                biases = method_biases[m]
                if biases:
                    avg_abs = float(np.mean(np.abs(biases)))
                    mean_bias = float(np.mean(biases))
                    if avg_naive_bias and avg_naive_bias > 1e-8:
                        reduction = 1.0 - avg_abs / avg_naive_bias
                    else:
                        reduction = None
                    topo_summary['methods'][m] = {
                        'mean_abs_bias': avg_abs,
                        'mean_bias': mean_bias,
                        'bias_reduction': float(reduction) if reduction is not None else None,
                        'n_valid': len(biases),
                    }
                    per_topo_method[topo][m].append(
                        float(reduction) if reduction is not None else None
                    )
                else:
                    topo_summary['methods'][m] = {
                        'mean_abs_bias': None,
                        'mean_bias': None,
                        'bias_reduction': None,
                        'n_valid': 0,
                    }

            config_results[topo] = topo_summary
            ppi_info = topo_summary['methods'].get('ppi', {})
            ppi_red = ppi_info.get('bias_reduction')
            ppi_str = f"{100*ppi_red:.1f}%" if ppi_red is not None else "N/A"
            print(f"  {topo:12s}: naive_bias={avg_naive_bias:.4f}" if avg_naive_bias else
                  f"  {topo:12s}: naive_bias=N/A", end="")
            print(f"  PPI++={ppi_str}")

        all_results[config_name] = config_results

    grand_summary = {}
    print("\n" + "=" * 70)
    print("GRAND SUMMARY: Mean bias reduction across 8 configs")
    print("=" * 70)
    print(f"\n{'Topology':14s}", end="")
    for m in METHODS:
        print(f"  {m:14s}", end="")
    print()
    print("-" * (14 + 16 * len(METHODS)))

    for topo in TOPOLOGIES:
        grand_summary[topo] = {}
        print(f"{topo:14s}", end="")
        for m in METHODS:
            vals = [v for v in per_topo_method[topo][m] if v is not None]
            if vals:
                mean_red = float(np.mean(vals))
                grand_summary[topo][m] = {
                    'mean_reduction': mean_red,
                    'std_reduction': float(np.std(vals)),
                    'n_configs': len(vals),
                }
                print(f"  {100*mean_red:+12.1f}%", end="")
            else:
                grand_summary[topo][m] = None
                print(f"  {'N/A':>13s}", end="")
        print()

    overall_ppi = []
    for topo in TOPOLOGIES:
        gs = grand_summary[topo].get('ppi')
        if gs:
            overall_ppi.append(gs['mean_reduction'])
    if overall_ppi:
        print(f"\nGrand mean PPI++ bias reduction: {100*np.mean(overall_ppi):.1f}%")

    output = {
        'meta': {
            'scope': 'HumAID K=10, 8 valid configs',
            'n_samples': N_SAMPLES,
            'n_reps': N_REPS,
            'gold_fraction': GOLD_FRACTION,
            'seed': SEED,
            'topologies': TOPOLOGIES,
            'methods': METHODS,
            'n_configs': len(configs),
            'configs': list(configs.keys()),
        },
        'tau_true': {t: float(tau_true[t]) for t in TOPOLOGIES},
        'per_config': all_results,
        'grand_summary': grand_summary,
    }

    out_path = os.path.join(PROJECT_ROOT, 'artifacts',
                            'ppi_empirical_validation.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\nResults saved to: {out_path}")
    print(f"Total runtime: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
