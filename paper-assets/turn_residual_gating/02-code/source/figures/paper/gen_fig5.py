from palette import *
import matplotlib.gridspec as gridspec
import numpy as np

apply_style()

# ── Data (unchanged) ──────────────────────────────────────────────
gen_beta =    [0.0,   0.5,   1.0,   2.0,   5.0,   10.0]
gen_gar =     [0.028, 0.0287, 0.0349, 0.062, 0.6795, 0.959]
gen_gar_std = [0.014, 0.008, 0.007, 0.011, 0.020, 0.003]
gen_ppl =     [1.41,  1.39,  1.36,  1.41,  1.91,  4.22]
gen_ppl_std = [0.12,  0.11,  0.10,  0.12,  0.36,  0.99]

gen50_beta =    [0.0,   2.0,   3.0,   4.0,   5.0,   10.0]
gen50_gar =     [0.064, 0.128, 0.556, 0.644, 0.727, 0.961]
gen50_gar_std = [0.081, 0.110, 0.060, 0.061, 0.061, 0.015]
gen50_ppl =     [1.43,  1.48,  1.56,  1.67,  1.77,  3.45]
gen50_ppl_std = [0.10,  0.14,  0.17,  0.22,  0.27,  1.78]

# ── Layout: 2×2 grid for double-column figure ─────────────────────
fig = plt.figure(figsize=(7.0, 2.8))
gs = gridspec.GridSpec(2, 2, hspace=0.55, wspace=0.35,
                       height_ratios=[1, 0.85])

ax_gar5  = fig.add_subplot(gs[0, 0])
ax_ppl5  = fig.add_subplot(gs[1, 0])
ax_gar50 = fig.add_subplot(gs[0, 1])
ax_ppl50 = fig.add_subplot(gs[1, 1])

XLO, XHI = -0.8, 11.3

# ── Shared plotting helpers ───────────────────────────────────────
def style_ax(ax):
    ax.grid(axis='y', alpha=0.08, linewidth=0.5)

def plot_gar(ax, beta, gar, gar_std, title):
    style_ax(ax)
    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)
    ax.axhline(y=0.535, color=C_GRAY, linestyle=':', linewidth=0.7, zorder=1)
    ax.errorbar(beta, gar, yerr=gar_std, fmt='-o', color=C_TEAL,
                markersize=4.5, markerfacecolor=C_TEAL, markeredgecolor='white',
                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,
                zorder=3)
    ax.set_ylabel('Mid-GAR', color=C_TEAL, fontsize=9)
    ax.set_ylim(-0.02, 1.08)
    ax.set_xlim(XLO, XHI)
    ax.tick_params(axis='y', colors=C_TEAL)
    ax.set_title(title, pad=6, loc='left', fontsize=9.5, fontweight='medium')

def plot_ppl(ax, beta, ppl, ppl_std):
    style_ax(ax)
    ax.axvspan(2, 5, alpha=0.07, color=C_SWEET, zorder=0)
    ax.errorbar(beta, ppl, yerr=ppl_std, fmt='--^', color=C_ROSE,
                markersize=4, markerfacecolor=C_ROSE, markeredgecolor='white',
                markeredgewidth=0.5, capsize=2, capthick=0.7, elinewidth=0.7,
                zorder=3, linewidth=1.1)
    ax.set_ylabel('PPL', color=C_ROSE, fontsize=9)
    ax.set_xlim(XLO, XHI)
    ax.tick_params(axis='y', colors=C_ROSE)
    ax.set_xlabel(r'$\beta$ (Steering Strength)', fontsize=9)

# ── Panel (a): N=5 ────────────────────────────────────────────────
plot_gar(ax_gar5, gen_beta, gen_gar, gen_gar_std,
         '(a) $N$=5 Generation')
ax_gar5.set_xticks([0, 1, 2, 5, 10])
ax_gar5.set_xticklabels([])
ax_gar5.text(8.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,
             va='bottom', ha='center')
ax_gar5.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',
             ha='center', va='top', fontstyle='italic', alpha=0.65)

plot_ppl(ax_ppl5, gen_beta, gen_ppl, gen_ppl_std)
ax_ppl5.set_xticks([0, 1, 2, 5, 10])
ax_ppl5.set_ylim(0.9, 5.5)

# ── Panel (b): N=50 ───────────────────────────────────────────────
plot_gar(ax_gar50, gen50_beta, gen50_gar, gen50_gar_std,
         '(b) $N$=50 Generation')
ax_gar50.set_xticks([0, 2, 3, 4, 5, 10])
ax_gar50.set_xticklabels([])
ax_gar50.text(9.5, 0.56, 'TF baseline', fontsize=6.5, color=C_GRAY,
              va='bottom', ha='center')
ax_gar50.text(3.5, 1.03, 'sweet spot', fontsize=6, color='#B8960F',
              ha='center', va='top', fontstyle='italic', alpha=0.65)

ax_gar50.annotate(r'$\beta$=3 operating pt.',
                  xy=(3, 0.556), xytext=(7.0, 0.15),
                  fontsize=7, color='#444444', ha='center',
                  arrowprops=dict(arrowstyle='->', color=C_GRAY,
                                  lw=0.7, connectionstyle='arc3,rad=-0.12'),
                  bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.9, linewidth=0.5))

plot_ppl(ax_ppl50, gen50_beta, gen50_ppl, gen50_ppl_std)
ax_ppl50.set_xticks([0, 2, 3, 4, 5, 10])
ax_ppl50.set_ylim(0.9, 5.5)

save_fig(fig, 'fig5_attention_steering')
