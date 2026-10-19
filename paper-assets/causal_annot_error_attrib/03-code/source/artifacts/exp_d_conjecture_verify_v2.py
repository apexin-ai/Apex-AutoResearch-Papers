#!/usr/bin/env python3
"""
Exp-D v2: Conjecture 1 verification with ANALYTIC plim (zero sampling noise).

The original exp_d_conjecture_verify.py computed plim via sufficient statistics
estimated from N=5M Monte Carlo simulation, introducing O(1/sqrt(N)) ~ 0.0004
sampling noise. At MONO_TOL=1e-8, this generated ~141k false monotonicity
violations.

This v2 computes ALL sufficient statistics analytically (closed-form for
confounding/mediation/exposure, Gauss-Hermite quadrature for collider/mbias/
frontdoor/iv), eliminating sampling noise entirely.

Topology-specific analytics:
  - confounding: fully analytic (categorical A, linear T and Y)
  - exposure:    fully analytic (categorical A, linear Y)
  - mediation:   fully analytic (binary T, softmax A|T, linear Y)
  - collider:    2D Gauss-Hermite over (T, eps_Y), both N(0,1)
  - mbias:       2D Gauss-Hermite over (U1, U2), both N(0,1)
  - frontdoor:   1D Gauss-Hermite over T ~ N(0, alpha_U^2 + 1)
  - iv:          1D Gauss-Hermite over U ~ N(0,1), with binary Z

Output: exp_d_conjecture_results_v2.json (same structure as v1)
"""

import numpy as np
import json
import time
import sys
import os
from scipy.special import roots_hermite, softmax as scipy_softmax
from scipy.optimize import minimize as scipy_minimize

# ====================================================================
# Gauss-Hermite quadrature setup
# ====================================================================
N_GH = 100  # points per dimension -- machine precision for smooth integrands

# roots_hermite: physicist's convention, weight = exp(-x^2)
# integral f(x) exp(-x^2) dx ~ sum w_i f(x_i)
# For N(0,1) expectation: E[f(X)] = (1/sqrt(pi)) sum w_i f(x_i * sqrt(2))
_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
GH_X = _gh_x_raw * np.sqrt(2)   # rescaled nodes for N(0,1)
GH_W = _gh_w_raw / np.sqrt(np.pi)  # rescaled weights: sum w_i f(x_i) = E_{N(0,1)}[f]

# Verify: E[1] should be 1.0, E[X^2] should be 1.0
assert abs(GH_W.sum() - 1.0) < 1e-12, f"GH weights sum to {GH_W.sum()}, expected 1.0"
assert abs((GH_W * GH_X**2).sum() - 1.0) < 1e-10, "GH E[X^2] != 1.0"

# 2D quadrature: outer product of 1D grids
GH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')  # (N_GH, N_GH)
GH_W2 = np.outer(GH_W, GH_W)  # (N_GH, N_GH)
GH_X2_a_flat = GH_X2_a.ravel()
GH_X2_b_flat = GH_X2_b.ravel()
GH_W2_flat = GH_W2.ravel()

# ====================================================================
# Configuration
# ====================================================================
K_VALUES = [3, 5, 7]
K_ADVERSARIAL = [3, 5]
N_RANDOM = 10_000
DELTA_STEP = 0.01
SEED = 12345
MONO_TOL = 1e-12  # much tighter than v1's 1e-8 since we have zero sampling noise

ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'iv', 'frontdoor']
TOPO_IDX = {t: i for i, t in enumerate(ALL_TOPOS)}
NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
NON_INCREASING = {'collider', 'mbias'}

ADV_DELTA_PAIRS = [(0.0, 0.2), (0.0, 0.5), (0.1, 0.3), (0.2, 0.5), (0.3, 0.7)]
ADV_N_STARTS = 100

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ====================================================================
# DGP Parameter Pools (identical to v1)
# ====================================================================
_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
_MBIAS_A1_POOL = [0.0, 0.8, -0.5, 0.6, -0.4, 0.5, -0.3]
_MBIAS_A2_POOL = [0.0, 0.6, 0.9, -0.4, 0.7, -0.3, 0.5]
_IV_DZ_POOL = [0.0, 1.0, -0.5, 0.8, -0.4, 0.6, -0.3]
_IV_DU_POOL = [0.0, 0.8, 0.6, -0.5, 0.7, -0.3, 0.4]
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
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),
                         beta_A=np.array(_BETA_A_POOL[:K - 1]), beta_T=2.0, sigma_T=1.0),
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


# ====================================================================
# Stable softmax utility
# ====================================================================
def _softmax(logits):
    """Softmax along last axis, numerically stable."""
    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)


# ====================================================================
# Analytic Sufficient Statistics classes
# ====================================================================
class AnalyticSuffStats:
    """Population moments for OLS topologies (with or without T)."""
    def __init__(self, K, has_T=True):
        self.K = K
        self.has_T = has_T
        self.p_A = None   # K-vector: P(A=k)
        self.E_Y = None   # scalar
        self.E_YD = None  # K-vector: E[Y * 1(A=k)]
        if has_T:
            self.E_T = None   # scalar
            self.E_T2 = None  # scalar: E[T^2]
            self.E_TY = None  # scalar: E[T*Y]
            self.E_TD = None  # K-vector: E[T * 1(A=k)]


