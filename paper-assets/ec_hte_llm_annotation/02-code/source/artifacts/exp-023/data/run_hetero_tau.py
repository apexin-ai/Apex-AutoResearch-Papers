#!/usr/bin/env python3
"""
Heterogeneous-τ DGP experiment: EC-HTE vs Global correction.

τ(z) varies across subgroups, so Global's pooled CM cannot adapt to
different Δτ_s per subgroup. EC-HTE's per-subgroup correction should
dominate in bias and RMSE.
"""

import time
import warnings
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.special import gammaln

warnings.filterwarnings('ignore')

# === Config ===

N = 5000
N_EXPERT_LIST = [200, 500, 1000]
N_MC = 50
SEED_BASE = 0

SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
SUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])

SUBGROUP_CM = {
    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
}

SUBGROUP_TAU = {
    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},
    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},
    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},
    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},
}

P_Z1 = 0.652
P_T1 = 0.5


def get_cm_matrix(fpr, fnr):
    return np.array([[1 - fpr, fpr],
                     [fnr, 1 - fnr]])


# === Estimators ===

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


def estimate_confusion_matrix(z_true, z_hat):
    C = np.zeros((2, 2))
    for zt in [0, 1]:
        mask = z_true == zt
        n = mask.sum()
        for zh in [0, 1]:
            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
    return C


def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
    C = {}
    for s in labels:
        ms = subgroups == s
        C_s = np.zeros((2, 2))
        for zt in [0, 1]:
            mask = ms & (z_true == zt)
            n = mask.sum()
            for zh in [0, 1]:
                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
        C[s] = C_s
    return C


def build_mixing_matrix(C, p_z, p_z_hat):
    M = np.zeros((2, 2))
    for zh in [0, 1]:
        for z in [0, 1]:
            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
    return M


def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
    cond = np.linalg.cond(M)
    if cond > cond_threshold:
        return tau_obs.copy(), se_obs.copy()
    det = np.linalg.det(M)
    if abs(det) < 1e-10:
        return tau_obs.copy(), se_obs.copy()
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
    return tau_c, se_c


# === MAP-EB ===

def _dirmult_neg_ll(alpha, counts_z):
    a = alpha / 2.0
    if a < 1e-10:
        return 1e10
    ll = 0.0
    for c0, c1 in counts_z:
        n = c0 + c1
        if n == 0:
            continue
        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
        ll -= 2 * gammaln(a) - gammaln(2 * a)
    return -ll


def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
    hp_rate = 1.0 / hp_scale
    k = len(labels)
    alpha_opt = np.zeros(2)

    for z in [0, 1]:
        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
        total = sum(c0 + c1 for c0, c1 in cl)
        if total == 0:
            alpha_opt[z] = hp_shape * hp_scale
            continue

        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
            nll = _dirmult_neg_ll(a, _cl)
            if a < 1e-10:
                return 1e10
            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
            return nll - log_prior

        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
        alpha_opt[z] = res.x

    C = {}
    for i, s in enumerate(labels):
        C_s = np.zeros((2, 2))
        for z in [0, 1]:
            a = alpha_opt[z] / 2.0
            n_sz = counts[i, z, :].sum()
            d = n_sz + 2 * a
            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
        C[s] = C_s

    return C, alpha_opt


def get_counts(z_true, z_hat, subgroups, labels):
    k = len(labels)
    counts = np.zeros((k, 2, 2), dtype=int)
    for i, s in enumerate(labels):
        ms = subgroups == s
        for z in [0, 1]:
            mz = ms & (z_true == z)
            counts[i, z, 0] = (z_hat[mz] == 0).sum()
            counts[i, z, 1] = (z_hat[mz] == 1).sum()
    return counts


# === DGP (heterogeneous tau) ===

