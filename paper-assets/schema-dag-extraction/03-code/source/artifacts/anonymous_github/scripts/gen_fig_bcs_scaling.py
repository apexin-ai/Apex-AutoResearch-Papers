import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

# --- Data (count_8, all pool sizes) ---
pool_sizes = np.array([16, 40, 80])
# Qwen3-32B (main model)
bcs_effect_qwen = np.array([9.1, 33.3, 31.2])   # |Δacc| in pp
low_bcs_qwen    = np.array([0.889, 0.833, 0.8229])
high_bcs_qwen   = np.array([0.798, 0.500, 0.5104])

# LLaMA-3.1-8B (cross-model, 80-rel only)
bcs_effect_llama_80 = 27.1
low_bcs_llama_80    = 0.7812
high_bcs_llama_80   = 0.5104

# Print data for verification
print("=== Data Verification (count_8) ===")
for ps, lo, hi, eff in zip(pool_sizes, low_bcs_qwen, high_bcs_qwen, bcs_effect_qwen):
    print(f"  Pool {ps:2d}-rel: low_bcs={lo:.4f}, high_bcs={hi:.4f}, Δ={eff:.1f}pp")
print(f"  LLaMA 80-rel: low_bcs={low_bcs_llama_80:.4f}, high_bcs={high_bcs_llama_80:.4f}, Δ={bcs_effect_llama_80:.1f}pp")

# --- Colors (Okabe-Ito) ---
C_MAIN  = '#0072B2'  # deep blue - Qwen
C_LLAMA = '#D55E00'  # orange-red - LLaMA
C_LOW   = '#56B4E9'  # sky blue - low BCS
C_HIGH  = '#E69F00'  # amber - high BCS

# --- Figure: Combined layout ---
fig, (ax_line, ax_bar) = plt.subplots(1, 2, figsize=(10, 4.2),
                                       gridspec_kw={'width_ratios': [1.1, 1]})

# ===== Left panel: BCS Effect Size vs Pool Size =====
ax = ax_line

# Solid line connecting 16-rel and 80-rel (independent pool sizes)
ax.plot([16, 80], [bcs_effect_qwen[0], bcs_effect_qwen[2]], 'o-', color=C_MAIN,
        markersize=9, zorder=3, label='Qwen3-32B')
# Dashed lines connecting to 40-rel (80-pool subset)
ax.plot([16, 40], [bcs_effect_qwen[0], bcs_effect_qwen[1]], '--', color=C_MAIN,
        linewidth=1.5, alpha=0.6, zorder=2)
ax.plot([40, 80], [bcs_effect_qwen[1], bcs_effect_qwen[2]], '--', color=C_MAIN,
        linewidth=1.5, alpha=0.6, zorder=2)
# 40-rel hollow marker
ax.plot(40, bcs_effect_qwen[1], 'o', color=C_MAIN, markersize=9,
        markerfacecolor='white', markeredgewidth=2, zorder=4)

# LLaMA point
ax.plot(80, bcs_effect_llama_80, 's', color=C_LLAMA, markersize=9,
        label='LLaMA-3.1-8B', zorder=3)

# 3.4x amplification annotation (16 -> 80 only, per C002)
ax.annotate('3.4×', xy=(48, 20), fontsize=14, fontweight='bold',
            color=C_MAIN, ha='center',
            arrowprops=dict(arrowstyle='->', color=C_MAIN, lw=1.5),
            xytext=(48, 12))
ax.annotate('', xy=(16, 9.1), xytext=(16, 12),
            arrowprops=dict(arrowstyle='-', color=C_MAIN, lw=1.2))
ax.annotate('', xy=(80, 31.2), xytext=(80, 20),
            arrowprops=dict(arrowstyle='-', color=C_MAIN, lw=1.2))
ax.plot([16, 16, 80, 80], [12, 12, 20, 20], color=C_MAIN, lw=1.2, ls='--', alpha=0.5)

# Axis formatting
ax.set_xlabel('Relation Pool Size')
ax.set_ylabel('BCS Effect Size (|Δaccuracy| in pp)')
ax.set_xticks(pool_sizes)
ax.set_xticklabels(['16', '40\n(80-pool\nsubset)', '80'])
ax.set_ylim(0, 40)
ax.set_xlim(5, 90)
ax.legend(loc='lower right', framealpha=0.9)
ax.grid(True, alpha=0.2, axis='y')
ax.set_title('(a) BCS Effect Scales with Pool Size', fontsize=12, pad=8)

# ===== Right panel: Grouped Bar (Low vs High BCS) =====
ax = ax_bar
x = np.arange(len(pool_sizes))
w = 0.32

bars_lo = ax.bar(x - w/2, low_bcs_qwen, w, color=C_LOW, label='Low BCS', zorder=2)
bars_hi = ax.bar(x + w/2, high_bcs_qwen, w, color=C_HIGH, label='High BCS', zorder=2)

# 40-rel bars (index 1) hatched to mark as 80-pool subset
bars_lo[1].set_hatch('///')
bars_lo[1].set_edgecolor(C_LOW)
bars_hi[1].set_hatch('///')
bars_hi[1].set_edgecolor(C_HIGH)

# Value labels
for bar_group in [bars_lo, bars_hi]:
    for bar in bar_group:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.01, f'{h:.2f}',
                ha='center', va='bottom', fontsize=8.5)

# Delta annotations
for i, delta in enumerate(bcs_effect_qwen):
    mid_x = x[i]
    mid_y = (low_bcs_qwen[i] + high_bcs_qwen[i]) / 2
    ax.annotate(f'Δ={delta:.1f}pp', xy=(mid_x, mid_y), fontsize=8.5,
                ha='center', va='center', fontweight='bold', color='#333333',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#cccccc', alpha=0.85))

ax.set_xlabel('Relation Pool Size')
ax.set_ylabel('Accuracy')
ax.set_xticks(x)
ax.set_xticklabels(['16', '40\n(80-pool subset)', '80'])
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.2, axis='y')
ax.set_title('(b) Low vs High BCS Accuracy', fontsize=12, pad=8)

plt.tight_layout(w_pad=3)
outpath = './figures/paper/fig_bcs_scaling.pdf'
plt.savefig(outpath)
plt.close()
print(f'\nSaved: {outpath}')
