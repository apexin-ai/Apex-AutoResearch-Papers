"""
exp-041: Asymmetric Misclassification MC Simulation
Validates bias identity R², diagnostic AUC degradation, EC-HTE RMSE and coverage
under asymmetric FPR≠FNR across a 48-config grid.
"""

import numpy as np
import pandas as pd
import time
import sys
import warnings
from itertools import product
from multiprocessing import Pool, cpu_count
from scipy.special import gammaln
from scipy.optimize import minimize_scalar
from sklearn.metrics import roc_auc_score

warnings.filterwarnings('ignore')

# === Constants ===
N = 5000
N_EXPERT = 250
N_MC = 100

FPR_FNR_RATIOS = {
    '1:2': 0.5, '1:3': 1/3, '1:5': 0.2,
    '2:1': 2.0, '3:1': 3.0, '5:1': 5.0,
}
K_VALUES = [2, 4]
DELTA_PI_VALUES = [0.05, 0.10, 0.15, 0.20]

BASE_PI = 0.20


# === FPR/FNR Generation ===

def generate_fpr_fnr(K, delta_pi, ratio, rng):
    """Generate per-subgroup FPR and FNR from ratio and delta_pi.

    Given total misclassification rate pi_s per subgroup and ratio r = FPR/FNR:
      pi_s = (FPR_s + FNR_s) / 2
      FPR_s = r * FNR_s
      => FNR_s = 2 * pi_s / (1 + r)
      => FPR_s = r * FNR_s
    """
    if K == 2:
        pi_vals = np.array([BASE_PI - delta_pi / 2, BASE_PI + delta_pi / 2])
    else:
        offsets = np.linspace(-1.5, 1.5, K)
        pi_vals = BASE_PI + offsets * delta_pi / 3.0

    pi_vals = np.clip(pi_vals, 0.03, 0.45)

    fpr = np.zeros(K)
    fnr = np.zeros(K)
    for s in range(K):
        fnr_s = 2 * pi_vals[s] / (1 + ratio)
        fpr_s = ratio * fnr_s
        fpr_s = np.clip(fpr_s, 0.005, 0.49)
        fnr_s = np.clip(fnr_s, 0.005, 0.49)
        fpr[s] = fpr_s
        fnr[s] = fnr_s

    return fpr, fnr, pi_vals


# === DGP ===

def generate_data(K, fpr, fnr, seed):
    rng = np.random.RandomState(seed)

    T = rng.binomial(1, 0.5, N)
    Z = rng.binomial(1, 0.5, N)
    S = rng.choice(K, N, p=[1/K]*K)
    X = rng.randn(N, 3)

    tau_z1 = 0.4
    tau_z0 = 0.1
    tau = np.where(Z == 1, tau_z1, tau_z0)
    eps = rng.randn(N)
    Y = 1.0 + tau * T + 0.3 * X[:, 0] + eps

    Z_hat = Z.copy()
    for s in range(K):
        s_mask = S == s
        z_s = Z[s_mask]
        flip_prob = np.where(z_s == 0, fpr[s], fnr[s])
        flip = rng.rand(s_mask.sum()) < flip_prob
        Z_hat[s_mask] = np.where(flip, 1 - z_s, z_s)

    expert_idx = rng.choice(N, N_EXPERT, replace=False)
    expert_mask = np.zeros(N, dtype=bool)
    expert_mask[expert_idx] = True

    return {
        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,
        'tau_z0': tau_z0, 'tau_z1': tau_z1,
        'expert_mask': expert_mask,
    }


# === Confusion Matrix Estimators ===

def estimate_cm_mle(z_true, z_hat):
    C = np.zeros((2, 2))
    for zt in [0, 1]:
        mask = z_true == zt
        for zh in [0, 1]:
            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)
    return C


def _dirmult_neg_ll(alpha, count_list):
    a = alpha
    if a < 1e-10:
        return 1e10
    ll = 0.0
    for c0, c1 in count_list:
        n = c0 + c1
        if n == 0:
            continue
        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
        ll -= 2 * gammaln(a) - gammaln(2 * a)
    return -ll


