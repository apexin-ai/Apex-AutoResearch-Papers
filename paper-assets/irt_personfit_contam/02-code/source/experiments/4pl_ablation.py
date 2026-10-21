"""4PL vs 3PL vs 2PL contamination detection sensitivity comparison.

Optimized: AUROC computed in main loop, items capped at 2000.
"""

import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/src')

import numpy as np
import pandas as pd
import json
from pathlib import Path
from sklearn.metrics import roc_auc_score
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from person_fit import (
    prob_4pl, generate_response, compute_lz_star,
    _estimate_theta_mle_batch, filter_valid_items
)

PROJ = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam')
PARAMS_DIR = PROJ / 'artifacts' / 'psn_irt_params'
OUT_DIR = PROJ / 'artifacts' / '4pl_ablation'
OUT_DIR.mkdir(parents=True, exist_ok=True)

BENCHMARKS = ['mmlu', 'hellaswag', 'gsm8k', 'arc_c', 'humaneval']
CONTAM_LEVELS = [0, 5, 10, 15, 25, 50, 75, 90, 100]
N_PERSONS = 500
N_SIMS = 10
MAX_ITEMS = 2000
SEED = 42
Z_CRIT = 1.96


def load_params(benchmark, max_items=None):
    df = pd.read_csv(PARAMS_DIR / f'{benchmark}_params.csv')
    a = df['a_discrimination'].values
    b = df['b_difficulty'].values
    c = df['c_guessing'].values
    d = df['d_feasibility'].values
    mask = filter_valid_items(a, b, c, d, min_a=0.01)
    a, b, c, d = a[mask], b[mask], c[mask], d[mask]
    if max_items and len(a) > max_items:
        rng = np.random.default_rng(0)
        idx = rng.choice(len(a), size=max_items, replace=False)
        idx.sort()
        a, b, c, d = a[idx], b[idx], c[idx], d[idx]
    return a, b, c, d


def make_parameterizations(a, b, c, d):
    return {
        '4PL': (a.copy(), b.copy(), c.copy(), d.copy()),
        '3PL': (a.copy(), b.copy(), c.copy(), np.ones_like(d)),
        '2PL': (a.copy(), b.copy(), np.full_like(c, 0.25), np.ones_like(d)),
    }


def contaminate(responses, contam_pct, rng):
    if contam_pct == 0:
        return responses.copy()
    X = responses.copy()
    N, J = X.shape
    n_contam = max(1, int(J * contam_pct / 100))
    for i in range(N):
        idx = rng.choice(J, size=n_contam, replace=False)
        X[i, idx] = 1
    return X


def compute_lz_for_param(responses, ap, bp, cp, dp):
    theta_hats = _estimate_theta_mle_batch(responses, ap, bp, cp, dp)
    lz_stars = compute_lz_star(responses, theta_hats[:, None], ap, bp, cp, dp)
    return lz_stars


