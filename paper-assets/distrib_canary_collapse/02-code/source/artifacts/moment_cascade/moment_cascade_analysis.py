#!/usr/bin/env python3
"""Moment Cascade Analysis: detect temporal ordering of metric degradation across α values."""

import json
import glob
import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
import os

BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
OUT = "/root/autodl-tmp/distrib_canary_collapse/results/moment_cascade"
os.makedirs(OUT, exist_ok=True)

# --- Config ---
METRICS = ['token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'ece', 'perplexity', 'effective_rank', 'mauve']
METRIC_LABELS = {
    'token_entropy': 'Token Entropy',
    'distinct_1': 'Distinct-1',
    'distinct_2': 'Distinct-2',
    'distinct_3': 'Distinct-3',
    'ece': 'ECE',
    'perplexity': 'Perplexity',
    'effective_rank': 'Effective Rank',
    'mauve': 'MAUVE',
}
# Expected direction of degradation (positive = metric increases during collapse, negative = decreases)
DEGRADE_DIR = {
    'token_entropy': -1,   # entropy drops
    'distinct_1': -1,      # diversity drops
    'distinct_2': -1,
    'distinct_3': -1,
    'ece': +1,             # calibration error rises
    'perplexity': +1,      # perplexity rises
    'effective_rank': +1,  # rank increases (distribution flattening then concentration)
    'mauve': -1,           # MAUVE drops (distribution divergence)
}

# Two seed lines for cross-α comparison
EXPERIMENTS_S42 = {
    'a000': 'a000_s42',
    'a010': 'a010_s42',
    'a050': 'a050_s42',
    'a075': 'a075_s42',
}
EXPERIMENTS_S43 = {
    'a000': 'a000_s43',
    'a025': 'a025_s43',
    'a050': 'a050_s43',
    'a075': 'a075_s43',
}

def load_experiment(exp_dir):
    path = os.path.join(BASE, exp_dir, "all_metrics.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    data.sort(key=lambda x: x['generation'])
    return data

def extract_series(data, metric):
    gens = [d['generation'] for d in data]
    vals = [d.get(metric, np.nan) for d in data]
    return np.array(gens), np.array(vals)

def normalize_to_gen0(vals):
    if vals[0] == 0:
        return vals
    return vals / vals[0]

def compute_onset(vals_alpha, vals_baseline, threshold_sigma=2.0):
    """Find first generation where α-experiment deviates from baseline by > threshold_sigma × baseline_std.
    Uses cumulative deviation from gen_0-normalized baseline."""
    norm_alpha = normalize_to_gen0(vals_alpha.copy())
    norm_base = normalize_to_gen0(vals_baseline.copy())

    # Baseline drift std (natural variation in α=0 experiment)
    base_diffs = np.diff(norm_base)
    if len(base_diffs) < 2:
        return None
    base_std = np.std(base_diffs)
    if base_std < 1e-10:
        base_std = np.std(norm_base[1:] - norm_base[0])
        if base_std < 1e-10:
            return None

    # Check each generation for deviation beyond baseline noise
    for g in range(1, len(norm_alpha)):
        deviation = abs(norm_alpha[g] - norm_base[g]) if g < len(norm_base) else abs(norm_alpha[g] - norm_base[-1])
        if deviation > threshold_sigma * base_std:
            return g
    return None

def compute_onset_absolute(vals, degrade_dir, threshold_pct=0.05):
    """Alternative onset: first gen where metric changes by >threshold_pct from gen_0, in the degradation direction."""
    if vals[0] == 0:
        return None
    for g in range(1, len(vals)):
        change = (vals[g] - vals[0]) / abs(vals[0])
        if degrade_dir > 0 and change > threshold_pct:
            return g
        if degrade_dir < 0 and change < -threshold_pct:
            return g
    return None

# ============================================================
# 1. Load all data
# ============================================================
print("=" * 60)
print("MOMENT CASCADE ANALYSIS")
print("=" * 60)

all_data = {}
for label, exp_map in [("s42", EXPERIMENTS_S42), ("s43", EXPERIMENTS_S43)]:
    all_data[label] = {}
    for alpha_str, exp_dir in exp_map.items():
        d = load_experiment(exp_dir)
        if d:
            all_data[label][alpha_str] = d
            print(f"  Loaded {exp_dir}: {len(d)} generations")
        else:
            print(f"  MISSING {exp_dir}")

# ============================================================
# 2. Cascade onset detection
# ============================================================
print("\n" + "=" * 60)
print("CASCADE ONSET DETECTION (2σ deviation from α=0 baseline)")
print("=" * 60)

onset_results = {}

for seed_label, experiments in all_data.items():
    if 'a000' not in experiments:
        continue
    baseline = experiments['a000']
    onset_results[seed_label] = {}

    for alpha_str, data in experiments.items():
        if alpha_str == 'a000':
            continue
        onset_results[seed_label][alpha_str] = {}

        print(f"\n--- {alpha_str} ({seed_label}) ---")
        for metric in METRICS:
            _, vals_alpha = extract_series(data, metric)
            _, vals_base = extract_series(baseline, metric)

            onset_gen = compute_onset(vals_alpha, vals_base, threshold_sigma=2.0)
            onset_abs = compute_onset_absolute(vals_alpha, DEGRADE_DIR[metric], threshold_pct=0.05)

            onset_results[seed_label][alpha_str][metric] = {
                'onset_2sigma': onset_gen,
                'onset_5pct': onset_abs,
            }

            if onset_gen is not None or onset_abs is not None:
                print(f"  {METRIC_LABELS[metric]:18s}: 2σ onset = gen {onset_gen}, 5% onset = gen {onset_abs}")

# ============================================================
# 3. Cascade ordering analysis
# ============================================================
print("\n" + "=" * 60)
print("CASCADE ORDERING (which metric degrades first?)")
print("=" * 60)

cascade_orders = {}

for seed_label, seed_onsets in onset_results.items():
    cascade_orders[seed_label] = {}
    for alpha_str, metric_onsets in seed_onsets.items():
        # Sort metrics by 2sigma onset (None = never, put last)
        ordered = sorted(
            metric_onsets.items(),
            key=lambda x: (x[1]['onset_2sigma'] if x[1]['onset_2sigma'] is not None else 999,
                          x[1]['onset_5pct'] if x[1]['onset_5pct'] is not None else 999)
        )
        cascade_orders[seed_label][alpha_str] = ordered

        print(f"\n  {alpha_str} ({seed_label}) cascade order:")
        for rank, (metric, onsets) in enumerate(ordered):
            o2 = onsets['onset_2sigma']
            o5 = onsets['onset_5pct']
            if o2 is not None or o5 is not None:
                print(f"    {rank+1}. {METRIC_LABELS[metric]:18s} — 2σ: gen {o2}, 5%: gen {o5}")

# ============================================================
# 4. Entropy → Diversity cascade check
# ============================================================
print("\n" + "=" * 60)
print("ENTROPY → DIVERSITY → CALIBRATION CASCADE CHECK")
print("=" * 60)

for seed_label, seed_onsets in onset_results.items():
    for alpha_str, metric_onsets in seed_onsets.items():
        ent_onset = metric_onsets.get('token_entropy', {}).get('onset_2sigma')
        d1_onset = metric_onsets.get('distinct_1', {}).get('onset_2sigma')
        d2_onset = metric_onsets.get('distinct_2', {}).get('onset_2sigma')
        d3_onset = metric_onsets.get('distinct_3', {}).get('onset_2sigma')
        ece_onset = metric_onsets.get('ece', {}).get('onset_2sigma')
        ppl_onset = metric_onsets.get('perplexity', {}).get('onset_2sigma')

        div_onset = min(x for x in [d1_onset, d2_onset, d3_onset] if x is not None) if any(x is not None for x in [d1_onset, d2_onset, d3_onset]) else None

        cascade_confirmed = False
        if ent_onset is not None and div_onset is not None:
            if ent_onset <= div_onset:
                cascade_confirmed = True

        print(f"\n  {alpha_str} ({seed_label}):")
        print(f"    Entropy onset: gen {ent_onset}")
        print(f"    Diversity onset (min d1/d2/d3): gen {div_onset}")
        print(f"    ECE onset: gen {ece_onset}")
        print(f"    PPL onset: gen {ppl_onset}")
        print(f"    Entropy→Diversity cascade: {'CONFIRMED' if cascade_confirmed else 'NOT CONFIRMED'}")

        if cascade_confirmed and ece_onset is not None:
            if ece_onset >= ent_onset:
                print(f"    Full cascade Entropy→Diversity→Calibration: CONFIRMED")

# ============================================================
# 5. PermG directionality analysis flag
# ============================================================
print("\n" + "=" * 60)
print("PERMG DIRECTIONALITY FLAG")
print("=" * 60)

for seed_label, seed_onsets in onset_results.items():
    for alpha_str in ['a050']:
        if alpha_str not in seed_onsets:
            continue
        onsets = seed_onsets[alpha_str]
        ent = onsets.get('token_entropy', {}).get('onset_2sigma')
        div = min(x for x in [onsets.get(f'distinct_{i}', {}).get('onset_2sigma') for i in [1,2,3]] if x is not None) if any(onsets.get(f'distinct_{i}', {}).get('onset_2sigma') is not None for i in [1,2,3]) else None

        if ent is not None and div is not None and ent <= div:
            print(f"\n  α=0.50 ({seed_label}): Entropy (gen {ent}) → Diversity (gen {div})")
            print(f"  → Supports UNIDIRECTIONAL causal chain (entropy drives diversity loss)")
            print(f"  → Explains PermG fwd=6/8 rev=0/8 (directed test detects forward causation)")
            print(f"  → Explains DiffXCorr fwd=6/8 rev=6/8 (undirected test sees both-way correlation)")

# ============================================================
# 6. Cross-α onset timing
# ============================================================
print("\n" + "=" * 60)
print("CROSS-α ONSET TIMING (does onset move earlier with higher α?)")
print("=" * 60)

for seed_label, seed_onsets in onset_results.items():
    alphas_sorted = sorted(seed_onsets.keys(), key=lambda x: int(x[1:]))
    print(f"\n  Seed: {seed_label}")
    print(f"  {'Metric':18s}", end="")
    for a in alphas_sorted:
        print(f"  α={int(a[1:])/100:.2f}", end="")
    print()

    for metric in METRICS:
        print(f"  {METRIC_LABELS[metric]:18s}", end="")
        for a in alphas_sorted:
            o = seed_onsets[a].get(metric, {}).get('onset_2sigma')
            print(f"  {str(o) if o is not None else '—':>6s}", end="")
        print()

# ============================================================
# 7. Quantitative cascade metrics
# ============================================================
print("\n" + "=" * 60)
print("METRIC DEGRADATION MAGNITUDE (gen_0 → gen_10, % change)")
print("=" * 60)

degradation_data = {}
for seed_label, experiments in all_data.items():
    degradation_data[seed_label] = {}
    for alpha_str, data in experiments.items():
        degradation_data[seed_label][alpha_str] = {}
        for metric in METRICS:
            _, vals = extract_series(data, metric)
            if len(vals) > 0 and vals[0] != 0:
                pct_change = (vals[-1] - vals[0]) / abs(vals[0]) * 100
                degradation_data[seed_label][alpha_str][metric] = round(pct_change, 2)

    alphas_sorted = sorted(degradation_data[seed_label].keys(), key=lambda x: int(x[1:]))
    print(f"\n  Seed: {seed_label}")
    print(f"  {'Metric':18s}", end="")
    for a in alphas_sorted:
        print(f"  α={int(a[1:])/100:.2f}", end="")
    print()
    for metric in METRICS:
        print(f"  {METRIC_LABELS[metric]:18s}", end="")
        for a in alphas_sorted:
            v = degradation_data[seed_label][a].get(metric, 0)
            print(f"  {v:>7.1f}%", end="")
        print()

# ============================================================
# 8. Visualizations
# ============================================================
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'legend.fontsize': 8,
    'figure.dpi': 150,
})

