"""Statistical tests for all multi-seed conditions in occsafe_vla."""
import json
import numpy as np
from scipy import stats

# Data extracted from registry (50-rollout evaluations at step 50000)
CONDITIONS = {
    "Vanilla": {
        "car": [0.788, 0.766, 0.786],  # mvp_vanilla_s0, s1, s2
        "tsr": [0.900, 0.918, 0.904],
    },
    "Full_OCC": {
        "car": [0.832, 0.788, 0.770],  # mvp_occ_s0, occ_s1_fresh, mvp_occ_s2
        "tsr": [0.904, 0.938, 0.840],
    },
    "Detach_BN": {
        "car": [0.746, 0.744, 0.748],  # ablation_occ_detach_s0, s1, s2
        "tsr": [0.914, 0.898, 0.624],
    },
    "Random_OCC": {
        "car": [0.814, 0.798, 0.754],  # ablation_random_occ_s0, s1, s2
        "tsr": [0.856, 0.902, 0.848],
    },
    "Depth": {
        "car": [0.736, 0.818, 0.758, 0.806],  # depth_s0, s1, s2, s3
        "tsr": [0.940, 0.906, 0.860, 0.848],
    },
    "Cutoff_35K": {
        "car": [0.768, 0.798, 0.770],  # cutoff_s0, s1, s2_v2
        "tsr": [0.912, 0.918, 0.970],
    },
    "Cutoff_15K": {
        "car": [0.804],  # cutoff_15k_s0
        "tsr": [0.912],
    },
    "Cutoff_25K": {
        "car": [0.688, 0.760],  # cutoff_25k_s0, s1
        "tsr": [0.844, 0.930],
    },
    "Cutoff_45K": {
        "car": [0.764],  # cutoff_45k_s0
        "tsr": [0.896],
    },
    "Reverse_Cutoff": {
        "car": [0.700, 0.736],  # reverse_cutoff_s0, s1
        "tsr": [0.788, 0.890],
    },
    "Detach_LN": {
        "car": [0.792, 0.756, 0.748],  # detach_ln_s0, s1, s2
        "tsr": [0.914, 0.906, 0.884],
    },
}


def bootstrap_ci(data, n_boot=10000, ci=0.95, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    data = np.array(data)
    n = len(data)
    boot_means = np.array([rng.choice(data, size=n, replace=True).mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return float(np.percentile(boot_means, alpha * 100)), float(np.percentile(boot_means, (1 - alpha) * 100))


def cohens_d(group, baseline):
    """Cohen's d with pooled std."""
    g = np.array(group)
    b = np.array(baseline)
    n1, n2 = len(g), len(b)
    var1, var2 = g.var(ddof=1), b.var(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((g.mean() - b.mean()) / pooled_std)


def paired_ttest(group, baseline):
    """Paired t-test. If lengths differ, use independent t-test."""
    g = np.array(group)
    b = np.array(baseline)
    if len(g) == len(b):
        t_stat, p_val = stats.ttest_rel(g, b)
    else:
        t_stat, p_val = stats.ttest_ind(g, b)
    return float(p_val)


def main():
    vanilla_car = np.array(CONDITIONS["Vanilla"]["car"])
    vanilla_tsr = np.array(CONDITIONS["Vanilla"]["tsr"])
    rng = np.random.default_rng(42)

    results = {}
    for name, data in CONDITIONS.items():
        car = np.array(data["car"])
        tsr = np.array(data["tsr"])
        n = len(car)

        entry = {"n_seeds": n}

        if n >= 2:
            car_ci = bootstrap_ci(car, rng=rng)
            tsr_ci = bootstrap_ci(tsr, rng=rng)
            entry["car"] = {
                "mean": round(float(car.mean()), 4),
                "std": round(float(car.std(ddof=1)), 4),
                "ci_lower": round(car_ci[0], 4),
                "ci_upper": round(car_ci[1], 4),
                "seeds": [round(x, 4) for x in car.tolist()],
            }
            entry["tsr"] = {
                "mean": round(float(tsr.mean()), 4),
                "std": round(float(tsr.std(ddof=1)), 4),
                "ci_lower": round(tsr_ci[0], 4),
                "ci_upper": round(tsr_ci[1], 4),
                "seeds": [round(x, 4) for x in tsr.tolist()],
            }
        else:
            entry["car"] = {
                "mean": round(float(car[0]), 4),
                "std": None,
                "ci_lower": None,
                "ci_upper": None,
                "seeds": [round(x, 4) for x in car.tolist()],
            }
            entry["tsr"] = {
                "mean": round(float(tsr[0]), 4),
                "std": None,
                "ci_lower": None,
                "ci_upper": None,
                "seeds": [round(x, 4) for x in tsr.tolist()],
            }

        if name == "Vanilla":
            entry["vs_vanilla"] = None
        elif n >= 2:
            entry["vs_vanilla"] = {
                "cohens_d_car": round(cohens_d(car, vanilla_car), 4),
                "cohens_d_tsr": round(cohens_d(tsr, vanilla_tsr), 4),
                "ttest_p_car": round(paired_ttest(car, vanilla_car), 4),
                "ttest_p_tsr": round(paired_ttest(tsr, vanilla_tsr), 4),
            }
        else:
            entry["vs_vanilla"] = "insufficient_seeds"

        results[name] = entry

    out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    # Print summary
    print(f"Written to {out_path}\n")
    for name, entry in results.items():
        car_mean = entry["car"]["mean"]
        n = entry["n_seeds"]
        if entry["vs_vanilla"] and entry["vs_vanilla"] != "insufficient_seeds":
            d = entry["vs_vanilla"]["cohens_d_car"]
            p = entry["vs_vanilla"]["ttest_p_car"]
            print(f"{name:15s}  n={n}  CAR={car_mean:.4f}  d={d:+.3f}  p={p:.4f}")
        else:
            print(f"{name:15s}  n={n}  CAR={car_mean:.4f}")


if __name__ == "__main__":
    main()
