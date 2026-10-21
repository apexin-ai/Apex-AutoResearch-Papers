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

COL_BLUE = '#0072B2'
COL_ORANGE = '#E69F00'
COL_GRAY = '#999999'
COL_LIGHT_BLUE = '#56B4E9'
COL_DARK_BLUE = '#0072B2'

OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(8, 3.5),
                                  gridspec_kw={'width_ratios': [1, 1.1]})

# === Panel (a): Effect Magnitude Decomposition ===
components = ['Predictor\nEffect', 'SPON\nCorrection', 'Cross-layer\nInteraction']
values = [482.65, 76.20, 147.74]
colors = [COL_BLUE, COL_ORANGE, COL_GRAY]

bars_a = ax_a.bar(range(3), values, color=colors, width=0.6, edgecolor='white', linewidth=0.5)

for bar, val in zip(bars_a, values):
    ax_a.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 12,
              f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

mid_x = (bars_a[0].get_x() + bars_a[0].get_width() / 2 +
          bars_a[1].get_x() + bars_a[1].get_width() / 2) / 2
mid_y = max(values[0], values[1]) * 0.55
ax_a.annotate('', xy=(bars_a[1].get_x() + bars_a[1].get_width() / 2, values[1] + 30),
              xytext=(bars_a[0].get_x() + bars_a[0].get_width() / 2, values[0] - 30),
              arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.2,
                              connectionstyle='arc3,rad=-0.2'))
ax_a.text(mid_x, mid_y, '6.3×', ha='center', va='center', fontsize=11,
          fontweight='bold', color='#333333',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc', alpha=0.9))

ax_a.text(0.97, 0.97, 'cos_sim = 0.196\nmag_ratio = 15.8%',
          transform=ax_a.transAxes, ha='right', va='top', fontsize=9,
          bbox=dict(boxstyle='round,pad=0.3', facecolor='#f7f7f7', edgecolor='#cccccc', alpha=0.9))

ax_a.set_xticks(range(3))
ax_a.set_xticklabels(components)
ax_a.set_ylabel('L2 Norm of Logit-Space Effect')
ax_a.set_ylim(0, 570)
ax_a.text(-0.12, 1.05, '(a)', transform=ax_a.transAxes, fontsize=13, fontweight='bold')

# === Panel (b): PPL Recovery ===
groups = ['Per-token\nSparse', 'TEAL']
no_spon = [9.22, 12.08]
with_spon = [8.99, 11.79]
recovery_pct = [7.3, 4.8]

x = np.arange(len(groups))
bar_w = 0.30

bars_no = ax_b.bar(x - bar_w / 2, no_spon, bar_w, color=COL_LIGHT_BLUE, label='No SPON',
                   edgecolor='white', linewidth=0.5)
bars_yes = ax_b.bar(x + bar_w / 2, with_spon, bar_w, color=COL_DARK_BLUE, label='With SPON',
                    edgecolor='white', linewidth=0.5)

for bar, val in zip(bars_no, no_spon):
    ax_b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08,
              f'{val:.2f}', ha='center', va='bottom', fontsize=9)
for bar, val in zip(bars_yes, with_spon):
    ax_b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08,
              f'{val:.2f}', ha='center', va='bottom', fontsize=9)

for i, pct in enumerate(recovery_pct):
    top = max(no_spon[i], with_spon[i]) + 0.55
    ax_b.annotate(f'{pct}% recovery', xy=(x[i], top),
                  ha='center', va='bottom', fontsize=9, color='#D55E00', fontweight='bold')

ax_b.set_xticks(x)
ax_b.set_xticklabels(groups)
ax_b.set_ylabel('WikiText-2 Perplexity')
y_lo = min(min(no_spon), min(with_spon)) - 1.0
y_hi = max(max(no_spon), max(with_spon)) + 1.5
ax_b.set_ylim(y_lo, y_hi)
ax_b.legend(loc='upper left', framealpha=0.9)
ax_b.text(-0.12, 1.05, '(b)', transform=ax_b.transAxes, fontsize=13, fontweight='bold')

plt.tight_layout(w_pad=2.5)

pdf_path = f'{OUT_DIR}/fig3_subsumption.pdf'
png_path = f'{OUT_DIR}/fig3_subsumption.png'
plt.savefig(pdf_path)
plt.savefig(png_path)
plt.close()

print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
