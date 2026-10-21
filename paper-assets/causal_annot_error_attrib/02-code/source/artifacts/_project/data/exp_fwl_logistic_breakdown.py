#!/usr/bin/env python3
"""
FWL invariance breakdown under logistic regression.

Hypothesis: matrix-based corrections (e.g., Naive plug-in C^{-1} premultiplication
of the dummy matrix) achieve exactly 0% bias reduction on the treatment
coefficient under OLS by FWL, but achieve non-zero bias reduction under
logistic regression because the nonlinear link breaks the column-space
invariance argument.

DGP (confounding topology):
  A ~ Categorical(p_A), K=3
  T = D @ gamma_conf + eps_T
  Y_linear   = tau*T + D @ beta + eps_Y           (linear DGP)
  Y_logistic ~ Bernoulli(sigmoid(tau*T + D @ beta))  (logistic DGP)

Estimators:
  OLS uncorrected:        Y_linear ~ T + D*
  OLS Naive corrected:    Y_linear ~ T + (C^{-1} @ D*_full)[:, 1:]
  Logistic uncorrected:   Y_logistic ~ T + D*
  Logistic Naive corr.:   Y_logistic ~ T + (C^{-1} @ D*_full)[:, 1:]

Bias reduction = 1 - |tau_corrected - tau_true| / |tau_uncorrected - tau_true|.

Runs N=10,000 x 500 MC reps against the 6 VAST K=3 confusion matrices.
"""
import json
import os
import time

import numpy as np
from sklearn.linear_model import LogisticRegression

N_SAMPLES = 10_000
N_REPS = 500
SEED = 4242
K = 3
TAU = 0.5

# DGP parameters (confounding)
GAMMA_CONF = np.array([0.5, -0.3])
BETA = np.array([0.0, 1.0, -0.5])
P_A = np.array([1.0, 0.5, 1.0 / 3.0])
P_A = P_A / P_A.sum()


def dummy_encode(A, K=K):
    N = len(A)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    return D


def full_dummy_encode(A, K=K):
    N = len(A)
    D = np.zeros((N, K))
    for j in range(K):
        D[:, j] = (A == j).astype(float)
    return D


def misclassify(A, C, rng):
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)


def gen_confounding_linear(N, rng):
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    T = D @ GAMMA_CONF + rng.normal(0, 1, N)
    Y = TAU * T + D @ BETA[1:] + rng.normal(0, 1, N)
    return T, Y, A


def gen_confounding_logistic(N, rng):
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    T = D @ GAMMA_CONF + rng.normal(0, 1, N)
    eta = TAU * T + D @ BETA[1:]
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A


def naive_plugin_dummies(A_star, C):
    """Naive plug-in correction: per-sample C^{-1} applied to the K-dim one-hot
    of A*; return the (K-1) non-reference columns.

    D_corrected[i, :] = (C_inv @ e_{A*_i})[1:]
    """
    C_inv = np.linalg.inv(C)
    return C_inv[:, A_star].T[:, 1:]


def ols_tau(T, Y, D):
    N = len(Y)
    X = np.column_stack([np.ones(N), T, D])
    coef, *_ = np.linalg.lstsq(X, Y, rcond=None)
    return float(coef[1])


def logit_tau(T, Y, D):
    X = np.column_stack([T, D])
    lr = LogisticRegression(C=1e12, max_iter=2000, solver='lbfgs')
    lr.fit(X, Y)
    return float(lr.coef_[0, 0])


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
    return {n.replace('vast/', ''): cms[n] for n in names}


def compute_true_logistic_tau(n_oracle=2_000_000, seed=99999):
    """Oracle large-N value of the logistic estimand under correctly observed A."""
    rng = np.random.default_rng(seed)
    T, Y, A = gen_confounding_logistic(n_oracle, rng)
    D = dummy_encode(A)
    return logit_tau(T, Y, D)


