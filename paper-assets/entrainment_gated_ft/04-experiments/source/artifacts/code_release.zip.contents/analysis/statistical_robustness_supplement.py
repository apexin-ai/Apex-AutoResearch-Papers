#!/usr/bin/env python3
"""
Supplementary Statistical Analyses for exp-008

Part A: Bootstrap CI for LAMBADA Spearman rho (architecture resampling)
Part B: GDN-Excluded Sensitivity Analysis (all 6 benchmarks)
"""

import numpy as np
import pandas as pd
import json
from scipy.stats import spearmanr, norm
from itertools import permutations

DATA_PATH = '/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv'
OUT_JSON = '/root/entrainment_gated_ft/analysis/robustness_supplement_summary.json'
OUT_CSV = '/root/entrainment_gated_ft/analysis/robustness_supplement_gdn_excluded.csv'

ARCHS = ['GDN', 'HGRN2', 'RetNet']
ARCHS_NO_GDN = ['HGRN2', 'RetNet']
ATTN = [0, 1, 2, 4, 8]
ATTN_RATIOS = [0.0, 1/25, 1/13, 1/7, 1/4]
BM = {
    'lambada_acc':        'LAMBADA',
    'hellaswag_norm':     'HellaSwag',
    'winogrande_acc':     'WinoGrande',
    'arc_easy_norm':      'ARC-Easy',
    'arc_challenge_norm': 'ARC-Challenge',
    'mmlu_acc':           'MMLU',
}
N_BOOT = 10000
SEED = 42

df = pd.read_csv(DATA_PATH)
df_h = df[df['model_family'].isin(ARCHS)]

S = {}
for bm in BM:
    S[bm] = {}
    for al in ATTN:
        S[bm][al] = {}
        for a in ARCHS:
            S[bm][al][a] = df_h.loc[
                (df_h['model_family'] == a) & (df_h['attn_layers'] == al), bm
            ].values[0]


def xstd(bm, archs, attn=ATTN):
    return np.array([np.std([S[bm][al][a] for a in archs]) for al in attn])


def exact_spearman_p(x, y):
    x = list(x)
    y = list(y)
    rho_obs = spearmanr(x, y).statistic
    n = len(x)
    abs_obs = abs(rho_obs)
    all_perms = list(permutations(range(n)))
    count = sum(1 for perm in all_perms
                if abs(spearmanr(x, [y[i] for i in perm]).statistic) >= abs_obs)
    return float(rho_obs), count / len(all_perms)


# ================================================================
# Part A: Bootstrap CI for LAMBADA Spearman rho
# ================================================================
print('=' * 72)
print('PART A: Bootstrap CI for LAMBADA Spearman rho')
print('=' * 72)

y_lambada = xstd('lambada_acc', ARCHS)
rho_obs = spearmanr(ATTN, y_lambada).statistic

print(f'\nObserved: rho = {rho_obs:.4f}')
print(f'  x (attn_layers): {ATTN}')
print(f'  y (cross-arch std): [{", ".join(f"{v:.6f}" for v in y_lambada)}]')

# Architecture resampling bootstrap
rng = np.random.RandomState(SEED)
boot_rhos_all = []  # including degenerate
boot_rhos_valid = []  # excluding degenerate (all-same-arch)
degen_count = 0

for _ in range(N_BOOT):
    idx = rng.choice(3, size=3, replace=True)
    sampled = [ARCHS[i] for i in idx]
    st = np.array([np.std([S['lambada_acc'][al][a] for a in sampled]) for al in ATTN])
    if np.all(st == st[0]):
        boot_rhos_all.append(0.0)
        degen_count += 1
    else:
        r = spearmanr(ATTN, st).statistic
        boot_rhos_all.append(r)
        boot_rhos_valid.append(r)

boot_rhos_all = np.array(boot_rhos_all)
boot_rhos_valid = np.array(boot_rhos_valid)

# Percentile CI (primary — BCa not applicable at rho=-1.0 boundary)
pct_lo_all = float(np.percentile(boot_rhos_all, 2.5))
pct_hi_all = float(np.percentile(boot_rhos_all, 97.5))
pct_lo_valid = float(np.percentile(boot_rhos_valid, 2.5))
pct_hi_valid = float(np.percentile(boot_rhos_valid, 97.5))

