"""
Figure 1 (composite): 2×2 panel figure for EMNLP 2026.
  (a) Clean Response Pattern       (b) Contaminated Response Pattern
  (c) Effect-Size Landscape        (d) Dose-Response Trajectory

Designed to publication-level quality: NPG palette, serif fonts, subtle details.
Output: fig_1_composite.{pdf,png}
"""
import matplotlib
matplotlib.use('Agg')

import sys, shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch
from pathlib import Path
from scipy.ndimage import uniform_filter1d

sys.path.insert(0, '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper')
import palette
palette.apply()

PROJ = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam')

WHITE_STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

# ═══════════════════════════════════════════════════════════════════════════════
# DATA: panels (a)+(b) — IRT response patterns
# ═══════════════════════════════════════════════════════════════════════════════
np.random.seed(42)
df = pd.read_csv(PROJ / 'artifacts' / 'psn_irt_params' / 'mmlu_params.csv')
N = 300
df_sorted = df.sort_values('b_difficulty')
indices = np.linspace(0, len(df) - 1, N, dtype=int)
items = df_sorted.iloc[indices].reset_index(drop=True).sort_values('b_difficulty').reset_index(drop=True)

a_param = items['a_discrimination'].values
b_param = items['b_difficulty'].values
c_param = items['c_guessing'].values
d_param = items['d_feasibility'].values

theta = 0.5
p_irt = c_param + (d_param - c_param) / (1 + np.exp(-a_param * (theta - b_param)))

clean = (np.random.random(N) < p_irt).astype(int)

contam = clean.copy()
hard_wrong_idx = np.where((b_param > 0.3) & (contam == 0))[0]
np.random.seed(42)
n_flip = min(45, len(hard_wrong_idx))
flip_hard = np.random.choice(hard_wrong_idx, n_flip, replace=False)
contam[flip_hard] = 1

memorized = np.zeros(N, dtype=bool)
memorized[flip_hard] = True

def lz_star(resp, a, b, c, d, th):
    pr = np.clip(c + (d - c) / (1 + np.exp(-a * (th - b))), 1e-10, 1 - 1e-10)
    ll = np.sum(resp * np.log(pr) + (1 - resp) * np.log(1 - pr))
    mu = np.sum(pr * np.log(pr) + (1 - pr) * np.log(1 - pr))
    var = np.sum(pr * (1 - pr) * (np.log(pr / (1 - pr)))**2)
    return (ll - mu) / np.sqrt(var)

lz_c = lz_star(clean, a_param, b_param, c_param, d_param, theta)
lz_t = lz_star(contam, a_param, b_param, c_param, d_param, theta)
delta_lz = abs(lz_c - lz_t)
print(f"ℓz* clean={lz_c:.2f}, contam={lz_t:.2f}, |Δℓz*|={delta_lz:.1f}")

p_smooth = uniform_filter1d(p_irt, size=7, mode='nearest')
x_items = np.arange(N)

# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE LAYOUT
# ═══════════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(7.2, 5.8))
gs = GridSpec(2, 2, figure=fig, wspace=0.30, hspace=0.48,
              left=0.08, right=0.97, top=0.96, bottom=0.08)

ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1], sharey=ax_a)
ax_c = fig.add_subplot(gs[1, 0])
ax_d = fig.add_subplot(gs[1, 1])

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: rug ticks
# ═══════════════════════════════════════════════════════════════════════════════
def draw_rug_ticks(ax, positions, y_centers, color, alpha=0.55, lw=0.9, height=0.05):
    y_centers = np.broadcast_to(np.asarray(y_centers, dtype=float), positions.shape)
    segments = [[(float(xi), float(yc - height / 2)),
                 (float(xi), float(yc + height / 2))]
                for xi, yc in zip(positions, y_centers)]
    if not segments:
        return
    lc = LineCollection(segments, colors=color, linewidths=lw, alpha=alpha, zorder=4)
    ax.add_collection(lc)

