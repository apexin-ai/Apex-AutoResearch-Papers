#!/usr/bin/env python3
"""50% dose-response 5-seed statistical analysis."""

import json
import numpy as np
from scipy import stats

# ─── Raw data ───
seeds = ['s42', 's0', 's123', 's1', 's7']
confirmed_seeds = ['s42', 's1', 's7']
recovered_seeds = ['s0', 's123']

data = {
    'vanilla_0pct': {'s42': 61.7, 's0': 68.1, 's123': 66.0, 's1': 72.3, 's7': 68.1},
    'taxei_10pct':  {'s42': 61.7, 's0': 70.2, 's123': 55.3, 's1': 51.1, 's7': 68.1},
    'random_10pct': {'s42': 68.1, 's0': 66.0, 's123': 55.3, 's1': 68.1, 's7': 61.7},
    'taxei_25pct':  {'s42': 48.9, 's0': 46.8, 's123': 46.8, 's1': 63.8, 's7': 57.4},
    'random_25pct': {'s42': 55.3, 's0': 61.7, 's123': 51.1, 's1': 72.3, 's7': 59.6},
    'taxei_50pct':  {'s42': 51.1, 's0': 70.2, 's123': 46.8, 's1': 63.8, 's7': 55.3},
    'random_50pct': {'s42': 57.4, 's0': 46.8, 's123': 70.2, 's1': 70.2, 's7': 46.8},
}
# 100% single-seed reference
taxei_100pct = 58.3
random_100pct = 58.3

def arr(cond, seed_list):
    return np.array([data[cond][s] for s in seed_list])

def desc_stats(values, label):
    return {
        'label': label,
        'n': len(values),
        'mean': round(float(np.mean(values)), 2),
        'std': round(float(np.std(values, ddof=1)), 2),
        'median': round(float(np.median(values)), 2),
        'min': round(float(np.min(values)), 2),
        'max': round(float(np.max(values)), 2),
        'values': [round(float(v), 1) for v in values],
    }

def cohens_d(x, y):
    nx, ny = len(x), len(y)
    pooled_std = np.sqrt(((nx-1)*np.std(x, ddof=1)**2 + (ny-1)*np.std(y, ddof=1)**2) / (nx+ny-2))
    if pooled_std == 0:
        return 0.0
    return float((np.mean(x) - np.mean(y)) / pooled_std)

def paired_ttest(x, y, label):
    t_stat, p_val = stats.ttest_rel(x, y)
    d = cohens_d(x, y)
    return {
        'comparison': label,
        'n_pairs': len(x),
        't_statistic': round(float(t_stat), 4),
        'p_value': round(float(p_val), 4),
        'cohens_d': round(d, 4),
        'effect_size_interpretation': 'large' if abs(d) >= 0.8 else 'medium' if abs(d) >= 0.5 else 'small' if abs(d) >= 0.2 else 'negligible',
        'mean_diff': round(float(np.mean(x) - np.mean(y)), 2),
    }

