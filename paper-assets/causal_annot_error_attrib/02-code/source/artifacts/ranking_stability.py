#!/usr/bin/env python3
"""
ASV topology ranking stability analysis.

Computes three things:
  1. ASV topology ranking stability: For N random Dirichlet(1,1,1) confusion
     matrices C0, compute magnitude ASV delta* for 6 topologies and measure
     Kendall tau correlation between empirical and theoretical ranking.
     Collider/M-bias are assigned ASV=inf (immune) since annotation error
     is protective (|B| non-increasing). IV is included but may produce NaN
     due to first-stage singularities.
  2. Epsilon-perturbation ranking robustness: At each delta*, check if
     perturbing by +/-0.013 would change the relative ranking between any
     pair of topologies.
  3. Large-scale Conjecture verification: Verify epsilon-approximate
     monotonicity of |B(C(delta))| along delta in [0,1] for non-IV topologies.
     Report worst-case step deviation across all matrices.

Uses analytic plim computation (Gauss-Hermite quadrature for nonlinear
topologies) -- zero sampling noise. Fully vectorized over matrices in chunks.

Input: Random K=3 Dirichlet(1,1,1) confusion matrices.
Output: artifacts/ranking_stability_results.json + console summary.
"""

import numpy as np
import json
import time
import sys
import os
from scipy.special import roots_hermite
from scipy.stats import kendalltau, rankdata

# ====================================================================
# Gauss-Hermite quadrature setup
# ====================================================================
N_GH = 100
_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
GH_X = _gh_x_raw * np.sqrt(2)
GH_W = _gh_w_raw / np.sqrt(np.pi)

GH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')
GH_W2 = np.outer(GH_W, GH_W)
GH_X2_a_flat = GH_X2_a.ravel()
GH_X2_b_flat = GH_X2_b.ravel()
GH_W2_flat = GH_W2.ravel()

# ====================================================================
# Configuration
# ====================================================================
K = 3
N_MATRICES = 1_000_000
CHUNK_SIZE = 10_000          # process this many matrices at once
SEED = 42
DELTA_STEP = 0.005           # step size for bias curve
ASV_EPSILON = 0.05           # magnitude ASV threshold (10% of tau=0.5)
PERTURB_EPSILON = 0.013      # perturbation for ranking robustness check
MONO_TOL = 1e-12             # tolerance for monotonicity violation detection

# Theoretical ranking (most fragile to most robust)
THEORETICAL_RANKING_ORDER = [
    'iv', 'frontdoor', 'mediation', 'confounding', 'collider', 'mbias'
]

RANKING_TOPOS = ['iv', 'frontdoor', 'mediation', 'confounding',
                 'collider', 'mbias']
CONJECTURE_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
                    'mbias', 'frontdoor']
ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'iv', 'frontdoor']

NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
NON_INCREASING = {'collider', 'mbias'}
PROTECTIVE = {'collider', 'mbias'}

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Fixed delta grid (delta_max capped at 1.0 for all Dirichlet matrices)
DELTAS = np.arange(0, 1.0 + DELTA_STEP / 2, DELTA_STEP)
N_DELTA = len(DELTAS)

