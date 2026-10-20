"""Generate cross-model comparison figure: TF-AR gap + gate profile overlay."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import numpy as np

apply_style()

fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.5, 5.8),
                                   gridspec_kw={'height_ratios': [1, 1.1]})

# ======================================================================
# Panel (a): Qwen vs Llama TF-AR gap (grouped bars, log scale)
# ======================================================================
models = ['Qwen-2.5-7B', 'Llama-3.1-8B']
tf_gar = [0.50, 0.484]
ar_gar = [0.064, 0.018]
gaps   = [7.8, 27]

x = np.arange(len(models))
w = 0.28

bars_tf = ax_a.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',
                   zorder=2, edgecolor='white', linewidth=0.4)
bars_ar = ax_a.bar(x + w/2, ar_gar, w, color=C_AR, label='Autoregressive',
                   zorder=2, edgecolor='white', linewidth=0.4)

ax_a.set_yscale('log')
ax_a.set_ylim(0.008, 1.5)
ax_a.set_xlim(-0.55, 2.0)

ax_a.axhspan(0.008, 0.08, color='#FFF3E0', alpha=0.15, zorder=0)
ax_a.axhspan(0.08, 1.5, color='#E8F5E9', alpha=0.15, zorder=0)

for i in range(len(models)):
    ax_a.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
             color=C_GRAY, linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))

for i, v in enumerate(tf_gar):
    ax_a.text(x[i] - w/2, v * 1.15, f'.{round(v*100):02d}', ha='center',
              va='bottom', fontsize=6, color=C_TF_DARK, fontweight='bold')

for i, v in enumerate(ar_gar):
    ax_a.text(x[i] + w/2, v * 1.20, f'.{round(v*1000):03d}', ha='center',
              va='bottom', fontsize=5.5, color=C_AR_DARK)

for i, gap in enumerate(gaps):
    geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
    suffix = '\n(median)' if i == 1 else ''
    t = ax_a.text(x[i] + w/2 + 0.14, geo_mean, f'{gap:.0f}×{suffix}',
                  fontsize=7.5, fontweight='bold', color=C_AR,
                  ha='left', va='center')
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

ax_a.set_xticks(x)
ax_a.set_xticklabels(models, fontsize=8)
ax_a.set_ylabel('GAR-ours (ThreadGate)')
ax_a.set_title('(a) TF-AR gap generalizes across architectures',
               fontsize=9, fontweight='bold', pad=8, loc='left')
ax_a.legend(loc='upper right',
            handletextpad=0.3, borderpad=0.35, fontsize=6.5)

ax_a.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax_a.grid(axis='y', which='major', alpha=0.10, zorder=0)

# ======================================================================
# Panel (b): Gate profile overlay (normalized depth)
# ======================================================================
qwen_gates = np.array([
    .883, .793, .996, .988, .984, .797, .961, .918,
    .965, .934, .969, .918, .926, .941, .930, .965,
    .941, .910, .961, .965, .973, .988, .969, .980,
    .980, .984, .988, 1.00
])
llama_gates = np.array([
    0.957, 0.973, 0.977, 0.965, 0.992, 0.969, 0.957, 0.957,
    0.961, 0.949, 0.938, 0.934, 0.969, 0.953, 0.957, 0.965,
    0.953, 0.961, 0.922, 0.902, 0.883, 0.863, 0.836, 0.844,
    0.809, 0.719, 0.762, 0.805, 0.801, 0.855, 0.898, 0.934
])

qwen_depth = np.linspace(0, 1, len(qwen_gates))
llama_depth = np.linspace(0, 1, len(llama_gates))

ax_b.plot(qwen_depth, qwen_gates, 'o-', color=C_TG, markersize=3.5,
          markeredgecolor='white', markeredgewidth=0.4,
          label='Qwen-2.5-7B (28L)', zorder=3, linewidth=1.5)
ax_b.plot(llama_depth, llama_gates, 's-', color=C_LO, markersize=3.5,
          markeredgecolor='white', markeredgewidth=0.4,
          label='Llama-3.1-8B (32L)', zorder=3, linewidth=1.5)

ax_b.axhline(1.0, color='#DDDDDD', linestyle=':', linewidth=0.6, zorder=1)
ax_b.text(0.98, 1.006, 'identity', fontsize=6, color='#BBBBBB',
          ha='right', va='bottom')

ax_b.annotate('L1=.793', xy=(qwen_depth[1], qwen_gates[1]),
              xytext=(qwen_depth[1] + 0.10, 0.755), fontsize=6,
              color=C_TG, ha='left',
              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))
ax_b.annotate('L5=.797', xy=(qwen_depth[5], qwen_gates[5]),
              xytext=(qwen_depth[5] + 0.10, 0.76), fontsize=6,
              color=C_TG, ha='left',
              arrowprops=dict(arrowstyle='->', color=C_TG, lw=0.5))

ax_b.annotate('L25=.719', xy=(llama_depth[25], llama_gates[25]),
              xytext=(llama_depth[25] - 0.15, 0.695), fontsize=6,
              color=C_LO, ha='right',
              arrowprops=dict(arrowstyle='->', color=C_LO, lw=0.5))

ax_b.set_xlabel('Normalized Depth (layer / L)')
ax_b.set_ylabel('Gate Value')
ax_b.set_ylim(0.68, 1.03)
ax_b.set_xlim(-0.02, 1.02)
ax_b.set_title('(b) Architecture-dependent gate patterns',
               fontsize=9, fontweight='bold', pad=8, loc='left')
ax_b.legend(loc='lower right',
            handletextpad=0.3, borderpad=0.35, fontsize=6.5)
ax_b.grid(axis='y', alpha=0.10, zorder=0)

plt.tight_layout(h_pad=1.8)
save_fig(fig, 'fig_crossmodel')
