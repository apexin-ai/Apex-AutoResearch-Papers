#!/usr/bin/env python3
"""
plan_007_correction_guidance.py — Correction Method Guidance MC Framework

Purpose: Evaluate 5 correction methods for K=3 LLM misclassification bias across
         7 DAG topologies and 6 confusion matrix structures via Monte Carlo simulation.

For each {topology x C_structure x correction_method}, runs N_sim MC replications to
measure bias_reduction, RMSE, 95% CI coverage, and method failure rates. Outputs an
optimal correction method mapping per {topology x C_structure}.

Input:   Hardcoded DGP parameters (consistent with plan_001/002),
         6 synthetic K=3 column-stochastic confusion matrices.
Output:  artifacts/plan007/correction_guidance_results.json  — full MC results
         artifacts/plan007/correction_mapping.txt            — {topo x C} -> best method
         artifacts/plan007/method_comparison_summary.txt     — cross-topology rankings

Dependencies: numpy, scipy (scipy only for polyfit fallback; core uses numpy)
"""

import numpy as np
import json
import hashlib
import os
import time
import argparse
from collections import OrderedDict

# ================================================================
# Constants
# ================================================================
K = 3
N_DATA_DEFAULT = 5000
N_SIM_DEFAULT = 1000
N_GOLD = 500
SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
SIMEX_B = 50
EM_MAX_ITER = 100
EM_TOL = 1e-6

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "artifacts", "plan007")

ALL_METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]


# ================================================================
# Confusion Matrices (column-stochastic, K=3)
# C[j,i] = P(A*=j | A=i)
# ================================================================
def _build_C_structures():
    cs = OrderedDict()
    # mild: diag≈0.867, off≈0.067
    cs["mild_uniform"] = 0.8 * np.eye(K) + (0.2 / K) * np.ones((K, K))
    # moderate: diag≈0.733, off≈0.133
    cs["moderate_uniform"] = 0.6 * np.eye(K) + (0.4 / K) * np.ones((K, K))
    # severe: diag=0.6, off=0.2
    cs["severe_uniform"] = 0.4 * np.eye(K) + (0.6 / K) * np.ones((K, K))
    # asymmetric: class 0->1 high (0.20), others low
    cs["asymmetric"] = np.array([
        [0.75, 0.05, 0.05],
        [0.20, 0.80, 0.10],
        [0.05, 0.15, 0.85]])
    # near-permutation: cyclic shift with P≈0.90
    cs["near_permutation"] = np.array([
        [0.05, 0.05, 0.90],
        [0.90, 0.05, 0.05],
        [0.05, 0.90, 0.05]])
    # realistic LLM: adjacent confusion high, distant low
    cs["realistic_llm"] = np.array([
        [0.78, 0.15, 0.03],
        [0.18, 0.72, 0.18],
        [0.04, 0.13, 0.79]])
    for name, C in cs.items():
        assert np.allclose(C.sum(axis=0), 1.0), f"{name} not column-stochastic"
        assert (C >= 0).all(), f"{name} has negative entries"
    return cs


C_STRUCTURES = _build_C_structures()


# ================================================================
# DGP Parameters (K=3, consistent with plan_001/002)
# ================================================================
DGP_PARAMS = dict(
    confounding=dict(
        p_A=np.array([0.40, 0.35, 0.25]),
        alpha=np.array([1.5, -1.0]),
        beta_A=np.array([1.0, -0.5]),
        beta_T=2.0, sigma_T=1.0),
    mediation=dict(
        tau=0.5,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 0.8, -0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    collider=dict(
        tau=1.0, g=np.zeros(K),
        dT=np.array([0.0, 0.5, -0.3]),
        dY=np.array([0.0, 0.8, 0.6])),
    exposure=dict(
        beta=np.array([0.0, 1.0, -0.5]),
        p_A=np.array([0.40, 0.35, 0.25])),
    mbias=dict(
        tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
        a1=np.array([0.0, 0.8, -0.5]),
        a2=np.array([0.0, 0.6, 0.9])),
    iv=dict(
        lam=1.0, g=np.zeros(K),
        dZ=np.array([0.0, 1.0, -0.5]),
        dU=np.array([0.0, 0.8, 0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    frontdoor=dict(
        alpha_U=1.0, lam_U=1.0,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 1.0, -0.8]),
        beta=np.array([0.0, 1.0, -0.5])),
)


# ================================================================
# Utilities
# ================================================================
def det_seed(topo, c_name, sim_idx, base=42):
    """Deterministic seed for data generation (same across methods)."""
    h = hashlib.sha256(f"{topo}|{c_name}|{sim_idx}|{base}".encode()).hexdigest()
    return int(h[:8], 16)


def det_seed_method(topo, c_name, method, sim_idx, base=42):
    """Deterministic seed for method-specific randomness."""
    h = hashlib.sha256(
        f"{topo}|{c_name}|{method}|{sim_idx}|{base}".encode()).hexdigest()
    return int(h[:8], 16)


def softmax_sample(logits, rng):
    """Sample from row-wise softmax (K=3 optimized)."""
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    p = e / e.sum(axis=1, keepdims=True)
    cum = np.cumsum(p, axis=1)
    u = rng.uniform(size=logits.shape[0])
    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)


def misclassify(A, C, rng):
    """Apply misclassification: A*_i ~ Cat(C[:, A_i])."""
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)


