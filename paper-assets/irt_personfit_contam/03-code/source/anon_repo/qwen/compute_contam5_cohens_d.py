#!/usr/bin/env python3
"""Compute fixed-theta lz* and Cohen's d for contam_5."""
import numpy as np
import json
import csv
import os

BASE_DIR = "/path/to/project/qwen"
EPS = 1e-10

def load_irt_params(path):
    a, b, c, d = [], [], [], []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            a.append(float(row["a_discrimination"]))
            b.append(float(row["b_difficulty"]))
            c.append(float(row["c_guessing"]))
            d.append(float(row["d_feasibility"]))
    return np.array(a), np.array(b), np.array(c), np.array(d)

def load_response_vector(path):
    with open(path, "r") as f:
        data = json.load(f)
    return np.array(data["response_vector"], dtype=np.float64)

def icc_4pl(theta, a, b, c, d):
    z = a * (theta - b)
    z = np.clip(z, -30, 30)
    P = c + (d - c) / (1.0 + np.exp(-z))
    P = np.clip(P, EPS, 1.0 - EPS)
    return P

def icc_derivative(theta, a, b, c, d):
    P = icc_4pl(theta, a, b, c, d)
    denom = d - c + EPS
    P_prime = a * (P - c) * (d - P) / denom
    return P, P_prime

def estimate_theta_mle(response, a, b, c, d, theta_init=0.0, max_iter=100, tol=1e-6):
    theta = theta_init
    for _ in range(max_iter):
        P, P_prime = icc_derivative(theta, a, b, c, d)
        PQ = P * (1.0 - P)
        PQ = np.clip(PQ, EPS, None)
        L_prime = np.sum((response - P) * P_prime / PQ)
        I_theta = np.sum(P_prime ** 2 / PQ)
        if I_theta < EPS:
            break
        delta = L_prime / I_theta
        theta = theta + delta
        theta = np.clip(theta, -4.0, 4.0)
        if abs(delta) < tol:
            break
    return float(theta)

def compute_lz_and_lz_star(response, a, b, c, d, theta):
    P, P_prime = icc_derivative(theta, a, b, c, d)
    P = np.clip(P, EPS, 1.0 - EPS)
    PQ = P * (1.0 - P)
    PQ = np.clip(PQ, EPS, None)
    log_P = np.log(P)
    log_Q = np.log(1.0 - P)
    log_ratio = log_P - log_Q
    l0 = np.sum(response * log_P + (1.0 - response) * log_Q)
    E_l = np.sum(P * log_P + (1.0 - P) * log_Q)
    Var_l = np.sum(PQ * log_ratio ** 2)
    if Var_l < EPS:
        lz = 0.0
    else:
        lz = (l0 - E_l) / np.sqrt(Var_l)
    I_theta = np.sum(P_prime ** 2 / PQ)
    h_j = P_prime * log_ratio
    C_theta = np.sum(h_j)
    if I_theta < EPS:
        Var_star = Var_l
    else:
        Var_star = Var_l - C_theta ** 2 / I_theta
    if Var_star < EPS:
        lz_star = lz
    else:
        lz_star = (l0 - E_l) / np.sqrt(Var_star)
    return float(lz), float(lz_star)

def bootstrap_cohens_d(clean_vals, contam_val, n_boot=10000, seed=42):
    clean_arr = np.array(clean_vals)
    rng = np.random.RandomState(seed)
    n = len(clean_arr)
    clean_std = np.std(clean_arr, ddof=1)
    if clean_std < EPS:
        return 0.0, 0.0, 0.0
    d_obs = (contam_val - np.mean(clean_arr)) / clean_std
    d_boots = np.empty(n_boot)
    for i in range(n_boot):
        boot_clean = rng.choice(clean_arr, size=n, replace=True)
        s = np.std(boot_clean, ddof=1)
        if s < EPS:
            d_boots[i] = 0.0
        else:
            d_boots[i] = (contam_val - np.mean(boot_clean)) / s
    ci_lo = float(np.percentile(d_boots, 2.5))
    ci_hi = float(np.percentile(d_boots, 97.5))
    return float(d_obs), ci_lo, ci_hi

