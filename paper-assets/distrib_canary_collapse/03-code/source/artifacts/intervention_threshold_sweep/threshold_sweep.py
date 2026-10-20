import json
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).parent

# ── Data (extracted from server) ──────────────────────────────────────────────

alpha_sweep = {
    0.00: [3.2342, 2.9906, 3.0210, 3.0143, 3.0407, 3.0335, 3.0566, 3.0500, 3.0663, 3.0427, 3.0693],
    0.10: [3.2342, 2.9861, 3.0126, 3.0295, 3.0241, 3.0352, 3.0489, 3.0548, 3.0515, 3.0684, 3.0858],
    0.25: [3.2342, 2.9830, 3.0154, 3.0395, 3.0511, 3.0340, 3.0488, 3.0668, 3.0631, 3.1037, 3.0794],
    0.50: [3.2342, 2.5131, 2.5110, 2.5816, 2.5883, 2.5856, 2.6080, 2.6564, 2.6603, 2.6724, 2.7075],
    0.75: [3.2342, 2.1738, 2.1055, 2.0913, 2.1229, 2.1407, 2.1617, 2.1652, 2.2023, 2.2407, 2.2830],
    1.00: [3.2342, 1.9099, 1.4611, 1.3379, 1.2805, 1.2912, 1.2253, 1.2369, 1.2482, 1.2390, 1.2269],
}

alpha_ppl = {
    0.00: [26.949, 19.299, 20.014, 20.262, 20.524, 20.922, 20.991, 20.955, 20.863, 21.015, 21.108],
    0.10: [26.949, 19.127, 20.035, 20.363, 20.549, 20.967, 20.818, 21.210, 21.515, 21.658, 21.845],
    0.25: [26.949, 19.386, 20.367, 20.751, 21.142, 21.296, 21.478, 21.882, 21.901, 22.254, 22.074],
    0.50: [26.949, 23.363, 26.686, 27.597, 28.710, 29.733, 29.887, 30.060, 31.024, 31.448, 31.462],
    0.75: [26.949, 31.799, 44.310, 50.528, 55.511, 61.037, 64.164, 68.920, 73.856, 75.961, 77.697],
    1.00: [26.949, 57.415, 162.151, 279.174, 394.018, 508.854, 598.726, 722.577, 814.682, 934.959, 1017.811],
}

interv_exps = {
    'pred_a075_s42': {
        'mode': 'predictive', 'alpha': 0.75, 'trigger_gen': 1,
        'entropy': [3.2342, 2.2120, 3.0489, 3.0526, 3.0669, 3.0467, 3.0512, 3.0553, 3.0575, 3.0325, 3.0487],
        'ppl': [26.949, 32.629, 20.797, 20.744, 20.958, 20.768, 20.930, 20.994, 20.668, 20.954, 20.815],
    },
    'pred_a100_s43': {
        'mode': 'predictive', 'alpha': 1.0, 'trigger_gen': 1,
        'entropy': [3.2574, 2.5233, 2.9029, 2.8767, 2.8631, 2.8494, 2.8393, 2.8455, 2.8258, 2.8254, 2.8169],
        'ppl': [27.681, 24.650, 17.490, 17.226, 16.943, 16.760, 16.682, 16.591, 16.567, 16.603, 16.683],
    },
    'react_a100_s43_fp32': {
        'mode': 'reactive', 'alpha': 1.0, 'trigger_gen': 2,
        'entropy': [3.2342, 1.7930, 1.4034, 3.1312, 3.0846, 3.0641, 3.0808, 3.0957, 3.0648, 3.0791, 3.0876],
        'ppl': [26.949, 55.589, 158.225, 21.976, 21.551, 21.215, 21.669, 21.316, 21.462, 21.357, 21.387],
    },
    'react_a100_s43_bf16': {
        'mode': 'reactive', 'alpha': 1.0, 'trigger_gen': 2,
        'entropy': [3.2574, 2.5202, 2.3497, 2.8868, 2.8636, 2.8433, 2.8452, 2.8402, 2.8235, 2.8230, 2.8169],
        'ppl': [27.681, 24.627, 38.709, 17.378, 16.998, 16.719, 16.735, 16.618, 16.562, 16.507, 16.515],
    },
    'pred_14b_s42': {
        'mode': 'predictive', 'alpha': 1.0, 'trigger_gen': 1,
        'entropy': [2.9457, 1.4177, 2.8922, 2.8796, 2.8778, 2.8385, 2.8397, 2.8418, 2.8578, 2.8292, 2.8318],
        'ppl': [19.683, 65.368, 17.441, 17.566, 17.639, 17.604, 17.443, 17.631, 17.546, 17.718, 17.603],
    },
}

