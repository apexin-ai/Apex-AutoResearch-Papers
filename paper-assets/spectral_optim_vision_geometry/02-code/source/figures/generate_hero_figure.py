import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.default': 'regular',
})

C_MUON = '#E8833A'
C_ADAM = '#4EABD1'
C_SGD  = '#BFBFBF'

fig = plt.figure(figsize=(10, 4.2), dpi=300, facecolor='white')
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1],
                       wspace=0.30, left=0.06, right=0.97, top=0.90, bottom=0.18)

# Panel (a): Norm-Swap Bar Chart
ax_bar = fig.add_subplot(gs[0])
norms = ['BN', 'GN', 'LN']
muon_acc = [76.88, 78.20, 78.52]
adam_acc  = [67.85, 55.73, 50.51]
sgd_acc  = [69.50, 23.90, 28.90]

x = np.arange(len(norms))
w_bar = 0.25
b1 = ax_bar.bar(x - w_bar, muon_acc, w_bar, color=C_MUON, alpha=0.85,
                label='Muon', edgecolor='white', linewidth=0.5)
b2 = ax_bar.bar(x, adam_acc, w_bar, color=C_ADAM, alpha=0.85,
                label='AdamW', edgecolor='white', linewidth=0.5)
b3 = ax_bar.bar(x + w_bar, sgd_acc, w_bar, color=C_SGD, alpha=0.85,
                label='SGD', edgecolor='white', linewidth=0.5)

ax_bar.set_ylabel('Top-1 Acc (%)', fontsize=11)
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(norms, fontsize=11)
ax_bar.set_ylim(15, 88)
ax_bar.tick_params(labelsize=11)
ax_bar.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.08, 1.12), frameon=False)

for bars in [b1, b2, b3]:
    for bar in bars:
        h = bar.get_height()
        ax_bar.text(bar.get_x() + bar.get_width()/2, h + 0.3, f'{h:.1f}',
                    ha='center', va='bottom', fontsize=10)

# Dashed lines + delta labels between Muon and AdamW bar tops
for i in range(len(norms)):
    m_h = muon_acc[i]
    a_h = adam_acc[i]
    x_m = x[i] - w_bar
    x_a = x[i]
    delta = m_h - a_h
    mid_y = (m_h + a_h) / 2
    ax_bar.plot([x_m, x_a], [m_h, m_h], color='#666', ls='--', lw=0.8)
    ax_bar.plot([x_m, x_a], [a_h, a_h], color='#666', ls='--', lw=0.8)
    ax_bar.plot([x_a, x_a], [a_h, m_h], color='#666', ls='--', lw=0.8)
    y_offset = 3.0 if i == 0 else 0  # shift BN delta label up
    ax_bar.text(x_a + 0.03, mid_y + y_offset, f'Δ={delta:.1f}',
                ha='left', va='center', fontsize=10, color='#444')

# Panel label below
ax_bar.text(0.5, -0.15, '(a) Norm-Swap Controlled Test',
            transform=ax_bar.transAxes, ha='center', fontsize=12, fontweight='bold')

# Panel (b): Accuracy Gap Heatmap
ax_heat = fig.add_subplot(gs[1])

archs = ['ResNet-50', 'ConvNeXt-T', 'DeiT-S']
datasets = ['CIFAR-100', 'Tiny-IN', 'IN-100']
gaps = np.array([
    [ 9.03,  5.90, 11.47],
    [16.08, 15.00, 24.30],
    [10.34,  7.69, 10.92],
])

im = ax_heat.imshow(gaps, cmap='Oranges', aspect='auto', vmin=0, vmax=26)

ax_heat.set_xticks(range(len(datasets)))
ax_heat.set_xticklabels(datasets, fontsize=11)
ax_heat.set_yticks(range(len(archs)))
ax_heat.set_yticklabels(archs, fontsize=11)
ax_heat.tick_params(length=0)

for i in range(len(archs)):
    for j in range(len(datasets)):
        val = gaps[i, j]
        color = 'white' if val > 10 else '#333'
        ax_heat.text(j, i, f'+{val:.1f}', ha='center', va='center',
                     fontsize=14, fontweight='bold', color=color)

cbar = plt.colorbar(im, ax=ax_heat, fraction=0.046, pad=0.04, shrink=0.85)
cbar.set_label('Muon − AdamW (pp)', fontsize=11)
cbar.ax.tick_params(labelsize=10)


# Panel label below
ax_heat.text(0.5, -0.15, '(b) Accuracy Gains Overview',
             transform=ax_heat.transAxes, ha='center', fontsize=12, fontweight='bold')

# Save
out_base = '/root/spectral_optim_vision_geometry/figures/hero_figure_v6'
fig.savefig(out_base + '.png', dpi=300, bbox_inches='tight', facecolor='white')
fig.savefig(out_base + '.pdf', bbox_inches='tight', facecolor='white')
print(f"Saved: {out_base}.png and {out_base}.pdf")
plt.close()