# ═══════════════════════════════════════════════════════════════════════════════
# PANELS (a) + (b): response patterns
# ═══════════════════════════════════════════════════════════════════════════════
def plot_response_panel(ax, responses, panel_label, subtitle, is_contam=False):
    # Gradient fill under IRT curve (layered for smooth effect)
    for i in range(15):
        frac_lo = i / 15
        frac_hi = (i + 1) / 15
        alpha = 0.07 * (1.0 - frac_lo * 0.9)
        ax.fill_between(x_items, p_smooth * frac_lo, p_smooth * frac_hi,
                        alpha=alpha, color=palette.CURVE, linewidth=0, zorder=1)

    # IRT probability curve
    ax.plot(x_items, p_smooth, color=palette.CURVE, linewidth=1.8, alpha=0.8, zorder=3)

    # Response rug ticks
    correct = responses == 1
    wrong = responses == 0
    np.random.seed(77)
    jitter_1 = np.random.uniform(-0.01, 0.01, N)
    jitter_0 = np.random.uniform(-0.01, 0.01, N)

    if is_contam:
        norm_c = correct & ~memorized
        draw_rug_ticks(ax, x_items[norm_c], 1.0 + jitter_1[norm_c],
                       palette.CURVE, alpha=0.50, lw=0.9)
        draw_rug_ticks(ax, x_items[wrong], 0.0 + jitter_0[wrong],
                       '#CCCCCC', alpha=0.55, lw=0.9)

        # Memorized items: prominent red diamonds
        mem_x = x_items[memorized]
        mem_y = np.ones(memorized.sum()) + jitter_1[memorized]
        ax.scatter(mem_x, mem_y,
                   s=35, color=palette.SIGNAL, alpha=0.92, edgecolors='white',
                   linewidths=0.7, zorder=7, marker='D')

        # Connection lines from memorized items to IRT curve
        for idx in flip_hard:
            ax.plot([x_items[idx], x_items[idx]],
                    [p_smooth[idx], 1.0 + jitter_1[idx]],
                    color=palette.SIGNAL, alpha=0.18, linewidth=0.5,
                    linestyle=(0, (3, 3)), zorder=2)

        # Small legend for memorized items
        ax.scatter([], [], s=25, color=palette.SIGNAL, marker='D',
                   edgecolors='white', linewidths=0.5, label='Memorized (seen)')
        leg = ax.legend(loc='lower right', frameon=True, framealpha=0.95,
                        edgecolor='#E0E0E0', fontsize=6, handletextpad=0.3,
                        borderpad=0.4, bbox_to_anchor=(0.98, 0.15))
        leg.get_frame().set_linewidth(0.3)
    else:
        draw_rug_ticks(ax, x_items[correct], 1.0 + jitter_1[correct],
                       palette.CURVE, alpha=0.50, lw=0.9)
        draw_rug_ticks(ax, x_items[wrong], 0.0 + jitter_0[wrong],
                       '#CCCCCC', alpha=0.55, lw=0.9)

    # Faint horizontal guides at 0 and 1
    ax.axhline(y=0, color='#000000', alpha=0.05, linewidth=0.4, zorder=0)
    ax.axhline(y=1, color='#000000', alpha=0.05, linewidth=0.4, zorder=0)

    # Panel label
    ax.text(0.02, 0.97, panel_label, transform=ax.transAxes,
            fontsize=11, fontweight='bold', va='top', ha='left',
            color=palette.TEXT, zorder=10)
    # Subtitle — positioned above the y=1 rug marks
    ax.text(0.14, 0.97, subtitle, transform=ax.transAxes,
            fontsize=7.5, va='top', ha='left',
            color=palette.ANNOTATION, fontstyle='italic', zorder=10)

    # ℓz* badge box
    if is_contam:
        lz_color = palette.SIGNAL
        bg_color = '#FDF0EE'
        lz_text = f'$|\\Delta\\ell_z^*|$ = {delta_lz:.1f}'
    else:
        lz_color = '#27AE60'
        bg_color = '#F0F7F0'
        lz_text = f'$\\ell_z^*$ = {lz_c:+.1f}'

    ax.text(0.50, -0.22, lz_text, transform=ax.transAxes,
            ha='center', va='top', fontsize=7.5, fontweight='bold',
            color=lz_color,
            bbox=dict(boxstyle='round,pad=0.35', facecolor=bg_color,
                      edgecolor=lz_color, alpha=0.95, linewidth=0.6),
            zorder=8)

    # "Easy → Hard" annotation
    ax.annotate('Easy', xy=(0.03, -0.12), xycoords='axes fraction',
                fontsize=5.5, color='#999999', style='italic')
    ax.annotate('Hard', xy=(0.88, -0.12), xycoords='axes fraction',
                fontsize=5.5, color='#999999', style='italic')
    ax.annotate('', xy=(0.87, -0.10), xytext=(0.12, -0.10),
                xycoords='axes fraction',
                arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.5))

    # Axis styling
    ax.set_xlabel('Items (sorted by difficulty)', labelpad=13, fontsize=7.5)
    ax.set_xlim(-3, N + 2)
    ax.set_ylim(-0.12, 1.14)
    ax.set_yticks([0, 1])
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    palette.style_ax(ax)