def estimate_cm_hb(counts_3d, K):
    """HB MAP-EB estimator for asymmetric confusion matrices."""
    alpha_opt = np.zeros(2)
    for z in [0, 1]:
        cl = [(int(counts_3d[i, z, 0]), int(counts_3d[i, z, 1])) for i in range(K)]
        total = sum(c0 + c1 for c0, c1 in cl)
        if total == 0:
            alpha_opt[z] = 3.0
            continue

        def neg_log_post(a, _cl=cl):
            nll = _dirmult_neg_ll(a, _cl)
            if a < 1e-10:
                return 1e10
            log_prior = 2.0 * np.log(a) - a
            return nll - log_prior

        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
        alpha_opt[z] = res.x

    C_hb = {}
    for i in range(K):
        C_s = np.zeros((2, 2))
        for z in [0, 1]:
            a = alpha_opt[z] / 2.0
            n_sz = counts_3d[i, z, :].sum()
            d = n_sz + 2 * a
            C_s[z, 0] = (counts_3d[i, z, 0] + a) / d if d > 0 else 0.5
            C_s[z, 1] = (counts_3d[i, z, 1] + a) / d if d > 0 else 0.5
        C_hb[i] = C_s

    return C_hb


def get_expert_counts(Z, Z_hat, S, expert_mask, K):
    counts = np.zeros((K, 2, 2), dtype=int)
    for s in range(K):
        ms = (S == s) & expert_mask
        for z in [0, 1]:
            mz = ms & (Z == z)
            counts[s, z, 0] = (Z_hat[mz] == 0).sum()
            counts[s, z, 1] = (Z_hat[mz] == 1).sum()
    return counts


# === Correction Methods ===

def diff_in_means(Y, T, mask):
    t1 = mask & (T == 1)
    t0 = mask & (T == 0)
    n1, n0 = t1.sum(), t0.sum()
    if n1 < 2 or n0 < 2:
        return np.nan, np.nan
    y1, y0 = Y[t1], Y[t0]
    tau_hat = y1.mean() - y0.mean()
    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
    return tau_hat, se


def build_mixing_matrix(C, p_z, p_z_hat):
    M = np.zeros((2, 2))
    for zh in [0, 1]:
        for z in [0, 1]:
            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]
    return M


def invert_mixing(M, tau_obs, se_obs):
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    M_inv = np.linalg.inv(M)
    tau_corrected = M_inv @ tau_obs
    sigma_obs = np.diag(se_obs ** 2)
    sigma_corrected = M_inv @ sigma_obs @ M_inv.T
    se_corrected = np.sqrt(np.maximum(np.diag(sigma_corrected), 0))
    return tau_corrected, se_corrected


# === Analytic Bias (for R² computation) ===

def compute_analytic_bias(fpr, fnr, K):
    """Compute analytic bias coefficients B_s for each subgroup.

    B_s = M_global^{-1} M_s - I
    bias(z, s) = [B_s @ tau]_z = delta_tau * [B_s]_{z,1}
    """
    p_z = np.array([0.5, 0.5])
    w = 1.0 / K

    M_global = np.zeros((2, 2))
    M_list = []
    for s in range(K):
        C_s = np.array([[1 - fpr[s], fpr[s]],
                        [fnr[s], 1 - fnr[s]]])
        p_zh = C_s.T @ p_z
        M_s = build_mixing_matrix(C_s, p_z, p_zh)
        M_list.append(M_s)
        M_global += w * M_s

    det_g = np.linalg.det(M_global)
    if abs(det_g) < 1e-10:
        return None, None

    M_global_inv = np.linalg.inv(M_global)
    B_list = []
    for s in range(K):
        B_s = M_global_inv @ M_list[s] - np.eye(2)
        B_list.append(B_s)

    return B_list, M_list


# === One MC Run ===

