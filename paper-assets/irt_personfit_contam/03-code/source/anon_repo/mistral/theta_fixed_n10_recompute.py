#!/usr/bin/env python3
"""
Theta-fixed lz* recomputation for Mistral with n=10 theta values.
Uses Snijders (2001) corrected lz* from person_fit.py.
"""
import csv, json, os, sys
import numpy as np

import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))
from person_fit import prob_4pl, compute_lz_star, estimate_theta_mle

BASE_DIR = "/path/to/project/mistral"
PARAMS_PATH = os.path.join(BASE_DIR, "mmlu_params.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# Load IRT params
a_list, b_list, c_list, d_list = [], [], [], []
with open(PARAMS_PATH) as f:
    reader = csv.DictReader(f)
    for row in reader:
        a_list.append(float(row["a_discrimination"]))
        b_list.append(float(row["b_difficulty"]))
        c_list.append(float(row["c_guessing"]))
        d_list.append(float(row["d_feasibility"]))

a = np.array(a_list)
b = np.array(b_list)
c = np.array(c_list)
d = np.array(d_list)
print(f"Loaded {len(a)} item parameters")

# All 10 clean theta_MLE values (exact)
ALL_THETA_MLE = {
    "clean":    -1.156850591775037,
    "clean_s2": -0.9626744673285949,
    "clean_s3": -0.9732527128586036,
    "clean_s4": -1.1693425305195067,
    "clean_s5": -1.1000473156072956,
    "clean_s6": -1.1405402100357416,
    "clean_s7": -1.0754882493879583,
    "clean_s8": -1.1456500811085557,
    "clean_s9": -1.1240254419150628,
    "clean_s10": -1.0285903748976144,
}

all_thetas = list(ALL_THETA_MLE.values())
theta_fixed_n10 = np.mean(all_thetas)
print(f"\nAll 10 theta_MLE values:")
for k, v in ALL_THETA_MLE.items():
    print(f"  {k}: {v:.6f}")
print(f"\ntheta_fixed_n10 = {theta_fixed_n10:.6f}")
print(f"theta_fixed_n6  = -1.065174 (old)")

# Load available result files (6 clean + 2 contam)
available_clean = ["clean", "clean_s2", "clean_s3", "clean_s8", "clean_s9", "clean_s10"]
contam_conditions = ["contam_15", "contam_50"]

results = {}
for cond in available_clean + contam_conditions:
    fpath = os.path.join(RESULTS_DIR, f"{cond}_results.json")
    with open(fpath) as f:
        data = json.load(f)
    rv = np.array(data["response_vector"], dtype=np.float64)
    theta_free = data["theta_mle"]
    
    lz_free_verify = compute_lz_star(rv, theta_free, a, b, c, d)
    lz_fixed = compute_lz_star(rv, theta_fixed_n10, a, b, c, d)

    results[cond] = {
        "theta_free": theta_free,
        "lz_star_free": float(lz_free_verify),
        "lz_star_fixed": float(lz_fixed),
    }
    
    print(f"\n{cond}: theta_free={theta_free:.4f}, lz*_free={lz_free_verify:.4f}, lz*_fixed={lz_fixed:.4f}")

# Clean stats
clean_lz_fixed = [results[c]["lz_star_fixed"] for c in available_clean]
clean_mean = np.mean(clean_lz_fixed)
clean_std = np.std(clean_lz_fixed, ddof=1)

print(f"\n{'='*60}")
print(f"CLEAN LZ*_FIXED (6 response vectors, theta from 10 seeds):")
for c in available_clean:
    print(f"  {c}: {results[c]['lz_star_fixed']:.4f}")
print(f"  mean = {clean_mean:.6f}")
print(f"  std  = {clean_std:.6f}")

# Bootstrap Cohen's d
def bootstrap_cohens_d(contam_val, clean_vals, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(clean_vals)
    ds = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        boot_clean = [clean_vals[i] for i in idx]
        m = np.mean(boot_clean)
        s = np.std(boot_clean, ddof=1)
        if s > 1e-10:
            ds.append((m - contam_val) / s)  # positive = contam deviates from clean
    ds = np.array(ds)
    return np.percentile(ds, 2.5), np.median(ds), np.percentile(ds, 97.5)

print(f"\n{'='*60}")
print("COHEN'S D (positive = contam deviates from clean):")
for cond in contam_conditions:
    contam_fixed = results[cond]["lz_star_fixed"]
    d_point = (clean_mean - contam_fixed) / clean_std
    ci_lo, d_median, ci_hi = bootstrap_cohens_d(contam_fixed, clean_lz_fixed)
    
    print(f"\n{cond}:")
    print(f"  lz*_fixed = {contam_fixed:.4f}")
    print(f"  d_point   = {d_point:.2f}")
    print(f"  d_median  = {d_median:.2f}")
    print(f"  95% CI    = [{ci_lo:.2f}, {ci_hi:.2f}]")

# Comparison with old n=6
print(f"\n{'='*60}")
print("COMPARISON (old n=6 vs new):")
print(f"  theta_fixed: -1.0652 → {theta_fixed_n10:.4f}")
print(f"")
print(f"  contam_15 d: 2.59 [1.45, 9.00] → see above")
print(f"  contam_50 d: 5.60 [3.71, 18.16] → see above")
print(f"\nNOTE: Cohen's d denominator uses 6 clean seeds (s4-s7 response vectors lost with server 19912)")

# Save
output = {
    "n_theta_seeds": 10,
    "n_rv_seeds": 6,
    "theta_fixed_n10": float(theta_fixed_n10),
    "theta_fixed_n6_old": -1.065173944980578,
    "all_theta_mle": {k: float(v) for k, v in ALL_THETA_MLE.items()},
    "clean_lz_star_fixed": {c: results[c]["lz_star_fixed"] for c in available_clean},
    "clean_lz_star_fixed_mean": float(clean_mean),
    "clean_lz_star_fixed_std": float(clean_std),
}
for cond in contam_conditions:
    contam_fixed = results[cond]["lz_star_fixed"]
    d_point = (clean_mean - contam_fixed) / clean_std
    ci_lo, d_median, ci_hi = bootstrap_cohens_d(contam_fixed, clean_lz_fixed)
    output[cond] = {
        "lz_star_fixed": results[cond]["lz_star_fixed"],
        "lz_star_free": results[cond]["lz_star_free"],
        "theta_mle": results[cond]["theta_free"],
        "cohens_d_point": float(d_point),
        "cohens_d_bootstrap_median": float(d_median),
        "cohens_d_95ci_lo": float(ci_lo),
        "cohens_d_95ci_hi": float(ci_hi),
    }

out_path = os.path.join(RESULTS_DIR, "theta_fixed_n10_recompute.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
