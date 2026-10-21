"""
exp-007: PPCI + DSL Baseline Comparison for EC-HTE
Compares measurement-model-level correction (EC-HTE) vs estimand-level correction (DSL)
vs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification,
outcome Y has no measurement error.
"""

import numpy as np
import pandas as pd
import sys
import time
import warnings
warnings.filterwarnings('ignore')

# === DGP ===

REGIMES = {
    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},
    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},
    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},
}

MISCLASS_K2 = {
    'extreme':     [0.25, 0.05],
    'moderate':    [0.15, 0.10],
    'homogeneous': [0.12, 0.12],
}

MISCLASS_K4 = {
    'extreme':     [0.30, 0.20, 0.10, 0.03],
    'moderate':    [0.20, 0.15, 0.10, 0.05],
    'homogeneous': [0.12, 0.12, 0.12, 0.12],
}

N = 5000
N_EXPERTS = [50, 100, 250, 500]
N_MC = 100


def generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed):
    """Generate synthetic data with pure covariate-error DGP.

    Only Z has misclassification (LLM annotation error). Y has no measurement error.
    T is randomized (Bernoulli 0.5). Effect modifier Z is binary.

    Args:
        regime_params: dict with tau_z0, tau_z1
        misclass_rates: list of k misclassification rates per subgroup
        n_expert: number of expert-labeled observations
        k_subgroups: number of subgroups
        seed: random seed

    Returns:
        dict with T, Z, Z_hat, S, X, Y, tau, expert_mask
    """
    rng = np.random.RandomState(seed)
    k = k_subgroups

    T = rng.binomial(1, 0.5, N)
    Z = rng.binomial(1, 0.5, N)
    S = rng.choice(k, N, p=[1/k]*k)
    X = rng.randn(N, 5)

    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
    eps = rng.randn(N)
    Y = 1 + tau * T + 0.5 * X[:, 0] + eps

    mc_rates = np.array([misclass_rates[s] for s in S])
    flip = rng.rand(N) < mc_rates
    Z_hat = np.where(flip, 1 - Z, Z)

    expert_idx = rng.choice(N, n_expert, replace=False)
    expert_mask = np.zeros(N, dtype=bool)
    expert_mask[expert_idx] = True

    return {
        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,
        'tau': tau, 'expert_mask': expert_mask,
    }


# === Confusion Matrix Estimators ===

def estimate_cm_mle(z_true, z_hat):
    """MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z)."""
    C = np.zeros((2, 2))
    for zt in [0, 1]:
        mask = z_true == zt
        for zh in [0, 1]:
            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)
    return C


def estimate_cm_hb(z_true, z_hat, all_subgroup_data):
    """Hierarchical Bayesian confusion matrix estimator (placeholder).

    TODO: Import from exp-001 when complete. Uses Dirichlet-Multinomial
    hierarchical model with partial pooling across subgroups.

    Args:
        z_true: expert Z labels for this subgroup
        z_hat: Z_hat values for this subgroup
        all_subgroup_data: list of (z_true_s, z_hat_s) for all subgroups
            (needed for partial pooling)

    Returns:
        C: 2x2 confusion matrix (posterior mean)
    """
    return estimate_cm_mle(z_true, z_hat)


# === Correction Methods ===

def diff_in_means(Y, T, mask):
    """Difference-in-means estimator for subpopulation defined by mask."""
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
    """M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule."""
    M = np.zeros((2, 2))
    for zh in [0, 1]:
        for z in [0, 1]:
            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]
    return M


def invert_mixing(M, tau_obs, se_obs):
    """Apply M^{-1} correction. Returns (tau_corrected, se_corrected)."""
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    M_inv = np.linalg.inv(M)
    tau_corrected = M_inv @ tau_obs
    sigma_obs = np.diag(se_obs ** 2)
    sigma_corrected = M_inv @ sigma_obs @ M_inv.T
    se_corrected = np.sqrt(np.diag(sigma_corrected))
    return tau_corrected, se_corrected


def method_oracle(data, s_val):
    """Oracle: use true Z within subgroup s."""
    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']
    s_mask = S == s_val
    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))
    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))
    return th0, th1, se0, se1


def method_naive(data, s_val):
    """Naive: use Z_hat within subgroup s, no correction."""
    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
    s_mask = S == s_val
    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
    return th0, th1, se0, se1


def method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):
    """Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs."""
    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
    s_mask = S == s_val

    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
    if np.isnan(th0) or np.isnan(th1):
        return np.nan, np.nan, np.nan, np.nan

    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)
    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))
    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]


def method_dsl(data, s_val, C_s, p_z_s, p_zh_s):
    """DSL (Direct Subgroup-Level): per-subgroup independent correction.

    Each subgroup estimates its own confusion matrix independently (no pooling).
    This is estimand-level correction -- correct the CATE estimate directly
    using the subgroup's own confusion matrix.

    Key difference from EC-HTE: no cross-subgroup shrinkage.
    When n_expert is small per subgroup, DSL has high variance.
    """
    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
    s_mask = S == s_val

    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
    if np.isnan(th0) or np.isnan(th1):
        return np.nan, np.nan, np.nan, np.nan

    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)
    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))
    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]


