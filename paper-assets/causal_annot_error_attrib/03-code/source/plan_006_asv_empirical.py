#!/usr/bin/env python3
"""
plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices

Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
= 27 C matrices) to compute:
  1. Downstream causal bias across 7 DAG topologies
  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
  4. Type I/II error rates before/after ASV filtering
  5. Inter-model error correlation

Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
        Each line: {"true_label": int, "predicted_label": int}

Output: artifacts/plan006/asv_empirical_results.json

Dependencies: numpy (required), matplotlib (optional for plots)
"""

import numpy as np
import json
import argparse
import os
import time
from collections import OrderedDict

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

# ============================================================================
# Constants
# ============================================================================

DATASETS = OrderedDict([
    ('civil_comments', {'K': 2}),
    ('vast', {'K': 3}),
    ('humaid', {'K': 10}),
])

MODELS = ['llama4', 'qwen3', 'deepseek']
PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']

TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']

N_PRECOMP = 2_000_000

# Parameter pools — K=3 values match plan_001/plan_005
_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]


# ============================================================================
# Utility Functions
# ============================================================================

def softmax_rows(logits):
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)


def sample_cat(probs, rng):
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=probs.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def generate_Astar(A, C, rng):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)


def ols_with_dummies(Y, T, Astar, K):
    N = len(Y)
    D = np.zeros((N, K - 1))
    for k in range(1, K):
        D[:, k - 1] = (Astar == k).astype(float)
    X = np.column_stack([np.ones(N), T, D])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        resid = Y - X @ beta
        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
        XtX_inv = np.linalg.inv(X.T @ X)
        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
    except np.linalg.LinAlgError:
        beta = np.full(X.shape[1], np.nan)
        se = np.full(X.shape[1], np.nan)
    return beta, se


def ols_no_T(Y, Astar, K):
    N = len(Y)
    D = np.zeros((N, K - 1))
    for k in range(1, K):
        D[:, k - 1] = (Astar == k).astype(float)
    X = np.column_stack([np.ones(N), D])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        resid = Y - X @ beta
        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
        XtX_inv = np.linalg.inv(X.T @ X)
        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
    except np.linalg.LinAlgError:
        beta = np.full(X.shape[1], np.nan)
        se = np.full(X.shape[1], np.nan)
    return beta, se


def wald_estimator(Z, Y, Astar, k=1):
    z1 = Z == 1; z0 = Z == 0
    n1, n0 = float(z1.sum()), float(z0.sum())
    if n1 < 2 or n0 < 2:
        return np.nan, np.nan
    RF = Y[z1].mean() - Y[z0].mean()
    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
    Dk_z1 = (Astar[z1] == k).astype(float).mean()
    Dk_z0 = (Astar[z0] == k).astype(float).mean()
    FS = Dk_z1 - Dk_z0
    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
    if abs(FS) < 1e-8:
        return np.nan, np.nan
    W = RF / FS
    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4
    return W, np.sqrt(max(var_W, 0))


# ============================================================================
# DGP Parameters (general K, K=3 matches plan_001/plan_005)
# ============================================================================

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


def make_dgp_params_H0(K, params):
    p0 = {}
    for topo, p in params.items():
        if topo == 'confounding':
            p0[topo] = dict(p, beta_T=0.0)
        elif topo == 'mediation':
            p0[topo] = dict(p, tau=0.0)
        elif topo == 'collider':
            p0[topo] = dict(p, tau=0.0)
        elif topo == 'exposure':
            p0[topo] = dict(p, beta=np.zeros(K))
        elif topo == 'mbias':
            p0[topo] = dict(p, tau=0.0)
        elif topo == 'iv':
            p0[topo] = dict(p, beta=np.zeros(K))
        elif topo == 'frontdoor':
            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,
                            delta_fd=np.zeros(K), beta=np.zeros(K))
    return p0


# ============================================================================
# DGP Generators (general K)
# ============================================================================

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


# ============================================================================
# Sufficient Statistics & Plim (general K)
# ============================================================================

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
            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
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


# ============================================================================
# 1. Data Loading & Confusion Matrix
# ============================================================================

