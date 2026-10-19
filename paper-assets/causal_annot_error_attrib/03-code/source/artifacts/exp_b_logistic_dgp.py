#!/usr/bin/env python3
"""
Exp-B: Logistic DGP Simulation

Validates sign-flip findings under nonlinear (logistic regression) DGP.
7 topologies (confounding, mediation, collider, exposure, mbias, frontdoor, iv)
× 6 real VAST K=3 CMs.  N=10,000 × 500 MC reps.

Each topology generates binary Y via a logistic link, then compares:
  - Linear estimator (OLS / 2SLS)
  - Nonlinear estimator (logistic regression / control-function)
under misclassified A*.
"""
import numpy as np
import json
import time
import os
from sklearn.linear_model import LogisticRegression

N_SAMPLES = 10_000
N_REPS = 500
SEED = 2026
TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'frontdoor', 'iv']

TAU = 0.5
BETA = np.array([0.0, 1.0, -0.5])
GAMMA_CONF = np.array([0.5, -0.3])
PI_IV = np.array([0.5, -0.3])

# Mediation parameters
MED_GAMMA = np.array([0.0, 0.5, -0.3])   # baseline logits for A|T
MED_DELTA = np.array([0.0, 0.8, -0.6])   # effect of T on A logits

# Collider parameters (T->A<-Y, so A depends on both T and Y)
COLL_G = np.array([0.0, 0.0, 0.0])       # baseline logits
COLL_DT = np.array([0.0, 0.5, -0.3])     # T -> A coefficients
COLL_DY = np.array([0.0, 0.8, 0.6])      # Y -> A coefficients

# M-bias parameters: U1->T, U1->A, U2->A, U2->Y, T->Y
MBIAS_DELTA_COEF = 1.0   # U1 -> T coefficient
MBIAS_LAM = 1.0           # U2 -> Y coefficient
MBIAS_A1 = np.array([0.0, 0.8, -0.5])    # U1 -> A logits
MBIAS_A2 = np.array([0.0, 0.6, 0.9])     # U2 -> A logits

# Front-door parameters: T->A->Y with U->T, U->Y
FD_ALPHA_U = 1.0          # U -> T coefficient
FD_LAM_U = 1.0            # U -> Y coefficient
FD_GAMMA = np.array([0.0, 0.5, -0.3])    # baseline logits for A|T
FD_DELTA = np.array([0.0, 1.0, -0.8])    # T -> A logit coefficients

K = 3
P_A = np.array([1/1, 1/2, 1/3])
P_A = P_A / P_A.sum()


def load_vast_cms(path):
    with open(path) as f:
        data = json.load(f)
    cms = {}
    for key, val in data.items():
        if key.startswith('vast/') and val.get('shape', [None])[0] == 3:
            cm = np.array(val['confusion_matrix_normalized'])
            if cm.shape == (3, 3):
                cms[key] = cm
    names = sorted(cms.keys())[:6]
    return {n: cms[n] for n in names}


def dummy_encode(A, K=3):
    N = len(A)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    return D


def misclassify(A, C, rng):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)


# ── DGP generators ──────────────────────────────────────────────

def gen_confounding(N, rng):
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    T = D @ GAMMA_CONF + rng.normal(0, 1, N)
    eta = TAU * T + D @ BETA[1:] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, None


def gen_exposure(N, rng):
    T = rng.normal(0, 1, N)
    logits = np.column_stack([
        np.zeros(N),
        0.3 * T + 0.2,
        -0.2 * T - 0.1,
    ])
    logits -= logits.max(axis=1, keepdims=True)
    probs = np.exp(logits)
    probs /= probs.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=N)[:, None]
    A = (u >= cum[:, :-1]).sum(axis=1).astype(int)
    D = dummy_encode(A)
    eta = D @ BETA[1:] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, None


def gen_iv(N, rng):
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    T = D @ PI_IV + rng.normal(0, 1, N)
    eta = TAU * T + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, D


