import csv
import json
import os
import numpy as np

BASE_DIR = "/path/to/project/qwen"
PARAMS_PATH = os.path.join(BASE_DIR, "mmlu_params.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
THETA_FIXED = -0.10223831233869138

def load_irt_params(path):
    params = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            idx = int(row["item_idx"])
            params[idx] = {
                "a": float(row["a_discrimination"]),
                "b": float(row["b_difficulty"]),
                "c": float(row["c_guessing"]),
                "d": float(row["d_feasibility"]),
            }
    return params

def irf_4pl(theta, a, b, c, d):
    return c + (d - c) / (1.0 + np.exp(-a * (theta - b)))

def compute_lz_drasgow(responses, irt_params, theta):
    """Drasgow's lz (uncorrected) — matches lz_fixed in theta_fixed_n10_consistent.json"""
    l0 = 0.0
    E_l0 = 0.0
    Var_l0 = 0.0
    for i in range(len(responses)):
        if i not in irt_params:
            continue
        p = irt_params[i]
        a, b, c, d = p["a"], p["b"], p["c"], p["d"]
        P = irf_4pl(theta, a, b, c, d)
        P = np.clip(P, 1e-10, 1.0 - 1e-10)
        Q = 1.0 - P
        x = responses[i]
        log_P = np.log(P)
        log_Q = np.log(Q)
        l0 += x * log_P + (1 - x) * log_Q
        E_l0 += P * log_P + Q * log_Q
        g = log_P - log_Q
        Var_l0 += P * Q * g ** 2
    if Var_l0 < 1e-15:
        return 0.0
    return (l0 - E_l0) / np.sqrt(Var_l0)

def compute_lz_star(responses, irt_params, theta):
    """lz* with Snijders (2001) variance correction"""
    l0 = 0.0
    E_l0 = 0.0
    Var_l0 = 0.0
    I_theta = 0.0
    C_theta = 0.0
    for i in range(len(responses)):
        if i not in irt_params:
            continue
        p = irt_params[i]
        a, b, c, d = p["a"], p["b"], p["c"], p["d"]
        P = irf_4pl(theta, a, b, c, d)
        P = np.clip(P, 1e-10, 1.0 - 1e-10)
        Q = 1.0 - P
        x = responses[i]
        log_P = np.log(P)
        log_Q = np.log(Q)
        l0 += x * log_P + (1 - x) * log_Q
        E_l0 += P * log_P + Q * log_Q
        g = log_P - log_Q
        Var_l0 += P * Q * g ** 2
        z = a * (theta - b)
        sigma = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
        dP = a * (d - c) * sigma * (1.0 - sigma)
        h = dP / (P * Q)
        I_theta += P * Q * h ** 2
        C_theta += P * Q * h * g
    if Var_l0 < 1e-15:
        return 0.0
    Var_star = Var_l0 - C_theta ** 2 / I_theta if I_theta > 1e-15 else Var_l0
    if Var_star <= 0:
        Var_star = Var_l0
    return (l0 - E_l0) / np.sqrt(Var_star)

def bootstrap_cohens_d(contam_val, clean_values, n_boot=10000, seed=42):
    rng = np.random.RandomState(seed)
    clean_arr = np.array(clean_values)
    n = len(clean_arr)
    ds = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        boot = clean_arr[idx]
        d = (contam_val - np.mean(boot)) / np.std(boot, ddof=1)
        ds.append(d)
    ds = np.array(ds)
    return np.percentile(ds, 2.5), np.percentile(ds, 97.5)

# Load IRT params
irt_params = load_irt_params(PARAMS_PATH)
n_items = len(irt_params)

# Conditions to compute
conditions = [
    "contam_15_s3",
    "contam_25",
    "contam_25_s2",
    "contam_25_s3",
    "contam_50_s2",
]

# Also verify clean baseline
clean_conditions = [f"clean_s{i}" for i in range(1, 11)]

# Load clean lz_fixed from existing file for verification
with open(os.path.join(RESULTS_DIR, "theta_fixed_n10_consistent.json")) as f:
    existing = json.load(f)

print(f"theta_fixed = {THETA_FIXED}")
print(f"n_irt_items = {n_items}")
print()

# Compute clean baseline with fixed theta
print("=== CLEAN BASELINE (fixed theta) ===")
clean_lz_fixed = []
clean_lz_star_fixed = []
for cond in clean_conditions:
    fpath = os.path.join(RESULTS_DIR, f"{cond}_results.json")
    with open(fpath) as f:
        data = json.load(f)
    resp = data["response_vector"]
    lz_val = compute_lz_drasgow(resp, irt_params, THETA_FIXED)
    lz_star_val = compute_lz_star(resp, irt_params, THETA_FIXED)
    clean_lz_fixed.append(lz_val)
    clean_lz_star_fixed.append(lz_star_val)
    # Verify against existing
    existing_val = existing["conditions"][cond]["lz_fixed"]
    print(f"  {cond}: lz_fixed={lz_val:.6f} (existing={existing_val:.6f}, diff={abs(lz_val-existing_val):.2e}), lz_star_fixed={lz_star_val:.6f}")

clean_lz_arr = np.array(clean_lz_fixed)
clean_lz_star_arr = np.array(clean_lz_star_fixed)
print(f"\nClean lz_fixed: mean={np.mean(clean_lz_arr):.6f}, std={np.std(clean_lz_arr, ddof=1):.6f}, n={len(clean_lz_arr)}")
print(f"Clean lz_star_fixed: mean={np.mean(clean_lz_star_arr):.6f}, std={np.std(clean_lz_star_arr, ddof=1):.6f}, n={len(clean_lz_star_arr)}")

# Also verify contam_15 s1 and contam_50 s1 (already known d_fixed)
print("\n=== VERIFICATION (already known d_fixed) ===")
for cond, expected_d in [("contam_15", 4.77), ("contam_50", 14.521)]:
    fpath = os.path.join(RESULTS_DIR, f"{cond}_results.json")
    with open(fpath) as f:
        data = json.load(f)
    resp = data["response_vector"]
    lz_val = compute_lz_drasgow(resp, irt_params, THETA_FIXED)
    lz_star_val = compute_lz_star(resp, irt_params, THETA_FIXED)
    d = (lz_val - np.mean(clean_lz_arr)) / np.std(clean_lz_arr, ddof=1)
    d_star = (lz_star_val - np.mean(clean_lz_star_arr)) / np.std(clean_lz_star_arr, ddof=1)
    print(f"  {cond}: lz_fixed={lz_val:.6f}, d_fixed={d:.3f} (expected={expected_d}), lz_star_fixed={lz_star_val:.6f}, d_star_fixed={d_star:.3f}")

# Also verify contam_15_s2 (d_fixed = 7.79)
fpath = os.path.join(RESULTS_DIR, "contam_15_s2_results.json")
with open(fpath) as f:
    data = json.load(f)
resp = data["response_vector"]
lz_val = compute_lz_drasgow(resp, irt_params, THETA_FIXED)
lz_star_val = compute_lz_star(resp, irt_params, THETA_FIXED)
d = (lz_val - np.mean(clean_lz_arr)) / np.std(clean_lz_arr, ddof=1)
print(f"  contam_15_s2: lz_fixed={lz_val:.6f}, d_fixed={d:.3f} (expected=7.79), lz_star_fixed={lz_star_val:.6f}")

# Compute for missing conditions
print("\n=== NEW COMPUTATIONS ===")
results = {}
for cond in conditions:
    fpath = os.path.join(RESULTS_DIR, f"{cond}_results.json")
    if not os.path.exists(fpath):
        print(f"  {cond}: SKIPPED (no results file)")
        continue
    with open(fpath) as f:
        data = json.load(f)
    resp = data["response_vector"]
    lz_val = compute_lz_drasgow(resp, irt_params, THETA_FIXED)
    lz_star_val = compute_lz_star(resp, irt_params, THETA_FIXED)
    d = (lz_val - np.mean(clean_lz_arr)) / np.std(clean_lz_arr, ddof=1)
    d_star = (lz_star_val - np.mean(clean_lz_star_arr)) / np.std(clean_lz_star_arr, ddof=1)
    ci_lo, ci_hi = bootstrap_cohens_d(lz_val, clean_lz_fixed)
    ci_star_lo, ci_star_hi = bootstrap_cohens_d(lz_star_val, clean_lz_star_fixed)
    results[cond] = {
        "lz_fixed": lz_val,
        "lz_star_fixed": lz_star_val,
        "d_fixed": d,
        "d_star_fixed": d_star,
        "ci_95": [ci_lo, ci_hi],
        "ci_star_95": [ci_star_lo, ci_star_hi],
        "theta_mle": data["theta_mle"],
        "lz_star_free": data["lz_star"],
        "accuracy": data["accuracy_overall"],
    }
    print(f"  {cond}: lz_fixed={lz_val:.4f}, d_fixed={d:.3f}, CI=[{ci_lo:.3f}, {ci_hi:.3f}] | lz*_fixed={lz_star_val:.4f}, d*_fixed={d_star:.3f}, CI*=[{ci_star_lo:.3f}, {ci_star_hi:.3f}]")

# Check contam_50_s3
fpath = os.path.join(RESULTS_DIR, "contam_50_s3_results.json")
if os.path.exists(fpath):
    with open(fpath) as f:
        data = json.load(f)
    resp = data["response_vector"]
    lz_val = compute_lz_drasgow(resp, irt_params, THETA_FIXED)
    lz_star_val = compute_lz_star(resp, irt_params, THETA_FIXED)
    d = (lz_val - np.mean(clean_lz_arr)) / np.std(clean_lz_arr, ddof=1)
    d_star = (lz_star_val - np.mean(clean_lz_star_arr)) / np.std(clean_lz_star_arr, ddof=1)
    ci_lo, ci_hi = bootstrap_cohens_d(lz_val, clean_lz_fixed)
    ci_star_lo, ci_star_hi = bootstrap_cohens_d(lz_star_val, clean_lz_star_fixed)
    results["contam_50_s3"] = {
        "lz_fixed": lz_val, "lz_star_fixed": lz_star_val,
        "d_fixed": d, "d_star_fixed": d_star,
        "ci_95": [ci_lo, ci_hi], "ci_star_95": [ci_star_lo, ci_star_hi],
    }
    print(f"  contam_50_s3: lz_fixed={lz_val:.4f}, d_fixed={d:.3f}, CI=[{ci_lo:.3f}, {ci_hi:.3f}]")
else:
    print(f"  contam_50_s3: SKIPPED (no results file yet)")

# Save results
output = {
    "theta_fixed": THETA_FIXED,
    "clean_baseline": {
        "lz_fixed_values": clean_lz_fixed,
        "lz_fixed_mean": float(np.mean(clean_lz_arr)),
        "lz_fixed_std": float(np.std(clean_lz_arr, ddof=1)),
        "lz_star_fixed_values": clean_lz_star_fixed,
        "lz_star_fixed_mean": float(np.mean(clean_lz_star_arr)),
        "lz_star_fixed_std": float(np.std(clean_lz_star_arr, ddof=1)),
        "n": len(clean_lz_fixed),
    },
    "contam_results": results,
}
out_path = os.path.join(RESULTS_DIR, "theta_fixed_all_seeds.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