# ====================================================================
# DGP parameters (paper defaults, K=3)
# ====================================================================
DGP_PARAMS = {
    'confounding': dict(
        p_A=np.array([0.40, 0.35, 0.25]),
        alpha=np.array([1.5, -1.0]),
        beta_A=np.array([1.0, -0.5]),
        beta_T=2.0, sigma_T=1.0),
    'mediation': dict(
        tau=0.5,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 0.8, -0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    'collider': dict(
        tau=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        dT=np.array([0.0, 0.5, -0.3]),
        dY=np.array([0.0, 0.8, 0.6])),
    'exposure': dict(
        beta=np.array([0.0, 1.0, -0.5]),
        p_A=np.array([0.40, 0.35, 0.25])),
    'mbias': dict(
        tau=1.0, delta_coef=1.0, lam=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        a1=np.array([0.0, 0.8, -0.5]),
        a2=np.array([0.0, 0.6, 0.9])),
    'iv': dict(
        lam=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        dZ=np.array([0.0, 1.0, -0.5]),
        dU=np.array([0.0, 0.8, 0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    'frontdoor': dict(
        alpha_U=1.0, lam_U=1.0,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 1.0, -0.8]),
        beta=np.array([0.0, 1.0, -0.5])),
}


# ====================================================================
# Stable softmax
# ====================================================================
def _softmax(logits):
    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


# ====================================================================
# Analytic Sufficient Statistics
# ====================================================================
class SuffStats:
    def __init__(self, K, has_T=True):
        self.K = K
        self.has_T = has_T


class IVSuffStats:
    def __init__(self, K):
        self.K = K


def compute_confounding_ss(p):
    ss = SuffStats(K, has_T=True)
    p_A = p['p_A']
    alpha = p['alpha']
    beta_A = p['beta_A']
    beta_T = p['beta_T']
    sigma_T = p['sigma_T']
    ss.p_A = p_A.copy()
    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))
    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2
    ss.E_TD = np.zeros(K)
    for k in range(1, K):
        ss.E_TD[k] = alpha[k - 1] * p_A[k]
    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))
    ss.E_YD = np.zeros(K)
    for k in range(1, K):
        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]
    ss.E_TY = beta_T * ss.E_T2 + sum(
        beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))
    return ss


def compute_exposure_ss(p):
    ss = SuffStats(K, has_T=False)
    p_A = p['p_A']
    beta = p['beta']
    ss.p_A = p_A.copy()
    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))
    ss.E_YD = np.zeros(K)
    ss.E_YD[0] = beta[0] * p_A[0]
    for k in range(1, K):
        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]
    return ss


def compute_mediation_ss(p):
    ss = SuffStats(K, has_T=True)
    tau = p['tau']
    gamma = p['gamma']
    delta_coef = p['delta']
    beta = p['beta']
    probs_T0 = _softmax(gamma)
    probs_T1 = _softmax(gamma + delta_coef)
    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1
    ss.E_T = 0.5
    ss.E_T2 = 0.5
    ss.E_TD = 0.5 * probs_T1
    ss.E_Y = (beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K))
              + tau * 0.5)
    ss.E_YD = np.zeros(K)
    for k in range(K):
        beta_k = beta[k] if k >= 1 else 0.0
        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]
    ss.E_TY = (beta[0] * 0.5
               + sum(beta[k] * ss.E_TD[k] for k in range(1, K))
               + tau * 0.5)
    return ss


def compute_collider_ss(p):
    ss = SuffStats(K, has_T=True)
    tau = p['tau']
    g, dT, dY = p['g'], p['dT'], p['dY']
    coeff1 = dT + tau * dY
    coeff2 = dY
    logits = (g[None, :]
              + coeff1[None, :] * GH_X2_a_flat[:, None]
              + coeff2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)
    T_vals = GH_X2_a_flat
    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat
    w = GH_W2_flat
    ss.p_A = (w[:, None] * probs).sum(axis=0)
    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)
    ss.E_T = 0.0
    ss.E_T2 = 1.0
    ss.E_Y = 0.0
    ss.E_TY = tau
    return ss


def compute_mbias_ss(p):
    ss = SuffStats(K, has_T=True)
    tau = p['tau']
    delta_coef = p['delta_coef']
    lam = p['lam']
    g, a1, a2 = p['g'], p['a1'], p['a2']
    logits = (g[None, :]
              + a1[None, :] * GH_X2_a_flat[:, None]
              + a2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)
    w = GH_W2_flat
    ss.p_A = (w[:, None] * probs).sum(axis=0)
    E_U1_Dk = (w[:, None] * GH_X2_a_flat[:, None] * probs).sum(axis=0)
    E_U2_Dk = (w[:, None] * GH_X2_b_flat[:, None] * probs).sum(axis=0)
    ss.E_TD = delta_coef * E_U1_Dk
    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk
    ss.E_T = 0.0
    ss.E_T2 = delta_coef**2 + 1.0
    ss.E_Y = 0.0
    ss.E_TY = tau * ss.E_T2
    return ss