def make_dummies(A):
    """K-1 dummy variables (reference category = 0)."""
    N = len(A)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    return D


def make_full_dummies(A):
    """Full K one-hot encoding."""
    N = len(A)
    D = np.zeros((N, K))
    for j in range(K):
        D[:, j] = (A == j).astype(float)
    return D


def ols(X, Y):
    """OLS point estimate."""
    return np.linalg.lstsq(X, Y, rcond=None)[0]


def ols_with_se(X, Y):
    """OLS point estimate + heteroskedasticity-naive SE."""
    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
    resid = Y - X @ beta
    n, p = X.shape
    s2 = resid @ resid / max(n - p, 1)
    try:
        XtX_inv = np.linalg.inv(X.T @ X)
        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
    except np.linalg.LinAlgError:
        se = np.full(p, np.nan)
    return beta, se


# ================================================================
# DGP Functions (7 topologies)
# Return: (X_other, Y, A, tau_idx)
#   X_other: non-A columns (always includes intercept)
#   A: true categorical (values 0..K-1)
#   tau_idx: target coefficient index in [X_other | D_{K-1}]
# ================================================================
def gen_confounding(N, rng):
    """A->T, A->Y, T->Y. Researcher controls for A*."""
    p = DGP_PARAMS["confounding"]
    A = rng.choice(K, size=N, p=p["p_A"])
    D = make_dummies(A)
    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
    return np.column_stack([np.ones(N), T]), Y, A, 1


def gen_mediation(N, rng):
    """T->A->Y. A mediates; researcher controls for A*."""
    p = DGP_PARAMS["mediation"]
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
    A = softmax_sample(logits, rng)
    D = make_dummies(A)
    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
    return np.column_stack([np.ones(N), T]), Y, A, 1


def gen_collider(N, rng):
    """T->A<-Y. Researcher wrongly controls for A*."""
    p = DGP_PARAMS["collider"]
    T = rng.normal(0, 1, N)
    Y = p["tau"] * T + rng.normal(0, 1, N)
    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
              + p["dY"][None, :] * Y[:, None])
    A = softmax_sample(logits, rng)
    return np.column_stack([np.ones(N), T]), Y, A, 1


def gen_exposure(N, rng):
    """A->Y (direct exposure, no T)."""
    p = DGP_PARAMS["exposure"]
    A = rng.choice(K, size=N, p=p["p_A"])
    D = make_dummies(A)
    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
    return np.ones((N, 1)), Y, A, 1


def gen_mbias(N, rng):
    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias."""
    p = DGP_PARAMS["mbias"]
    U1, U2 = rng.normal(0, 1, N), rng.normal(0, 1, N)
    T = p["delta_coef"] * U1 + rng.normal(0, 1, N)
    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
              + p["a2"][None, :] * U2[:, None])
    A = softmax_sample(logits, rng)
    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N)
    return np.column_stack([np.ones(N), T]), Y, A, 1


def gen_iv(N, rng):
    """Z->A->Y, U->{A,Y}. OLS on A* (no IV correction)."""
    p = DGP_PARAMS["iv"]
    Z, U = rng.normal(0, 1, N), rng.normal(0, 1, N)
    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
              + p["dU"][None, :] * U[:, None])
    A = softmax_sample(logits, rng)
    D = make_dummies(A)
    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
    return np.ones((N, 1)), Y, A, 1


def gen_frontdoor(N, rng):
    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator)."""
    p = DGP_PARAMS["frontdoor"]
    U = rng.normal(0, 1, N)
    T = p["alpha_U"] * U + rng.normal(0, 1, N)
    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
    M = softmax_sample(logits, rng)
    D_M = make_dummies(M)
    Y = p["beta"][0] + D_M @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
    return np.ones((N, 1)), Y, M, 1


