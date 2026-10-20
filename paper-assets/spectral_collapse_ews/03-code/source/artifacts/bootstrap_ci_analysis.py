"""Bootstrap 95% CI analysis for Pythia-410M SLV trajectories across mixing ratios."""

import json
import numpy as np
from pathlib import Path

np.random.seed(2026)
B = 10_000
ALPHA = 0.05
GENS = list(range(11))

# ── Per-seed SLV trajectories (Gen 0–10) ──
data = {
    "r=0": {
        "seed42": [2366.6836, 2464.7622, 2469.9277, 2440.5657, 2405.0498,
                   2370.1726, 2335.1653, 2304.1904, 2252.1189, 2207.5684, 2178.9490],
        "seed43": [2366.68, 2462.62, 2466.63, 2438.38, 2404.60,
                   2365.13, 2325.01, 2291.55, 2248.26, 2234.80, 2210.77],
        "seed44": [2366.68, 2459.40, 2467.38, 2442.40, 2408.35,
                   2362.67, 2318.17, 2283.98, 2237.81, 2188.92, 2154.34],
    },
    "r=0.2": {
        "seed42": [2366.68, 2367.46, 2358.31, 2362.52, 2379.19,
                   2398.93, 2429.83, 2436.35, 2454.30, 2463.14, 2479.70],
        "seed43": [2366.68, 2365.31, 2358.84, 2365.74, 2377.37,
                   2395.98, 2411.37, 2426.30, 2436.78, 2453.63, 2455.78],
        "seed44": [2366.68, 2369.43, 2361.11, 2365.55, 2377.06,
                   2395.62, 2411.78, 2424.37, 2436.08, 2451.25, 2466.15],
    },
    "r=0.25": {
        "seed42": [2366.68, 2362.13, 2363.10, 2380.88, 2393.37,
                   2421.22, 2436.38, 2447.08, 2463.81, 2476.58, 2485.01],
        "seed43": [2366.6829, 2365.3518, 2362.5420, 2380.5476, 2395.0469,
                   2414.8440, 2426.5466, 2448.4216, 2465.0208, 2477.8367, 2488.5769],
        "seed44": [2366.68, 2366.13, 2364.59, 2378.05, 2402.71,
                   2415.91, 2437.92, 2456.77, 2463.28, 2482.46, 2490.74],
    },
    "r=0.3": {
        "seed42": [2366.68, 2366.13, 2372.45, 2386.72, 2404.02,
                   2431.17, 2452.00, 2467.05, 2485.91, 2497.30, 2511.13],
        "seed43": [2366.68, 2363.89, 2363.64, 2389.87, 2408.14,
                   2431.29, 2445.24, 2462.25, 2474.35, 2493.43, 2508.33],
        "seed44": [2366.68, 2365.49, 2371.06, 2389.22, 2414.51,
                   2425.20, 2451.59, 2465.51, 2479.89, 2499.64, 2505.25],
    },
    "r=0.5": {
        "seed42": [2366.68, 2366.58, 2395.36, 2425.64, 2451.72,
                   2486.34, 2507.62, 2525.55, 2544.03, 2562.13, 2573.20],
        "seed43": [2366.68, 2361.66, 2393.57, 2419.34, 2454.90,
                   2479.81, 2507.73, 2528.07, 2548.02, 2560.14, 2570.09],
    },
}


def bootstrap_ci(arr_2d, B=10_000, alpha=0.05):
    """arr_2d: (n_seeds, n_gens). Returns mean, ci_lo, ci_hi per gen."""
    n_seeds, n_gens = arr_2d.shape
    boot_means = np.empty((B, n_gens))
    for b in range(B):
        idx = np.random.randint(0, n_seeds, size=n_seeds)
        boot_means[b] = arr_2d[idx].mean(axis=0)
    lo = np.percentile(boot_means, 100 * alpha / 2, axis=0)
    hi = np.percentile(boot_means, 100 * (1 - alpha / 2), axis=0)
    mean = arr_2d.mean(axis=0)
    return mean, lo, hi