def compute_frontdoor_ss(p):
    ss = SuffStats(K, has_T=True)
    alpha_U = p['alpha_U']
    lam_U = p['lam_U']
    gamma = p['gamma']
    delta_coef = p['delta']
    beta = p['beta']
    sigma_T2 = alpha_U**2 + 1.0
    sigma_T = np.sqrt(sigma_T2)
    T_nodes = GH_X * sigma_T
    T_weights = GH_W
    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
    probs = _softmax(logits)
    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)
    E_U_given_T = alpha_U / sigma_T2 * T_nodes
    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)
    ss.E_YD = np.zeros(K)
    for k in range(K):
        beta_k = beta[k] if k >= 1 else 0.0
        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]
    ss.E_T = 0.0
    ss.E_T2 = sigma_T2
    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
    ss.E_TY = (sum(beta[k] * ss.E_TD[k] for k in range(1, K))
               + lam_U * alpha_U)
    return ss


def compute_iv_ss(p):
    ivss = IVSuffStats(K)
    g, dZ, dU = p['g'], p['dZ'], p['dU']
    beta = p['beta']
    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]
    probs_z0 = _softmax(logits_z0)
    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)
    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]
    probs_z1 = _softmax(logits_z1)
    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)
    ivss.FS = P_A_z1 - P_A_z0
    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))
    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))
    ivss.RF = E_Y_z1 - E_Y_z0
    return ivss


COMPUTE_SS = {
    'confounding': compute_confounding_ss,
    'mediation': compute_mediation_ss,
    'collider': compute_collider_ss,
    'exposure': compute_exposure_ss,
    'mbias': compute_mbias_ss,
    'iv': compute_iv_ss,
    'frontdoor': compute_frontdoor_ss,
}


def get_tau_true(topo, ss):
    """True causal parameter."""
    p = DGP_PARAMS[topo]
    if topo in PROTECTIVE:
        return p['tau']
    if topo == 'iv':
        if abs(ss.FS[1]) < 1e-15:
            return np.nan
        return ss.RF / ss.FS[1]
    elif topo == 'exposure':
        q = ss.p_A
        EZZ = np.zeros((K, K))
        EZZ[0, 0] = 1.0
        EZZ[0, 1:] = q[1:]
        EZZ[1:, 0] = q[1:]
        for j in range(K - 1):
            EZZ[j + 1, j + 1] = q[j + 1]
        EZY = np.zeros(K)
        EZY[0] = ss.E_Y
        EZY[1:] = ss.E_YD[1:]
        return np.linalg.solve(EZZ, EZY)[1]
    else:
        q = ss.p_A
        ct = ss.E_TD
        cy = ss.E_YD
        dim = K + 1
        EZZ = np.zeros((dim, dim))
        EZZ[0, 0] = 1.0
        EZZ[0, 1] = ss.E_T
        EZZ[1, 0] = ss.E_T
        EZZ[1, 1] = ss.E_T2
        EZZ[0, 2:] = q[1:]
        EZZ[2:, 0] = q[1:]
        EZZ[1, 2:] = ct[1:]
        EZZ[2:, 1] = ct[1:]
        for j in range(K - 1):
            EZZ[j + 2, j + 2] = q[j + 1]
        EZY = np.zeros(dim)
        EZY[0] = ss.E_Y
        EZY[1] = ss.E_TY
        EZY[2:] = cy[1:]
        return np.linalg.solve(EZZ, EZY)[1]