def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
    d = np.load(path, allow_pickle=True)
    C = d['C']
    assert C.shape == (K, K), f"Expected ({K},{K}), got {C.shape}"
    return C


def load_annotations(data_dir, dataset, model, prompt):
    for suffix in ['_annotations.jsonl', '.jsonl']:
        path = os.path.join(data_dir, dataset, f"{model}_{prompt}{suffix}")
        if os.path.exists(path):
            break
    else:
        raise FileNotFoundError(f"No annotation file for {dataset}/{model}_{prompt}")
    records = []
    label_set = set()
    with open(path) as f:
        for line in f:
            rec = json.loads(line.strip())
            gl = rec.get('true_label', rec.get('gold_label'))
            pl = rec.get('predicted_label', rec.get('pred_label'))
            if gl is not None and pl is not None:
                label_set.add(gl)
                label_set.add(pl)
                records.append((gl, pl))
    if records and isinstance(records[0][0], str):
        sorted_labels = sorted(label_set)
        label_map = {l: i for i, l in enumerate(sorted_labels)}
        records = [(label_map[g], label_map[p]) for g, p in records]
    else:
        records = [(int(g), int(p)) for g, p in records]
    return records


def build_confusion_matrix(records, K):
    counts = np.zeros((K, K))
    for true_k, pred_k in records:
        if 0 <= true_k < K and 0 <= pred_k < K:
            counts[pred_k, true_k] += 1
    col_sums = counts.sum(axis=0)
    col_sums = np.where(col_sums < 1, 1, col_sums)
    return counts / col_sums


def load_all_confusion_matrices(data_dir, dataset_filter=None):
    matrices = {}
    for dataset, info in DATASETS.items():
        if dataset_filter and dataset not in dataset_filter:
            continue
        K = info['K']
        for model in MODELS:
            for prompt in PROMPTS:
                try:
                    C = load_confusion_matrix_npz(data_dir, dataset, model, prompt, K)
                    matrices[(dataset, model, prompt)] = C
                except (FileNotFoundError, Exception):
                    try:
                        records = load_annotations(data_dir, dataset, model, prompt)
                        C = build_confusion_matrix(records, K)
                        matrices[(dataset, model, prompt)] = C
                    except FileNotFoundError:
                        print(f"  [WARN] Missing: {dataset}/{model}_{prompt}")
    return matrices


# ============================================================================
# 2. Downstream Causal Bias
# ============================================================================

def compute_bias_for_topology(C, K, topology, st, tau_true):
    plim_result = compute_plim(C, st, K)
    tau_hat = extract_tau(plim_result, topology)
    if np.isnan(tau_hat) or np.isnan(tau_true):
        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}
    bias = tau_hat - tau_true
    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None
    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)
    return {
        'tau_hat': float(tau_hat), 'bias': float(bias),
        'bias_pct': float(bias_pct) if bias_pct is not None else None,
        'sign_flip': sign_flip,
    }


def compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):
    results = []
    for (dataset, model, prompt), C in confusion_matrices.items():
        K = DATASETS[dataset]['K']
        for topology in TOPOLOGIES:
            st = all_suff_stats[(K, topology)]
            tau_true = all_tau_true[(K, topology)]
            info = compute_bias_for_topology(C, K, topology, st, tau_true)
            results.append({
                'dataset': dataset, 'model': model, 'prompt': prompt,
                'K': K, 'topology': topology, **info,
            })
    return results


# ============================================================================
# 3. ASV Computation
# ============================================================================

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


def compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,
                           n_grid=1500, se_ref=None):
    dmax = compute_delta_max(C0)
    deltas = np.linspace(0, dmax, n_grid)
    tau_curve = np.zeros(n_grid)
    for i, d in enumerate(deltas):
        C_d = C_interpolated(C0, d, K)
        plim_result = compute_plim(C_d, st, K)
        tau_curve[i] = extract_tau(plim_result, topology)

    bias_abs = np.abs(tau_curve - tau_true)
    envelope = np.zeros(n_grid)
    running_max = 0.0
    for i in range(n_grid):
        if np.isfinite(bias_abs[i]):
            running_max = max(running_max, bias_abs[i])
        envelope[i] = running_max

    if asv_type == 'sign_flip':
        if abs(tau_true) < 1e-12:
            return None
        baseline_sign = np.sign(tau_true)
        for i in range(n_grid):
            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:
                return float(deltas[i])
        return None
    elif asv_type == 'magnitude':
        if abs(tau_true) < 1e-12:
            return None
        thresh = 0.1 * abs(tau_true)
        for i in range(n_grid):
            if envelope[i] > thresh:
                return float(deltas[i])
        return None
    elif asv_type == 'significance':
        if se_ref is None or se_ref < 1e-12:
            return None
        for i in range(n_grid):
            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:
                return float(deltas[i])
        return None
    return None


def estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):
    gen_fn = GEN_FNS[topology]
    rng = np.random.default_rng(seed)
    tau_hats = []
    for _ in range(n_mc):
        first_var, Y, A = gen_fn(K, N_ref, params, rng)
        if topology == 'iv':
            th, _ = wald_estimator(first_var, Y, A, k=1)
        elif topology == 'exposure':
            b, _ = ols_no_T(Y, A, K)
            th = b[1]
        else:
            b, _ = ols_with_dummies(Y, first_var, A, K)
            th = b[1]
        if np.isfinite(th):
            tau_hats.append(th)
    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan


def compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):
    results = []
    for (dataset, model, prompt), C in confusion_matrices.items():
        K = DATASETS[dataset]['K']
        for topology in TOPOLOGIES:
            st = all_suff_stats[(K, topology)]
            tau_true = all_tau_true[(K, topology)]
            se_ref = all_se_ref.get((K, topology))
            for asv_type in ['magnitude', 'significance', 'sign_flip']:
                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,
                                             asv_type, se_ref=se_ref)
                results.append({
                    'dataset': dataset, 'model': model, 'prompt': prompt,
                    'K': K, 'topology': topology, 'asv_type': asv_type,
                    'asv': asv,
                })
    return results


# ============================================================================
# 4. F1 vs Downstream Bias
# ============================================================================

def compute_f1_from_C(C, K, p_A=None):
    if p_A is None:
        p_A = np.ones(K) / K
    precision = np.zeros(K)
    recall = np.zeros(K)
    f1 = np.zeros(K)
    for i in range(K):
        recall[i] = C[i, i]
        denom = sum(C[i, j] * p_A[j] for j in range(K))
        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0
        if precision[i] + recall[i] > 1e-12:
            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])
    return {
        'macro_f1': float(f1.mean()),
        'weighted_f1': float((p_A * f1).sum()),
        'per_class_f1': f1.tolist(),
    }


def f1_vs_bias_analysis(confusion_matrices, biases):
    results = []
    for b in biases:
        key = (b['dataset'], b['model'], b['prompt'])
        if key not in confusion_matrices:
            continue
        C = confusion_matrices[key]
        K = b['K']
        p_A = make_p_A(K)
        f1_info = compute_f1_from_C(C, K, p_A)
        abs_bias = abs(b['bias']) if b['bias'] is not None else None
        results.append({
            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],
            'K': K, 'topology': b['topology'],
            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],
            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],
            'sign_flip': b['sign_flip'],
        })
    return results


# ============================================================================
# 5. Type I/II Error Rates
# ============================================================================

def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,
                              st_H1, tau_true,
                              n_sim=100, N_sample=5000, seed=42):
    gen_fn = GEN_FNS[topology]
    rng = np.random.default_rng(seed)

    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')
    asv_safe = (masv is None or masv > 1.0)

    def _run_mc(params_t, n):
        valid = 0; rej = 0
        for _ in range(n):
            fv, Y, A = gen_fn(K, N_sample, params_t, rng)
            Astar = generate_Astar(A, C, rng)
            if topology == 'iv':
                th, se = wald_estimator(fv, Y, Astar, k=1)
            elif topology == 'exposure':
                b, svec = ols_no_T(Y, Astar, K)
                th, se = b[1], svec[1]
            else:
                b, svec = ols_with_dummies(Y, fv, Astar, K)
                th, se = b[1], svec[1]
            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:
                valid += 1
                if abs(th / se) > 1.96:
                    rej += 1
        return rej / max(valid, 1), valid

    type1_before, v0 = _run_mc(params_H0[topology], n_sim)
    power_before, v1 = _run_mc(params_H1[topology], n_sim)
    type1_after = type1_before if asv_safe else 0.0
    power_after = power_before if asv_safe else 0.0

    return {
        'type1_before': float(type1_before), 'type1_after': float(type1_after),
        'power_before': float(power_before), 'power_after': float(power_after),
        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,
        'valid_h0': int(v0), 'valid_h1': int(v1),
    }