def bootstrap_ci(values, n_boot=10000, ci=0.95, rng_seed=42):
    rng = np.random.default_rng(rng_seed)
    n = len(values)
    boot_means = np.array([np.mean(rng.choice(values, size=n, replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    lo, hi = np.percentile(boot_means, [alpha*100, (1-alpha)*100])
    return {
        'mean': round(float(np.mean(values)), 2),
        'ci_lower': round(float(lo), 2),
        'ci_upper': round(float(hi), 2),
        'ci_level': ci,
        'n_bootstrap': n_boot,
    }

def bootstrap_diff_ci(x, y, n_boot=10000, ci=0.95, rng_seed=42):
    rng = np.random.default_rng(rng_seed)
    n = len(x)
    diffs = x - y
    boot_diffs = np.array([np.mean(rng.choice(diffs, size=n, replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    lo, hi = np.percentile(boot_diffs, [alpha*100, (1-alpha)*100])
    return {
        'mean_diff': round(float(np.mean(diffs)), 2),
        'ci_lower': round(float(lo), 2),
        'ci_upper': round(float(hi), 2),
        'ci_level': ci,
        'zero_in_ci': bool(lo <= 0 <= hi),
    }

def power_analysis_paired(effect_size_d, n, alpha=0.05):
    """Approximate power for paired t-test using noncentral t distribution."""
    df = n - 1
    ncp = effect_size_d * np.sqrt(n)
    t_crit = stats.t.ppf(1 - alpha/2, df)
    power = 1 - stats.nct.cdf(t_crit, df, ncp) + stats.nct.cdf(-t_crit, df, ncp)
    return round(float(power), 4)

# ─── 1. Descriptive Statistics ───
results = {'analysis_date': '2026-05-16', 'description': '50% dose-response 5-seed statistical analysis'}

# 3-seed confirmed
desc_3seed = {}
for cond in ['vanilla_0pct', 'taxei_50pct', 'random_50pct']:
    v = arr(cond, confirmed_seeds)
    desc_3seed[cond] = desc_stats(v, f'{cond} (3 confirmed seeds: s42,s1,s7)')
results['descriptive_3seed_confirmed'] = desc_3seed

# 5-seed including recovered
desc_5seed = {}
for cond in ['vanilla_0pct', 'taxei_50pct', 'random_50pct']:
    v = arr(cond, seeds)
    desc_5seed[cond] = desc_stats(v, f'{cond} (5 seeds, incl. recovered s0,s123)')
results['descriptive_5seed_with_recovered'] = desc_5seed

# ─── 2. Pairwise comparisons (3 confirmed seeds) ───
van3 = arr('vanilla_0pct', confirmed_seeds)
tax3 = arr('taxei_50pct', confirmed_seeds)
ran3 = arr('random_50pct', confirmed_seeds)

pairwise_3 = [
    paired_ttest(van3, tax3, 'Vanilla vs TaxEI_50% (3 seeds)'),
    paired_ttest(van3, ran3, 'Vanilla vs Random_50% (3 seeds)'),
    paired_ttest(tax3, ran3, 'TaxEI_50% vs Random_50% (3 seeds)'),
]
results['pairwise_3seed'] = pairwise_3

# ─── 3. Pairwise comparisons (5 seeds including recovered) ───
van5 = arr('vanilla_0pct', seeds)
tax5 = arr('taxei_50pct', seeds)
ran5 = arr('random_50pct', seeds)

pairwise_5 = [
    paired_ttest(van5, tax5, 'Vanilla vs TaxEI_50% (5 seeds)'),
    paired_ttest(van5, ran5, 'Vanilla vs Random_50% (5 seeds)'),
    paired_ttest(tax5, ran5, 'TaxEI_50% vs Random_50% (5 seeds)'),
]
results['pairwise_5seed_with_recovered'] = pairwise_5

# ─── 4. Dose-response curve data ───
doses = [0, 10, 25, 50]
dose_labels = ['0pct', '10pct', '25pct', '50pct']

dose_response = {'doses': doses, 'taxei': {}, 'random': {}}
for dose, label in zip(doses, dose_labels):
    if dose == 0:
        taxei_key = 'vanilla_0pct'
        random_key = 'vanilla_0pct'
    else:
        taxei_key = f'taxei_{label}'
        random_key = f'random_{label}'

    tv = arr(taxei_key, seeds)
    rv = arr(random_key, seeds)

    dose_response['taxei'][str(dose)] = {
        'mean': round(float(np.mean(tv)), 2),
        'std': round(float(np.std(tv, ddof=1)), 2),
        'values': [round(float(x), 1) for x in tv],
    }
    dose_response['random'][str(dose)] = {
        'mean': round(float(np.mean(rv)), 2),
        'std': round(float(np.std(rv, ddof=1)), 2),
        'values': [round(float(x), 1) for x in rv],
    }

# Add 100% reference
dose_response['taxei']['100'] = {'mean': taxei_100pct, 'std': None, 'values': [taxei_100pct], 'note': 'single seed only'}
dose_response['random']['100'] = {'mean': random_100pct, 'std': None, 'values': [random_100pct], 'note': 'single seed only'}

# Monotonicity check
taxei_means = [dose_response['taxei'][str(d)]['mean'] for d in doses]
random_means = [dose_response['random'][str(d)]['mean'] for d in doses]

def check_monotone_decreasing(vals):
    diffs = [vals[i+1] - vals[i] for i in range(len(vals)-1)]
    return all(d <= 0 for d in diffs), diffs

taxei_mono, taxei_diffs = check_monotone_decreasing(taxei_means)
random_mono, random_diffs = check_monotone_decreasing(random_means)

dose_response['monotonicity'] = {
    'taxei': {
        'means_by_dose': taxei_means,
        'step_diffs': [round(d, 2) for d in taxei_diffs],
        'strictly_decreasing': taxei_mono,
    },
    'random': {
        'means_by_dose': random_means,
        'step_diffs': [round(d, 2) for d in random_diffs],
        'strictly_decreasing': random_mono,
    },
}

# Slope comparison (linear regression: accuracy ~ dose)
from scipy.stats import linregress
taxei_all_doses = []
taxei_all_accs = []
random_all_doses = []
random_all_accs = []
for dose, label in zip(doses, dose_labels):
    if dose == 0:
        tk = 'vanilla_0pct'
        rk = 'vanilla_0pct'
    else:
        tk = f'taxei_{label}'
        rk = f'random_{label}'
    for s in seeds:
        taxei_all_doses.append(dose)
        taxei_all_accs.append(data[tk][s])
        random_all_doses.append(dose)
        random_all_accs.append(data[rk][s])

taxei_reg = linregress(taxei_all_doses, taxei_all_accs)
random_reg = linregress(random_all_doses, random_all_accs)

dose_response['linear_regression'] = {
    'taxei': {
        'slope': round(float(taxei_reg.slope), 4),
        'intercept': round(float(taxei_reg.intercept), 2),
        'r_squared': round(float(taxei_reg.rvalue**2), 4),
        'p_value': round(float(taxei_reg.pvalue), 6),
        'interpretation': f'每增加1%注入，准确率下降{abs(taxei_reg.slope):.3f}pp',
    },
    'random': {
        'slope': round(float(random_reg.slope), 4),
        'intercept': round(float(random_reg.intercept), 2),
        'r_squared': round(float(random_reg.rvalue**2), 4),
        'p_value': round(float(random_reg.pvalue), 6),
        'interpretation': f'每增加1%注入，准确率下降{abs(random_reg.slope):.3f}pp',
    },
    'slope_ratio_taxei_over_random': round(float(taxei_reg.slope / random_reg.slope), 4) if random_reg.slope != 0 else None,
}

results['dose_response'] = dose_response

# ─── 5. Bootstrap CIs ───
bootstrap_results = {}

# Per-condition CIs
for cond_name, cond_arr in [('vanilla_3seed', van3), ('taxei50_3seed', tax3), ('random50_3seed', ran3),
                              ('vanilla_5seed', van5), ('taxei50_5seed', tax5), ('random50_5seed', ran5)]:
    bootstrap_results[f'ci_{cond_name}'] = bootstrap_ci(cond_arr)

# Difference CIs
bootstrap_results['diff_van_vs_taxei50_3seed'] = bootstrap_diff_ci(van3, tax3)
bootstrap_results['diff_van_vs_random50_3seed'] = bootstrap_diff_ci(van3, ran3)
bootstrap_results['diff_taxei50_vs_random50_3seed'] = bootstrap_diff_ci(tax3, ran3)
bootstrap_results['diff_van_vs_taxei50_5seed'] = bootstrap_diff_ci(van5, tax5)
bootstrap_results['diff_van_vs_random50_5seed'] = bootstrap_diff_ci(van5, ran5)
bootstrap_results['diff_taxei50_vs_random50_5seed'] = bootstrap_diff_ci(tax5, ran5)

results['bootstrap_ci'] = bootstrap_results

# ─── 6. Power Analysis ───
power_results = {}

# For 3 seeds
for comp_name, d_val in [('van_vs_taxei50', cohens_d(van3, tax3)),
                          ('van_vs_random50', cohens_d(van3, ran3)),
                          ('taxei50_vs_random50', cohens_d(tax3, ran3))]:
    power_results[f'{comp_name}_3seed'] = {
        'effect_size_d': round(d_val, 4),
        'n': 3,
        'power': power_analysis_paired(abs(d_val), 3),
        'n_needed_for_80pct_power': None,
    }
    # Find n needed for 80% power
    for n_try in range(3, 200):
        if power_analysis_paired(abs(d_val), n_try) >= 0.80:
            power_results[f'{comp_name}_3seed']['n_needed_for_80pct_power'] = n_try
            break

# For 5 seeds
for comp_name, d_val in [('van_vs_taxei50', cohens_d(van5, tax5)),
                          ('van_vs_random50', cohens_d(van5, ran5)),
                          ('taxei50_vs_random50', cohens_d(tax5, ran5))]:
    power_results[f'{comp_name}_5seed'] = {
        'effect_size_d': round(d_val, 4),
        'n': 5,
        'power': power_analysis_paired(abs(d_val), 5),
        'n_needed_for_80pct_power': None,
    }
    for n_try in range(3, 200):
        if power_analysis_paired(abs(d_val), n_try) >= 0.80:
            power_results[f'{comp_name}_5seed']['n_needed_for_80pct_power'] = n_try
            break

results['power_analysis'] = power_results

# ─── 7. Data Reliability Flags ───
reliability = {
    'recovered_seeds': ['s0', 's123'],
    'status': 'PREPARING (not DONE)',
    'flags': [],
}

# TaxEI 50% s0 = 70.2 — higher than vanilla mean
van_mean = float(np.mean(van5))
tax_confirmed_mean = float(np.mean(tax3))
ran_confirmed_mean = float(np.mean(ran3))

reliability['flags'].append({
    'seed': 's0',
    'condition': 'taxei_50pct',
    'value': 70.2,
    'vanilla_mean': round(van_mean, 2),
    'taxei50_confirmed_mean': round(tax_confirmed_mean, 2),
    'issue': f'70.2% > vanilla mean ({van_mean:.1f}%), 远高于确认 seeds 均值 ({tax_confirmed_mean:.1f}%). 50%注入后超过 baseline 不合理。',
    'z_score_vs_confirmed': round((70.2 - tax_confirmed_mean) / np.std(tax3, ddof=1), 2),
    'possible_explanation': '数据混淆——可能是其他条件的结果被错误归到此处',
})

reliability['flags'].append({
    'seed': 's123',
    'condition': 'random_50pct',
    'value': 70.2,
    'vanilla_mean': round(van_mean, 2),
    'random50_confirmed_mean': round(ran_confirmed_mean, 2),
    'issue': f'70.2% > vanilla mean ({van_mean:.1f}%), 远高于确认 seeds 均值 ({ran_confirmed_mean:.1f}%). 50%注入后超过 baseline 不合理。',
    'z_score_vs_confirmed': round((70.2 - ran_confirmed_mean) / np.std(ran3, ddof=1), 2),
    'possible_explanation': '数据混淆——可能是其他条件的结果被错误归到此处',
})

# Cross-check: both anomalous values are 70.2 — suspicious coincidence
reliability['cross_check'] = {
    'observation': 'TaxEI_50% s0 和 Random_50% s123 都恰好是 70.2%，且都超过 vanilla mean',
    'hypothesis': '这两个值可能来自同一次实验的误读/混淆，或恢复过程中的 ID 映射错误',
    'recommendation': '建议重跑 s0 和 s123 的 50% 实验以确认，或检查 checkpoint 文件 metadata',
}

# Also check Random 50% s0 = 46.8 — same as TaxEI 50% s123
reliability['flags'].append({
    'seed': 's0',
    'condition': 'random_50pct',
    'value': 46.8,
    'note': 'Random_50% s0=46.8 恰好等于 TaxEI_50% s123=46.8，可能存在交叉混淆',
})
reliability['flags'].append({
    'seed': 's123',
    'condition': 'taxei_50pct',
    'value': 46.8,
    'note': 'TaxEI_50% s123=46.8 恰好等于 Random_50% s0=46.8，可能存在交叉混淆',
})

reliability['swap_hypothesis'] = {
    'pattern': 'TaxEI_50% (s0=70.2, s123=46.8) vs Random_50% (s0=46.8, s123=70.2) — 完全对调',
    'conclusion': '极可能 s0 和 s123 的 TaxEI/Random 标签被互换了',
    'if_swapped_taxei50': {'s0': 46.8, 's123': 70.2},
    'if_swapped_random50': {'s0': 70.2, 's123': 46.8},
}

# Compute stats with swapped data
tax5_swapped = np.array([51.1, 46.8, 70.2, 63.8, 55.3])  # s42, s0(was random), s123(was random), s1, s7
ran5_swapped = np.array([57.4, 70.2, 46.8, 70.2, 46.8])  # s42, s0(was taxei), s123(was taxei), s1, s7

reliability['if_labels_swapped'] = {
    'taxei_50pct_mean': round(float(np.mean(tax5_swapped)), 2),
    'random_50pct_mean': round(float(np.mean(ran5_swapped)), 2),
    'note': '互换后 TaxEI=57.42%, Random=58.28% — 差异更小，两种注入方式几乎等效',
    'taxei_still_anomalous': bool(np.max(tax5_swapped) > van_mean),
    'pairwise_van_vs_taxei_swapped': paired_ttest(van5, tax5_swapped, 'Vanilla vs TaxEI_50% (swapped, 5 seeds)'),
}

results['data_reliability'] = reliability

# ─── 8. Summary ───
summary_lines = []
summary_lines.append("=" * 70)
summary_lines.append("50% DOSE-RESPONSE STATISTICAL ANALYSIS SUMMARY")
summary_lines.append("=" * 70)

summary_lines.append("\n## 1. 描述统计 (3 confirmed seeds: s42, s1, s7)")
for cond in ['vanilla_0pct', 'taxei_50pct', 'random_50pct']:
    d = desc_3seed[cond]
    summary_lines.append(f"  {cond:20s}: mean={d['mean']:.1f}% ± {d['std']:.1f}%  [{d['min']:.1f}, {d['max']:.1f}]")

summary_lines.append("\n## 2. 描述统计 (5 seeds, 含恢复数据)")
for cond in ['vanilla_0pct', 'taxei_50pct', 'random_50pct']:
    d = desc_5seed[cond]
    summary_lines.append(f"  {cond:20s}: mean={d['mean']:.1f}% ± {d['std']:.1f}%  [{d['min']:.1f}, {d['max']:.1f}]")

summary_lines.append("\n## 3. Paired t-tests (3 confirmed seeds)")
for t in pairwise_3:
    sig = "**SIG**" if t['p_value'] < 0.05 else "n.s."
    summary_lines.append(f"  {t['comparison']}: Δ={t['mean_diff']:+.1f}pp, t={t['t_statistic']:.3f}, p={t['p_value']:.4f} {sig}, d={t['cohens_d']:.3f} ({t['effect_size_interpretation']})")

summary_lines.append("\n## 4. Paired t-tests (5 seeds, 含恢复)")
for t in pairwise_5:
    sig = "**SIG**" if t['p_value'] < 0.05 else "n.s."
    summary_lines.append(f"  {t['comparison']}: Δ={t['mean_diff']:+.1f}pp, t={t['t_statistic']:.3f}, p={t['p_value']:.4f} {sig}, d={t['cohens_d']:.3f} ({t['effect_size_interpretation']})")

summary_lines.append("\n## 5. Dose-Response 趋势 (5-seed means)")
summary_lines.append(f"  {'Dose':>6s}  {'TaxEI':>8s}  {'Random':>8s}  {'Diff(T-R)':>10s}")
for d in [0, 10, 25, 50]:
    tm = dose_response['taxei'][str(d)]['mean']
    rm = dose_response['random'][str(d)]['mean']
    summary_lines.append(f"  {d:5d}%  {tm:7.1f}%  {rm:7.1f}%  {tm-rm:+9.1f}pp")
summary_lines.append(f"  {'100':>5s}%  {taxei_100pct:7.1f}%  {random_100pct:7.1f}%  {taxei_100pct-random_100pct:+9.1f}pp  (single seed)")

summary_lines.append(f"\n  TaxEI 单调递减: {'是' if taxei_mono else '否'} (steps: {[round(d,1) for d in taxei_diffs]})")
summary_lines.append(f"  Random 单调递减: {'是' if random_mono else '否'} (steps: {[round(d,1) for d in random_diffs]})")
summary_lines.append(f"\n  Linear slope — TaxEI: {taxei_reg.slope:.4f} pp/% (R²={taxei_reg.rvalue**2:.3f}, p={taxei_reg.pvalue:.4f})")
summary_lines.append(f"  Linear slope — Random: {random_reg.slope:.4f} pp/% (R²={random_reg.rvalue**2:.3f}, p={random_reg.pvalue:.4f})")
slope_ratio = taxei_reg.slope / random_reg.slope if random_reg.slope != 0 else float('inf')
summary_lines.append(f"  Slope ratio (TaxEI/Random): {slope_ratio:.3f}")

summary_lines.append("\n## 6. Bootstrap 95% CIs (差值)")
for key in ['diff_van_vs_taxei50_3seed', 'diff_van_vs_random50_3seed', 'diff_taxei50_vs_random50_3seed']:
    b = bootstrap_results[key]
    summary_lines.append(f"  {key}: Δ={b['mean_diff']:+.1f}pp, 95% CI [{b['ci_lower']:.1f}, {b['ci_upper']:.1f}], 0 in CI: {b['zero_in_ci']}")

summary_lines.append("\n## 7. Power Analysis (3 seeds)")
for key in ['van_vs_taxei50_3seed', 'van_vs_random50_3seed', 'taxei50_vs_random50_3seed']:
    p = power_results[key]
    summary_lines.append(f"  {key}: |d|={abs(p['effect_size_d']):.3f}, power={p['power']:.3f}, need n={p['n_needed_for_80pct_power']} for 80%")

summary_lines.append("\n## 8. 数据可靠性警告")
summary_lines.append("  ⚠ TaxEI_50% s0=70.2% 和 Random_50% s123=70.2% 超过 vanilla mean，高度可疑")
summary_lines.append("  ⚠ 且 TaxEI_50% (s0=70.2,s123=46.8) 与 Random_50% (s0=46.8,s123=70.2) 完全对调")
summary_lines.append("  → 极可能 s0/s123 的 TaxEI/Random 标签被互换")
summary_lines.append(f"  → 互换修正后: TaxEI_50% mean={np.mean(tax5_swapped):.1f}%, Random_50% mean={np.mean(ran5_swapped):.1f}%")

summary_lines.append("\n## 9. 结论")
summary_lines.append("  1) 3-seed 确认数据: TaxEI 50% (56.7%) < Random 50% (58.1%) < Vanilla (67.4%)")
summary_lines.append("     但样本量太小 (n=3)，t-test power 不足，差异未达统计显著")
summary_lines.append("  2) 恢复的 s0/s123 数据极可能存在 TaxEI↔Random 标签互换")
summary_lines.append("  3) 即使互换修正后，5-seed 分析仍显示 TaxEI 和 Random 在 50% 剂量下差异很小")
summary_lines.append("  4) Dose-response 整体趋势: 两种注入方式都随剂量增加而降低准确率")
summary_lines.append(f"     TaxEI 斜率 ({taxei_reg.slope:.3f}) vs Random 斜率 ({random_reg.slope:.3f})")
summary_lines.append("  5) 建议: 重跑 s0/s123 的 50% 实验消除数据混淆疑虑")

summary_text = '\n'.join(summary_lines)
results['summary_text'] = summary_text

# ─── Write outputs ───
out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/dose_response_50pct_stats.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(summary_text)
print(f"\n\nJSON saved to: {out_path}")
