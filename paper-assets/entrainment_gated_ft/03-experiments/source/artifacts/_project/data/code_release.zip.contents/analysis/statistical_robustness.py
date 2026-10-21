#!/usr/bin/env python3
"""
Statistical Robustness Framework (exp-008)

Tests robustness of the core claim: cross-architecture std on LAMBADA
decreases monotonically with attention ratio (Spearman rho = -1.0).

Analyses:
  1. Baseline Spearman rho per benchmark
  2. Bootstrap CI (percentile + BCa) for Spearman rho
  3. GDN exclusion sensitivity (D004 confound)
  4. Multiple comparison correction (Bonferroni + BH-FDR)
  5. Effect sizes (Cohen's d, eta-squared, omega-squared)

FIX [2026-05-19]: Replace scipy.stats.spearmanr asymptotic p-values with
exact two-tailed permutation test. Asymptotic approximation is invalid for
n=5 (produced p=1.4e-24 for LAMBADA, clearly wrong).
"""

import numpy as np
import pandas as pd
from scipy import stats
from itertools import permutations

np.random.seed(42)

DATA_PATH = '/root/entrainment_gated_ft/lm_eval_clean/summary_all_1.3b.csv'
OUT_CSV = '/root/entrainment_gated_ft/analysis/robustness_results.csv'
OUT_MD = '/root/entrainment_gated_ft/analysis/robustness_summary.md'

ARCHS = ['GDN', 'HGRN2', 'RetNet']
ATTN = [0, 1, 2, 4, 8]
BM = {
    'lambada_acc':        'LAMBADA',
    'hellaswag_norm':     'HellaSwag',
    'winogrande_acc':     'WinoGrande',
    'arc_easy_norm':      'ARC-Easy',
    'arc_challenge_norm': 'ARC-Challenge',
    'mmlu_acc':           'MMLU',
}
N_BOOT = 10000

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
    """Exact two-tailed permutation test for Spearman rho.
    For n=5: enumerates all 5!=120 permutations.
    Returns (rho_observed, exact_p_two_tailed).
    """
    x = list(x)
    y = list(y)
    rho_obs = stats.spearmanr(x, y).statistic
    n = len(x)
    abs_obs = abs(rho_obs)
    all_perms = list(permutations(range(n)))
    count = sum(1 for perm in all_perms
                if abs(stats.spearmanr(x, [y[i] for i in perm]).statistic) >= abs_obs)
    return float(rho_obs), count / len(all_perms)


def spearman(stds):
    if np.all(stds == stds[0]):
        return 0.0, 1.0
    return exact_spearman_p(ATTN, stds)


# ================================================================
# 1. Baseline
# ================================================================
print('=' * 72)
print('STATISTICAL ROBUSTNESS FRAMEWORK - exp-008 (EXACT PERMUTATION P-VALUES)')
print('=' * 72)
print('\n## 1  Baseline Spearman rho (3 architectures, 5 attention ratios)\n')

base = {}
for bm, nm in BM.items():
    st = xstd(bm, ARCHS)
    r, p = spearman(st)
    mono = all(st[i] >= st[i+1] for i in range(4))
    base[bm] = dict(stds=st, rho=r, p=p, mono=mono)
    print(f'  {nm:<16} rho={r:+.4f}  p={p:.4f}  mono={"Y" if mono else "N"}'
          f'  std=[{" ".join(f"{s:.5f}" for s in st)}]')

# Sanity check: no p < 1e-10 (would indicate bug not fixed)
for bm, nm in BM.items():
    assert base[bm]['p'] >= 1e-10, (
        f"BUG NOT FIXED: {nm} has p={base[bm]['p']:.2e} < 1e-10")


# ================================================================
# 2. Bootstrap CI
# ================================================================
print('\n## 2  Bootstrap CI for Spearman rho (n_boot=10000)\n')

boot_all = {}
for bm, nm in BM.items():
    rhos = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = np.random.randint(0, 3, size=3)
        sa = [ARCHS[i] for i in idx]
        st = np.array([np.std([S[bm][al][a] for a in sa]) for al in ATTN])
        if np.all(st == st[0]):
            rhos[b] = 0.0
        else:
            rhos[b] = stats.spearmanr(ATTN, st).statistic
    lo, hi = np.percentile(rhos, [2.5, 97.5])
    boot_all[bm] = dict(rhos=rhos, pct_lo=lo, pct_hi=hi)
    neg_frac = np.mean(rhos < 0)
    print(f'  {nm:<16} obs rho={base[bm]["rho"]:+.4f}  '
          f'95% CI=[{lo:.4f}, {hi:.4f}]  P(rho<0)={neg_frac:.3f}')

