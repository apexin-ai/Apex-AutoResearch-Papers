"""
Majority Vote Ensemble POC + ρ(σ, J) Rank Correlation
Computed from existing per-example analysis artifacts.
"""
import json
import itertools
import math

# ===== Task 1: Majority Vote Ensemble =====

# From formal_multiplicity_metrics.json: disagreement_distribution
# {k}_of_3 = number of examples where exactly k architectures got it correct
benchmarks = {
    "LAMBADA": {
        "N": 5153,
        "h3-1": {"0_of_3": 1768, "1_of_3": 746, "2_of_3": 779, "3_of_3": 1860},
        "pure": {"0_of_3": 1719, "1_of_3": 762, "2_of_3": 818, "3_of_3": 1854},
        "individual_h3_1": {
            "GDN": (2800 - 616 + 461) / 5153,
            "RetNet": (2666 - 497 + 420) / 5153,
            "HGRN2": (2494 - 392 + 548) / 5153,
        },
    },
    "HellaSwag (acc_norm)": {
        "N": 10042,
        "h3-1": {"0_of_3": 3320, "1_of_3": 732, "2_of_3": 779, "3_of_3": 5211},
        "pure": {"0_of_3": 3321, "1_of_3": 736, "2_of_3": 752, "3_of_3": 5233},
        "individual_h3_1": None,  # acc_norm per-arch not directly available
    },
    "ARC-Easy": {
        "N": 2376,
        "h3-1": {"0_of_3": 445, "1_of_3": 245, "2_of_3": 254, "3_of_3": 1432},
        "pure": {"0_of_3": 456, "1_of_3": 194, "2_of_3": 292, "3_of_3": 1434},
        "individual_h3_1": {
            "GDN": (171 + 1512) / 2376,
            "RetNet": (144 + 1510) / 2376,
            "HGRN2": (164 + 1548) / 2376,
        },
    },
    "BoolQ": {
        "N": 3270,
        "h3-1": {"0_of_3": 556, "1_of_3": 644, "2_of_3": 839, "3_of_3": 1231},
        "pure": {"0_of_3": 540, "1_of_3": 752, "2_of_3": 899, "3_of_3": 1079},
        "individual_h3_1": None,
    },
}

print("=" * 70)
print("TASK 1: Majority Vote Ensemble (h3-1, 3 architectures)")
print("=" * 70)

results_mv = {}
for bench, data in benchmarks.items():
    N = data["N"]
    dd = data["h3-1"]

    # Majority vote: correct if >= 2/3 correct
    mv_correct = dd["2_of_3"] + dd["3_of_3"]
    mv_acc = mv_correct / N

    # Mean individual accuracy (from disagreement distribution)
    total_correct = dd["1_of_3"] + 2 * dd["2_of_3"] + 3 * dd["3_of_3"]
    mean_acc = total_correct / (3 * N)

    # Agreement/disagreement
    agreement = (dd["0_of_3"] + dd["3_of_3"]) / N
    disagreement = (dd["1_of_3"] + dd["2_of_3"]) / N

    result = {
        "N": N,
        "majority_vote_acc": round(mv_acc, 4),
        "mean_individual_acc": round(mean_acc, 4),
        "mv_vs_mean_pp": round((mv_acc - mean_acc) * 100, 2),
        "agreement_pct": round(agreement * 100, 2),
        "disagreement_pct": round(disagreement * 100, 2),
        "unanimous_correct": dd["3_of_3"],
        "two_of_three": dd["2_of_3"],
        "one_of_three": dd["1_of_3"],
        "unanimous_wrong": dd["0_of_3"],
    }

    if data["individual_h3_1"]:
        indiv = data["individual_h3_1"]
        best_arch = max(indiv, key=indiv.get)
        best_acc = indiv[best_arch]
        result["individual_accs"] = {k: round(v, 4) for k, v in indiv.items()}
        result["best_single"] = best_arch
        result["best_single_acc"] = round(best_acc, 4)
        result["mv_vs_best_pp"] = round((mv_acc - best_acc) * 100, 2)

    results_mv[bench] = result

    print(f"\n--- {bench} (N={N}) ---")
    if data["individual_h3_1"]:
        for arch, acc in data["individual_h3_1"].items():
            print(f"  {arch:8s}: {acc:.4f} ({acc*100:.2f}%)")
    print(f"  Mean individual: {mean_acc:.4f} ({mean_acc*100:.2f}%)")
    print(f"  Majority vote:   {mv_acc:.4f} ({mv_acc*100:.2f}%)")
    if data["individual_h3_1"]:
        indiv = data["individual_h3_1"]
        best_arch = max(indiv, key=indiv.get)
        best_acc = indiv[best_arch]
        print(f"  Best single ({best_arch}): {best_acc:.4f} ({best_acc*100:.2f}%)")
        print(f"  MV vs best:  {(mv_acc - best_acc)*100:+.2f}pp")
    print(f"  MV vs mean:  {(mv_acc - mean_acc)*100:+.2f}pp")
    print(f"  Agreement:   {agreement*100:.1f}%  (3/3={dd['3_of_3']}, 0/3={dd['0_of_3']})")
    print(f"  Disagreement:{disagreement*100:.1f}%  (2/3={dd['2_of_3']}, 1/3={dd['1_of_3']})")


# ===== Task 2: ρ(σ, J) Rank Correlation =====

print("\n" + "=" * 70)
print("TASK 2: ρ(σ, J) Rank Correlation on LAMBADA")
print("=" * 70)

