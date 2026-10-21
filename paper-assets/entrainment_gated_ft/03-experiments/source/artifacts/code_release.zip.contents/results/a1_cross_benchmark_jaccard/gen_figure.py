import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_DIR = "/root/entrainment_gated_ft/results/a1_cross_benchmark_jaccard"
with open(f"{OUT_DIR}/cross_benchmark_jaccard_trajectories.json") as f:
    data = json.load(f)

RATIOS = data["attention_ratios"]
RATIO_LABELS = data["ratio_labels"]
VARIANTS = data["variants"]
HYBRID_VARIANTS = ["h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_RATIOS = RATIOS[1:]

plt.rcParams.update({
    'font.size': 13,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 11,
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
})

fig, axes = plt.subplots(1, 4, figsize=(20, 4.8))
benchmarks = ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]
bench_titles = ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]

color_sigma = '#2166ac'
color_j_helped = '#b2182b'
color_j_hurt = '#ef8a62'

for idx, bench in enumerate(benchmarks):
    ax1 = axes[idx]
    ax2 = ax1.twinx()
    
    sigmas = [data["sigma_trajectories"][bench][v] for v in VARIANTS]
    l1, = ax1.plot(RATIOS, sigmas, 'o-', color=color_sigma, linewidth=2.2, markersize=7,
                   label=r'$\sigma$ (cross-arch)', zorder=3)
    
    jd = data["jaccard_trajectories"][bench]
    j_helped = [jd[v]["J_helped"] for v in HYBRID_VARIANTS]
    j_hurt = [jd[v]["J_hurt"] for v in HYBRID_VARIANTS]
    
    l2, = ax2.plot(HYBRID_RATIOS, j_helped, 's--', color=color_j_helped, linewidth=1.8,
                   markersize=6, label=r'$\bar{J}$(helped)', zorder=2)
    l3, = ax2.plot(HYBRID_RATIOS, j_hurt, 'D--', color=color_j_hurt, linewidth=1.8,
                   markersize=6, label=r'$\bar{J}$(hurt)', zorder=2)
    
    ax1.set_xlabel('Attention ratio')
    ax1.set_xticks(RATIOS)
    ax1.set_xticklabels(RATIO_LABELS, rotation=30, ha='right')
    
    if idx == 0:
        ax1.set_ylabel(r'Cross-arch $\sigma$', color=color_sigma)
    ax1.tick_params(axis='y', labelcolor=color_sigma)
    
    if idx == 3:
        ax2.set_ylabel('Mean pairwise Jaccard', color=color_j_helped)
    ax2.tick_params(axis='y', labelcolor=color_j_helped)
    
    st = data["statistics"][bench]
    rho_s = st["sigma_rho"]
    p_s = st["sigma_p"]
    rho_j = st["jaccard_mean_rho"]
    p_j = st["jaccard_mean_p"]
    
    def fmt_p(p):
        if p < 0.001:
            return "<.001"
        elif p < 0.01:
            return f"={p:.3f}"
        elif p < 0.1:
            return f"={p:.3f}"
        else:
            return f"={p:.2f}"
    
    ann_text = (f'$\\sigma$: $\\rho$={rho_s:.2f}, p{fmt_p(p_s)}\n'
                f'$\\bar{{J}}$: $\\rho$={rho_j:.2f}, p{fmt_p(p_j)}')
    ax1.text(0.05, 0.95, ann_text, transform=ax1.transAxes,
             verticalalignment='top', fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.7))
    
    ax1.set_title(bench_titles[idx], fontsize=13, fontweight='bold')
    
    sigma_range = max(sigmas) - min(sigmas)
    if sigma_range < 0.001:
        sigma_range = 0.005
    ax1.set_ylim(min(sigmas) - sigma_range * 0.3, max(sigmas) + sigma_range * 0.3)
    
    all_j = j_helped + j_hurt
    j_range = max(all_j) - min(all_j)
    if j_range < 0.01:
        j_range = 0.02
    ax2.set_ylim(min(all_j) - j_range * 0.5, max(all_j) + j_range * 0.5)
    
    if idx == 0:
        lines = [l1, l2, l3]
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='lower left', fontsize=9.5, framealpha=0.8)

plt.tight_layout(w_pad=2.5)
fig.savefig(f"{OUT_DIR}/fig_cross_benchmark_decoupling.pdf", bbox_inches='tight', dpi=300)
fig.savefig(f"{OUT_DIR}/fig_cross_benchmark_decoupling.png", bbox_inches='tight', dpi=150)
print(f"Saved PDF and PNG")
