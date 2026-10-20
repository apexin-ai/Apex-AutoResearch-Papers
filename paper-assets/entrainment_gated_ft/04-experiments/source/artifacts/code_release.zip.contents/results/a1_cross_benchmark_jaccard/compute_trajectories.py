import json
import numpy as np
from itertools import permutations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_DIR = "/root/entrainment_gated_ft/results/a1_cross_benchmark_jaccard"

# ============================================================
# 1. Accuracy data (aggregate) for σ computation
# ============================================================
# Order: [pure, h24-1, h12-1, h6-1, h3-1]
RATIOS = [0.0, 0.04, 0.0769, 0.1429, 0.25]
RATIO_LABELS = ["0%", "4%", "7.7%", "14.3%", "25%"]
VARIANTS = ["pure", "h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_VARIANTS = ["h24-1", "h12-1", "h6-1", "h3-1"]
HYBRID_RATIOS = [0.04, 0.0769, 0.1429, 0.25]

# LAMBADA acc
acc_lambada = {
    "GDN":   [0.5429846691247817, 0.5396856200271687, 0.5336697069668155, 0.5109644867067727, 0.5134872889578886],
    "RetNet":[0.5165922763438774, 0.5152338443625073, 0.5070832524742869, 0.4971861051814477, 0.5032020182418009],
    "HGRN2": [0.48418397050261985, 0.5002910925674364, 0.5030079565301766, 0.5088298078789055, 0.5138754123811372],
}

# HellaSwag acc_norm
acc_hellaswag = {
    "GDN":   [0.6080462059350727, 0.59699263095001, 0.610336586337383, 0.6046604262099183, 0.6030671181039634],
    "RetNet":[0.5798645688109938, 0.5821549492133041, 0.5882294363672576, 0.5852419836685919, 0.5777733519219279],
    "HGRN2": [0.5982871937860984, 0.6025692093208525, 0.6053574985062736, 0.6048595897231627, 0.6026687910774746],
}

# PIQA acc
acc_piqa = {
    "GDN":   [0.7236126224156693, 0.7290533188248096, 0.7257889009793254, 0.7312295973884657, 0.7377584330794341],
    "RetNet":[0.7263329706202394, 0.7236126224156693, 0.7263329706202394, 0.7252448313384113, 0.7290533188248096],
    "HGRN2": [0.73449401523395, 0.736126224156692, 0.7372143634385201, 0.7334058759521219, 0.7301414581066377],
}

# ARC-Easy acc
acc_arceasy = {
    "GDN":   [0.7121212121212122, 0.7091750841750841, 0.6994949494949495, 0.7175925925925926, 0.7083333333333334],
    "RetNet":[0.7129629629629629, 0.7087542087542088, 0.7201178451178452, 0.718013468013468, 0.6961279461279462],
    "HGRN2": [0.7129629629629629, 0.7302188552188552, 0.7331649831649831, 0.7411616161616161, 0.7205387205387206],
}

all_acc = {
    "LAMBADA": acc_lambada,
    "HellaSwag": acc_hellaswag,
    "PIQA": acc_piqa,
    "ARC-Easy": acc_arceasy,
}

# ============================================================
# 2. Compute cross-architecture σ
# ============================================================
sigma_data = {}
for bench, acc_dict in all_acc.items():
    sigmas = []
    for i in range(5):
        vals = [acc_dict[a][i] for a in ["GDN", "RetNet", "HGRN2"]]
        sigmas.append(float(np.std(vals, ddof=0)))
    sigma_data[bench] = sigmas

# Verify LAMBADA against known values
print("=== σ Verification (LAMBADA) ===")
known_sigma = [0.024047, 0.016238, 0.013596, 0.006055, 0.004943]
for i, (comp, known) in enumerate(zip(sigma_data["LAMBADA"], known_sigma)):
    diff = abs(comp - known)
    status = "OK" if diff < 0.001 else "MISMATCH"
    print(f"  {VARIANTS[i]}: computed={comp:.6f}, known={known:.6f}, diff={diff:.6f} [{status}]")

# ============================================================
# 3. Load Jaccard data from existing files
# ============================================================

# --- LAMBADA: from decoupling_data.csv ---
lambada_jaccard = {
    "h24-1": {"J_helped": 0.094523, "J_hurt": 0.087332},
    "h12-1": {"J_helped": 0.09509, "J_hurt": 0.08087},
    "h6-1":  {"J_helped": 0.09223, "J_hurt": 0.098795},
    "h3-1":  {"J_helped": 0.100182, "J_hurt": 0.092811},
}

# --- HellaSwag: from hellaswag_jaccard_analysis.json ---
with open("/root/entrainment_gated_ft/hellaswag_jaccard_analysis.json") as f:
    hs_data = json.load(f)

hellaswag_jaccard = {}
for var in HYBRID_VARIANTS:
    jd = hs_data["jaccard_similarity"][var]
    pairs = list(jd.keys())
    h_vals = [jd[p]["helped_jaccard"] for p in pairs]
    u_vals = [jd[p]["hurt_jaccard"] for p in pairs]
    hellaswag_jaccard[var] = {
        "J_helped": float(np.mean(h_vals)),
        "J_hurt": float(np.mean(u_vals)),
        "pair_details": {p: {"helped": jd[p]["helped_jaccard"], "hurt": jd[p]["hurt_jaccard"]} for p in pairs},
    }

# --- ARC-Easy: from arc_easy_jaccard_analysis.json ---
with open("/root/entrainment_gated_ft/arc_easy_jaccard_analysis.json") as f:
    ae_data = json.load(f)

arceasy_jaccard = {}
for var in HYBRID_VARIANTS:
    jd = ae_data["jaccard_similarity"][var]
    pairs = list(jd.keys())
    h_vals = [jd[p]["helped_jaccard"] for p in pairs]
    u_vals = [jd[p]["hurt_jaccard"] for p in pairs]
    arceasy_jaccard[var] = {
        "J_helped": float(np.mean(h_vals)),
        "J_hurt": float(np.mean(u_vals)),
        "pair_details": {p: {"helped": jd[p]["helped_jaccard"], "hurt": jd[p]["hurt_jaccard"]} for p in pairs},
    }

# --- PIQA: from piqa_jaccard_analysis.json ---
with open("/root/entrainment_gated_ft/lm_eval_clean/analysis/piqa_jaccard_analysis.json") as f:
    piqa_data = json.load(f)

piqa_jaccard = {}
for var in HYBRID_VARIANTS:
    jd = piqa_data["jaccard_analysis"][var]
    pairs = list(jd.keys())
    h_vals = [jd[p]["helped"]["J"] for p in pairs]
    u_vals = [jd[p]["hurt"]["J"] for p in pairs]
    piqa_jaccard[var] = {
        "J_helped": float(np.mean(h_vals)),
        "J_hurt": float(np.mean(u_vals)),
        "pair_details": {p: {"helped": jd[p]["helped"]["J"], "hurt": jd[p]["hurt"]["J"]} for p in pairs},
    }

all_jaccard = {
    "LAMBADA": lambada_jaccard,
    "HellaSwag": hellaswag_jaccard,
    "PIQA": piqa_jaccard,
    "ARC-Easy": arceasy_jaccard,
}

# Print Jaccard trajectories
print("\n=== Mean Pairwise Jaccard Trajectories ===")
for bench in ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]:
    jd = all_jaccard[bench]
    print(f"\n{bench}:")
    print(f"  {'ratio':>8s}  {'J_helped':>10s}  {'J_hurt':>10s}  {'J_mean':>10s}")
    for var in HYBRID_VARIANTS:
        j = jd[var]
        j_mean = (j["J_helped"] + j["J_hurt"]) / 2
        print(f"  {var:>8s}  {j['J_helped']:>10.4f}  {j['J_hurt']:>10.4f}  {j_mean:>10.4f}")

