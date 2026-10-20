import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open("/root/contamcal-irt-calibration/analysis/subset_distribution_results.json") as f:
    results = json.load(f)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Random 300-item Subset vs Full MMLU (N=14,042)", fontsize=13, fontweight='bold', y=1.02)

r = results["random_300"]

# Panel A: Difficulty histogram
ax = axes[0]
d = r["difficulty"]
bin_labels = d["bin_labels"]
x = np.arange(len(bin_labels))
w = 0.35
full_pct = 100 * np.array(d["full_hist"]) / sum(d["full_hist"])
sub_pct = 100 * np.array(d["sub_hist"]) / sum(d["sub_hist"])
bars1 = ax.bar(x - w/2, full_pct, w, label="Full (N=14,042)", color="#4878CF", alpha=0.85, edgecolor='white')
bars2 = ax.bar(x + w/2, sub_pct, w, label="Subset (n=300)", color="#D65F5F", alpha=0.85, edgecolor='white')
ax.set_xticks(x)
ax.set_xticklabels(bin_labels, fontsize=9)
ax.set_ylabel("Percentage (%)", fontsize=10)
ax.set_xlabel("Baseline Accuracy (d=0%)", fontsize=10)
ax.set_title(f"(a) Difficulty Distribution\nKS D={d['ks_stat']:.3f}, p={d['ks_p']:.3f}, Cohen's d={d['cohens_d']:.3f}", fontsize=10)
ax.legend(fontsize=9, loc='upper right')
ax.set_ylim(0, 30)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Panel B: Domain proportions
ax = axes[1]
dm = r["domain"]
domains = sorted(dm["full_pct"].keys())
x = np.arange(len(domains))
full_pct_d = [dm["full_pct"][d] for d in domains]
sub_pct_d = [dm["sub_pct"][d] for d in domains]
ax.bar(x - w/2, full_pct_d, w, label="Full", color="#4878CF", alpha=0.85, edgecolor='white')
ax.bar(x + w/2, sub_pct_d, w, label="Subset", color="#D65F5F", alpha=0.85, edgecolor='white')
ax.set_xticks(x)
ax.set_xticklabels(domains, fontsize=9)
ax.set_ylabel("Percentage (%)", fontsize=10)
ax.set_xlabel("MMLU Domain", fontsize=10)
ax.set_title(f"(b) Domain Distribution\nχ²={dm['chi2']:.2f}, p={dm['chi2_p']:.3f}, Cramér's V={dm['cramers_v']:.3f}", fontsize=10)
ax.legend(fontsize=9, loc='upper right')
ax.set_ylim(0, 45)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
fig_path = "/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.png"
plt.savefig(fig_path, dpi=150, bbox_inches='tight')
plt.savefig(fig_path.replace('.png', '.pdf'), bbox_inches='tight')
print(f"Saved: {fig_path}")
