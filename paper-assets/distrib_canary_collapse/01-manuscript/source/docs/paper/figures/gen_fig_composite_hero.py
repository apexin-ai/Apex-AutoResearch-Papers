#!/usr/bin/env python3
"""Figure 1: Composite hero figure (2×2) — detection landscape overview.
Panels: (a) Phase diagram, (b) Dose-response, (c) Method comparison, (d) Cross-architecture.
Double-column width for EMNLP 2026."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
import numpy as np
import csv
from collections import defaultdict
from pathlib import Path

BASE = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse')
OUT = BASE / 'docs/paper/figures'

# ── Unified style ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 8,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
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

# Unified colors
C_PERMG = '#2166AC'
C_ANNOT = '#B2182B'
C_NAIVE = '#B2182B'
C_DIFF = '#E08214'
C_THRESH = '#6A3D9A'
C_TY = '#1B7837'

# ── Figure: 2×2 double-column ──
fig = plt.figure(figsize=(7.0, 5.8))
gs = fig.add_gridspec(2, 2, hspace=0.45, wspace=0.38,
                      left=0.07, right=0.97, top=0.96, bottom=0.06)

# ============================================================
# Panel (a): Phase Diagram
# ============================================================
ax_a = fig.add_subplot(gs[0, 0])

alphas_pd = [0.45, 0.50, 0.60, 0.75]
Ts_pd = [5, 10, 15, 20, 25]
pd_data = {
    (5, 0.45): 0, (5, 0.50): 0, (5, 0.60): 0, (5, 0.75): 0,
    (10, 0.45): 0, (10, 0.50): 6, (10, 0.60): 0, (10, 0.75): 6,
    (15, 0.45): 6, (15, 0.50): 6, (15, 0.60): 0, (15, 0.75): 6,
    (20, 0.45): 5, (20, 0.50): 6, (20, 0.60): 0, (20, 0.75): 6,
    (25, 0.45): 6, (25, 0.50): 6, (25, 0.60): 5, (25, 0.75): 6,
}

cmap_pd = plt.cm.RdYlBu_r
CELL_PAD = 0.46

for i, T in enumerate(Ts_pd):
    for j, a in enumerate(alphas_pd):
        val = pd_data[(T, a)]
        rate = val / 8.0
        rect = plt.Rectangle(
            (j - CELL_PAD, i - CELL_PAD), CELL_PAD * 2, CELL_PAD * 2,
            facecolor=cmap_pd(rate), edgecolor='white', linewidth=0.8,
            zorder=1, joinstyle='round')
        ax_a.add_patch(rect)
        is_dark = rate >= 0.75 or rate == 0
        txt_color = '#FFFFFF' if is_dark else '#2A2A2A'
        stroke_col = '#00000033' if is_dark else '#FFFFFF33'
        ax_a.text(j, i, f'{val}/8', ha='center', va='center',
                  fontsize=7.5, fontweight='semibold', color=txt_color, zorder=8,
                  path_effects=[pe.withStroke(linewidth=1.2, foreground=stroke_col)])
        if a == 0.60 and val == 0:
            d = 0.26
            diamond = plt.Polygon(
                [(j, i + d), (j + d, i), (j, i - d), (j - d, i)],
                fill=False, edgecolor='#6A3D9A', linewidth=1.2, zorder=6)
            ax_a.add_patch(diamond)
        if T == 25 and a == 0.60:
            ax_a.plot(j + 0.24, i + 0.24, marker='*', markersize=7,
                      color='#D4A843', markeredgecolor='#6B5A30',
                      markeredgewidth=0.4, zorder=7, clip_on=False)

# Theory curve
T_curve = np.linspace(4, 30, 500)
alpha_c_curve = np.clip(130.39 * T_curve ** (-2.083), 0, 1.0)
mask = (alpha_c_curve >= alphas_pd[0] - 0.02) & (alpha_c_curve <= alphas_pd[-1] + 0.02)
x_crv = np.interp(alpha_c_curve, alphas_pd, range(len(alphas_pd)))
y_crv = np.interp(T_curve, Ts_pd, range(len(Ts_pd)))
valid = mask & (x_crv >= -0.5) & (x_crv <= len(alphas_pd) - 0.5)
ax_a.plot(x_crv[valid], y_crv[valid], color='#1A1A1A', linewidth=1.1,
          linestyle='--', zorder=5, dashes=(4, 3))

ax_a.set_xticks(range(len(alphas_pd)))
ax_a.set_xticklabels([f'{a:.2f}' for a in alphas_pd])
ax_a.set_yticks(range(len(Ts_pd)))
ax_a.set_yticklabels([str(T) for T in Ts_pd])
ax_a.set_xlabel(r'Contamination $\alpha$', labelpad=2)
ax_a.set_ylabel(r'Window $T$', labelpad=2)
ax_a.set_xlim(-0.5, len(alphas_pd) - 0.5)
ax_a.set_ylim(-0.5, len(Ts_pd) - 0.5)
ax_a.tick_params(length=0)
for spine in ax_a.spines.values():
    spine.set_visible(False)

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cmap_pd, norm=plt.Normalize(0, 8))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax_a, fraction=0.046, pad=0.06,
                     ticks=[0, 2, 4, 6, 8], aspect=16)
cbar.set_label('Pairs (of 8)', fontsize=6.5, labelpad=4)
cbar.ax.tick_params(labelsize=6, length=1.5)
cbar.outline.set_linewidth(0.3)
cbar.outline.set_edgecolor('#AAAAAA')

# Legend
handles_a = [
    plt.Line2D([], [], color='#1A1A1A', linewidth=1.0, linestyle='--',
               dashes=(4, 3), label=r'$\alpha_c(T)$'),
    plt.Line2D([], [], marker='D', color='#6A3D9A', markersize=3.5,
               linestyle='None', markerfacecolor='none',
               markeredgecolor='#6A3D9A', markeredgewidth=1.0,
               label='Sync-dip'),
    plt.Line2D([], [], marker='*', color='#D4A843', markersize=5.5,
               linestyle='None', markeredgecolor='#6B5A30',
               markeredgewidth=0.3, label='Dissolves'),
]
ax_a.legend(handles=handles_a, loc='upper center',
            bbox_to_anchor=(0.45, -0.12), ncol=3,
            framealpha=0.0, edgecolor='none',
            handlelength=1.5, handletextpad=0.3,
            borderpad=0.15, columnspacing=0.6, fontsize=6)

ax_a.text(-0.08, 1.05, '(a)', transform=ax_a.transAxes,
          fontsize=10, fontweight='bold', va='bottom', ha='left')


# ============================================================
# Panel (b): Dose-Response
# ============================================================
ax_b = fig.add_subplot(gs[0, 1])

data_by_alpha = defaultdict(list)
with open(BASE / 'artifacts/dose_response_d120_compiled.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['category'] == 'alpha_sweep' and row['dataset'] == 'wikitext':
            data_by_alpha[float(row['alpha'])].append(float(row['permg_rate']))

alphas_dr = sorted(data_by_alpha.keys())
means_dr = np.array([np.mean(data_by_alpha[a]) for a in alphas_dr])
stds_dr = np.array([np.std(data_by_alpha[a], ddof=0) for a in alphas_dr])

def sigmoid(a, k, ac, ym):
    return ym / (1.0 + np.exp(-k * (a - ac)))

K_FIT, AC_FIT, YM_FIT = 200.0, 0.483, 0.7518

np.random.seed(42)
N_BOOT = 1000
log_k_mu = np.log(np.sqrt(73.6 * 500))
log_k_sig = (np.log(500) - np.log(73.6)) / (2 * 1.96)
k_samp = np.exp(np.random.normal(log_k_mu, log_k_sig, N_BOOT))
ac_samp = np.random.normal(0.483, (0.558 - 0.425) / (2 * 1.96), N_BOOT)
ym_samp = np.random.normal(0.7518, (0.895 - 0.691) / (2 * 1.96), N_BOOT)

alpha_c_arr = np.linspace(0, 1.0, 300)
curves = np.array([sigmoid(alpha_c_arr, k, ac, ym)
                    for k, ac, ym in zip(k_samp, ac_samp, ym_samp)])
ci_lo = np.clip(np.percentile(curves, 2.5, axis=0), 0, 1)
ci_hi = np.clip(np.percentile(curves, 97.5, axis=0), 0, 1)
fit_y = np.clip(sigmoid(alpha_c_arr, K_FIT, AC_FIT, YM_FIT), 0, 1)

# Regime bands
regimes = [
    (0.0, 0.47, '#F4F6F9', 'Blind'),
    (0.47, 0.55, '#EBF0F7', 'Onset'),
    (0.55, 0.68, '#FDF5EE', 'Dip'),
    (0.68, 1.0, '#F0F5EF', 'Detection'),
]
for x0, x1, col, lab in regimes:
    ax_b.axvspan(x0, x1, color=col, zorder=0)

regime_labels_pos = [(0.23, 'Blind'), (0.51, 'Onset'),
                     (0.615, 'Dip'), (0.84, 'Detection')]
for lx, lab in regime_labels_pos:
    ax_b.text(lx, 1.04, lab, transform=ax_b.get_xaxis_transform(),
              ha='center', va='bottom', fontsize=6, color='#666666',
              fontstyle='italic', clip_on=False)

for xb in (0.47, 0.55, 0.68):
    ax_b.axvline(xb, color='#E0E0E0', ls=':', lw=0.4, zorder=1)

ax_b.fill_between(alpha_c_arr, ci_lo, ci_hi, color=C_PERMG, alpha=0.08,
                   label='95% CI', zorder=2, lw=0)
ax_b.plot(alpha_c_arr, fit_y, color=C_PERMG, lw=1.3,
          label=r'Sigmoid ($\alpha_c{=}0.483$)', zorder=3)
ax_b.axvline(AC_FIT, color=C_PERMG, ls='--', lw=0.6, alpha=0.3, zorder=1)

rng = np.random.default_rng(42)
for a in alphas_dr:
    rates = data_by_alpha[a]
    n = len(rates)
    jit = rng.uniform(-0.008, 0.008, n) if n > 1 else np.zeros(1)
    ax_b.scatter(a + jit, rates, s=7, c='#666666', alpha=0.35, zorder=4, edgecolors='none')

ax_b.errorbar(alphas_dr, means_dr, yerr=stds_dr, fmt='D', ms=2.5,
              color='#1A1A1A', ecolor='#555555', elinewidth=0.6, capsize=1.0,
              capthick=0.5, label=r'Mean $\pm$ SD', zorder=5, markeredgewidth=0)

ax_b.plot(0.45, 0.0, 'o', ms=4, mfc='none', mec=C_ANNOT, mew=0.8, zorder=6)
ax_b.annotate(
    '$p_{\\mathrm{FDR}}$=.059,.091',
    xy=(0.45, 0.02), xycoords='data',
    xytext=(0.18, 0.48), textcoords='data',
    fontsize=5.5, color=C_ANNOT, ha='center', va='center',
    arrowprops=dict(arrowstyle='->', color=C_ANNOT, lw=0.7,
                    connectionstyle='arc3,rad=-0.12'),
    bbox=dict(boxstyle='round,pad=0.15', fc='white', ec=C_ANNOT, lw=0.4, alpha=0.9),
    zorder=7)

ax_b.set_xlabel(r'Contamination $\alpha$', labelpad=2)
ax_b.set_ylabel('PermG detection rate', labelpad=2)
ax_b.set_xlim(-0.02, 1.02)
ax_b.set_ylim(-0.05, 1.08)
ax_b.set_xticks([0, 0.25, 0.50, 0.75, 1.0])

ax_b.legend(loc='upper left', framealpha=0.92, edgecolor='none',
            borderpad=0.15, handlelength=1.0, fontsize=5.5)

ax_b.text(-0.08, 1.05, '(b)', transform=ax_b.transAxes,
          fontsize=10, fontweight='bold', va='bottom', ha='left')


# ============================================================
# Panel (c): Method Comparison
# ============================================================
ax_c = fig.add_subplot(gs[1, 0])

alpha_labels_mc = [r'$\alpha{=}0$', r'$\alpha{=}.25$', r'$\alpha{=}.50$',
                   r'$\alpha{=}.75$', r'$\alpha{=}1$']
methods_mc = ['Naive XCorr', 'Diff. XCorr', r'Thresh. ($3\sigma$)',
              'Perm. Granger', 'Toda–Yam.']
mc_data = {
    'Naive XCorr':            [75,   62.5, 62.5, 0,    0],
    'Diff. XCorr':            [0,    25,   12.5, 0,    0],
    r'Thresh. ($3\sigma$)':   [37.5, 62.5, 100,  100,  25],
    'Perm. Granger':          [0,    0,    75,   75,   75],
    'Toda–Yam.':              [12.5, 37.5, 50,   100,  12.5],
}
mc_colors = {
    'Naive XCorr': C_NAIVE,
    'Diff. XCorr': C_DIFF,
    r'Thresh. ($3\sigma$)': C_THRESH,
    'Perm. Granger': C_PERMG,
    'Toda–Yam.': C_TY,
}

n_groups = len(alpha_labels_mc)
n_methods = len(methods_mc)
bar_width = 0.14
x_mc = np.arange(n_groups)

ax_c.axvspan(-0.45, 0.45, color='#FDEDEC', alpha=0.40, zorder=0)
ax_c.text(0, 106, 'null', ha='center', va='bottom',
          fontsize=4.5, color='#B03A2E', fontstyle='italic', fontweight='bold')
ax_c.axvspan(1.55, 2.45, color='#EBF5FB', alpha=0.30, zorder=0)
ax_c.text(2, 106, 'onset', ha='center', va='bottom',
          fontsize=4.5, color='#1A5276', fontstyle='italic', fontweight='bold')
ax_c.axhline(y=5, color='#B03A2E', linewidth=0.4, linestyle='--', alpha=0.40, zorder=1)

bar_containers = {}
for i, method in enumerate(methods_mc):
    offset = (i - n_methods / 2 + 0.5) * bar_width
    vals = mc_data[method]
    c = mc_colors[method]
    is_hero = method == 'Perm. Granger'
    alpha_val = 1.0 if is_hero else 0.70
    edgecolor = '#222222' if is_hero else 'none'
    linewidth = 0.8 if is_hero else 0
    bars = ax_c.bar(x_mc + offset, vals, bar_width * 0.90,
                    color=c, alpha=alpha_val, label=method,
                    edgecolor=edgecolor, linewidth=linewidth, zorder=2)
    bar_containers[method] = (bars, offset)

hero_bars, hero_offset = bar_containers['Perm. Granger']
hero_vals = mc_data['Perm. Granger']
for j, v in enumerate(hero_vals):
    if v > 0:
        ax_c.text(x_mc[j] + hero_offset, v + 1.5, f'{int(v)}',
                  ha='center', va='bottom', fontsize=4,
                  fontweight='bold', color=C_PERMG)
    else:
        ax_c.text(x_mc[j] + hero_offset, 1.5, '0',
                  ha='center', va='bottom', fontsize=4,
                  fontweight='bold', color=C_PERMG, alpha=0.6)

ax_c.set_xticks(x_mc)
ax_c.set_xticklabels(alpha_labels_mc, fontsize=6.5)
ax_c.set_ylabel('FDR-sig. pairs (%)', labelpad=2)
ax_c.set_ylim(0, 113)
ax_c.set_yticks([0, 25, 50, 75, 100])
ax_c.set_xlim(-0.55, n_groups - 0.45)
ax_c.yaxis.grid(True, alpha=0.15, linewidth=0.4, zorder=0)
ax_c.set_axisbelow(True)

leg_c = ax_c.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
                    frameon=True, framealpha=0.95,
                    edgecolor='#cccccc', ncol=3, handlelength=0.8,
                    handletextpad=0.25, columnspacing=0.5, borderpad=0.15,
                    fontsize=5.5)
leg_c.get_frame().set_linewidth(0.3)

ax_c.text(-0.08, 1.05, '(c)', transform=ax_c.transAxes,
          fontsize=10, fontweight='bold', va='bottom', ha='left')


# ============================================================
# Panel (d): Cross-Architecture Heatmap
# ============================================================
ax_d = fig.add_subplot(gs[1, 1])

ca_rows = []
with open(BASE / 'artifacts/cross_arch_table7.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['PermG_fwd'] and row['note'] not in ('RUNNING', 'RUNNING (~50h)', 'FAILED EXIT_CODE=1'):
            ca_rows.append(row)

def parse_frac(s):
    if not s:
        return np.nan
    num, den = s.split('/')
    return int(num) / int(den)

ca_labels = []
ca_permg = []
ca_k3 = []
for r in ca_rows:
    model = r['model']
    seed = r['seed']
    domain = r['domain']
    prec = r['precision']
    suffix = ''
    if domain == 'C4':
        suffix = ' (C4)'
    elif prec == 'bf16':
        suffix = ' (bf16)'
    short_model = model.replace('Padding-', 'Pad-')
    label = f"{short_model} {seed}{suffix}"
    ca_labels.append(label)
    ca_permg.append(parse_frac(r['PermG_fwd']))
    ca_k3.append(parse_frac(r['K3_3sigma']))

n_ca = len(ca_labels)
y_ca = np.arange(n_ca)
bar_h = 0.32

permg_pct = [v * 100 for v in ca_permg]
k3_pct = [v * 100 for v in ca_k3]
# Highlight non-confirming conditions with lower alpha
permg_alphas = [0.9 if p >= 75 else 0.55 for p in permg_pct]
for i_bar in range(n_ca):
    ax_d.barh(y_ca[i_bar] + bar_h/2, permg_pct[i_bar], bar_h,
              color=C_PERMG, alpha=permg_alphas[i_bar],
              edgecolor='#222222', linewidth=0.4,
              label='PermG fwd' if i_bar == 0 else '_nolegend_')
    ax_d.barh(y_ca[i_bar] - bar_h/2, k3_pct[i_bar], bar_h,
              color='#A6CEE3', alpha=0.75,
              label=r'$K{\geq}3$' if i_bar == 0 else '_nolegend_')

for i, (pv, kv) in enumerate(zip(ca_permg, ca_k3)):
    ax_d.text(pv * 100 + 1.2, i + bar_h/2, f'{int(pv*8)}/8',
              va='center', ha='left', fontsize=5, color=C_PERMG, fontweight='bold')
    ax_d.text(kv * 100 + 1.2, i - bar_h/2, f'{int(kv*8)}/8',
              va='center', ha='left', fontsize=5, color='#6BAED6')

ax_d.set_yticks(y_ca)
ax_d.set_yticklabels(ca_labels, fontsize=6)
ax_d.set_xlabel('Detection rate (%)', labelpad=2)
ax_d.set_xlim(0, 115)
ax_d.set_xticks([0, 25, 50, 75, 100])
ax_d.invert_yaxis()
ax_d.xaxis.grid(True, alpha=0.12, linewidth=0.3)
ax_d.set_axisbelow(True)
ax_d.axvline(x=75, color=C_PERMG, linewidth=0.5, linestyle=':', alpha=0.30)
ax_d.axvspan(75, 115, color='#EBF5FB', alpha=0.15, zorder=0)

leg_d = ax_d.legend(loc='lower right', frameon=True, framealpha=0.9,
                    edgecolor='#cccccc', borderpad=0.2, fontsize=5.5)
leg_d.get_frame().set_linewidth(0.3)

ax_d.text(-0.08, 1.05, '(d)', transform=ax_d.transAxes,
          fontsize=10, fontweight='bold', va='bottom', ha='left')


# ── Save ──
for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_composite_hero.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/fig_composite_hero.pdf + .png')
