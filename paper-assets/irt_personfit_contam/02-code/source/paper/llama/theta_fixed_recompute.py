#!/usr/bin/env python3
"""Theta-fixed lz* recomputation for Llama ctrl-contam experiment.
Uses Snijders (2001) corrected lz* formula."""

import csv, json, os
import numpy as np

BASE_DIR = "/path/to/project/llama"
PARAMS_PATH = os.path.join(BASE_DIR, "mmlu_params.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

def prob_4pl(theta, a, b, c, d):
    z = a * (theta - b)
    sigmoid = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
    P = c + (d - c) * sigmoid
    return np.clip(P, 1e-15, 1 - 1e-15)

def compute_lz_star(x, theta_hat, a, b, c, d):
    """Snijders (2001) corrected lz*."""
    P = prob_4pl(theta_hat, a, b, c, d)
    Q = 1 - P
    x = np.asarray(x, dtype=np.float64)

    z = a * (theta_hat - b)
    sigma = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
    dP = a * (d - c) * sigma * (1 - sigma)

    h = dP / (P * Q)
    g = np.log(P / Q)

    l = np.sum(x * np.log(P) + (1 - x) * np.log(Q))
    E_l = np.sum(P * np.log(P) + Q * np.log(Q))
    Var_l = np.sum(P * Q * g ** 2)

    I_theta = np.sum(P * Q * h ** 2)
    C_theta = np.sum(P * Q * h * g)

    Var_star = Var_l - C_theta ** 2 / I_theta

    if Var_star <= 0:
        Var_use = Var_l
    else:
        Var_use = Var_star

    return float((l - E_l) / np.sqrt(Var_use))

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

# Use exact clean theta as theta_fixed
clean_data = json.load(open(os.path.join(RESULTS_DIR, "clean_results.json")))
THETA_FIXED = clean_data["theta_mle"]
print(f"theta_fixed = {THETA_FIXED} (exact clean MLE)")

# Load results and compute
conditions = ["clean", "contam_15", "contam_50"]
output = {
    "theta_fixed": THETA_FIXED,
    "conditions": {},
    "note": "Using lz* (Snijders 2001 corrected)"
}

for cond in conditions:
    fpath = os.path.join(RESULTS_DIR, f"{cond}_results.json")
    data = json.load(open(fpath))
    rv = np.array(data["response_vector"], dtype=np.float64)
    theta_free = data["theta_mle"]

    lz_star_free = compute_lz_star(rv, theta_free, a, b, c, d)
    lz_star_fixed = compute_lz_star(rv, THETA_FIXED, a, b, c, d)

    entry = {
        "theta_free": round(theta_free, 6),
        "lz_star_free": round(lz_star_free, 6),
        "lz_star_fixed": round(lz_star_fixed, 6),
        "accuracy": round(data["accuracy_overall"], 6)
    }
    output["conditions"][cond] = entry
    print(f"{cond}: theta_free={theta_free:.4f}, lz*_free={lz_star_free:.4f}, lz*_fixed={lz_star_fixed:.4f}")

# Validation: clean lz*_fixed == lz*_free
print(f"\nValidation: clean lz*_free={output['conditions']['clean']['lz_star_free']}, lz*_fixed={output['conditions']['clean']['lz_star_fixed']}")

# Compute deltas relative to clean
clean_fixed = output["conditions"]["clean"]["lz_star_fixed"]
for cond in ["contam_15", "contam_50"]:
    delta = output["conditions"][cond]["lz_star_fixed"] - clean_fixed
    output["conditions"][cond]["delta_lz_star_fixed"] = round(delta, 6)
    print(f"{cond}: delta_lz*_fixed = {delta:.4f}")

# Dose-response ratio
d15 = output["conditions"]["contam_15"]["delta_lz_star_fixed"]
d50 = output["conditions"]["contam_50"]["delta_lz_star_fixed"]
ratio = abs(d50) / abs(d15) if abs(d15) > 1e-10 else float("inf")
monotonic = abs(d50) > abs(d15)

output["dose_response_ratio"] = round(ratio, 6)
output["monotonic"] = monotonic

print(f"\nDose-response ratio (fixed): {ratio:.4f}")
print(f"Monotonic: {monotonic}")

# Free-theta comparison
clean_free = output["conditions"]["clean"]["lz_star_free"]
d15_free = output["conditions"]["contam_15"]["lz_star_free"] - clean_free
d50_free = output["conditions"]["contam_50"]["lz_star_free"] - clean_free
ratio_free = abs(d50_free) / abs(d15_free) if abs(d15_free) > 1e-10 else float("inf")
print(f"Dose-response ratio (free):  {ratio_free:.4f}")

# Save
out_path = os.path.join(RESULTS_DIR, "theta_fixed_llama.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {out_path}")