# Load unified results for clean baselines
with open(os.path.join(BASE_DIR, "unified_lz_results.json"), "r") as f:
    unified = json.load(f)

theta_fixed = unified["meta"]["theta_fixed"]
print(f"theta_fixed = {theta_fixed:.6f}")

# Load IRT params
a, b, c, d = load_irt_params(os.path.join(BASE_DIR, "mmlu_params.csv"))
print(f"Loaded {len(a)} IRT items")

# Load contam_5 response vector
resp_path = os.path.join(BASE_DIR, "results", "contam_5_results.json")
resp = load_response_vector(resp_path)
print(f"contam_5 response vector: {len(resp)} items, acc={np.mean(resp):.4f}")

# Compute free-theta lz* (verify matches existing)
theta_mle = estimate_theta_mle(resp, a, b, c, d)
lz_free, lz_star_free = compute_lz_and_lz_star(resp, a, b, c, d, theta_mle)
print(f"\n=== Free-theta ===")
print(f"theta_mle = {theta_mle:.6f}")
print(f"lz = {lz_free:.6f}, lz* = {lz_star_free:.6f}")

# Compute fixed-theta lz*
lz_fixed, lz_star_fixed = compute_lz_and_lz_star(resp, a, b, c, d, theta_fixed)
print(f"\n=== Fixed-theta (theta={theta_fixed:.6f}) ===")
print(f"lz = {lz_fixed:.6f}, lz* = {lz_star_fixed:.6f}")

# Get clean baselines
clean_lz_stars_free = [unified["per_condition"][f"clean_s{i}"]["lz_star"] for i in range(1, 11)]
clean_lz_stars_fixed = [unified["per_condition"][f"clean_s{i}"]["lz_star_fixed"] for i in range(1, 11)]
print(f"\nClean lz* (free): mean={np.mean(clean_lz_stars_free):.4f}, std={np.std(clean_lz_stars_free, ddof=1):.4f}")
print(f"Clean lz* (fixed): mean={np.mean(clean_lz_stars_fixed):.4f}, std={np.std(clean_lz_stars_fixed, ddof=1):.4f}")

# Cohen's d
d_free, ci_lo_free, ci_hi_free = bootstrap_cohens_d(clean_lz_stars_free, lz_star_free)
d_fixed, ci_lo_fixed, ci_hi_fixed = bootstrap_cohens_d(clean_lz_stars_fixed, lz_star_fixed)

print(f"\n=== Cohen's d ===")
print(f"Free-theta:  d = {d_free:+.4f}, 95% CI = [{ci_lo_free:+.4f}, {ci_hi_free:+.4f}]")
print(f"Fixed-theta: d = {d_fixed:+.4f}, 95% CI = [{ci_lo_fixed:+.4f}, {ci_hi_fixed:+.4f}]")

# Save results
output = {
    "condition": "contam_5",
    "theta_mle": theta_mle,
    "theta_fixed": theta_fixed,
    "lz_star_free": lz_star_free,
    "lz_star_fixed": lz_star_fixed,
    "lz_free": lz_free,
    "lz_fixed": lz_fixed,
    "accuracy": float(np.mean(resp)),
    "n_items": int(len(resp)),
    "n_seen": 702,
    "cohens_d": {
        "free_theta": {"d": d_free, "ci_lo": ci_lo_free, "ci_hi": ci_hi_free},
        "fixed_theta": {"d": d_fixed, "ci_lo": ci_lo_fixed, "ci_hi": ci_hi_fixed},
    },
    "clean_baselines": {
        "lz_star_free_mean": float(np.mean(clean_lz_stars_free)),
        "lz_star_free_std": float(np.std(clean_lz_stars_free, ddof=1)),
        "lz_star_fixed_mean": float(np.mean(clean_lz_stars_fixed)),
        "lz_star_fixed_std": float(np.std(clean_lz_stars_fixed, ddof=1)),
    },
}

out_path = os.path.join(BASE_DIR, "results", "contam_5_cohens_d.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