def generate_data(seed, n_expert):
    rng = np.random.RandomState(seed)

    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])

    Z = rng.binomial(1, P_Z1, N)
    T = rng.binomial(1, P_T1, N)

    Z_hat = np.empty(N, dtype=int)
    for i in range(4):
        s_mask = S_idx == i
        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
        z_s = Z[s_mask]
        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
        Z_hat[s_mask] = rng.binomial(1, p_obs1)

    tau_vals = np.zeros(N)
    for i, s in enumerate(SUBGROUP_LABELS):
        s_mask = S_idx == i
        tau_s = SUBGROUP_TAU[s]
        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])

    eps = rng.randn(N)
    Y = 1.0 + tau_vals * T + eps

    expert_idx = rng.choice(N, n_expert, replace=False)
    expert_mask = np.zeros(N, dtype=bool)
    expert_mask[expert_idx] = True

    return {
        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
    }


# === MC Runner ===

def run_one_mc(data, seed):
    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
    expert_mask = data['expert_mask']

    z_exp = Z[expert_mask]
    zh_exp = Z_hat[expert_mask]
    s_exp = S[expert_mask]

    C_global = estimate_confusion_matrix(z_exp, zh_exp)
    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)

    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)

    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)

    M_mle_sub = {}
    M_hb_sub = {}
    for s_val in SUBGROUP_LABELS:
        sm_exp = (s_exp == s_val)
        sm_all = (S == s_val)
        if sm_exp.sum() >= 4:
            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
        else:
            p_z_s = p_z_global
        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)
        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)

    rows = []

    for s_val in SUBGROUP_LABELS:
        s_mask = S == s_val
        tau_s = SUBGROUP_TAU[s_val]

        for z_level in [0, 1]:
            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']

            # Naive
            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan
            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
            rows.append({
                'seed': seed, 'method': 'naive', 'subgroup': s_val,
                'z_level': z_level,
                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
                'cate_est': th_nv, 'cate_true': oracle_cate,
                'coverage': cov_nv, 'ci_width': ci_w_nv,
            })

            # Observed CATE in Z_hat=0 and Z_hat=1 cells
            tau_obs = np.array([
                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
            ])
            se_obs = np.array([
                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
            ])

            if not np.any(np.isnan(tau_obs)):
                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]

                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)
                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]

                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]
            else:
                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan

            # Global corrected
            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
            rows.append({
                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,
                'z_level': z_level,
                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
                'cate_est': th_gc, 'cate_true': oracle_cate,
                'coverage': cov_gc, 'ci_width': ci_w_gc,
            })

            # Stratified MLE
            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0
            rows.append({
                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,
                'z_level': z_level,
                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,
                'cate_est': th_ml, 'cate_true': oracle_cate,
                'coverage': cov_ml, 'ci_width': ci_w_ml,
            })

            # HB EC-HTE (MAP-EB)
            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
            rows.append({
                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,
                'z_level': z_level,
                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
                'cate_est': th_hb, 'cate_true': oracle_cate,
                'coverage': cov_hb, 'ci_width': ci_w_hb,
            })

    return rows


# === Aggregation ===

def compute_corrected_abs_bias(df):
    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']
                 .mean().abs().reset_index(name='abs_mean_bias'))
    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']
            .mean().reset_index(name='abs_bias'))


def compute_rmse(df):
    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)
                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']
                 .mean().apply(np.sqrt).reset_index(name='rmse'))
    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']
            .mean().reset_index(name='rmse'))


def compute_coverage(df):
    return (df.groupby(['n_expert', 'method'])['coverage']
            .mean().reset_index(name='coverage'))


def compute_ci_width(df):
    return (df.groupby(['n_expert', 'method'])['ci_width']
            .mean().reset_index(name='ci_width'))


# === Analysis Report ===