def run():
    artifacts_dir = os.path.dirname(os.path.abspath(__file__))
    cm_path = os.path.join(artifacts_dir, 'plan011_frontier_cms.json')
    cms = load_vast_cms(cm_path)
    print(f'Loaded {len(cms)} VAST K=3 CMs: {list(cms.keys())}')

    print('Computing oracle logistic tau (N=2M)...')
    tau_log_true = compute_true_logistic_tau()
    print(f'  tau_true_ols     = {TAU:.6f}')
    print(f'  tau_true_logistic = {tau_log_true:.6f}  (large-N plim under correct A)')

    results = []
    t0 = time.time()
    for ci, (cm_name, C) in enumerate(cms.items()):
        cond_C = float(np.linalg.cond(C))
        rng = np.random.default_rng(SEED + ci * 7919)

        ols_un = np.zeros(N_REPS)
        ols_co = np.zeros(N_REPS)
        log_un = np.zeros(N_REPS)
        log_co = np.zeros(N_REPS)
        valid = 0

        for m in range(N_REPS):
            # Shared latent draw, two outcomes for paired comparison
            A = rng.choice(K, size=N_SAMPLES, p=P_A)
            D = dummy_encode(A)
            T = D @ GAMMA_CONF + rng.normal(0, 1, N_SAMPLES)
            Y_lin = TAU * T + D @ BETA[1:] + rng.normal(0, 1, N_SAMPLES)
            eta = TAU * T + D @ BETA[1:]
            prob = 1.0 / (1.0 + np.exp(-eta))
            Y_log = rng.binomial(1, prob, N_SAMPLES).astype(float)

            A_star = misclassify(A, C, rng)
            D_star = dummy_encode(A_star)
            D_corr = naive_plugin_dummies(A_star, C)

            try:
                ols_un[m] = ols_tau(T, Y_lin, D_star)
                ols_co[m] = ols_tau(T, Y_lin, D_corr)
                log_un[m] = logit_tau(T, Y_log, D_star)
                log_co[m] = logit_tau(T, Y_log, D_corr)
                valid += 1
            except Exception:
                ols_un[m] = ols_co[m] = log_un[m] = log_co[m] = np.nan

        m_ols_un = float(np.nanmean(ols_un))
        m_ols_co = float(np.nanmean(ols_co))
        m_log_un = float(np.nanmean(log_un))
        m_log_co = float(np.nanmean(log_co))

        bias_ols_un = abs(m_ols_un - TAU)
        bias_ols_co = abs(m_ols_co - TAU)
        bias_log_un = abs(m_log_un - tau_log_true)
        bias_log_co = abs(m_log_co - tau_log_true)

        # Per-rep bias (more honest than mean-of-estimates) for MC SE
        ols_un_bias_reps = np.abs(ols_un - TAU)
        ols_co_bias_reps = np.abs(ols_co - TAU)
        log_un_bias_reps = np.abs(log_un - tau_log_true)
        log_co_bias_reps = np.abs(log_co - tau_log_true)

        def br(bu, bc):
            return None if bu < 1e-12 else (1.0 - bc / bu)

        bred_ols = br(bias_ols_un, bias_ols_co)
        bred_log = br(bias_log_un, bias_log_co)

        # Bias reduction computed per-rep then averaged (sanity check / SE)
        def br_per_rep(bu_arr, bc_arr):
            ok = np.isfinite(bu_arr) & np.isfinite(bc_arr) & (bu_arr > 1e-12)
            if ok.sum() == 0:
                return None, None
            r = 1.0 - bc_arr[ok] / bu_arr[ok]
            return float(np.mean(r)), float(np.std(r) / np.sqrt(ok.sum()))

        bred_ols_rep, bred_ols_se = br_per_rep(ols_un_bias_reps, ols_co_bias_reps)
        bred_log_rep, bred_log_se = br_per_rep(log_un_bias_reps, log_co_bias_reps)

        # Diff-in-estimates (corrected vs uncorrected) — should be exactly 0 for OLS
        ols_diff = float(np.nanmean(ols_co - ols_un))
        log_diff = float(np.nanmean(log_co - log_un))
        ols_diff_max = float(np.nanmax(np.abs(ols_co - ols_un)))
        log_diff_max = float(np.nanmax(np.abs(log_co - log_un)))

        results.append({
            'cm_name': cm_name,
            'cond_C': cond_C,
            'min_diag': float(np.diag(C).min()),
            'n_valid': valid,
            'tau_true_ols': TAU,
            'tau_true_logistic': tau_log_true,
            'mean_tau_ols_uncorrected': m_ols_un,
            'mean_tau_ols_corrected': m_ols_co,
            'mean_tau_logistic_uncorrected': m_log_un,
            'mean_tau_logistic_corrected': m_log_co,
            'bias_ols_uncorrected': bias_ols_un,
            'bias_ols_corrected': bias_ols_co,
            'bias_logistic_uncorrected': bias_log_un,
            'bias_logistic_corrected': bias_log_co,
            'bias_reduction_ols': bred_ols,
            'bias_reduction_logistic': bred_log,
            'bias_reduction_ols_per_rep_mean': bred_ols_rep,
            'bias_reduction_ols_per_rep_se': bred_ols_se,
            'bias_reduction_logistic_per_rep_mean': bred_log_rep,
            'bias_reduction_logistic_per_rep_se': bred_log_se,
            'mean_ols_diff_co_minus_un': ols_diff,
            'max_ols_diff_co_minus_un': ols_diff_max,
            'mean_logistic_diff_co_minus_un': log_diff,
            'max_logistic_diff_co_minus_un': log_diff_max,
        })

        el = time.time() - t0
        eta_s = el / (ci + 1) * (len(cms) - ci - 1)
        print(f'  [{ci+1}/{len(cms)}] {cm_name:<28} '
              f'OLS_br={bred_ols if bred_ols is None else f"{bred_ols:+.4f}":>9s} '
              f'LOG_br={bred_log if bred_log is None else f"{bred_log:+.4f}":>9s} '
              f'OLS|max_diff|={ols_diff_max:.2e} '
              f'LOG|max_diff|={log_diff_max:.2e} '
              f'({el:.0f}s, ETA {eta_s:.0f}s)')

    # Aggregate across CMs
    bred_ols_all = [r['bias_reduction_ols'] for r in results if r['bias_reduction_ols'] is not None]
    bred_log_all = [r['bias_reduction_logistic'] for r in results if r['bias_reduction_logistic'] is not None]
    ols_max_diff_all = [r['max_ols_diff_co_minus_un'] for r in results]
    log_max_diff_all = [r['max_logistic_diff_co_minus_un'] for r in results]

    summary = {
        'mean_bias_reduction_ols': float(np.mean(bred_ols_all)) if bred_ols_all else None,
        'mean_bias_reduction_logistic': float(np.mean(bred_log_all)) if bred_log_all else None,
        'max_abs_bias_reduction_ols': float(np.max(np.abs(bred_ols_all))) if bred_ols_all else None,
        'max_abs_bias_reduction_logistic': float(np.max(np.abs(bred_log_all))) if bred_log_all else None,
        'max_ols_diff_co_minus_un': float(np.max(ols_max_diff_all)),
        'max_logistic_diff_co_minus_un': float(np.max(log_max_diff_all)),
    }

    output = {
        'config': {
            'N': N_SAMPLES,
            'n_reps': N_REPS,
            'K': K,
            'tau_true_ols': TAU,
            'tau_true_logistic': tau_log_true,
            'topology': 'confounding',
            'seed': SEED,
        },
        'results': results,
        'summary': summary,
    }

    out_path = os.path.join(artifacts_dir, 'exp_fwl_logistic_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f'\nWrote {out_path}')

    # Print summary table
    print('\n' + '=' * 90)
    print(f'{"CM":<28} {"OLS bias red.":>14} {"LOG bias red.":>14} {"OLS |Δ|":>12} {"LOG |Δ|":>12}')
    print('-' * 90)
    for r in results:
        bo = r['bias_reduction_ols']
        bl = r['bias_reduction_logistic']
        print(f'{r["cm_name"]:<28} '
              f'{(f"{bo:+.4%}" if bo is not None else "N/A"):>14} '
              f'{(f"{bl:+.4%}" if bl is not None else "N/A"):>14} '
              f'{r["max_ols_diff_co_minus_un"]:>12.2e} '
              f'{r["max_logistic_diff_co_minus_un"]:>12.2e}')
    print('-' * 90)
    print(f'{"MEAN":<28} '
          f'{(f"{summary["mean_bias_reduction_ols"]:+.4%}"):>14} '
          f'{(f"{summary["mean_bias_reduction_logistic"]:+.4%}"):>14} '
          f'{summary["max_ols_diff_co_minus_un"]:>12.2e} '
          f'{summary["max_logistic_diff_co_minus_un"]:>12.2e}')
    print('=' * 90)

    return output


if __name__ == '__main__':
    run()
