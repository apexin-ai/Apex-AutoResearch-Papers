import json
import numpy as np

np.random.seed(42)

# === Raw data from W&B and logs ===
steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

data = {
    "cka_only": {
        "reward_mean": [0.253125, 0.218125, 0.25, 0.234375, 0.354375, 0.299375, 0.3075, 0.341875, 0.241875, 0.344375],
        "reward_std":  [0.387209, 0.359799, 0.389845, 0.349655, 0.454006, 0.390239, 0.421871, 0.432306, 0.349333, 0.444011],
        "frac_zero_std": [0.175, 0.2, 0.2, 0.35, 0.15, 0.2, 0.125, 0.25, 0.3, 0.2],
        "wandb_run_id": "li451oi4",
        "source": "wandb"
    },
    "standard": {
        "reward_mean": [0.05125, 0.055625, 0.066875, 0.08125, 0.01875, 0.043125, 0.046875, 0.045625, 0.030625, 0.05375],
        "reward_std":  [0.167951, 0.165603, 0.206658, 0.216719, 0.052165, 0.125806, 0.135433, 0.147164, 0.066939, 0.14187],
        "frac_zero_std": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55],
        "wandb_run_id": "tyv20u2k",
        "source": "wandb"
    },
    "rasp": {
        "reward_mean": [0.016875, 0.020625, 0.0225, 0.02125, 0.06125, 0.053125, 0.055625, 0.03, 0.015, 0.01],
        "reward_std":  [0.058262, 0.064115, 0.053727, 0.069157, 0.201187, 0.17678, 0.158018, 0.109178, 0.06, 0.04],
        "frac_zero_std": [0.85, 0.85, 0.8, 0.85, 0.725, 0.75, 0.675, 0.775, 0.9, 0.85],
        "wandb_run_id": "s5zf5akl",
        "source": "wandb"
    },
    "random": {
        "reward_mean": [0.1606, 0.1419, 0.1663, 0.145, 0.175, 0.1844, 0.19, 0.1419, 0.1725, None],
        "reward_std":  [0.3094, 0.28, 0.3471, 0.3033, 0.3244, 0.3162, 0.3493, 0.2674, 0.2861, None],
        "frac_zero_std": [0.3, 0.325, 0.325, 0.4, 0.3, 0.35, 0.3, 0.375, 0.325, None],
        "wandb_run_id": None,
        "source": "log_file (crashed before step 100, no W&B sync)"
    }
}

# === Bootstrap parameters ===
N_BOOTSTRAP = 10000
CONFIDENCE_LEVEL = 0.95
# Effective sample size per logging interval:
# per_device_train_batch_size=2, num_generations=4, logged every 10 steps
# n = 2 prompts × 4 generations × 10 steps = 80 completions
N_SAMPLES_PER_INTERVAL = 80

alpha = 1 - CONFIDENCE_LEVEL
methods = ["cka_only", "standard", "rasp", "random"]
pairs = []
for i, m1 in enumerate(methods):
    for m2 in methods[i+1:]:
        pairs.append((m1, m2))

# === Parametric bootstrap ===
results = {
    "metadata": {
        "analysis": "Bootstrap CI on reward trajectory gaps",
        "n_bootstrap": N_BOOTSTRAP,
        "confidence_level": CONFIDENCE_LEVEL,
        "n_samples_per_interval": N_SAMPLES_PER_INTERVAL,
        "limitation": (
            "W&B only stores aggregate metrics (mean, std) per logging interval, "
            "not per-sample rewards. We use PARAMETRIC bootstrap: at each step, "
            "sample the mean from Normal(mu, sigma^2/n) where n=80 is the estimated "
            "effective sample size (2 prompts × 4 generations × 10 steps per interval). "
            "This assumes approximate normality of the sample mean (CLT with n=80). "
            "True non-parametric bootstrap would require per-sample reward data."
        ),
        "random_note": "grpo_random_20 crashed at step 90; step 100 is missing.",
        "methods": {k: {"wandb_run_id": v["wandb_run_id"], "source": v["source"]}
                    for k, v in data.items()}
    },
    "per_step_rewards": {},
    "pairwise_gaps": {},
    "trajectory_summary": {}
}

# Store per-step rewards
for step_idx, step in enumerate(steps):
    step_key = f"step_{step}"
    results["per_step_rewards"][step_key] = {}
    for method in methods:
        mu = data[method]["reward_mean"][step_idx]
        sigma = data[method]["reward_std"][step_idx]
        if mu is not None:
            se = sigma / np.sqrt(N_SAMPLES_PER_INTERVAL)
            results["per_step_rewards"][step_key][method] = {
                "mean": mu,
                "std": sigma,
                "se": round(se, 6),
                "ci_95_lower": round(mu - 1.96 * se, 6),
                "ci_95_upper": round(mu + 1.96 * se, 6)
            }

