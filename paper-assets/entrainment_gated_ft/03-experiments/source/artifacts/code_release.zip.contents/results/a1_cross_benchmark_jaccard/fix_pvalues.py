import json
import numpy as np
from itertools import permutations

def spearman_rho(x, y):
    from scipy.stats import rankdata
    rx = rankdata(x)
    ry = rankdata(y)
    n = len(x)
    d2 = np.sum((rx - ry) ** 2)
    return 1 - 6 * d2 / (n * (n**2 - 1))

def exact_permutation_test_sigma(x, y):
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

OUT_DIR = "/root/entrainment_gated_ft/results/a1_cross_benchmark_jaccard"
with open(f"{OUT_DIR}/cross_benchmark_jaccard_trajectories.json") as f:
    data = json.load(f)

RATIOS = [0.0, 0.04, 0.0769, 0.1429, 0.25]
benchmarks = ["LAMBADA", "HellaSwag", "PIQA", "ARC-Easy"]

print("=== Fixed σ Spearman (exact permutation, n=5, 120 perms) ===")
for bench in benchmarks:
    sigmas = [data["sigma_trajectories"][bench][v] for v in data["variants"]]
    rho, p, n_perms = exact_permutation_test_sigma(RATIOS, sigmas)
    data["statistics"][bench]["sigma_rho"] = float(rho)
    data["statistics"][bench]["sigma_p"] = float(p)
    data["statistics"][bench]["sigma_n_permutations"] = n_perms
    print(f"  {bench}: ρ={rho:.4f}, p={p:.4f} ({n_perms} perms)")

with open(f"{OUT_DIR}/cross_benchmark_jaccard_trajectories.json", "w") as f:
    json.dump(data, f, indent=2)
print("\nJSON updated.")
