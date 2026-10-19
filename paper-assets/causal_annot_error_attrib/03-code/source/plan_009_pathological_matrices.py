#!/usr/bin/env python3
"""
Plan 009: Pathological Confusion Matrix Analysis

Studies extreme bias behavior under 3 classes of pathological K*K
column-stochastic confusion matrices across 7 DAG topologies and K in {3,5,7}.

Pathological C types (M=1000 instances each per (K, type, param)):
  (a) Near-permutation: C = (1-eps)P + eps*U, eps in {0.01, 0.05, 0.1, 0.2}
  (b) Rank-deficient: SVD truncation to rank r in {1, ..., K-1}
  (c) Block-diagonal: b blocks, b in {2, max(K//2, 2)}

Matrix features extracted per C:
  spectral_gap, diag_dominance, effective_rank, condition_number, off_diagonal_max

Analysis:
  - Per-(topo, K, C_type, param): bias distribution statistics
  - OLS regression: |bias| ~ features (per-topology + global)
  - Catastrophic bias detection: |bias| > 2*|tau_true|

Input:
  DGP parameters from plan_002 (7 topologies), N_LARGE=5M samples for plim
Output -> artifacts/plan009/:
  pathological_bias_summary.json, regression_results.txt

Dependencies: torch (CUDA), numpy, scipy.stats
"""

import torch
import numpy as np
import json
import time
import os
import sys
import hashlib
import argparse

# ================================================================
# Configuration
# ================================================================
K_VALUES = [3, 5, 7]
M_DEFAULT = 1000
N_LARGE = 5_000_000
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
DTYPE = torch.float64

ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'iv', 'frontdoor']
NEAR_PERM_EPSILONS = [0.01, 0.05, 0.1, 0.2]
FEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank',
                 'condition_number', 'off_diagonal_max']

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(SCRIPT_DIR, 'artifacts', 'plan009')


def _det_seed(topo_name, K, c_type, base_seed=42):
    h = hashlib.sha256(
        f"{topo_name}_{K}_{c_type}_{base_seed}".encode()
    ).hexdigest()
    return int(h[:8], 16) % (2**31)


# ================================================================
# DGP parameter pools (from plan_002_k57_extended_7topo.py)
# ================================================================
_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
_MBIAS_A1    = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
_MBIAS_A2    = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
_IV_DZ       = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
_IV_DU       = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
_FD_GAMMA    = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_FD_DELTA    = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]


def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()


def make_all_params(K):
    p_A = make_p_A(K)
    return dict(
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),
                         beta_A=np.array(_BETA_A_POOL[:K-1]),
                         beta_T=2.0, sigma_T=1.0),
        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),
                       delta=np.array(_DELTA_POOL[:K]),
                       beta=np.array(_BETA_POOL[:K])),
        collider=dict(tau=1.0, g=np.zeros(K),
                      dT=np.array(_DT_POOL[:K]),
                      dY=np.array(_DY_POOL[:K])),
        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),
        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
                   a1=np.array(_MBIAS_A1[:K]),
                   a2=np.array(_MBIAS_A2[:K])),
        iv=dict(lam=1.0, g=np.zeros(K),
                dZ=np.array(_IV_DZ[:K]),
                dU=np.array(_IV_DU[:K]),
                beta=np.array(_BETA_POOL[:K])),
        frontdoor=dict(alpha_U=1.0, lam_U=1.0,
                       gamma=np.array(_FD_GAMMA[:K]),
                       delta=np.array(_FD_DELTA[:K]),
                       beta=np.array(_BETA_POOL[:K])),
    )


# ================================================================
# DGP generators (from plan_002_k57_extended_7topo.py)
# ================================================================
def _softmax_rows(logits):
    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
    return e / e.sum(axis=-1, keepdims=True)


def _sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum).sum(axis=1).astype(int)


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
    A = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1)
    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
    return T, Y, A


def gen_collider(K, N, p, rng):
    T = rng.normal(0, 1, N)
    Y = p['tau'] * T + rng.normal(0, 1, N)
    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
              + p['dY'][None, :] * Y[:, None])
    A = _sample_cat(_softmax_rows(logits), rng)
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
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['g'][j] + p['a1'][j] * U1 + p['a2'][j] * U2
    A = _sample_cat(_softmax_rows(logits), rng)
    return T, Y, A


def gen_iv(K, N, p, rng):
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    eps = rng.normal(0, 1, N)
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['g'][j] + p['dZ'][j] * Z + p['dU'][j] * U
    A = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam'] * U + eps
    return Z, Y, A


