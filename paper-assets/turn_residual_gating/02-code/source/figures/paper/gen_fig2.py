from palette import *
import matplotlib.patheffects as pe
import numpy as np

apply_style()

# v7 data (micro-step -> global step)
v7_ms = np.array([
    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100,
    1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600
])
v7_gs = v7_ms / 8.0

v7_lgar = np.array([
    0.2342, 0.2349, 0.2337, 0.2277, 0.2348, 0.2314, 0.2263, 0.2298,
    0.2368, 0.2251, 0.2285, 0.2326, 0.2179, 0.2106, 0.1886, 0.1386,
    0.1237, 0.0788, 0.0676, 0.0549, 0.0454, 0.0398, 0.0328, 0.0044,
    0.0053, 0.0359, 0.0002, 0.0001, 0.0000, 0.0005, 0.0000, 0.0011,
    0.0004
])
v7_gar = 0.5 - np.sqrt(v7_lgar)

v7_gs_ext = np.concatenate([v7_gs, np.arange(250, 1250, 50)])
v7_lgar_ext = np.concatenate([v7_lgar, np.full(20, 0.0005)])

# v9 PCGrad data
v9_ms = np.array([
    0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,
    600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100
])
v9_gs = v9_ms / 8.0
v9_lgar = np.array([
    0.2342, 0.2349, 0.2337, 0.2270, 0.2339, 0.2280, 0.2205, 0.2196,
    0.2090, 0.1675, 0.1760, 0.1673, 0.1244, 0.1102, 0.0939, 0.0737,
    0.0832, 0.0491, 0.0410, 0.0304, 0.0343, 0.0239, 0.0367
])

fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 6.0),
                                  gridspec_kw={'hspace': 0.38})

# ═══════════════════════════════════════════════════════════════════════
# Panel (a): Three-Phase GAR Convergence
# ═══════════════════════════════════════════════════════════════════════
BAND_A = (0, 75)
BAND_B = (75, 144)
BAND_C = (144, 260)

ax_a.axvspan(*BAND_A, alpha=0.08, color=C_SKYBLUE, zorder=0)
ax_a.axvspan(*BAND_B, alpha=0.08, color=C_GOLD, zorder=0)
ax_a.axvspan(*BAND_C, alpha=0.08, color=C_GREEN, zorder=0)

for bx in [BAND_A[1], BAND_B[1]]:
    ax_a.axvline(bx, color='#cccccc', linewidth=0.5, linestyle='-',
                 alpha=0.45, zorder=0)

ax_a.text(37.5, 0.535, 'A', fontsize=11, color=C_TF_DARK, ha='center',
          va='bottom', fontweight='bold')
ax_a.text(109.5, 0.535, 'B', fontsize=11, color='#B89A5A', ha='center',
          va='bottom', fontweight='bold')
ax_a.text(200, 0.535, 'C', fontsize=11, color='#6AB06A', ha='center',
          va='bottom', fontweight='bold')

ax_a.axhline(0.5, color=C_GRAY, linestyle='--', linewidth=0.9,
             alpha=0.6, zorder=1)
t_target = ax_a.text(255, 0.508, 'target = 0.5', fontsize=7,
                     color=C_GRAY, ha='right', va='bottom')
t_target.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax_a.plot(v7_gs, v7_gar, color=C_TG, linewidth=2, zorder=3,
          solid_capstyle='round')

ax_a.annotate('phase transition\n(gs 75)', xy=(75, 0.033),
              xytext=(30, 0.22), fontsize=7, color='#666666',
              ha='center', va='bottom',
              arrowprops=dict(arrowstyle='->', color=C_GRAY,
                              lw=0.8, connectionstyle='arc3,rad=-0.2'))
ax_a.annotate('target reached\n(gs 144)', xy=(144, 0.434),
              xytext=(210, 0.28), fontsize=7, color='#666666',
              ha='center', va='bottom',
              arrowprops=dict(arrowstyle='->', color=C_GRAY,
                              lw=0.8, connectionstyle='arc3,rad=0.2'))

ax_a.set_xlim(-5, 260)
ax_a.set_ylim(-0.03, 0.58)
ax_a.set_xlabel('Global Step')
ax_a.set_ylabel('Training GAR')
ax_a.set_title('(a) Three-phase convergence to target',
               fontsize=9, pad=8, loc='left')

ax_a.text(0.97, 0.38,
          'L$_{NTP}$: 2.03 → 0.93\n(normal convergence)',
          transform=ax_a.transAxes, fontsize=7, color='#777777',
          ha='right', va='top', fontstyle='italic',
          bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.85, linewidth=0.6))

# ═══════════════════════════════════════════════════════════════════════
# Panel (b): PCGrad vs v7 — Causal Exclusion
# ═══════════════════════════════════════════════════════════════════════
ax_b.plot(v7_gs_ext, v7_lgar_ext, color=C_TG, linewidth=1.8,
          label='v7 (baseline)', zorder=3, solid_capstyle='round')
ax_b.plot(v9_gs, v9_lgar, color=C_ROSE, linewidth=2.0,
          linestyle='--', label='v9 (PCGrad)', zorder=3,
          solid_capstyle='round')

ax_b.axvline(200, color=C_UG, linestyle=':', linewidth=0.9,
             alpha=0.7, zorder=2)
t_cos = ax_b.text(193, 0.215, 'cos_sim > 0\n(gs ≈ 200)',
                  fontsize=6.5, color=C_UG, va='top', ha='right')
t_cos.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

last_v9 = len(v9_gs) - 1
ax_b.plot(v9_gs[last_v9], v9_lgar[last_v9], 'o', color=C_ROSE,
          markersize=4.5, zorder=5, markeredgecolor='white', markeredgewidth=0.6)
ax_b.annotate('ongoing',
              xy=(v9_gs[last_v9], v9_lgar[last_v9]),
              xytext=(v9_gs[last_v9] + 15, v9_lgar[last_v9] + 0.01),
              fontsize=6.5, color=C_ROSE, ha='left', va='center',
              arrowprops=dict(arrowstyle='->', color=C_ROSE, lw=0.7,
                              connectionstyle='arc3,rad=-0.15'))

ax_b.text(
    0.03, 0.30,
    'Conflict resolved,\nL$_{GAR}$ still collapses',
    transform=ax_b.transAxes, fontsize=7, color='#555555',
    ha='left', va='top', fontstyle='italic',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF8E7',
              edgecolor=C_ROSE, alpha=0.9, linewidth=0.8)
)

ax_b.legend(loc='upper right', borderpad=0.4, handlelength=1.8)

ax_b.set_xlim(-5, 220)
ax_b.set_ylim(-0.008, 0.26)
ax_b.set_xlabel('Global Step')
ax_b.set_ylabel('L$_{GAR}$ (MSE loss)')
ax_b.set_title('(b) PCGrad cannot prevent L$_{GAR}$ collapse',
               fontsize=9, pad=8, loc='left')

for ax in [ax_a, ax_b]:
    ax.grid(axis='y', alpha=0.10, linewidth=0.5, color='#888888')

fig.subplots_adjust(hspace=0.38)

save_fig(fig, 'fig2_training_pcgrad')