def main():
    rng_master = np.random.default_rng(SEED)
    all_rows = []
    d_analysis_rows = []

    # Store lz* values for AUROC computation
    # Key: (bench, pname) -> {contam_pct: [lz_arrays]}
    lz_store = {}

    for bench in BENCHMARKS:
        print(f'Processing {bench}...', flush=True)
        a, b, c, d = load_params(bench, max_items=MAX_ITEMS)
        J = len(a)
        print(f'  Items: {J}', flush=True)
        parameterizations = make_parameterizations(a, b, c, d)

        for pname in parameterizations:
            lz_store[(bench, pname)] = {}

        for contam_pct in CONTAM_LEVELS:
            print(f'  contam={contam_pct}%...', flush=True)
            lz_by_param = {pn: [] for pn in parameterizations}

            for sim_idx in range(N_SIMS):
                seed = rng_master.integers(0, 2**31)
                rng = np.random.default_rng(seed)
                thetas = rng.standard_normal(N_PERSONS)

                # Generate with 4PL (ground truth)
                responses_clean = generate_response(thetas, a, b, c, d, rng=rng)
                responses = contaminate(responses_clean, contam_pct,
                                       np.random.default_rng(rng.integers(0, 2**31)))

                for pname, (ap, bp, cp, dp) in parameterizations.items():
                    lz_vals = compute_lz_for_param(responses, ap, bp, cp, dp)
                    lz_by_param[pname].append(lz_vals)

            for pname in parameterizations:
                lz_all = np.concatenate(lz_by_param[pname])
                finite_mask = np.isfinite(lz_all)
                lz_finite = lz_all[finite_mask]
                n_total = len(lz_finite)

                lz_store[(bench, pname)][contam_pct] = lz_finite

                rejected = np.abs(lz_finite) > Z_CRIT
                power = rejected.mean() if n_total > 0 else np.nan
                mean_abs_lz = np.mean(np.abs(lz_finite)) if n_total > 0 else np.nan
                mean_lz = np.mean(lz_finite) if n_total > 0 else np.nan
                std_lz = np.std(lz_finite) if n_total > 0 else np.nan

                all_rows.append({
                    'benchmark': bench,
                    'parameterization': pname,
                    'contam_pct': contam_pct,
                    'power': power,
                    'mean_abs_lz': mean_abs_lz,
                    'mean_lz': mean_lz,
                    'std_lz': std_lz,
                    'n_valid': n_total,
                    'n_items': J,
                })

        # AUROC: use stored lz* from contam=0 as clean, each contam>0 as contaminated
        print(f'  Computing AUROC...', flush=True)
        for pname in parameterizations:
            clean_lz = lz_store[(bench, pname)].get(0, np.array([]))
            for contam_pct in [c for c in CONTAM_LEVELS if c > 0]:
                contam_lz = lz_store[(bench, pname)].get(contam_pct, np.array([]))
                if len(clean_lz) > 0 and len(contam_lz) > 0:
                    labels = np.concatenate([np.zeros(len(clean_lz)), np.ones(len(contam_lz))])
                    scores = np.concatenate([-clean_lz, -contam_lz])
                    try:
                        auroc = roc_auc_score(labels, scores)
                    except ValueError:
                        auroc = np.nan
                else:
                    auroc = np.nan

                for row in all_rows:
                    if (row['benchmark'] == bench and
                        row['parameterization'] == pname and
                        row['contam_pct'] == contam_pct):
                        row['auroc'] = auroc
                        break

        # d-bucket analysis (only on item subsets)
        print(f'  d-bucket analysis...', flush=True)
        d_buckets = [
            ('d<0.8', d < 0.8),
            ('0.8<=d<0.9', (d >= 0.8) & (d < 0.9)),
            ('0.9<=d<0.95', (d >= 0.9) & (d < 0.95)),
            ('d>=0.95', d >= 0.95),
        ]

        for bucket_name, item_mask in d_buckets:
            n_items_bucket = item_mask.sum()
            if n_items_bucket < 5:
                continue
            a_sub, b_sub, c_sub, d_sub = a[item_mask], b[item_mask], c[item_mask], d[item_mask]
            params_sub = {
                '4PL': (a_sub, b_sub, c_sub, d_sub),
                '3PL': (a_sub, b_sub, c_sub, np.ones_like(d_sub)),
            }

            for contam_pct in [25, 50, 75]:
                lz_bucket = {pn: [] for pn in params_sub}
                for sim_idx in range(5):  # fewer sims for bucket analysis
                    seed = rng_master.integers(0, 2**31)
                    rng = np.random.default_rng(seed)
                    thetas = rng.standard_normal(N_PERSONS)
                    resp = generate_response(thetas, a_sub, b_sub, c_sub, d_sub, rng=rng)
                    resp = contaminate(resp, contam_pct,
                                      np.random.default_rng(rng.integers(0, 2**31)))
                    for pn, (ap, bp, cp, dp) in params_sub.items():
                        lz = compute_lz_for_param(resp, ap, bp, cp, dp)
                        lz_bucket[pn].append(lz)

                for pn in params_sub:
                    lz_all = np.concatenate(lz_bucket[pn])
                    lz_all = lz_all[np.isfinite(lz_all)]
                    d_analysis_rows.append({
                        'benchmark': bench,
                        'd_bucket': bucket_name,
                        'n_items': int(n_items_bucket),
                        'parameterization': pn,
                        'contam_pct': contam_pct,
                        'power': float((np.abs(lz_all) > Z_CRIT).mean()) if len(lz_all) > 0 else np.nan,
                        'mean_abs_lz': float(np.mean(np.abs(lz_all))) if len(lz_all) > 0 else np.nan,
                    })

    df = pd.DataFrame(all_rows)
    df.loc[df['contam_pct'] == 0, 'auroc'] = np.nan
    df.to_csv(OUT_DIR / 'ablation_results.csv', index=False)

    df_d = pd.DataFrame(d_analysis_rows)
    df_d.to_csv(OUT_DIR / 'd_bucket_analysis.csv', index=False)

    # ---- Summary JSON ----
    summary = build_summary(df, df_d)
    with open(OUT_DIR / 'ablation_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    print('Simulation done. Generating plots...', flush=True)
    make_plots(df, df_d)

    report = generate_report(df, df_d, summary)
    with open(OUT_DIR / 'ablation_report.md', 'w') as f:
        f.write(report)

    print(f'All outputs saved to {OUT_DIR}')


def build_summary(df, df_d):
    summary = {
        'benchmarks': BENCHMARKS,
        'n_persons': N_PERSONS,
        'n_sims': N_SIMS,
        'max_items': MAX_ITEMS,
        'contam_levels': CONTAM_LEVELS,
    }

    for bench in BENCHMARKS:
        df_params = pd.read_csv(PARAMS_DIR / f'{bench}_params.csv')
        d_all = df_params['d_feasibility'].values
        summary[f'd_stats_{bench}'] = {
            'n_items_total': len(d_all),
            'mean': float(np.mean(d_all)),
            'std': float(np.std(d_all)),
            'pct_below_095': float((d_all < 0.95).mean() * 100),
            'pct_below_090': float((d_all < 0.9).mean() * 100),
            'pct_below_080': float((d_all < 0.8).mean() * 100),
        }

    far_rows = df[df['contam_pct'] == 0]
    summary['false_alarm_rates'] = {}
    for _, row in far_rows.iterrows():
        key = f"{row['benchmark']}_{row['parameterization']}"
        summary['false_alarm_rates'][key] = round(row['power'], 4)

    power_at_25 = df[df['contam_pct'] == 25]
    summary['power_at_25pct'] = {}
    for _, row in power_at_25.iterrows():
        key = f"{row['benchmark']}_{row['parameterization']}"
        summary['power_at_25pct'][key] = round(row['power'], 4)

    summary['4pl_vs_3pl_power_gain'] = {}
    summary['3pl_vs_2pl_power_gain'] = {}
    for bench in BENCHMARKS:
        gains_43 = []
        gains_32 = []
        for cp in [c for c in CONTAM_LEVELS if c > 0]:
            p4 = df[(df['benchmark'] == bench) & (df['parameterization'] == '4PL') & (df['contam_pct'] == cp)]['power'].values
            p3 = df[(df['benchmark'] == bench) & (df['parameterization'] == '3PL') & (df['contam_pct'] == cp)]['power'].values
            p2 = df[(df['benchmark'] == bench) & (df['parameterization'] == '2PL') & (df['contam_pct'] == cp)]['power'].values
            if len(p4) > 0 and len(p3) > 0:
                gains_43.append(float(p4[0] - p3[0]))
            if len(p3) > 0 and len(p2) > 0:
                gains_32.append(float(p3[0] - p2[0]))
        summary['4pl_vs_3pl_power_gain'][bench] = {
            'mean': round(np.mean(gains_43), 4) if gains_43 else None,
            'max': round(np.max(gains_43), 4) if gains_43 else None,
        }
        summary['3pl_vs_2pl_power_gain'][bench] = {
            'mean': round(np.mean(gains_32), 4) if gains_32 else None,
            'max': round(np.max(gains_32), 4) if gains_32 else None,
        }

    return summary


def make_plots(df, df_d):
    colors = {'4PL': '#e41a1c', '3PL': '#377eb8', '2PL': '#4daf4a'}
    markers = {'4PL': 'o', '3PL': 's', '2PL': '^'}

    # ---- Plot 1: Power comparison ----
    fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
    for i, bench in enumerate(BENCHMARKS):
        ax = axes[i]
        for pn in ['4PL', '3PL', '2PL']:
            sub = df[(df['benchmark'] == bench) & (df['parameterization'] == pn)].sort_values('contam_pct')
            ax.plot(sub['contam_pct'], sub['power'],
                    color=colors[pn], marker=markers[pn], markersize=5,
                    linewidth=1.5, label=pn)
        ax.axhline(0.05, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
        ax.set_title(bench.upper(), fontsize=11)
        ax.set_xlabel('Contamination %')
        if i == 0:
            ax.set_ylabel('Detection Power')
        ax.set_ylim(-0.02, 1.05)
        ax.legend(fontsize=8)
    plt.suptitle('Detection Power: 4PL vs 3PL vs 2PL', fontsize=13, y=1.02)
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'power_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ---- Plot 2: AUROC comparison ----
    fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
    for i, bench in enumerate(BENCHMARKS):
        ax = axes[i]
        for pn in ['4PL', '3PL', '2PL']:
            sub = df[(df['benchmark'] == bench) & (df['parameterization'] == pn) & (df['contam_pct'] > 0)]
            sub = sub.dropna(subset=['auroc']).sort_values('contam_pct')
            if len(sub) > 0:
                ax.plot(sub['contam_pct'], sub['auroc'],
                        color=colors[pn], marker=markers[pn], markersize=5,
                        linewidth=1.5, label=pn)
        ax.axhline(0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
        ax.set_title(bench.upper(), fontsize=11)
        ax.set_xlabel('Contamination %')
        if i == 0:
            ax.set_ylabel('AUROC')
        ax.set_ylim(0.45, 1.05)
        ax.legend(fontsize=8)
    plt.suptitle('AUROC: 4PL vs 3PL vs 2PL', fontsize=13, y=1.02)
    plt.tight_layout()
    plt.savefig(OUT_DIR / 'auroc_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ---- Plot 3: d-parameter analysis ----
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    buckets_order = ['d<0.8', '0.8<=d<0.9', '0.9<=d<0.95', 'd>=0.95']

    # Top-left: d distribution
    ax = axes[0, 0]
    for bench in BENCHMARKS:
        df_p = pd.read_csv(PARAMS_DIR / f'{bench}_params.csv')
        ax.hist(df_p['d_feasibility'].values, bins=50, alpha=0.5, label=bench.upper(), density=True)
    ax.set_xlabel('d (upper asymptote)')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of d parameter')
    ax.legend(fontsize=7)
    ax.axvline(1.0, color='black', linestyle='--', linewidth=0.8)

    # Top-center: % items below thresholds
    ax = axes[0, 1]
    thresholds = [0.8, 0.85, 0.9, 0.95]
    x_pos = np.arange(len(BENCHMARKS))
    width = 0.2
    for j, thr in enumerate(thresholds):
        pcts = []
        for bench in BENCHMARKS:
            df_p = pd.read_csv(PARAMS_DIR / f'{bench}_params.csv')
            pcts.append((df_p['d_feasibility'].values < thr).mean() * 100)
        ax.bar(x_pos + j * width, pcts, width, label=f'd < {thr}')
    ax.set_xticks(x_pos + 1.5 * width)
    ax.set_xticklabels([b.upper() for b in BENCHMARKS], fontsize=8)
    ax.set_ylabel('% items')
    ax.set_title('Items below d thresholds')
    ax.legend(fontsize=7)

    # Top-right: Power by d-bucket (MMLU, 50% contam)
    ax = axes[0, 2]
    if len(df_d) > 0:
        bench_sub = 'mmlu'
        cp_sub = 50
        sub = df_d[(df_d['benchmark'] == bench_sub) & (df_d['contam_pct'] == cp_sub)]
        x_bk = np.arange(len(buckets_order))
        for pn, offset in [('4PL', -0.15), ('3PL', 0.15)]:
            vals = []
            for bk in buckets_order:
                row = sub[(sub['d_bucket'] == bk) & (sub['parameterization'] == pn)]
                vals.append(row['power'].values[0] if len(row) > 0 else 0)
            ax.bar(x_bk + offset, vals, 0.3, label=pn, color=colors[pn], alpha=0.8)
        ax.set_xticks(x_bk)
        ax.set_xticklabels(buckets_order, fontsize=8, rotation=15)
        ax.set_ylabel('Power')
        ax.set_title(f'Power by d-bucket ({bench_sub.upper()}, {cp_sub}% contam)')
        ax.legend(fontsize=8)

    # Bottom-left: 4PL - 3PL power diff
    ax = axes[1, 0]
    for bench in BENCHMARKS:
        diffs, cl = [], []
        for cp in CONTAM_LEVELS:
            p4 = df[(df['benchmark'] == bench) & (df['parameterization'] == '4PL') & (df['contam_pct'] == cp)]['power'].values
            p3 = df[(df['benchmark'] == bench) & (df['parameterization'] == '3PL') & (df['contam_pct'] == cp)]['power'].values
            if len(p4) > 0 and len(p3) > 0:
                diffs.append(p4[0] - p3[0])
                cl.append(cp)
        ax.plot(cl, diffs, marker='o', markersize=4, linewidth=1.5, label=bench.upper())
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_xlabel('Contamination %')
    ax.set_ylabel('Power(4PL) - Power(3PL)')
    ax.set_title('4PL advantage over 3PL')
    ax.legend(fontsize=7)

    # Bottom-center: 3PL - 2PL power diff
    ax = axes[1, 1]
    for bench in BENCHMARKS:
        diffs, cl = [], []
        for cp in CONTAM_LEVELS:
            p3 = df[(df['benchmark'] == bench) & (df['parameterization'] == '3PL') & (df['contam_pct'] == cp)]['power'].values
            p2 = df[(df['benchmark'] == bench) & (df['parameterization'] == '2PL') & (df['contam_pct'] == cp)]['power'].values
            if len(p3) > 0 and len(p2) > 0:
                diffs.append(p3[0] - p2[0])
                cl.append(cp)
        ax.plot(cl, diffs, marker='o', markersize=4, linewidth=1.5, label=bench.upper())
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_xlabel('Contamination %')
    ax.set_ylabel('Power(3PL) - Power(2PL)')
    ax.set_title('3PL advantage over 2PL')
    ax.legend(fontsize=7)

    # Bottom-right: 4PL power by d-bucket across benchmarks
    ax = axes[1, 2]
    if len(df_d) > 0:
        cp_sub = 50
        sub = df_d[df_d['contam_pct'] == cp_sub]
        for bench in BENCHMARKS:
            bs = sub[(sub['benchmark'] == bench) & (sub['parameterization'] == '4PL')]
            if len(bs) > 0:
                order = {bk: i for i, bk in enumerate(buckets_order)}
                bs = bs.copy()
                bs['order'] = bs['d_bucket'].map(order)
                bs = bs.dropna(subset=['order']).sort_values('order')
                ax.plot(range(len(bs)), bs['power'].values, marker='o', markersize=4, label=bench.upper())
        ax.set_xticks(range(len(buckets_order)))
        ax.set_xticklabels(buckets_order, fontsize=8, rotation=15)
        ax.set_ylabel('4PL Power')
        ax.set_title('4PL power by d-bucket (50% contam)')
        ax.legend(fontsize=7)

    plt.tight_layout()
    plt.savefig(OUT_DIR / 'd_parameter_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()


def generate_report(df, df_d, summary):
    lines = ['# 4PL vs 3PL vs 2PL Detection Sensitivity Ablation\n']
    lines.append('## Setup\n')
    lines.append(f'- N_persons = {N_PERSONS}, N_sims = {N_SIMS}, seed = {SEED}')
    lines.append(f'- Max items per benchmark = {MAX_ITEMS} (sampled if larger)')
    lines.append(f'- Contamination levels: {CONTAM_LEVELS}')
    lines.append('- Data generation: always 4PL (ground truth)')
    lines.append('- Detection: lz* computed under 4PL / 3PL(d=1) / 2PL(c=0.25,d=1)\n')

    lines.append('## d-parameter distribution (full item sets)\n')
    lines.append('| Benchmark | N items | mean(d) | std(d) | % d<0.95 | % d<0.90 | % d<0.80 |')
    lines.append('|-----------|---------|---------|--------|----------|----------|----------|')
    for bench in BENCHMARKS:
        s = summary[f'd_stats_{bench}']
        lines.append(f"| {bench.upper()} | {s['n_items_total']} | {s['mean']:.4f} | {s['std']:.4f} | {s['pct_below_095']:.1f}% | {s['pct_below_090']:.1f}% | {s['pct_below_080']:.1f}% |")

    lines.append('\n## False alarm rate (contam=0%)\n')
    lines.append('Expected: ~5% (two-sided α=0.05)\n')
    lines.append('| Benchmark | 4PL | 3PL | 2PL |')
    lines.append('|-----------|-----|-----|-----|')
    for bench in BENCHMARKS:
        far = summary['false_alarm_rates']
        f4 = far.get(f'{bench}_4PL', float('nan'))
        f3 = far.get(f'{bench}_3PL', float('nan'))
        f2 = far.get(f'{bench}_2PL', float('nan'))
        lines.append(f"| {bench.upper()} | {f4:.4f} | {f3:.4f} | {f2:.4f} |")

    lines.append('\n## Detection power at 25% contamination\n')
    lines.append('| Benchmark | 4PL | 3PL | 2PL | Δ(4PL-3PL) | Δ(3PL-2PL) |')
    lines.append('|-----------|-----|-----|-----|------------|------------|')
    for bench in BENCHMARKS:
        p = summary['power_at_25pct']
        p4 = p.get(f'{bench}_4PL', 0)
        p3 = p.get(f'{bench}_3PL', 0)
        p2 = p.get(f'{bench}_2PL', 0)
        lines.append(f"| {bench.upper()} | {p4:.4f} | {p3:.4f} | {p2:.4f} | {p4-p3:+.4f} | {p3-p2:+.4f} |")

    lines.append('\n## Power gain: 4PL vs 3PL (averaged over contamination levels)\n')
    lines.append('| Benchmark | Mean Δpower | Max Δpower |')
    lines.append('|-----------|-------------|------------|')
    for bench in BENCHMARKS:
        g = summary['4pl_vs_3pl_power_gain'].get(bench, {})
        lines.append(f"| {bench.upper()} | {g.get('mean', 0):+.4f} | {g.get('max', 0):+.4f} |")

    lines.append('\n## Power gain: 3PL vs 2PL (averaged over contamination levels)\n')
    lines.append('| Benchmark | Mean Δpower | Max Δpower |')
    lines.append('|-----------|-------------|------------|')
    for bench in BENCHMARKS:
        g = summary['3pl_vs_2pl_power_gain'].get(bench, {})
        lines.append(f"| {bench.upper()} | {g.get('mean', 0):+.4f} | {g.get('max', 0):+.4f} |")

    lines.append('\n## d-bucket analysis (4PL vs 3PL power at 50% contamination)\n')
    if len(df_d) > 0:
        lines.append('| Benchmark | d<0.8 | 0.8≤d<0.9 | 0.9≤d<0.95 | d≥0.95 |')
        lines.append('|-----------|-------|-----------|------------|--------|')
        for bench in BENCHMARKS:
            vals = []
            for bk in ['d<0.8', '0.8<=d<0.9', '0.9<=d<0.95', 'd>=0.95']:
                r4 = df_d[(df_d['benchmark'] == bench) & (df_d['d_bucket'] == bk) &
                          (df_d['parameterization'] == '4PL') & (df_d['contam_pct'] == 50)]
                r3 = df_d[(df_d['benchmark'] == bench) & (df_d['d_bucket'] == bk) &
                          (df_d['parameterization'] == '3PL') & (df_d['contam_pct'] == 50)]
                if len(r4) > 0 and len(r3) > 0:
                    diff = r4['power'].values[0] - r3['power'].values[0]
                    vals.append(f'{diff:+.4f}')
                else:
                    vals.append('N/A')
            lines.append(f"| {bench.upper()} | {' | '.join(vals)} |")

    lines.append('\n## Full power table\n')
    lines.append('| Benchmark | Param | 0% | 5% | 10% | 15% | 25% | 50% | 75% | 90% | 100% |')
    lines.append('|-----------|-------|' + '|'.join(['------'] * 9) + '|')
    for bench in BENCHMARKS:
        for pn in ['4PL', '3PL', '2PL']:
            row_vals = []
            for cp in CONTAM_LEVELS:
                sub = df[(df['benchmark'] == bench) & (df['parameterization'] == pn) & (df['contam_pct'] == cp)]
                if len(sub) > 0:
                    row_vals.append(f"{sub['power'].values[0]:.3f}")
                else:
                    row_vals.append('N/A')
            lines.append(f"| {bench.upper()} | {pn} | {' | '.join(row_vals)} |")

    return '\n'.join(lines)


if __name__ == '__main__':
    main()