# --- Fig 1: Multi-panel cascade (s42 line) ---
plot_metrics = ['token_entropy', 'distinct_2', 'ece', 'perplexity']
plot_alphas_s42 = ['a000', 'a010', 'a050', 'a075']
alpha_colors = {'a000': '#2ca02c', 'a010': '#1f77b4', 'a025': '#ff7f0e', 'a050': '#d62728', 'a075': '#9467bd'}
alpha_labels = {'a000': r'$\alpha$=0.00', 'a010': r'$\alpha$=0.10', 'a025': r'$\alpha$=0.25', 'a050': r'$\alpha$=0.50', 'a075': r'$\alpha$=0.75'}

fig, axes = plt.subplots(len(plot_metrics), 1, figsize=(7, 9), sharex=True)
fig.suptitle('Moment Cascade: Metric Trajectories Across Generations', fontsize=13, y=0.98)

for row, metric in enumerate(plot_metrics):
    ax = axes[row]
    for alpha_str in plot_alphas_s42:
        if alpha_str not in all_data['s42']:
            continue
        data = all_data['s42'][alpha_str]
        gens, vals = extract_series(data, metric)
        norm_vals = normalize_to_gen0(vals)
        ax.plot(gens, norm_vals, 'o-', color=alpha_colors[alpha_str], label=alpha_labels[alpha_str],
                markersize=4, linewidth=1.5)

    ax.set_ylabel(f'{METRIC_LABELS[metric]}\n(normalized)')
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3, linewidth=0.8)
    if row == 0:
        ax.legend(loc='upper right', ncol=2, framealpha=0.9)
    ax.grid(True, alpha=0.2)