class AnalyticIVSuffStats:
    """Population moments for IV topology (Wald estimator)."""
    def __init__(self, K):
        self.K = K
        self.RF = None   # E[Y|Z=1] - E[Y|Z=0]
        self.FS = None   # K-vector: P(A=k|Z=1) - P(A=k|Z=0)


# ====================================================================
# Topology 1: Confounding -- FULLY ANALYTIC
# ====================================================================
# DGP: A ~ Cat(p_A), T = sum_{j=1}^{K-1} alpha_j D_j + eps_T,
#       Y = beta_T * T + sum_{j=1}^{K-1} beta_A_j D_j + eps_Y
# D_j = 1(A=j+1) for j=0,...,K-2 (ref category A=0)
# Wait -- looking at original code more carefully:
#   D[:, j] = (A == j + 1) for j in range(K-1)
# So D_j = 1(A = j+1), j=0,...,K-2
# T = D @ alpha + eps_T = sum_{j=0}^{K-2} alpha_j * 1(A=j+1) + eps_T
# Y = beta_T * T + D @ beta_A + eps_Y = beta_T * T + sum_{j=0}^{K-2} beta_A_j * 1(A=j+1) + eps_Y
#
# For the plim regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}:
# D*_j = 1(A* = j) for j=1,...,K-1 (ref category A*=0)
# The sufficient stats use A (not A*), and the C matrix maps A->A*.
# Actually looking at the SuffStats class: DA[:, k] = (A == k) for k=0,...,K-1
# So p_A[k] = P(A=k), E_TD[k] = E[T * 1(A=k)], E_YD[k] = E[Y * 1(A=k)]

def compute_confounding_ss(K, p):
    """Analytic sufficient stats for confounding topology."""
    ss = AnalyticSuffStats(K, has_T=True)
    p_A = p['p_A']       # K-vector
    alpha = p['alpha']    # (K-1)-vector: alpha_0,...,alpha_{K-2}
    beta_A = p['beta_A']  # (K-1)-vector
    beta_T = p['beta_T']
    sigma_T = p['sigma_T']

    ss.p_A = p_A.copy()

    # E[T] = sum_{j=0}^{K-2} alpha_j * P(A=j+1)
    # (since eps_T has mean 0)
    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))

    # E[T^2] = E[(sum alpha_j D_j)^2] + sigma_T^2
    # = sum_j alpha_j^2 P(A=j+1) + sigma_T^2
    # (since D_j D_k = 0 for j!=k, D_j^2 = D_j)
    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2

    # E[T * 1(A=k)]:
    # For k=0: E[(sum alpha_j D_j + eps_T) * 1(A=0)]
    #        = sum_j alpha_j E[D_j * 1(A=0)] + E[eps_T * 1(A=0)]
    #        = 0 + 0 = 0  (since D_j=1(A=j+1) and A=0 => D_j=0, and eps_T indep of A)
    # Actually eps_T is independent of A, so E[eps_T * 1(A=k)] = 0 * P(A=k) = 0
    # For k>=1: E[(sum_j alpha_j D_j + eps_T) * 1(A=k)]
    #         = alpha_{k-1} * P(A=k) + 0
    ss.E_TD = np.zeros(K)
    for k in range(1, K):
        ss.E_TD[k] = alpha[k - 1] * p_A[k]

    # E[Y] = beta_T * E[T] + sum_{j=0}^{K-2} beta_A_j * P(A=j+1)
    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))

    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + sum_j beta_A_j * E[D_j * 1(A=k)] + E[eps_Y * 1(A=k)]
    # E[D_j * 1(A=k)] = P(A=j+1, A=k) = P(A=k) if j+1=k else 0
    # E[eps_Y * 1(A=k)] = 0
    # So for k=0: E[Y * 1(A=0)] = beta_T * 0 + 0 + 0 = 0 ... wait that's wrong
    # Actually: Y = beta_T * T + sum beta_A_j D_j + eps_Y
    # E[Y * 1(A=0)] = beta_T * E[T * 1(A=0)] + sum_j beta_A_j * E[D_j * 1(A=0)] + E[eps_Y * 1(A=0)]
    #               = beta_T * 0 + 0 + 0 = 0
    # Hmm, that gives E_Y = sum_k E[Y * 1(A=k)] = 0 + sum_{k>=1} stuff, but we need E_Y correctly.
    # Let me reconsider: the intercept in the Y equation.
    # gen_confounding: Y = beta_T * T + D @ beta_A + eps_Y
    # There's no explicit intercept in Y. So E[Y | A=0] = beta_T * E[T | A=0] + 0
    # E[T | A=0] = 0 (since all alpha terms vanish) + E[eps_T] = 0
    # So E[Y * 1(A=0)] = E[Y | A=0] * P(A=0) = 0 * p_A[0] = 0
    # That seems correct.

    # For k >= 1:
    # E[Y * 1(A=k)] = beta_T * E[T * 1(A=k)] + beta_A[k-1] * P(A=k)
    ss.E_YD = np.zeros(K)
    for k in range(1, K):
        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]
    # k=0: already 0

    # E[TY] = E[T * (beta_T * T + sum beta_A_j D_j + eps_Y)]
    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * D_j] + E[T * eps_Y]
    #        = beta_T * E[T^2] + sum_j beta_A_j * E[T * 1(A=j+1)] + 0
    ss.E_TY = beta_T * ss.E_T2 + sum(beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))

    return ss