def gen_frontdoor(K, N, p, rng):
    U = rng.normal(0, 1, N)
    T = p['alpha_U'] * U + rng.normal(0, 1, N)
    logits = np.zeros((N, K))
    for j in range(1, K):
        logits[:, j] = p['gamma'][j] + p['delta'][j] * T
    M = _sample_cat(_softmax_rows(logits), rng)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (M == j + 1).astype(float)
    Y = D @ p['beta'][1:] + p['lam_U'] * U + rng.normal(0, 1, N)
    return T, Y, M


_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
            collider=gen_collider, exposure=gen_exposure,
            mbias=gen_mbias, iv=gen_iv, frontdoor=gen_frontdoor)


# ================================================================
# Sufficient statistics
# ================================================================
class SuffStats:
    def __init__(self, T, Y, A, K):
        self.K = K
        self.has_T = T is not None
        N = len(Y)
        DA = np.zeros((N, K))
        for k in range(K):
            DA[:, k] = (A == k).astype(float)
        self.p_A = DA.mean(0)
        self.E_Y = Y.mean()
        self.E_YD = (DA * Y[:, None]).mean(0)
        if self.has_T:
            self.E_T = T.mean()
            self.E_T2 = (T ** 2).mean()
            self.E_TY = (T * Y).mean()
            self.E_TD = (DA * T[:, None]).mean(0)

    def to_device(self, dev):
        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)
        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)
        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)
        if self.has_T:
            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)
            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)
            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)
            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)
        return self


class IVSuffStats:
    def __init__(self, Z, Y, A, K):
        self.K = K
        z1 = Z == 1
        z0 = Z == 0
        self.RF = Y[z1].mean() - Y[z0].mean()
        self.FS = np.zeros(K)
        for k in range(K):
            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()

    def to_device(self, dev):
        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)
        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)
        return self


