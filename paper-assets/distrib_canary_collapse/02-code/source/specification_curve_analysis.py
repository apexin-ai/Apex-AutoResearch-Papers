#!/usr/bin/env python3
"""
Specification Curve Analysis for Distributional Canary Collapse.

For each experiment (alpha):
  For each specification (method x direction x correction x K-threshold):
    Extract binary detection conclusion from 8 canary-downstream pairs.

Output:
  1. spec_curve_a075.pdf/png  — Full specification curve for alpha=0.75
  2. spec_curve_a050.pdf/png  — Transition regime
  3. spec_curve_comparison.pdf/png — Side-by-side alpha=0.50 vs 0.75
  4. spec_curve_heatmap.pdf/png — alpha x specification heatmap (main figure)
  5. spec_curve_results.json   — Full results
  6. spec_curve_stats.json     — Summary statistics
"""

import json
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from collections import OrderedDict

BASE_DIR = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
OUTPUT_DIR = "/root/autodl-tmp/distrib_canary_collapse/results/spec_curve_analysis"

ALPHA_DIR_MAP = OrderedDict([
    (0.00, "a000_s42_fp32"),
    (0.05, "a005_s42_fp32_v3_d080"),
    (0.10, "a010_s42_fp32"),
    (0.25, "a025_s42_fp32"),
    (0.30, "a030_s42_fp32"),
    (0.35, "a035_s42_fp32"),
    (0.40, "a040_s42_fp32"),
    (0.45, "a045_s42_fp32"),
    (0.46, "a046_s42_fp32"),
    (0.48, "a048_s42_fp32"),
    (0.50, "a050_s42_fp32"),
    (0.52, "a052_s42_fp32"),
    (0.60, "a060_s42_fp32_v4"),
    (0.65, "a065_s42_fp32"),
    (0.70, "a070_s42_fp32"),
    (0.75, "a075_s42_fp32"),
])

METHODS = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
METHOD_LABEL = {
    'naive_xcorr': 'NaiveXCorr',
    'diff_xcorr': 'DiffXCorr',
    'threshold_onset': 'ThreshOnset',
    'perm_granger': 'PermG',
    'ty_granger': 'TY',
}
HAS_FDR = {'diff_xcorr', 'perm_granger'}

METHOD_COLOR = {
    'NaiveXCorr': '#2171b5',
    'DiffXCorr': '#e6550d',
    'ThreshOnset': '#31a354',
    'PermG': '#d62728',
    'TY': '#756bb1',
}
CONSENSUS_COLOR = '#636363'


def build_specs():
    specs = []
    for method in METHODS:
        label = METHOD_LABEL[method]
        for direction in ['forward', 'reverse']:
            d = 'Fwd' if direction == 'forward' else 'Rev'
            specs.append({
                'name': f"{label}_{d}",
                'method': method, 'direction': direction,
                'correction': 'none', 'type': 'method',
                'label': label,
            })
            if method in HAS_FDR:
                specs.append({
                    'name': f"{label}_{d}_FDR",
                    'method': method, 'direction': direction,
                    'correction': 'fdr', 'type': 'method',
                    'label': label,
                })
    for direction in ['forward', 'reverse']:
        d = 'Fwd' if direction == 'forward' else 'Rev'
        for K in [3, 4]:
            specs.append({
                'name': f"K>={K}_{d}",
                'direction': direction, 'type': 'consensus', 'K': K,
                'label': f"K>={K}",
            })
    return specs


def extract_detection(pair, spec):
    dir_data = pair.get(spec['direction'], {})
    if spec['type'] == 'method':
        md = dir_data.get(spec['method'], {})
        if spec['correction'] == 'fdr':
            return int(bool(md.get('significant_fdr', False)))
        return int(bool(md.get('significant', False)))
    elif spec['type'] == 'consensus':
        count = sum(
            1 for m in METHODS
            if dir_data.get(m, {}).get('significant', False)
        )
        return int(count >= spec['K'])
    return 0


