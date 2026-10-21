#!/usr/bin/env python3
"""Permutation test for CV and I^2 differences between instruction and control ablation.

Tests whether the observed CV and I^2 differences could arise from random
group assignment, using exact paired permutation (swap labels within each
dimension/task pair).
"""

import json
import numpy as np
from itertools import product


def compute_I2(d_values, n_per_task=500):
    """Cochran's Q and I^2 using w_i = n weights (matches original analysis)."""
    d = np.array(d_values, dtype=np.float64)
    k = len(d)
    d_mean = d.mean()
    Q = n_per_task * np.sum((d - d_mean) ** 2)
    I2 = max(0.0, (Q - (k - 1)) / Q) if Q > 0 else 0.0
    return Q, I2


with open("/root/autodl-tmp/vla-ssd/results/action_trajectory_extended_analysis.json") as f:
    ext = json.load(f)

# ---------- extract data ----------
per_dim_cv = ext["temporal_coherence_proxy"]["per_dim_cv"]
inst_cvs_7d = [d["inst_cv"] for d in per_dim_cv]
ctrl_cvs_7d = [d["ctrl_cv"] for d in per_dim_cv]
inst_cvs_6d = inst_cvs_7d[:6]
ctrl_cvs_6d = ctrl_cvs_7d[:6]

cross_task = ext["temporal_coherence_proxy"]["cross_task_heterogeneity"]
inst_ds = cross_task["instruction_ablation"]["per_task_d"]
ctrl_ds = cross_task["control_ablation"]["per_task_d"]

# ---------- observed values ----------
obs_cv_inst = np.mean(inst_cvs_6d)
obs_cv_ctrl = np.mean(ctrl_cvs_6d)
_, obs_I2_inst = compute_I2(inst_ds)
_, obs_I2_ctrl = compute_I2(ctrl_ds)

obs_cv_diff = obs_cv_ctrl - obs_cv_inst   # ctrl > inst
obs_I2_diff = obs_I2_inst - obs_I2_ctrl    # inst > ctrl

print("=== Observed ===")
print(f"CV  inst={obs_cv_inst:.4f}  ctrl={obs_cv_ctrl:.4f}  diff={obs_cv_diff:.4f}")
print(f"I2  inst={obs_I2_inst:.4f}  ctrl={obs_I2_ctrl:.4f}  diff={obs_I2_diff:.4f}")

# ==========================================================
# 1. Exact paired permutation — CV (6 continuous dims, 2^6=64)
# ==========================================================
n_dims = len(inst_cvs_6d)
cv_null = []
for perm in product([False, True], repeat=n_dims):
    pi, pc = [], []
    for i, swap in enumerate(perm):
        if swap:
            pi.append(ctrl_cvs_6d[i]); pc.append(inst_cvs_6d[i])
        else:
            pi.append(inst_cvs_6d[i]); pc.append(ctrl_cvs_6d[i])
    cv_null.append(np.mean(pc) - np.mean(pi))
cv_null = np.array(cv_null)
p_cv_exact = np.mean(cv_null >= obs_cv_diff)

print(f"\n--- CV exact paired permutation (2^{n_dims}={2**n_dims}) ---")
print(f"Null: mean={cv_null.mean():.4f} std={cv_null.std():.4f}")
print(f"Observed={obs_cv_diff:.4f}  p={p_cv_exact:.6f}  sig={p_cv_exact<0.05}")

# sensitivity: 7 dims
cv_null_7d = []
for perm in product([False, True], repeat=7):
    pi, pc = [], []
    for i, swap in enumerate(perm):
        if swap:
            pi.append(ctrl_cvs_7d[i]); pc.append(inst_cvs_7d[i])
        else:
            pi.append(inst_cvs_7d[i]); pc.append(ctrl_cvs_7d[i])
    cv_null_7d.append(np.mean(pc) - np.mean(pi))
cv_null_7d = np.array(cv_null_7d)
obs_cv_diff_7d = np.mean(ctrl_cvs_7d) - np.mean(inst_cvs_7d)
p_cv_7d = np.mean(cv_null_7d >= obs_cv_diff_7d)
print(f"[7d sensitivity] diff={obs_cv_diff_7d:.4f}  p={p_cv_7d:.6f}")

# ==========================================================
# 2. Exact paired permutation — I^2 (5 tasks, 2^5=32)
# ==========================================================
n_tasks = len(inst_ds)
I2_null = []
for perm in product([False, True], repeat=n_tasks):
    pi_d, pc_d = [], []
    for i, swap in enumerate(perm):
        if swap:
            pi_d.append(ctrl_ds[i]); pc_d.append(inst_ds[i])
        else:
            pi_d.append(inst_ds[i]); pc_d.append(ctrl_ds[i])
    _, i2_pi = compute_I2(pi_d)
    _, i2_pc = compute_I2(pc_d)
    I2_null.append(i2_pi - i2_pc)
I2_null = np.array(I2_null)
p_I2_exact = np.mean(I2_null >= obs_I2_diff)