# BCa for LAMBADA
br = boot_all['lambada_acc']['rhos']
obs = base['lambada_acc']['rho']

jk = np.empty(3)
for i in range(3):
    loo = [ARCHS[j] for j in range(3) if j != i]
    st = np.array([np.std([S['lambada_acc'][al][a] for a in loo]) for al in ATTN])
    jk[i] = spearman(st)[0]

n_below = np.sum(br < obs)
n_equal = np.sum(br == obs)
prop = (n_below + 0.5 * n_equal) / N_BOOT
z0 = stats.norm.ppf(prop) if 0 < prop < 1 else 0.0

jm = jk.mean()
d_jk = jm - jk
denom = np.sum(d_jk**2)
a_hat = np.sum(d_jk**3) / (6 * denom**1.5) if denom > 0 else 0


def bca_quantile(z0, a, z):
    return stats.norm.cdf(z0 + (z0 + z) / (1 - a * (z0 + z)))


a1 = bca_quantile(z0, a_hat, stats.norm.ppf(0.025))
a2 = bca_quantile(z0, a_hat, stats.norm.ppf(0.975))
a1 = np.clip(a1, 0.001, 0.999)
a2 = np.clip(a2, 0.001, 0.999)
bca_lo = float(np.percentile(br, 100 * a1))
bca_hi = float(np.percentile(br, 100 * a2))

print(f'\n  LAMBADA BCa detail:')
print(f'    z0={z0:.4f}  a_hat={a_hat:.4f}')
print(f'    Jackknife rhos: {jk}')
print(f'    95% BCa CI: [{bca_lo:.4f}, {bca_hi:.4f}]')
print(f'    95% Pct CI: [{boot_all["lambada_acc"]["pct_lo"]:.4f}, '
      f'{boot_all["lambada_acc"]["pct_hi"]:.4f}]')
frac_neg = np.mean(br < 0)
frac_m1 = np.mean(br == -1.0)
frac_0 = np.mean(br == 0.0)
print(f'    Distribution: rho<0 {frac_neg*100:.1f}%  rho=-1 {frac_m1*100:.1f}%  rho=0 {frac_0*100:.1f}%')


# ================================================================
# 3. GDN Exclusion Sensitivity
# ================================================================
print('\n## 3  GDN Exclusion (RetNet + HGRN2 only)\n')

A2 = ['RetNet', 'HGRN2']
excl = {}
for bm, nm in BM.items():
    st = xstd(bm, A2)
    r, p = spearman(st)
    mono = all(st[i] >= st[i+1] for i in range(4))
    excl[bm] = dict(stds=st, rho=r, p=p, mono=mono)
    print(f'  {nm:<16} rho={r:+.4f}  p={p:.4f}  mono={"Y" if mono else "N"}'
          f'  std=[{" ".join(f"{s:.5f}" for s in st)}]')

print(f'\n  LAMBADA score detail:')
print(f'  {"attn":<6} {"GDN":>10} {"HGRN2":>10} {"RetNet":>10} '
      f'{"std(3)":>10} {"std(2)":>10}')
for al in ATTN:
    g = S['lambada_acc'][al]['GDN']
    h = S['lambada_acc'][al]['HGRN2']
    ret = S['lambada_acc'][al]['RetNet']
    s3 = np.std([g, h, ret])
    s2 = np.std([h, ret])
    print(f'  {al:<6} {g:10.6f} {h:10.6f} {ret:10.6f} {s3:10.6f} {s2:10.6f}')


# ================================================================
# 4. Multiple Comparison Correction
# ================================================================
print('\n## 4  Multiple Comparison Correction (m=6)\n')

bm_keys = list(BM.keys())
bm_names = list(BM.values())
pvals = np.array([base[b]['p'] for b in bm_keys])

bonf = np.minimum(pvals * 6, 1.0)

order = np.argsort(pvals)
ranked_p = pvals[order]
m = 6
bh_sorted = np.empty(m)
for i in range(m):
    bh_sorted[i] = ranked_p[i] * m / (i + 1)
for i in range(m - 2, -1, -1):
    bh_sorted[i] = min(bh_sorted[i], bh_sorted[i + 1])
bh_sorted = np.minimum(bh_sorted, 1.0)
bh = np.empty(m)
for rank_i, orig_i in enumerate(order):
    bh[orig_i] = bh_sorted[rank_i]