# ============================================================
# 4. Statistical tests: Spearman ρ + exact permutation (n=4)
# ============================================================

def spearman_rho(x, y):
    from scipy.stats import rankdata
    rx = rankdata(x)
    ry = rankdata(y)
    n = len(x)
    d2 = np.sum((rx - ry) ** 2)
    return 1 - 6 * d2 / (n * (n**2 - 1))

def exact_permutation_test(x, y):
    n = len(x)
    observed = spearman_rho(x, y)
    count_extreme = 0
    total = 0
    for perm in permutations(range(n)):
        y_perm = [y[i] for i in perm]
        rho_perm = spearman_rho(x, y_perm)
        if abs(rho_perm) >= abs(observed):
            count_extreme += 1
        total += 1
    return observed, count_extreme / total, total

print("\n=== Statistical Tests ===")
rank_x = list(range(1, 5))  # attention ratio rank: 1=h24-1, 2=h12-1, 3=h6-1, 4=h3-1

stats_results = {}
for bench in ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]:
    jd = all_jaccard[bench]
    j_helped = [jd[v]["J_helped"] for v in HYBRID_VARIANTS]
    j_hurt = [jd[v]["J_hurt"] for v in HYBRID_VARIANTS]
    j_mean = [(h + u) / 2 for h, u in zip(j_helped, j_hurt)]
    
    # Spearman with mean Jaccard
    rho_mean, p_mean, n_perms = exact_permutation_test(rank_x, j_mean)
    rho_helped, p_helped, _ = exact_permutation_test(rank_x, j_helped)
    rho_hurt, p_hurt, _ = exact_permutation_test(rank_x, j_hurt)
    
    # σ trajectory Spearman (5 points, all ratios)
    from scipy.stats import spearmanr
    rho_sigma, p_sigma = spearmanr(RATIOS, sigma_data[bench])
    
    stats_results[bench] = {
        "jaccard_mean_rho": rho_mean, "jaccard_mean_p": p_mean,
        "jaccard_helped_rho": rho_helped, "jaccard_helped_p": p_helped,
        "jaccard_hurt_rho": rho_hurt, "jaccard_hurt_p": p_hurt,
        "sigma_rho": float(rho_sigma), "sigma_p": float(p_sigma),
        "n_permutations": n_perms,
    }
    
    print(f"\n{bench}:")
    print(f"  σ trajectory:     ρ={rho_sigma:.4f}, p={p_sigma:.4f}")
    print(f"  J_mean trajectory: ρ={rho_mean:.4f}, p={p_mean:.4f} (exact, {n_perms} perms)")
    print(f"  J_helped:          ρ={rho_helped:.4f}, p={p_helped:.4f}")
    print(f"  J_hurt:            ρ={rho_hurt:.4f}, p={p_hurt:.4f}")

