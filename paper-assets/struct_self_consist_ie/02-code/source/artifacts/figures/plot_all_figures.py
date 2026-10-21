#!/usr/bin/env python3
"""Generate 3 paper figures from experiment data."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'text.usetex': False,
})

OUT = Path('/root/autodl-tmp/struct_self_consist_ie/output')
FIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/artifacts/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ── Load data ──────────────────────────────────────────────────────────────

def load_json(path):
    with open(path) as f:
        return json.load(f)

# exp_015_v2 has all 5 signals for SciERC NER/RE at N=16
metrics_v2 = load_json(OUT / 'exp_015_v2' / 'exp015_v2_metrics.json')

# n16_5signal_results has CoNLL NER Qwen
n16_data = load_json(OUT / 'n16_5signal_results.json')

# LLaMA CoNLL 3-seed summary
llama_conll = load_json(OUT / 'llama_conll_n16_3seed_5signal_summary.json')

# Selection F1 data
sel_exp016 = load_json(OUT / 'exp016_signal_ensemble' / 'selection_f1_comparison.json')
sel_exp006 = load_json(OUT / 'exp_006_v2' / 'exp_006_v2_results.json')

# Temperature data
temp_data = load_json(OUT / 'exp_005_v2_temperature' / 'temperature_sensitivity_report.json')

# ── Figure 1: Signal Comparison Heatmap ───────────────────────────────────

signals = ['SJ', 'FK', 'EM', 'voting_conf', 'logprob']
signal_labels = ['SJ', 'FK', 'EM', 'VotConf', 'LogProb']
configs = ['SciERC NER\n(Qwen)', 'CoNLL NER\n(Qwen)', 'CoNLL NER\n(LLaMA)', 'SciERC RE\n(Qwen)']

def extract_rho(section, sig):
    return section['metrics'][sig]['Spearman_rho']['value']

# Full set rho
scierc_ner_s42 = metrics_v2['scierc_n16_seed42_ner']
scierc_ner_s123 = metrics_v2['scierc_n16_seed123_ner']
scierc_re_s42 = metrics_v2['scierc_n16_seed42_re']
scierc_re_s123 = metrics_v2['scierc_n16_seed123_re']

full_rho = np.zeros((4, 5))
cond_rho = np.zeros((4, 5))

# SciERC NER Qwen: 3-seed mean (seed42/123/456) from all_signals_report.json
scierc_ner_3seed_full = {
    'SJ':          [0.4280, 0.4244, 0.3838],
    'FK':          [0.2809, 0.2752, 0.2234],
    'EM':          [0.3347, 0.3369, 0.3162],
    'voting_conf': [0.4408, 0.4131, 0.4111],
    'logprob':     [0.2194, 0.2513, 0.2322],
}
for j, sig in enumerate(signals):
    full_rho[0, j] = np.mean(scierc_ner_3seed_full[sig])

# CoNLL NER Qwen
conll_full = n16_data['exp_002_conll_n16']['full']
for j, sig in enumerate(signals):
    full_rho[1, j] = conll_full[sig]['rho']

# CoNLL NER LLaMA (3-seed mean)
llama_full = llama_conll['3seed_summary_full_rho']
for j, sig in enumerate(signals):
    full_rho[2, j] = llama_full[sig]['mean']

# RE Qwen: 2-seed mean
for j, sig in enumerate(signals):
    full_rho[3, j] = (extract_rho(scierc_re_s42, sig) + extract_rho(scierc_re_s123, sig)) / 2

# Conditional set rho
# CoNLL NER Qwen conditional
conll_cond = n16_data['exp_002_conll_n16']['conditional']
for j, sig in enumerate(signals):
    cond_rho[1, j] = conll_cond[sig]['rho']

# CoNLL NER LLaMA conditional (3-seed mean)
llama_cond = llama_conll['3seed_summary_conditional_rho']
for j, sig in enumerate(signals):
    cond_rho[2, j] = llama_cond[sig]['mean']

# SciERC NER conditional: 3-seed mean (seed42/123/456) from all_signals_report.json
scierc_ner_3seed_cond = {
    'SJ':          [0.3688, 0.3757, 0.3494],
    'FK':          [0.1934, 0.1785, 0.1565],
    'EM':          [0.4151, 0.4036, 0.4058],
    'voting_conf': [0.3531, 0.3393, 0.3459],
    'logprob':     [0.1560, 0.1727, 0.1707],
}
for j, sig in enumerate(signals):
    cond_rho[0, j] = np.mean(scierc_ner_3seed_cond[sig])

# SciERC RE conditional: 2-seed mean (seed42/123) from re_all_signals_report.json
scierc_re_2seed_cond = {
    'SJ':          [0.3274, 0.3092],
    'FK':          [0.1540, 0.1415],
    'EM':          [0.4899, 0.4793],
    'voting_conf': [0.3409, 0.3494],
    'logprob':     [0.0036, 0.0000],
}
for j, sig in enumerate(signals):
    cond_rho[3, j] = np.mean(scierc_re_2seed_cond[sig])

# Plot heatmap
fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.4), gridspec_kw={'wspace': 0.08})

for ax_idx, (data, title) in enumerate([(full_rho, 'Full set'), (cond_rho, 'Conditional set')]):
    ax = axes[ax_idx]
    vmin, vmax = 0.05, 0.55
    im = ax.imshow(data, cmap='RdYlGn', aspect='auto', vmin=vmin, vmax=vmax)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data[i, j]
            color = 'white' if val < 0.2 or val > 0.45 else 'black'
            ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=7.5, color=color, fontweight='medium')

    ax.set_xticks(range(len(signal_labels)))
    ax.set_xticklabels(signal_labels)
    ax.set_yticks(range(len(configs)))
    if ax_idx == 0:
        ax.set_yticklabels(configs, fontsize=7.5)
    else:
        ax.set_yticklabels([])
    ax.set_title(title, fontsize=9, fontweight='bold', pad=4)
    ax.tick_params(length=2, pad=2)

cbar = fig.colorbar(im, ax=axes, shrink=0.85, pad=0.02, label='Spearman ρ')
cbar.ax.tick_params(labelsize=7)
cbar.set_label('Spearman ρ', fontsize=8)

fig.savefig(FIG_DIR / 'fig_signal_heatmap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_signal_heatmap.png', format='png')
plt.close(fig)
print("✓ fig_signal_heatmap saved")

# ── Figure 2: Correlation-Selection Gap ───────────────────────────────────

# NER data from exp016 selection comparison
ner_sel = sel_exp016['ner']['summary']
re_sel = sel_exp016['re']['summary']

# Also get the exp_006_v2 data for NER with more signals
ner_sel_v2 = sel_exp006.get('scierc_ner_s42', {}).get('signals', {})
re_sel_v2 = sel_exp006.get('scierc_re', {}).get('signals', {})

# NER correlation rho (from exp_015_v2 seed42 N=16)
ner_full_rho_per_sig = {}
for sig in signals:
    ner_full_rho_per_sig[sig] = extract_rho(scierc_ner_s42, sig)

# RE correlation rho
re_full_rho_per_sig = {}
for sig in signals:
    re_full_rho_per_sig[sig] = extract_rho(scierc_re_s42, sig)

# Selection F1 delta vs greedy
ner_greedy = ner_sel['greedy']
re_greedy = re_sel['greedy']

# NER selection: from exp016 + exp_006_v2
ner_sel_f1 = {
    'SJ': ner_sel.get('sj_best', ner_sel_v2.get('SJ', {}).get('mean_f1', ner_greedy)),
    'FK': ner_sel_v2.get('FK', {}).get('mean_f1', ner_greedy),
    'EM': ner_sel_v2.get('EM', {}).get('mean_f1', ner_greedy),
    'voting_conf': ner_sel.get('voting_conf_best', ner_sel_v2.get('voting_conf', {}).get('mean_f1', ner_greedy)),
    'logprob': ner_sel.get('logprob_best', ner_sel_v2.get('logprob', {}).get('mean_f1', ner_greedy)),
}

re_sel_f1 = {
    'SJ': re_sel.get('sj_best', re_sel_v2.get('SJ', {}).get('mean_f1', re_greedy)),
    'FK': re_sel_v2.get('FK', {}).get('mean_f1', re_greedy),
    'EM': re_sel_v2.get('EM', {}).get('mean_f1', re_greedy),
    'voting_conf': re_sel.get('voting_conf_best', re_sel_v2.get('voting_conf', {}).get('mean_f1', re_greedy)),
    'logprob': re_sel.get('logprob_best', re_sel_v2.get('logprob', {}).get('mean_f1', re_greedy)),
}

fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'wspace': 0.45})

for panel_idx, (task_label, rho_dict, sel_dict, greedy_val, oracle_val) in enumerate([
    ('NER (SciERC)', ner_full_rho_per_sig, ner_sel_f1, ner_greedy, ner_sel['oracle']),
    ('RE (SciERC)', re_full_rho_per_sig, re_sel_f1, re_greedy, re_sel['oracle']),
]):
    ax = axes[panel_idx]
    ax2 = ax.twinx()

    x = np.arange(len(signals))
    width = 0.45

    rho_vals = [rho_dict[s] for s in signals]
    delta_f1 = [(sel_dict[s] - greedy_val) * 100 for s in signals]

    bars = ax.bar(x, rho_vals, width, color='#4c72b0', alpha=0.75, edgecolor='#3b5998', linewidth=0.5, label='Spearman ρ', zorder=2)

    line = ax2.plot(x, delta_f1, 'D-', color='#c44e52', markersize=5, linewidth=1.5, label='ΔF1 vs greedy', zorder=3)
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)

    # Oracle gap as text annotation (not line, to avoid scale compression)
    oracle_delta = (oracle_val - greedy_val) * 100
    ax2.annotate(f'oracle: +{oracle_delta:.1f}pp', xy=(0.98, 0.95), xycoords='axes fraction',
                fontsize=6.5, color='#2ca02c', ha='right', va='top',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))

    ax.set_xlabel('')
    ax.set_ylabel('Spearman ρ', color='#4c72b0', fontsize=8)
    ax2.set_ylabel('ΔF1 vs greedy (pp)', color='#c44e52', fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(signal_labels, fontsize=7.5)
    ax.set_ylim(0, 0.55)
    delta_max = max(abs(d) for d in delta_f1) + 1.5
    ax2.set_ylim(-delta_max, delta_max)
    ax.set_title(task_label, fontsize=9, fontweight='bold', pad=4)
    ax.tick_params(axis='y', colors='#4c72b0', labelsize=7)
    ax2.tick_params(axis='y', colors='#c44e52', labelsize=7)

    for xi, d in zip(x, delta_f1):
        offset_y = 7 if d >= 0 else -12
        ax2.annotate(f'{d:+.1f}', xy=(xi, d), xytext=(0, offset_y), textcoords='offset points',
                    ha='center', fontsize=6.5, color='#c44e52', fontweight='bold')

    if panel_idx == 0:
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=6.5, framealpha=0.85)

fig.savefig(FIG_DIR / 'fig_correlation_selection_gap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_correlation_selection_gap.png', format='png')
plt.close(fig)
print("✓ fig_correlation_selection_gap saved")

# ── Figure 3: Temperature Robustness ─────────────────────────────────────

ner_temp = temp_data['results']['ner']['full']
re_temp = temp_data['results']['re']['full']
ner_boot = temp_data['results']['ner'].get('bootstrap', {})
re_boot = temp_data['results']['re'].get('bootstrap', {})

sig_map_temp = {
    'SJ': 'soft_jaccard', 'FK': 'fleiss_kappa', 'EM': 'exact_match',
    'voting_conf': 'voting_conf', 'logprob': 'mean_logprob'
}

fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'wspace': 0.3})

for panel_idx, (task_label, task_temp, task_boot) in enumerate([
    ('NER (SciERC)', ner_temp, ner_boot),
    ('RE (SciERC)', re_temp, re_boot),
]):
    ax = axes[panel_idx]
    x = np.arange(len(signals))
    width = 0.28

    t07_vals = []
    t10_vals = []
    deltas = []

    for sig in signals:
        k = sig_map_temp[sig]
        if k in task_temp:
            entry = task_temp[k]
            t07 = entry.get('T07', {}).get('rho', float('nan'))
            t10 = entry.get('T10', {}).get('rho', float('nan'))
            if t07 is None or (isinstance(t07, float) and np.isnan(t07)):
                t07 = float('nan')
            if t10 is None or (isinstance(t10, float) and np.isnan(t10)):
                t10 = float('nan')
            t07_vals.append(t07)
            t10_vals.append(t10)
            if not np.isnan(t07) and not np.isnan(t10):
                deltas.append(t07 - t10)
            else:
                deltas.append(float('nan'))
        else:
            t07_vals.append(float('nan'))
            t10_vals.append(float('nan'))
            deltas.append(float('nan'))

    t07_arr = np.array(t07_vals)
    t10_arr = np.array(t10_vals)
    valid_mask = ~(np.isnan(t07_arr) | np.isnan(t10_arr))

    bars_07 = ax.bar(x[valid_mask] - width/2, t07_arr[valid_mask], width,
                     color='#4c72b0', alpha=0.85, label='T = 0.7', edgecolor='white', linewidth=0.3)
    bars_10 = ax.bar(x[valid_mask] + width/2, t10_arr[valid_mask], width,
                     color='#dd8452', alpha=0.85, label='T = 1.0', edgecolor='white', linewidth=0.3)

    t10_only = ~valid_mask & ~np.isnan(t10_arr)
    if np.any(t10_only):
        ax.bar(x[t10_only], t10_arr[t10_only], width,
               color='#dd8452', alpha=0.85, edgecolor='white', linewidth=0.3)
        for idx in np.where(t10_only)[0]:
            ax.annotate('T=0.7 n/a', xy=(x[idx], 0.01), fontsize=5, color='gray', ha='center')

    # Delta annotations above bars
    for xi, d, v07, v10 in zip(x, deltas, t07_vals, t10_vals):
        if not np.isnan(d):
            y_pos = max(v07, v10) + 0.02
            color = '#2ca02c' if abs(d) < 0.03 else '#d62728'
            ax.annotate(f'Δ{d:+.3f}', xy=(xi, y_pos),
                       ha='center', fontsize=5.5, color=color, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(signal_labels, fontsize=7.5)
    ax.set_ylabel('Spearman ρ', fontsize=8)
    ax.set_title(task_label, fontsize=9, fontweight='bold', pad=4)
    y_lo = min(0, min(v for v in t07_vals + t10_vals if not np.isnan(v))) - 0.05
    ax.set_ylim(y_lo, 0.62)
    ax.axhline(y=0, color='gray', linewidth=0.3, alpha=0.5)
    ax.legend(loc='upper left', fontsize=6.5, framealpha=0.85)
    ax.tick_params(labelsize=7)

fig.savefig(FIG_DIR / 'fig_temperature_robustness.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_temperature_robustness.png', format='png')
plt.close(fig)
print("✓ fig_temperature_robustness saved")

# ── Print summary ─────────────────────────────────────────────────────────
print("\n=== Data Summary ===")
print(f"Heatmap full rho:\n{full_rho}")
print(f"\nHeatmap cond rho:\n{cond_rho}")
print(f"\nNER greedy={ner_greedy:.4f}, oracle={ner_sel['oracle']:.4f}")
print(f"RE greedy={re_greedy:.4f}, oracle={re_sel['oracle']:.4f}")
print(f"\nNER selection delta: {[f'{(ner_sel_f1[s]-ner_greedy)*100:+.2f}pp' for s in signals]}")
print(f"RE selection delta: {[f'{(re_sel_f1[s]-re_greedy)*100:+.2f}pp' for s in signals]}")
print(f"\nAll figures saved to {FIG_DIR}")
