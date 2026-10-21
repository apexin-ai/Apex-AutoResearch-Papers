"""Generate diagnostic plots for §4 empirical validation.

Data source: HumAID (K=10) ONLY — real LLM confusion matrices from
plan_006_asv_empirical.py, loaded directly from asv_empirical_results.json.

Outputs:
  fig5_f1_vs_bias.pdf / .png  — F1 vs downstream bias scatter (HumAID only)
  fig6_asv_heatmap.pdf / .png — ASV magnitude by topology (HumAID only)
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# ── Unified academic style (consistent across all paper figures) ─────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
})

# ── Unified paper palette (deep, saturated) ──────────────────────────────
TOPO_COLORS = {
    'confounding': '#1B4F72',
    'mediation':   '#117A65',
    'collider':    '#1A5276',
    'exposure':    '#C0392B',
    'mbias':       '#2E4053',
    'iv':          '#922B21',
    'frontdoor':   '#6C3483',
}
TOPO_MARKERS = {
    'confounding': 'o', 'mediation': 's', 'collider': '^',
    'exposure': 'D', 'mbias': 'v', 'iv': 'X', 'frontdoor': 'P',
}
TOPO_LABELS = {
    'confounding': 'Confounding', 'mediation': 'Mediation',
    'collider': 'Collider', 'exposure': 'Exposure',
    'mbias': 'M-bias', 'iv': 'IV', 'frontdoor': 'Front-door',
}
C_TEXT = '#1C2833'
C_TEXT_SEC = '#566573'
C_RULE = '#D5D8DC'
C_ROW_ALT = '#f5f6f8'

# ── Data loading ─────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SCRIPT_DIR, '../../artifacts/plan006/asv_empirical_results.json')

with open(JSON_PATH) as f:
    data = json.load(f)

TOPOS = ['confounding', 'mediation', 'collider', 'exposure', 'M-bias', 'IV', 'front-door']
TOPO_KEYS = ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']

zero_configs = {(e['model'], e['prompt'])
                for e in data['f1_vs_bias'] if e['macro_f1'] == 0}

def is_valid(e):
    return (e['model'], e['prompt']) not in zero_configs


# ══════════════════════════════════════════════════════════════════════════
# Figure 5: F1 vs Downstream Bias (Okabe-Ito palette)
# ══════════════════════════════════════════════════════════════════════════

entries = [e for e in data['f1_vs_bias'] if is_valid(e) and e['macro_f1'] > 0]
f1_all = [e['macro_f1'] for e in entries]

fig, ax = plt.subplots(1, 1, figsize=(7, 3.3))

# Subtle background regime bands
ax.axhspan(0, 10, color='#154360', alpha=0.035, zorder=0)
ax.axhspan(10, 50, color='#922B21', alpha=0.025, zorder=0)

for tk in TOPO_KEYS:
    pts = [e for e in entries if e['topology'] == tk]
    if not pts:
        continue
    f1s = np.array([e['macro_f1'] for e in pts])
    biases = np.array([abs(e['bias_pct']) * 100 for e in pts])
    ax.scatter(f1s, biases, c=TOPO_COLORS[tk],
               marker=TOPO_MARKERS[tk], s=48, alpha=0.85, linewidths=0.7,
               edgecolors='white', label=TOPO_LABELS[tk], zorder=3)

# 10% bias threshold
ax.axhline(10, color='#922B21', ls='--', lw=0.9, alpha=0.45, zorder=2)
x_mid = (min(f1_all) + max(f1_all)) / 2
t = ax.text(x_mid, 11.2, '10% bias threshold', ha='center', va='bottom',
            fontsize=7.5, color='#922B21', alpha=0.65, fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Annotate IV max
iv_pts = [e for e in entries if e['topology'] == 'iv']
max_iv = max(iv_pts, key=lambda e: abs(e['bias_pct']))
ax.annotate(f'IV: {abs(max_iv["bias_pct"])*100:.1f}% bias at F1={max_iv["macro_f1"]:.2f}',
            xy=(max_iv['macro_f1'], abs(max_iv['bias_pct'])*100),
            xytext=(max_iv['macro_f1'] + 0.022, abs(max_iv['bias_pct'])*100 - 5),
            fontsize=7.5, ha='left', color=TOPO_COLORS['iv'],
            arrowprops=dict(arrowstyle='->', color=TOPO_COLORS['iv'], lw=0.8))

ax.set_xlabel('Macro F1')
ax.set_ylabel('|Relative Bias| (%)')
ax.set_xlim(min(f1_all) - 0.01, max(f1_all) + 0.01)
ax.set_ylim(0, 48)
ax.legend(fontsize=7.5, ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.16),
          frameon=False, handletextpad=0.3, columnspacing=1.0)
ax.grid(True, axis='y', alpha=0.12, lw=0.4, zorder=0)
ax.set_title('Topology Determines Bias, Not F1', fontsize=11,
             pad=8, fontweight='bold', loc='left', color=C_TEXT)

plt.tight_layout()
out_base = os.path.join(SCRIPT_DIR, 'fig5_f1_vs_bias')
for ext in ['pdf', 'png']:
    fig.savefig(f'{out_base}.{ext}', dpi=300, bbox_inches='tight')
plt.close()
print("fig5: plotted", len(entries), "data points with Okabe-Ito palette")


# ══════════════════════════════════════════════════════════════════════════
# Figure 6: ASV Magnitude by Topology (forest-plot style, matching fig3)
# ══════════════════════════════════════════════════════════════════════════

t1t2 = [e for e in data['type1_type2'] if is_valid(e)]

asv_ranges = {}
asv_unsafe = {}
for tk in TOPO_KEYS:
    topo_entries = [e for e in t1t2 if e['topology'] == tk]
    magnitudes = [e['magnitude_asv'] for e in topo_entries
                  if e['magnitude_asv'] is not None]
    unsafe_count = sum(1 for e in topo_entries if not e['asv_safe'])
    total_count = len(topo_entries)
    asv_unsafe[tk] = (unsafe_count, total_count)
    if magnitudes and unsafe_count > 0:
        asv_ranges[tk] = (min(magnitudes), max(magnitudes))
    else:
        asv_ranges[tk] = None

fig = plt.figure(figsize=(7.0, 3.2))
gs = fig.add_gridspec(1, 2, width_ratios=[3, 1.2], wspace=0.12)
ax_asv = fig.add_subplot(gs[0])
ax_bar = fig.add_subplot(gs[1])

N = len(TOPO_KEYS)
y_pos = np.arange(N)
ROW_H = 0.5

for ax in (ax_asv, ax_bar):
    ax.set_ylim(N - ROW_H, -ROW_H)
    for i in range(N):
        if i % 2 == 0:
            ax.axhspan(i - ROW_H, i + ROW_H, color=C_ROW_ALT, zorder=0, lw=0)

# Fragile zone in left panel
ax_asv.axvspan(0, 0.5, alpha=0.06, color='#922B21', zorder=0)
ax_asv.axvline(0.5, color='#922B21', lw=0.5, ls=':', alpha=0.25, zorder=0)

for i, tk in enumerate(TOPO_KEYS):
    rng = asv_ranges[tk]
    color = TOPO_COLORS[tk]

    if rng is None:
        ax_asv.annotate(
            '', xy=(1.85, i), xytext=(1.2, i),
            arrowprops=dict(arrowstyle='-|>', color='#154360', lw=1.8,
                            mutation_scale=12))
    else:
        lo, hi = rng
        mid = (lo + hi) / 2
        ax_asv.plot([lo, hi], [i, i], color=color, lw=2.5,
                    solid_capstyle='round', zorder=2, alpha=0.55)
        ax_asv.plot(mid, i, 'o', color=color, ms=7, zorder=3,
                    mec='white', mew=1.0)
        ax_asv.plot(lo, i, '|', color=color, ms=5, mew=1.0, zorder=3)
        ax_asv.plot(hi, i, '|', color=color, ms=5, mew=1.0, zorder=3)

ax_asv.set_xlim(-0.02, 2.1)
ax_asv.set_xlabel('Magnitude ASV ($\\delta^*$)', fontsize=9, color=C_TEXT_SEC, labelpad=6)
ax_asv.set_title('ASV Range', fontweight='normal',
                 loc='left', pad=8, fontsize=10, color=C_TEXT)
ax_asv.set_yticks(range(N))
ax_asv.set_yticklabels(TOPOS, fontsize=10, color=C_TEXT)
ax_asv.grid(True, axis='x', alpha=0.10, zorder=0, lw=0.4)
ax_asv.spines['left'].set_visible(False)
ax_asv.spines['bottom'].set_color(C_RULE)
ax_asv.tick_params(axis='y', length=0)
ax_asv.tick_params(axis='x', colors='#888888', labelsize=9)
ax_asv.axvline(1.0, color='grey', ls=':', lw=0.6, alpha=0.4)

# Right panel: % Unsafe (horizontal bars)
unsafe_pcts = [asv_unsafe[tk][0] / asv_unsafe[tk][1] * 100 for tk in TOPO_KEYS]

for i, (tk, pct) in enumerate(zip(TOPO_KEYS, unsafe_pcts)):
    color = TOPO_COLORS[tk] if pct > 0 else '#154360'
    ax_bar.barh(i, pct, color=color, edgecolor='white', linewidth=0.5,
                height=0.55, alpha=0.75, zorder=2)
    if pct >= 80:
        ax_bar.text(pct - 3, i, f'{pct:.0f}%', va='center', ha='right',
                    fontsize=8, color='white', fontweight='bold')

ax_bar.set_xlim(-2, 115)
ax_bar.set_yticks([])
ax_bar.set_xlabel('% Unsafe', fontsize=9, color=C_TEXT_SEC, labelpad=6)
ax_bar.set_title('% Unsafe', fontweight='normal',
                 loc='left', pad=8, fontsize=10, color=C_TEXT)
ax_bar.spines['left'].set_visible(False)
ax_bar.spines['bottom'].set_color(C_RULE)
ax_bar.tick_params(axis='x', colors='#888888', labelsize=9)
ax_bar.grid(True, axis='x', alpha=0.10, zorder=0, lw=0.4)
ax_bar.axvline(50, color='#922B21', lw=0.5, ls=':', alpha=0.25, zorder=0)

fig.subplots_adjust(left=0.12, right=0.97, top=0.86, bottom=0.18, wspace=0.12)
for ext in ['pdf', 'png']:
    fig.savefig(os.path.join(SCRIPT_DIR, f'fig6_asv_heatmap.{ext}'),
                dpi=300, bbox_inches='tight')
plt.close()

print("fig6: ASV ranges and unsafe counts computed from JSON")
for tk in TOPO_KEYS:
    u, t = asv_unsafe[tk]
    rng = asv_ranges[tk]
    rng_str = f'{rng[0]:.4f}--{rng[1]:.4f}' if rng else 'safe'
    print(f"  {tk}: {u}/{t} unsafe ({u/t*100:.1f}%), ASV range: {rng_str}")

print("\nGenerated: fig5_f1_vs_bias.pdf/.png, fig6_asv_heatmap.pdf/.png")