def load_experiment(alpha):
    dir_name = ALPHA_DIR_MAP.get(alpha)
    if not dir_name:
        return None
    path = os.path.join(BASE_DIR, dir_name, "analysis", "5method_leadlag.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def spec_color(spec_name):
    for key, c in METHOD_COLOR.items():
        if spec_name.startswith(key):
            return c
    return CONSENSUS_COLOR


def plot_spec_curve(results, specs, alpha_val, filename):
    if alpha_val not in results:
        print(f"  skip α={alpha_val}: no data")
        return
    rates = results[alpha_val]
    sorted_items = sorted(rates.items(), key=lambda x: (-x[1], x[0]))
    names = [s[0] for s in sorted_items]
    values = [s[1] for s in sorted_items]
    colors = [spec_color(n) for n in names]

    spec_map = {s['name']: s for s in specs}

    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(2, 1, height_ratios=[2.5, 2], hspace=0.02)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1], sharex=ax_top)

    x = np.arange(len(names))
    ax_top.bar(x, values, color=colors, edgecolor='white', linewidth=0.5, width=0.85)
    ax_top.set_ylabel('Detection rate (sig pairs / 8)', fontsize=11)
    ax_top.set_title(f'Specification Curve — α = {alpha_val:.2f}', fontsize=13, fontweight='bold')
    ax_top.set_ylim(0, 1.08)
    ax_top.axhline(0.5, color='#aaaaaa', ls='--', lw=0.7)
    ax_top.set_xlim(-0.6, len(names) - 0.4)
    for spine in ['top', 'right', 'bottom']:
        ax_top.spines[spine].set_visible(False)
    ax_top.tick_params(bottom=False, labelbottom=False)

    rows = [
        ('Method', lambda s: spec_map[s].get('label', '?')),
        ('Direction', lambda s: 'Fwd' if 'Fwd' in s else 'Rev'),
        ('Correction', lambda s: 'FDR' if s.endswith('_FDR') else ('—' if spec_map[s]['type'] == 'consensus' else 'None')),
    ]

    all_vals_per_row = []
    for rname, fn in rows:
        vals = sorted(set(fn(n) for n in names))
        all_vals_per_row.append((rname, vals, fn))

    y = 0
    yticks = []
    ytick_labels = []
    for rname, vals, fn in all_vals_per_row:
        for vi, v in enumerate(vals):
            for xi, n in enumerate(names):
                if fn(n) == v:
                    c = spec_color(n) if rname == 'Method' else ('#333333' if fn(n) in ('Fwd', 'FDR') else '#aaaaaa')
                    ax_bot.plot(xi, y, 's', color=c, markersize=5.5, alpha=0.85)
            yticks.append(y)
            ytick_labels.append(v)
            y += 1
        y += 0.6

    ax_bot.set_ylim(y - 0.6, -0.8)
    ax_bot.set_yticks(yticks)
    ax_bot.set_yticklabels(ytick_labels, fontsize=8)
    for spine in ax_bot.spines.values():
        spine.set_visible(False)
    ax_bot.tick_params(left=False, bottom=False, labelbottom=False)

    cat_y = 0
    for rname, vals, fn in all_vals_per_row:
        mid = cat_y + (len(vals) - 1) / 2
        ax_bot.text(-2.0, mid, rname, ha='right', va='center', fontsize=9, fontweight='bold',
                    transform=ax_bot.get_yaxis_transform())
        cat_y += len(vals) + 0.6

    for ext in ['pdf', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f"{filename}.{ext}"), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  saved {filename}")


