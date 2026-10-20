import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# --- Data ---
steps = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
ss_ratio = [1.047, 1.077, 1.104, 1.041, 1.247, 1.243, 1.350, 1.398, 1.466, 1.373, 1.610, 1.678]
ve_ratio = [0.005, 0.022, 0.156, 0.163, 0.215, 0.229, 1.591, 0.360, 0.616, 0.621, 1.399, 1.399]

# --- Colors (Okabe-Ito semantic) ---
C_BLUE = '#0072B2'
C_RED  = '#D55E00'
C_GRAY = '#888888'

# --- Style ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'STIXGeneral'],
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'lines.linewidth': 1.6,
    'mathtext.fontset': 'stix',
})

fig, ax1 = plt.subplots(figsize=(5, 3))

# --- Left Y axis: SS fidelity ratio ---
ln1 = ax1.plot(steps, ss_ratio, color=C_BLUE, marker='o', markersize=4.5,
               markerfacecolor=C_BLUE, markeredgecolor='white', markeredgewidth=0.5,
               linewidth=1.5, label='SS fidelity ratio', zorder=4)
ax1.set_xlabel('Training Steps (K)', labelpad=4)
ax1.set_ylabel(r'SS Fidelity Ratio ($d_{t{=}2}\!/\!d_{t{=}1}$)', color=C_BLUE, labelpad=3)
ax1.tick_params(axis='y', colors=C_BLUE, length=3, width=0.6)
ax1.tick_params(axis='x', length=3, width=0.6)
ax1.spines['left'].set_color(C_BLUE)
ax1.spines['left'].set_linewidth(0.8)
ax1.spines['bottom'].set_linewidth(0.6)
ax1.spines['right'].set_visible(False)

# --- Right Y axis: VE ratio ---
ax2 = ax1.twinx()
ln2 = ax2.plot(steps, ve_ratio, color=C_RED, marker='^', markersize=4.5,
               markerfacecolor=C_RED, markeredgecolor='white', markeredgewidth=0.5,
               linewidth=1.5, label='VE ratio', zorder=4)
ax2.set_ylabel('Value Overestimation Ratio', color=C_RED, labelpad=3)
ax2.tick_params(axis='y', colors=C_RED, length=3, width=0.6)
ax2.spines['right'].set_visible(True)
ax2.spines['right'].set_color(C_RED)
ax2.spines['right'].set_linewidth(0.8)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(False)

import matplotlib.patheffects as pe
stroke = [pe.withStroke(linewidth=2.5, foreground='white')]

# --- Threshold lines (labels inside plot) ---
ax1.axhline(y=1.1, color=C_GRAY, linestyle='--', linewidth=0.6, alpha=0.35, zorder=1)
t1 = ax1.text(56, 1.115, 'SS > 1.1×', fontsize=6, color=C_GRAY, va='bottom', ha='left',
              fontstyle='italic', alpha=0.65)
t1.set_path_effects(stroke)

ax2.axhline(y=1.5, color=C_GRAY, linestyle=':', linewidth=0.6, alpha=0.35, zorder=1)
t2 = ax2.text(11, 1.53, 'VE > 1.5×', fontsize=6, color=C_GRAY, va='bottom', ha='left',
              fontstyle='italic', alpha=0.65)
t2.set_path_effects(stroke)

# --- Vertical shaded band: lag region (~20K to ~30K, onset-to-onset) ---
ax1.axvspan(20, 30, alpha=0.04, color='#666666', zorder=0)

# lag arrow + label inside the band, upper region
ax1.annotate('', xy=(29.5, 1.72), xytext=(20.5, 1.72),
             arrowprops=dict(arrowstyle='<->', color=C_GRAY, lw=0.7))
tlag = ax1.text(25, 1.735, '~10K step lag', fontsize=7, color='#555555', ha='center',
                va='bottom', fontstyle='italic', fontweight='medium')
tlag.set_path_effects(stroke)

# --- Annotations ---
ax1.annotate('Fidelity onset', xy=(20, 1.104), xytext=(14, 1.35),
             fontsize=7, color=C_BLUE, ha='center', va='bottom',
             arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=0.7,
                             shrinkA=0, shrinkB=3, connectionstyle='arc3,rad=-0.15'))

ax2.annotate('VE spike', xy=(40, 1.591), xytext=(47, 1.85),
             fontsize=7, color=C_RED, ha='center', va='bottom',
             arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.7,
                             shrinkA=0, shrinkB=3, connectionstyle='arc3,rad=-0.15'))

# --- X axis ---
ax1.set_xlim(8, 67)
ax1.set_xticks(steps)

# --- Y axis limits ---
ax1.set_ylim(0.9, 1.80)
ax2.set_ylim(-0.1, 2.1)

# --- Legend (combined, bottom-left to avoid lag annotation) ---
lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='lower right', frameon=True, framealpha=0.92,
           edgecolor='#cccccc', fancybox=False, borderpad=0.4,
           handlelength=1.8, handletextpad=0.5)

# --- Remove grid ---
ax1.grid(False)
ax2.grid(False)

# --- Background ---
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/figures/paper'
plt.savefig(f'{out_dir}/fig_temporal_ordering.pdf', format='pdf')
plt.savefig(f'{out_dir}/fig_temporal_ordering.png', format='png')
print('Saved PDF and PNG.')
plt.close()