np.random.seed(7)
plot_response_panel(ax_a, clean, '(a)', 'Clean model', is_contam=False)
np.random.seed(7)
plot_response_panel(ax_b, contam, '(b)', 'Contaminated model', is_contam=True)

ax_a.set_ylabel('Response', labelpad=4, fontsize=8)
ax_a.set_yticklabels(['0', '1'], fontsize=7)
plt.setp(ax_b.get_yticklabels(), visible=False)

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL (c): effect-size landscape
# ═══════════════════════════════════════════════════════════════════════════════
data_c = {
    '5':  [(67.8, 4.15, 2.74, 9.85, 'Qwen')],
    '15': [(67.8, 5.36, 4.26, 6.46, 'Qwen'),
           (59.4, 2.80, 2.20, 3.40, 'Llama'),
           (52.4, 3.37, 2.69, 4.05, 'Mistral'),
           (89.7, 3.16, 2.01, 9.54, 'ARC-C')],
    '25': [(67.8, 7.44, 5.58, 9.30, 'Qwen'),
           (59.4, 2.56, 2.04, 3.08, 'Llama')],
    '50': [(67.8, 5.08, 2.06, 8.10, 'Qwen'),
           (59.4, 2.30, 2.00, 2.60, 'Llama'),
           (52.4, 4.09, 3.56, 4.62, 'Mistral'),
           (89.7, 5.30, 3.60, 15.20, 'ARC-C')],
}

color_map = {'Qwen': palette.QWEN, 'Llama': palette.LLAMA,
             'Mistral': palette.MISTRAL, 'ARC-C': palette.ARCC}
marker_map = {'5': 'D', '15': '^', '25': 's', '50': 'o'}
size_map = {'5': 65, '15': 75, '25': 65, '50': 72}
Y_MAX_C = 11.0

for level, pts in data_c.items():
    mk = marker_map[level]
    sz = size_map[level]
    for acc, d_val, ci_lo, ci_hi, model in pts:
        col = color_map[model]
        ax_c.errorbar(acc, d_val,
                      yerr=[[max(d_val - ci_lo, 0)],
                            [min(ci_hi - d_val, Y_MAX_C - d_val)]],
                      fmt='none', ecolor=col, capsize=2.5, capthick=0.7,
                      elinewidth=0.9, alpha=0.28, zorder=4)
        ax_c.scatter(acc, d_val, marker=mk, s=sz, color=col,
                     edgecolors='white', linewidths=0.7, zorder=6)

# Marker legend (horizontal, bottom)
for lk, mk, lbl in [('5', 'D', '5%'), ('15', '^', '15%'),
                     ('25', 's', '25%'), ('50', 'o', '50%')]:
    ax_c.scatter([], [], marker=mk, s=40, color='#777777',
                 edgecolors='white', linewidths=0.4, label=lbl)
leg_c = ax_c.legend(loc='upper left', frameon=True, framealpha=0.92,
                    edgecolor='none', facecolor='white',
                    borderpad=0.35, handletextpad=0.25, handlelength=1.0,
                    fontsize=6, ncol=4, columnspacing=0.5)
leg_c.get_frame().set_linewidth(0)

# |d|=0.8 threshold
ax_c.axhline(y=0.8, color=palette.REFERENCE, linestyle=':', linewidth=0.7, zorder=1)
t_thr = ax_c.text(96, 1.1, 'large effect', fontsize=5, color=palette.REFERENCE,
                  style='italic', ha='right')
t_thr.set_path_effects(WHITE_STROKE)