def trajectory_metrics(traj):
    """Compute trajectory-level summary metrics for permutation testing."""
    gen0 = traj[0]
    dip_depth = gen0 - np.min(traj[:4])  # how far SLV dips in Gen 0-3
    min_gen = np.argmin(traj[:4])  # which gen has the minimum in early phase
    slope_early = traj[3] - traj[1]  # Gen1→Gen3 slope
    recovery_gen = None
    for g in range(1, len(traj)):
        if traj[g] > gen0:
            recovery_gen = g
            break
    if recovery_gen is None:
        recovery_gen = len(traj)
    return {
        "dip_depth": float(dip_depth),
        "min_gen_early": int(min_gen),
        "slope_gen1_to_gen3": float(slope_early),
        "recovery_gen": int(recovery_gen),
        "final_gain": float(traj[-1] - traj[0]),
    }


def permutation_test_metric(group_a, group_b, metric_fn, n_perm=10_000):
    """Two-sample permutation test on a scalar metric extracted from trajectories."""
    all_trajs = np.vstack([group_a, group_b])
    na = len(group_a)
    observed_diff = abs(metric_fn(group_a).mean() - metric_fn(group_b).mean())
    count = 0
    for _ in range(n_perm):
        perm = np.random.permutation(len(all_trajs))
        a_perm = all_trajs[perm[:na]]
        b_perm = all_trajs[perm[na:]]
        diff = abs(metric_fn(a_perm).mean() - metric_fn(b_perm).mean())
        if diff >= observed_diff:
            count += 1
    return count / n_perm


# ── Main analysis ──
results = {"bootstrap_ci": {}, "permutation_tests": {}, "ci_overlap_analysis": {}}

# 1. Bootstrap CIs
for r_label, seeds_dict in data.items():
    arr = np.array(list(seeds_dict.values()))
    n_seeds = arr.shape[0]
    mean, lo, hi = bootstrap_ci(arr, B=B, alpha=ALPHA)
    ci_width = hi - lo
    results["bootstrap_ci"][r_label] = {
        "n_seeds": n_seeds,
        "generations": GENS,
        "mean": mean.round(2).tolist(),
        "ci_lower": lo.round(2).tolist(),
        "ci_upper": hi.round(2).tolist(),
        "ci_width": ci_width.round(2).tolist(),
    }

# 2. Permutation tests: r=0.25 vs r=0.3
arr_025 = np.array(list(data["r=0.25"].values()))
arr_030 = np.array(list(data["r=0.3"].values()))

metrics_to_test = {
    "slope_gen1_to_gen3": lambda x: np.array([row[3] - row[1] for row in x]),
    "recovery_gen": lambda x: np.array([
        next((g for g in range(1, len(row)) if row[g] > row[0]), len(row))
        for row in x
    ]),
    "final_gain": lambda x: np.array([row[-1] - row[0] for row in x]),
    "dip_depth_gen0_3": lambda x: np.array([row[0] - np.min(row[:4]) for row in x]),
    "gen2_below_gen0": lambda x: np.array([1.0 if row[2] < row[0] else 0.0 for row in x]),
}

for metric_name, metric_fn in metrics_to_test.items():
    vals_025 = metric_fn(arr_025)
    vals_030 = metric_fn(arr_030)
    p_val = permutation_test_metric(arr_025, arr_030, metric_fn, n_perm=B)
    results["permutation_tests"][metric_name] = {
        "r025_values": vals_025.round(4).tolist(),
        "r030_values": vals_030.round(4).tolist(),
        "r025_mean": float(np.round(vals_025.mean(), 4)),
        "r030_mean": float(np.round(vals_030.mean(), 4)),
        "observed_diff": float(np.round(abs(vals_025.mean() - vals_030.mean()), 4)),
        "p_value": float(np.round(p_val, 4)),
    }