# ====================================================================
# Topology 2: Exposure -- FULLY ANALYTIC
# ====================================================================
# DGP: A ~ Cat(p_A), Y = beta[0] + D @ beta[1:] + eps_Y
# No T variable.

def compute_exposure_ss(K, p):
    """Analytic sufficient stats for exposure topology."""
    ss = AnalyticSuffStats(K, has_T=False)
    p_A = p['p_A']
    beta = p['beta']  # K-vector: beta[0] is intercept

    ss.p_A = p_A.copy()

    # E[Y] = beta[0] + sum_{j=1}^{K-1} beta[j] * P(A=j)
    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))

    # E[Y * 1(A=k)] = E[(beta[0] + sum_j beta[j] D_j + eps_Y) * 1(A=k)]
    # = beta[0] * P(A=k) + beta[k] * P(A=k) (if k>=1) + 0
    # For k=0: = beta[0] * P(A=0) + 0 = beta[0] * p_A[0]
    ss.E_YD = np.zeros(K)
    ss.E_YD[0] = beta[0] * p_A[0]
    for k in range(1, K):
        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]

    return ss


# ====================================================================
# Topology 3: Mediation -- FULLY ANALYTIC (T is binary)
# ====================================================================
# DGP: T ~ Bern(0.5), A | T ~ Cat(softmax(gamma + delta * T))
#       Y = beta[0] + D @ beta[1:] + tau * T + eps_Y
# D_j = 1(A = j+1) for j=0,...,K-2

def compute_mediation_ss(K, p):
    """Analytic sufficient stats for mediation topology."""
    ss = AnalyticSuffStats(K, has_T=True)
    tau = p['tau']
    gamma = p['gamma']  # K-vector
    delta_coef = p['delta']   # K-vector
    beta = p['beta']    # K-vector

    # P(A=k | T=t) = softmax(gamma + delta * t)[k]
    probs_T0 = _softmax(gamma)          # K-vector
    probs_T1 = _softmax(gamma + delta_coef)  # K-vector

    # P(A=k) = 0.5 * P(A=k|T=0) + 0.5 * P(A=k|T=1)
    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1

    # E[T] = 0.5, E[T^2] = 0.5 (since T is Bernoulli(0.5))
    ss.E_T = 0.5
    ss.E_T2 = 0.5

    # E[T * 1(A=k)] = E[T * 1(A=k)]
    # = 0.5 * 0 * P(A=k|T=0) + 0.5 * 1 * P(A=k|T=1)
    # = 0.5 * probs_T1[k]
    ss.E_TD = 0.5 * probs_T1

    # E[Y] = beta[0] + sum_{k=1}^{K-1} beta[k] * P(A=k) + tau * E[T]
    # Wait, gen_mediation:
    #   Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + eps_Y
    # D_j = 1(A=j+1), so D @ beta[1:] = sum_{j=0}^{K-2} beta[j+1] * 1(A=j+1)
    # = sum_{k=1}^{K-1} beta[k] * 1(A=k)
    ss.E_Y = beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K)) + tau * 0.5

    # E[Y * 1(A=k)] for each k:
    # Y = beta[0] + sum_j beta[j+1]*D_j + tau*T + eps_Y
    # E[Y * 1(A=k)] = E[(beta[0] + beta[k]*1(k>=1) + tau*T + eps_Y) * 1(A=k)]
    # = (beta[0] + beta[k]*(k>=1)) * P(A=k) + tau * E[T * 1(A=k)]

    ss.E_YD = np.zeros(K)
    for k in range(K):
        beta_k = beta[k] if k >= 1 else 0.0
        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]

    # E[TY] = E[T * (beta[0] + sum beta[k]*1(A=k) + tau*T + eps_Y)]
    # = beta[0] * E[T] + sum_{k=1}^{K-1} beta[k] * E[T * 1(A=k)] + tau * E[T^2] + 0
    ss.E_TY = beta[0] * 0.5 + sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + tau * 0.5

    return ss


# ====================================================================
# Topology 4: Collider -- 2D GAUSS-HERMITE
# ====================================================================
# DGP: T ~ N(0,1), eps_Y ~ N(0,1) independent
#       Y = tau * T + eps_Y
#       A | T, Y ~ Cat(softmax(g + dT * T + dY * Y))
#
# Reparametrize: let Z1=T, Z2=eps_Y, both N(0,1) independent
# Y = tau * Z1 + Z2
# A | Z1, Z2 ~ Cat(softmax(g + dT * Z1 + dY * (tau * Z1 + Z2)))
#            = Cat(softmax(g + (dT + tau * dY) * Z1 + dY * Z2))