# ================================================================
# Plim functions (batched GPU)
# ================================================================
def plim_with_T(ss, C):
    B, K = C.shape[0], ss.K
    dim = K + 1
    q = C @ ss.t_p_A
    ct = C @ ss.t_E_TD
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = ss.t_E_T
    EZZ[:, 1, 0] = ss.t_E_T
    EZZ[:, 1, 1] = ss.t_E_T2
    EZZ[:, 0, 2:] = q[:, 1:]
    EZZ[:, 2:, 0] = q[:, 1:]
    EZZ[:, 1, 2:] = ct[:, 1:]
    EZZ[:, 2:, 1] = ct[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y
    EZY[:, 1] = ss.t_E_TY
    EZY[:, 2:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_exposure(ss, C):
    B, K = C.shape[0], ss.K
    dim = K
    q = C @ ss.t_p_A
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1:] = q[:, 1:]
    EZZ[:, 1:, 0] = q[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y
    EZY[:, 1:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_iv_batched(ss, C):
    FS_star = C @ ss.t_FS
    denom = FS_star[:, 1]
    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)
    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)
    return result.unsqueeze(1)


# ================================================================
# Pathological C matrix generators
# ================================================================
def gen_near_permutation(K, M, epsilon, rng):
    """C = (1-eps)*P + eps*U where P=random permutation, U=random col-stochastic."""
    Cs = np.zeros((M, K, K))
    for i in range(M):
        perm = rng.permutation(K)
        P = np.zeros((K, K))
        P[perm, np.arange(K)] = 1.0
        U = rng.dirichlet(np.ones(K), size=K).T
        C = (1 - epsilon) * P + epsilon * U
        C = np.clip(C, 1e-12, None)
        C /= C.sum(axis=0, keepdims=True)
        Cs[i] = C
    return Cs


def gen_rank_deficient(K, M, rank, rng):
    """Rank-r col-stochastic via SVD truncation + non-negative projection."""
    Cs = np.zeros((M, K, K))
    for i in range(M):
        C_full = rng.dirichlet(np.ones(K) * 2.0, size=K).T
        U, S, Vt = np.linalg.svd(C_full, full_matrices=True)
        S_trunc = np.zeros_like(S)
        S_trunc[:rank] = S[:rank]
        C_approx = U @ np.diag(S_trunc) @ Vt
        C_approx = np.clip(C_approx, 1e-12, None)
        C_approx /= C_approx.sum(axis=0, keepdims=True)
        Cs[i] = C_approx
    return Cs


def gen_block_diagonal(K, M, n_blocks, rng):
    """Block-diagonal: high intra-block accuracy, low inter-block leakage."""
    block_sizes = []
    base = K // n_blocks
    remainder = K % n_blocks
    for b in range(n_blocks):
        block_sizes.append(base + (1 if b < remainder else 0))

    Cs = np.zeros((M, K, K))
    for i in range(M):
        C = np.zeros((K, K))
        leak = rng.uniform(0.001, 0.05)
        start = 0
        for bs in block_sizes:
            end = start + bs
            for col in range(start, end):
                within = rng.dirichlet(5.0 * np.ones(bs))
                n_outside = K - bs
                if n_outside > 0:
                    between = rng.dirichlet(np.ones(n_outside)) * leak
                else:
                    between = np.array([])
                C[start:end, col] = within * (1 - leak)
                idx = 0
                for row in range(K):
                    if row < start or row >= end:
                        C[row, col] = between[idx]
                        idx += 1
            start = end
        C = np.clip(C, 1e-12, None)
        C /= C.sum(axis=0, keepdims=True)
        Cs[i] = C
    return Cs


# ================================================================
# Matrix feature extraction
# ================================================================
def extract_features(C_batch):
    M, K, _ = C_batch.shape
    feats = {fn: np.zeros(M) for fn in FEATURE_NAMES}

    diags = np.diagonal(C_batch, axis1=1, axis2=2)
    feats['diag_dominance'] = diags.min(axis=1) * K

    svd_vals = np.linalg.svd(C_batch, compute_uv=False)
    sv_sum = svd_vals.sum(axis=1)
    sv_sq_sum = (svd_vals ** 2).sum(axis=1)
    feats['effective_rank'] = np.where(
        sv_sum > 0, sv_sum**2 / sv_sq_sum, 0.0)
    feats['condition_number'] = (
        svd_vals[:, 0] / np.maximum(svd_vals[:, -1], 1e-15))

    eye_mask = ~np.eye(K, dtype=bool)
    for i in range(M):
        eigvals = np.linalg.eigvals(C_batch[i])
        eig_abs = np.sort(np.abs(eigvals))[::-1]
        feats['spectral_gap'][i] = (
            eig_abs[0] - eig_abs[1] if K > 1 else eig_abs[0])
        feats['off_diagonal_max'][i] = C_batch[i][eye_mask].max()

    return feats


# ================================================================
# OLS regression
# ================================================================
def ols_regression(y, X_raw):
    n = len(y)
    p = X_raw.shape[1]
    if n < p + 5:
        return None

    X_mean = X_raw.mean(axis=0)
    X_std = X_raw.std(axis=0)
    X_std[X_std < 1e-15] = 1.0
    Xs = (X_raw - X_mean) / X_std
    X = np.column_stack([np.ones(n), Xs])

    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    y_hat = X @ beta
    ss_res = ((y - y_hat) ** 2).sum()
    ss_tot = ((y - y.mean()) ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0

    dof = n - X.shape[1]
    if dof <= 0:
        pv = np.full(p, np.nan)
    else:
        mse = ss_res / dof
        try:
            cov_mat = mse * np.linalg.inv(X.T @ X)
            se = np.sqrt(np.maximum(np.diag(cov_mat), 0))
            t_stat = np.where(se > 1e-15, beta / se, 0.0)
            from scipy.stats import t as t_dist
            pv = 2 * (1 - t_dist.cdf(np.abs(t_stat[1:]), dof))
        except np.linalg.LinAlgError:
            pv = np.full(p, np.nan)

    return dict(
        r_squared=float(r2),
        coefs={fn: float(beta[i + 1]) for i, fn in enumerate(FEATURE_NAMES)},
        p_values={fn: float(pv[i]) for i, fn in enumerate(FEATURE_NAMES)},
        n_obs=n,
    )


# ================================================================
# Main
# ================================================================
def main():
    parser = argparse.ArgumentParser(
        description='Plan 009: Pathological confusion matrix bias analysis '
                    'across 7 DAG topologies')
    parser.add_argument('--M', type=int, default=M_DEFAULT,
                        help=f'C instances per config [default: {M_DEFAULT}]')
    parser.add_argument('--N', type=int, default=N_LARGE,
                        help=f'DGP sample size [default: {N_LARGE}]')
    parser.add_argument('--K', type=int, nargs='+', default=K_VALUES,
                        help=f'K values [default: {K_VALUES}]')
    parser.add_argument('--topos', type=str, nargs='+', default=ALL_TOPOS,
                        help='Topologies')
    parser.add_argument('--dry-run', action='store_true',
                        help='Quick test: M=10, K=[3], 1 topo, N=100k')
    args = parser.parse_args()

    if args.dry_run:
        args.M = 10
        args.K = [3]
        args.topos = ['confounding']
        args.N = 100_000
        print("=== DRY RUN ===\n")

    os.makedirs(OUT_DIR, exist_ok=True)
    t0 = time.time()
    print(f"Plan 009: Pathological Matrices")
    print(f"  Device={DEVICE}  M={args.M}  N={args.N:,}")
    print(f"  K={args.K}  topos={args.topos}")
    print(f"  Output -> {OUT_DIR}\n")

    all_results = {}
    topo_bias = {t: [] for t in ALL_TOPOS}
    topo_feats = {t: {fn: [] for fn in FEATURE_NAMES} for t in ALL_TOPOS}

    for K in args.K:
        params = make_all_params(K)
        rank_vals = list(range(1, K))
        block_vals = sorted(set([2, max(K // 2, 2)]))

        c_configs = {
            'near_permutation': [(f'eps={e}', e) for e in NEAR_PERM_EPSILONS],
            'rank_deficient': [(f'rank={r}', r) for r in rank_vals],
            'block_diagonal': [(f'blocks={b}', b) for b in block_vals],
        }

        for topo in args.topos:
            tk = time.time()
            print(f"{'='*70}")
            print(f"  {topo}  K={K}")
            print(f"{'='*70}")

            seed_dgp = _det_seed(topo, K, 'dgp')
            rng = np.random.default_rng(seed_dgp)
            T_or_Z, Y, A = _GEN[topo](K, args.N, params[topo], rng)

            if topo == 'iv':
                ss = IVSuffStats(T_or_Z, Y, A, K).to_device(DEVICE)
                plim_fn = plim_iv_batched
                tau_idx = 0
            elif topo == 'exposure':
                ss = SuffStats(None, Y, A, K).to_device(DEVICE)
                plim_fn = plim_exposure
                tau_idx = 1
            else:
                ss = SuffStats(T_or_Z, Y, A, K).to_device(DEVICE)
                plim_fn = plim_with_T
                tau_idx = 1

            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
            plim_true = plim_fn(ss, I_batch).squeeze(0)
            tau_true = plim_true[tau_idx].item()
            print(f"  tau_true(C=I) = {tau_true:.6f}  "
                  f"[DGP {time.time()-tk:.1f}s]")

            for c_type, param_list in c_configs.items():
                for param_label, param_val in param_list:
                    seed = _det_seed(topo, K,
                                     f'{c_type}_{param_label}')
                    rng_c = np.random.default_rng(seed)

                    if c_type == 'near_permutation':
                        Cb = gen_near_permutation(
                            K, args.M, param_val, rng_c)
                    elif c_type == 'rank_deficient':
                        Cb = gen_rank_deficient(
                            K, args.M, param_val, rng_c)
                    else:
                        Cb = gen_block_diagonal(
                            K, args.M, param_val, rng_c)

                    Ct = torch.tensor(Cb, dtype=DTYPE, device=DEVICE)
                    plim_batch = plim_fn(ss, Ct)
                    bias = (plim_batch[:, tau_idx]
                            - tau_true).cpu().numpy()

                    valid = np.isfinite(bias)
                    bias = bias[valid]
                    Cb_valid = Cb[valid]

                    key = f"{topo}_K{K}_{c_type}_{param_label}"
                    if len(bias) == 0:
                        all_results[key] = dict(error='all_nan')
                        print(f"    {c_type:20s} {param_label:10s}:"
                              f" ALL NaN")
                        continue

                    ab = np.abs(bias)
                    feats = extract_features(Cb_valid)

                    cat_thr = 2 * abs(tau_true)
                    if abs(tau_true) > 1e-10:
                        cat_frac = float((ab > cat_thr).mean())
                    else:
                        cat_frac = float('nan')

                    stats = dict(
                        n_valid=int(len(bias)),
                        bias_mean=float(bias.mean()),
                        bias_std=float(bias.std()),
                        abs_bias_mean=float(ab.mean()),
                        abs_bias_max=float(ab.max()),
                        abs_bias_min=float(ab.min()),
                        abs_bias_p5=float(np.percentile(ab, 5)),
                        abs_bias_p25=float(np.percentile(ab, 25)),
                        abs_bias_p50=float(np.percentile(ab, 50)),
                        abs_bias_p75=float(np.percentile(ab, 75)),
                        abs_bias_p95=float(np.percentile(ab, 95)),
                        catastrophic_frac=cat_frac,
                        catastrophic_threshold=float(cat_thr),
                        feat_means={fn: float(feats[fn].mean())
                                    for fn in FEATURE_NAMES},
                    )
                    all_results[key] = stats

                    topo_bias[topo].extend(ab.tolist())
                    for fn in FEATURE_NAMES:
                        topo_feats[topo][fn].extend(
                            feats[fn].tolist())

                    cat_s = (f"  cat={cat_frac:.1%}"
                             if cat_frac == cat_frac else "")
                    print(
                        f"    {c_type:20s} {param_label:10s}: "
                        f"n={len(bias):4d}  "
                        f"|bias| mean={ab.mean():.4f} "
                        f"max={ab.max():.4f} "
                        f"p95={np.percentile(ab, 95):.4f}"
                        f"{cat_s}")

            print(f"  [{time.time()-tk:.1f}s]\n")
            sys.stdout.flush()

    # ================================================================
    # Regression
    # ================================================================
    print(f"\n{'='*80}")
    print("  REGRESSION: |bias| ~ spectral_gap + diag_dominance "
          "+ effective_rank")
    print("              + condition_number + off_diagonal_max")
    print(f"{'='*80}")

    reg_lines = ["Plan 009: OLS Regression Results",
                 "=" * 80, ""]
    regression_results = {}
    all_bias_g = []
    all_feats_g = {fn: [] for fn in FEATURE_NAMES}

    for topo in args.topos:
        y = np.array(topo_bias[topo])
        if len(y) < 20:
            continue
        X = np.column_stack(
            [np.array(topo_feats[topo][fn])
             for fn in FEATURE_NAMES])

        all_bias_g.extend(y.tolist())
        for fn in FEATURE_NAMES:
            all_feats_g[fn].extend(topo_feats[topo][fn])

        reg = ols_regression(y, X)
        if reg is None:
            continue
        regression_results[topo] = reg

        hdr = (f"\n  {topo} (n={reg['n_obs']}):  "
               f"R2 = {reg['r_squared']:.4f}")
        print(hdr)
        reg_lines.append(hdr)
        col = f"    {'Feature':25s} {'Coef':>10s} {'p-value':>12s}"
        print(col)
        reg_lines.append(col)
        sep = f"    {'-'*49}"
        print(sep)
        reg_lines.append(sep)
        for fn in FEATURE_NAMES:
            c = reg['coefs'][fn]
            pv = reg['p_values'][fn]
            sig = ('***' if pv < 0.001
                   else ('**' if pv < 0.01
                         else ('*' if pv < 0.05 else '')))
            ln = (f"    {fn:25s} {c:10.4f} "
                  f"{pv:12.6f} {sig}")
            print(ln)
            reg_lines.append(ln)

    y_g = np.array(all_bias_g)
    if len(y_g) >= 20:
        X_g = np.column_stack(
            [np.array(all_feats_g[fn]) for fn in FEATURE_NAMES])
        reg_g = ols_regression(y_g, X_g)
        if reg_g is not None:
            regression_results['_global'] = reg_g
            hdr = (f"\n  GLOBAL (n={reg_g['n_obs']}):  "
                   f"R2 = {reg_g['r_squared']:.4f}")
            print(hdr)
            reg_lines.append(hdr)
            col = (f"    {'Feature':25s} {'Coef':>10s} "
                   f"{'p-value':>12s}")
            print(col)
            reg_lines.append(col)
            sep = f"    {'-'*49}"
            print(sep)
            reg_lines.append(sep)
            for fn in FEATURE_NAMES:
                c = reg_g['coefs'][fn]
                pv = reg_g['p_values'][fn]
                sig = ('***' if pv < 0.001
                       else ('**' if pv < 0.01
                             else ('*' if pv < 0.05 else '')))
                ln = (f"    {fn:25s} {c:10.4f} "
                      f"{pv:12.6f} {sig}")
                print(ln)
                reg_lines.append(ln)

    # ================================================================
    # Save
    # ================================================================
    summary = dict(
        config=dict(
            M=args.M, N=args.N, K_values=args.K,
            topologies=args.topos,
            near_perm_epsilons=NEAR_PERM_EPSILONS,
            feature_names=FEATURE_NAMES),
        bias_results=all_results,
        regression=regression_results,
    )

    json_path = os.path.join(OUT_DIR,
                             'pathological_bias_summary.json')
    with open(json_path, 'w') as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nSaved {json_path}")

    reg_path = os.path.join(OUT_DIR, 'regression_results.txt')
    with open(reg_path, 'w') as f:
        f.write('\n'.join(reg_lines))
    print(f"Saved {reg_path}")

    print(f"\nTotal: {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