def run_one_mc(args):
    K, fpr, fnr, seed = args
    data = generate_data(K, fpr, fnr, seed)
    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
    expert_mask = data['expert_mask']
    tau_z0, tau_z1 = data['tau_z0'], data['tau_z1']

    # Global CM from expert labels
    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])
    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)
    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)

    # Per-subgroup CMs
    counts_3d = get_expert_counts(Z, Z_hat, S, expert_mask, K)
    C_hb = estimate_cm_hb(counts_3d, K)

    C_mle_sub = {}
    for s in range(K):
        expert_s = expert_mask & (S == s)
        if expert_s.sum() >= 4:
            C_mle_sub[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])
        else:
            C_mle_sub[s] = C_global

    rows = []

    for s in range(K):
        s_mask = S == s
        expert_s = expert_mask & s_mask
        if expert_s.sum() >= 4:
            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)
        else:
            p_z_s = p_z_global
        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)

        base = {'subgroup': s, 'mc_run': seed, 'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}

        def make_row(method, th0, th1, se0, se1):
            return {**base, 'method': method,
                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
                    'se_z0': se0 if not np.isnan(se0) else np.nan,
                    'se_z1': se1 if not np.isnan(se1) else np.nan,
                    'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,
                    'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,
                    'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,
                    'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}

        # Oracle
        th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))
        th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))
        rows.append(make_row('oracle', th0, th1, se0, se1))

        # Naive
        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
        rows.append(make_row('naive', th0, th1, se0, se1))

        # Global corrected
        th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))
        th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))
        if not (np.isnan(th0_obs) or np.isnan(th1_obs)):
            M_g = build_mixing_matrix(C_global, p_z_global, p_zh_global)
            tau_corr, se_corr = invert_mixing(M_g, np.array([th0_obs, th1_obs]), np.array([se0_obs, se1_obs]))
            rows.append(make_row('global_corrected', tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]))
        else:
            rows.append(make_row('global_corrected', np.nan, np.nan, np.nan, np.nan))

        # EC-HTE (HB)
        if not (np.isnan(th0_obs) or np.isnan(th1_obs)):
            M_s = build_mixing_matrix(C_hb[s], p_z_s, p_zh_s)
            tau_corr, se_corr = invert_mixing(M_s, np.array([th0_obs, th1_obs]), np.array([se0_obs, se1_obs]))
            rows.append(make_row('ec_hte', tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]))
        else:
            rows.append(make_row('ec_hte', np.nan, np.nan, np.nan, np.nan))

    return rows


# === Aggregation ===