print(f'  {"Benchmark":<16} {"p":>8} {"Bonf":>8} {"BH-FDR":>8} {"Bonf sig":>10} {"BH sig":>8}')
for i, nm in enumerate(bm_names):
    print(f'  {nm:<16} {pvals[i]:8.4f} {bonf[i]:8.4f} {bh[i]:8.4f} '
          f'{"Y" if bonf[i]<0.05 else "N":>10} {"Y" if bh[i]<0.05 else "N":>8}')

li = bm_keys.index('lambada_acc')
print(f'\n  LAMBADA raw p = {pvals[li]:.6f}')
print(f'  Bonferroni adj = {bonf[li]:.4f} -> {"SIG" if bonf[li]<0.05 else "NOT SIG"} at alpha=0.05')
print(f'  BH-FDR adj     = {bh[li]:.4f} -> {"SIG" if bh[li]<0.05 else "NOT SIG"} at alpha=0.05')
print(f'  Note: 6 benchmarks share model weights -> non-independent -> Bonferroni overcorrects.')
print(f'  FDR recommended as primary correction.')


# ================================================================
# 5. Effect Sizes
# ================================================================
print('\n## 5  Effect Sizes\n')

print('  5a  Cohen d: pure vs h3-1 (paired, n=3 archs per benchmark)\n')
print(f'  {"Benchmark":<16} {"d":>8} {"95% CI":>22} {"mean_diff":>12}')
cd = {}
for bm, nm in BM.items():
    p0 = np.array([S[bm][0][a] for a in ARCHS])
    p8 = np.array([S[bm][8][a] for a in ARCHS])
    diff = p8 - p0
    md = diff.mean()
    sp = np.sqrt((p0.std(ddof=1)**2 + p8.std(ddof=1)**2) / 2)
    dv = md / sp if sp > 0 else 0.0
    n = 3
    se = np.sqrt(2/n + dv**2 / (4*n))
    ci = (dv - 1.96*se, dv + 1.96*se)
    cd[bm] = dict(d=dv, ci=ci, md=md)
    print(f'  {nm:<16} {dv:+8.3f} [{ci[0]:+8.3f}, {ci[1]:+8.3f}] {md:+12.6f}')

print(f'\n  5b  Cohen d per architecture (across 6 benchmarks)\n')
cd_arch = {}
for a in ARCHS:
    p0 = np.array([S[bm][0][a] for bm in BM])
    p8 = np.array([S[bm][8][a] for bm in BM])
    diff = p8 - p0
    md = diff.mean()
    sp = np.sqrt((p0.std(ddof=1)**2 + p8.std(ddof=1)**2) / 2)
    dv = md / sp if sp > 0 else 0.0
    n = 6
    se = np.sqrt(2/n + dv**2 / (4*n))
    ci = (dv - 1.96*se, dv + 1.96*se)
    cd_arch[a] = dict(d=dv, ci=ci, md=md)
    print(f'  {a:<10} d={dv:+.3f}  95% CI=[{ci[0]:+.3f}, {ci[1]:+.3f}]  mean_diff={md:+.6f}')

print(f'\n  5c  eta-squared (one-way ANOVA, factor=attn_ratio, n=3 per group)\n')
print(f'  {"Benchmark":<16} {"F":>8} {"p":>10} {"eta2":>8} {"omega2":>8}')
eta = {}
for bm, nm in BM.items():
    groups = [[S[bm][al][a] for a in ARCHS] for al in ATTN]
    flat = np.concatenate(groups)
    gm = flat.mean()
    ssb = sum(len(g) * (np.mean(g) - gm)**2 for g in groups)
    sst = np.sum((flat - gm)**2)
    k = len(ATTN)
    N = len(flat)
    ssw = sst - ssb
    msw = ssw / (N - k)
    e2 = ssb / sst if sst > 0 else 0
    o2 = (ssb - (k-1)*msw) / (sst + msw) if (sst + msw) > 0 else 0
    F, pa = stats.f_oneway(*groups)
    eta[bm] = dict(eta2=e2, omega2=o2, F=F, p=pa)
    print(f'  {nm:<16} {F:8.4f} {pa:10.4f} {e2:8.4f} {o2:8.4f}')

print(f'\n  5d  Kruskal-Wallis (non-parametric)\n')
print(f'  {"Benchmark":<16} {"H":>8} {"p":>10} {"eps2":>8}')
kw = {}
for bm, nm in BM.items():
    groups = [[S[bm][al][a] for a in ARCHS] for al in ATTN]
    H, pk = stats.kruskal(*groups)
    N_tot = 15
    k = 5
    eps2 = (H - k + 1) / (N_tot - k)
    kw[bm] = dict(H=H, p=pk, eps2=eps2)
    print(f'  {nm:<16} {H:8.4f} {pk:10.4f} {eps2:8.4f}')