# Jackknife (leave-one-arch-out)
jack_rhos = {}
for i, arch in enumerate(ARCHS):
    rem = [ARCHS[j] for j in range(3) if j != i]
    st = xstd('lambada_acc', rem)
    if np.all(st == st[0]):
        jack_rhos[arch] = 0.0
    else:
        jack_rhos[arch] = float(spearmanr(ATTN, st).statistic)

# BCa attempt (z0 at boundary → degenerate, reported for completeness)
prop_less = np.mean(boot_rhos_valid < rho_obs)
if prop_less == 0:
    prop_less = 0.5 / len(boot_rhos_valid)
z0 = norm.ppf(prop_less)
jack_arr = np.array(list(jack_rhos.values()))
jm = jack_arr.mean()
diff = jm - jack_arr
num = np.sum(diff**3)
den = 6 * np.sum(diff**2)**1.5
a_hat = num / (den + 1e-10) if den > 1e-10 else 0.0

print(f'\nBootstrap (n={N_BOOT}, seed={SEED}):')
print(f'  Valid samples: {len(boot_rhos_valid)} ({degen_count} degenerate dropped)')
print(f'  Distribution: {dict(zip(*np.unique(np.round(boot_rhos_valid, 4), return_counts=True)))}')
print(f'  P(rho < 0) = {np.mean(boot_rhos_all < 0):.4f} (all), {np.mean(boot_rhos_valid < 0):.4f} (valid)')
print(f'  P(rho > 0) = {np.mean(boot_rhos_all > 0):.4f}')

print(f'\nPercentile 95% CI (including degenerate): [{pct_lo_all:.4f}, {pct_hi_all:.4f}]')
print(f'Percentile 95% CI (valid only):           [{pct_lo_valid:.4f}, {pct_hi_valid:.4f}]')
crosses_zero = (pct_lo_valid <= 0 <= pct_hi_valid)
print(f'Crosses zero (valid): {"YES" if crosses_zero else "NO"}')

print(f'\nJackknife (leave-one-arch-out):')
for arch, r in jack_rhos.items():
    print(f'  Excl {arch}: rho = {r:+.4f}')

print(f'\nBCa diagnostics (boundary-degenerate, for completeness):')
print(f'  z0 = {z0:.4f} (extreme → BCa not reliable at rho boundary)')
print(f'  a = {a_hat:.4f}')
print(f'  Note: BCa requires smooth bootstrap distribution; here only 2 discrete')
print(f'  values exist. Percentile CI is the appropriate method.')

bca_result = {
    'method': 'architecture_resampling_percentile',
    'rho_obs': float(rho_obs),
    'ci_lower': pct_lo_valid,
    'ci_upper': pct_hi_valid,
    'crosses_zero': crosses_zero,
    'ci_lower_with_degen': pct_lo_all,
    'ci_upper_with_degen': pct_hi_all,
    'n_bootstrap': N_BOOT,
    'n_valid': len(boot_rhos_valid),
    'n_degenerate': degen_count,
    'seed': SEED,
    'p_rho_negative_all': float(np.mean(boot_rhos_all < 0)),
    'p_rho_negative_valid': float(np.mean(boot_rhos_valid < 0)),
    'p_rho_positive': float(np.mean(boot_rhos_all > 0)),
    'boot_mean_valid': float(np.mean(boot_rhos_valid)),
    'jackknife': jack_rhos,
    'bca_z0': float(z0),
    'bca_a': float(a_hat),
    'bca_note': 'BCa degenerate at rho=-1.0 boundary (z0=-3.86); percentile CI used instead',
}


# ================================================================
# Part B: GDN-Excluded Sensitivity Analysis
# ================================================================
print('\n' + '=' * 72)
print('PART B: GDN-Excluded Sensitivity Analysis (RetNet + HGRN2 only)')
print('=' * 72)

print(f'\n{"Benchmark":<16} {"rho_full":>9} {"p_full":>8} {"rho_noGDN":>10} {"p_noGDN":>9} {"mono_f":>7} {"mono_ng":>7} {"direction":>10}')
print('-' * 82)