def _softmax_sample(logits, rng):
    """Sample from softmax(logits) for each row. logits: (N, K)."""
    logits = logits - logits.max(axis=1, keepdims=True)
    probs = np.exp(logits)
    probs /= probs.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=logits.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def gen_mediation(N, rng):
    """Mediation: T -> A -> Y (with direct T -> Y).
    T is binary, A mediates via softmax, Y is binary (logistic link).
    """
    T = rng.binomial(1, 0.5, N).astype(float)
    # A | T via softmax
    logits = MED_GAMMA[None, :] + MED_DELTA[None, :] * T[:, None]
    A = _softmax_sample(logits, rng)
    D = dummy_encode(A)
    # Y via logistic link: P(Y=1) = sigmoid(tau*T + D@beta[1:] + beta[0])
    eta = TAU * T + D @ BETA[1:] + BETA[0] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, None


def gen_collider(N, rng):
    """Collider: T -> A <- Y.  A is caused by both T and Y.
    T ~ N(0,1), Y = tau*T + eps via logistic link (binary),
    then A | T, Y via softmax.
    """
    T = rng.normal(0, 1, N)
    # Generate binary Y first (logistic link, tau*T drives Y)
    eta_y = TAU * T + rng.normal(0, 1, N)
    prob_y = 1.0 / (1.0 + np.exp(-eta_y))
    Y = rng.binomial(1, prob_y, N).astype(float)
    # A | T, Y via softmax
    logits = (COLL_G[None, :] + COLL_DT[None, :] * T[:, None]
              + COLL_DY[None, :] * Y[:, None])
    A = _softmax_sample(logits, rng)
    return T, Y, A, None


def gen_mbias(N, rng):
    """M-bias: U1->T, U1->A, U2->A, U2->Y, T->Y.
    A is a collider of U1 and U2.  Adjusting for A introduces M-bias.
    Y is binary (logistic link).
    """
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = MBIAS_DELTA_COEF * U1 + rng.normal(0, 1, N)
    # A | U1, U2 via softmax
    logits = (np.zeros((N, K)) + MBIAS_A1[None, :] * U1[:, None]
              + MBIAS_A2[None, :] * U2[:, None])
    A = _softmax_sample(logits, rng)
    # Y via logistic link: tau*T + lam*U2 + noise
    eta = TAU * T + MBIAS_LAM * U2 + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, None


def gen_frontdoor(N, rng):
    """Front-door: T -> A -> Y with U -> T, U -> Y (unmeasured confounding).
    A is the front-door mediator.  Y is binary (logistic link).
    """
    U = rng.normal(0, 1, N)
    T = FD_ALPHA_U * U + rng.normal(0, 1, N)
    # A | T via softmax
    logits = FD_GAMMA[None, :] + FD_DELTA[None, :] * T[:, None]
    A = _softmax_sample(logits, rng)
    D = dummy_encode(A)
    # Y via logistic link: D@beta[1:] + lam_U*U + noise
    eta = D @ BETA[1:] + FD_LAM_U * U + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A, None


GEN = {
    'confounding': gen_confounding, 'mediation': gen_mediation,
    'collider': gen_collider, 'exposure': gen_exposure,
    'mbias': gen_mbias, 'frontdoor': gen_frontdoor, 'iv': gen_iv,
}


# ── Estimators ──────────────────────────────────────────────────

def est_logistic_confounding(T, Y, D_star):
    X = np.column_stack([T, D_star])
    try:
        lr = LogisticRegression(C=np.inf, max_iter=1000, solver='lbfgs')
        lr.fit(X, Y)
        return lr.coef_[0]
    except Exception:
        return np.full(X.shape[1], np.nan)


def est_linear_confounding(T, Y, D_star):
    N = len(Y)
    X = np.column_stack([np.ones(N), T, D_star])
    try:
        coef = np.linalg.lstsq(X, Y, rcond=None)[0]
        return coef[1:]
    except np.linalg.LinAlgError:
        return np.full(1 + D_star.shape[1], np.nan)


def est_logistic_exposure(Y, D_star):
    X = D_star
    try:
        lr = LogisticRegression(C=np.inf, max_iter=1000, solver='lbfgs')
        lr.fit(X, Y)
        return lr.coef_[0]
    except Exception:
        return np.full(X.shape[1], np.nan)


def est_linear_exposure(Y, D_star):
    N = len(Y)
    X = np.column_stack([np.ones(N), D_star])
    try:
        coef = np.linalg.lstsq(X, Y, rcond=None)[0]
        return coef[1:]
    except np.linalg.LinAlgError:
        return np.full(D_star.shape[1], np.nan)