def plot_comparison(results, specs):
    if 0.50 not in results or 0.75 not in results:
        print("  skip comparison: missing data")
        return

    fig, axes = plt.subplots(1, 2, figsize=(16, 5.5), sharey=True)
    for ax, alpha_val, subtitle in zip(
        axes, [0.50, 0.75], ['α = 0.50  (transition)', 'α = 0.75  (detection)']
    ):
        rates = results[alpha_val]
        sorted_items = sorted(rates.items(), key=lambda x: (-x[1], x[0]))
        names = [s[0] for s in sorted_items]
        values = [s[1] for s in sorted_items]
        colors = [spec_color(n) for n in names]
        x = np.arange(len(names))
        ax.bar(x, values, color=colors, edgecolor='white', linewidth=0.5, width=0.85)
        ax.set_title(subtitle, fontsize=12, fontweight='bold')
        ax.set_ylim(0, 1.08)
        ax.axhline(0.5, color='#aaaaaa', ls='--', lw=0.7)
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=90, fontsize=6.5)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    axes[0].set_ylabel('Detection rate', fontsize=11)
    fig.suptitle('Specification Curve: Transition vs Detection Regime',
                 fontsize=14, fontweight='bold', y=1.01)
    plt.tight_layout()
    for ext in ['pdf', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f"spec_curve_comparison.{ext}"), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  saved spec_curve_comparison")


