#!/usr/bin/env python3
"""
Paper figures for Importance Margin VLA Compress.
Reads registry.yaml, produces crossover_heatmap.pdf, disruption_curve.pdf, cv_scatter.pdf.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import yaml
import re
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REGISTRY_PATH = SCRIPT_DIR.parent / 'registry.yaml'
OUTPUT_DIR = SCRIPT_DIR

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

METHOD_COLORS = {
    'random':    '#E69F00',
    'l2norm':    '#0072B2',
    'attention': '#009E73',
    'baseline':  '#555555',
}
METHOD_LABELS = {
    'random': 'Random', 'l2norm': 'L2-Norm',
    'attention': 'Attention', 'baseline': 'Baseline',
}
SUITE_COLORS = {
    'Object': '#0072B2', 'Goal': '#D55E00',
    'Spatial': '#009E73', 'Long': '#CC79A7',
}
MODEL_COLORS = {
    'OpenVLA': '#D55E00', u'π0.5': '#0072B2',
    'X-VLA': '#009E73', 'SmolVLA': '#CC79A7',
    'OpenVLA-OFT': '#F0E442',
}

VALID_CONCLUSIONS = {'success', 'negative'}


# ── Data extraction ──────────────────────────────────────────────

def load_registry():
    with open(REGISTRY_PATH) as f:
        return yaml.safe_load(f).get('experiments', {})


def normalize_sr(val):
    if val is None:
        return None
    try:
        val = float(val)
    except (TypeError, ValueError):
        return None
    return val * 100 if val <= 1.0 else val


def extract_model(eid):
    e = eid.lower()
    if 'oft' in e:
        return 'OpenVLA-OFT'
    if 'openvla' in e:
        return 'OpenVLA'
    if 'pi05' in e:
        return 'π0.5'
    if 'xvla' in e:
        return 'X-VLA'
    if 'smolvla' in e:
        return 'SmolVLA'
    return None


def extract_suite(eid, exp):
    spec = exp.get('spec', {}) or {}
    cmd = (spec.get('command', '') or '').lower()
    dp = (spec.get('data_path', '') or '').lower()
    e = eid.lower()
    blob = f'{e} {cmd} {dp}'
    if any(x in blob for x in ['libero_object', 'libero-object', '_object_', '_obj_']):
        return 'Object'
    if any(x in blob for x in ['libero_goal', 'libero-goal', '_goal_']):
        return 'Goal'
    if any(x in blob for x in ['libero_spatial', 'libero-spatial', '_spatial_']):
        return 'Spatial'
    if any(x in blob for x in ['libero_10', 'libero-10', '_long_']):
        return 'Long'
    if ('xvla' in e or 'openvla' in e) and re.search(r'(?:prune|pruning)_k\d', e):
        return 'Object'
    return None


def extract_method(eid, exp):
    spec = exp.get('spec', {}) or {}
    cmd = (spec.get('command', '') or '').lower()
    e = eid.lower()
    if 'baseline' in e or 'prune_mode none' in cmd:
        return 'baseline'
    if any(x in e for x in ['attention', 'attn']) or \
       any(x in cmd for x in ['attention_prune', 'attention_last', 'attention_mean', 'attention_rollout']):
        return 'attention'
    if 'l2norm' in e or 'l2_norm' in cmd or 'l2norm' in cmd:
        return 'l2norm'
    if 'random' in e or 'random_prune' in cmd or '--mode random' in cmd:
        return 'random'
    if re.search(r'(?:prune|pruning)_k\d', e):
        return 'random'
    return None


def extract_k(eid, exp):
    spec = exp.get('spec', {}) or {}
    cmd = spec.get('command', '') or ''
    e = eid.lower()
    if 'baseline' in e:
        return 1.0
    for pat in [r'keep_ratio\s+([\d.]+)', r'k_ratio\s+([\d.]+)']:
        m = re.search(pat, cmd)
        if m:
            return float(m.group(1))
    m = re.search(r'_k(\d+?)(?:_|$)', e)
    if m:
        digits = m.group(1)
        val = int(digits)
        n = len(digits)
        if n <= 2:
            return val / 10.0
        elif n == 3:
            return val / 100.0
        elif n == 4:
            return val / 1000.0
    return None


def get_sr(exp):
    m = exp.get('metrics') or {}
    for f in ['success_rate', 'overall_sr', 'overall_SR', 'overall_success_rate']:
        if f in m:
            return normalize_sr(m[f])
    return None


def version_score(eid):
    e = eid.lower()
    s = 0
    if 'postfix' in e:
        s += 1000
    vm = re.search(r'_v(\d+)', e)
    if vm:
        s += int(vm.group(1)) * 10
    return s


def build_data(exps):
    records = []
    for eid, exp in exps.items():
        if not isinstance(exp, dict):
            continue
        if exp.get('conclusion') not in VALID_CONCLUSIONS:
            continue
        model = extract_model(eid)
        suite = extract_suite(eid, exp)
        method = extract_method(eid, exp)
        k = extract_k(eid, exp)
        sr = get_sr(exp)
        if not all([model, suite, method]) or k is None or sr is None:
            continue
        records.append({
            'model': model, 'suite': suite, 'method': method,
            'k': round(k, 4), 'sr': sr, 'exp_id': eid,
            'vscore': version_score(eid),
        })
    best = {}
    for r in records:
        key = (r['model'], r['suite'], r['method'], r['k'])
        if key not in best or r['vscore'] > best[key]['vscore']:
            best[key] = r
    return list(best.values())


def build_raw_records(exps):
    """All valid records without dedup (for worst-case analysis)."""
    records = []
    for eid, exp in exps.items():
        if not isinstance(exp, dict):
            continue
        if exp.get('conclusion') not in VALID_CONCLUSIONS:
            continue
        model = extract_model(eid)
        suite = extract_suite(eid, exp)
        method = extract_method(eid, exp)
        k = extract_k(eid, exp)
        sr = get_sr(exp)
        if not all([model, suite, method]) or k is None or sr is None:
            continue
        records.append({
            'model': model, 'suite': suite, 'method': method,
            'k': round(k, 4), 'sr': sr,
        })
    return records


# ── Figure 1: Crossover Heatmap ─────────────────────────────────

def cell_bg(method, sr):
    base = mcolors.to_rgb(METHOD_COLORS[method])
    t = 0.15 + 0.55 * (sr / 100.0)
    return tuple(1 - t * (1 - c) for c in base)


def text_col(bg):
    lum = 0.299 * bg[0] + 0.587 * bg[1] + 0.114 * bg[2]
    return 'white' if lum < 0.55 else '#222222'


def plot_crossover_heatmap(data, outpath):
    models = ['OpenVLA', 'π0.5', 'X-VLA']
    suites = ['Object', 'Goal', 'Spatial', 'Long']
    methods_order = ['random', 'l2norm', 'attention']

    k09 = [r for r in data if abs(r['k'] - 0.9) < 0.01
           and r['method'] != 'baseline' and r['model'] in models]

    cells = defaultdict(dict)
    for r in k09:
        cells[(r['model'], r['suite'])][r['method']] = r['sr']

    fig, ax = plt.subplots(figsize=(7.5, 3.8))

    for i, model in enumerate(models):
        for j, suite in enumerate(suites):
            mdata = cells.get((model, suite), {})
            x0, y0 = j - 0.5, i - 0.5

            if not mdata:
                rect = plt.Rectangle((x0, y0), 1, 1,
                                     facecolor='#F0F0F0', edgecolor='white', lw=2)
                ax.add_patch(rect)
                ax.text(j, i, '—', ha='center', va='center',
                        fontsize=14, color='#AAAAAA')
                continue

            best_m = max(mdata, key=mdata.get)
            best_sr = mdata[best_m]
            bg = cell_bg(best_m, best_sr)
            tc = text_col(bg)

            rect = plt.Rectangle((x0, y0), 1, 1,
                                 facecolor=bg, edgecolor='white', lw=2)
            ax.add_patch(rect)

            ax.text(j, i - 0.15, f'{best_sr:.1f}%', ha='center', va='center',
                    fontsize=13, fontweight='bold', color=tc)
            ax.text(j, i + 0.15, METHOD_LABELS[best_m], ha='center', va='center',
                    fontsize=8, color=tc, alpha=0.85, fontstyle='italic')

            others = {m: s for m, s in mdata.items() if m != best_m}
            if others:
                parts = [f'{METHOD_LABELS[m][:3]}={s:.0f}' for m, s in
                         sorted(others.items(), key=lambda x: -x[1])]
                info = '  '.join(parts)
                ax.text(j, i + 0.37, info, ha='center', va='center',
                        fontsize=5.5, color=tc, alpha=0.6)

    ax.set_xlim(-0.5, len(suites) - 0.5)
    ax.set_ylim(len(models) - 0.5, -0.5)
    ax.set_xticks(range(len(suites)))
    ax.set_xticklabels(suites, fontsize=11, fontweight='bold')
    ax.set_yticks(range(len(models)))
    ax.set_yticklabels(models, fontsize=11, fontweight='bold')
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    legend_patches = [mpatches.Patch(facecolor=METHOD_COLORS[m],
                                     label=METHOD_LABELS[m], alpha=0.8)
                      for m in methods_order]
    legend_patches.append(mpatches.Patch(facecolor='#F0F0F0',
                                         edgecolor='#CCCCCC', label='No data'))
    ax.legend(handles=legend_patches, loc='upper left',
              bbox_to_anchor=(1.02, 1.0), fontsize=9, frameon=False)

    ax.set_title('Best SR at $k{=}0.9$: method crossover across models and suites',
                 fontsize=11.5, pad=12)

    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f'Saved: {outpath}')


# ── Figure 2: π0.5 Disruption Curve ─────────────────────────────

def plot_disruption_curve(data, outpath):
    pi_model = 'π0.5'
    pi_data = [r for r in data if r['model'] == pi_model]

    baselines = {}
    for r in pi_data:
        if r['method'] == 'baseline' and r['k'] == 1.0:
            baselines[r['suite']] = r['sr']

    curves = defaultdict(dict)
    for r in pi_data:
        if r['method'] in ('random', 'l2norm'):
            curves[(r['suite'], r['method'])][r['k']] = r['sr']

    for suite, bl in baselines.items():
        for method in ('random', 'l2norm'):
            curves[(suite, method)][1.0] = bl

    fig, (ax_main, ax_sec) = plt.subplots(1, 2, figsize=(12, 4.8),
                                           gridspec_kw={'width_ratios': [1.6, 1]},
                                           sharey=True)

    # ── Left panel: Object suite (primary story) ──
    ax = ax_main
    ax.axvspan(0.85, 0.925, alpha=0.07, color='#D32F2F', zorder=0)
    t = ax.text(0.8875, 3, 'cliff zone', ha='center', va='bottom',
                fontsize=8, color='#B71C1C', alpha=0.45, fontstyle='italic')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

    lstyles = {'random': '-', 'l2norm': '--'}
    markers = {'random': 'o', 'l2norm': 's'}

    for method in ('random', 'l2norm'):
        key = ('Object', method)
        if key not in curves or len(curves[key]) < 2:
            continue
        pts = sorted(curves[key].items())
        ks, srs = zip(*pts)
        c = METHOD_COLORS[method]
        ax.plot(ks, srs, lstyles[method], color=c,
                marker=markers[method], markersize=5, alpha=0.9,
                label=METHOD_LABELS[method], zorder=3, linewidth=2.2)

    r85 = curves.get(('Object', 'random'), {}).get(0.85)
    l85 = curves.get(('Object', 'l2norm'), {}).get(0.85)
    if r85 is not None and l85 is not None:
        ax.annotate(f'{r85:.1f}%', xy=(0.85, r85),
                    xytext=(0.72, r85 + 18), fontsize=8, color=METHOD_COLORS['random'],
                    fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=METHOD_COLORS['random'], lw=0.8),
                    zorder=5)
        ax.annotate(f'{l85:.1f}%', xy=(0.85, l85),
                    xytext=(0.72, l85 - 12), fontsize=8, color=METHOD_COLORS['l2norm'],
                    fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color=METHOD_COLORS['l2norm'], lw=0.8),
                    zorder=5)

    r09 = curves.get(('Object', 'random'), {}).get(0.9)
    l09 = curves.get(('Object', 'l2norm'), {}).get(0.9)
    if r09 is not None and l09 is not None:
        gap = l09 - r09
        mid_y = (r09 + l09) / 2
        ax.annotate('', xy=(0.9, r09 + 2), xytext=(0.9, l09 - 2),
                    arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.2), zorder=4)
        txt = ax.text(0.908, mid_y, f'Δ={gap:.0f}pp', fontsize=8,
                      color='#555555', va='center', fontweight='bold')
        txt.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

    ax.set_xlabel('Keep Ratio ($k$)', fontsize=12)
    ax.set_ylabel('Success Rate (%)', fontsize=12)
    ax.set_xlim(0.25, 1.03)
    ax.set_ylim(-3, 108)
    ax.set_xticks([0.3, 0.5, 0.7, 0.85, 0.9, 0.925, 0.95, 1.0])
    ax.set_xticklabels(['0.3', '0.5', '0.7', '0.85', '0.9', '', '0.95', '1.0'], fontsize=9)
    ax.grid(True, alpha=0.12, zorder=0)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.92, edgecolor='none')
    ax.set_title('(a) Object suite', fontsize=11, pad=6)

    # ── Right panel: Goal, Spatial, Long ──
    ax2 = ax_sec
    ax2.axvspan(0.85, 0.925, alpha=0.07, color='#D32F2F', zorder=0)

    for suite in ['Goal', 'Spatial', 'Long']:
        base_color = SUITE_COLORS[suite]
        for method in ('random', 'l2norm'):
            key = (suite, method)
            if key not in curves or len(curves[key]) < 2:
                continue
            pts = sorted(curves[key].items())
            ks, srs = zip(*pts)
            label = f'{suite} {METHOD_LABELS[method]}'
            ax2.plot(ks, srs, lstyles[method], color=base_color,
                     marker=markers[method], markersize=3.5, alpha=0.75,
                     label=label, zorder=3, linewidth=1.5)

    ax2.set_xlabel('Keep Ratio ($k$)', fontsize=12)
    ax2.set_xlim(0.25, 1.03)
    ax2.set_xticks([0.3, 0.5, 0.7, 0.85, 0.9, 0.95, 1.0])
    ax2.set_xticklabels(['0.3', '0.5', '0.7', '0.85', '0.9', '0.95', '1.0'], fontsize=9)
    ax2.grid(True, alpha=0.12, zorder=0)
    ax2.legend(loc='lower left', fontsize=6.5, ncol=1, framealpha=0.92,
               edgecolor='none', columnspacing=0.8)
    ax2.set_title('(b) Other suites', fontsize=11, pad=6)

    fig.suptitle('π0.5 Disruption Curves: Random vs L2-Norm',
                 fontsize=13, fontweight='bold', y=1.02)

    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f'Saved: {outpath}')


# ── Figure 3: CV Diagnostic Scatter ─────────────────────────────

def plot_cv_scatter(data, raw_records, outpath):
    cv_known = {
        'π0.5':     0.038,
        'OpenVLA':       0.215,
        'SmolVLA':       0.314,
        'X-VLA':         0.025,
    }

    baselines = {}
    worst_k09 = {}

    for r in raw_records:
        if r['suite'] != 'Object':
            continue
        model = r['model']
        if r['method'] == 'baseline' or r['k'] == 1.0:
            baselines[model] = max(baselines.get(model, 0), r['sr'])
        if abs(r['k'] - 0.9) < 0.01 and r['method'] != 'baseline':
            if model not in worst_k09 or r['sr'] < worst_k09[model]:
                worst_k09[model] = r['sr']

    bl_fallback = {
        'OpenVLA': 74.0, 'π0.5': 98.2, 'X-VLA': 99.2,
        'SmolVLA': 57.2,
    }
    for m, b in bl_fallback.items():
        baselines.setdefault(m, b)

    points = []
    for model in cv_known:
        if model not in baselines or model not in worst_k09:
            continue
        cv = cv_known[model]
        drop = baselines[model] - worst_k09[model]
        points.append((model, cv, drop))

    if not points:
        print('Warning: no data for CV scatter')
        return

    fig, ax = plt.subplots(figsize=(6.5, 4.5))

    ax.axhspan(0, 15, alpha=0.04, color='#4CAF50', zorder=0)
    ax.axhspan(50, 105, alpha=0.04, color='#F44336', zorder=0)
    ax.text(0.005, 7, 'robust', fontsize=8, color='#66BB6A', alpha=0.5,
            fontstyle='italic', va='center')
    ax.text(0.005, 80, 'fragile', fontsize=8, color='#EF5350', alpha=0.5,
            fontstyle='italic', va='center')

    offsets = {
        'π0.5': (12, -14), 'OpenVLA': (12, 8), 'X-VLA': (12, -12),
        'SmolVLA': (12, 8),
    }

    for model, cv, drop in points:
        color = MODEL_COLORS.get(model, '#333333')
        ax.scatter(cv, drop, c=color, s=160, zorder=4,
                   edgecolors='white', linewidths=1.5)
        ox, oy = offsets.get(model, (12, 8))
        arrow = dict(arrowstyle='-', color='gray', lw=0.4) if abs(ox) > 20 or abs(oy) > 20 else None
        ax.annotate(model, (cv, drop), xytext=(ox, oy),
                    textcoords='offset points', fontsize=10, color=color,
                    fontweight='bold', arrowprops=arrow)

        detail = f'drop={drop:.1f}pp'
        ax.annotate(detail, (cv, drop), xytext=(ox, oy - 13),
                    textcoords='offset points', fontsize=7, color=color, alpha=0.7)

    ax.set_xlabel('Importance Score CV (coefficient of variation)', fontsize=11)
    ax.set_ylabel('Max SR Drop at $k{=}0.9$ (pp)', fontsize=11)
    ax.set_title('Token Importance CV vs Pruning Sensitivity', fontsize=12, pad=10)
    ax.grid(True, alpha=0.12, zorder=0)

    cv_vals = [p[1] for p in points]
    drop_vals = [p[2] for p in points]
    ax.set_xlim(-0.02, max(cv_vals) + 0.06)
    ax.set_ylim(min(-5, min(drop_vals) - 8), max(drop_vals) + 15)

    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()
    print(f'Saved: {outpath}')


# ── Main ─────────────────────────────────────────────────────────

def main():
    print('Loading registry...')
    exps = load_registry()
    data = build_data(exps)
    raw = build_raw_records(exps)
    n_valid = sum(1 for e in exps.values()
                  if isinstance(e, dict) and e.get('conclusion') in VALID_CONCLUSIONS)
    print(f'Parsed {len(data)} unique data points from {n_valid} experiments')

    plot_crossover_heatmap(data, OUTPUT_DIR / 'crossover_heatmap.pdf')
    plot_disruption_curve(data, OUTPUT_DIR / 'disruption_curve.pdf')
    plot_cv_scatter(data, raw, OUTPUT_DIR / 'cv_scatter.pdf')

    print('\nAll figures saved to:', OUTPUT_DIR)


if __name__ == '__main__':
    main()