# ============================================================================
# 6. Inter-model Error Correlation
# ============================================================================

def compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,
                                    n_samples=1000, seed=42):
    rng = np.random.default_rng(seed)
    p_A = make_p_A(K)
    true_labels = rng.choice(K, size=n_samples, p=p_A)

    predictions = {}
    for model in MODELS:
        key = (dataset, model, prompt)
        if key in confusion_matrices:
            predictions[model] = generate_Astar(true_labels,
                                                confusion_matrices[key], rng)
        else:
            predictions[model] = true_labels.copy()

    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]
    results = {}
    for m1, m2 in pairs:
        p1, p2 = predictions[m1], predictions[m2]
        agreement = float((p1 == p2).mean())
        observed = agreement
        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))
        kappa = float((observed - expected) / (1 - expected)
                      ) if expected < 1 - 1e-10 else 0.0
        err1 = (p1 != true_labels).astype(float)
        err2 = (p2 != true_labels).astype(float)
        if err1.std() > 1e-10 and err2.std() > 1e-10:
            error_corr = float(np.corrcoef(err1, err2)[0, 1])
        else:
            error_corr = 0.0
        results[f"{m1}-{m2}"] = {
            'agreement': agreement,
            'kappa': kappa,
            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,
        }
    return results


# ============================================================================
# Mock Data Generation
# ============================================================================

def generate_mock_C(K, rng, diag_range):
    C = np.zeros((K, K))
    for j in range(K):
        diag_val = rng.uniform(diag_range[0], diag_range[1])
        remaining = 1.0 - diag_val
        if K > 2:
            dists = np.abs(np.arange(K) - j).astype(float)
            dists[j] = np.inf
            weights = 1.0 / dists
            weights[j] = 0
            noise = rng.uniform(0.5, 1.5, K)
            noise[j] = 0
            weights = weights * noise
            weights /= weights.sum()
            C[:, j] = remaining * weights
        else:
            C[1 - j, j] = remaining
        C[j, j] = diag_val
    return C


def generate_mock_confusion_matrices(seed=12345):
    rng = np.random.default_rng(seed)
    matrices = {}
    diag_ranges = {
        'civil_comments': (0.85, 0.95),
        'vast': (0.70, 0.90),
        'humaid': (0.60, 0.85),
    }
    for dataset, info in DATASETS.items():
        K = info['K']
        dr = diag_ranges[dataset]
        for model in MODELS:
            for prompt in PROMPTS:
                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)
    return matrices


# ============================================================================
# Diagnostic Plots (optional)
# ============================================================================

def save_f1_vs_bias_plot(f1_bias, output_dir):
    if not HAS_MPL:
        return
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    for idx, topo in enumerate(TOPOLOGIES):
        ax = axes[idx]
        subset = [r for r in f1_bias if r['topology'] == topo
                  and r['abs_bias'] is not None]
        if not subset:
            ax.set_title(topo)
            continue
        f1s = [r['macro_f1'] for r in subset]
        biases = [r['abs_bias'] for r in subset]
        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]
        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)
        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)
        ax.set_xlabel('Macro F1')
        ax.set_ylabel('|bias|')
        ax.set_title(topo)
    if len(TOPOLOGIES) < 8:
        axes[-1].axis('off')
    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)
    plt.close(fig)