# Inline model labels
for model, xy, xytext, rad in [
    ('Qwen', (67.8, 7.44), (74, 9.8), 0.2),
    ('Llama', (59.4, 2.30), (51.5, 0.8), -0.2),
    ('Mistral', (52.4, 4.09), (46, 5.8), 0.25),
    ('ARC-C', (89.7, 5.30), (94, 8.0), -0.2),
]:
    col = color_map[model]
    t = ax_c.annotate(model, xy=xy, xytext=xytext,
                      fontsize=6.5, color=col, fontweight='bold',
                      arrowprops=dict(arrowstyle='-', color=col,
                                      lw=0.5, alpha=0.5,
                                      connectionstyle=f'arc3,rad={rad}'))
    t.set_path_effects(WHITE_STROKE)

# Mechanism annotations
t1 = ax_c.text(77, 1.5, r'$\theta$-shift' + '\nabsorption',
               fontsize=5.5, color=palette.ANNOTATION, style='italic',
               ha='center', linespacing=1.0)
t1.set_path_effects(WHITE_STROKE)

t2 = ax_c.text(94, 9.5, 'ceiling\nreversal', fontsize=5.5,
               color=palette.ANNOTATION, style='italic', ha='center',
               linespacing=1.0)
t2.set_path_effects(WHITE_STROKE)

ax_c.set_xlabel('Baseline Accuracy (%)', fontsize=8)
ax_c.set_ylabel("Cohen's |$d$|", fontsize=8)
ax_c.set_xlim(44, 98)
ax_c.set_ylim(0, Y_MAX_C)
ax_c.set_yticks([0, 2, 4, 6, 8, 10])

ax_c.text(0.02, 0.97, '(c)', transform=ax_c.transAxes,
          fontsize=11, fontweight='bold', va='top', ha='left',
          color=palette.TEXT)
palette.style_ax(ax_c)

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL (d): dose-response trajectory
# ═══════════════════════════════════════════════════════════════════════════════
x_dose = np.array([0, 1, 2, 3])
qwen_free_d   = np.array([4.15, 5.36, 7.44, 5.08])
qwen_free_sd  = np.array([0.0,  1.10, 1.86, 3.02])
qwen_fixed_d  = np.array([3.52, 6.85, 5.89, 12.32])
qwen_fixed_sd = np.array([0.0,  1.80, 1.27, 2.38])
llama_free_d  = np.array([2.57, 2.80, 2.56, 2.30])
llama_free_sd = np.array([0.99, 0.60, 0.52, 0.30])

# |d|=0.8 reference
ax_d.axhline(y=0.8, color=palette.REFERENCE, linestyle=':', linewidth=0.6, zorder=1)
t_ref = ax_d.text(3.4, 1.1, '$|d|{=}0.8$', fontsize=5, color=palette.REFERENCE,
                  ha='right', va='bottom')
t_ref.set_path_effects(WHITE_STROKE)

# Llama free-θ
ax_d.fill_between(x_dose, llama_free_d - llama_free_sd,
                  llama_free_d + llama_free_sd,
                  alpha=0.10, color=palette.LLAMA, zorder=2)
ax_d.errorbar(x_dose, llama_free_d, yerr=llama_free_sd,
              fmt='^-', color=palette.LLAMA, markersize=5, linewidth=1.2,
              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
              label=r'Llama free-$\theta$', zorder=4, markeredgecolor='white',
              markeredgewidth=0.6)

# Qwen free-θ
qf_sd_vis = qwen_free_sd.copy()
qf_sd_vis[0] = 0.35
ax_d.fill_between(x_dose, qwen_free_d - qf_sd_vis,
                  qwen_free_d + qf_sd_vis,
                  alpha=0.10, color=palette.QWEN, zorder=2)
ax_d.errorbar(x_dose[1:], qwen_free_d[1:], yerr=qwen_free_sd[1:],
              fmt='o-', color=palette.QWEN, markersize=5.5, linewidth=1.4,
              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
              label=r'Qwen free-$\theta$', zorder=5, markeredgecolor='white',
              markeredgewidth=0.6)
ax_d.plot(x_dose[:2], qwen_free_d[:2], '-', color=palette.QWEN, linewidth=1.4,
          alpha=0.85, zorder=5)
# Hollow marker at 5% (single-seed)
ax_d.plot(x_dose[0], qwen_free_d[0], 'o', color=palette.QWEN, markersize=5.5,
          markerfacecolor='white', markeredgecolor=palette.QWEN,
          markeredgewidth=1.2, zorder=6)