THRESHOLDS = [5, 10, 15, 20, 25, 30, 40, 50]

# ── Analysis ──────────────────────────────────────────────────────────────────

def compute_entropy_drops(entropy_seq):
    e0 = entropy_seq[0]
    return [(e0 - e) / e0 * 100 for e in entropy_seq]

def find_trigger_gen(drops, threshold):
    for gen, d in enumerate(drops):
        if gen == 0:
            continue
        if d >= threshold:
            return gen
    return None

# 1. Threshold sensitivity on counterfactual alpha sweep
rows = []
for alpha, entropy in sorted(alpha_sweep.items()):
    drops = compute_entropy_drops(entropy)
    ppl = alpha_ppl[alpha]
    for th in THRESHOLDS:
        tg = find_trigger_gen(drops, th)
        max_drop_pct = max(drops[1:])
        if tg is not None:
            ppl_at_trigger = ppl[tg]
            ppl_peak_after = max(ppl[tg:]) if tg < len(ppl) else ppl[-1]
        else:
            ppl_at_trigger = None
            ppl_peak_after = None
        rows.append({
            'alpha': alpha,
            'threshold_pct': th,
            'trigger_gen': tg if tg is not None else 'no_trigger',
            'max_entropy_drop_pct': round(max_drop_pct, 2),
            'ppl_at_trigger': round(ppl_at_trigger, 2) if ppl_at_trigger else None,
            'ppl_peak_no_interv': round(ppl[-1], 2),
        })

# 2. Intervention experiments: ppl reduction vs counterfactual
interv_rows = []
for name, exp in interv_exps.items():
    alpha = exp['alpha']
    tg = exp['trigger_gen']
    cf_ppl = alpha_ppl.get(alpha, alpha_ppl[1.00])
    for gen in range(tg + 1, len(exp['ppl'])):
        ppl_interv = exp['ppl'][gen]
        ppl_cf = cf_ppl[gen]
        reduction = (ppl_cf - ppl_interv) / ppl_cf * 100
        interv_rows.append({
            'experiment': name, 'mode': exp['mode'], 'alpha': alpha,
            'trigger_gen': tg, 'gen': gen,
            'ppl_interv': round(ppl_interv, 2),
            'ppl_counterfactual': round(ppl_cf, 2),
            'ppl_reduction_pct': round(reduction, 2),
        })

peak_reductions = {}
for name in interv_exps:
    exp_rows = [r for r in interv_rows if r['experiment'] == name]
    if exp_rows:
        peak_reductions[name] = max(exp_rows, key=lambda r: r['ppl_reduction_pct'])

# 3. False alarm analysis on null (α=0.0)
null_drops = compute_entropy_drops(alpha_sweep[0.00])
false_alarms = {}
for th in THRESHOLDS:
    tg = find_trigger_gen(null_drops, th)
    false_alarms[th] = tg is not None

null_max_drop = max(null_drops[1:])

# ── CSV Export ────────────────────────────────────────────────────────────────