def compute_collider_ss(K, p):
    """Analytic sufficient stats for collider via 2D GH quadrature."""
    ss = AnalyticSuffStats(K, has_T=True)
    tau = p['tau']
    g = p['g']      # K-vector
    dT = p['dT']    # K-vector
    dY = p['dY']    # K-vector

    # Quadrature over (Z1, Z2) = (T, eps_Y), both N(0,1)
    # Logits for each quadrature point: g + (dT + tau*dY) * Z1 + dY * Z2
    coeff1 = dT + tau * dY   # K-vector: coefficient of Z1
    coeff2 = dY               # K-vector: coefficient of Z2

    # Compute softmax probabilities at each quadrature point
    # logits shape: (N_GH^2, K)
    logits = (g[None, :]
              + coeff1[None, :] * GH_X2_a_flat[:, None]
              + coeff2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)  # (N_GH^2, K)

    # T = Z1, Y = tau * Z1 + Z2
    T_vals = GH_X2_a_flat
    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat

    # Weighted expectations
    w = GH_W2_flat  # (N_GH^2,)

    ss.p_A = (w[:, None] * probs).sum(axis=0)
    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)

    # Moments of T and Y (independent of A, can compute analytically):
    ss.E_T = 0.0
    ss.E_T2 = 1.0
    ss.E_Y = 0.0  # E[tau*T + eps] = 0
    ss.E_TY = tau  # E[T(tau*T + eps)] = tau * E[T^2] = tau

    return ss


# ====================================================================
# Topology 5: M-bias -- 2D GAUSS-HERMITE
# ====================================================================
# DGP: U1, U2 ~ N(0,1) independent
#       T = delta_coef * U1 + eta, eta ~ N(0,1)
#       Y = tau * T + lam * U2 + eps_Y, eps_Y ~ N(0,1)
#       A | U1, U2 ~ Cat(softmax(g + a1 * U1 + a2 * U2))
#
# Note: T and Y depend on (U1, U2, eta, eps_Y) but A only depends on (U1, U2).
# Since eta, eps_Y are independent of (U1, U2, A):
#   E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)] + E[eta * 1(A=k)]
#                  = delta_coef * E[U1 * 1(A=k)]  (eta indep of A)
#
#   E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)] + 0
#
# So we need 2D GH over (U1, U2) to compute:
#   P(A=k), E[U1 * 1(A=k)], E[U2 * 1(A=k)]

def compute_mbias_ss(K, p):
    """Analytic sufficient stats for M-bias via 2D GH quadrature."""
    ss = AnalyticSuffStats(K, has_T=True)
    tau = p['tau']
    delta_coef = p['delta_coef']
    lam = p['lam']
    g = p['g']
    a1 = p['a1']
    a2 = p['a2']

    # Logits: g + a1 * U1 + a2 * U2
    logits = (g[None, :]
              + a1[None, :] * GH_X2_a_flat[:, None]
              + a2[None, :] * GH_X2_b_flat[:, None])
    probs = _softmax(logits)  # (N_GH^2, K)

    w = GH_W2_flat
    U1_vals = GH_X2_a_flat
    U2_vals = GH_X2_b_flat

    ss.p_A = (w[:, None] * probs).sum(axis=0)
    E_U1_Dk = (w[:, None] * U1_vals[:, None] * probs).sum(axis=0)  # E[U1 * 1(A=k)]
    E_U2_Dk = (w[:, None] * U2_vals[:, None] * probs).sum(axis=0)  # E[U2 * 1(A=k)]

    # E[T * 1(A=k)] = delta_coef * E[U1 * 1(A=k)]
    ss.E_TD = delta_coef * E_U1_Dk

    # E[Y * 1(A=k)] = tau * E[T * 1(A=k)] + lam * E[U2 * 1(A=k)]
    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk

    # Marginal moments:
    # E[T] = 0 (since E[U1]=0, E[eta]=0)
    # E[T^2] = delta_coef^2 * E[U1^2] + E[eta^2] = delta_coef^2 + 1
    # E[Y] = 0
    # E[TY] = tau * E[T^2] + lam * E[T*U2]
    # E[T*U2] = E[(delta_coef * U1 + eta) * U2] = 0 (all independent)
    ss.E_T = 0.0
    ss.E_T2 = delta_coef**2 + 1.0
    ss.E_Y = 0.0
    ss.E_TY = tau * ss.E_T2

    return ss


# ====================================================================
# Topology 6: Front-door -- 1D GAUSS-HERMITE
# ====================================================================
# DGP: U ~ N(0,1), T = alpha_U * U + eta (eta ~ N(0,1))
#       M | T ~ Cat(softmax(gamma + delta * T))  -- M is the "annotator" variable
#       Y = D_M @ beta[1:] + lam_U * U + eps_Y
# where D_M[j] = 1(M=j+1), j=0,...,K-2
#
# The regression is Y ~ 1 + T + D*_1 + ... + D*_{K-1}
# (M plays the role of A in the plim computation)
#
# T ~ N(0, sigma_T^2) where sigma_T^2 = alpha_U^2 + 1
# We do 1D GH over T (after rescaling for its variance).
#
# For the moments involving U:
# E[U | T] = Cov(U,T)/Var(T) * T = alpha_U / (alpha_U^2 + 1) * T
# (since Cov(U,T) = alpha_U, Var(T) = alpha_U^2 + 1)
#
# P(M=k) = E_T[softmax(gamma + delta * T)[k]]
# E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]
# E[Y * 1(M=k)] = E[E[Y | T, M] * 1(M=k)]
#               = E_T[ E[Y|T,M=k] * softmax(gamma+delta*T)[k] ]
# E[Y|T,M=k] = beta[k] (if k>=1, else 0 for the intercept part from D_M)
#              + lam_U * E[U|T] + 0
# Wait, let me reconsider:
# Y = sum_{j=0}^{K-2} beta[j+1] * 1(M=j+1) + lam_U * U + eps_Y
# (from gen_frontdoor: Y = D @ beta[1:] + lam_U * U + eps_Y,
#  where beta = p['beta'] and D[j] = 1(M=j+1))
# There's no intercept beta[0] in the Y equation in gen_frontdoor!
# Let me re-check: gen_frontdoor has Y = D @ p['beta'][1:] + p['lam_U'] * U + eps_Y
# So Y = sum_{k=1}^{K-1} beta[k] * 1(M=k) + lam_U * U + eps_Y
#
# E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)] + 0
# For k=0: E[Y * 1(M=0)] = 0 + lam_U * E[U * 1(M=0)] + 0