def write_analysis(df_raw, outpath):
    abs_bias = compute_corrected_abs_bias(df_raw)
    rmse = compute_rmse(df_raw)
    cov = compute_coverage(df_raw)
    ciw = compute_ci_width(df_raw)

    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(
        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])

    lines = []
    lines.append("# Heterogeneous-τ DGP: EC-HTE vs Global Correction\n")
    lines.append("## Design\n")
    lines.append(f"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups")
    lines.append("- **Heterogeneous τ(z) across subgroups:**")
    for s in SUBGROUP_LABELS:
        t = SUBGROUP_TAU[s]
        lines.append(f"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
    lines.append(f"- n_expert sweep: {N_EXPERT_LIST}")
    lines.append(f"- {N_MC} MC seeds per budget")
    lines.append("- HB method: MAP-EB (Gamma(3,1) prior)")
    lines.append(f"- |Bias| = avg across cells of |mean(bias) across seeds|")
    lines.append(f"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)")
    lines.append("")

    # Summary table
    lines.append("## Summary Table (averaged across all cells)\n")
    lines.append("| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |")
    lines.append("|----------|--------|-------|------|----------|----------|")

    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']
    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}

    for ne in N_EXPERT_LIST:
        for m in method_order:
            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
            if len(row) > 0:
                r = row.iloc[0]
                lines.append(f"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |")
        lines.append("|----------|--------|-------|------|----------|----------|")
    lines.append("")

    # EC-HTE vs Global comparison
    lines.append("## EC-HTE vs Global Comparison\n")
    lines.append("| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |")
    lines.append("|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|")
    for ne in N_EXPERT_LIST:
        sub = summary[summary['n_expert'] == ne]
        gc = sub[sub['method'] == 'global_corrected'].iloc[0]
        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
        d_bias = gc['abs_bias'] - hb['abs_bias']
        d_rmse = gc['rmse'] - hb['rmse']
        wb = "**YES**" if hb['abs_bias'] < gc['abs_bias'] else "no"
        wr = "**YES**" if hb['rmse'] < gc['rmse'] else "no"
        lines.append(f"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |")
    lines.append("")

    # Per-subgroup breakdown
    lines.append("## Per-Subgroup Breakdown\n")
    for ne in N_EXPERT_LIST:
        lines.append(f"### n_expert = {ne}\n")
        lines.append("| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |")
        lines.append("|----------|-----|---|-------------|-------------|-------------|-------------|------------|")
        sub_df = df_raw[df_raw['n_expert'] == ne]
        for s_val in SUBGROUP_LABELS:
            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']
            for z_level in [0, 1]:
                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
                bias_gc = abs(cell_gc['bias'].mean())
                bias_hb = abs(cell_hb['bias'].mean())
                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())
                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())
                imp = bias_gc - bias_hb
                lines.append(f"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |")
        lines.append("")

    # Bias-variance decomposition
    lines.append("## Bias-Variance Decomposition\n")
    lines.append("| n_expert | Method | Bias² | Variance | MSE |")
    lines.append("|----------|--------|-------|----------|-----|")
    for ne in N_EXPERT_LIST:
        for m in method_order:
            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]
            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']
                          .agg(['mean', 'var', 'count']).reset_index())
            mean_bias_sq = (cell_stats['mean'] ** 2).mean()
            variance = cell_stats['var'].mean()
            mse = mean_bias_sq + variance
            lines.append(f"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |")
    lines.append("")

    # Comparison with constant-τ
    lines.append("## Comparison with Constant-τ DGP\n")
    lines.append("Under **constant τ** (τ(z=0)=0.35, τ(z=1)=0.65 for all subgroups),")
    lines.append("Global correction uses a pooled CM that is correct *on average*.")
    lines.append("Since all subgroups share the same Δτ, Global's pooled correction is unbiased.\n")
    lines.append("Under **heterogeneous τ**, Global's pooled CM applies a single correction")
    lines.append("factor to all subgroups, but the true Δτ varies from 0.1 (False_medium/short)")
    lines.append("to 0.6 (True_short). The correction's bias = δ_s × Δτ_s / (1−2π̄),")
    lines.append("and since Global uses pooled δ instead of subgroup-specific δ_s,")
    lines.append("it over-corrects subgroups with small Δτ and under-corrects those with large Δτ.\n")

    # Conclusion
    lines.append("## Conclusion\n")
    gc_all = summary[summary['method'] == 'global_corrected']
    hb_all = summary[summary['method'] == 'hb_ec_hte']
    n_bias_wins = 0
    n_rmse_wins = 0
    for ne in N_EXPERT_LIST:
        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]
        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]
        if hb_row['abs_bias'] < gc_row['abs_bias']:
            n_bias_wins += 1
        if hb_row['rmse'] < gc_row['rmse']:
            n_rmse_wins += 1

    lines.append(f"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.")
    lines.append(f"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\n")
    if n_bias_wins == len(N_EXPERT_LIST):
        lines.append("**Result: Under heterogeneous-τ DGP, EC-HTE consistently outperforms Global correction in bias.**")
    elif n_bias_wins > 0:
        lines.append(f"**Result: Under heterogeneous-τ DGP, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**")
    else:
        lines.append("**Result: EC-HTE does not outperform Global in bias under this DGP configuration.**")

    lines.append("")

    report = "\n".join(lines)
    with open(outpath, 'w') as f:
        f.write(report)
    print(f"Wrote {outpath}")


