"""Regenerate Figures 19 (decoding strategy) and 20 (9-gen scale) with refined palette."""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
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
    'axes.spines.top': False,
    'axes.spines.right': False,
    'mathtext.fontset': 'cm',
})

# Sophisticated academic palette (Nature/Lancet-inspired)
C1 = '#3C5488'  # deep slate blue
C2 = '#00A087'  # emerald teal
C3 = '#E8B960'  # warm gold
C_ACCENT = '#E76F51'  # terracotta accent


# ━━━━━━━━━━ Figure 19: Decoding Strategy Robustness ━━━━━━━━━━
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 3.0), gridspec_kw={'width_ratios': [4, 3]})

features_all = ['ent_mean', 'TTR', 'hapax', 'ent_std', 'ent_max', 'ent_min', 'tail_decay']
labels_all = ['Ent. Mean', 'TTR', 'Hapax', 'Ent. Std', 'Ent. Max', 'Ent. Min', 'Tail Decay']

nucleus_d = [1.09, 0.85, 0.76, 0.46, 0.08, 0.04, 0.13]
greedy_d  = [1.16, 0.85, 0.80, 0.83, 0.06, 0.04, 0.06]
topk_d    = [0.79, 0.63, 0.59, 0.23, 0.10, 0.04, 0.16]

x = np.arange(len(features_all))
w = 0.25

ax1.bar(x - w, nucleus_d, w, label='Nucleus ($p$=0.9)', color=C1, edgecolor='white', linewidth=0.5)
ax1.bar(x,     greedy_d,  w, label='Greedy ($\\tau$=0)', color=C2, edgecolor='white', linewidth=0.5)
ax1.bar(x + w, topk_d,    w, label='Top-$k$ ($k$=50)', color=C3, edgecolor='white', linewidth=0.5)

ax1.axhline(y=0.50, color='#999999', linestyle=':', linewidth=0.6, alpha=0.6)
ax1.axhline(y=0.15, color='#999999', linestyle=':', linewidth=0.6, alpha=0.6)
ax1.text(6.7, 0.52, '$d$=0.50', fontsize=6.5, color='#777777')
ax1.text(6.7, 0.17, '$d$=0.15', fontsize=6.5, color='#777777')

ax1.axvline(x=2.5, color='#AAAAAA', linestyle='--', linewidth=0.6, alpha=0.4)

ax1.set_xticks(x)
ax1.set_xticklabels(labels_all, rotation=30, ha='right')
ax1.set_ylabel("Mean Cohen's $d$ (gen-1 vs. gen-2+)")
ax1.set_title('(a) Mean effect size by feature and strategy', fontsize=9, pad=4)
ax1.legend(loc='upper right', framealpha=0.9, edgecolor='#CCCCCC', fontsize=7)
ax1.set_ylim(0, 1.35)

# Panel (b): Shape features across generators
generators = ['Py-2.8B', 'Py-1B', 'OLMo', 'Qw-0.6B', 'Qw-1.7B', 'Qw-8B', 'Llama', 'Mistral']

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

ax2.barh(y - h, shape_nuc,  h, label='Nucleus', color=C1, edgecolor='white', linewidth=0.5)
ax2.barh(y,     shape_gr,   h, label='Greedy',  color=C2, edgecolor='white', linewidth=0.5)
ax2.barh(y + h, shape_topk, h, label='Top-$k$', color=C3, edgecolor='white', linewidth=0.5)

ax2.axvline(x=0.15, color='#C0392B', linestyle=':', linewidth=0.8, alpha=0.5)
ax2.text(0.16, -0.7, 'Stationary\nthreshold', fontsize=6, color='#C0392B', alpha=0.6)

ax2.set_yticks(y)
ax2.set_yticklabels(generators)
ax2.set_xlabel("Mean shape-feature $|d|$")
ax2.set_title('(b) Shape stability per generator', fontsize=9, pad=4)
ax2.set_xlim(0, 0.25)
ax2.invert_yaxis()

plt.tight_layout()
plt.savefig('fig_appendix_decoding.pdf')
plt.savefig('fig_appendix_decoding.png')
plt.close()
print("OK fig_appendix_decoding")


# ━━━━━━━━━━ Figure 20: 9-Generator Scale ━━━━━━━━━━
fig, ax = plt.subplots(figsize=(3.4, 2.8))

gens = ['Pythia-1B', 'Qwen3-0.6B', 'Pythia-2.8B', 'Qwen3-1.7B', 'OLMo-2-1B',
        'Llama-3.2-3B', 'Qwen3-8B', 'Gemma-2-2B', 'Mistral-7B']
f1_3class = [0.857, 0.819, 0.812, 0.811, 0.773, 0.759, 0.696, 0.628, 0.605]
params = [1.0, 0.6, 2.8, 1.7, 1.5, 3.2, 8.2, 2.6, 7.0]

colors = [C1 if g != 'Gemma-2-2B' else C2 for g in gens]
y = np.arange(len(gens))

bars = ax.barh(y, f1_3class, color=colors, edgecolor='white', linewidth=0.5, height=0.7)

for i, (f1, p) in enumerate(zip(f1_3class, params)):
    ax.text(f1 + 0.005, i, f'{f1:.3f} ({p}B)', va='center', fontsize=7)

ax.axvline(x=np.mean(f1_3class), color='#999999', linestyle='--', linewidth=0.8, alpha=0.6)
ax.text(np.mean(f1_3class) + 0.005, -0.85, f'9-gen avg: {np.mean(f1_3class):.3f}',
        fontsize=6.5, color='#333333', va='top', ha='left')

ax.set_yticks(y)
ax.set_yticklabels(gens, fontsize=8)
ax.set_xlabel('3-class LOGO F1')
ax.set_xlim(0.55, 0.98)
ax.invert_yaxis()

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=C1, label='Original 8 gen.'),
                   Patch(facecolor=C2, label='Gemma-2-2B (new)')]
ax.legend(handles=legend_elements, loc='lower right', frameon=False, fontsize=7)

plt.tight_layout()
plt.savefig('fig_appendix_9gen_scale.pdf')
plt.savefig('fig_appendix_9gen_scale.png')
plt.close()
print("OK fig_appendix_9gen_scale")

print("\nAll figures regenerated.")