def compute_frontdoor_ss(K, p):
    """Analytic sufficient stats for front-door via 1D GH quadrature."""
    ss = AnalyticSuffStats(K, has_T=True)
    alpha_U = p['alpha_U']
    lam_U = p['lam_U']
    gamma = p['gamma']
    delta_coef = p['delta']
    beta = p['beta']

    sigma_T2 = alpha_U**2 + 1.0
    sigma_T = np.sqrt(sigma_T2)

    # 1D GH over T ~ N(0, sigma_T^2): rescale nodes
    T_nodes = GH_X * sigma_T  # (N_GH,)
    T_weights = GH_W          # (N_GH,) -- already normalized for E_{N(0,1)}

    # softmax(gamma + delta * T) at each T node
    # logits shape: (N_GH, K)
    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
    probs = _softmax(logits)  # (N_GH, K)

    # P(M=k) = E_T[softmax(gamma + delta * T)[k]]
    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)

    # E[T * 1(M=k)] = E_T[T * softmax(gamma + delta * T)[k]]
    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)

    # E[U * 1(M=k)] via the law of iterated expectations:
    # E[U * 1(M=k)] = E_T[ E[U|T] * P(M=k|T) ]
    # E[U|T] = alpha_U / sigma_T^2 * T
    E_U_given_T = alpha_U / sigma_T2 * T_nodes  # (N_GH,)
    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)

    # E[Y * 1(M=k)] = beta[k] * P(M=k) (for k>=1) + lam_U * E[U * 1(M=k)]
    ss.E_YD = np.zeros(K)
    for k in range(K):
        beta_k = beta[k] if k >= 1 else 0.0
        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]

    # Marginal moments:
    # E[T] = 0
    # E[T^2] = sigma_T^2
    # E[Y] = sum_{k=1}^{K-1} beta[k] * P(M=k) + lam_U * E[U] + 0
    #       = sum_{k=1}^{K-1} beta[k] * P(M=k)
    ss.E_T = 0.0
    ss.E_T2 = sigma_T2
    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))

    # E[TY] = sum_{k=1}^{K-1} beta[k] * E[T * 1(M=k)] + lam_U * E[T*U] + E[T*eps_Y]
    # E[T*U] = Cov(T,U) = alpha_U (since both mean 0)
    # E[T*eps_Y] = 0
    ss.E_TY = sum(beta[k] * ss.E_TD[k] for k in range(1, K)) + lam_U * alpha_U

    return ss


# ====================================================================
# Topology 7: IV -- 1D GAUSS-HERMITE over U, binary Z
# ====================================================================
# DGP: Z ~ Bern(0.5), U ~ N(0,1), eps_Y ~ N(0,1)
#       A | Z, U ~ Cat(softmax(g + dZ * Z + dU * U))
#       Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps_Y
#
# Wald estimator: tau_hat = RF / FS*[1]
# RF = E[Y|Z=1] - E[Y|Z=0]
# FS[k] = P(A=k|Z=1) - P(A=k|Z=0)
#
# P(A=k|Z=z) = E_U[softmax(g + dZ * z + dU * U)[k]]
# E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z) + lam * E[U] + E[eps]
#           = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)

def compute_iv_ss(K, p):
    """Analytic sufficient stats for IV via 1D GH quadrature."""
    ivss = AnalyticIVSuffStats(K)
    g = p['g']
    dZ = p['dZ']
    dU = p['dU']
    beta = p['beta']
    lam = p['lam']

    # P(A=k|Z=z) for z=0 and z=1
    # logits for Z=0: g + dU * U
    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]  # (N_GH, K)
    probs_z0 = _softmax(logits_z0)
    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)  # K-vector

    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]
    probs_z1 = _softmax(logits_z1)
    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)  # K-vector

    # First stage
    ivss.FS = P_A_z1 - P_A_z0  # K-vector

    # Reduced form
    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)
    # (lam * E[U] = 0, E[eps] = 0, beta[0] cancels out since it's not in gen_iv)
    # Actually gen_iv: Y = D @ p['beta'][1:] + p['lam'] * U + eps
    # So Y = sum_{k=1}^{K-1} beta[k] * 1(A=k) + lam * U + eps
    # E[Y|Z=z] = sum_{k=1}^{K-1} beta[k] * P(A=k|Z=z)
    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))
    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))

    ivss.RF = E_Y_z1 - E_Y_z0

    return ivss