# ============================================================
# 5. Build comprehensive output JSON
# ============================================================
output = {
    "description": "Cross-benchmark Jaccard trajectory analysis (A1)",
    "benchmarks": ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"],
    "attention_ratios": RATIOS,
    "ratio_labels": RATIO_LABELS,
    "variants": VARIANTS,
    "metrics_used": {
        "LAMBADA": "acc",
        "HellaSwag": "acc_norm",
        "PIQA": "acc",
        "ARC-Easy": "acc",
    },
    "sigma_trajectories": {},
    "jaccard_trajectories": {},
    "statistics": stats_results,
}

for bench in ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]:
    output["sigma_trajectories"][bench] = {
        v: sigma_data[bench][i] for i, v in enumerate(VARIANTS)
    }
    jd = all_jaccard[bench]
    output["jaccard_trajectories"][bench] = {}
    for var in HYBRID_VARIANTS:
        j = jd[var]
        entry = {"J_helped": j["J_helped"], "J_hurt": j["J_hurt"], "J_mean": (j["J_helped"] + j["J_hurt"]) / 2}
        if "pair_details" in j:
            entry["pair_details"] = j["pair_details"]
        output["jaccard_trajectories"][bench][var] = entry

with open(f"{OUT_DIR}/cross_benchmark_jaccard_trajectories.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {OUT_DIR}/cross_benchmark_jaccard_trajectories.json")

# ============================================================
# 6. Generate 4-panel figure
# ============================================================
plt.rcParams.update({
    'font.size': 13,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
})

fig, axes = plt.subplots(1, 4, figsize=(20, 4.5))
benchmarks = ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]
bench_titles = ["LAMBADA", "HellaSwag (acc_norm)", "PIQA", "ARC-Easy"]

color_sigma = '#2166ac'
color_j_helped = '#b2182b'
color_j_hurt = '#ef8a62'
color_j_mean = '#d6604d'