GEN_FUNCS = OrderedDict([
    ("confounding", gen_confounding), ("mediation", gen_mediation),
    ("collider", gen_collider), ("exposure", gen_exposure),
    ("mbias", gen_mbias), ("iv", gen_iv), ("frontdoor", gen_frontdoor),
])


# ================================================================
# Oracle: plim of OLS with true A (large-sample reference)
# ================================================================
_oracle_cache = {}


def compute_oracle_tau(topo_name, n_large=500_000, seed=999999):
    if topo_name in _oracle_cache:
        return _oracle_cache[topo_name]
    rng = np.random.default_rng(seed)
    X_other, Y, A, tau_idx = GEN_FUNCS[topo_name](n_large, rng)
    D = make_dummies(A)
    X = np.column_stack([X_other, D])
    beta = ols(X, Y)
    _oracle_cache[topo_name] = float(beta[tau_idx])
    return _oracle_cache[topo_name]


# ================================================================
# Correction Methods
# All return (tau_hat, se_tau, success: bool)
# ================================================================
def estimate_uncorrected(X_other, Y, Astar, tau_idx):
    D_star = make_dummies(Astar)
    X = np.column_stack([X_other, D_star])
    try:
        beta, se = ols_with_se(X, Y)
        return beta[tau_idx], se[tau_idx], True
    except Exception:
        return np.nan, np.nan, False


def correct_naive_plugin(X_other, Y, Astar, C, tau_idx):
    """Per-observation correction: corrected_i = C^{-1}[:, A*_i].
    Unbiased for any invertible C."""
    try:
        C_inv = np.linalg.inv(C)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False
    # C_inv[:, Astar] is K x N; transpose to N x K
    D_corrected = C_inv[:, Astar].T[:, 1:]  # drop ref cat
    X = np.column_stack([X_other, D_corrected])
    try:
        beta, se = ols_with_se(X, Y)
        return beta[tau_idx], se[tau_idx], True
    except Exception:
        return np.nan, np.nan, False


def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx):
    """EM-based joint estimation of regression params and C.
    Uses gold-standard labels for initialization and E-step anchoring."""
    N = len(Y)
    n_other = X_other.shape[1]
    silver_mask = ~gold_mask

    # Initialize C from gold data
    C_est = np.zeros((K, K))
    for j in range(K):
        for k in range(K):
            C_est[k, j] = ((A_gold[gold_mask] == j)
                           & (Astar[gold_mask] == k)).sum()
    col_sums = C_est.sum(axis=0)
    col_sums[col_sums == 0] = 1.0
    C_est /= col_sums
    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))

    # Initialize beta from naive OLS
    D_star = make_dummies(Astar)
    X_init = np.column_stack([X_other, D_star])
    try:
        beta = ols(X_init, Y)
    except Exception:
        return np.nan, np.nan, False
    sigma2 = 1.0

    # Pre-compute base predictions
    for it in range(EM_MAX_ITER):
        base = X_other @ beta[:n_other]

        # E-step: P(A=j | A*_i, Y_i, X_i; beta, C, sigma2)
        resp = np.zeros((N, K))
        for j in range(K):
            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
            resp[:, j] = (-0.5 * (Y - mu_j) ** 2 / sigma2
                          + np.log(np.clip(C_est[Astar, j], 1e-15, None)))

        resp -= resp.max(axis=1, keepdims=True)
        resp = np.exp(resp)
        resp /= resp.sum(axis=1, keepdims=True)

        # Anchor gold observations
        resp[gold_mask] = 0.0
        resp[gold_mask, A_gold[gold_mask]] = 1.0

        # M-step: beta from expected dummies
        D_exp = resp[:, 1:]
        X_new = np.column_stack([X_other, D_exp])
        try:
            beta_new = ols(X_new, Y)
        except Exception:
            return np.nan, np.nan, False

        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)

        # M-step: update C from responsibilities
        C_new = np.zeros((K, K))
        for j in range(K):
            for k in range(K):
                C_new[k, j] = resp[Astar == k, j].sum()
        cs = C_new.sum(axis=0)
        cs[cs == 0] = 1.0
        C_new /= cs

        converged = (np.max(np.abs(beta_new - beta)) < EM_TOL
                     and np.max(np.abs(C_new - C_est)) < EM_TOL)
        beta, C_est, sigma2 = beta_new, C_new, sigma2_new
        if converged:
            break

    # Final estimate with converged responsibilities
    X_final = np.column_stack([X_other, resp[:, 1:]])
    try:
        beta_f, se_f = ols_with_se(X_final, Y)
        return beta_f[tau_idx], se_f[tau_idx], True
    except Exception:
        return np.nan, np.nan, False


def correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx, rng):
    """PPI++ with bootstrap lambda tuning.
    Combines gold-standard OLS (unbiased, high var) with full-sample A* OLS."""
    gold_idx = np.where(gold_mask)[0]
    n_gold = len(gold_idx)

    D_g_true = make_dummies(A_gold[gold_mask])
    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])
    D_g_star = make_dummies(Astar[gold_mask])
    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])
    D_all_star = make_dummies(Astar)
    X_all_star = np.column_stack([X_other, D_all_star])

    try:
        b_g_true = ols(X_g_true, Y[gold_mask])
        b_g_star = ols(X_g_star, Y[gold_mask])
        b_all_star = ols(X_all_star, Y)
    except Exception:
        return np.nan, np.nan, False

    # Bootstrap for PPI++ lambda
    n_boot = 50
    tau_true_boot = np.zeros(n_boot)
    tau_rect_boot = np.zeros(n_boot)
    for b in range(n_boot):
        idx = rng.choice(gold_idx, size=n_gold, replace=True)
        try:
            bt = ols(np.column_stack([X_other[idx], make_dummies(A_gold[idx])]),
                     Y[idx])
            bs = ols(np.column_stack([X_other[idx], make_dummies(Astar[idx])]),
                     Y[idx])
            tau_true_boot[b] = bt[tau_idx]
            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]
        except Exception:
            tau_true_boot[b] = tau_rect_boot[b] = np.nan

    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
    if valid.sum() > 5:
        var_r = np.var(tau_rect_boot[valid])
        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
    else:
        lam = 1.0

    tau_ppi = (b_g_true[tau_idx]
               + lam * (b_all_star[tau_idx] - b_g_star[tau_idx]))

    se_est = np.std(tau_true_boot[valid]) if valid.sum() > 1 else np.nan
    return tau_ppi, se_est, True


def correct_mcsimex(X_other, Y, Astar, C, tau_idx, rng):
    """MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.
    At lambda>0, apply C^lambda to A* producing A**; fit OLS and average over B draws.
    Quadratic extrapolation to lambda=-1 (no error)."""
    try:
        eigvals, eigvecs = np.linalg.eig(C)
        eigvecs_inv = np.linalg.inv(eigvecs)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False

    lambdas = np.array([0.0] + SIMEX_LAMBDAS)
    tau_lam = np.zeros(len(lambdas))

    for li, lam in enumerate(lambdas):
        if lam == 0.0:
            D_star = make_dummies(Astar)
            X = np.column_stack([X_other, D_star])
            try:
                tau_lam[li] = ols(X, Y)[tau_idx]
            except Exception:
                return np.nan, np.nan, False
        else:
            # C^lambda via eigendecomposition
            C_lam_raw = np.real((eigvecs * (eigvals ** lam)) @ eigvecs_inv)
            C_lam = np.clip(C_lam_raw, 0, None)
            cs = C_lam.sum(axis=0)
            cs[cs == 0] = 1.0
            C_lam /= cs

            tau_b = np.zeros(SIMEX_B)
            for b in range(SIMEX_B):
                rng_b = np.random.default_rng(
                    rng.integers(0, 2**31) + b * 1000 + li * 100000)
                Astar_extra = misclassify(Astar, C_lam, rng_b)
                D_extra = make_dummies(Astar_extra)
                X_extra = np.column_stack([X_other, D_extra])
                try:
                    tau_b[b] = ols(X_extra, Y)[tau_idx]
                except Exception:
                    tau_b[b] = np.nan

            ok = np.isfinite(tau_b)
            if ok.sum() < SIMEX_B // 2:
                return np.nan, np.nan, False
            tau_lam[li] = tau_b[ok].mean()

    # Quadratic extrapolation to lambda=-1
    try:
        coeffs = np.polyfit(lambdas, tau_lam, 2)
        tau_simex = np.polyval(coeffs, -1.0)
    except Exception:
        return np.nan, np.nan, False

    # SE proxy from naive OLS (SIMEX SE requires bootstrap, not done here)
    D_star = make_dummies(Astar)
    X = np.column_stack([X_other, D_star])
    try:
        _, se = ols_with_se(X, Y)
        return tau_simex, se[tau_idx], True
    except Exception:
        return tau_simex, np.nan, True