def est_linear_2sls(T, Y, D_star):
    N = len(Y)
    X_fs = np.column_stack([np.ones(N), D_star])
    try:
        coef_fs = np.linalg.lstsq(X_fs, T, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.array([np.nan])
    T_hat = X_fs @ coef_fs
    X_ss = np.column_stack([np.ones(N), T_hat])
    try:
        coef_ss = np.linalg.lstsq(X_ss, Y, rcond=None)[0]
        return coef_ss[1:]
    except np.linalg.LinAlgError:
        return np.array([np.nan])


def est_control_function_iv(T, Y, D_star):
    N = len(Y)
    X_fs = np.column_stack([np.ones(N), D_star])
    try:
        coef_fs = np.linalg.lstsq(X_fs, T, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.full(2, np.nan)
    T_hat = X_fs @ coef_fs
    resid = T - T_hat
    X_ss = np.column_stack([T, resid])
    try:
        lr = LogisticRegression(C=np.inf, max_iter=1000, solver='lbfgs')
        lr.fit(X_ss, Y)
        return lr.coef_[0]
    except Exception:
        return np.full(2, np.nan)


# ── True parameters (large-N oracle) ──────────────────────────

def compute_true_params():
    """Compute oracle true parameters with N=2M for each topology."""
    N_oracle = 2_000_000
    rng = np.random.default_rng(9999)
    true = {}

    # --- Confounding ---
    T, Y, A, _ = gen_confounding(N_oracle, rng)
    D = dummy_encode(A)
    coef_log = est_logistic_confounding(T, Y, D)
    coef_lin = est_linear_confounding(T, Y, D)
    true['confounding'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- Mediation --- (same estimator form as confounding: Y ~ T + D)
    rng2 = np.random.default_rng(10001)
    T, Y, A, _ = gen_mediation(N_oracle, rng2)
    D = dummy_encode(A)
    coef_log = est_logistic_confounding(T, Y, D)
    coef_lin = est_linear_confounding(T, Y, D)
    true['mediation'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- Collider --- (estimator: Y ~ T + D*, conditioning on collider)
    rng3 = np.random.default_rng(10002)
    T, Y, A, _ = gen_collider(N_oracle, rng3)
    D = dummy_encode(A)
    coef_log = est_logistic_confounding(T, Y, D)
    coef_lin = est_linear_confounding(T, Y, D)
    true['collider'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- Exposure ---
    T, Y, A, _ = gen_exposure(N_oracle, rng)
    D = dummy_encode(A)
    coef_log = est_logistic_exposure(Y, D)
    coef_lin = est_linear_exposure(Y, D)
    true['exposure'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- M-bias --- (estimator: Y ~ T + D*, adjusting for M-bias collider)
    rng4 = np.random.default_rng(10003)
    T, Y, A, _ = gen_mbias(N_oracle, rng4)
    D = dummy_encode(A)
    coef_log = est_logistic_confounding(T, Y, D)
    coef_lin = est_linear_confounding(T, Y, D)
    true['mbias'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- Front-door --- (estimator: Y ~ T + D*, controlling for mediator)
    rng5 = np.random.default_rng(10004)
    T, Y, A, _ = gen_frontdoor(N_oracle, rng5)
    D = dummy_encode(A)
    coef_log = est_logistic_confounding(T, Y, D)
    coef_lin = est_linear_confounding(T, Y, D)
    true['frontdoor'] = {
        'logistic': coef_log.tolist(),
        'linear': coef_lin.tolist(),
    }

    # --- IV ---
    T, Y, A, D_true = gen_iv(N_oracle, rng)
    coef_2sls = est_linear_2sls(T, Y, D_true)
    coef_cf = est_control_function_iv(T, Y, D_true)
    true['iv'] = {
        'linear_2sls': coef_2sls.tolist(),
        'control_function': coef_cf.tolist(),
    }
    return true


# ── MC simulation ──────────────────────────────────────────────

def run_mc(cms):
    true_params = compute_true_params()
    print("True parameters (oracle N=2M):")
    for topo, vals in true_params.items():
        for model, coefs in vals.items():
            print(f"  {topo}/{model}: {[f'{c:.4f}' for c in coefs]}")

    results = []
    n_configs = len(TOPOLOGIES) * len(cms)
    idx = 0
    t0 = time.time()

    # Topologies that use the T+D regression form (same estimator as confounding)
    T_D_TOPOS = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}

    for topo in TOPOLOGIES:
        for cm_name, C in cms.items():
            idx += 1
            rng = np.random.default_rng(SEED + idx * 1000)
            short_name = cm_name.replace('vast/', '')

            # Load true parameters for this topology
            if topo == 'iv':
                true_2sls = np.array(true_params['iv']['linear_2sls'])
                true_cf = np.array(true_params['iv']['control_function'])
            elif topo == 'exposure':
                true_log = np.array(true_params['exposure']['logistic'])
                true_lin = np.array(true_params['exposure']['linear'])
            else:
                # confounding, mediation, collider, mbias, frontdoor
                true_log = np.array(true_params[topo]['logistic'])
                true_lin = np.array(true_params[topo]['linear'])

            log_coefs = []
            lin_coefs = []
            log_sf_any = 0
            lin_sf_any = 0
            log_sf_tau = 0
            lin_sf_tau = 0
            log_sf_dummy = 0
            lin_sf_dummy = 0
            valid = 0

            for m in range(N_REPS):
                T, Y, A, D_true = GEN[topo](N_SAMPLES, rng)
                A_star = misclassify(A, C, rng)
                D_star = dummy_encode(A_star)

                if topo in T_D_TOPOS:
                    # Y ~ T + D* (logistic and linear)
                    c_log = est_logistic_confounding(T, Y, D_star)
                    c_lin = est_linear_confounding(T, Y, D_star)
                    if np.all(np.isfinite(c_log)) and np.all(np.isfinite(c_lin)):
                        valid += 1
                        log_coefs.append(c_log)
                        lin_coefs.append(c_lin)
                        if np.any(np.sign(c_log) != np.sign(true_log)):
                            log_sf_any += 1
                        if np.any(np.sign(c_lin) != np.sign(true_lin)):
                            lin_sf_any += 1
                        if np.sign(c_log[0]) != np.sign(true_log[0]):
                            log_sf_tau += 1
                        if np.sign(c_lin[0]) != np.sign(true_lin[0]):
                            lin_sf_tau += 1
                        if np.any(np.sign(c_log[1:]) != np.sign(true_log[1:])):
                            log_sf_dummy += 1
                        if np.any(np.sign(c_lin[1:]) != np.sign(true_lin[1:])):
                            lin_sf_dummy += 1

                elif topo == 'exposure':
                    c_log = est_logistic_exposure(Y, D_star)
                    c_lin = est_linear_exposure(Y, D_star)
                    if np.all(np.isfinite(c_log)) and np.all(np.isfinite(c_lin)):
                        valid += 1
                        log_coefs.append(c_log)
                        lin_coefs.append(c_lin)
                        if np.any(np.sign(c_log) != np.sign(true_log)):
                            log_sf_any += 1
                        if np.any(np.sign(c_lin) != np.sign(true_lin)):
                            lin_sf_any += 1
                        log_sf_dummy += int(np.any(np.sign(c_log) != np.sign(true_log)))
                        lin_sf_dummy += int(np.any(np.sign(c_lin) != np.sign(true_lin)))

                elif topo == 'iv':
                    c_2sls = est_linear_2sls(T, Y, D_star)
                    c_cf = est_control_function_iv(T, Y, D_star)
                    if np.all(np.isfinite(c_2sls)) and np.all(np.isfinite(c_cf)):
                        valid += 1
                        lin_coefs.append(c_2sls)
                        log_coefs.append(c_cf)
                        if np.any(np.sign(c_2sls) != np.sign(true_2sls)):
                            lin_sf_any += 1
                        if np.any(np.sign(c_cf) != np.sign(true_cf)):
                            log_sf_any += 1
                        if np.sign(c_2sls[0]) != np.sign(true_2sls[0]):
                            lin_sf_tau += 1
                        if np.sign(c_cf[0]) != np.sign(true_cf[0]):
                            log_sf_tau += 1

            if valid > 0:
                log_arr = np.array(log_coefs)
                lin_arr = np.array(lin_coefs)

                if topo == 'iv':
                    log_mean_bias = float(np.mean(np.abs(log_arr - true_cf[None, :])))
                    lin_mean_bias = float(np.mean(np.abs(lin_arr - true_2sls[None, :])))
                    log_coef_means = log_arr.mean(axis=0).tolist()
                    lin_coef_means = lin_arr.mean(axis=0).tolist()
                    true_log_list = true_cf.tolist()
                    true_lin_list = true_2sls.tolist()
                    model_log = 'control_function'
                    model_lin = 'linear_2sls'
                else:
                    log_mean_bias = float(np.mean(np.abs(log_arr - true_log[None, :])))
                    lin_mean_bias = float(np.mean(np.abs(lin_arr - true_lin[None, :])))
                    log_coef_means = log_arr.mean(axis=0).tolist()
                    lin_coef_means = lin_arr.mean(axis=0).tolist()
                    true_log_list = true_log.tolist()
                    true_lin_list = true_lin.tolist()
                    model_log = 'logistic'
                    model_lin = 'linear'
            else:
                log_mean_bias = lin_mean_bias = None
                log_coef_means = lin_coef_means = None
                true_log_list = true_lin_list = None
                model_log = 'logistic' if topo != 'iv' else 'control_function'
                model_lin = 'linear' if topo != 'iv' else 'linear_2sls'

            def sfr(cnt):
                return cnt / valid if valid > 0 else None

            results.append({
                'topology': topo,
                'cm_name': short_name,
                'model': model_log,
                'sign_flip_rate': sfr(log_sf_any),
                'tau_sign_flip_rate': sfr(log_sf_tau),
                'dummy_sign_flip_rate': sfr(log_sf_dummy),
                'mean_bias': log_mean_bias,
                'coef_means': log_coef_means,
                'true_coefs': true_log_list,
                'n_valid': valid,
            })
            results.append({
                'topology': topo,
                'cm_name': short_name,
                'model': model_lin,
                'sign_flip_rate': sfr(lin_sf_any),
                'tau_sign_flip_rate': sfr(lin_sf_tau),
                'dummy_sign_flip_rate': sfr(lin_sf_dummy),
                'mean_bias': lin_mean_bias,
                'coef_means': lin_coef_means,
                'true_coefs': true_lin_list,
                'n_valid': valid,
            })

            el = time.time() - t0
            eta = el / idx * (n_configs - idx) if idx > 0 else 0
            log_sfr_val = sfr(log_sf_any)
            lin_sfr_val = sfr(lin_sf_any)
            log_s = f"{log_sfr_val:.3f}" if log_sfr_val is not None else "N/A"
            lin_s = f"{lin_sfr_val:.3f}" if lin_sfr_val is not None else "N/A"
            print(f"  [{idx}/{n_configs}] {topo:<13} {short_name:<30} "
                  f"log_SF={log_s} lin_SF={lin_s} "
                  f"valid={valid}/{N_REPS} ({el:.0f}s, ETA {eta:.0f}s)")

    return results, true_params


def _get_model_names(topo):
    """Return (nonlinear_model_name, linear_model_name) for a topology."""
    if topo == 'iv':
        return 'control_function', 'linear_2sls'
    return 'logistic', 'linear'


def build_comparison(results):
    comp = {}
    for topo in TOPOLOGIES:
        sub = [r for r in results if r['topology'] == topo]
        log_model, lin_model = _get_model_names(topo)

        def extract(model, field):
            return [r[field] for r in sub
                    if r['model'] == model and r[field] is not None]

        comp[topo] = {
            'nonlinear_mean_sf': float(np.mean(extract(log_model, 'sign_flip_rate'))) if extract(log_model, 'sign_flip_rate') else None,
            'linear_mean_sf': float(np.mean(extract(lin_model, 'sign_flip_rate'))) if extract(lin_model, 'sign_flip_rate') else None,
            'nonlinear_mean_tau_sf': float(np.mean(extract(log_model, 'tau_sign_flip_rate'))) if extract(log_model, 'tau_sign_flip_rate') else None,
            'linear_mean_tau_sf': float(np.mean(extract(lin_model, 'tau_sign_flip_rate'))) if extract(lin_model, 'tau_sign_flip_rate') else None,
            'nonlinear_model': log_model,
            'linear_model': lin_model,
            'n_cms': len(extract(log_model, 'sign_flip_rate')),
        }
    return comp


TOPO_LABELS = {
    'confounding': 'Confounding', 'mediation': 'Mediation',
    'collider': 'Collider', 'exposure': 'Exposure',
    'mbias': 'M-bias', 'frontdoor': 'Front-door', 'iv': 'IV',
}


def write_tex(results, path):
    lines = [
        r'\begin{table}[t]',
        r'\centering',
        r'\caption{Sign flip rates under linear vs.\ logistic DGP across 6 real confusion matrices (VAST, $K\!=\!3$). '
        r'SF$_\tau$: treatment coefficient only; SF$_\text{any}$: any coefficient. '
        r'Each cell: $N\!=\!10{,}000 \times 500$ MC reps.}',
        r'\label{tab:logistic-robustness}',
        r'\small\setlength{\tabcolsep}{3pt}',
        r'\begin{tabular}{llrrrr}',
        r'\toprule',
        r' & & \multicolumn{2}{c}{Linear} & \multicolumn{2}{c}{Nonlinear} \\',
        r'\cmidrule(lr){3-4} \cmidrule(lr){5-6}',
        r'Topology & CM & SF$_\tau$ & SF$_\text{any}$ & SF$_\tau$ & SF$_\text{any}$ \\',
        r'\midrule',
    ]

    for ti, topo in enumerate(TOPOLOGIES):
        if ti > 0:
            lines.append(r'\midrule')
        topo_label = TOPO_LABELS.get(topo, topo.capitalize())
        log_model, lin_model = _get_model_names(topo)

        sub = [r for r in results if r['topology'] == topo]
        cm_names = sorted(set(r['cm_name'] for r in sub))
        first = True
        for cm in cm_names:
            lin_r = next((r for r in sub if r['cm_name'] == cm and r['model'] == lin_model), None)
            log_r = next((r for r in sub if r['cm_name'] == cm and r['model'] == log_model), None)

            def fmt(r, field):
                if r and r.get(field) is not None:
                    return f"{r[field]:.3f}"
                return '--'

            tl = topo_label if first else ''
            cm_short = cm.replace('_', r'\_')
            if topo == 'exposure':
                lin_tau = '--'
                log_tau = '--'
            else:
                lin_tau = fmt(lin_r, 'tau_sign_flip_rate')
                log_tau = fmt(log_r, 'tau_sign_flip_rate')
            lin_any = fmt(lin_r, 'sign_flip_rate')
            log_any = fmt(log_r, 'sign_flip_rate')
            lines.append(f'{tl} & {cm_short} & {lin_tau} & {lin_any} & {log_tau} & {log_any} \\\\')
            first = False

    lines += [
        r'\bottomrule',
        r'\end{tabular}',
        r'\end{table}',
    ]
    with open(path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def clean(o):
    if isinstance(o, (float, np.floating)):
        v = float(o)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean(v) for v in o]
    return o


def main():
    t0 = time.time()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    cm_path = os.path.join(out_dir, 'plan011_frontier_cms.json')

    cms = load_vast_cms(cm_path)
    print(f"Loaded {len(cms)} VAST K=3 CMs: {list(cms.keys())}")

    results, true_params = run_mc(cms)

    comp = build_comparison(results)
    output = clean({
        'results': results,
        'comparison_with_linear': comp,
        'true_params': true_params,
        'config': {
            'N': N_SAMPLES, 'n_reps': N_REPS, 'K': K,
            'tau': TAU, 'beta': BETA.tolist(),
            'topologies': TOPOLOGIES,
        },
    })

    jpath = os.path.join(out_dir, 'exp_b_logistic_results.json')
    with open(jpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON -> {jpath}")

    tpath = os.path.join(out_dir, 'exp_b_logistic_table.tex')
    write_tex(results, tpath)
    print(f"TeX  -> {tpath}")

    total = time.time() - t0
    print(f"\nDone in {total:.0f}s ({total/60:.1f}min)")

    print("\nComparison summary (any-coef SF / tau-only SF):")
    for topo, c in comp.items():
        nl = c['nonlinear_mean_sf']
        li = c['linear_mean_sf']
        nl_tau = c['nonlinear_mean_tau_sf']
        li_tau = c['linear_mean_tau_sf']
        def s(v): return f"{v:.4f}" if v is not None else 'N/A'
        print(f"  {topo:<13}: linear={s(li)}/{s(li_tau)} "
              f"nonlinear={s(nl)}/{s(nl_tau)} ({c['nonlinear_model']})")


if __name__ == '__main__':
    main()