with open(OUT / 'threshold_sensitivity.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

with open(OUT / 'intervention_ppl_reduction.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=interv_rows[0].keys())
    w.writeheader()
    w.writerows(interv_rows)

# ── Plotting ──────────────────────────────────────────────────────────────────

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'legend.fontsize': 8.5,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

blues = plt.cm.Blues(np.linspace(0.3, 0.95, 6))
reds = plt.cm.Reds(np.linspace(0.35, 0.85, 3))

# ── Figure 1: Threshold vs Trigger Generation ────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 3.8))

signal_alphas = [0.10, 0.25, 0.50, 0.75, 1.00]
colors_map = {0.10: blues[1], 0.25: blues[2], 0.50: blues[3], 0.75: blues[4], 1.00: blues[5]}
markers = {0.10: 'v', 0.25: 's', 0.50: 'D', 0.75: 'o', 1.00: '^'}

for alpha in signal_alphas:
    drops = compute_entropy_drops(alpha_sweep[alpha])
    tgens = []
    ths_plot = []
    no_trigger_start = None
    for th in THRESHOLDS:
        tg = find_trigger_gen(drops, th)
        if tg is not None:
            tgens.append(tg)
            ths_plot.append(th)
        elif no_trigger_start is None:
            no_trigger_start = th
    if ths_plot:
        ax.plot(ths_plot, tgens, marker=markers[alpha], color=colors_map[alpha],
                label=f'α={alpha:.2f}', linewidth=1.5, markersize=5, zorder=3)
    max_d = max(drops[1:])
    if max_d < max(THRESHOLDS):
        ax.axvline(x=max_d, color=colors_map[alpha], linestyle=':', alpha=0.35, linewidth=0.8)

ax.axhspan(-0.5, 0.5, color='0.95', zorder=0)
ax.set_xlabel('Entropy Drop Threshold (%)')
ax.set_ylabel('Trigger Generation')
ax.set_xticks(THRESHOLDS)
ax.set_yticks(range(0, 6))
ax.set_ylim(-0.3, 5.3)
ax.legend(title='Contamination α', loc='upper left', frameon=True, fancybox=False, edgecolor='0.7')
ax.set_title('Intervention Trigger Timing vs. Threshold')
ax.grid(axis='y', alpha=0.3, linewidth=0.5)

fig.savefig(OUT / 'fig_threshold_timing.pdf')
fig.savefig(OUT / 'fig_threshold_timing.png')
plt.close(fig)

# ── Figure 2: PPL Trajectories — Intervention vs Counterfactual ──────────────
fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=False)

gens = list(range(11))

# Panel A: α=0.75
ax = axes[0]
ax.plot(gens, alpha_ppl[0.75], 'o--', color='0.5', markersize=4, linewidth=1.2,
        label='Counterfactual (α=0.75, no interv.)')
exp = interv_exps['pred_a075_s42']
ax.plot(gens, exp['ppl'], 's-', color=blues[4], markersize=4, linewidth=1.5,
        label=f'Predictive interv. (trigger gen {exp["trigger_gen"]})')
ax.axvline(x=exp['trigger_gen'], color=blues[4], linestyle=':', alpha=0.5)
ax.fill_between(gens, exp['ppl'], alpha_ppl[0.75], alpha=0.12, color=blues[3])
ax.set_xlabel('Generation')
ax.set_ylabel('Perplexity')
ax.set_title('α = 0.75')
ax.legend(fontsize=7, loc='upper left', frameon=True, fancybox=False, edgecolor='0.8')
ax.set_xticks(range(0, 11, 2))
ax.grid(alpha=0.2, linewidth=0.5)

# Panel B: α=1.00
ax = axes[1]
ax.plot(gens, alpha_ppl[1.00], 'o--', color='0.5', markersize=4, linewidth=1.2,
        label='Counterfactual (α=1.0, no interv.)')
for name, c, m, ls in [
    ('pred_a100_s43', blues[4], 's', '-'),
    ('react_a100_s43_fp32', reds[1], 'D', '--'),
]:
    exp = interv_exps[name]
    lab = f'{exp["mode"].capitalize()} interv. (trigger gen {exp["trigger_gen"]})'
    ax.plot(gens, exp['ppl'], marker=m, linestyle=ls, color=c, markersize=4, linewidth=1.5,
            label=lab)
ax.set_xlabel('Generation')
ax.set_title('α = 1.00')
ax.legend(fontsize=6.5, loc='upper left', frameon=True, fancybox=False, edgecolor='0.8')
ax.set_xticks(range(0, 11, 2))
ax.grid(alpha=0.2, linewidth=0.5)

fig.suptitle('PPL Recovery: Intervention vs. Counterfactual', fontsize=12, y=1.02)
fig.tight_layout()
fig.savefig(OUT / 'fig_threshold_ppl.pdf')
fig.savefig(OUT / 'fig_threshold_ppl.png')
plt.close(fig)

# ── Figure 3: ROC-like curve ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 4.5))

signal_alphas_all = [0.10, 0.25, 0.50, 0.75, 1.00]
extended_thresholds = list(range(1, 65))

det_rates = []
fa_rates = []

null_drops_ext = compute_entropy_drops(alpha_sweep[0.00])

for th in extended_thresholds:
    detected = sum(1 for a in signal_alphas_all
                   if find_trigger_gen(compute_entropy_drops(alpha_sweep[a]), th) is not None)
    dr = detected / len(signal_alphas_all)
    fa = 1 if find_trigger_gen(null_drops_ext, th) is not None else 0
    det_rates.append(dr)
    fa_rates.append(fa)

ax.plot(fa_rates, det_rates, '-', color='0.6', linewidth=1, zorder=1)
ax.plot([0, 1], [0, 1], 'k--', alpha=0.25, linewidth=0.8, label='Random')

# Mark key thresholds with non-overlapping annotations
th_positions = {
    5:  (0.08, 0.06),   # fa=1, dr=1.0
    10: (-0.06, 0.04),   # fa=0, dr=0.6
    15: (-0.06, 0.05),
    20: (-0.06, 0.05),
    25: (0.04, -0.06),
    30: (0.04, -0.06),
    40: (0.04, -0.06),
    50: (0.04, -0.06),
}

prev_dr = None
for th in THRESHOLDS:
    idx = extended_thresholds.index(th)
    dr = det_rates[idx]
    fa = fa_rates[idx]
    ax.plot(fa, dr, 'o', color=blues[4], markersize=8, zorder=5)

    dx, dy = th_positions[th]
    if prev_dr == dr and fa == 0:
        dy += 0.03 * (THRESHOLDS.index(th) % 2)
    ax.annotate(f'{th}%', (fa, dr), fontsize=8, color='0.25',
                xytext=(fa + dx, dr + dy), arrowprops=dict(arrowstyle='-', color='0.6', lw=0.5),
                ha='center', va='center')
    prev_dr = dr

ax.fill_between([0, 0], [0, 0.6], alpha=0)
ax.axvspan(-0.05, 0.05, color='#e8f4e8', alpha=0.5, zorder=0, label='Zero false alarms')

ax.set_xlabel('False Alarm Rate')
ax.set_ylabel('Detection Rate')
ax.set_title('Detection–False Alarm Tradeoff\nAcross Entropy-Drop Thresholds')
ax.set_xlim(-0.08, 1.08)
ax.set_ylim(-0.08, 1.08)
ax.set_aspect('equal')
ax.legend(fontsize=8, loc='lower right', frameon=True, fancybox=False, edgecolor='0.8')
ax.grid(alpha=0.15, linewidth=0.5)

# Inset: per-α detection
ax_in = fig.add_axes([0.50, 0.18, 0.38, 0.30])
for i, alpha in enumerate(signal_alphas_all):
    drops = compute_entropy_drops(alpha_sweep[alpha])
    max_d = max(drops[1:])
    ax_in.barh(i, max_d, height=0.6, color=blues[i+1], edgecolor='white', linewidth=0.5)
    ax_in.text(max_d + 1, i, f'{max_d:.0f}%', va='center', fontsize=7, color='0.3')
ax_in.set_yticks(range(len(signal_alphas_all)))
ax_in.set_yticklabels([f'α={a}' for a in signal_alphas_all], fontsize=7)
ax_in.set_xlabel('Max Entropy Drop (%)', fontsize=7)
ax_in.set_title('Detection Ceiling', fontsize=8)
ax_in.set_xlim(0, 70)
ax_in.tick_params(labelsize=6)
ax_in.spines['top'].set_visible(False)
ax_in.spines['right'].set_visible(False)
ax_in.axvline(x=15, color='red', linestyle='--', alpha=0.4, linewidth=0.8)
ax_in.text(16, -0.7, '15% threshold', fontsize=5.5, color='red', alpha=0.6)

fig.savefig(OUT / 'fig_roc_detection.pdf')
fig.savefig(OUT / 'fig_roc_detection.png')
plt.close(fig)

# ── Report ────────────────────────────────────────────────────────────────────

report_lines = []
report_lines.append("# Intervention Threshold Sensitivity Sweep\n")
report_lines.append("## Overview\n")
report_lines.append("Simulated different entropy-drop thresholds (5–50%) on counterfactual α-sweep data")
report_lines.append("to determine optimal intervention trigger timing and false alarm rates.\n")

report_lines.append("## Data Sources\n")
report_lines.append("- **Counterfactual trajectories**: α ∈ {0.00, 0.10, 0.25, 0.50, 0.75, 1.00} (no intervention)")
report_lines.append("- **Intervention experiments**: 3 predictive + 2 reactive runs")
report_lines.append("- **Null baseline**: α=0.00 (pure real data, no contamination)\n")

report_lines.append("## Key Findings\n")

report_lines.append("### 1. Trigger Timing\n")
report_lines.append("| α | Max Entropy Drop (%) | Trigger at 15% | Trigger at 25% | Trigger at 30% |")
report_lines.append("|---|---------------------|----------------|----------------|----------------|")
for alpha in [0.00, 0.10, 0.25, 0.50, 0.75, 1.00]:
    drops = compute_entropy_drops(alpha_sweep[alpha])
    max_d = max(drops[1:])
    t15 = find_trigger_gen(drops, 15)
    t25 = find_trigger_gen(drops, 25)
    t30 = find_trigger_gen(drops, 30)
    report_lines.append(f"| {alpha:.2f} | {max_d:.1f} | {t15 if t15 else '—'} | {t25 if t25 else '—'} | {t30 if t30 else '—'} |")

report_lines.append("")
report_lines.append("### 2. False Alarm Analysis (α=0.00)\n")
report_lines.append(f"- Max entropy drop on null: **{null_max_drop:.1f}%**")

fa_thresh = min(th for th in THRESHOLDS if not false_alarms[th]) if any(not v for v in false_alarms.values()) else None
fa_trigger_ths = [th for th in THRESHOLDS if false_alarms[th]]

if fa_trigger_ths:
    report_lines.append(f"- **Threshold = {fa_trigger_ths[0]}% triggers false alarm** on null (null drop = {null_max_drop:.1f}%)")
    report_lines.append(f"- **All thresholds ≥ {fa_thresh}% produce zero false alarms**\n")
else:
    report_lines.append(f"- **All tested thresholds produce zero false alarms** on null data\n")

report_lines.append("### 3. Detection Boundaries\n")
for alpha in signal_alphas_all:
    drops = compute_entropy_drops(alpha_sweep[alpha])
    max_d = max(drops[1:])
    report_lines.append(f"- **α = {alpha:.2f}**: max drop {max_d:.1f}% → detectable at threshold ≤ {int(max_d)}%")
report_lines.append("")

report_lines.append("### 4. PPL Recovery from Intervention\n")
for name, pr in peak_reductions.items():
    report_lines.append(f"- **{name}**: peak PPL reduction = {pr['ppl_reduction_pct']:.1f}% at gen {pr['gen']} "
                       f"(interv={pr['ppl_interv']:.1f} vs cf={pr['ppl_counterfactual']:.1f})")
report_lines.append("")

report_lines.append("### 5. Recommended Operating Point\n")
report_lines.append("- **Threshold = 15%**: catches α ≥ 0.50 at gen 1, zero false alarms on null")
report_lines.append("- **Threshold = 10%**: catches α ≥ 0.50 at gen 1, zero false alarms (same detection as 15%)")
report_lines.append("- **Threshold = 25%**: misses α = 0.50, catches α ≥ 0.75 (most conservative)")
report_lines.append("- **Threshold = 5%**: catches α ≥ 0.10 but triggers false alarm on null — not recommended\n")

report_lines.append("## Artifacts\n")
report_lines.append("- `threshold_sensitivity.csv` — trigger gen × threshold × α")
report_lines.append("- `intervention_ppl_reduction.csv` — PPL reduction per gen per experiment")
report_lines.append("- `fig_threshold_timing.pdf` — trigger gen vs threshold")
report_lines.append("- `fig_threshold_ppl.pdf` — PPL trajectories: intervention vs counterfactual")
report_lines.append("- `fig_roc_detection.pdf` — detection–false alarm tradeoff")

with open(OUT / 'report.md', 'w') as f:
    f.write('\n'.join(report_lines) + '\n')

print("Done. Files written:")
for p in sorted(OUT.glob('*')):
    if p.name != Path(__file__).name:
        print(f"  {p.name}")