# ====================================================================
# Plim computation (from original, unchanged)
# ====================================================================
def plim_ols_with_T(C, ss):
    """Plim of OLS regression Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
    K = ss.K
    q = C @ ss.p_A        # misclassified P(A*=k)
    ct = C @ ss.E_TD       # E[T * 1(A*=k)]
    cy = C @ ss.E_YD       # E[Y * 1(A*=k)]
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
    try:
        return np.linalg.solve(EZZ, EZY)
    except np.linalg.LinAlgError:
        return np.full(dim, np.nan)


def plim_ols_exposure(C, ss):
    """Plim of OLS regression Y ~ 1 + D*_1 + ... + D*_{K-1}."""
    K = ss.K
    q = C @ ss.p_A
    cy = C @ ss.E_YD
    dim = K
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    EZZ[0, 1:] = q[1:]
    EZZ[1:, 0] = q[1:]
    for j in range(K - 1):
        EZZ[j + 1, j + 1] = q[j + 1]
    EZY = np.zeros(dim)
    EZY[0] = ss.E_Y
    EZY[1:] = cy[1:]
    try:
        return np.linalg.solve(EZZ, EZY)
    except np.linalg.LinAlgError:
        return np.full(dim, np.nan)


def plim_iv_single(C, ss):
    """Plim of Wald IV estimator with misclassified A."""
    FS_star = C @ ss.FS
    if abs(FS_star[1]) < 1e-15:
        return np.nan
    return ss.RF / FS_star[1]


def get_tau_at_C(topo, C, ss):
    if topo == 'iv':
        return plim_iv_single(C, ss)
    elif topo == 'exposure':
        return plim_ols_exposure(C, ss)[1]
    else:
        return plim_ols_with_T(C, ss)[1]


def get_tau_true(topo, K, params, ss):
    """True causal parameter.

    For correctly-identified topologies: tau_true = plim(I).
    For protective topologies (collider, mbias): tau_true = DGP tau,
    so B(0) = plim(I) - tau != 0 (existing bias from Berkson/M-bias).
    """
    p = params[topo]
    if topo == 'collider':
        return p['tau']
    elif topo == 'mbias':
        return p['tau']
    else:
        return get_tau_at_C(topo, np.eye(K), ss)


# ====================================================================
# Batched bias curve computation (from original, unchanged)
# ====================================================================
def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
    K = C0.shape[0]
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        delta_max = 10.0
    else:
        delta_max = min(1.0 / (1.0 - min_diag), 10.0)

    deltas = np.arange(0, delta_max + delta_step / 2, delta_step)
    n = len(deltas)
    d = deltas[:, None]

    if topo == 'iv':
        FS0 = C0 @ ss.FS
        fs_star = (1 - d) * ss.FS[None, :] + d * FS0[None, :]
        denom = fs_star[:, 1]
        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
    elif topo == 'exposure':
        pA0 = C0 @ ss.p_A
        YD0 = C0 @ ss.E_YD
        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
        dim = K
        EZZ = np.zeros((n, dim, dim))
        EZZ[:, 0, 0] = 1.0
        EZZ[:, 0, 1:] = q[:, 1:]
        EZZ[:, 1:, 0] = q[:, 1:]
        for j in range(K - 1):
            EZZ[:, j + 1, j + 1] = q[:, j + 1]
        EZY = np.zeros((n, dim))
        EZY[:, 0] = ss.E_Y
        EZY[:, 1:] = cy[:, 1:]
        try:
            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
            taus = coefs[:, 1]
        except np.linalg.LinAlgError:
            taus = np.full(n, np.nan)
    else:
        pA0 = C0 @ ss.p_A
        TD0 = C0 @ ss.E_TD
        YD0 = C0 @ ss.E_YD
        q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
        ct = (1 - d) * ss.E_TD[None, :] + d * TD0[None, :]
        cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
        dim = K + 1
        EZZ = np.zeros((n, dim, dim))
        EZZ[:, 0, 0] = 1.0
        EZZ[:, 0, 1] = ss.E_T
        EZZ[:, 1, 0] = ss.E_T
        EZZ[:, 1, 1] = ss.E_T2
        EZZ[:, 0, 2:] = q[:, 1:]
        EZZ[:, 2:, 0] = q[:, 1:]
        EZZ[:, 1, 2:] = ct[:, 1:]
        EZZ[:, 2:, 1] = ct[:, 1:]
        for j in range(K - 1):
            EZZ[:, j + 2, j + 2] = q[:, j + 1]
        EZY = np.zeros((n, dim))
        EZY[:, 0] = ss.E_Y
        EZY[:, 1] = ss.E_TY
        EZY[:, 2:] = cy[:, 1:]
        try:
            coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
            taus = coefs[:, 1]
        except np.linalg.LinAlgError:
            taus = np.full(n, np.nan)

    bias_abs = np.abs(taus - tau_true)
    return deltas, bias_abs


def check_monotonicity(bias_abs, topo, tol=MONO_TOL):
    valid = ~np.isnan(bias_abs)
    ba = bias_abs[valid]
    if len(ba) < 2:
        return 0
    diffs = np.diff(ba)
    if topo in NON_DECREASING:
        return int(np.sum(diffs < -tol))
    else:
        return int(np.sum(diffs > tol))


# ====================================================================
# Precompute analytic sufficient statistics
# ====================================================================
_COMPUTE_SS = {
    'confounding': lambda K, p: compute_confounding_ss(K, p),
    'mediation':   lambda K, p: compute_mediation_ss(K, p),
    'collider':    lambda K, p: compute_collider_ss(K, p),
    'exposure':    lambda K, p: compute_exposure_ss(K, p),
    'mbias':       lambda K, p: compute_mbias_ss(K, p),
    'iv':          lambda K, p: compute_iv_ss(K, p),
    'frontdoor':   lambda K, p: compute_frontdoor_ss(K, p),
}


def precompute_all():
    print("\nPrecomputing analytic sufficient statistics...")
    sys.stdout.flush()
    t0 = time.time()
    all_ss = {}
    all_tau_true = {}

    for K in K_VALUES:
        params = make_all_params(K)
        for topo in ALL_TOPOS:
            ss = _COMPUTE_SS[topo](K, params[topo])
            tau_true = get_tau_true(topo, K, params, ss)
            all_ss[(topo, K)] = ss
            all_tau_true[(topo, K)] = tau_true

    print("  Done ({:.3f}s). tau_true values:".format(time.time() - t0))
    for topo in ALL_TOPOS:
        vals = [all_tau_true[(topo, K)] for K in K_VALUES]
        vals_s = ", ".join(
            f"K{K}={v:.10f}" if v is not None and not np.isnan(v) else f"K{K}=NaN"
            for K, v in zip(K_VALUES, vals))
        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
        print(f"    {topo:<14} [{direction}] {vals_s}")
    sys.stdout.flush()
    return all_ss, all_tau_true


# ====================================================================
# Part 1: Random Verification
# ====================================================================
def part1_random(all_ss, all_tau_true):
    print("\n" + "=" * 70)
    print("PART 1: Random Verification ({:,} C0 per topology x K)".format(N_RANDOM))
    print("  MONO_TOL = {:.0e} (analytic -- zero sampling noise)".format(MONO_TOL))
    print("=" * 70)
    sys.stdout.flush()

    results = {}
    total_tests = 0
    total_violations = 0

    for K in K_VALUES:
        print(f"\n  K = {K}")
        print(f"  {'Topology':<14} {'Direction':<10} {'Tested':>8} "
              f"{'Violations':>11} {'NaN_curves':>11} {'Worst_mag':>12} {'Time':>7}")
        print(f"  {'-' * 75}")
        sys.stdout.flush()

        for topo in ALL_TOPOS:
            t0 = time.time()
            ss = all_ss[(topo, K)]
            tau_true = all_tau_true[(topo, K)]

            rng_C = np.random.default_rng(SEED * 2 + K * 1000 + TOPO_IDX[topo])
            violations = 0
            nan_curves = 0
            worst_mag = 0.0

            for i in range(N_RANDOM):
                C0 = np.zeros((K, K))
                for j in range(K):
                    C0[:, j] = rng_C.dirichlet(np.ones(K))

                _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)

                n_nan = np.isnan(bias_abs).sum()
                if n_nan > len(bias_abs) * 0.5:
                    nan_curves += 1
                    continue

                n_viol = check_monotonicity(bias_abs, topo)
                if n_viol > 0:
                    violations += 1
                    valid = ~np.isnan(bias_abs)
                    ba = bias_abs[valid]
                    diffs = np.diff(ba)
                    if topo in NON_DECREASING:
                        worst_mag = max(worst_mag, abs(diffs.min()))
                    else:
                        worst_mag = max(worst_mag, diffs.max())

            elapsed = time.time() - t0
            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
            print(f"  {topo:<14} {direction:<10} {N_RANDOM:>8} "
                  f"{violations:>11} {nan_curves:>11} {worst_mag:>12.2e} {elapsed:>6.1f}s")
            sys.stdout.flush()

            results[f"{topo}_K{K}"] = {
                "n_tested": N_RANDOM,
                "violations": violations,
                "nan_curves": nan_curves,
                "direction": direction,
                "worst_violation_magnitude": float(worst_mag),
                "tau_true": float(tau_true) if not np.isnan(tau_true) else None,
            }
            total_tests += N_RANDOM
            total_violations += violations

    print(f"\n  Grand total: {total_tests:,} tests, {total_violations} violations")
    return results


# ====================================================================
# Part 2: Adversarial Search
# ====================================================================
def part2_adversarial(all_ss, all_tau_true):
    print("\n" + "=" * 70)
    print(f"PART 2: Adversarial Search ({ADV_N_STARTS} starts x "
          f"{len(ADV_DELTA_PAIRS)} delta-pairs)")
    print("=" * 70)
    sys.stdout.flush()

    results = {}

    for K in K_ADVERSARIAL:
        print(f"\n  K = {K}")
        print(f"  {'Topology':<14} {'Direction':<10} {'best_obj':>12} "
              f"{'Counterex':>11} {'Time':>7}")
        print(f"  {'-' * 57}")
        sys.stdout.flush()

        for topo in ALL_TOPOS:
            t0 = time.time()
            ss = all_ss[(topo, K)]
            tau_true = all_tau_true[(topo, K)]

            best_objective = np.inf
            found_counterexample = False
            rng_adv = np.random.default_rng(
                SEED * 3 + K * 10000 + TOPO_IDX[topo] * 100)

            for d1, d2 in ADV_DELTA_PAIRS:
                for _ in range(ADV_N_STARTS):
                    theta0 = rng_adv.normal(0, 1, K * K)

                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
                                  _d1=d1, _d2=d2, _K=K):
                        logits = theta.reshape(_K, _K)
                        exp_l = np.exp(logits - logits.max(axis=0, keepdims=True))
                        C0 = exp_l / exp_l.sum(axis=0, keepdims=True)

                        C1 = (1 - _d1) * np.eye(_K) + _d1 * C0
                        C2 = (1 - _d2) * np.eye(_K) + _d2 * C0

                        tau1 = get_tau_at_C(_topo, C1, _ss)
                        tau2 = get_tau_at_C(_topo, C2, _ss)

                        if np.isnan(tau1) or np.isnan(tau2):
                            return 0.0

                        b1_sq = (tau1 - _tt) ** 2
                        b2_sq = (tau2 - _tt) ** 2

                        if _topo in NON_DECREASING:
                            return b2_sq - b1_sq
                        else:
                            return b1_sq - b2_sq

                    res = scipy_minimize(objective, theta0, method='L-BFGS-B',
                                         options={'maxiter': 100, 'ftol': 1e-15})

                    if res.fun < best_objective:
                        best_objective = res.fun

                    if res.fun < -1e-8:
                        found_counterexample = True

            elapsed = time.time() - t0
            direction = "non-dec" if topo in NON_DECREASING else "non-inc"
            ce_str = "YES!" if found_counterexample else "no"
            print(f"  {topo:<14} {direction:<10} {best_objective:>12.2e} "
                  f"{ce_str:>11} {elapsed:>6.1f}s")
            sys.stdout.flush()

            results[f"{topo}_K{K}"] = {
                "n_starts": ADV_N_STARTS * len(ADV_DELTA_PAIRS),
                "best_objective": float(best_objective),
                "found_counterexample": found_counterexample,
                "delta_pairs": [[d1, d2] for d1, d2 in ADV_DELTA_PAIRS],
            }

    return results


# ====================================================================
# Main
# ====================================================================
def main():
    t_total = time.time()
    print("Exp-D v2: Conjecture 1 Verification with ANALYTIC plim")
    print(f"  Random: {N_RANDOM:,} C0 x {len(ALL_TOPOS)} topologies x K in {K_VALUES}")
    print(f"  Adversarial: {ADV_N_STARTS} starts x {len(ADV_DELTA_PAIRS)} "
          f"delta-pairs x K in {K_ADVERSARIAL}")
    print(f"  GH quadrature: {N_GH} points/dim, MONO_TOL={MONO_TOL:.0e}")
    print(f"  seed={SEED}")
    sys.stdout.flush()

    all_ss, all_tau_true = precompute_all()

    random_results = part1_random(all_ss, all_tau_true)
    adversarial_results = part2_adversarial(all_ss, all_tau_true)

    # Build output
    total_random = sum(r['n_tested'] for r in random_results.values())
    total_viol = sum(r['violations'] for r in random_results.values())
    total_ce = sum(1 for r in adversarial_results.values()
                   if r['found_counterexample'])

    if total_viol == 0 and total_ce == 0:
        summary = (f"Zero violations across {total_random:,} random tests + "
                   f"0 counterexamples found by adversarial search "
                   f"(analytic plim, MONO_TOL={MONO_TOL:.0e})")
    else:
        summary = (f"{total_viol} violations across {total_random:,} random tests + "
                   f"{total_ce} counterexamples found by adversarial search "
                   f"(analytic plim, MONO_TOL={MONO_TOL:.0e})")

    output = {
        "method": "analytic_plim",
        "gh_quadrature_points": N_GH,
        "mono_tol": MONO_TOL,
        "random_verification": {},
        "adversarial_search": {},
        "summary": summary,
    }

    for topo in ALL_TOPOS:
        rv = {}
        for K in K_VALUES:
            key = f"{topo}_K{K}"
            if key in random_results:
                rv[f"K{K}"] = random_results[key]
        output["random_verification"][topo] = rv

    for topo in ALL_TOPOS:
        av = {}
        for K in K_ADVERSARIAL:
            key = f"{topo}_K{K}"
            if key in adversarial_results:
                av[f"K{K}"] = adversarial_results[key]
        output["adversarial_search"][topo] = av

    out_path = os.path.join(OUT_DIR, 'exp_d_conjecture_results_v2.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")

    total_time = time.time() - t_total
    print(f"\n{'=' * 70}")
    print(f"SUMMARY: {summary}")
    print(f"Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
    print(f"{'=' * 70}")

    # Print comparison note
    print("\nComparison with v1 (Monte Carlo, N=5M, MONO_TOL=1e-8):")
    print("  v1 found 141,514 violations across 210,000 tests")
    print("  v1 found 13 adversarial 'counterexamples'")
    print(f"  v2 found {total_viol} violations across {total_random:,} tests")
    print(f"  v2 found {total_ce} adversarial counterexamples")


if __name__ == "__main__":
    main()
