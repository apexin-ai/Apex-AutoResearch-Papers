#!/usr/bin/env python3
"""
Plan 009: Pathological Confusion Matrix Analysis

Identifies structural conditions under which pathological confusion matrices
produce catastrophic estimation bias across 7 DAG topologies.

Three types of pathological C matrices (K×K column-stochastic):

  (a) Near-permutation: C = (1-ε)P + ε·(1/K)·𝟏𝟏ᵀ
      P = random permutation matrix, ε ~ U(0.01, 0.99).
      Models systematic label swaps with varying noise levels.

  (b) Rank-deficient: Dirichlet-generated C with row j ≈ row i + 𝒩(0, σ²),
      σ ~ U(1e-6, 0.05), then column-renormalized.
      Models annotators who cannot distinguish certain categories.

  (c) Block-diagonal: K partitioned into 2 blocks; high within-block confusion
      (Dirichlet α=5), low between-block leakage ~ U(0.001, 0.1).
      Models structured confusion (e.g., fine-grained subcategory mix-ups).

Features computed per matrix:
  - spectral_gap:     λ₁ - λ₂ (top two eigenvalue magnitudes of C)
  - diag_dominance:   min(diag(C)) / (1/K)
  - effective_rank:   (Σσᵢ)² / Σσᵢ² (from SVD)
  - condition_number: σ_max / σ_min

Output:
  - Per-topology OLS regression: bias ~ features (standardized coefficients, R²)
  - Feature importance ranking across topologies
  - Catastrophic bias thresholds per feature
  - Scatter plot: spectral_gap vs |bias| by topology (PNG)
"""

import torch
import numpy as np
import time
import os
import sys
from itertools import permutations

# ================================================================
# Configuration
# ================================================================
K_VALUES = [3]  # primary K; append 5 for extended analysis
N_SAMPLES = 100_000
N_LARGE = 5_000_000
BASE_SEED = 42
DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
DTYPE = torch.float64
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
CATASTROPHIC_BIAS = 0.5

C_TYPES = ['near_permutation', 'rank_deficient', 'block_diagonal']
ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'iv', 'frontdoor']
FEATURE_NAMES = ['spectral_gap', 'diag_dominance', 'effective_rank', 'condition_number']


def get_seed(topo_name, K, c_type, base_seed=BASE_SEED):
    """Deterministic seed per (topo, K, C_type) combination."""
    return hash((topo_name, K, c_type, base_seed)) % (2**32)


# ================================================================
# Parameter Pools (from plan_002, K=3 values match plan_001)
# ================================================================
_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
_IV_DZ_POOL  = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
_IV_DU_POOL  = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
_FD_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_FD_DELTA_POOL = [0.0, 1.0, -0.8, 0.7, -0.5, 0.4, -0.3]


def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()


