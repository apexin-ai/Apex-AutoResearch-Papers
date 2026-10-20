"""Generate capability gap scatter plot for §6.

DeBERTa-MNLI primary (6 pts) + LLaMA-8B (1 pt, distinct marker) + multi-verifier (2 pts)
+ fine-tuned DeBERTa (2 pts). All gains at w=3.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import spearmanr, linregress

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

# Primary: DeBERTa-MNLI across model x dataset at w=3
deberta_pts = [
    (-36.76, 0.49, 'Qwen3-14B$_{\\mathrm{think}}$\n(FOLIO)'),
    (-33.82, 0.49, 'Qwen3-14B\n(FOLIO)'),
    (-30.83, 0.50, 'Qwen3-14B\n(PW-D5)'),
    (-19.00, 0.67, 'Qwen2.5-14B\n(PW-D5)'),
    (-6.37,  2.94, 'Mistral-7B\n(FOLIO)'),
    (15.67,  6.67, 'Mistral-7B\n(ProofWriter)'),
]

# LLaMA point (different model family, separate marker)
llama_pt = (-17.50, 0.83, 'LLaMA-8B\n(PW-D5)')

# Secondary: other NLI verifiers on Mistral-7B ProofWriter at w=3
multi_nli = [
    (-1.66, 4.17, 'RoBERTa'),   # 37.67 - 39.33
    (6.84,  5.17, 'BART'),       # 46.17 - 39.33
]

# Fine-tuned DeBERTa on ProofWriter OWA (99.67% standalone), w=3
finetuned_pts = [
    (27.17, 11.67, 'LLaMA-8B'),    # 99.67 - 72.50 (finetuned SC)
    (60.34, 12.67, 'Mistral-7B'),   # 99.67 - 39.33
]

dx = np.array([p[0] for p in deberta_pts])
dy = np.array([p[1] for p in deberta_pts])

# DeBERTa-only (excl. LLaMA) stats
rho_excl, p_excl = spearmanr(dx, dy)
print(f"DeBERTa-only (excl LLaMA) Spearman rho={rho_excl:.3f} (n={len(dx)}, p={p_excl:.4f})")

# All DeBERTa-verifier points (incl. LLaMA)
dx_all = np.append(dx, llama_pt[0])
dy_all = np.append(dy, llama_pt[1])
rho, p_rho = spearmanr(dx_all, dy_all)
print(f"DeBERTa-all (incl LLaMA) Spearman rho={rho:.3f} (n={len(dx_all)}, p={p_rho:.4f})")
slope, intercept, r_value, p_lin, _ = linregress(dx_all, dy_all)
print(f"DeBERTa-all linear: R²={r_value**2:.3f}, p={p_lin:.4f}")

# Sigmoid with Director's parameters as guide
def sigmoid(x, L, k, x0, b):
    return L / (1 + np.exp(-k * (x - x0))) + b

# Use all points for visual fit (DeBERTa + LLaMA + multi-NLI)
all_pts = deberta_pts + [llama_pt] + multi_nli
ax_all = np.array([p[0] for p in all_pts])
ay_all = np.array([p[1] for p in all_pts])

try:
    popt, _ = curve_fit(sigmoid, ax_all, ay_all,
                        p0=[3.5, 0.3, 1.0, 0.2],
                        bounds=([0.5, 0.01, -10, -1], [5.0, 2.0, 15, 2.0]),
                        maxfev=50000)
    x_fit = np.linspace(-42, 68, 500)
    y_sig = sigmoid(x_fit, *popt)
    ss_res = np.sum((ay_all - sigmoid(ax_all, *popt))**2)
    ss_tot = np.sum((ay_all - np.mean(ay_all))**2)
    r2_sig = 1 - ss_res / ss_tot
    inflection = popt[2]
    print(f"Sigmoid ({len(ax_all)}pt): R²={r2_sig:.3f}, inflection={inflection:.1f}pp, L={popt[0]:.2f}, k={popt[1]:.3f}")
    has_sigmoid = True
except Exception as e:
    print(f"Sigmoid fit failed: {e}")
    has_sigmoid = False
    x_fit = np.linspace(-42, 68, 500)

# Plot
fig, ax = plt.subplots(figsize=(3.8, 2.8))
fig.subplots_adjust(left=0.16, bottom=0.20, right=0.96, top=0.94)

# DeBERTa primary points (Mistral/Qwen generators)
ax.scatter(dx, dy, marker='o', c='#2166ac', s=50, zorder=5,
           label='DeBERTa-MNLI', edgecolors='white', linewidths=0.5)

# LLaMA generator (different model family)
ax.scatter([llama_pt[0]], [llama_pt[1]], marker='D', c='#e66101', s=50, zorder=5,
           label='DeBERTa-MNLI (LLaMA)', edgecolors='white', linewidths=0.5)

# Multi-NLI secondary points
mx = [p[0] for p in multi_nli]
my = [p[1] for p in multi_nli]
ml = [p[2] for p in multi_nli]
ax.scatter([mx[0]], [my[0]], marker='s', c='#b2182b', s=40, zorder=5,
           label='RoBERTa-MNLI', edgecolors='white', linewidths=0.5)
ax.scatter([mx[1]], [my[1]], marker='^', c='#4dac26', s=40, zorder=5,
           label='BART-MNLI', edgecolors='white', linewidths=0.5)

# Fine-tuned DeBERTa points
fx = [p[0] for p in finetuned_pts]
fy = [p[1] for p in finetuned_pts]
ax.scatter(fx, fy, marker='*', c='#7b3294', s=100, zorder=6,
           label='Fine-tuned DeBERTa', edgecolors='white', linewidths=0.5)

# Sigmoid curve
if has_sigmoid:
    ax.plot(x_fit, y_sig, '-', color='#555555', linewidth=1.0, alpha=0.6,
            label=f'Sigmoid fit')

# Annotations for DeBERTa points
annot_config = [
    (-36.76, 0.49, 'Qwen3-14B$_{\\mathrm{think}}$\nFOLIO', (6, -3), 'left'),
    (-35.29, 0.49, 'Qwen3-14B\nFOLIO', (6, -15), 'left'),
    (-30.83, 0.50, 'Qwen3-14B\nPW-D5', (6, 3), 'left'),
    (-19.00, 0.67, 'Qwen2.5-14B\nPW-D5', (6, -8), 'left'),
    (-6.37,  2.94, 'Mistral-7B\nFOLIO', (6, -8), 'left'),
    (15.67,  6.67, 'Mistral-7B\nPW-D5', (-6, 5), 'right'),
]
for x, y, lbl, offset, ha in annot_config:
    ax.annotate(lbl, (x, y), textcoords='offset points',
                xytext=offset, fontsize=5.5, ha=ha, color='#444444',
                linespacing=0.9)

# LLaMA annotation (distinct color)
ax.annotate('LLaMA-8B\nPW-D5', (llama_pt[0], llama_pt[1]),
            textcoords='offset points', xytext=(6, -10), fontsize=5.5,
            ha='left', color='#e66101', linespacing=0.9)

# Annotations for multi-NLI
ax.annotate('RoBERTa', (mx[0], my[0]), textcoords='offset points',
            xytext=(5, 5), fontsize=5.5, ha='left', color='#b2182b')
ax.annotate('BART', (mx[1], my[1]), textcoords='offset points',
            xytext=(5, 5), fontsize=5.5, ha='left', color='#4dac26')

# Annotations for fine-tuned
ax.annotate('LLaMA-8B\n(fine-tuned)', (fx[0], fy[0]), textcoords='offset points',
            xytext=(-6, 5), fontsize=5.5, ha='right', color='#7b3294', linespacing=0.9)
ax.annotate('Mistral-7B\n(fine-tuned)', (fx[1], fy[1]), textcoords='offset points',
            xytext=(-6, 5), fontsize=5.5, ha='right', color='#7b3294', linespacing=0.9)

# Reference lines
ax.axhline(0, color='black', linewidth=0.3, alpha=0.2)
ax.axvline(0, color='black', linewidth=0.5, alpha=0.25, linestyle=':')

# Region labels
ax.text(-21, 14.0, 'verifier $<$ generator', fontsize=6.5, color='#aaaaaa',
        ha='center', style='italic')
ax.text(40, 14.0, 'verifier $>$ generator', fontsize=6.5, color='#aaaaaa',
        ha='center', style='italic')

ax.set_xlabel('Capability gap (verifier $-$ generator SC, pp)')
ax.set_ylabel('Combo gain over SC (pp, $w{=}3$)')
ax.set_xlim(-42, 68)
ax.set_ylim(-0.3, 15.0)
ax.legend(loc='lower right', framealpha=0.9, edgecolor='#cccccc',
          borderpad=0.3, handletextpad=0.4, bbox_to_anchor=(1.0, 0.0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# no tight_layout — manual subplots_adjust above
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{outdir}/capability_gap_scatter.pdf')
fig.savefig(f'{outdir}/capability_gap_scatter.png')
print("Saved to", outdir)
