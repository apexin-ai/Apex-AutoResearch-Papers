#!/usr/bin/env python3
"""Generate 10 appendix figures for the EMNLP 2026 paper.
Reads from artifacts/ JSON/CSV data files, outputs PDF+PNG to docs/paper/figures/.
Unified colorblind-safe palette (Wong/project standard).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
import csv
from pathlib import Path

ROOT = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse')
DATA = ROOT / 'artifacts' / '_project' / 'data'
OUT = ROOT / 'docs' / 'paper' / 'figures'

# ── Unified palette ──
PAL = {
    'blue':     '#4A90C4',
    'red':      '#CC5A5A',
    'green':    '#4DAF7C',
    'orange':   '#E8A04C',
    'purple':   '#8B6BB0',
    'ltblue':   '#B8D4E8',
    'grey':     '#999999',
    'ltgrey':   '#DDDDDD',
}
METHOD_COLORS = {
    'NaiveXCorr': PAL['red'],
    'DiffXCorr':  PAL['orange'],
    'Threshold':  PAL['purple'],
    'PermG':      PAL['blue'],
    'TY':         PAL['green'],
}

def _style():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
        'font.size': 9,
        'axes.labelsize': 10,
        'axes.titlesize': 10,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'legend.fontsize': 7,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'mathtext.fontset': 'cm',
        'lines.linewidth': 1.4,
    })

def _save(fig, name):
    for ext in ('pdf', 'png'):
        fig.savefig(OUT / f'{name}.{ext}')
    plt.close(fig)
    print(f'  Saved {name}.pdf + .png')


# ═══════════════════════════════════════════════════════════
# Figure 1: Null-control FPR diagnostic (5 methods)
# ═══════════════════════════════════════════════════════════
def fig_null_fpr_diagnostic():
    print('Fig 1: null_fpr_diagnostic')
    # Data from appendix Table null_fpr_methods (6 seeds × 6 pairs = 36 total)
    methods_order = ['NaiveXCorr', 'DiffXCorr', 'Threshold', 'PermG', 'TY']
    method_labels = ['Naive\nXCorr', 'Diff.\nXCorr', 'Threshold\n$(3\\sigma)$', 'Perm.\nGranger', 'Toda–\nYam.']
    # Rejections out of 36
    rejections = {'NaiveXCorr': 33, 'DiffXCorr': 1, 'Threshold': 10, 'PermG': 4, 'TY': 14}
    pooled_fpr = {m: rejections[m] / 36 * 100 for m in methods_order}

    # Per-seed data from fpr_transparency_all_seeds.json for seed-level dots
    with open(ROOT / 'artifacts' / 'fpr_transparency_all_seeds.json') as f:
        d = json.load(f)

    seed_fpr = {m: [] for m in methods_order}
    for sd in d['seeds']:
        pairs = sd['pairs']
        n = len(pairs)
        counts = {m: 0 for m in methods_order}
        for p in pairs:
            if p.get('naive_xcorr_sig', False):
                counts['NaiveXCorr'] += 1
            if p.get('diff_xcorr_fwd_sig_fdr', False):
                counts['DiffXCorr'] += 1
            if p.get('threshold_onset_sig', False):
                counts['Threshold'] += 1
            if p.get('perm_granger_fwd_sig_fdr', False):
                counts['PermG'] += 1
            if p.get('ty_granger_sig', False):
                counts['TY'] += 1
        for m in methods_order:
            seed_fpr[m].append(counts[m] / n * 100)

    fig, ax = plt.subplots(figsize=(4.5, 2.8))
    x = np.arange(len(methods_order))
    colors = [METHOD_COLORS[m] for m in methods_order]

    # Individual seed dots (6 seeds)
    rng = np.random.default_rng(42)
    for m_idx, m in enumerate(methods_order):
        jitter = rng.uniform(-0.15, 0.15, len(seed_fpr[m]))
        ax.scatter(x[m_idx] + jitter, seed_fpr[m], color=colors[m_idx],
                   alpha=0.4, s=18, zorder=3, edgecolors='none')

    # Pooled bar (from paper's reported values)
    bars = ax.bar(x, [pooled_fpr[m] for m in methods_order], width=0.55,
                  color=colors, alpha=0.7, edgecolor='white', linewidth=0.5, zorder=2)

    # Value labels
    for i, m in enumerate(methods_order):
        ax.text(i, pooled_fpr[m] + 3, f'{pooled_fpr[m]:.1f}%',
                ha='center', va='bottom', fontsize=7, fontweight='bold',
                color=colors[i])

    ax.axhline(5, color=PAL['red'], ls='--', lw=0.8, alpha=0.5, zorder=1)
    t = ax.text(-0.45, 6.5, '5% nominal', fontsize=6.5, color=PAL['red'], alpha=0.7)
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

    ax.set_xticks(x)
    ax.set_xticklabels(method_labels)
    ax.set_ylabel('False Positive Rate (%)')
    ax.set_ylim(0, 105)
    ax.yaxis.grid(True, alpha=0.15, lw=0.4)
    ax.set_axisbelow(True)
    _save(fig, 'fig_null_fpr_diagnostic')


# ═══════════════════════════════════════════════════════════
# Figure 2: Per-method phase heatmaps (2×3 grid)
# ═══════════════════════════════════════════════════════════
def fig_per_method_phase():
    print('Fig 2: per_method_phase')
    with open(ROOT / 'artifacts' / 'dose_response_d120_recompiled.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Filter: alpha_sweep, wikitext, fp32, T=10, seed=42
    filtered = [r for r in rows
                if r['category'] == 'alpha_sweep'
                and r['domain'] == 'wikitext'
                and r['precision'] == 'fp32'
                and r['T'] == '10'
                and r['seed'] == '42']

    # Also add t20 data
    t20 = [r for r in rows if r['category'] == 't20' and r['seed'] == '42']

    method_cols = {
        'Naive XCorr': 'naive_fwd',
        'Diff. XCorr': 'diffxcorr_fwd_fdr',
        'Threshold': 'threshold_fwd',
        'Perm. Granger': 'permg_fwd_fdr',
        'Toda–Yam.': 'ty_fwd',
    }
    method_colors_list = ['#333333'] * 5

    # Build alpha grid from filtered data
    alpha_vals = sorted(set(float(r['alpha']) for r in filtered))
    T_vals = [10]
    # Add T=20 alphas
    t20_alphas = sorted(set(float(r['alpha']) for r in t20))

    # For each method, build a matrix: alpha × T
    # Use T=10 from filtered, T=20 from t20
    all_T = [10, 20]
    all_alpha = sorted(set(alpha_vals + t20_alphas))

    fig, axes = plt.subplots(2, 3, figsize=(7.2, 4.2), gridspec_kw={'hspace': 0.45, 'wspace': 0.35})
    axes_flat = axes.flatten()

    for idx, (mname, mcol) in enumerate(method_cols.items()):
        ax = axes_flat[idx]
        # Build matrix: rows=T, cols=alpha
        n_pairs = 8
        matrix = np.full((len(all_T), len(all_alpha)), np.nan)

        for r in filtered:
            a = float(r['alpha'])
            if a in all_alpha:
                ai = all_alpha.index(a)
                val = int(r[mcol]) / n_pairs * 100
                matrix[0, ai] = val

        for r in t20:
            a = float(r['alpha'])
            if a in all_alpha:
                ai = all_alpha.index(a)
                val = int(r[mcol]) / n_pairs * 100
                matrix[1, ai] = val

        im = ax.imshow(matrix, aspect='auto', cmap='RdYlBu_r', vmin=0, vmax=100,
                       interpolation='nearest')

        # Annotate cells
        for ti in range(len(all_T)):
            for ai in range(len(all_alpha)):
                v = matrix[ti, ai]
                if not np.isnan(v):
                    txt_color = 'white' if v > 60 else 'black'
                    ax.text(ai, ti, f'{v:.0f}', ha='center', va='center',
                            fontsize=5.5, color=txt_color, fontweight='bold')

        ax.set_title(mname, fontsize=9, color=method_colors_list[idx], fontweight='bold')
        ax.set_yticks(range(len(all_T)))
        ax.set_yticklabels([f'T={t}' for t in all_T], fontsize=7)

        # Show only a subset of alpha labels
        ax.set_xticks(range(len(all_alpha)))
        alpha_labels = [f'{a:.2f}' if a in [0, 0.25, 0.5, 0.75, 1.0] else '' for a in all_alpha]
        ax.set_xticklabels(alpha_labels, fontsize=6, rotation=45, ha='right')
        if idx >= 3:
            ax.set_xlabel(r'$\alpha$', fontsize=8)

    # Summary panel (bottom right)
    ax_sum = axes_flat[5]
    ax_sum.axis('off')
    summary_text = (
        'Detection rate (%) by method\n'
        'across contamination levels\n'
        '(Pythia-410M, seed 42, fp32)\n\n'
        'Color scale: 0% (blue)\n'
        'to 100% (red)\n\n'
        'PermG shows sharpest\n'
        'onset transition at\n'
        r'$\alpha \approx 0.50$'
    )
    ax_sum.text(0.5, 0.5, summary_text, ha='center', va='center',
                fontsize=7.5, transform=ax_sum.transAxes,
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f0f0', edgecolor=PAL['ltgrey']))

    # Colorbar
    cbar = fig.colorbar(im, ax=axes_flat, shrink=0.6, aspect=30, pad=0.02)
    cbar.set_label('Detection rate (%)', fontsize=8)

    _save(fig, 'fig_per_method_phase')


# ═══════════════════════════════════════════════════════════
# Figure 3: AR(1) diagnostic
# ═══════════════════════════════════════════════════════════
def fig_ar1_diagnostic():
    print('Fig 3: ar1_diagnostic')
    with open(ROOT / 'artifacts' / 'empirical_ar1_coefficients.json') as f:
        d = json.load(f)['experiments']

    exps = ['a000_s42', 'a025_s42', 'a050_s42', 'a075_s42', 'a100_s42']
    labels = [r'$\alpha{=}0.00$', r'$\alpha{=}0.25$', r'$\alpha{=}0.50$',
              r'$\alpha{=}0.75$', r'$\alpha{=}1.00$']
    metrics = ['token_entropy', 'distinct_1']
    metric_titles = ['Token Entropy', 'Distinct-1']

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), gridspec_kw={'wspace': 0.3})

    for mi, (metric, mtitle) in enumerate(zip(metrics, metric_titles)):
        ax = axes[mi]
        x = np.arange(len(exps))
        w = 0.35

        raw_vals = [d[e][metric]['ar1_raw'] for e in exps]
        diff_vals = [d[e][metric]['ar1_diff'] for e in exps]

        ax.bar(x - w/2, raw_vals, w, color=PAL['blue'], alpha=0.8,
               label='Raw', edgecolor='white', linewidth=0.5)
        ax.bar(x + w/2, diff_vals, w, color=PAL['orange'], alpha=0.8,
               label='First-diff', edgecolor='white', linewidth=0.5)

        # Danger zone
        ax.axhline(0.95, color=PAL['red'], ls='--', lw=0.8, alpha=0.6)
        ax.axhline(-0.95, color=PAL['red'], ls='--', lw=0.8, alpha=0.6)
        if mi == 1:
            t = ax.text(len(exps)-0.5, 0.97, r'$\varphi{=}0.95$', fontsize=6,
                        color=PAL['red'], va='bottom', ha='right')
            t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

        ax.axhline(0, color='grey', lw=0.4, alpha=0.5)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=7)
        ax.set_ylabel(r'AR(1) coefficient $\varphi$')
        ax.set_title(mtitle, fontsize=10)
        ax.set_ylim(-1.1, 1.15)
        ax.yaxis.grid(True, alpha=0.12, lw=0.4)
        ax.set_axisbelow(True)

        # Panel label
        ax.text(-0.15, 1.05, f'({"ab"[mi]})', transform=ax.transAxes,
                fontsize=10, fontweight='bold', va='bottom')

    axes[0].legend(loc='upper left', framealpha=0.9, edgecolor='none')
    _save(fig, 'fig_ar1_diagnostic')


# ═══════════════════════════════════════════════════════════
# Figure 4: Cascade onset timeline (Gantt-style)
# ═══════════════════════════════════════════════════════════
def fig_cascade_onset():
    print('Fig 4: cascade_onset')
    with open(DATA / 'moment_cascade_analysis.json') as f:
        d = json.load(f)

    conditions = [
        ('s42', 'a010', r'$\alpha{=}0.10$, s42'),
        ('s42', 'a050', r'$\alpha{=}0.50$, s42'),
        ('s42', 'a075', r'$\alpha{=}0.75$, s42'),
        ('s43', 'a050', r'$\alpha{=}0.50$, s43'),
        ('s43', 'a075', r'$\alpha{=}0.75$, s43'),
    ]
    metrics = ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'perplexity', 'mauve']
    metric_labels = ['Entropy', 'ECE', 'Dist-1', 'Dist-2', 'Dist-3', 'PPL', 'MAUVE']
    metric_colors = [PAL['blue'], PAL['ltblue'], PAL['red'], PAL['orange'],
                     PAL['purple'], PAL['grey'], PAL['green']]

    fig, ax = plt.subplots(figsize=(5.5, 3.5))

    y_pos = 0
    y_ticks = []
    y_labels = []

    for ci, (seed, alpha, label) in enumerate(conditions):
        onset_data = d['onset_results'].get(seed, {}).get(alpha, {})

        for mi, (metric, mlabel) in enumerate(zip(metrics, metric_labels)):
            onset = onset_data.get(metric, {}).get('onset_5pct', None)
            if onset is not None:
                ax.barh(y_pos, 0.6, left=onset - 0.3, height=0.7,
                        color=metric_colors[mi], alpha=0.8, edgecolor='white', linewidth=0.3)
                ax.text(onset, y_pos, str(onset), ha='center', va='center',
                        fontsize=6, fontweight='bold', color='white')
            else:
                ax.text(0.5, y_pos, '—', ha='center', va='center',
                        fontsize=7, color=PAL['grey'])

            if ci == 0:
                y_ticks.append(y_pos)
                y_labels.append(mlabel)
            y_pos += 1

        # Separator between conditions
        if ci < len(conditions) - 1:
            ax.axhline(y_pos - 0.5, color=PAL['ltgrey'], lw=0.5, ls='-')
        y_pos += 0.5

    # Add condition labels on right
    y_start = 0
    for ci, (_, _, label) in enumerate(conditions):
        mid = y_start + len(metrics) / 2 - 0.5
        ax.text(10.5, mid, label, ha='left', va='center', fontsize=7,
                fontstyle='italic', color=PAL['grey'])
        y_start += len(metrics) + 0.5

    ax.set_xlabel('Onset generation (5% threshold)')
    ax.set_xlim(-0.5, 10)
    ax.set_yticks([y_ticks[i] for i in range(len(metrics))])
    ax.set_yticklabels(y_labels, fontsize=7)
    ax.invert_yaxis()
    ax.xaxis.grid(True, alpha=0.15, lw=0.4)
    ax.set_axisbelow(True)
    ax.set_xticks(range(0, 11))

    # Phase annotations
    ax.axvspan(-0.5, 1.5, alpha=0.05, color=PAL['blue'], zorder=0)
    ax.axvspan(1.5, 3.5, alpha=0.05, color=PAL['orange'], zorder=0)
    ax.text(0.5, -1.8, 'Phase 1\n(canary)', ha='center', fontsize=6, color=PAL['blue'])
    ax.text(2.5, -1.8, 'Phase 2\n(diversity)', ha='center', fontsize=6, color=PAL['orange'])

    _save(fig, 'fig_cascade_onset')


# ═══════════════════════════════════════════════════════════
# Figure 5: Bootstrap FPR distribution
# ═══════════════════════════════════════════════════════════
def fig_bootstrap_fpr():
    print('Fig 5: bootstrap_fpr')
    with open(ROOT / 'artifacts' / 'fpr_transparency_all_seeds.json') as f:
        d = json.load(f)

    # Per-seed PermG FPR (from 6 seeds)
    per_seed = d['summary']['per_seed_permg_fwd_fdr']
    seed_fprs = [v / 6 * 100 for v in per_seed.values()]  # 6 pairs per seed

    # Bootstrap
    rng = np.random.default_rng(42)
    n_boot = 10000
    boot_means = []
    for _ in range(n_boot):
        sample = rng.choice(seed_fprs, size=len(seed_fprs), replace=True)
        boot_means.append(np.mean(sample))

    boot_means = np.array(boot_means)
    ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])
    mean_fpr = np.mean(seed_fprs)

    fig, ax = plt.subplots(figsize=(4.0, 2.8))

    ax.hist(boot_means, bins=40, color=PAL['blue'], alpha=0.6, edgecolor='white',
            linewidth=0.3, density=True, zorder=2)

    # KDE overlay
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(boot_means, bw_method=0.3)
    x_kde = np.linspace(0, max(boot_means) * 1.2, 200)
    ax.plot(x_kde, kde(x_kde), color=PAL['blue'], lw=1.5, zorder=3)

    # Mean and CI
    ax.axvline(mean_fpr, color=PAL['red'], ls='-', lw=1.5, zorder=4,
               label=f'Mean = {mean_fpr:.1f}%')
    ax.axvline(ci_lo, color=PAL['orange'], ls='--', lw=1.0, zorder=4)
    ax.axvline(ci_hi, color=PAL['orange'], ls='--', lw=1.0, zorder=4,
               label=f'95% CI [{ci_lo:.1f}%, {ci_hi:.1f}%]')

    # Fill CI
    ax.axvspan(ci_lo, ci_hi, alpha=0.1, color=PAL['orange'], zorder=1)

    # 5% nominal
    ax.axvline(5, color=PAL['grey'], ls=':', lw=0.8, alpha=0.6)
    ax.text(5, ax.get_ylim()[1] * 0.95, '5%\nnominal', fontsize=6,
            color=PAL['grey'], ha='center', va='top')

    ax.set_xlabel('PermG FPR (%)')
    ax.set_ylabel('Bootstrap density')
    ax.legend(loc='upper right', framealpha=0.9, edgecolor='none', fontsize=7)
    ax.yaxis.grid(True, alpha=0.12, lw=0.4)
    ax.set_axisbelow(True)
    _save(fig, 'fig_bootstrap_fpr')


# ═══════════════════════════════════════════════════════════
# Figure 6: Detection surface (α × T contour)
# ═══════════════════════════════════════════════════════════
def fig_detection_surface():
    print('Fig 6: detection_surface')
    # Build detection matrix from dose_response CSV
    with open(ROOT / 'artifacts' / 'dose_response_d120_recompiled.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Collect PermG forward detection rates for WikiText, fp32, Pythia-410M
    data_points = {}
    for r in rows:
        if r['domain'] != 'wikitext' or r['precision'] != 'fp32':
            continue
        if r['model'] != 'gpt2':
            continue
        cat = r['category']
        if cat not in ('alpha_sweep', 't20'):
            continue
        a = float(r['alpha'])
        T = int(r['T'])
        n = int(r['n_pairs'])
        det = int(r['permg_fwd_fdr'])
        rate = det / n
        key = (a, T)
        if key not in data_points:
            data_points[key] = []
        data_points[key].append(rate)

    # Average across seeds
    grid = {k: np.mean(v) for k, v in data_points.items()}

    # Also add T=5 data (all 0) and T=15/T=25 from scale/t20 categories
    # Check for phase_diagram entries
    for r in rows:
        cat = r['category']
        if cat == 'scale' and r['model'] == 'gpt2' and r['precision'] == 'fp32' and r['domain'] == 'wikitext':
            a = float(r['alpha'])
            T = int(r['T'])
            n = int(r['n_pairs'])
            det = int(r['permg_fwd_fdr'])
            rate = det / n
            key = (a, T)
            if key not in data_points:
                data_points[key] = []
            data_points[key].append(rate)
    grid = {k: np.mean(v) for k, v in data_points.items()}

    # Get unique sorted alphas and T values
    alphas = sorted(set(k[0] for k in grid.keys()))
    T_vals = sorted(set(k[1] for k in grid.keys()))

    # Build matrix
    Z = np.full((len(T_vals), len(alphas)), np.nan)
    for (a, t), v in grid.items():
        if a in alphas and t in T_vals:
            Z[T_vals.index(t), alphas.index(a)] = v * 100

    fig, ax = plt.subplots(figsize=(5.0, 3.5))

    # Contourf
    A, T = np.meshgrid(alphas, T_vals)
    levels = np.linspace(0, 100, 11)
    cf = ax.contourf(A, T, Z, levels=levels, cmap='RdYlBu_r', alpha=0.85)
    cs = ax.contour(A, T, Z, levels=[50], colors=[PAL['blue']], linewidths=1.5, linestyles='--')
    ax.clabel(cs, fmt='%d%%', fontsize=7, colors=[PAL['blue']])

    # Scatter actual data points
    for (a, t), v in grid.items():
        ax.scatter(a, t, c=v * 100, cmap='RdYlBu_r', vmin=0, vmax=100,
                   s=25, edgecolors='black', linewidths=0.3, zorder=5)

    # α_c(T) theory curve
    alpha_c_10 = 0.483
    gamma = 1.3
    T_theory = np.linspace(5, 25, 50)
    alpha_c_T = alpha_c_10 * (10 / T_theory) ** gamma
    alpha_c_T = np.clip(alpha_c_T, 0, 1.0)
    ax.plot(alpha_c_T, T_theory, '-', color='white', lw=2.5, zorder=6)
    ax.plot(alpha_c_T, T_theory, '-', color=PAL['blue'], lw=1.5, zorder=7,
            label=r'$\alpha_c(T)$ boundary')

    # Regime labels
    ax.text(0.15, 12, 'Blind', fontsize=9, color='white', fontweight='bold',
            ha='center', va='center',
            path_effects=[pe.withStroke(linewidth=2, foreground=PAL['blue'])])
    ax.text(0.8, 15, 'Detection', fontsize=9, color='white', fontweight='bold',
            ha='center', va='center',
            path_effects=[pe.withStroke(linewidth=2, foreground=PAL['red'])])

    cbar = fig.colorbar(cf, ax=ax, shrink=0.85, aspect=25, pad=0.03)
    cbar.set_label('Detection rate (%)', fontsize=8)

    ax.set_xlabel(r'Contamination fraction $\alpha$')
    ax.set_ylabel(r'Observation window $T$')
    ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')
    _save(fig, 'fig_detection_surface')


# ═══════════════════════════════════════════════════════════
# Figure 7: CUSUM monitoring
# ═══════════════════════════════════════════════════════════
def fig_cusum_monitoring():
    print('Fig 7: cusum_monitoring')
    # Simulate CUSUM on token entropy trajectories from regime_map_data
    with open(DATA / 'regime_map_data.json') as f:
        d = json.load(f)

    # Use empirical AR1 data for entropy series
    with open(ROOT / 'artifacts' / 'empirical_ar1_coefficients.json') as f:
        ar = json.load(f)['experiments']

    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), gridspec_kw={'wspace': 0.3})

    for pi, (exp_key, alpha_label) in enumerate([
        ('a050_s42', r'$\alpha{=}0.50$'),
        ('a075_s42', r'$\alpha{=}0.75$'),
    ]):
        ax = axes[pi]
        series = np.array(ar[exp_key]['token_entropy']['series'])
        gens = np.arange(len(series))

        # Compute CUSUM for different k (allowance) values
        mu0 = series[0]
        k_vals = [0.05, 0.10, 0.25]
        k_colors = [PAL['blue'], PAL['orange'], PAL['red']]
        k_styles = ['-', '--', ':']

        for ki, (k, kc, ks) in enumerate(zip(k_vals, k_colors, k_styles)):
            cusum_pos = np.zeros(len(series))
            cusum_neg = np.zeros(len(series))
            for i in range(1, len(series)):
                z = (series[i] - mu0) / (np.std(series[:3]) + 1e-8)
                cusum_pos[i] = max(0, cusum_pos[i-1] + (-z) - k)
                cusum_neg[i] = max(0, cusum_neg[i-1] + z - k)

            ax.plot(gens, cusum_pos, color=kc, ls=ks, lw=1.2,
                    label=f'$k={k}$', zorder=3)

        # Alarm threshold
        h = 4.0
        ax.axhline(h, color=PAL['grey'], ls='--', lw=0.8, alpha=0.6)
        ax.text(len(series)-1, h + 0.3, f'$h={h}$', fontsize=6,
                color=PAL['grey'], ha='right')

        ax.set_xlabel('Generation')
        ax.set_ylabel('CUSUM$^+$ statistic')
        ax.set_title(alpha_label, fontsize=10)
        ax.set_xlim(0, len(series)-1)
        ax.yaxis.grid(True, alpha=0.12, lw=0.4)
        ax.set_axisbelow(True)
        ax.text(-0.15, 1.05, f'({"ab"[pi]})', transform=ax.transAxes,
                fontsize=10, fontweight='bold', va='bottom')

    axes[0].legend(loc='upper left', framealpha=0.9, edgecolor='none', fontsize=7)
    _save(fig, 'fig_cusum_monitoring')


# ═══════════════════════════════════════════════════════════
# Figure 8: Window sensitivity
# ═══════════════════════════════════════════════════════════
def fig_window_sensitivity():
    print('Fig 8: window_sensitivity')
    # Data from appendix Table window_sensitivity (hardcoded from report)
    # T_min values and consensus stable pairs for α=1.0
    T_min = [5, 6, 7, 8, 9, 10]
    consensus_stable = [0, 6, 6, 6, 6, 6]  # out of 6

    # Per-method stability from report
    methods = ['Naive\nXCorr', 'Diff.\nXCorr', 'Threshold', 'Perm.\nGranger', 'Toda–\nYam.']
    method_stable_from = [5, 5, 5, 6, 7]  # T_min at which method becomes stable

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.8), gridspec_kw={'wspace': 0.35})

    # Panel (a): Consensus stability vs T_min
    ax1.fill_between(T_min, consensus_stable, alpha=0.2, color=PAL['blue'])
    ax1.plot(T_min, consensus_stable, 'o-', color=PAL['blue'], markersize=5,
             markeredgewidth=0, lw=1.5, zorder=3)
    ax1.axhline(6, color=PAL['green'], ls=':', lw=0.7, alpha=0.5)
    ax1.text(5.1, 6.2, '6/6 (stable)', fontsize=6.5, color=PAL['green'])
    ax1.set_xlabel(r'Minimum window $T_{\min}$')
    ax1.set_ylabel('Stable consensus pairs (/6)')
    ax1.set_ylim(-0.5, 7)
    ax1.set_xticks(T_min)
    ax1.yaxis.grid(True, alpha=0.12, lw=0.4)
    ax1.set_axisbelow(True)
    ax1.text(-0.15, 1.05, '(a)', transform=ax1.transAxes,
             fontsize=10, fontweight='bold', va='bottom')

    # Panel (b): Method stability onset
    colors = [PAL['red'], PAL['orange'], PAL['purple'], PAL['blue'], PAL['green']]
    y = np.arange(len(methods))
    bars = ax2.barh(y, method_stable_from, height=0.6, color=colors,
                    alpha=0.8, edgecolor='white', linewidth=0.5)

    for i, v in enumerate(method_stable_from):
        ax2.text(v + 0.1, i, f'$T \\geq {v}$', va='center', fontsize=7,
                 color=colors[i], fontweight='bold')

    ax2.set_yticks(y)
    ax2.set_yticklabels(methods, fontsize=7)
    ax2.set_xlabel(r'$T_{\min}$ for stable detection')
    ax2.set_xlim(0, 10)
    ax2.xaxis.grid(True, alpha=0.12, lw=0.4)
    ax2.set_axisbelow(True)
    ax2.invert_yaxis()
    ax2.text(-0.18, 1.05, '(b)', transform=ax2.transAxes,
             fontsize=10, fontweight='bold', va='bottom')

    _save(fig, 'fig_window_sensitivity')


# ═══════════════════════════════════════════════════════════
# Figure 9: 1.4B Phase diagram
# ═══════════════════════════════════════════════════════════
def fig_14b_phase():
    print('Fig 9: 14b_phase')
    # Data from D213 artifacts
    with open(DATA / 'D213_14b_s42_6pair_combined.json') as f:
        d42 = json.load(f)
    with open(DATA / 'D213_14b_s43_t10_6pair_combined.json') as f:
        d43 = json.load(f)

    # Build grid: alpha × T → PermG fwd detection
    all_results = d42['results'] + d43['results']
    grid = {}
    for r in all_results:
        a = r['alpha']
        T = r['T']
        fwd_str = r['PermG_fwd']
        num, denom = fwd_str.split('/')
        rate = int(num) / int(denom)
        key = (a, T)
        if key not in grid:
            grid[key] = []
        grid[key].append(rate)

    # Average across seeds
    avg_grid = {k: np.mean(v) for k, v in grid.items()}

    alphas = sorted(set(k[0] for k in avg_grid))
    T_vals = sorted(set(k[1] for k in avg_grid))

    Z = np.full((len(T_vals), len(alphas)), np.nan)
    for (a, t), v in avg_grid.items():
        Z[T_vals.index(t), alphas.index(a)] = v * 100

    fig, ax = plt.subplots(figsize=(4.5, 2.8))

    im = ax.imshow(Z, aspect='auto', cmap='RdYlBu_r', vmin=0, vmax=100,
                   interpolation='nearest', origin='lower')

    # Annotate with individual seed fractions
    for ti in range(len(T_vals)):
        for ai in range(len(alphas)):
            v = Z[ti, ai]
            if not np.isnan(v):
                key = (alphas[ai], T_vals[ti])
                entries = [r for r in all_results if r['alpha'] == alphas[ai] and r['T'] == T_vals[ti]]
                if len(entries) == 1:
                    txt = entries[0]['PermG_fwd']
                else:
                    fracs = [r['PermG_fwd'] for r in entries]
                    txt = ' | '.join(fracs)
                tc = 'white' if v > 55 else 'black'
                ax.text(ai, ti, txt, ha='center', va='center',
                        fontsize=6, color=tc, fontweight='bold')

    ax.set_xticks(range(len(alphas)))
    ax.set_xticklabels([f'{a}' for a in alphas])
    ax.set_yticks(range(len(T_vals)))
    ax.set_yticklabels([f'T={t}' for t in T_vals])
    ax.set_xlabel(r'Contamination fraction $\alpha$')
    ax.set_ylabel('Observation window')

    cbar = fig.colorbar(im, ax=ax, shrink=0.85, aspect=25, pad=0.03)
    cbar.set_label('Detection rate (%)', fontsize=8)
    _save(fig, 'fig_14b_phase')


# ═══════════════════════════════════════════════════════════
# Figure 10: Channel effect size (diversity vs perplexity)
# ═══════════════════════════════════════════════════════════
def fig_channel_effect():
    print('Fig 10: channel_effect')
    # Data from appendix Table channel_retention
    channels = ['Diversity', 'Perplexity']
    naive_r = [0.943, 0.924]
    diff_r = [0.921, 0.900]
    med_F = [67.8, 11.5]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.5), gridspec_kw={'wspace': 0.4})

    # Panel (a): Correlation retention
    x = np.arange(2)
    w = 0.3
    ax1.bar(x - w/2, naive_r, w, color=PAL['blue'], alpha=0.8, label='Naive $|r|$',
            edgecolor='white', linewidth=0.5)
    ax1.bar(x + w/2, diff_r, w, color=PAL['orange'], alpha=0.8, label='Diff $|r|$',
            edgecolor='white', linewidth=0.5)

    for i in range(2):
        retention = diff_r[i] / naive_r[i]
        ax1.text(i, max(naive_r[i], diff_r[i]) + 0.01,
                 f'{retention:.1%}\nretained', ha='center', fontsize=6, color=PAL['grey'])

    ax1.set_xticks(x)
    ax1.set_xticklabels(channels)
    ax1.set_ylabel('$|r|$ (correlation)')
    ax1.set_ylim(0.85, 1.0)
    ax1.legend(loc='lower left', framealpha=0.9, edgecolor='none')
    ax1.yaxis.grid(True, alpha=0.12, lw=0.4)
    ax1.set_axisbelow(True)
    ax1.text(-0.15, 1.05, '(a)', transform=ax1.transAxes,
             fontsize=10, fontweight='bold', va='bottom')

    # Panel (b): Granger F-statistic
    bars = ax2.bar(x, med_F, width=0.5, color=[PAL['blue'], PAL['grey']],
                   alpha=0.8, edgecolor='white', linewidth=0.5)
    for i, v in enumerate(med_F):
        ax2.text(i, v + 2, f'$F={v}$', ha='center', fontsize=7, fontweight='bold',
                 color=[PAL['blue'], PAL['grey']][i])

    ratio = med_F[0] / med_F[1]
    ax2.annotate(f'{ratio:.0f}×', xy=(0.5, max(med_F) * 0.5),
                 fontsize=10, ha='center', color=PAL['red'], fontweight='bold')

    ax2.set_xticks(x)
    ax2.set_xticklabels(channels)
    ax2.set_ylabel('Median Granger $F$-statistic')
    ax2.yaxis.grid(True, alpha=0.12, lw=0.4)
    ax2.set_axisbelow(True)
    ax2.text(-0.15, 1.05, '(b)', transform=ax2.transAxes,
             fontsize=10, fontweight='bold', va='bottom')

    _save(fig, 'fig_channel_effect')


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    _style()
    print('Generating appendix figures...\n')

    fig_null_fpr_diagnostic()   # 1
    fig_per_method_phase()      # 2
    fig_ar1_diagnostic()        # 3
    fig_cascade_onset()         # 4
    fig_bootstrap_fpr()         # 5
    fig_detection_surface()     # 6
    fig_cusum_monitoring()      # 7
    fig_window_sensitivity()    # 8
    fig_14b_phase()             # 9
    fig_channel_effect()        # 10

    print('\nAll 10 appendix figures generated.')