for idx, (bench, title) in enumerate(zip(benchmarks, bench_titles)):
    ax1 = axes[idx]
    ax2 = ax1.twinx()
    
    # σ trajectory (5 points)
    sigmas = sigma_data[bench]
    l1, = ax1.plot(RATIOS, sigmas, 'o-', color=color_sigma, linewidth=2, markersize=7,
                   label=r'$\sigma$ (cross-arch)', zorder=3)
    
    # Jaccard trajectories (4 points, no pure)
    jd = all_jaccard[bench]
    j_helped = [jd[v]["J_helped"] for v in HYBRID_VARIANTS]
    j_hurt = [jd[v]["J_hurt"] for v in HYBRID_VARIANTS]
    j_mean = [(h + u) / 2 for h, u in zip(j_helped, j_hurt)]
    
    l2, = ax2.plot(HYBRID_RATIOS, j_helped, 's--', color=color_j_helped, linewidth=1.5,
                   markersize=6, label='J(helped)', zorder=2)
    l3, = ax2.plot(HYBRID_RATIOS, j_hurt, 'D--', color=color_j_hurt, linewidth=1.5,
                   markersize=6, label='J(hurt)', zorder=2)
    
    ax1.set_xlabel('Attention ratio')
    ax1.set_xticks(RATIOS)
    ax1.set_xticklabels(RATIO_LABELS, rotation=30, ha='right')
    
    if idx == 0:
        ax1.set_ylabel(r'Cross-arch $\sigma$', color=color_sigma)
    ax1.tick_params(axis='y', labelcolor=color_sigma)
    
    if idx == 3:
        ax2.set_ylabel('Mean pairwise Jaccard', color=color_j_helped)
    ax2.tick_params(axis='y', labelcolor=color_j_helped)
    
    # Add statistics annotation
    st = stats_results[bench]
    rho_s = st["sigma_rho"]
    p_s = st["sigma_p"]
    rho_j = st["jaccard_mean_rho"]
    p_j = st["jaccard_mean_p"]
    
    ann_text = (f'$\\sigma$: $\\rho$={rho_s:.2f}, p={p_s:.3f}\n'
                f'J: $\\rho$={rho_j:.2f}, p={p_j:.3f}')
    ax1.text(0.05, 0.95, ann_text, transform=ax1.transAxes,
             verticalalignment='top', fontsize=10,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.7))
    
    ax1.set_title(title, fontsize=13, fontweight='bold')
    
    # Unified y limits per panel
    sigma_range = max(sigmas) - min(sigmas)
    ax1.set_ylim(min(sigmas) - sigma_range * 0.3, max(sigmas) + sigma_range * 0.3)
    
    all_j = j_helped + j_hurt
    j_range = max(all_j) - min(all_j)
    if j_range < 0.01:
        j_range = 0.02
    ax2.set_ylim(min(all_j) - j_range * 0.5, max(all_j) + j_range * 0.5)
    
    if idx == 0:
        lines = [l1, l2, l3]
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='lower left', fontsize=9, framealpha=0.8)

plt.tight_layout()
fig.savefig(f"{OUT_DIR}/fig_cross_benchmark_decoupling.pdf", bbox_inches='tight', dpi=150)
fig.savefig(f"{OUT_DIR}/fig_cross_benchmark_decoupling.png", bbox_inches='tight', dpi=150)
print(f"Saved: {OUT_DIR}/fig_cross_benchmark_decoupling.pdf")
print(f"Saved: {OUT_DIR}/fig_cross_benchmark_decoupling.png")

# ============================================================
# 7. Summary table
# ============================================================
print("\n=== Summary Table ===")
print(f"{'Benchmark':>12s} | {'σ_pure':>8s} {'σ_h3-1':>8s} {'σ_reduction':>12s} | {'J_helped range':>16s} {'J_hurt range':>16s} | {'σ_ρ':>6s} {'σ_p':>8s} {'J_ρ':>6s} {'J_p':>8s}")
print("-" * 120)
for bench in benchmarks:
    s = sigma_data[bench]
    jd = all_jaccard[bench]
    jh = [jd[v]["J_helped"] for v in HYBRID_VARIANTS]
    ju = [jd[v]["J_hurt"] for v in HYBRID_VARIANTS]
    st = stats_results[bench]
    reduction = (1 - s[4] / s[0]) * 100
    print(f"{bench:>12s} | {s[0]:.6f} {s[4]:.6f} {reduction:>10.1f}% | [{min(jh):.4f}, {max(jh):.4f}] [{min(ju):.4f}, {max(ju):.4f}] | {st['sigma_rho']:>6.2f} {st['sigma_p']:>8.4f} {st['jaccard_mean_rho']:>6.2f} {st['jaccard_mean_p']:>8.4f}")

print("\nDone.")