# From decoupling_data.csv (4 non-zero attention ratios only)
sigma = [0.016238, 0.013596, 0.006055, 0.004943]
j_helped = [0.09452, 0.09509, 0.09223, 0.10018]
j_hurt = [0.08733, 0.08087, 0.09880, 0.09281]
j_mean = [(h + u) / 2 for h, u in zip(j_helped, j_hurt)]
ratios = ["4% (h24-1)", "7.7% (h12-1)", "14.3% (h6-1)", "25% (h3-1)"]

def spearman_rho(x, y):
    n = len(x)
    # Compute ranks (1-based, ascending)
    def ranks(vals):
        sorted_idx = sorted(range(n), key=lambda i: vals[i])
        r = [0] * n
        for rank, idx in enumerate(sorted_idx):
            r[idx] = rank + 1
        return r

    rx = ranks(x)
    ry = ranks(y)
    d_sq = sum((rx[i] - ry[i]) ** 2 for i in range(n))
    rho = 1 - 6 * d_sq / (n * (n**2 - 1))
    return rho, rx, ry, d_sq

def exact_perm_p(x, y, n):
    """Exact two-tailed permutation test for Spearman rho with n items."""
    observed_rho, _, _, _ = spearman_rho(x, y)
    count = 0
    total = 0
    for perm in itertools.permutations(range(n)):
        y_perm = [y[p] for p in perm]
        rho_perm, _, _, _ = spearman_rho(x, y_perm)
        total += 1
        if abs(rho_perm) >= abs(observed_rho) - 1e-10:
            count += 1
    return count / total

# Compute for J_helped
rho_h, rx_h, ry_h, dsq_h = spearman_rho(sigma, j_helped)
p_h = exact_perm_p(sigma, j_helped, 4)

# Compute for J_hurt
rho_u, rx_u, ry_u, dsq_u = spearman_rho(sigma, j_hurt)
p_u = exact_perm_p(sigma, j_hurt, 4)

# Compute for J_mean
rho_m, rx_m, ry_m, dsq_m = spearman_rho(sigma, j_mean)
p_m = exact_perm_p(sigma, j_mean, 4)

print(f"\n{'Ratio':20s} {'σ':>10s} {'J(helped)':>10s} {'J(hurt)':>10s} {'J(mean)':>10s}")
print("-" * 62)
for i in range(4):
    print(f"{ratios[i]:20s} {sigma[i]:10.6f} {j_helped[i]:10.5f} {j_hurt[i]:10.5f} {j_mean[i]:10.5f}")

print(f"\nσ coefficient of variation: {(max(sigma)-min(sigma))/((max(sigma)+min(sigma))/2)*100:.1f}%")
print(f"J(helped) range: [{min(j_helped):.5f}, {max(j_helped):.5f}], CV: {(max(j_helped)-min(j_helped))/((max(j_helped)+min(j_helped))/2)*100:.1f}%")

print(f"\nSpearman ρ(σ, J_helped) = {rho_h:.2f}, p = {p_h:.4f} (exact permutation, two-tailed, n=4)")
print(f"Spearman ρ(σ, J_hurt)  = {rho_u:.2f}, p = {p_u:.4f}")
print(f"Spearman ρ(σ, J_mean)  = {rho_m:.2f}, p = {p_m:.4f}")

# Floor effect refutation
# From jaccard_upper_bound.json
j_max_data = {
    "h24-1": {"J_obs_helped": 0.0946, "J_max_helped": 0.9489, "pct": 10.0},
    "h12-1": {"J_obs_helped": 0.0951, "J_max_helped": 0.8869, "pct": 10.7},
    "h6-1": {"J_obs_helped": 0.0922, "J_max_helped": 0.8370, "pct": 11.0},
    "h3-1": {"J_obs_helped": 0.1002, "J_max_helped": 0.8475, "pct": 11.8},
}

print(f"\n--- Floor Effect Refutation ---")
print(f"{'Ratio':15s} {'J_obs':>8s} {'J_max':>8s} {'J_obs/J_max':>12s} {'Room':>8s}")
print("-" * 53)
for ratio, d in j_max_data.items():
    room = d["J_max_helped"] - d["J_obs_helped"]
    print(f"{ratio:15s} {d['J_obs_helped']:8.4f} {d['J_max_helped']:8.4f} {d['pct']:10.1f}%   {room:8.4f}")

mean_ratio = sum(d["pct"] for d in j_max_data.values()) / 4
print(f"\nMean J_obs/J_max = {mean_ratio:.1f}%")
print("Conclusion: J_obs is only ~11% of J_max across all ratios.")
print("There is ample room for J to increase if helped sets were more aligned.")
print("Low J reflects genuine architecture-specific responses, not a floor effect.")

# ===== Save results =====
output = {
    "task_1_majority_vote": results_mv,
    "task_2_rho_sigma_j": {
        "sigma_values": sigma,
        "j_helped_values": j_helped,
        "j_hurt_values": j_hurt,
        "j_mean_values": j_mean,
        "rho_sigma_j_helped": {"rho": rho_h, "p_exact": p_h},
        "rho_sigma_j_hurt": {"rho": rho_u, "p_exact": p_u},
        "rho_sigma_j_mean": {"rho": rho_m, "p_exact": p_m},
        "sigma_range_pct": round((max(sigma) - min(sigma)) / ((max(sigma) + min(sigma)) / 2) * 100, 1),
        "j_helped_range_pct": round((max(j_helped) - min(j_helped)) / ((max(j_helped) + min(j_helped)) / 2) * 100, 1),
        "floor_effect_refutation": {
            "mean_j_obs_over_j_max_pct": mean_ratio,
            "conclusion": "J_obs is ~11% of theoretical J_max. Low J is genuine architecture specificity, not floor effect."
        }
    }
}

out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/paper_data/majority_vote_and_rho_analysis.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved: {out_path}")