# Pairwise gap bootstrap
for m1, m2 in pairs:
    pair_key = f"{m1}_vs_{m2}"
    results["pairwise_gaps"][pair_key] = {}

    for step_idx, step in enumerate(steps):
        step_key = f"step_{step}"
        mu1 = data[m1]["reward_mean"][step_idx]
        mu2 = data[m2]["reward_mean"][step_idx]
        s1 = data[m1]["reward_std"][step_idx]
        s2 = data[m2]["reward_std"][step_idx]

        if mu1 is None or mu2 is None:
            results["pairwise_gaps"][pair_key][step_key] = {
                "gap": None,
                "note": "missing data for one or both methods"
            }
            continue

        se1 = s1 / np.sqrt(N_SAMPLES_PER_INTERVAL)
        se2 = s2 / np.sqrt(N_SAMPLES_PER_INTERVAL)

        boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)
        boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)
        boot_gap = boot_m1 - boot_m2

        ci_lower = float(np.percentile(boot_gap, 100 * alpha / 2))
        ci_upper = float(np.percentile(boot_gap, 100 * (1 - alpha / 2)))
        gap_mean = float(np.mean(boot_gap))
        gap_se = float(np.std(boot_gap))

        significant = (ci_lower > 0) or (ci_upper < 0)

        results["pairwise_gaps"][pair_key][step_key] = {
            "gap_observed": round(mu1 - mu2, 6),
            "gap_bootstrap_mean": round(gap_mean, 6),
            "gap_bootstrap_se": round(gap_se, 6),
            "ci_95": [round(ci_lower, 6), round(ci_upper, 6)],
            "significant": significant,
            "favors": m1 if (mu1 - mu2) > 0 else m2
        }

# Trajectory-level summary: average gap over all available steps
for m1, m2 in pairs:
    pair_key = f"{m1}_vs_{m2}"
    all_gaps = []
    all_boot_gaps = np.zeros(N_BOOTSTRAP)
    n_valid = 0

    for step_idx, step in enumerate(steps):
        mu1 = data[m1]["reward_mean"][step_idx]
        mu2 = data[m2]["reward_mean"][step_idx]
        s1 = data[m1]["reward_std"][step_idx]
        s2 = data[m2]["reward_std"][step_idx]

        if mu1 is None or mu2 is None:
            continue

        se1 = s1 / np.sqrt(N_SAMPLES_PER_INTERVAL)
        se2 = s2 / np.sqrt(N_SAMPLES_PER_INTERVAL)

        boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)
        boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)
        all_boot_gaps += (boot_m1 - boot_m2)
        all_gaps.append(mu1 - mu2)
        n_valid += 1

    if n_valid > 0:
        avg_boot_gap = all_boot_gaps / n_valid
        ci_lower = float(np.percentile(avg_boot_gap, 2.5))
        ci_upper = float(np.percentile(avg_boot_gap, 97.5))
        results["trajectory_summary"][pair_key] = {
            "mean_gap_observed": round(np.mean(all_gaps), 6),
            "mean_gap_bootstrap": round(float(np.mean(avg_boot_gap)), 6),
            "ci_95": [round(ci_lower, 6), round(ci_upper, 6)],
            "n_steps_compared": n_valid,
            "significant": (ci_lower > 0) or (ci_upper < 0),
            "favors": m1 if np.mean(all_gaps) > 0 else m2
        }

# === Sensitivity analysis: vary n ===
sensitivity = {}
for n_eff in [40, 80, 160]:
    key = f"n_eff_{n_eff}"
    sensitivity[key] = {}
    for m1, m2 in pairs:
        pair_key = f"{m1}_vs_{m2}"
        all_boot_gaps = np.zeros(N_BOOTSTRAP)
        n_valid = 0
        for step_idx in range(len(steps)):
            mu1 = data[m1]["reward_mean"][step_idx]
            mu2 = data[m2]["reward_mean"][step_idx]
            s1 = data[m1]["reward_std"][step_idx]
            s2 = data[m2]["reward_std"][step_idx]
            if mu1 is None or mu2 is None:
                continue
            se1 = s1 / np.sqrt(n_eff)
            se2 = s2 / np.sqrt(n_eff)
            boot_m1 = np.random.normal(mu1, se1, N_BOOTSTRAP)
            boot_m2 = np.random.normal(mu2, se2, N_BOOTSTRAP)
            all_boot_gaps += (boot_m1 - boot_m2)
            n_valid += 1
        if n_valid > 0:
            avg_boot_gap = all_boot_gaps / n_valid
            ci_lower = float(np.percentile(avg_boot_gap, 2.5))
            ci_upper = float(np.percentile(avg_boot_gap, 97.5))
            sensitivity[key][pair_key] = {
                "ci_95": [round(ci_lower, 6), round(ci_upper, 6)],
                "significant": (ci_lower > 0) or (ci_upper < 0)
            }

results["sensitivity_n_eff"] = sensitivity

# Write output
output_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/bootstrap_ci_reward_trajectories.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print(f"Written to {output_path}")
print(f"\n=== Trajectory-level summary (mean gap over all steps, 95% CI) ===")
for pair_key, v in results["trajectory_summary"].items():
    sig = "***" if v["significant"] else "n.s."
    print(f"  {pair_key}: gap={v['mean_gap_observed']:.4f}, CI=[{v['ci_95'][0]:.4f}, {v['ci_95'][1]:.4f}] {sig} favors {v['favors']}")

print(f"\n=== Per-step significant gaps (step 100) ===")
for pair_key, steps_data in results["pairwise_gaps"].items():
    s100 = steps_data.get("step_100", {})
    if s100.get("gap_observed") is not None:
        sig = "***" if s100["significant"] else "n.s."
        print(f"  {pair_key}: gap={s100['gap_observed']:.4f}, CI=[{s100['ci_95'][0]:.4f}, {s100['ci_95'][1]:.4f}] {sig}")
    else:
        print(f"  {pair_key}: step 100 data missing")

print(f"\n=== Sensitivity to n_eff (trajectory mean gap) ===")
for n_key, pairs_data in results["sensitivity_n_eff"].items():
    print(f"  {n_key}:")
    for pair_key, v in pairs_data.items():
        sig = "***" if v["significant"] else "n.s."
        print(f"    {pair_key}: CI=[{v['ci_95'][0]:.4f}, {v['ci_95'][1]:.4f}] {sig}")