def plot_heatmap(results, specs):
    alpha_list = sorted(results.keys())
    spec_names = [s['name'] for s in specs]

    mean_rates = {
        sn: np.mean([results[a].get(sn, 0) for a in alpha_list])
        for sn in spec_names
    }
    sorted_sn = sorted(spec_names, key=lambda s: -mean_rates[s])

    mat = np.full((len(alpha_list), len(sorted_sn)), np.nan)
    for i, a in enumerate(alpha_list):
        for j, sn in enumerate(sorted_sn):
            mat[i, j] = results[a].get(sn, np.nan)

    cmap = LinearSegmentedColormap.from_list(
        'detect', ['#f7f7f7', '#fee08b', '#fc8d59', '#d73027', '#a50026'], N=256
    )

    fig, ax = plt.subplots(figsize=(17, 8))
    im = ax.imshow(mat, aspect='auto', cmap=cmap, vmin=0, vmax=1, interpolation='nearest')

    ax.set_xticks(np.arange(len(sorted_sn)))
    ax.set_xticklabels(sorted_sn, rotation=90, fontsize=7.5)
    ax.set_yticks(np.arange(len(alpha_list)))
    ax.set_yticklabels([f"α={a:.2f}" for a in alpha_list], fontsize=9)

    for i in range(len(alpha_list)):
        for j in range(len(sorted_sn)):
            v = mat[i, j]
            if np.isnan(v):
                continue
            tc = 'white' if v > 0.65 else 'black'
            frac = f"{v:.0%}" if v in (0, 1) else f"{v:.0%}"
            ax.text(j, i, frac, ha='center', va='center', fontsize=6.5, color=tc, fontweight='medium')

    top_colors = [spec_color(sn) for sn in sorted_sn]
    for j, c in enumerate(top_colors):
        ax.plot(j, -0.6, 's', color=c, markersize=5, clip_on=False)

    ax.set_title('Detection Rate across α × Specification', fontsize=14, fontweight='bold', pad=18)
    ax.set_xlabel('Specification (sorted by mean detection rate)', fontsize=11)
    ax.set_ylabel('Contamination level α', fontsize=11)

    cbar = plt.colorbar(im, ax=ax, shrink=0.75, pad=0.02)
    cbar.set_label('Detection rate (sig / 8 pairs)', fontsize=10)

    handles = [plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=c, markersize=8, label=l)
               for l, c in METHOD_COLOR.items()]
    handles.append(plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=CONSENSUS_COLOR,
                              markersize=8, label='Consensus'))
    ax.legend(handles=handles, loc='upper left', bbox_to_anchor=(1.08, 0.5),
              fontsize=8, frameon=False, title='Method', title_fontsize=9)

    plt.tight_layout()
    for ext in ['pdf', 'png']:
        fig.savefig(os.path.join(OUTPUT_DIR, f"spec_curve_heatmap.{ext}"), dpi=200, bbox_inches='tight')
    plt.close(fig)
    print("  saved spec_curve_heatmap")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    specs = build_specs()
    alphas = sorted(ALPHA_DIR_MAP.keys())

    print(f"Specifications defined: {len(specs)}")
    for s in specs:
        print(f"  {s['name']}")

    # --- Data collection ---
    print("\n=== DATA COLLECTION ===")
    results = {}
    missing = []
    for alpha in alphas:
        data = load_experiment(alpha)
        if data is None:
            missing.append(alpha)
            print(f"  α={alpha:.2f}: MISSING")
            continue
        pairs = data['pairs']
        n_pairs = len(pairs)
        results[alpha] = {}
        for spec in specs:
            detections = [extract_detection(p, spec) for p in pairs]
            results[alpha][spec['name']] = sum(detections) / n_pairs
        print(f"  α={alpha:.2f}: loaded ({n_pairs} pairs)")

    # --- Save results ---
    out_results = {f"{a:.2f}": v for a, v in sorted(results.items())}
    with open(os.path.join(OUTPUT_DIR, "spec_curve_results.json"), 'w') as f:
        json.dump(out_results, f, indent=2)
    print(f"\nSaved spec_curve_results.json ({len(results)} experiments × {len(specs)} specs)")

    # --- Statistics ---
    print("\n=== STATISTICS ===")
    stats = {}
    for alpha in sorted(results.keys()):
        rates = list(results[alpha].values())
        q25, q50, q75 = np.percentile(rates, [25, 50, 75])
        stats[f"{alpha:.2f}"] = {
            'median': round(float(q50), 4),
            'iqr': round(float(q75 - q25), 4),
            'mean': round(float(np.mean(rates)), 4),
            'std': round(float(np.std(rates)), 4),
            'min': round(float(min(rates)), 4),
            'max': round(float(max(rates)), 4),
            'n_always_detected': sum(1 for r in rates if r == 1.0),
            'n_never_detected': sum(1 for r in rates if r == 0.0),
            'n_specs': len(rates),
        }
        s = stats[f"{alpha:.2f}"]
        print(f"  α={alpha:.2f}: median={s['median']:.3f}  IQR={s['iqr']:.3f}  "
              f"always={s['n_always_detected']}/{s['n_specs']}  never={s['n_never_detected']}/{s['n_specs']}")

    with open(os.path.join(OUTPUT_DIR, "spec_curve_stats.json"), 'w') as f:
        json.dump(stats, f, indent=2)

    # --- Specification sensitivity ---
    print("\n=== SPECIFICATION SENSITIVITY (high-α ≥0.60 vs low-α ≤0.25) ===")
    spec_names = [s['name'] for s in specs]
    sensitivity = {}
    for sn in spec_names:
        high = [results[a][sn] for a in results if a >= 0.60]
        low = [results[a][sn] for a in results if a <= 0.25]
        mh = np.mean(high) if high else np.nan
        ml = np.mean(low) if low else np.nan
        delta = mh - ml
        sensitivity[sn] = {'high_mean': mh, 'low_mean': ml, 'delta': delta}
        print(f"  {sn:28s}  high={mh:.3f}  low={ml:.3f}  Δ={delta:+.3f}")

    robust = [sn for sn in spec_names
              if all(results[a].get(sn, 0) > 0 for a in results if a >= 0.60)]
    always_null = [sn for sn in spec_names
                   if all(results[a].get(sn, 0) == 0 for a in results if a <= 0.30)]
    print(f"\n  Robust at high-α (>0 for all α≥0.60): {robust}")
    print(f"  Consistently null at low-α (=0 for all α≤0.30): {always_null}")

    # --- Visualization ---
    print("\n=== GENERATING FIGURES ===")
    plot_spec_curve(results, specs, 0.75, "spec_curve_a075")
    plot_spec_curve(results, specs, 0.50, "spec_curve_a050")
    plot_comparison(results, specs)
    plot_heatmap(results, specs)

    print(f"\n=== DONE ===")
    print(f"All outputs in {OUTPUT_DIR}")
    if missing:
        print(f"Missing alphas: {missing}")


if __name__ == "__main__":
    main()
