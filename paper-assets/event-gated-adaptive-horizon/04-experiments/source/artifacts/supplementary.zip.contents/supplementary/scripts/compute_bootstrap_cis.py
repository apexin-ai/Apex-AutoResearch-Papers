import json
import numpy as np
import os

np.random.seed(42)

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"
OUTPATH = "/root/autodl-tmp/event-gated-adaptive-horizon/analysis/bootstrap_cis.json"

def bootstrap_ci(data, n_boot=10000, ci=0.95):
    data = np.array(data, dtype=float)
    if len(data) < 2:
        m = float(np.mean(data))
        return {"mean": m, "ci_lower": m, "ci_upper": m, "n": len(data)}
    boot_means = np.array([
        np.mean(np.random.choice(data, size=len(data), replace=True))
        for _ in range(n_boot)
    ])
    alpha = (1 - ci) / 2
    return {
        "mean": float(np.mean(data)),
        "ci_lower": float(np.percentile(boot_means, alpha * 100)),
        "ci_upper": float(np.percentile(boot_means, (1 - alpha) * 100)),
        "n": len(data)
    }

def bootstrap_ci_paired_diff(a, b, n_boot=10000, ci=0.95):
    """Bootstrap CI on paired differences a - b."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    diffs = a - b
    n = len(diffs)
    boot_means = np.array([
        np.mean(np.random.choice(diffs, size=n, replace=True))
        for _ in range(n_boot)
    ])
    alpha = (1 - ci) / 2
    return {
        "mean_diff": float(np.mean(diffs)),
        "ci_lower": float(np.percentile(boot_means, alpha * 100)),
        "ci_upper": float(np.percentile(boot_means, (1 - alpha) * 100)),
        "n": n
    }

def load_metrics(exp_name):
    path = os.path.join(LOGDIR, exp_name, "metrics.jsonl")
    eval_rows = {}
    train_rows = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line.strip())
            step = row.get("step")
            if step is None:
                continue
            if "eval_return" in row:
                if step not in eval_rows:  # skip duplicates, keep first
                    eval_rows[step] = row
            if "value_mean" in row:
                train_rows[step] = row
    return eval_rows, train_rows

def compute_ve_ratio(eval_rows, train_rows):
    results = {}
    for step in sorted(eval_rows.keys()):
        er = eval_rows[step]["eval_return"]
        if step in train_rows and er != 0:
            vm = train_rows[step]["value_mean"]
            results[step] = vm / er
    return results

def interp_to_steps(source_steps, source_vals, target_steps):
    """Linearly interpolate source trajectory to target steps."""
    src_s = np.array(sorted(source_steps))
    src_v = np.array([source_vals[s] for s in sorted(source_steps)])
    tgt = np.array(target_steps)
    mask = (tgt >= src_s[0]) & (tgt <= src_s[-1])
    interped = np.interp(tgt[mask], src_s, src_v)
    return tgt[mask].tolist(), interped.tolist()

results = {}

# ============================================================
# 1. NVE comparison
# ============================================================
print("=== NVE Comparison ===")

bl_eval, bl_train = load_metrics("baseline_s1")
bl_ve = compute_ve_ratio(bl_eval, bl_train)

# exp_008d CIVO trigger
d8_eval, d8_train = load_metrics("exp_008d_subsample_on_h8")
d8_ve = compute_ve_ratio(d8_eval, d8_train)

# NVE at matching steps
nve_008d = {}
for step in sorted(d8_ve.keys()):
    if 35000 <= step <= 105000 and step in bl_ve and bl_ve[step] != 0:
        nve_008d[step] = d8_ve[step] / bl_ve[step]

print(f"exp_008d NVE steps: {sorted(nve_008d.keys())}")
for s, v in sorted(nve_008d.items()):
    print(f"  step {s}: NVE={v:.4f}  (008d_ve={d8_ve[s]:.4f}, bl_ve={bl_ve[s]:.4f})")

results["nve"] = {}
if nve_008d:
    results["nve"]["exp_008d_civo_trigger"] = {
        "description": "NVE = ve_ratio(008d) / ve_ratio(baseline_s1), ve_ratio = value_mean / eval_return",
        "step_range": f"{min(nve_008d.keys())}-{max(nve_008d.keys())}",
        "per_step": {str(k): {"nve": round(v, 6), "exp_ve": round(d8_ve[k], 6), "bl_ve": round(bl_ve[k], 6)} for k, v in sorted(nve_008d.items())},
        "bootstrap_ci": bootstrap_ci(list(nve_008d.values()))
    }

# exp_018: Flag that it shares baseline data
e18_eval, e18_train = load_metrics("exp_018_full_sgs_walker_s1")
e18_ve = compute_ve_ratio(e18_eval, e18_train)
shared = sum(1 for s in e18_ve if s in bl_ve and abs(e18_ve[s] - bl_ve[s]) < 1e-10)
results["nve"]["exp_018_full_sgs"] = {
    "description": "exp_018 shares identical metrics with baseline_s1 at all overlapping steps",
    "note": f"All {shared}/{len(e18_ve)} steps have identical ve_ratio to baseline → NVE=1.0 trivially",
    "total_checkpoints": len(e18_ve),
    "per_step_ve_ratio": {str(k): round(v, 6) for k, v in sorted(e18_ve.items()) if 35000 <= k <= 105000}
}

# Baseline ve_ratio reference
bl_ve_range = {k: v for k, v in bl_ve.items() if 35000 <= k <= 105000}
if bl_ve_range:
    results["nve"]["baseline_s1_ve_ratio_ref"] = {
        "description": "baseline_s1 ve_ratio = value_mean / eval_return (reference denominator)",
        "step_range": f"{min(bl_ve_range.keys())}-{max(bl_ve_range.keys())}",
        "per_step": {str(k): round(v, 6) for k, v in sorted(bl_ve_range.items())},
        "bootstrap_ci": bootstrap_ci(list(bl_ve_range.values()))
    }

# ============================================================
# 2. eval_return seed variability with interpolation
# ============================================================
print("\n=== Seed Variability (with interpolation) ===")

s0_eval, _ = load_metrics("exp_009d_baseline_walker_s0")

bl_steps = sorted(bl_eval.keys())
s0_steps = sorted(s0_eval.keys())
bl_vals = {s: bl_eval[s]["eval_return"] for s in bl_steps}
s0_vals = {s: s0_eval[s]["eval_return"] for s in s0_steps}

# Interpolate s0 to baseline's step grid (since baseline has cleaner 10K spacing)
interp_steps, interp_s0 = interp_to_steps(s0_steps, s0_vals, bl_steps)
bl_at_common = [bl_vals[int(s)] for s in interp_steps]

print(f"Interpolated {len(interp_steps)} common steps: {int(interp_steps[0])}-{int(interp_steps[-1])}")

diff_all = bootstrap_ci_paired_diff(bl_at_common, interp_s0)
print(f"Mean diff (bl - s0): {diff_all['mean_diff']:.2f} [{diff_all['ci_lower']:.2f}, {diff_all['ci_upper']:.2f}]")

results["seed_variability"] = {
    "description": "eval_return: baseline_s1 (seed1) vs exp_009d_s0 (seed0), interpolated to common steps",
    "method": "exp_009d_s0 linearly interpolated to baseline_s1's step grid",
    "n_steps": len(interp_steps),
    "step_range": f"{int(interp_steps[0])}-{int(interp_steps[-1])}",
    "mean_diff_ci": diff_all,
    "baseline_s1_eval_return_ci": bootstrap_ci(bl_at_common),
    "exp_009d_s0_eval_return_ci": bootstrap_ci(interp_s0),
}

# Last 10 checkpoints
if len(interp_steps) >= 10:
    last10_bl = bl_at_common[-10:]
    last10_s0 = interp_s0[-10:]
    results["seed_variability"]["last_10_diff_ci"] = bootstrap_ci_paired_diff(last10_bl, last10_s0)
    results["seed_variability"]["last_10_steps"] = f"{int(interp_steps[-10])}-{int(interp_steps[-1])}"
    print(f"Last 10 diff: {results['seed_variability']['last_10_diff_ci']['mean_diff']:.2f} [{results['seed_variability']['last_10_diff_ci']['ci_lower']:.2f}, {results['seed_variability']['last_10_diff_ci']['ci_upper']:.2f}]")

# ============================================================
# 3. exp_010a Cheetah baseline NVE
# ============================================================
print("\n=== Cheetah Baseline ===")

ch_eval, ch_train = load_metrics("exp_010a_cheetah_baseline_s1")
ch_ve = compute_ve_ratio(ch_eval, ch_train)

if ch_ve:
    sorted_steps = sorted(ch_ve.keys())
    ve_vals = [ch_ve[s] for s in sorted_steps]

    results["cheetah_baseline"] = {
        "description": "exp_010a Cheetah baseline: ve_ratio = value_mean / eval_return",
        "n_checkpoints": len(ch_ve),
        "step_range": f"{min(ch_ve.keys())}-{max(ch_ve.keys())}",
        "ve_ratio_all_ci": bootstrap_ci(ve_vals),
    }

    if len(sorted_steps) >= 10:
        last10_ve = [ch_ve[s] for s in sorted_steps[-10:]]
        results["cheetah_baseline"]["ve_ratio_last10_ci"] = bootstrap_ci(last10_ve)
        results["cheetah_baseline"]["last10_steps"] = f"{sorted_steps[-10]}-{sorted_steps[-1]}"

    ch_er_all = [ch_eval[s]["eval_return"] for s in sorted(ch_eval.keys())]
    results["cheetah_baseline"]["eval_return_all_ci"] = bootstrap_ci(ch_er_all)
    if len(ch_er_all) >= 10:
        results["cheetah_baseline"]["eval_return_last10_ci"] = bootstrap_ci(ch_er_all[-10:])

    # Per-step ve_ratio for key ranges
    results["cheetah_baseline"]["per_step_ve_ratio_35K_105K"] = {
        str(k): round(v, 6) for k, v in sorted(ch_ve.items()) if 35000 <= k <= 105000
    }

    print(f"Cheetah ve_ratio: {len(ch_ve)} checkpoints, all CI: [{results['cheetah_baseline']['ve_ratio_all_ci']['ci_lower']:.4f}, {results['cheetah_baseline']['ve_ratio_all_ci']['ci_upper']:.4f}]")
else:
    results["cheetah_baseline"] = {"error": "No matching value_mean + eval_return steps"}

# ============================================================
# Save
# ============================================================
with open(OUTPATH, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved to {OUTPATH}")