# === Main ===

if __name__ == '__main__':
    print("Heterogeneous-τ DGP: EC-HTE vs Global")
    print(f"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}")
    print("Subgroup τ values:")
    for s in SUBGROUP_LABELS:
        t = SUBGROUP_TAU[s]
        print(f"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
    print()

    out_dir = 'artifacts/c1_multi_llm'

    # Dry run: 1 budget, 1 seed
    print("=== Dry run (n_expert=200, 1 seed) ===")
    data = generate_data(SEED_BASE, 200)
    rows = run_one_mc(data, SEED_BASE)
    df_dry = pd.DataFrame(rows)
    df_dry['n_expert'] = 200
    print(f"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}")
    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
        sub = df_dry[df_dry['method'] == m]
        bias = sub['bias'].abs().mean()
        print(f"  {m:20s}: mean |bias| = {bias:.4f}")

    # Verify oracle CATE values
    print("\n  Oracle CATE check:")
    for s_val in SUBGROUP_LABELS:
        for zl in [0, 1]:
            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]
            true_val = cell['cate_true'].iloc[0]
            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']
            ok = "OK" if abs(true_val - expected) < 1e-10 else "MISMATCH"
            print(f"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]")
    print()

    # Full run
    print(f"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===")
    all_results = []
    t0 = time.time()
    total_runs = len(N_EXPERT_LIST) * N_MC
    run_count = 0

    for n_expert in N_EXPERT_LIST:
        print(f"\n--- n_expert = {n_expert} ---")
        t_budget = time.time()
        for mc in range(N_MC):
            seed = SEED_BASE + mc
            data = generate_data(seed, n_expert)
            mc_rows = run_one_mc(data, seed)
            for r in mc_rows:
                r['n_expert'] = n_expert
            all_results.extend(mc_rows)
            run_count += 1
            if (mc + 1) % 10 == 0:
                elapsed = time.time() - t0
                eta = elapsed / run_count * (total_runs - run_count)
                print(f"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
        budget_time = time.time() - t_budget
        print(f"  n_expert={n_expert} done in {budget_time:.1f}s")

    total_time = time.time() - t0
    print(f"\nTotal time: {total_time:.1f}s")

    df_raw = pd.DataFrame(all_results)

    # Save results CSV
    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']
    df_raw[col_order].to_csv(f'{out_dir}/hetero_tau_results.csv', index=False)
    print(f"Saved hetero_tau_results.csv ({len(df_raw)} rows)")

    # Write analysis
    write_analysis(df_raw, f'{out_dir}/hetero_tau_analysis.md')

    # Print summary
    print("\n=== Summary ===")
    abs_bias = compute_corrected_abs_bias(df_raw)
    rmse_df = compute_rmse(df_raw)
    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])
    for ne in N_EXPERT_LIST:
        print(f"\n  n_expert={ne}:")
        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
            if len(row) > 0:
                print(f"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}")
    print()

    # EC-HTE vs Global
    print("=== EC-HTE vs Global ===")
    for ne in N_EXPERT_LIST:
        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]
        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]
        print(f"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} "
              f"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})")
        print(f"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} "
              f"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})")