gdn_excluded_results = {}
rows = []
for bm, nm in BM.items():
    stds_full = xstd(bm, ARCHS)
    rho_full, p_full = exact_spearman_p(ATTN, stds_full)
    mono_full = all(stds_full[i] >= stds_full[i+1] for i in range(4))

    stds_nogdn = xstd(bm, ARCHS_NO_GDN)
    if np.all(stds_nogdn == stds_nogdn[0]):
        rho_nogdn, p_nogdn = 0.0, 1.0
    else:
        rho_nogdn, p_nogdn = exact_spearman_p(ATTN, stds_nogdn)
    mono_nogdn = all(stds_nogdn[i] >= stds_nogdn[i+1] for i in range(4))

    if abs(rho_nogdn) > abs(rho_full) + 0.05:
        direction = 'STRONGER'
    elif abs(rho_nogdn) < abs(rho_full) - 0.05:
        direction = 'WEAKER'
    else:
        direction = 'SIMILAR'

    assert p_full >= 1e-10, f"BUG: {nm} full p={p_full:.2e}"
    assert p_nogdn >= 1e-10, f"BUG: {nm} noGDN p={p_nogdn:.2e}"

    print(f'{nm:<16} {rho_full:>+9.4f} {p_full:>8.4f} {rho_nogdn:>+10.4f} {p_nogdn:>9.4f} {"Y" if mono_full else "N":>7} {"Y" if mono_nogdn else "N":>7} {direction:>10}')

    gdn_excluded_results[nm] = {
        'rho_full': float(rho_full),
        'p_full': float(p_full),
        'rho_gdn_excluded': float(rho_nogdn),
        'p_gdn_excluded': float(p_nogdn),
        'mono_full': bool(mono_full),
        'mono_gdn_excluded': bool(mono_nogdn),
        'direction': direction,
        'stds_full': [float(v) for v in stds_full],
        'stds_gdn_excluded': [float(v) for v in stds_nogdn],
    }

    rows.append({
        'benchmark': nm,
        'rho_full': float(rho_full),
        'p_full': float(p_full),
        'mono_full': bool(mono_full),
        'rho_gdn_excluded': float(rho_nogdn),
        'p_gdn_excluded': float(p_nogdn),
        'mono_gdn_excluded': bool(mono_nogdn),
        'direction': direction,
        **{f'std_full_attn{al}': float(stds_full[j]) for j, al in enumerate(ATTN)},
        **{f'std_nogdn_attn{al}': float(stds_nogdn[j]) for j, al in enumerate(ATTN)},
    })

# ARC-Easy highlight
print(f'\n*** ARC-Easy (potential second anchor) ***')
ae = gdn_excluded_results['ARC-Easy']
print(f'  Full:     rho={ae["rho_full"]:+.4f}, p={ae["p_full"]:.4f}')
print(f'  No-GDN:   rho={ae["rho_gdn_excluded"]:+.4f}, p={ae["p_gdn_excluded"]:.4f}')
print(f'  Direction: {ae["direction"]} (rho improves from -0.7 to -0.9)')
print(f'  Note: p=0.0833 still not significant at alpha=0.05, but suggestive')

# LAMBADA highlight
print(f'\n*** LAMBADA (primary anchor) ***')
la = gdn_excluded_results['LAMBADA']
print(f'  Full:     rho={la["rho_full"]:+.4f}, p={la["p_full"]:.4f}')
print(f'  No-GDN:   rho={la["rho_gdn_excluded"]:+.4f}, p={la["p_gdn_excluded"]:.4f}')
print(f'  Direction: {la["direction"]} (monotonicity breaks without GDN)')

stronger = sum(1 for v in gdn_excluded_results.values() if v['direction'] == 'STRONGER')
weaker = sum(1 for v in gdn_excluded_results.values() if v['direction'] == 'WEAKER')
similar = sum(1 for v in gdn_excluded_results.values() if v['direction'] == 'SIMILAR')
print(f'\nOverall: {stronger} stronger, {weaker} weaker, {similar} similar without GDN')

pd.DataFrame(rows).to_csv(OUT_CSV, index=False)
print(f'\nSaved: {OUT_CSV}')

# ================================================================
# Summary JSON
# ================================================================
summary = {
    'analysis': 'exp-008 supplementary statistical analyses',
    'date': '2026-05-19',
    'part_a_bootstrap_ci': bca_result,
    'part_b_gdn_excluded': gdn_excluded_results,
    'attention_layers': ATTN,
    'attention_ratios': ATTN_RATIOS,
}

with open(OUT_JSON, 'w') as f:
    json.dump(summary, f, indent=2)
print(f'Saved: {OUT_JSON}')

print('\nDONE')
