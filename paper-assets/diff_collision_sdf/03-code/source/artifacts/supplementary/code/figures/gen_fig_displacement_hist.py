import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyBboxPatch

np.random.seed(42)

# --- Mock Data ---
a1_collapsed = np.random.lognormal(mean=-2, sigma=0.5, size=797)
a1_collapsed = np.clip(a1_collapsed, 0.001, 1)
a1_real = np.array([50, 120, 280])
data_a = np.concatenate([a1_collapsed, a1_real])

pi05_collapsed = np.random.lognormal(mean=-1, sigma=0.8, size=56)
pi05_collapsed = np.clip(pi05_collapsed, 0.01, 5)
pi05_real = np.random.lognormal(mean=4.5, sigma=0.8, size=544)
pi05_real = np.clip(pi05_real, 10, 500)
data_b = np.concatenate([pi05_collapsed, pi05_real])

data_c = np.random.lognormal(mean=3.8, sigma=0.6, size=200)
data_c = np.clip(data_c, 5, 300)

# --- Plot ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

bins = np.logspace(-3, 3, 40)
tau_d = 100  # μm = 0.1 mm

fig, axes = plt.subplots(3, 1, figsize=(5, 6), sharex=True)

color_frozen = '#FF6B6B'
color_frozen_edge = '#c0392b'
color_real = '#4CAF50'
color_real_edge = '#2E7D32'

panels = [
    (data_a, r'A1-LoRA (Pi0): 99.6% action-collapsed ($d_\mathrm{max} < \tau_d$)', '(a)'),
    (data_b, r'Pi0.5 baseline: ~9% action-collapsed ($d_\mathrm{max} < \tau_d$)', '(b)'),
    (data_c, r'Pi0.5+A1 (SDF aux): 0% action-collapsed ($d_\mathrm{max} < \tau_d$)', '(c)'),
]

for ax, (data, label, panel_id) in zip(axes, panels):
    counts, _, patches = ax.hist(data, bins=bins, color=color_real, edgecolor=color_real_edge, linewidth=0.4)

    for patch, left_edge in zip(patches, bins[:-1]):
        if left_edge < tau_d:
            patch.set_facecolor(color_frozen)
            patch.set_edgecolor(color_frozen_edge)
            patch.set_linewidth(0.4)
        else:
            patch.set_facecolor(color_real)
            patch.set_edgecolor(color_real_edge)

    ax.axvline(x=tau_d, color='#c0392b', linestyle='--', linewidth=1.0, zorder=5)
    ax.set_xscale('log')
    ax.set_ylabel('Episode Count')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0.001, 1000)

    ax.text(0.02, 0.92, f'{panel_id} {label}', transform=ax.transAxes,
            fontsize=7.5, fontweight='bold', va='top', ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc', linewidth=0.4, alpha=0.9))

# --- Overlays after ylims settled ---
for idx, (ax, (data, label, panel_id)) in enumerate(zip(axes, panels)):
    ymin, ymax = ax.get_ylim()

    # Subtle shading for fake-safe zone
    ax.axvspan(0.001, tau_d, alpha=0.06, color='#c0392b', zorder=0)

    # τ_d label on top panel only
    if idx == 0:
        ax.annotate(r'$\tau_d = 0.1\,\mathrm{mm}$', xy=(tau_d, ymax * 0.95),
                     xytext=(tau_d * 3, ymax * 0.95), fontsize=7, color='#c0392b',
                     va='top', ha='left',
                     arrowprops=dict(arrowstyle='->', color='#c0392b', lw=0.8))

    # "Fake Safe" label — placed at fixed position in collapsed zone
    if idx == 0:
        ax.text(0.005, ymax * 0.55, 'Fake Safe', fontsize=6.5, color='#c0392b',
                ha='left', va='top', alpha=0.8, style='italic', fontweight='bold',
                rotation=0)
    elif idx == 1:
        ax.text(0.015, ymax * 0.75, 'Fake\nSafe', fontsize=6, color='#c0392b',
                ha='left', va='top', alpha=0.8, style='italic', fontweight='bold')

axes[-1].set_xlabel('End-Effector Displacement (μm)')
axes[-1].xaxis.set_major_locator(mticker.LogLocator(base=10, numticks=10))
axes[-1].xaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f'{x:g}' if x in [0.001, 0.01, 0.1, 1, 10, 100, 1000] else ''))

fig.text(0.5, 0.005, '[Mock data — replace with real eval data]',
         ha='center', fontsize=6.5, color='#999999', style='italic')

plt.tight_layout(rect=[0, 0.025, 1, 1])
plt.subplots_adjust(hspace=0.12)

out_path = './output/fig_displacement_hist.pdf'
fig.savefig(out_path, dpi=300, bbox_inches='tight')
print(f'Saved to {out_path}')