# ====================================================================
# Batch bias curve + ASV + monotonicity (fully vectorized)
# ====================================================================
def process_batch_iv(C0_batch, ss, tau_true):
    """Process a batch of C0 matrices for IV topology.

    Args:
        C0_batch: (M, K, K) confusion matrices
        ss: IVSuffStats
        tau_true: scalar

    Returns:
        asv_vals: (M,) ASV values (inf if threshold never crossed)
    """
    M = C0_batch.shape[0]
    # FS0[m, k] = sum_j C0[m, k, j] * ss.FS[j]
    FS0 = np.einsum('mkj,j->mk', C0_batch, ss.FS)  # (M, K)

    # For each delta, FS*(delta) = (1-d)*ss.FS + d*FS0
    # Shape: (N_DELTA, M, K)
    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
    fs_star = (1 - d) * ss.FS[None, None, :] + d * FS0[None, :, :]
    denom = fs_star[:, :, 1]  # (N_DELTA, M)

    # tau(delta) = RF / denom
    with np.errstate(divide='ignore', invalid='ignore'):
        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)

    bias_abs = np.abs(taus - tau_true)  # (N_DELTA, M)

    # ASV: find first delta where running-max envelope > ASV_EPSILON
    # Compute running max along delta axis
    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
    # Find first crossing
    crossed = envelope > ASV_EPSILON  # (N_DELTA, M)
    # For each matrix, find first delta index where crossed
    # Use argmax on the crossed array (first True)
    any_crossed = crossed.any(axis=0)  # (M,)
    first_idx = crossed.argmax(axis=0)  # (M,) — 0 if never crossed
    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)

    return asv_vals


def process_batch_exposure(C0_batch, ss, tau_true):
    """Process batch for exposure topology.

    Returns:
        asv_vals: (M,) ASV values
        worst_devs: (M,) worst monotonicity violation per matrix
    """
    M = C0_batch.shape[0]
    # Precompute C0 @ ss.p_A and C0 @ ss.E_YD for all matrices
    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)  # (M, K)
    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)  # (M, K)

    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
    # q[delta, m, k] = (1-delta)*ss.p_A[k] + delta*pA0[m, k]
    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]

    # Build EZZ: (N_DELTA, M, K, K) — but K=3, so (N_D, M, 3, 3)
    dim = K
    EZZ = np.zeros((N_DELTA, M, dim, dim))
    EZZ[:, :, 0, 0] = 1.0
    EZZ[:, :, 0, 1:] = q[:, :, 1:]
    EZZ[:, :, 1:, 0] = q[:, :, 1:]
    for j in range(K - 1):
        EZZ[:, :, j + 1, j + 1] = q[:, :, j + 1]

    EZY = np.zeros((N_DELTA, M, dim))
    EZY[:, :, 0] = ss.E_Y
    EZY[:, :, 1:] = cy[:, :, 1:]

    # Solve for all at once: (N_DELTA * M, dim, dim) solve
    EZZ_flat = EZZ.reshape(-1, dim, dim)
    EZY_flat = EZY.reshape(-1, dim, 1)
    try:
        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
    except np.linalg.LinAlgError:
        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
    taus = coefs_flat[:, 1].reshape(N_DELTA, M)

    bias_abs = np.abs(taus - tau_true)

    # ASV
    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
    crossed = envelope > ASV_EPSILON
    any_crossed = crossed.any(axis=0)
    first_idx = crossed.argmax(axis=0)
    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)

    # Monotonicity: non-decreasing
    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
    diffs = np.diff(valid_bias, axis=0)  # (N_DELTA-1, M)
    violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
    worst_devs = violations.max(axis=0)  # (M,)

    return asv_vals, worst_devs