def save_asv_heatmap(asvs, output_dir):
    if not HAS_MPL:
        return
    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']
    datasets_list = list(DATASETS.keys())
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    for didx, dataset in enumerate(datasets_list):
        ax = axes[didx]
        subset = [r for r in mag_asvs if r['dataset'] == dataset]
        configs = sorted(set((r['model'], r['prompt']) for r in subset))
        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)
        for r in subset:
            ti = TOPOLOGIES.index(r['topology'])
            ci = configs.index((r['model'], r['prompt']))
            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan
        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',
                       vmin=0, vmax=2)
        ax.set_xticks(range(len(configs)))
        ax.set_xticklabels([f"{m[:3]}_{p[:3]}" for m, p in configs],
                           rotation=45, ha='right', fontsize=7)
        ax.set_yticks(range(len(TOPOLOGIES)))
        ax.set_yticklabels(TOPOLOGIES, fontsize=8)
        ax.set_title(f'{dataset} (K={DATASETS[dataset]["K"]})')
        plt.colorbar(im, ax=ax, shrink=0.8)
    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)
    plt.close(fig)


# ============================================================================
# JSON Serialization
# ============================================================================

def _to_json_safe(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    elif isinstance(obj, np.ndarray):
        return _to_json_safe(obj.tolist())
    elif isinstance(obj, dict):
        return {str(k): _to_json_safe(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_to_json_safe(v) for v in obj]
    elif isinstance(obj, (bool, np.bool_)):
        return bool(obj)
    elif isinstance(obj, float):
        return None if (np.isnan(obj) or np.isinf(obj)) else obj
    return obj


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')
    parser.add_argument('--data-dir', default='data/')
    parser.add_argument('--output-dir', default='artifacts/plan006/')
    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')
    parser.add_argument('--datasets', type=str, default=None,
                        help='Comma-separated dataset filter (e.g. humaid,vast)')
    parser.add_argument('--n-sim', type=int, default=1000)
    parser.add_argument('--device', type=str, default='cpu')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    t_total = time.time()
    n_precomp = 500_000 if args.mock else N_PRECOMP

    dataset_filter = None
    if args.datasets:
        dataset_filter = [d.strip() for d in args.datasets.split(',')]

    print("=" * 70)
    print("plan_006: Empirical ASV Calibration")
    if dataset_filter:
        print(f"  Dataset filter: {dataset_filter}")
    print("=" * 70)

    # --- 1. Confusion matrices ---
    if args.mock:
        print("\n[1/6] Generating mock confusion matrices...")
        confusion_matrices = generate_mock_confusion_matrices()
        if dataset_filter:
            confusion_matrices = {k: v for k, v in confusion_matrices.items()
                                  if k[0] in dataset_filter}
    else:
        print("\n[1/6] Loading confusion matrices...")
        confusion_matrices = load_all_confusion_matrices(args.data_dir,
                                                         dataset_filter=dataset_filter)

    print(f"  {len(confusion_matrices)} matrices loaded")
    for (ds, m, p), C in list(confusion_matrices.items())[:3]:
        K = DATASETS[ds]['K']
        print(f"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}")

    # --- 2. Precompute sufficient statistics ---
    print("\n[2/6] Precomputing sufficient statistics...")
    active_datasets = dataset_filter if dataset_filter else list(DATASETS.keys())
    K_values = sorted(set(DATASETS[ds]['K'] for ds in active_datasets if ds in DATASETS))
    all_suff_stats = {}
    all_tau_true = {}
    all_params = {}
    all_params_H0 = {}
    all_se_ref = {}

    for K in K_values:
        params = make_dgp_params(K)
        params_H0 = make_dgp_params_H0(K, params)
        all_params[K] = params
        all_params_H0[K] = params_H0
        for topology in TOPOLOGIES:
            seed = K * 1000 + abs(hash(topology)) % 1000
            st = precompute_suff_stats(K, topology, params[topology],
                                       N=n_precomp, seed=seed)
            plim_I = compute_plim(np.eye(K), st, K)
            tau_true = extract_tau(plim_I, topology)
            all_suff_stats[(K, topology)] = st
            all_tau_true[(K, topology)] = tau_true

            se = estimate_reference_se(K, topology, params[topology],
                                       N_ref=5000,
                                       n_mc=min(args.n_sim, 30),
                                       seed=seed + 500)
            all_se_ref[(K, topology)] = se
            se_s = f"{se:.4f}" if np.isfinite(se) else "N/A"
            print(f"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}")

    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)
    n_sign_flips = sum(1 for b in biases if b['sign_flip'])
    print(f"  {len(biases)} bias values ({n_sign_flips} sign flips)")

    # --- 3. ASV ---
    print("\n[3/6] Computing ASV values...")
    t3 = time.time()
    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,
                            all_tau_true, all_se_ref)
    print(f"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)")
    for at in ['magnitude', 'sign_flip', 'significance']:
        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]
        if sub:
            print(f"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} "
                  f"max={max(sub):.3f} ({len(sub)} non-None)")

    # --- 4. F1 vs bias ---
    print("\n[4/6] F1 vs bias analysis...")
    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)
    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]
    high_f1_high_bias = [r for r in total_high_f1
                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]
    if total_high_f1:
        pct = len(high_f1_high_bias) / len(total_high_f1) * 100
        print(f"  Baumann check: F1>0.93 with |bias|>0.05: "
              f"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%")
    # Sample rows
    for r in f1_bias[:3]:
        print(f"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: "
              f"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}")

    # --- 5. Type I/II ---
    print("\n[5/6] Type I/II error rates...")
    t5 = time.time()
    type1_type2_results = []
    n_configs = len(confusion_matrices) * len(TOPOLOGIES)
    idx = 0
    for (dataset, model, prompt), C in confusion_matrices.items():
        K = DATASETS[dataset]['K']
        for topology in TOPOLOGIES:
            idx += 1
            st = all_suff_stats[(K, topology)]
            tau_true = all_tau_true[(K, topology)]
            r = compute_type1_type2_for_C(
                C, K, topology, all_params[K], all_params_H0[K],
                st, tau_true,
                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)
            type1_type2_results.append({
                'dataset': dataset, 'model': model, 'prompt': prompt,
                'K': K, 'topology': topology, **r,
            })
            if idx % 50 == 0:
                print(f"    {idx}/{n_configs}...")
    print(f"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)")
    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])
    print(f"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}")

    # --- 6. Inter-model correlation ---
    print("\n[6/6] Inter-model error correlation...")
    inter_model_results = {}
    for dataset in DATASETS:
        K = DATASETS[dataset]['K']
        for prompt in PROMPTS:
            r = compute_inter_model_correlation(
                confusion_matrices, K, dataset, prompt,
                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)
            inter_model_results[f"{dataset}_{prompt}"] = r
    print(f"  {len(inter_model_results)} (dataset, prompt) pairs")
    for key, pairs in list(inter_model_results.items())[:2]:
        for pair, vals in pairs.items():
            print(f"    {key} {pair}: agree={vals['agreement']:.3f} "
                  f"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}")

    # --- Summary ---
    summary = {
        'f1_gt_093_total': len(total_high_f1),
        'f1_gt_093_with_high_bias_pct': (
            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),
        'ppi_recommended_scenarios': unsafe,
        'total_scenarios': len(type1_type2_results),
        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,
    }

    # --- Save ---
    output = _to_json_safe({
        'confusion_matrices': {
            f"{ds}_{m}_{p}": C.tolist()
            for (ds, m, p), C in confusion_matrices.items()
        },
        'biases': biases,
        'asvs': asvs,
        'f1_vs_bias': f1_bias,
        'type1_type2': type1_type2_results,
        'inter_model_correlation': inter_model_results,
        'summary': summary,
    })

    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

    # --- Plots ---
    save_f1_vs_bias_plot(f1_bias, args.output_dir)
    save_asv_heatmap(asvs, args.output_dir)
    if HAS_MPL:
        print(f"Plots saved to {args.output_dir}")

    # --- Validation ---
    with open(out_path) as f:
        data = json.load(f)
    n_null = str(data).count('null')
    print(f"\nValidation: JSON has {n_null} null values "
          f"(expected for NaN/None ASV entries)")
    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:
        print(f"  {section}: {len(data[section])} records")

    elapsed = time.time() - t_total
    print(f"\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)")
    print(f"\nSummary:")
    print(f"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%")
    print(f"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/"
          f"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)")
    print("=" * 70)


if __name__ == "__main__":
    main()