def correct_mla(X_other, Y, Astar, C, tau_idx):
    """MLA: right-multiply full dummies by C^{-1}.
    D_corrected = D*_full @ C^{-1}. Unbiased only when C is symmetric."""
    try:
        C_inv = np.linalg.inv(C)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False
    D_full = make_full_dummies(Astar)
    D_corrected = (D_full @ C_inv)[:, 1:]  # drop ref cat
    X = np.column_stack([X_other, D_corrected])
    try:
        beta, se = ols_with_se(X, Y)
        return beta[tau_idx], se[tau_idx], True
    except Exception:
        return np.nan, np.nan, False


# ================================================================
# MC Framework
# ================================================================
def run_mc(topo_name, c_name, methods, n_sim, n_data):
    """Run MC for one {topo x C} pair across all requested methods."""
    C = C_STRUCTURES[c_name]
    gen_fn = GEN_FUNCS[topo_name]
    tau_true = compute_oracle_tau(topo_name)

    tau_uncorr = np.zeros(n_sim)
    store = {m: {"tau": np.zeros(n_sim), "se": np.zeros(n_sim),
                 "ok": np.zeros(n_sim, dtype=bool)} for m in methods}

    for i in range(n_sim):
        seed = det_seed(topo_name, c_name, i)
        rng = np.random.default_rng(seed)
        X_other, Y, A_true, tau_idx = gen_fn(n_data, rng)
        Astar = misclassify(A_true, C, rng)

        gold_mask = np.zeros(n_data, dtype=bool)
        gold_mask[:min(N_GOLD, n_data)] = True

        t_u, _, _ = estimate_uncorrected(X_other, Y, Astar, tau_idx)
        tau_uncorr[i] = t_u

        for m in methods:
            rng_m = np.random.default_rng(
                det_seed_method(topo_name, c_name, m, i))
            if m == "naive_plugin":
                t, s, ok = correct_naive_plugin(
                    X_other, Y, Astar, C, tau_idx)
            elif m == "dsl":
                t, s, ok = correct_dsl(
                    X_other, Y, Astar, A_true, gold_mask, tau_idx)
            elif m == "ppi":
                t, s, ok = correct_ppi(
                    X_other, Y, Astar, A_true, gold_mask, tau_idx, rng_m)
            elif m == "mcsimex":
                t, s, ok = correct_mcsimex(
                    X_other, Y, Astar, C, tau_idx, rng_m)
            elif m == "mla":
                t, s, ok = correct_mla(
                    X_other, Y, Astar, C, tau_idx)
            else:
                raise ValueError(f"Unknown method: {m}")
            store[m]["tau"][i] = t
            store[m]["se"][i] = s
            store[m]["ok"][i] = ok

    # Aggregate
    v_u = np.isfinite(tau_uncorr)
    results = []
    for m in methods:
        v = store[m]["ok"] & np.isfinite(store[m]["tau"])
        v_both = v & v_u
        fail = 1.0 - v.mean()

        if v_both.sum() < 10:
            results.append(dict(
                method=m, topo=topo_name, c_name=c_name,
                tau_true=tau_true, failure_rate=float(fail),
                valid_count=int(v.sum()),
                bias_uncorrected=np.nan, bias_corrected=np.nan,
                bias_reduction_pct=np.nan,
                rmse_uncorrected=np.nan, rmse_corrected=np.nan,
                coverage_95=np.nan))
            continue

        bias_u = float(np.mean(tau_uncorr[v_both]) - tau_true)
        bias_c = float(np.mean(store[m]["tau"][v_both]) - tau_true)
        rmse_u = float(np.sqrt(np.mean((tau_uncorr[v_both] - tau_true) ** 2)))
        rmse_c = float(np.sqrt(np.mean((store[m]["tau"][v_both] - tau_true) ** 2)))

        abs_u, abs_c = abs(bias_u), abs(bias_c)
        br = float(1.0 - abs_c / abs_u) if abs_u > 1e-10 else 0.0

        # 95% CI coverage
        v_se = v_both & np.isfinite(store[m]["se"])
        if v_se.sum() > 0:
            lo = store[m]["tau"][v_se] - 1.96 * store[m]["se"][v_se]
            hi = store[m]["tau"][v_se] + 1.96 * store[m]["se"][v_se]
            cov = float(np.mean((tau_true >= lo) & (tau_true <= hi)))
        else:
            cov = np.nan

        results.append(dict(
            method=m, topo=topo_name, c_name=c_name,
            tau_true=tau_true,
            failure_rate=float(fail),
            valid_count=int(v_both.sum()),
            bias_uncorrected=bias_u,
            bias_corrected=bias_c,
            bias_reduction_pct=br,
            rmse_uncorrected=rmse_u,
            rmse_corrected=rmse_c,
            coverage_95=cov))
    return results