def process_batch_with_T(C0_batch, ss, tau_true, topo):
    """Process batch for topologies with treatment T.

    Returns:
        asv_vals: (M,) ASV values (None if protective)
        worst_devs: (M,) worst monotonicity violation per matrix
    """
    M = C0_batch.shape[0]
    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)
    TD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_TD)
    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)

    d = DELTAS[:, None, None]
    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
    ct = (1 - d) * ss.E_TD[None, None, :] + d * TD0[None, :, :]
    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]

    dim = K + 1
    EZZ = np.zeros((N_DELTA, M, dim, dim))
    EZZ[:, :, 0, 0] = 1.0
    EZZ[:, :, 0, 1] = ss.E_T
    EZZ[:, :, 1, 0] = ss.E_T
    EZZ[:, :, 1, 1] = ss.E_T2
    EZZ[:, :, 0, 2:] = q[:, :, 1:]
    EZZ[:, :, 2:, 0] = q[:, :, 1:]
    EZZ[:, :, 1, 2:] = ct[:, :, 1:]
    EZZ[:, :, 2:, 1] = ct[:, :, 1:]
    for j in range(K - 1):
        EZZ[:, :, j + 2, j + 2] = q[:, :, j + 1]

    EZY = np.zeros((N_DELTA, M, dim))
    EZY[:, :, 0] = ss.E_Y
    EZY[:, :, 1] = ss.E_TY
    EZY[:, :, 2:] = cy[:, :, 1:]

    EZZ_flat = EZZ.reshape(-1, dim, dim)
    EZY_flat = EZY.reshape(-1, dim, 1)
    try:
        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
    except np.linalg.LinAlgError:
        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
    taus = coefs_flat[:, 1].reshape(N_DELTA, M)

    bias_abs = np.abs(taus - tau_true)

    # ASV (only for non-protective topologies)
    asv_vals = None
    if topo not in PROTECTIVE:
        envelope = np.fmax.accumulate(
            np.nan_to_num(bias_abs, nan=0.0), axis=0)
        crossed = envelope > ASV_EPSILON
        any_crossed = crossed.any(axis=0)
        first_idx = crossed.argmax(axis=0)
        asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)

    # Monotonicity
    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
    diffs = np.diff(valid_bias, axis=0)
    if topo in NON_DECREASING:
        violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
    else:
        violations = np.where(diffs > MONO_TOL, diffs, 0.0)
    worst_devs = violations.max(axis=0)

    return asv_vals, worst_devs


