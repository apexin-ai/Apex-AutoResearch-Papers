#!/usr/bin/env python3
"""
Unified lz* recomputation for Qwen MMLU.
Single-source: Snijders (2001) lz* + Drasgow lz + theta_MLE.
All 12 conditions from response vectors.
"""

import numpy as np
import json
import csv
import os
from pathlib import Path

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

    # Point estimate

    clean_std = np.std(clean_arr, ddof=1)
    if clean_std < EPS:
        return 0.0, 0.0, 0.0
    d_obs = (contam_val - np.mean(clean_arr)) / clean_std

    # Bootstrap: resample clean, keep contam fixed
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


# ---- Main ----
print("Loading IRT parameters...")
a, b, c, d = load_irt_params(os.path.join(BASE_DIR, "mmlu_params.csv"))
print(f"  {len(a)} items loaded")

conditions = [f"clean_s{i}" for i in range(1, 11)] + ["contam_15", "contam_50"]

results = {}
print("\n=== Phase 1: Per-condition MLE theta + lz + lz* ===")
for cond in conditions:
    path = os.path.join(BASE_DIR, "results", f"{cond}_results.json")
    if not os.path.exists(path):
        print(f"  WARNING: {path} not found, skipping")
        continue

    resp = load_response_vector(path)
    assert len(resp) == len(a), f"Length mismatch: resp={len(resp)}, params={len(a)}"

    theta = estimate_theta_mle(resp, a, b, c, d)
    lz, lz_star = compute_lz_and_lz_star(resp, a, b, c, d, theta)
    acc = float(np.mean(resp))

    results[cond] = {
        "theta_mle": theta,
        "lz": lz,
        "lz_star": lz_star,
        "accuracy": acc,
    }
    print(f"  {cond:12s}  theta={theta:+.4f}  lz={lz:+.4f}  lz*={lz_star:+.4f}  acc={acc:.4f}")

# Phase 2: theta-fixed
print("\n=== Phase 2: Theta-fixed analysis ===")
clean_thetas = [results[f"clean_s{i}"]["theta_mle"] for i in range(1, 11)]
theta_fixed = float(np.mean(clean_thetas))
print(f"  theta_fixed (mean of 10 clean) = {theta_fixed:.6f}")

for cond in conditions:
    path = os.path.join(BASE_DIR, "results", f"{cond}_results.json")
    resp = load_response_vector(path)
    lz_f, lz_star_f = compute_lz_and_lz_star(resp, a, b, c, d, theta_fixed)
    results[cond]["lz_fixed"] = lz_f
    results[cond]["lz_star_fixed"] = lz_star_f

# Table 1
print("\n" + "=" * 95)
print("Table 1: Per-condition values (unified recomputation)")
print("=" * 95)
print(f"{'Condition':>12s} | {'theta_MLE':>9s} | {'lz (Drasgow)':>12s} | {'lz* (Snijders)':>14s} | {'lz*_fixed':>10s} | {'accuracy':>8s}")
print("-" * 95)
for cond in conditions:
    r = results[cond]
    print(f"{cond:>12s} | {r['theta_mle']:>+9.4f} | {r['lz']:>+12.4f} | {r['lz_star']:>+14.4f} | {r['lz_star_fixed']:>+10.4f} | {r['accuracy']:>8.4f}")

# Phase 3: Cohen's d
print("\n" + "=" * 95)
print("Table 2: Cohen's d + 95% Bootstrap CI")
print("=" * 95)

clean_lz_stars = [results[f"clean_s{i}"]["lz_star"] for i in range(1, 11)]
clean_lz_stars_fixed = [results[f"clean_s{i}"]["lz_star_fixed"] for i in range(1, 11)]

cohens_d_results = {}
for contam_cond in ["contam_15", "contam_50"]:
    d_free, ci_lo_free, ci_hi_free = bootstrap_cohens_d(
        clean_lz_stars, results[contam_cond]["lz_star"]
    )
    d_fixed, ci_lo_fixed, ci_hi_fixed = bootstrap_cohens_d(
        clean_lz_stars_fixed, results[contam_cond]["lz_star_fixed"]
    )

    cohens_d_results[contam_cond] = {
        "free_theta": {"d": d_free, "ci_lo": ci_lo_free, "ci_hi": ci_hi_free},
        "fixed_theta": {"d": d_fixed, "ci_lo": ci_lo_fixed, "ci_hi": ci_hi_fixed},
    }

print(f"{'Metric':>20s} | {'d(15%)':>8s} | {'95% CI':>20s} | {'d(50%)':>8s} | {'95% CI':>20s}")
print("-" * 95)
for label, key in [("lz* free-theta", "free_theta"), ("lz* theta-fixed", "fixed_theta")]:
    r15 = cohens_d_results["contam_15"][key]
    r50 = cohens_d_results["contam_50"][key]
    print(f"{label:>20s} | {r15['d']:>+8.4f} | [{r15['ci_lo']:>+8.4f}, {r15['ci_hi']:>+8.4f}] | {r50['d']:>+8.4f} | [{r50['ci_lo']:>+8.4f}, {r50['ci_hi']:>+8.4f}]")

# Save JSON
output = {
    "meta": {
        "description": "Unified lz* recomputation - Snijders (2001)",
        "n_items": int(len(a)),
        "theta_fixed": theta_fixed,
        "implementation": "unified_lz_recompute.py",
        "note": "All values from single codebase, single execution"
    },
    "per_condition": results,
    "cohens_d": cohens_d_results,
}

out_path = os.path.join(BASE_DIR, "unified_lz_results.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_path}")