# 3. CI overlap analysis for r=0.25 vs r=0.3 at each generation
ci_025 = results["bootstrap_ci"]["r=0.25"]
ci_030 = results["bootstrap_ci"]["r=0.3"]

overlap_by_gen = {}
for g in GENS:
    lo_025, hi_025 = ci_025["ci_lower"][g], ci_025["ci_upper"][g]
    lo_030, hi_030 = ci_030["ci_lower"][g], ci_030["ci_upper"][g]
    overlaps = lo_025 <= hi_030 and lo_030 <= hi_025
    if overlaps:
        overlap_amount = min(hi_025, hi_030) - max(lo_025, lo_030)
    else:
        overlap_amount = -(max(lo_025, lo_030) - min(hi_025, hi_030))  # negative = gap
    overlap_by_gen[f"gen{g}"] = {
        "r025_ci": [round(lo_025, 2), round(hi_025, 2)],
        "r030_ci": [round(lo_030, 2), round(hi_030, 2)],
        "overlaps": overlaps,
        "overlap_or_gap": round(overlap_amount, 2),
    }
results["ci_overlap_analysis"] = overlap_by_gen

# 4. Per-seed trajectory metrics
results["per_seed_metrics"] = {}
for r_label, seeds_dict in data.items():
    results["per_seed_metrics"][r_label] = {}
    for seed_name, traj in seeds_dict.items():
        results["per_seed_metrics"][r_label][seed_name] = trajectory_metrics(traj)

# Save
out_path = Path(__file__).parent / "bootstrap_ci_results.json"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)

# ── Print summary ──
print("=" * 70)
print("BOOTSTRAP 95% CI ANALYSIS — Pythia-410M SLV Trajectories")
print("=" * 70)

for r_label in data:
    ci = results["bootstrap_ci"][r_label]
    n = ci["n_seeds"]
    print(f"\n{'─' * 70}")
    print(f"  {r_label}  (N={n} seeds, B={B})")
    print(f"{'─' * 70}")
    print(f"  Gen │ {'Mean':>9} │ {'CI_lo':>9} │ {'CI_hi':>9} │ {'Width':>8}")
    print(f"  ────┼───────────┼───────────┼───────────┼─────────")
    for g in GENS:
        print(f"  {g:3d} │ {ci['mean'][g]:9.2f} │ {ci['ci_lower'][g]:9.2f} │ {ci['ci_upper'][g]:9.2f} │ {ci['ci_width'][g]:8.2f}")

print(f"\n{'=' * 70}")
print("PERMUTATION TESTS: r=0.25 vs r=0.3")
print(f"{'=' * 70}")
for metric_name, res in results["permutation_tests"].items():
    sig = "***" if res["p_value"] < 0.001 else "**" if res["p_value"] < 0.01 else "*" if res["p_value"] < 0.05 else "n.s."
    print(f"  {metric_name:25s} │ r025={res['r025_mean']:8.2f}  r030={res['r030_mean']:8.2f}  │ diff={res['observed_diff']:7.2f}  p={res['p_value']:.4f} {sig}")

print(f"\n{'=' * 70}")
print("CI OVERLAP: r=0.25 vs r=0.3")
print(f"{'=' * 70}")
print(f"  Gen │ {'r=0.25 CI':>22} │ {'r=0.3 CI':>22} │ Overlap?  │ Amount")
print(f"  ────┼────────────────────────┼────────────────────────┼───────────┼────────")
for g in GENS:
    ov = results["ci_overlap_analysis"][f"gen{g}"]
    ci25 = f"[{ov['r025_ci'][0]:8.2f}, {ov['r025_ci'][1]:8.2f}]"
    ci30 = f"[{ov['r030_ci'][0]:8.2f}, {ov['r030_ci'][1]:8.2f}]"
    flag = "YES" if ov["overlaps"] else "NO "
    print(f"  {g:3d} │ {ci25} │ {ci30} │    {flag}    │ {ov['overlap_or_gap']:7.2f}")

print(f"\nResults saved to {out_path}")