print(f"\n--- I^2 exact paired permutation (2^{n_tasks}={2**n_tasks}) ---")
print(f"Null: mean={I2_null.mean():.4f} std={I2_null.std():.4f}")
print(f"Observed={obs_I2_diff:.4f}  p={p_I2_exact:.6f}  sig={p_I2_exact<0.05}")

# ==========================================================
# 3. Monte-Carlo unpaired permutation (10k) for higher resolution
# ==========================================================
rng = np.random.default_rng(42)
N_MC = 10_000

# CV: pool 12 values, split 6+6
all_cvs = inst_cvs_6d + ctrl_cvs_6d
mc_cv = np.empty(N_MC)
for k in range(N_MC):
    idx = rng.permutation(12)
    mc_cv[k] = np.mean([all_cvs[i] for i in idx[6:]]) - np.mean([all_cvs[i] for i in idx[:6]])
p_cv_mc = float(np.mean(mc_cv >= obs_cv_diff))

# I^2: pool 10 d-values, split 5+5
all_ds = inst_ds + ctrl_ds
mc_I2 = np.empty(N_MC)
for k in range(N_MC):
    idx = rng.permutation(10)
    g1 = [all_ds[i] for i in idx[:5]]
    g2 = [all_ds[i] for i in idx[5:]]
    _, i2_1 = compute_I2(g1)
    _, i2_2 = compute_I2(g2)
    mc_I2[k] = i2_1 - i2_2
p_I2_mc = float(np.mean(np.abs(mc_I2) >= abs(obs_I2_diff)))

print(f"\n--- Monte-Carlo unpaired ({N_MC} iterations) ---")
print(f"CV:  null mean={mc_cv.mean():.4f} std={mc_cv.std():.4f}  p={p_cv_mc:.4f}")
print(f"I^2: null mean={mc_I2.mean():.4f} std={mc_I2.std():.4f}  p(two-sided)={p_I2_mc:.4f}")

# ==========================================================
# Build output
# ==========================================================
conclusion_parts = []
if p_cv_exact < 0.05:
    conclusion_parts.append(
        f"CV difference significant (exact paired p={p_cv_exact:.4f}): "
        f"instruction CV ({obs_cv_inst:.2f}) < control CV ({obs_cv_ctrl:.2f}), "
        f"instruction heads produce more uniform perturbation across action dims."
    )
else:
    conclusion_parts.append(
        f"CV difference not significant at alpha=0.05 (exact paired p={p_cv_exact:.4f})."
    )

if p_I2_exact < 0.05:
    conclusion_parts.append(
        f"I^2 difference not significant at alpha=0.05 (exact paired p={p_I2_exact:.4f}, "
        f"min possible={1/2**n_tasks:.4f}). "
        f"Limited resolution with 2^5=32 permutations."
    )
else:
    conclusion_parts.append(
        f"I^2 difference not significant at alpha=0.05 (exact paired p={p_I2_exact:.4f}, "
        f"min possible={1/2**n_tasks:.4f}). "
        f"Limited resolution with 2^5=32 permutations."
    )

conclusion_parts.append(
    f"MC unpaired: CV p={p_cv_mc:.4f}, I^2 p(two-sided)={p_I2_mc:.4f}."
)

conclusion = " ".join(conclusion_parts)
print(f"\nConclusion: {conclusion}")

results = {
    "method": "exact_paired_permutation_test",
    "data_source": {
        "instruction_ablation": "24 heads, per-dim CV from 6 continuous dims, per-task d from 5 tasks",
        "control_ablation": "8 heads, same dimensions and tasks",
    },
    "observed": {
        "cv_inst": float(obs_cv_inst),
        "cv_ctrl": float(obs_cv_ctrl),
        "cv_diff_ctrl_minus_inst": float(obs_cv_diff),
        "I2_inst": float(obs_I2_inst),
        "I2_ctrl": float(obs_I2_ctrl),
        "I2_diff_inst_minus_ctrl": float(obs_I2_diff),
    },
    "cv_test_exact_paired": {
        "n_dims": n_dims,
        "n_permutations": 2 ** n_dims,
        "null_mean": float(cv_null.mean()),
        "null_std": float(cv_null.std()),
        "p_value_one_sided": float(p_cv_exact),
        "significant_005": bool(p_cv_exact < 0.05),
    },
    "cv_test_7d_sensitivity": {
        "observed_diff": float(obs_cv_diff_7d),
        "p_value": float(p_cv_7d),
    },
    "I2_test_exact_paired": {
        "n_tasks": n_tasks,
        "n_permutations": 2 ** n_tasks,
        "null_mean": float(I2_null.mean()),
        "null_std": float(I2_null.std()),
        "p_value_one_sided": float(p_I2_exact),
        "significant_005": bool(p_I2_exact < 0.05),
        "note": f"Min possible p = 1/{2**n_tasks} = {1/2**n_tasks:.4f}",
    },
    "monte_carlo_unpaired": {
        "n_iterations": N_MC,
        "seed": 42,
        "cv_p_value": float(p_cv_mc),
        "I2_p_value_two_sided": float(p_I2_mc),
    },
    "conclusion": conclusion,
}

out = "/root/autodl-tmp/vla-ssd/results/permutation_test_I2.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {out}")