def make_all_params(K):
    p_A = make_p_A(K)
    return dict(
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K-1]),
                         beta_A=np.array(_BETA_A_POOL[:K-1]), beta_T=2.0, sigma_T=1.0),
        mediation=dict(tau=0.5, gamma=np.array(_GAMMA_POOL[:K]),
                       delta=np.array(_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
        collider=dict(tau=1.0, g=np.zeros(K), dT=np.array(_DT_POOL[:K]),
                      dY=np.array(_DY_POOL[:K])),
        exposure=dict(beta=np.array(_BETA_POOL[:K]), p_A=p_A),
        mbias=dict(tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
                   a1=np.array(_MBIAS_A1_POOL[:K]), a2=np.array(_MBIAS_A2_POOL[:K])),
        iv=dict(lam=1.0, g=np.zeros(K), dZ=np.array(_IV_DZ_POOL[:K]),
                dU=np.array(_IV_DU_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
        frontdoor=dict(alpha_U=1.0, lam_U=1.0, gamma=np.array(_FD_GAMMA_POOL[:K]),
                       delta=np.array(_FD_DELTA_POOL[:K]), beta=np.array(_BETA_POOL[:K])),
    )


# ================================================================
# DGP Generators (from plan_002)
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
    logits = p['g'][None, :] + p['dT'][None, :] * T[:, None] + p['dY'][None, :] * Y[:, None]
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


_GEN_OLS = dict(confounding=gen_confounding, mediation=gen_mediation,
                collider=gen_collider, mbias=gen_mbias, frontdoor=gen_frontdoor)


# ================================================================
# Sufficient Statistics (from plan_002)
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
        z1 = Z == 1; z0 = Z == 0
        self.RF = Y[z1].mean() - Y[z0].mean()
        self.FS = np.zeros(K)
        for k in range(K):
            self.FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()

    def to_device(self, dev):
        self.t_RF = torch.tensor(self.RF, dtype=DTYPE, device=dev)
        self.t_FS = torch.tensor(self.FS, dtype=DTYPE, device=dev)
        return self


# ================================================================
# GPU-Batched Plim Functions (from plan_002)
# ================================================================
def plim_with_T(ss, C):
    """Plim of OLS Y ~ 1 + T + D_A* for topologies with treatment T."""
    B, K = C.shape[0], ss.K
    dim = K + 1
    q = C @ ss.t_p_A
    ct = C @ ss.t_E_TD
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1] = ss.t_E_T; EZZ[:, 1, 0] = ss.t_E_T
    EZZ[:, 1, 1] = ss.t_E_T2
    EZZ[:, 0, 2:] = q[:, 1:]; EZZ[:, 2:, 0] = q[:, 1:]
    EZZ[:, 1, 2:] = ct[:, 1:]; EZZ[:, 2:, 1] = ct[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y; EZY[:, 1] = ss.t_E_TY; EZY[:, 2:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_exposure(ss, C):
    """Plim of OLS Y ~ 1 + D_A* for exposure topology (no treatment)."""
    B, K = C.shape[0], ss.K
    dim = K
    q = C @ ss.t_p_A
    cy = C @ ss.t_E_YD
    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1:] = q[:, 1:]; EZZ[:, 1:, 0] = q[:, 1:]
    idx = torch.arange(K - 1, device=C.device)
    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
    EZY[:, 0] = ss.t_E_Y; EZY[:, 1:] = cy[:, 1:]
    return torch.linalg.solve(EZZ, EZY)


def plim_iv_batched(ss, C):
    """Plim of Wald IV estimator for IV topology."""
    FS_star = C @ ss.t_FS
    denom = FS_star[:, 1]
    nan_val = torch.tensor(float('nan'), dtype=DTYPE, device=C.device)
    result = torch.where(denom.abs() < 1e-8, nan_val, ss.t_RF / denom)
    return result.unsqueeze(1)


# ================================================================
# Pathological C Matrix Generators
# ================================================================
def gen_near_permutation(K, N, device, seed):
    """Near-permutation matrices: C = (1-ε)P + ε·(1/K)·𝟏𝟏ᵀ.

    P is a uniformly random K×K permutation matrix. ε ~ U(0.01, 0.99).
    When ε→0, C is a pure label permutation (worst case for some topologies).
    When ε→1, C approaches uniform confusion (1/K everywhere).
    Column-stochastic by construction (convex combination of stochastic matrices).
    """
    rng = np.random.default_rng(seed)

    all_perms = np.array(list(permutations(range(K))))
    n_perms = len(all_perms)

    perm_indices = rng.integers(0, n_perms, size=N)
    epsilons = rng.uniform(0.01, 0.99, size=N)

    P = np.zeros((N, K, K))
    selected = all_perms[perm_indices]
    batch_idx = np.arange(N)[:, None].repeat(K, axis=1)
    col_idx = np.arange(K)[None, :].repeat(N, axis=0)
    P[batch_idx, selected, col_idx] = 1.0

    uniform = np.ones((K, K)) / K
    eps = epsilons[:, None, None]
    C = (1 - eps) * P + eps * uniform[None, :, :]

    return torch.tensor(C, dtype=DTYPE, device=device)


def gen_rank_deficient(K, N, device, seed):
    """Rank-deficient matrices: row j set to row i plus small noise, then renormalized.

    Starts from Dirichlet-generated column-stochastic C (full rank).
    Picks random rows i≠j and sets C[j,:] = C[i,:] + 𝒩(0, σ²), σ ~ U(1e-6, 0.05).
    Clipped to positive and column-renormalized.
    Models annotators who conflate two categories (near-singular label mapping).
    """
    rng = np.random.default_rng(seed)

    C = np.zeros((N, K, K))
    for j in range(K):
        C[:, :, j] = rng.dirichlet(np.ones(K), N)

    row_i = rng.integers(0, K, size=N)
    row_j = (row_i + rng.integers(1, K, size=N)) % K
    noise_scale = rng.uniform(1e-6, 0.05, size=(N, 1))
    noise = rng.normal(0, 1, size=(N, K)) * noise_scale

    batch_idx = np.arange(N)
    C[batch_idx, row_j, :] = C[batch_idx, row_i, :] + noise

    C = np.maximum(C, 1e-10)
    C /= C.sum(axis=1, keepdims=True)

    return torch.tensor(C, dtype=DTYPE, device=device)


def gen_block_diagonal(K, N, device, seed):
    """Block-diagonal matrices: high within-block confusion, low between-block leakage.

    K classes partitioned into 2 blocks. Within-block columns drawn from
    Dirichlet(α=5) (concentrated). Between-block leakage ~ U(0.001, 0.1) per matrix.
    Models structured confusion where annotators confuse fine-grained subcategories
    within semantic groups but rarely across groups.
    """
    rng = np.random.default_rng(seed)

    if K == 3:
        blocks = [[0, 1], [2]]
    elif K == 5:
        blocks = [[0, 1], [2, 3, 4]]
    else:
        mid = K // 2
        blocks = [list(range(mid)), list(range(mid, K))]

    class_to_block = np.zeros(K, dtype=int)
    for b_idx, block in enumerate(blocks):
        for k in block:
            class_to_block[k] = b_idx

    C = np.zeros((N, K, K))
    leakage = rng.uniform(0.001, 0.1, size=N)

    for j in range(K):
        b_idx = class_to_block[j]
        own_block = blocks[b_idx]
        other_rows = [r for r in range(K) if r not in own_block]
        block_size = len(own_block)
        other_size = len(other_rows)

        within_mass = np.maximum(1.0 - leakage * other_size, 0.1)
        within_probs = rng.dirichlet(np.ones(block_size) * 5, size=N)
        for idx, row in enumerate(own_block):
            C[:, row, j] = within_mass * within_probs[:, idx]

        if other_size > 0:
            between_total = 1.0 - within_mass
            between_probs = rng.dirichlet(np.ones(other_size), size=N)
            for idx, row in enumerate(other_rows):
                C[:, row, j] = between_total * between_probs[:, idx]

    C = np.maximum(C, 1e-10)
    C /= C.sum(axis=1, keepdims=True)

    return torch.tensor(C, dtype=DTYPE, device=device)


_C_GENERATORS = {
    'near_permutation': gen_near_permutation,
    'rank_deficient': gen_rank_deficient,
    'block_diagonal': gen_block_diagonal,
}


# ================================================================
# Matrix Feature Computation (GPU-batched)
# ================================================================
def compute_matrix_features(C_batch):
    """Compute spectral and structural features for a batch of C matrices.

    Returns dict of (B,) real tensors on same device as C_batch:
      spectral_gap:     |λ₁| - |λ₂|  (eigenvalue magnitude gap)
      diag_dominance:   min(diag(C)) * K  (ratio to uniform baseline 1/K)
      effective_rank:   (Σσ)² / Σσ²  (SVD-based effective dimensionality)
      condition_number: σ_max / σ_min  (numerical conditioning)
    """
    B, K, _ = C_batch.shape

    eigvals = torch.linalg.eigvals(C_batch)
    eigvals_abs = eigvals.abs()
    eigvals_sorted, _ = eigvals_abs.sort(dim=1, descending=True)
    spectral_gap = eigvals_sorted[:, 0] - eigvals_sorted[:, 1]

    diag_vals = torch.diagonal(C_batch, dim1=1, dim2=2)
    diag_dominance = diag_vals.min(dim=1).values * K

    sv = torch.linalg.svdvals(C_batch)
    sv_sum = sv.sum(dim=1)
    sv_sq_sum = (sv ** 2).sum(dim=1)
    effective_rank = (sv_sum ** 2) / sv_sq_sum.clamp(min=1e-30)
    condition_number = sv[:, 0] / sv[:, -1].clamp(min=1e-15)

    return {
        'spectral_gap': spectral_gap,
        'diag_dominance': diag_dominance,
        'effective_rank': effective_rank,
        'condition_number': condition_number,
    }


# ================================================================
# Regression Analysis
# ================================================================
def run_regression(bias_np, features_np, feature_names):
    """Standardized OLS: bias ~ spectral_gap + diag_dominance + effective_rank + condition_number.

    Returns standardized coefficients (unit-free, comparable across features) and R².
    Uses z-scored features so |β*| directly indicates relative predictive strength.
    """
    y = bias_np.copy()
    X = np.column_stack([features_np[name] for name in feature_names])

    valid = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
    y, X = y[valid], X[valid]
    if len(y) < 10:
        return None

    X_mean, X_std = X.mean(0), X.std(0)
    X_std[X_std < 1e-10] = 1.0
    X_z = (X - X_mean) / X_std
    y_mean, y_std = y.mean(), y.std()
    if y_std < 1e-10:
        return None
    y_z = (y - y_mean) / y_std

    X_aug = np.column_stack([np.ones(len(y_z)), X_z])
    beta, _, _, _ = np.linalg.lstsq(X_aug, y_z, rcond=None)

    y_pred = X_aug @ beta
    ss_res = ((y_z - y_pred) ** 2).sum()
    ss_tot = (y_z ** 2).sum()
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {
        'coefs': dict(zip(feature_names, beta[1:])),
        'r_squared': r2,
        'n_valid': len(y),
    }


def find_catastrophic_thresholds(bias_np, features_np, feature_names,
                                  bias_thr=CATASTROPHIC_BIAS, prob_thr=0.9):
    """Find feature thresholds where P(|bias| > bias_thr | condition) > prob_thr.

    For spectral_gap, diag_dominance, effective_rank: search feature < threshold (low = bad).
    For condition_number: search feature > threshold (high = bad).
    Scans percentile grid; returns first threshold crossing prob_thr or None.
    """
    is_catastrophic = bias_np > bias_thr
    if is_catastrophic.sum() == 0:
        return {name: None for name in feature_names}

    thresholds = {}
    for name in feature_names:
        x = features_np[name]
        valid = np.isfinite(x) & np.isfinite(bias_np)
        x_v, cat_v = x[valid], is_catastrophic[valid]

        if name == 'condition_number':
            percentiles = np.percentile(x_v, np.arange(95, 0, -5))
            best = None
            for p_val in percentiles:
                mask = x_v > p_val
                if mask.sum() < 10:
                    continue
                if cat_v[mask].mean() >= prob_thr:
                    best = p_val
                    break
            thresholds[name] = best
        else:
            percentiles = np.percentile(x_v, np.arange(5, 100, 5))
            best = None
            for p_val in percentiles:
                mask = x_v < p_val
                if mask.sum() < 10:
                    continue
                if cat_v[mask].mean() >= prob_thr:
                    best = p_val
                    break
            thresholds[name] = best

    return thresholds


# ================================================================
# Visualization
# ================================================================
def save_scatter_plot(plot_data, K, out_path):
    """Scatter: spectral_gap vs |bias|, colored by topology, faceted by C type."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, len(C_TYPES), figsize=(6 * len(C_TYPES), 5))
    if len(C_TYPES) == 1:
        axes = [axes]

    colors = plt.cm.tab10(np.linspace(0, 1, len(ALL_TOPOS)))
    topo_colors = dict(zip(ALL_TOPOS, colors))

    for ax, c_type in zip(axes, C_TYPES):
        for topo in ALL_TOPOS:
            key = (topo, c_type)
            if key not in plot_data:
                continue
            sg = plot_data[key]['spectral_gap']
            bias = plot_data[key]['bias']
            n = len(bias)
            idx = np.random.default_rng(0).choice(n, min(2000, n), replace=False)
            ax.scatter(sg[idx], bias[idx], alpha=0.3, s=5,
                       color=topo_colors[topo], label=topo)
        ax.set_xlabel('Spectral Gap (λ₁ − λ₂)')
        ax.set_ylabel('|Bias|')
        ax.set_title(f'K={K}, {c_type}')
        ax.legend(fontsize=7, markerscale=3)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {out_path}")


# ================================================================
# Main
# ================================================================
def main():
    t0 = time.time()
    print("=" * 100)
    print("  PLAN 009: PATHOLOGICAL CONFUSION MATRIX ANALYSIS")
    print("=" * 100)
    print(f"  Device: {DEVICE}")
    if DEVICE.type == 'cuda':
        print(f"  GPU: {torch.cuda.get_device_name(0)}")
        print(f"  VRAM: {torch.cuda.get_device_properties(0).total_mem // 1024**3} GB")
    print(f"  K_values={K_VALUES}, N_samples={N_SAMPLES:,}, N_large={N_LARGE:,}")
    print(f"  C_types: {C_TYPES}")
    print(f"  Catastrophic bias threshold: {CATASTROPHIC_BIAS}")
    sys.stdout.flush()

    all_regressions = {}
    all_thresholds = {}
    plot_data = {}

    for K in K_VALUES:
        params = make_all_params(K)
        print(f"\n{'='*100}")
        print(f"  K = {K}")
        print(f"{'='*100}")
        sys.stdout.flush()

        # ---- Phase 1: Precompute sufficient statistics ----
        suff_stats = {}
        plim_true_vals = {}

        for topo in ALL_TOPOS:
            p = params[topo]
            rng = np.random.default_rng(BASE_SEED)

            if topo == 'iv':
                Z, Y, A = gen_iv(K, N_LARGE, p, rng)
                ss = IVSuffStats(Z, Y, A, K).to_device(DEVICE)
                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                tau_I = plim_iv_batched(ss, I_batch)[0, 0].item()
                suff_stats[topo] = ss
                plim_true_vals[topo] = tau_I
                print(f"  {topo}: tau_true(Wald) = {tau_I:.6f}")
            elif topo == 'exposure':
                _, Y, A = gen_exposure(K, N_LARGE, p, rng)
                ss = SuffStats(None, Y, A, K).to_device(DEVICE)
                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                plim_I = plim_exposure(ss, I_batch).squeeze(0)
                tau_I = plim_I[1].item()
                suff_stats[topo] = ss
                plim_true_vals[topo] = tau_I
                print(f"  {topo}: beta1_true = {tau_I:.6f}")
            else:
                T, Y, A = _GEN_OLS[topo](K, N_LARGE, p, rng)
                ss = SuffStats(T, Y, A, K).to_device(DEVICE)
                I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
                plim_I = plim_with_T(ss, I_batch).squeeze(0)
                tau_I = plim_I[1].item()
                suff_stats[topo] = ss
                plim_true_vals[topo] = tau_I
                print(f"  {topo}: tau_true = {tau_I:.6f}")
            sys.stdout.flush()

        # ---- Phase 2: Compute bias & features per (topo, C_type) ----
        print(f"\n  --- Computing bias & features ---")

        for c_type in C_TYPES:
            print(f"\n  C_type: {c_type}")

            for topo in ALL_TOPOS:
                tk = time.time()
                seed = get_seed(topo, K, c_type)
                ss = suff_stats[topo]
                tau_I = plim_true_vals[topo]

                C_batch = _C_GENERATORS[c_type](K, N_SAMPLES, DEVICE, seed)

                if topo == 'iv':
                    plim_all = plim_iv_batched(ss, C_batch)[:, 0]
                elif topo == 'exposure':
                    plim_all = plim_exposure(ss, C_batch)[:, 1]
                else:
                    plim_all = plim_with_T(ss, C_batch)[:, 1]

                bias = (plim_all - tau_I).abs()

                feats = compute_matrix_features(C_batch)

                valid = torch.isfinite(bias)
                for fname in FEATURE_NAMES:
                    valid &= torch.isfinite(feats[fname])
                n_valid = valid.sum().item()

                bias_np = bias[valid].cpu().double().numpy()
                feats_np = {name: feats[name][valid].cpu().double().numpy()
                            for name in FEATURE_NAMES}

                plot_data[(topo, c_type)] = {
                    'bias': bias_np,
                    'spectral_gap': feats_np['spectral_gap'],
                }

                reg = run_regression(bias_np, feats_np, FEATURE_NAMES)
                key = (topo, K, c_type)
                all_regressions[key] = reg

                thr = find_catastrophic_thresholds(bias_np, feats_np, FEATURE_NAMES)
                all_thresholds[key] = thr

                cat_frac = (bias_np > CATASTROPHIC_BIAS).mean() if len(bias_np) > 0 else 0
                print(f"    {topo:14s}: valid={n_valid:,}/{N_SAMPLES:,}  "
                      f"bias_mean={bias_np.mean():.4f}  bias_max={bias_np.max():.4f}  "
                      f"catastrophic={cat_frac:.1%}  [{time.time()-tk:.1f}s]")
                sys.stdout.flush()

        # ---- Phase 3: Regression results ----
        print(f"\n{'='*100}")
        print(f"  REGRESSION RESULTS: bias ~ features (standardized coefficients), K={K}")
        print(f"{'='*100}")

        for c_type in C_TYPES:
            print(f"\n  C_type: {c_type}")
            print(f"  {'Topology':14s} {'R²':>6s}  {'spectral_gap':>14s} {'diag_domin':>12s} "
                  f"{'eff_rank':>10s} {'cond_num':>10s}")
            print(f"  {'-'*72}")

            for topo in ALL_TOPOS:
                reg = all_regressions.get((topo, K, c_type))
                if reg is None:
                    print(f"  {topo:14s}  (insufficient data)")
                    continue
                coefs = reg['coefs']
                print(f"  {topo:14s} {reg['r_squared']:6.3f}  "
                      f"{coefs['spectral_gap']:>14.4f} {coefs['diag_dominance']:>12.4f} "
                      f"{coefs['effective_rank']:>10.4f} {coefs['condition_number']:>10.4f}")

        # ---- Phase 4: Feature importance ranking ----
        print(f"\n  TOP PREDICTIVE FEATURES (avg |standardized β| across topologies)")
        for c_type in C_TYPES:
            avg_imp = {fname: 0.0 for fname in FEATURE_NAMES}
            count = 0
            for topo in ALL_TOPOS:
                reg = all_regressions.get((topo, K, c_type))
                if reg is None:
                    continue
                count += 1
                for fname in FEATURE_NAMES:
                    avg_imp[fname] += abs(reg['coefs'][fname])
            if count > 0:
                for fname in FEATURE_NAMES:
                    avg_imp[fname] /= count

            ranked = sorted(avg_imp.items(), key=lambda x: -x[1])
            print(f"\n  {c_type}:")
            for rank, (fname, imp) in enumerate(ranked, 1):
                print(f"    #{rank}: {fname:20s}  avg|β*| = {imp:.4f}")

        # ---- Phase 5: Catastrophic bias thresholds ----
        print(f"\n  CATASTROPHIC BIAS THRESHOLDS: P(|bias|>{CATASTROPHIC_BIAS}) > 90%")
        for c_type in C_TYPES:
            print(f"\n  {c_type}:")
            print(f"  {'Topology':14s} {'spectral_gap':>14s} {'diag_domin':>14s} "
                  f"{'eff_rank':>14s} {'cond_num':>14s}")
            print(f"  {'-'*72}")
            for topo in ALL_TOPOS:
                thr = all_thresholds.get((topo, K, c_type), {})
                parts = [f"  {topo:14s}"]
                for fname in FEATURE_NAMES:
                    val = thr.get(fname)
                    if val is None:
                        s = "N/A"
                    elif fname == 'condition_number':
                        s = f">{val:.1f}"
                    else:
                        s = f"<{val:.4f}"
                    parts.append(f"{s:>14s}")
                print("".join(parts))

        # ---- Phase 6: Scatter plot ----
        png_path = os.path.join(OUT_DIR, f"plan_009_scatter_K{K}.png")
        try:
            save_scatter_plot(plot_data, K, png_path)
        except Exception as e:
            print(f"  Warning: plot failed: {e}")

    print(f"\n{'='*100}")
    print(f"  Total runtime: {time.time() - t0:.0f}s")
    print(f"{'='*100}")


if __name__ == "__main__":
    main()