# Qwen fixed-θ
ax_d.fill_between(x_dose, qwen_fixed_d - qwen_fixed_sd,
                  np.minimum(qwen_fixed_d + qwen_fixed_sd, 15.5),
                  alpha=0.08, color=palette.SIGNAL, zorder=2)
ax_d.errorbar(x_dose[1:], qwen_fixed_d[1:], yerr=qwen_fixed_sd[1:],
              fmt='s--', color=palette.SIGNAL, markersize=5, linewidth=1.3,
              capsize=2.5, capthick=0.6, elinewidth=0.7, alpha=0.85,
              label=r'Qwen fixed-$\theta$', zorder=5, markeredgecolor='white',
              markeredgewidth=0.6)
ax_d.plot(x_dose[:2], qwen_fixed_d[:2], '--', color=palette.SIGNAL, linewidth=1.3,
          alpha=0.85, zorder=5)
# Hollow marker at 5%
ax_d.plot(x_dose[0], qwen_fixed_d[0], 's', color=palette.SIGNAL, markersize=5,
          markerfacecolor='white', markeredgecolor=palette.SIGNAL,
          markeredgewidth=1.2, zorder=6)

# Annotations
ax_d.annotate('',
              xy=(3, 5.35), xycoords='data',
              xytext=(2, 7.44), textcoords='data',
              arrowprops=dict(arrowstyle='->', color=palette.QWEN,
                              lw=0.8, connectionstyle='arc3,rad=0.3'))
t_abs = ax_d.text(3.45, 1.8, r'$\theta$-shift absorption',
                  fontsize=5.5, color=palette.QWEN, ha='right', va='top',
                  linespacing=1.0, fontstyle='italic')
t_abs.set_path_effects(WHITE_STROKE)

t_fix = ax_d.text(1.6, 15.2, r'$\theta$-anchoring recovers signal',
                  fontsize=5.5, color=palette.SIGNAL, ha='center', va='bottom',
                  fontstyle='italic', linespacing=1.0)
t_fix.set_path_effects(WHITE_STROKE)

# Single-seed label
ax_d.text(-0.25, 4.5, '$n{=}1$', fontsize=5.5, color=palette.REFERENCE,
          fontstyle='italic')

ax_d.set_xticks(x_dose)
ax_d.set_xticklabels(['5%', '15%', '25%', '50%'])
ax_d.set_xlabel('Contamination level', fontsize=8)
ax_d.set_ylabel("Cohen's |$d$|", fontsize=8)
ax_d.set_ylim(0, 15.5)
ax_d.set_xlim(-0.4, 3.55)

# Legend
handles, labels = ax_d.get_legend_handles_labels()
order = [1, 2, 0]  # Qwen free, Qwen fixed, Llama
leg_d = ax_d.legend([handles[i] for i in order], [labels[i] for i in order],
                    loc='upper right', frameon=True, framealpha=0.95,
                    edgecolor='none', facecolor='white',
                    handlelength=1.8, handletextpad=0.4, fontsize=6,
                    borderpad=0.4, bbox_to_anchor=(0.98, 0.62))
leg_d.get_frame().set_linewidth(0)

ax_d.text(0.02, 0.97, '(d)', transform=ax_d.transAxes,
          fontsize=11, fontweight='bold', va='top', ha='left',
          color=palette.TEXT)
palette.style_ax(ax_d)

# ═══════════════════════════════════════════════════════════════════════════════
# SAVE + COPY
# ═══════════════════════════════════════════════════════════════════════════════
out_dir = PROJ / 'figures' / 'paper'
fig.savefig(out_dir / 'fig_1_composite.pdf', format='pdf')
fig.savefig(out_dir / 'fig_1_composite.png', format='png')
plt.close()
print("Saved fig_1_composite.pdf and .png")

copy_targets = [
    PROJ / 'paper' / 'paper',
    PROJ / 'paper' / 'paper' / 'figures' / 'paper',
]
for tgt in copy_targets:
    tgt.mkdir(parents=True, exist_ok=True)
    for ext in ['pdf', 'png']:
        src = out_dir / f'fig_1_composite.{ext}'
        dst = tgt / f'fig_1_composite.{ext}'
        shutil.copy2(str(src), str(dst))
        print(f"  → {dst}")

print("Done.")