def method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):
    """EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.

    Uses HB estimator (partial pooling) for confusion matrix, then applies
    subgroup-level correction. The key advantage over DSL is that the
    confusion matrix estimate borrows strength across subgroups.

    TODO: Use HB posterior mean from exp-001 Gibbs/PyMC sampler.
    Currently falls back to MLE (same as DSL) until HB is integrated.
    """
    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
    s_mask = S == s_val

    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
    if np.isnan(th0) or np.isnan(th1):
        return np.nan, np.nan, np.nan, np.nan

    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)
    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))
    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]


# === PPCI Method (Placeholder) ===

def method_ppci(data, s_val, expert_mask_s, Z_s, Z_hat_s):
    """PPCI (Posterior Predictive Correction of Inference).

    Standard literature approach: uses posterior predictive distribution of
    true labels to correct inference. Typically involves:
    1. Fit classification model P(Z | Z_hat, covariates) on expert labels
    2. Generate multiple imputed Z from posterior predictive
    3. Run analysis on each imputed dataset
    4. Combine results (Rubin's rules)

    TODO: Implement full PPCI pipeline.
    """
    return np.nan, np.nan, np.nan, np.nan


# === Main Simulation Loop ===

def run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed):
    """Run one MC iteration for all methods."""
    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed)
    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
    expert_mask = data['expert_mask']
    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']

    # Global confusion matrix (from all expert labels)
    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])
    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)
    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)

    # Per-subgroup confusion matrices
    C_mle = {}
    C_hb = {}
    all_subgroup_expert_data = []

    for s in range(k_subgroups):
        s_mask = S == s
        expert_s = expert_mask & s_mask
        if expert_s.sum() >= 4:
            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])
            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))
        else:
            C_mle[s] = C_global
            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))

    # HB estimates (placeholder — will use exp-001 code)
    for s in range(k_subgroups):
        s_mask = S == s
        expert_s = expert_mask & s_mask
        if expert_s.sum() >= 4:
            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)
        else:
            C_hb[s] = C_global

    rows = []
    base = {
        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,
        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,
    }

    def make_row(method, subgroup, th0, th1, se0, se1):
        return {**base, 'method': method, 'subgroup': subgroup,
                'tau_hat_z0': th0, 'tau_hat_z1': th1,
                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,
                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,
                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,
                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}

    for s in range(k_subgroups):
        s_mask = S == s
        expert_s = expert_mask & s_mask
        if expert_s.sum() >= 4:
            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)
        else:
            p_z_s = p_z_global
        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)

        # Oracle
        th0, th1, se0, se1 = method_oracle(data, s)
        rows.append(make_row('oracle', s, th0, th1, se0, se1))

        # Naive
        th0, th1, se0, se1 = method_naive(data, s)
        rows.append(make_row('naive', s, th0, th1, se0, se1))

        # Global-corrected
        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)
        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))

        # DSL
        th0, th1, se0, se1 = method_dsl(data, s, C_mle[s], p_z_s, p_zh_s)
        rows.append(make_row('dsl', s, th0, th1, se0, se1))

        # EC-HTE
        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)
        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))

    return rows


def aggregate_results(df):
    """Aggregate per-run results into summary statistics."""
    rows = []
    group_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
    for keys, grp in df.groupby(group_cols):
        row = dict(zip(group_cols, keys))
        for z in ['z0', 'z1']:
            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']
            valid = err.dropna()
            if len(valid) == 0:
                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})
                continue
            row[f'bias_{z}'] = valid.mean()
            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())
            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &
                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()
            row[f'coverage_{z}'] = covered
            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))
        rows.append(row)
    return pd.DataFrame(rows)


def run_simulation(n_mc, k_list=[2, 4], verbose=True):
    """Run full simulation sweep."""
    results = []
    configs = []
    for regime_name in REGIMES:
        for k in k_list:
            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]
            for ne in N_EXPERTS:
                configs.append((regime_name, k, misclass, ne))

    total = len(configs) * n_mc
    count = 0
    t0 = time.time()

    for regime_name, k, misclass, ne in configs:
        for mc in range(n_mc):
            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc)
            results.extend(rows)
            count += 1
            if verbose and count % max(1, total // 20) == 0:
                elapsed = time.time() - t0
                eta = elapsed / count * (total - count)
                print(f"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | k={k} {regime_name} ne={ne} mc={mc}")

    return pd.DataFrame(results), time.time() - t0


if __name__ == '__main__':
    n_mc = int(sys.argv[1]) if len(sys.argv) > 1 else N_MC
    print(f"exp-007: PPCI + DSL Baseline Comparison")
    print(f"N={N}, N_MC={n_mc}")
    print(f"Methods: oracle, naive, global_corrected, dsl, ec_hte")
    print(f"Note: ec_hte currently uses MLE fallback (HB placeholder)")
    print()

    df_raw, elapsed = run_simulation(n_mc)
    df_agg = aggregate_results(df_raw)

    # Save
    raw_path = 'results/exp007_ppci_dsl_raw.csv'
    agg_path = 'results/exp007_ppci_dsl.csv'
    df_raw.to_csv(raw_path, index=False)
    df_agg.to_csv(agg_path, index=False)

    print(f"\nTotal time: {elapsed:.1f}s")
    print(f"Saved: {raw_path}, {agg_path}")

    # Print summary
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 240)
    pd.set_option('display.float_format', '{:.4f}'.format)

    for regime in REGIMES:
        print(f"\n{'='*120}")
        print(f"Regime: {regime}")
        print(f"{'='*120}")
        sub = df_agg[df_agg['regime'] == regime]
        cols = ['n_expert', 'k_subgroups', 'subgroup', 'method', 'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']
        print(sub[cols].to_string(index=False))