# ================================================================
# Empirical Validation Placeholder
# ================================================================
def run_empirical_validation(plan003_data_path=None):
    """Placeholder: validate corrections on real LLM annotation data from plan_003.
    To be filled when plan_003 produces annotated datasets."""
    if plan003_data_path is None:
        return None
    raise NotImplementedError("Awaiting plan_003 completion")


# ================================================================
# Output
# ================================================================
def save_results(all_results, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    # 1. Full JSON
    jp = os.path.join(out_dir, "correction_guidance_results.json")
    with open(jp, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"  -> {jp}")

    # 2. Optimal method mapping
    mp = os.path.join(out_dir, "correction_mapping.txt")
    with open(mp, "w") as f:
        f.write("Optimal Correction Method: {topology x C_structure} -> best method\n")
        f.write("Criterion: max bias_reduction_pct (tie-break: min RMSE)\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"{'Topology':<14} {'C Structure':<20} {'Best Method':<16} "
                f"{'BiasRed%':>9} {'RMSE':>8}\n")
        f.write("-" * 67 + "\n")
        for topo in GEN_FUNCS:
            for cn in C_STRUCTURES:
                cands = [r for r in all_results
                         if r["topo"] == topo and r["c_name"] == cn]
                if not cands:
                    continue
                best = max(cands, key=lambda r: (
                    r["bias_reduction_pct"]
                    if np.isfinite(r.get("bias_reduction_pct", np.nan))
                    else -999,
                    -(r["rmse_corrected"]
                      if np.isfinite(r.get("rmse_corrected", np.nan))
                      else 999)))
                br = best.get("bias_reduction_pct", np.nan)
                rm = best.get("rmse_corrected", np.nan)
                if np.isfinite(br) and np.isfinite(rm):
                    f.write(f"{topo:<14} {cn:<20} {best['method']:<16} "
                            f"{br:>8.1%} {rm:>8.4f}\n")
                else:
                    f.write(f"{topo:<14} {cn:<20} {best['method']:<16} "
                            f"{'N/A':>9} {'N/A':>8}\n")
            f.write("\n")
    print(f"  -> {mp}")

    # 3. Method comparison summary
    sp = os.path.join(out_dir, "method_comparison_summary.txt")
    with open(sp, "w") as f:
        f.write("Cross-Topology Method Comparison Summary\n")
        f.write("=" * 90 + "\n")

        for method in ALL_METHODS:
            mr = [r for r in all_results if r["method"] == method]
            if not mr:
                continue
            f.write(f"\n--- {method} ---\n")
            br = [r["bias_reduction_pct"] for r in mr
                  if np.isfinite(r.get("bias_reduction_pct", np.nan))]
            rm = [r["rmse_corrected"] for r in mr
                  if np.isfinite(r.get("rmse_corrected", np.nan))]
            cv = [r["coverage_95"] for r in mr
                  if np.isfinite(r.get("coverage_95", np.nan))]
            fl = [r["failure_rate"] for r in mr]

            f.write(f"  Scenarios: {len(mr)}\n")
            if br:
                f.write(f"  Bias reduction: mean={np.mean(br):.1%}  "
                        f"median={np.median(br):.1%}  "
                        f"[{np.min(br):.1%}, {np.max(br):.1%}]\n")
            if rm:
                f.write(f"  RMSE: mean={np.mean(rm):.4f}  "
                        f"median={np.median(rm):.4f}\n")
            if cv:
                f.write(f"  Coverage 95%: mean={np.mean(cv):.1%}  "
                        f"min={np.min(cv):.1%}\n")
            f.write(f"  Failure rate: mean={np.mean(fl):.1%}  "
                    f"max={np.max(fl):.1%}\n")

            by_topo = {}
            for r in mr:
                by_topo.setdefault(r["topo"], []).append(
                    r["bias_reduction_pct"])
            f.write("  By topology (mean bias reduction):\n")
            for t, vs in by_topo.items():
                vv = [x for x in vs if np.isfinite(x)]
                if vv:
                    f.write(f"    {t:<14}: {np.mean(vv):.1%}\n")

        # Win counts
        f.write("\n\n--- Method Win Counts ---\n")
        f.write(f"{'Method':<16} {'Wins':>6} {'Rate':>8}\n")
        f.write("-" * 30 + "\n")
        wins = {m: 0 for m in ALL_METHODS}
        total = 0
        for topo in GEN_FUNCS:
            for cn in C_STRUCTURES:
                cands = [r for r in all_results
                         if r["topo"] == topo and r["c_name"] == cn]
                if cands:
                    total += 1
                    b = max(cands, key=lambda r: (
                        r["bias_reduction_pct"]
                        if np.isfinite(r.get("bias_reduction_pct", np.nan))
                        else -999))
                    wins[b["method"]] += 1
        for m in ALL_METHODS:
            rate = wins[m] / total if total > 0 else 0
            f.write(f"{m:<16} {wins[m]:>6} {rate:>7.1%}\n")
    print(f"  -> {sp}")


# ================================================================
# Main
# ================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Plan 007: Correction Method Guidance MC Framework. "
                    "Evaluates 5 correction methods x 7 DAG topologies x "
                    "6 confusion matrices via Monte Carlo simulation.")
    parser.add_argument("--n-sim", type=int, default=N_SIM_DEFAULT,
                        help=f"MC replications per combination "
                             f"(default: {N_SIM_DEFAULT})")
    parser.add_argument("--n-data", type=int, default=N_DATA_DEFAULT,
                        help=f"Sample size per replication "
                             f"(default: {N_DATA_DEFAULT})")
    parser.add_argument("--topos", nargs="+",
                        default=list(GEN_FUNCS.keys()),
                        choices=list(GEN_FUNCS.keys()),
                        help="Topologies to evaluate")
    parser.add_argument("--c-types", nargs="+",
                        default=list(C_STRUCTURES.keys()),
                        choices=list(C_STRUCTURES.keys()),
                        help="C structures to evaluate")
    parser.add_argument("--methods", nargs="+",
                        default=ALL_METHODS, choices=ALL_METHODS,
                        help="Correction methods to evaluate")
    parser.add_argument("--out-dir", default=OUT_DIR,
                        help="Output directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Quick validation: 1 topo x 1 C x 1 method x "
                             "10 sims")
    args = parser.parse_args()

    if args.dry_run:
        args.n_sim = 10
        args.topos = args.topos[:1]
        args.c_types = args.c_types[:1]
        args.methods = args.methods[:1]
        print("=== DRY RUN ===\n")

    print(f"Plan 007: Correction Guidance MC Framework")
    print(f"  Topologies : {args.topos}")
    print(f"  C structures: {args.c_types}")
    print(f"  Methods    : {args.methods}")
    print(f"  N_sim={args.n_sim}  N_data={args.n_data}  N_gold={N_GOLD}")
    print(f"  Output     : {args.out_dir}\n")

    all_results = []
    t0 = time.time()
    n_combos = len(args.topos) * len(args.c_types)
    combo_i = 0

    for topo in args.topos:
        for cn in args.c_types:
            combo_i += 1
            t1 = time.time()
            print(f"[{combo_i}/{n_combos}] {topo} x {cn} ... ",
                  end="", flush=True)
            results = run_mc(topo, cn, args.methods, args.n_sim, args.n_data)
            all_results.extend(results)
            elapsed = time.time() - t1
            # Print summary for this combo
            for r in results:
                br = r["bias_reduction_pct"]
                br_s = f"{br:.1%}" if np.isfinite(br) else "N/A"
                print(f"\n    {r['method']:<14} bias_red={br_s:>7}  "
                      f"fail={r['failure_rate']:.0%}", end="")
            print(f"  [{elapsed:.1f}s]")

    print(f"\nTotal: {time.time() - t0:.0f}s\n")
    print("Saving results...")
    save_results(all_results, args.out_dir)
    print("\nDone.")


if __name__ == "__main__":
    main()