def aggregate_config(df_raw, fpr, fnr, K, ratio_label, delta_pi):
    """Aggregate MC runs for one config. Compute bias, RMSE, coverage, R², diagnostic AUC."""

    tau_z0 = df_raw['tau_true_z0'].iloc[0]
    tau_z1 = df_raw['tau_true_z1'].iloc[0]
    delta_tau = tau_z1 - tau_z0

    # --- Per-method aggregation ---
    method_rows = []
    group_cols = ['subgroup', 'method']
    for (sub, method), grp in df_raw.groupby(group_cols):
        row = {'subgroup': sub, 'method': method}
        for z, tz in [('z0', tau_z0), ('z1', tau_z1)]:
            err = grp[f'tau_hat_{z}'] - tz
            valid = err.dropna()
            if len(valid) == 0:
                row.update({f'bias_{z}': np.nan, f'abs_bias_{z}': np.nan,
                            f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})
                continue
            row[f'bias_{z}'] = valid.mean()
            row[f'abs_bias_{z}'] = valid.abs().mean()
            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())
            covered = ((grp[f'ci_lower_{z}'] <= tz) & (tz <= grp[f'ci_upper_{z}'])).mean()
            row[f'coverage_{z}'] = covered
        method_rows.append(row)

    df_methods = pd.DataFrame(method_rows)

    # --- Bias identity R² ---
    B_list, M_list = compute_analytic_bias(fpr, fnr, K)
    r2 = np.nan
    if B_list is not None:
        analytic_biases = []
        mc_biases = []
        for s in range(K):
            for z_idx, z_label in enumerate(['z0', 'z1']):
                analytic_b = delta_tau * B_list[s][z_idx, 1]
                sub_gc = df_methods[(df_methods['subgroup'] == s) & (df_methods['method'] == 'global_corrected')]
                if len(sub_gc) > 0:
                    mc_b = sub_gc[f'bias_{z_label}'].values[0]
                    if not np.isnan(mc_b):
                        analytic_biases.append(analytic_b)
                        mc_biases.append(mc_b)

        if len(analytic_biases) >= 3:
            analytic_biases = np.array(analytic_biases)
            mc_biases = np.array(mc_biases)
            ss_res = np.sum((mc_biases - analytic_biases)**2)
            ss_tot = np.sum((mc_biases - mc_biases.mean())**2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else np.nan

    # --- Diagnostic AUC ---
    diag_auc = np.nan
    if B_list is not None and K >= 2:
        labels = []
        scores = []
        for s in range(K):
            for z_idx, z_label in enumerate(['z0', 'z1']):
                sub_naive = df_methods[(df_methods['subgroup'] == s) & (df_methods['method'] == 'naive')]
                sub_gc = df_methods[(df_methods['subgroup'] == s) & (df_methods['method'] == 'global_corrected')]
                if len(sub_naive) > 0 and len(sub_gc) > 0:
                    naive_abs = abs(sub_naive[f'bias_{z_label}'].values[0])
                    gc_abs = abs(sub_gc[f'bias_{z_label}'].values[0])
                    if not (np.isnan(naive_abs) or np.isnan(gc_abs)):
                        hurts = int(gc_abs > naive_abs)
                        score = abs(B_list[s][z_idx, 1])
                        labels.append(hurts)
                        scores.append(score)

        if len(set(labels)) == 2 and len(labels) >= 4:
            try:
                diag_auc = roc_auc_score(labels, scores)
            except:
                pass

    # --- Summary rows ---
    summary_rows = []
    for method in ['oracle', 'naive', 'global_corrected', 'ec_hte']:
        sub = df_methods[df_methods['method'] == method]
        if len(sub) == 0:
            continue
        mean_abs_bias = np.nanmean([sub[f'abs_bias_{z}'].mean() for z in ['z0', 'z1']])
        mean_rmse = np.nanmean([sub[f'rmse_{z}'].mean() for z in ['z0', 'z1']])
        mean_coverage = np.nanmean([sub[f'coverage_{z}'].mean() for z in ['z0', 'z1']])

        summary_rows.append({
            'fpr_fnr_ratio': ratio_label,
            'K': K,
            'delta_pi': delta_pi,
            'method': method,
            'mean_abs_bias': mean_abs_bias,
            'rmse': mean_rmse,
            'coverage': mean_coverage,
            'r2': r2,
            'diagnostic_auc': diag_auc,
        })

    return summary_rows


# === Main ===

def run_experiment(n_mc=N_MC, n_workers=None, test_mode=False):
    if n_workers is None:
        n_workers = min(cpu_count(), 8)

    configs = []
    for ratio_label, ratio_val in FPR_FNR_RATIOS.items():
        for K in K_VALUES:
            for dp in DELTA_PI_VALUES:
                fpr, fnr, pi_vals = generate_fpr_fnr(K, dp, ratio_val, np.random.RandomState(0))
                configs.append((ratio_label, ratio_val, K, dp, fpr, fnr, pi_vals))

    if test_mode:
        configs = configs[:1]
        n_mc = 10
        print(f"TEST MODE: 1 config, {n_mc} MC runs")

    print(f"exp-041: Asymmetric Misclassification MC")
    print(f"  {len(configs)} configs × {n_mc} MC runs = {len(configs) * n_mc} total")
    print(f"  Workers: {n_workers}")
    print()

    all_raw = []
    all_summary = []
    t0 = time.time()

    for ci, (ratio_label, ratio_val, K, dp, fpr, fnr, pi_vals) in enumerate(configs):
        config_t0 = time.time()

        mc_args = [(K, fpr, fnr, 42 + mc) for mc in range(n_mc)]

        if n_workers > 1:
            with Pool(n_workers) as pool:
                results = pool.map(run_one_mc, mc_args)
        else:
            results = [run_one_mc(a) for a in mc_args]

        config_rows = []
        for r in results:
            config_rows.extend(r)

        df_config = pd.DataFrame(config_rows)
        df_config['fpr_fnr_ratio'] = ratio_label
        df_config['K'] = K
        df_config['delta_pi'] = dp
        all_raw.append(df_config)

        summary = aggregate_config(df_config, fpr, fnr, K, ratio_label, dp)
        all_summary.extend(summary)

        elapsed = time.time() - t0
        config_time = time.time() - config_t0
        eta = elapsed / (ci + 1) * (len(configs) - ci - 1)
        r2_val = summary[0]['r2'] if summary else np.nan
        print(f"  [{ci+1}/{len(configs)}] ratio={ratio_label} K={K} dp={dp:.2f} "
              f"R²={r2_val:.4f} | {config_time:.1f}s (ETA {eta:.0f}s)")

    df_raw = pd.concat(all_raw, ignore_index=True)
    df_summary = pd.DataFrame(all_summary)

    base = '/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/results'
    raw_path = f'{base}/exp041_asymmetric_grid.csv'
    sum_path = f'{base}/exp041_asymmetric_summary.csv'
    df_raw.to_csv(raw_path, index=False)
    df_summary.to_csv(sum_path, index=False)

    total_time = time.time() - t0
    print(f"\nTotal time: {total_time:.1f}s")
    print(f"Saved: {raw_path}")
    print(f"Saved: {sum_path}")

    return df_raw, df_summary


if __name__ == '__main__':
    test_mode = '--test' in sys.argv
    n_mc = N_MC
    if '--mc' in sys.argv:
        idx = sys.argv.index('--mc')
        n_mc = int(sys.argv[idx + 1])

    df_raw, df_summary = run_experiment(n_mc=n_mc, test_mode=test_mode)

    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 200)
    pd.set_option('display.float_format', '{:.4f}'.format)
    print("\n=== Summary ===")
    print(df_summary.to_string(index=False))