# ====================================================================
# Main
# ====================================================================
def main():
    t_total = time.time()

    print("ASV Topology Ranking Stability Analysis")
    print(f"  N_matrices = {N_MATRICES:,}")
    print(f"  K = {K}, ASV_threshold = {ASV_EPSILON}")
    print(f"  Perturbation epsilon = {PERTURB_EPSILON}")
    print(f"  delta_step = {DELTA_STEP}, n_delta = {N_DELTA}")
    print(f"  GH quadrature: {N_GH} pts/dim")
    print(f"  Chunk size: {CHUNK_SIZE:,}")
    print(f"  Seed = {SEED}")
    print("=" * 70)
    sys.stdout.flush()

    # ── Precompute sufficient statistics ──────────────────────────────
    print("\nPrecomputing analytic sufficient statistics...")
    all_ss = {}
    all_tau_true = {}
    for topo in ALL_TOPOS:
        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
        all_ss[topo] = ss
        all_tau_true[topo] = get_tau_true(topo, ss)
        print(f"  {topo:<14} tau_true = {all_tau_true[topo]:.10f}")
    sys.stdout.flush()

    # ── Generate random confusion matrices ────────────────────────────
    print(f"\nGenerating {N_MATRICES:,} Dirichlet(1,1,1) C0 matrices...")
    sys.stdout.flush()
    rng = np.random.default_rng(SEED)
    all_C0 = np.zeros((N_MATRICES, K, K))
    for j in range(K):
        all_C0[:, :, j] = rng.dirichlet(np.ones(K), size=N_MATRICES)

    # ── Storage ───────────────────────────────────────────────────────
    ranking_topo_idx = {t: i for i, t in enumerate(RANKING_TOPOS)}
    n_rank = len(RANKING_TOPOS)
    asv_matrix = np.full((N_MATRICES, n_rank), np.nan)

    # Collider and M-bias: ASV = inf (protective)
    asv_matrix[:, ranking_topo_idx['collider']] = np.inf
    asv_matrix[:, ranking_topo_idx['mbias']] = np.inf

    worst_step_dev = {t: 0.0 for t in CONJECTURE_TOPOS}
    violation_count = {t: 0 for t in CONJECTURE_TOPOS}

    # ── Process topologies in chunks ──────────────────────────────────
    print(f"\nProcessing topologies (chunk_size={CHUNK_SIZE:,})...")
    sys.stdout.flush()

    n_chunks = (N_MATRICES + CHUNK_SIZE - 1) // CHUNK_SIZE

    for topo in ALL_TOPOS:
        t0 = time.time()
        ss = all_ss[topo]
        tau_true = all_tau_true[topo]

        need_asv = (topo in ranking_topo_idx and topo not in PROTECTIVE)
        need_conj = topo in CONJECTURE_TOPOS

        if not need_asv and not need_conj:
            continue

        topo_worst = 0.0
        topo_viol = 0

        for c in range(n_chunks):
            start = c * CHUNK_SIZE
            end = min(start + CHUNK_SIZE, N_MATRICES)
            C0_chunk = all_C0[start:end]

            if topo == 'iv':
                asv_vals = process_batch_iv(C0_chunk, ss, tau_true)
                if need_asv:
                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
                # No conjecture for IV
            elif topo == 'exposure':
                asv_vals, w_devs = process_batch_exposure(
                    C0_chunk, ss, tau_true)
                if need_asv:
                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
                if need_conj:
                    chunk_worst = float(w_devs.max())
                    topo_worst = max(topo_worst, chunk_worst)
                    topo_viol += int((w_devs > 0).sum())
            else:
                asv_vals, w_devs = process_batch_with_T(
                    C0_chunk, ss, tau_true, topo)
                if need_asv and asv_vals is not None:
                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
                if need_conj:
                    chunk_worst = float(w_devs.max())
                    topo_worst = max(topo_worst, chunk_worst)
                    topo_viol += int((w_devs > 0).sum())

            if (c + 1) % max(1, n_chunks // 5) == 0:
                elapsed = time.time() - t0
                frac = (c + 1) / n_chunks
                eta = elapsed / frac * (1 - frac)
                print(f"    {topo}: chunk {c+1}/{n_chunks} "
                      f"({elapsed:.0f}s, ~{eta:.0f}s left)")
                sys.stdout.flush()

        if need_conj:
            worst_step_dev[topo] = topo_worst
            violation_count[topo] = topo_viol

        elapsed = time.time() - t0
        extras = []
        if need_conj:
            extras.append(f"worst_dev={topo_worst:.2e}")
            extras.append(f"viol={topo_viol}")
        if need_asv and topo in ranking_topo_idx:
            col = asv_matrix[:, ranking_topo_idx[topo]]
            finite = col[np.isfinite(col)]
            if len(finite) > 0:
                extras.append(f"med_ASV={np.median(finite):.4f}")
        print(f"  {topo:<14} {elapsed:.1f}s  {', '.join(extras)}")
        sys.stdout.flush()

    # ── Part 1: Kendall tau ranking analysis ──────────────────────────
    print("\n" + "=" * 70)
    print("PART 1: ASV Topology Ranking Stability")
    print("=" * 70)

    theoretical_ranks = np.array([
        THEORETICAL_RANKING_ORDER.index(t) + 1 for t in RANKING_TOPOS
    ], dtype=float)

    # Vectorized Kendall tau for all valid matrices
    valid_mask = ~np.any(np.isnan(asv_matrix), axis=1)
    n_valid = int(valid_mask.sum())

    kendall_taus = np.full(N_MATRICES, np.nan)
    exact_match_count = 0

    if n_valid > 0:
        valid_asv = asv_matrix[valid_mask]
        emp_ranks = np.apply_along_axis(
            lambda x: rankdata(x, method='average'), 1, valid_asv)

        theo_order = np.argsort(theoretical_ranks)

        for idx in range(n_valid):
            tau_corr, _ = kendalltau(theoretical_ranks, emp_ranks[idx])
            orig_idx = np.where(valid_mask)[0][idx]
            kendall_taus[orig_idx] = tau_corr

            emp_order = np.argsort(emp_ranks[idx])
            if np.array_equal(theo_order, emp_order):
                exact_match_count += 1

    valid_taus = kendall_taus[~np.isnan(kendall_taus)]
    mean_tau = float(np.mean(valid_taus)) if len(valid_taus) > 0 else float('nan')
    min_tau = float(np.min(valid_taus)) if len(valid_taus) > 0 else float('nan')
    median_tau = float(np.median(valid_taus)) if len(valid_taus) > 0 else float('nan')
    exact_frac = exact_match_count / n_valid if n_valid > 0 else 0.0

    print(f"  Valid rankings: {n_valid:,} / {N_MATRICES:,}")
    print(f"  Kendall tau:")
    print(f"    Mean:   {mean_tau:.4f}")
    print(f"    Median: {median_tau:.4f}")
    print(f"    Min:    {min_tau:.4f}")
    print(f"  Exact match: {exact_match_count:,}/{n_valid:,} ({exact_frac:.6f})")

    tau_dist = {}
    for t in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        frac = float(np.mean(valid_taus >= t)) if len(valid_taus) > 0 else 0.0
        tau_dist[f"ge_{t:.1f}"] = frac
        print(f"    tau >= {t:.1f}: {frac:.4f}")
    sys.stdout.flush()

    # ── Part 2: epsilon-perturbation ranking robustness ───────────────
    print("\n" + "=" * 70)
    print(f"PART 2: Perturbation Robustness (eps={PERTURB_EPSILON})")
    print("=" * 70)

    # Vectorized: for each valid matrix, check all pairs
    n_reversals = 0
    n_pair_reversals = 0
    n_checked = n_valid
    n_pairs_per = n_rank * (n_rank - 1) // 2
    n_pairs_total = n_checked * n_pairs_per

    if n_valid > 0:
        valid_asv = asv_matrix[valid_mask]
        for a in range(n_rank):
            for b in range(a + 1, n_rank):
                va = valid_asv[:, a]
                vb = valid_asv[:, b]
                # Both inf => no reversal
                both_inf = np.isinf(va) & np.isinf(vb)
                gap = np.abs(va - vb)
                pair_rev = (~both_inf) & (gap < 2 * PERTURB_EPSILON)
                n_pair_reversals += int(pair_rev.sum())

        # Count matrices with any reversal
        has_reversal = np.zeros(n_valid, dtype=bool)
        for a in range(n_rank):
            for b in range(a + 1, n_rank):
                va = valid_asv[:, a]
                vb = valid_asv[:, b]
                both_inf = np.isinf(va) & np.isinf(vb)
                gap = np.abs(va - vb)
                has_reversal |= (~both_inf) & (gap < 2 * PERTURB_EPSILON)
        n_reversals = int(has_reversal.sum())

    rev_frac = n_reversals / n_checked if n_checked > 0 else 0.0
    pair_rev_frac = (n_pair_reversals / n_pairs_total
                     if n_pairs_total > 0 else 0.0)

    print(f"  Matrices checked: {n_checked:,}")
    print(f"  Any pairwise reversal: {n_reversals:,}/{n_checked:,} "
          f"({rev_frac:.4f})")
    print(f"  Pairwise reversals: {n_pair_reversals:,}/{n_pairs_total:,} "
          f"({pair_rev_frac:.4f})")
    sys.stdout.flush()

    # ── Part 3: Conjecture verification ───────────────────────────────
    print("\n" + "=" * 70)
    print("PART 3: Conjecture Verification (non-IV topologies)")
    print("=" * 70)

    global_worst = 0.0
    global_worst_topo = None
    total_viol = 0

    for topo in CONJECTURE_TOPOS:
        dev = worst_step_dev[topo]
        viol = violation_count[topo]
        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
        total_viol += viol
        print(f"  {topo:<14} [{direction}]  worst_dev={dev:.6e}  "
              f"violations={viol:,}/{N_MATRICES:,}")
        if dev > global_worst:
            global_worst = dev
            global_worst_topo = topo

    print(f"\n  Global worst step deviation: {global_worst:.6e} "
          f"({global_worst_topo})")
    conj_holds = global_worst < 0.06
    print(f"  Conjecture holds (worst_dev < 0.06)? {conj_holds}")
    sys.stdout.flush()

    # ── ASV summary ───────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("ASV Summary (per topology)")
    print("=" * 70)
    asv_summary = {}
    for topo in RANKING_TOPOS:
        col = asv_matrix[:, ranking_topo_idx[topo]]
        finite = col[np.isfinite(col) & ~np.isnan(col)]
        pct_inf = float(np.mean(np.isinf(col) & (col > 0)) * 100)
        pct_nan = float(np.mean(np.isnan(col)) * 100)
        if len(finite) > 0:
            med = float(np.median(finite))
            mn = float(np.mean(finite))
            print(f"  {topo:<14} median={med:.4f}  mean={mn:.4f}  "
                  f"immune={pct_inf:.1f}%  NaN={pct_nan:.1f}%")
            asv_summary[topo] = {
                "median": med, "mean": mn,
                "pct_immune": pct_inf, "pct_nan": pct_nan
            }
        else:
            print(f"  {topo:<14} all inf/NaN  immune={pct_inf:.1f}%  "
                  f"NaN={pct_nan:.1f}%")
            asv_summary[topo] = {
                "median": None, "mean": None,
                "pct_immune": pct_inf, "pct_nan": pct_nan
            }
    sys.stdout.flush()

    # ── Save results ──────────────────────────────────────────────────
    total_time = time.time() - t_total

    results = {
        "description": "ASV topology ranking stability analysis",
        "config": {
            "n_matrices": N_MATRICES,
            "K": K,
            "asv_threshold": ASV_EPSILON,
            "perturbation_epsilon": PERTURB_EPSILON,
            "delta_step": DELTA_STEP,
            "n_delta": N_DELTA,
            "gh_quadrature_points": N_GH,
            "mono_tol": MONO_TOL,
            "seed": SEED,
            "theoretical_ranking": THEORETICAL_RANKING_ORDER,
        },
        "part1_ranking_stability": {
            "n_valid_rankings": n_valid,
            "kendall_tau_mean": mean_tau,
            "kendall_tau_median": median_tau,
            "kendall_tau_min": min_tau,
            "exact_match_count": exact_match_count,
            "exact_match_fraction": exact_frac,
            "tau_distribution": tau_dist,
        },
        "part2_perturbation_robustness": {
            "n_checked": n_checked,
            "n_reversals": n_reversals,
            "reversal_fraction": rev_frac,
            "n_pair_reversals": n_pair_reversals,
            "n_pairs_total": n_pairs_total,
            "pair_reversal_fraction": pair_rev_frac,
        },
        "part3_conjecture_verification": {
            "global_worst_step_deviation": global_worst,
            "global_worst_topology": global_worst_topo,
            "conjecture_holds_0_06": conj_holds,
            "per_topology": {
                topo: {
                    "worst_step_deviation": worst_step_dev[topo],
                    "violation_count": violation_count[topo],
                    "direction": ("non-dec" if topo in NON_DECREASING
                                  else "non-inc"),
                }
                for topo in CONJECTURE_TOPOS
            },
        },
        "asv_summary": asv_summary,
        "total_time_seconds": total_time,
    }

    out_path = os.path.join(OUT_DIR, 'ranking_stability_results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON saved: {out_path}")

    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Kendall tau: mean={mean_tau:.4f}, median={median_tau:.4f}, "
          f"min={min_tau:.4f}")
    print(f"  Exact ranking match: {exact_frac:.6f}")
    print(f"  Reversal rate (eps={PERTURB_EPSILON}): {rev_frac:.4f}")
    print(f"  Worst |B| step deviation: {global_worst:.6e} "
          f"({global_worst_topo})")
    print(f"  Conjecture holds: {conj_holds}")
    print(f"  Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