# ================================================================
# 6. Save outputs
# ================================================================

rows = []
for i, (bm, nm) in enumerate(BM.items()):
    rows.append({
        'benchmark': nm,
        'spearman_rho': base[bm]['rho'],
        'p_value_exact': base[bm]['p'],
        'monotone_decreasing': base[bm]['mono'],
        'bonferroni_adj_p': float(bonf[i]),
        'bh_fdr_adj_p': float(bh[i]),
        'boot_ci_lower': boot_all[bm]['pct_lo'],
        'boot_ci_upper': boot_all[bm]['pct_hi'],
        'rho_excl_gdn': excl[bm]['rho'],
        'p_excl_gdn_exact': excl[bm]['p'],
        'mono_excl_gdn': excl[bm]['mono'],
        'cohen_d': cd[bm]['d'],
        'cohen_d_ci_lo': cd[bm]['ci'][0],
        'cohen_d_ci_hi': cd[bm]['ci'][1],
        'eta_squared': eta[bm]['eta2'],
        'omega_squared': eta[bm]['omega2'],
        **{f'std_attn{al}': float(base[bm]['stds'][j]) for j, al in enumerate(ATTN)},
        **{f'std_nogdn_attn{al}': float(excl[bm]['stds'][j]) for j, al in enumerate(ATTN)},
    })
pd.DataFrame(rows).to_csv(OUT_CSV, index=False)
print(f'\nSaved: {OUT_CSV}')

md = []
md.append('# Statistical Robustness Analysis - exp-008\n')
md.append('**P-values: exact two-tailed permutation test (n=5, 120 permutations)**\n')

md.append('## Bootstrap CI (n=10000)\n')
md.append('| Benchmark | obs rho | 95% Pct CI | P(rho<0) |')
md.append('|-----------|---------|------------|----------|')
for bm, nm in BM.items():
    r = base[bm]['rho']
    lo, hi = boot_all[bm]['pct_lo'], boot_all[bm]['pct_hi']
    neg = np.mean(boot_all[bm]['rhos'] < 0)
    md.append(f'| {nm} | {r:+.4f} | [{lo:.4f}, {hi:.4f}] | {neg:.3f} |')
md.append(f'\nLAMBDA BCa CI: [{bca_lo:.4f}, {bca_hi:.4f}] (z0={z0:.4f}, a={a_hat:.4f})\n')

md.append('## GDN Exclusion\n')
md.append('| Benchmark | rho(3 arch) | rho(no GDN) | p_exact(no GDN) | mono |')
md.append('|-----------|-------------|-------------|-----------------|------|')
for bm, nm in BM.items():
    md.append(f'| {nm} | {base[bm]["rho"]:+.4f} | {excl[bm]["rho"]:+.4f} | '
              f'{excl[bm]["p"]:.4f} | {"Y" if excl[bm]["mono"] else "N"} |')

md.append('\n## Multiple Comparison Correction (exact permutation p-values)\n')
md.append('| Benchmark | p_exact | Bonferroni | BH-FDR | Bonf sig | BH sig |')
md.append('|-----------|---------|------------|--------|----------|--------|')
for i, (bm, nm) in enumerate(BM.items()):
    md.append(f'| {nm} | {pvals[i]:.4f} | {bonf[i]:.4f} | {bh[i]:.4f} | '
              f'{"Y" if bonf[i]<0.05 else "N"} | {"Y" if bh[i]<0.05 else "N"} |')
md.append(f'\n**LAMBADA: Bonferroni adj-p = {bonf[li]:.4f}, BH-FDR adj-p = {bh[li]:.4f}**\n')

md.append('## Effect Sizes (pure vs h3-1)\n')
md.append('| Benchmark | Cohen d | 95% CI | eta2 | omega2 |')
md.append('|-----------|---------|--------|------|--------|')
for bm, nm in BM.items():
    md.append(f'| {nm} | {cd[bm]["d"]:+.3f} | [{cd[bm]["ci"][0]:+.3f}, {cd[bm]["ci"][1]:+.3f}] | '
              f'{eta[bm]["eta2"]:.4f} | {eta[bm]["omega2"]:.4f} |')

with open(OUT_MD, 'w') as f:
    f.write('\n'.join(md) + '\n')
print(f'Saved: {OUT_MD}')
print('\nDONE')