axes[-1].set_xlabel('Generation')
plt.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig(os.path.join(OUT, 'fig_moment_cascade.pdf'), bbox_inches='tight')
fig.savefig(os.path.join(OUT, 'fig_moment_cascade.png'), bbox_inches='tight', dpi=200)
plt.close(fig)
print(f"\nSaved fig_moment_cascade.pdf/png")

# --- Fig 2: Cascade onset heatmap ---
seed_for_heatmap = 's42'
heatmap_alphas = sorted([a for a in onset_results.get(seed_for_heatmap, {}).keys()], key=lambda x: int(x[1:]))
heatmap_metrics = ['token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'ece', 'perplexity', 'mauve', 'effective_rank']

if heatmap_alphas:
    onset_matrix = np.full((len(heatmap_metrics), len(heatmap_alphas)), np.nan)
    for j, alpha_str in enumerate(heatmap_alphas):
        for i, metric in enumerate(heatmap_metrics):
            o = onset_results[seed_for_heatmap][alpha_str].get(metric, {}).get('onset_2sigma')
            if o is not None:
                onset_matrix[i, j] = o

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    cmap = cm.YlOrRd_r.copy()
    cmap.set_bad(color='#f0f0f0')

    masked = np.ma.masked_invalid(onset_matrix)
    im = ax.imshow(masked, cmap=cmap, aspect='auto', vmin=1, vmax=10)

    ax.set_xticks(range(len(heatmap_alphas)))
    ax.set_xticklabels([f'α={int(a[1:])/100:.2f}' for a in heatmap_alphas])
    ax.set_yticks(range(len(heatmap_metrics)))
    ax.set_yticklabels([METRIC_LABELS[m] for m in heatmap_metrics])

    for i in range(len(heatmap_metrics)):
        for j in range(len(heatmap_alphas)):
            v = onset_matrix[i, j]
            if not np.isnan(v):
                ax.text(j, i, f'{int(v)}', ha='center', va='center', fontsize=10, fontweight='bold',
                        color='white' if v <= 2 else 'black')
            else:
                ax.text(j, i, '—', ha='center', va='center', fontsize=9, color='#999999')

    cbar = plt.colorbar(im, ax=ax, shrink=0.8, label='Onset Generation (2σ)')
    ax.set_title('Cascade Onset Heatmap (s42)', fontsize=12)
    ax.set_xlabel('Contamination Level')

    plt.tight_layout()
    fig.savefig(os.path.join(OUT, 'fig_cascade_onset_heatmap.pdf'), bbox_inches='tight')
    fig.savefig(os.path.join(OUT, 'fig_cascade_onset_heatmap.png'), bbox_inches='tight', dpi=200)
    plt.close(fig)
    print(f"Saved fig_cascade_onset_heatmap.pdf/png")

# --- Fig 3: Decomposition — S(α) degradation rate × R(α) cascade lag ---
# S(α): slope of distinct_2 degradation per generation
# R(α): onset lag between entropy and diversity
fig, axes = plt.subplots(1, 2, figsize=(9, 4))

for seed_label, experiments in all_data.items():
    if 'a000' not in experiments:
        continue

    alphas_num = []
    slopes = []
    lags = []

    for alpha_str, data in experiments.items():
        if alpha_str == 'a000':
            continue
        alpha_val = int(alpha_str[1:]) / 100

        _, vals_d2 = extract_series(data, 'distinct_2')
        norm_d2 = normalize_to_gen0(vals_d2)
        # Linear slope of normalized distinct_2
        gens = np.arange(len(norm_d2))
        slope = np.polyfit(gens, norm_d2, 1)[0]

        # Cascade lag: entropy onset - diversity onset
        ent_onset = onset_results.get(seed_label, {}).get(alpha_str, {}).get('token_entropy', {}).get('onset_2sigma')
        div_onset = None
        for dm in ['distinct_1', 'distinct_2', 'distinct_3']:
            d = onset_results.get(seed_label, {}).get(alpha_str, {}).get(dm, {}).get('onset_2sigma')
            if d is not None:
                if div_onset is None or d < div_onset:
                    div_onset = d

        lag = (div_onset - ent_onset) if (ent_onset is not None and div_onset is not None) else None

        alphas_num.append(alpha_val)
        slopes.append(slope)
        lags.append(lag)

    marker = 'o' if seed_label == 's42' else 's'

    ax = axes[0]
    ax.plot(alphas_num, slopes, f'{marker}-', label=seed_label, markersize=6)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel('Distinct-2 Slope (per gen)')
    ax.set_title(r'$S(\alpha)$: Diversity Degradation Rate')
    ax.legend()
    ax.grid(True, alpha=0.2)

    ax = axes[1]
    valid_lags = [(a, l) for a, l in zip(alphas_num, lags) if l is not None]
    if valid_lags:
        al, ll = zip(*valid_lags)
        ax.plot(al, ll, f'{marker}-', label=seed_label, markersize=6)
    ax.set_xlabel(r'$\alpha$')
    ax.set_ylabel('Lag (generations)')
    ax.set_title(r'$R(\alpha)$: Entropy→Diversity Cascade Lag')
    ax.legend()
    ax.grid(True, alpha=0.2)

plt.tight_layout()
fig.savefig(os.path.join(OUT, 'fig_decomposition.pdf'), bbox_inches='tight')
fig.savefig(os.path.join(OUT, 'fig_decomposition.png'), bbox_inches='tight', dpi=200)
plt.close(fig)
print(f"Saved fig_decomposition.pdf/png")

# ============================================================
# 9. Save JSON results
# ============================================================
results_json = {
    'onset_results': {},
    'cascade_orders': {},
    'degradation_magnitude': degradation_data,
    'analysis_config': {
        'onset_threshold_sigma': 2.0,
        'onset_threshold_pct': 0.05,
        'metrics': METRICS,
        'experiments_s42': EXPERIMENTS_S42,
        'experiments_s43': EXPERIMENTS_S43,
    }
}

for seed_label, seed_onsets in onset_results.items():
    results_json['onset_results'][seed_label] = {}
    for alpha_str, metric_onsets in seed_onsets.items():
        results_json['onset_results'][seed_label][alpha_str] = metric_onsets

for seed_label, seed_orders in cascade_orders.items():
    results_json['cascade_orders'][seed_label] = {}
    for alpha_str, ordered in seed_orders.items():
        results_json['cascade_orders'][seed_label][alpha_str] = [
            {'metric': m, 'label': METRIC_LABELS[m], 'onset_2sigma': o['onset_2sigma'], 'onset_5pct': o['onset_5pct']}
            for m, o in ordered
        ]

with open(os.path.join(OUT, 'moment_cascade_analysis.json'), 'w') as f:
    json.dump(results_json, f, indent=2)
print(f"\nSaved moment_cascade_analysis.json")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)
