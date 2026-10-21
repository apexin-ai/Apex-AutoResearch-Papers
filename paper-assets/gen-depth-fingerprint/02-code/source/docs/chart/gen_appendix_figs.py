"""Generate appendix visualization figures from paper table data."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
})

# ── Figure 1: Variance Decomposition ──
fig, ax = plt.subplots(figsize=(3.4, 2.4))

features = ['Ent. Mean', 'TTR', 'Hapax', 'Ent. Max', 'Ent. Min', 'Tail Decay', 'Ent. Std']
eta_depth = [0.341, 0.370, 0.364, 0.007, 0.002, 0.002, 0.054]
eta_gen   = [0.022, 0.024, 0.017, 0.002, 0.001, 0.023, 0.020]
eta_int   = [0.010, 0.007, 0.006, 0.003, 0.001, 0.009, 0.011]

x = np.arange(len(features))
w = 0.25

colors_drift = ['#2166AC', '#4393C3', '#92C5DE']
colors_shape = ['#B2182B', '#D6604D', '#F4A582']

bar_colors_depth = ['#2166AC']*3 + ['#D95F02']*3 + ['#7570B3']
bar_colors_gen   = ['#4393C3']*3 + ['#E6AB02']*3 + ['#A6761D']

bars1 = ax.bar(x - w, eta_depth, w, label=r'$\eta^2_{\mathrm{depth}}$',
               color=bar_colors_depth, edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x, eta_gen, w, label=r'$\eta^2_{\mathrm{gen}}$',
               color='#999999', edgecolor='white', linewidth=0.5)
bars3 = ax.bar(x + w, eta_int, w, label=r'$\eta^2_{\mathrm{int}}$',
               color='#CCCCCC', edgecolor='white', linewidth=0.5)

ax.axvline(x=2.5, color='gray', linestyle='--', linewidth=0.6, alpha=0.5)
ax.axvline(x=5.5, color='gray', linestyle='--', linewidth=0.6, alpha=0.5)

ax.text(1.0, 0.39, 'Drifting', ha='center', fontsize=7, fontstyle='italic', color='#2166AC')
ax.text(4.0, 0.39, 'Stationary', ha='center', fontsize=7, fontstyle='italic', color='#D95F02')
ax.text(6.0, 0.39, 'Interm.', ha='center', fontsize=7, fontstyle='italic', color='#7570B3')

ax.set_xticks(x)
ax.set_xticklabels(features, rotation=30, ha='right')
ax.set_ylabel(r'$\eta^2$ (proportion of total SS)')
ax.legend(loc='upper right', framealpha=0.9, edgecolor='gray')
ax.set_ylim(0, 0.44)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('fig_appendix_variance_decomp.pdf')
plt.savefig('fig_appendix_variance_decomp.png')
plt.close()
print("✓ variance decomposition figure")


# ── Figure 2: Decoding Strategy Robustness ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw={'width_ratios': [4, 3]})

# Panel (a): Mean Cohen's d across strategies for all features
features_all = ['ent_mean', 'TTR', 'hapax', 'ent_std', 'ent_max', 'ent_min', 'tail_decay']
labels_all = ['Ent. Mean', 'TTR', 'Hapax', 'Ent. Std', 'Ent. Max', 'Ent. Min', 'Tail Decay']
# Mean values from tables
nucleus_d = [1.09, 0.85, 0.76, 0.46, 0.08, 0.04, 0.13]
greedy_d  = [1.16, 0.85, 0.80, 0.83, 0.06, 0.04, 0.06]
topk_d    = [0.79, 0.63, 0.59, 0.23, 0.10, 0.04, 0.16]

x = np.arange(len(features_all))
w = 0.25

ax1.bar(x - w, nucleus_d, w, label='Nucleus ($p$=0.9)', color='#2166AC', edgecolor='white', linewidth=0.5)
ax1.bar(x,     greedy_d,  w, label='Greedy ($\\tau$=0)', color='#D95F02', edgecolor='white', linewidth=0.5)
ax1.bar(x + w, topk_d,    w, label='Top-$k$ ($k$=50)', color='#7570B3', edgecolor='white', linewidth=0.5)

ax1.axhline(y=0.50, color='gray', linestyle=':', linewidth=0.6, alpha=0.6)
ax1.axhline(y=0.15, color='gray', linestyle=':', linewidth=0.6, alpha=0.6)
ax1.text(6.7, 0.52, '$d$=0.50', fontsize=6.5, color='gray')
ax1.text(6.7, 0.17, '$d$=0.15', fontsize=6.5, color='gray')

ax1.axvline(x=2.5, color='gray', linestyle='--', linewidth=0.6, alpha=0.4)

ax1.set_xticks(x)
ax1.set_xticklabels(labels_all, rotation=30, ha='right')
ax1.set_ylabel("Mean Cohen's $d$ (gen-1 vs. gen-2+)")
ax1.set_title('(a) Mean effect size by feature and strategy', fontsize=9, pad=4)
ax1.legend(loc='upper right', framealpha=0.9, edgecolor='gray', fontsize=7)
ax1.set_ylim(0, 1.35)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Panel (b): Shape features across generators (heatmap-like dot plot)
generators = ['Py-2.8B', 'Py-1B', 'OLMo', 'Qw-0.6B', 'Qw-1.7B', 'Qw-8B', 'Llama', 'Mistral']
strategies = ['Nuc.', 'Gr.', 'Top-$k$']

# Average of shape features (ent_max, ent_min, tail_decay) per generator per strategy
shape_nuc = [np.mean([0.25, 0.03, 0.07]), np.mean([0.21, 0.02, 0.08]),
             np.mean([0.06, 0.07, 0.22]), np.mean([0.01, 0.10, 0.08]),
             np.mean([0.02, 0.05, 0.09]), np.mean([0.04, 0.01, 0.15]),
             np.mean([0.01, 0.01, 0.19]), np.mean([0.00, 0.04, 0.16])]
shape_gr  = [np.mean([0.09, 0.08, 0.07]), np.mean([0.12, 0.04, 0.04]),
             np.mean([0.03, 0.03, 0.03]), np.mean([0.09, 0.02, 0.03]),
             np.mean([0.08, 0.01, 0.04]), np.mean([0.01, 0.06, 0.08]),
             np.mean([0.06, 0.07, 0.04]), np.mean([0.01, 0.02, 0.14])]
shape_topk = [np.mean([0.26, 0.04, 0.12]), np.mean([0.27, 0.04, 0.18]),
              np.mean([0.01, 0.01, 0.22]), np.mean([0.02, 0.10, 0.13]),
              np.mean([0.03, 0.03, 0.14]), np.mean([0.05, 0.07, 0.17]),
              np.mean([0.08, 0.03, 0.20]), np.mean([0.06, 0.01, 0.12])]

y = np.arange(len(generators))
h = 0.25

ax2.barh(y - h, shape_nuc,  h, label='Nucleus', color='#2166AC', edgecolor='white', linewidth=0.5)
ax2.barh(y,     shape_gr,   h, label='Greedy',  color='#D95F02', edgecolor='white', linewidth=0.5)
ax2.barh(y + h, shape_topk, h, label='Top-$k$', color='#7570B3', edgecolor='white', linewidth=0.5)

ax2.axvline(x=0.15, color='red', linestyle=':', linewidth=0.8, alpha=0.6)
ax2.text(0.16, -0.7, 'Stationary\nthreshold', fontsize=6, color='red', alpha=0.7)

ax2.set_yticks(y)
ax2.set_yticklabels(generators)
ax2.set_xlabel("Mean shape-feature $|d|$")
ax2.set_title('(b) Shape stability per generator', fontsize=9, pad=4)
ax2.set_xlim(0, 0.25)
ax2.invert_yaxis()
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('fig_appendix_decoding.pdf')
plt.savefig('fig_appendix_decoding.png')
plt.close()
print("✓ decoding strategy figure")


# ── Figure 3: 9-Generator Scale ──
fig, ax = plt.subplots(figsize=(3.4, 2.8))

gens = ['Pythia-1B', 'Qwen3-0.6B', 'Pythia-2.8B', 'Qwen3-1.7B', 'OLMo-2-1B',
        'Llama-3.2-3B', 'Qwen3-8B', 'Gemma-2-2B', 'Mistral-7B']
f1_3class = [0.857, 0.819, 0.812, 0.811, 0.773, 0.759, 0.696, 0.628, 0.605]
params = [1.0, 0.6, 2.8, 1.7, 1.5, 3.2, 8.2, 2.6, 7.0]

colors = ['#2166AC' if g != 'Gemma-2-2B' else '#D95F02' for g in gens]
y = np.arange(len(gens))

bars = ax.barh(y, f1_3class, color=colors, edgecolor='white', linewidth=0.5, height=0.7)

for i, (f1, p) in enumerate(zip(f1_3class, params)):
    ax.text(f1 + 0.005, i, f'{f1:.3f} ({p}B)', va='center', fontsize=7)

ax.axvline(x=np.mean(f1_3class), color='gray', linestyle='--', linewidth=0.8, alpha=0.6)
ax.text(np.mean(f1_3class) - 0.005, -0.6, f'9-gen avg: {np.mean(f1_3class):.3f}',
        fontsize=6.5, color='gray', va='top', ha='right')

ax.set_yticks(y)
ax.set_yticklabels(gens, fontsize=8)
ax.set_xlabel('3-class LOGO F1')
ax.set_xlim(0.55, 0.93)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#2166AC', label='Original 8 generators'),
                   Patch(facecolor='#D95F02', label='Gemma-2-2B (new)')]
ax.legend(handles=legend_elements, loc='lower left', framealpha=0.9,
          edgecolor='gray', fontsize=7)

plt.tight_layout()
plt.savefig('fig_appendix_9gen_scale.pdf')
plt.savefig('fig_appendix_9gen_scale.png')
plt.close()
print("✓ 9-gen scale figure")

print("\nAll figures generated successfully.")
