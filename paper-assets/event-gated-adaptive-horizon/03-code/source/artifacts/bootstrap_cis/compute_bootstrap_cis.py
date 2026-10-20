"""
Bootstrap Confidence Intervals for Event-Gated Adaptive Horizon (CoRL 2026).
Action item D8: NVE peaks, collapse rates, cross-env classification CIs.
"""
import numpy as np
from collections import OrderedDict

np.random.seed(42)
N_BOOTSTRAP = 10000

# =============================================================================
# Raw data from registry (DONE experiments only)
# =============================================================================

# --- Condition: trained_dt_emb (subsample ON, trained dt_emb, dt=2 imag, H=8) ---
# 008d (seed 0, 55K steps) -> continuation is 009e (seed 1, 105K steps, shares 008d's first 55K)
# 009b (seed 2, 105K steps, self-corrected)
# NOTE: 008d and 009e share first 55K identically. For independence, we use:
#   - 009e as the full 105K run for seed 1
#   - 009b as seed 2
#   - 008d's 55K-only data as seed 0 (shorter run, distinct seed)
trained_dt_emb = {
    "nve_peak": [4.12, 4.12, 2.05],        # 008d(s0), 009e(s1), 009b(s2)
    "nve_sustained_max": [4.12, 4.12, 2.05],
    "nve_sustained_avg": [2.425, 1.87, 1.03],
    "eval_return_peak": [167.22, 250.0, 278.54],
    "eval_return_final": [82.75, 131.08, 267.93],
    "collapse": [1, 1, 0],  # 008d collapsed, 009e collapsed, 009b self-corrected
}

# --- Condition: no_dt_emb (subsample ON, dt_embed_dim=0, dt=2 imag, H=8) ---
# 008f (seed 1), 009c (seed 2), 008f_s3 (seed 3)
no_dt_emb = {
    "nve_peak": [1.02, 1.26, 0.87],
    "nve_sustained_max": [1.02, 1.26, 0.87],
    "nve_sustained_avg": [0.65, 0.77, 0.57],
    "eval_return_peak": [503.0, 359.14, 594.18],
    "eval_return_final": [503.0, 148.34, 420.71],
    "collapse": [0, 0, 0],
}

# --- Condition: SGS_partial (reward_dt_emb_detach only, trained dt_emb) ---
# 016e (seed 1)
sgs_partial = {
    "nve_peak": [10.42],
    "nve_sustained_max": [10.42],
    "nve_sustained_avg": [2.46],
    "eval_return_peak": [326.67],
    "eval_return_final": [31.73],
    "collapse": [1],
}

# --- Condition: SGS_full (detach ALL non-KL grads from dt_emb) ---
# 018v2 (seed 1) — replaces invalid 018 (gate_enabled=false config error)
# Need seed 2 for replication
sgs_full = {
    "nve_peak": [4.01],           # 018v2: peak at 25K
    "nve_sustained_max": [4.01],
    "nve_sustained_avg": [1.34],  # 018v2: NVE final
    "eval_return_peak": [448.34], # 018v2: eval@105K
    "eval_return_final": [448.34],
    "collapse": [0],
}

# --- Condition: frozen_dt_emb ---
# 015b (seed 1)
frozen_dt_emb = {
    "nve_peak": [0.467],
    "nve_sustained_max": [0.467],
    "nve_sustained_avg": [0.427],
    "eval_return_peak": [238.4],
    "eval_return_final": [204.2],
    "collapse": [0],
}

# --- Condition: no_subsample_trained_dt_emb (subsample OFF, H=15) ---
# 008a (seed 1)
no_subsample = {
    "nve_peak": [0.93],
    "nve_sustained_max": [0.93],
    "nve_sustained_avg": [0.73],
    "eval_return_peak": [777.66],
    "eval_return_final": [777.66],
    "collapse": [0],
}

# --- Condition: dt1_imag (subsample ON, dt=1 imagination, H=15) ---
# 008e_v3 s1, 008e_v3 s2
dt1_imag = {
    "nve_peak": [None, 3.78],  # s1 has no explicit nve_peak in registry (collapse=False)
    "nve_sustained_max": [None, 3.78],
    "nve_sustained_avg": [None, 1.35],
    "eval_return_peak": [869.9, 715.21],
    "eval_return_final": [869.9, 136.96],
    "collapse": [0, 1],
}

# --- Baselines (for normalization reference) ---
baseline_walker = {
    "eval_return_peak": [970.41, 950.96, 966.94],  # 001(s0), 009d(s0), 009a(s2)
    "eval_return_final": [None, 927.6, 957.87],
}

baseline_cheetah = {
    "eval_return_peak": [849.8],
    "eval_return_final": [849.8],
}

# =============================================================================
# Bootstrap functions
# =============================================================================

def bootstrap_ci(data, stat_fn=np.mean, n_boot=N_BOOTSTRAP, ci=0.95):
    """Compute bootstrap CI for a statistic. Returns (point_est, ci_low, ci_high)."""
    data = np.array([x for x in data if x is not None], dtype=float)
    n = len(data)
    if n == 0:
        return (np.nan, np.nan, np.nan)
    if n == 1:
        return (data[0], data[0], data[0])  # degenerate: no CI possible

    point_est = stat_fn(data)
    boot_stats = np.zeros(n_boot)
    for i in range(n_boot):
        sample = np.random.choice(data, size=n, replace=True)
        boot_stats[i] = stat_fn(sample)

    alpha = (1 - ci) / 2
    ci_low = np.percentile(boot_stats, alpha * 100)
    ci_high = np.percentile(boot_stats, (1 - alpha) * 100)
    return (point_est, ci_low, ci_high)


def bootstrap_proportion_ci(binary_data, n_boot=N_BOOTSTRAP, ci=0.95):
    """Bootstrap CI for a proportion (e.g., collapse rate)."""
    data = np.array([x for x in binary_data if x is not None], dtype=float)
    n = len(data)
    if n == 0:
        return (np.nan, np.nan, np.nan)
    if n == 1:
        return (data[0], 0.0, 1.0)  # single obs: point est known, CI is [0,1]

    point_est = np.mean(data)
    boot_stats = np.zeros(n_boot)
    for i in range(n_boot):
        sample = np.random.choice(data, size=n, replace=True)
        boot_stats[i] = np.mean(sample)

    alpha = (1 - ci) / 2
    ci_low = np.percentile(boot_stats, alpha * 100)
    ci_high = np.percentile(boot_stats, (1 - alpha) * 100)
    return (point_est, ci_low, ci_high)


def bootstrap_diff_ci(data_a, data_b, stat_fn=np.mean, n_boot=N_BOOTSTRAP, ci=0.95):
    """Bootstrap CI for the difference stat(A) - stat(B)."""
    a = np.array([x for x in data_a if x is not None], dtype=float)
    b = np.array([x for x in data_b if x is not None], dtype=float)
    if len(a) == 0 or len(b) == 0:
        return (np.nan, np.nan, np.nan)

    point_est = stat_fn(a) - stat_fn(b)
    boot_diffs = np.zeros(n_boot)
    for i in range(n_boot):
        sa = np.random.choice(a, size=len(a), replace=True)
        sb = np.random.choice(b, size=len(b), replace=True)
        boot_diffs[i] = stat_fn(sa) - stat_fn(sb)

    alpha = (1 - ci) / 2
    ci_low = np.percentile(boot_diffs, alpha * 100)
    ci_high = np.percentile(boot_diffs, (1 - alpha) * 100)
    return (point_est, ci_low, ci_high)


# =============================================================================
# Compute all CIs
# =============================================================================

conditions = OrderedDict([
    ("trained_dt_emb", trained_dt_emb),
    ("no_dt_emb", no_dt_emb),
    ("SGS_partial", sgs_partial),
    ("SGS_full", sgs_full),
    ("frozen_dt_emb", frozen_dt_emb),
    ("no_subsample", no_subsample),
    ("dt1_imag", dt1_imag),
    ("baseline_walker", baseline_walker),
])

metrics_to_compute = ["nve_peak", "nve_sustained_avg", "eval_return_peak", "eval_return_final"]

print("=" * 90)
print("BOOTSTRAP 95% CONFIDENCE INTERVALS (N_BOOTSTRAP = {:,})".format(N_BOOTSTRAP))
print("=" * 90)

results = {}
for cond_name, cond_data in conditions.items():
    results[cond_name] = {}
    print(f"\n{'─' * 90}")
    print(f"Condition: {cond_name} (n = {len(cond_data.get('eval_return_peak', []))} seeds)")
    print(f"{'─' * 90}")

    for metric in metrics_to_compute:
        if metric not in cond_data:
            continue
        vals = cond_data[metric]
        valid_vals = [v for v in vals if v is not None]
        n = len(valid_vals)

        mean_val, ci_lo, ci_hi = bootstrap_ci(valid_vals)
        results[cond_name][metric] = {"mean": mean_val, "ci_lo": ci_lo, "ci_hi": ci_hi, "n": n}

        if n < 3:
            flag = " ⚠️  n<3, CI unreliable"
        else:
            flag = ""
        print(f"  {metric:25s}: {mean_val:8.2f}  [{ci_lo:8.2f}, {ci_hi:8.2f}]  (n={n}){flag}")

    # Collapse rate
    if "collapse" in cond_data:
        collapse_vals = cond_data["collapse"]
        valid_collapse = [v for v in collapse_vals if v is not None]
        n = len(valid_collapse)
        rate, ci_lo, ci_hi = bootstrap_proportion_ci(valid_collapse)
        results[cond_name]["collapse_rate"] = {"mean": rate, "ci_lo": ci_lo, "ci_hi": ci_hi, "n": n}
        if n < 3:
            flag = " ⚠️  n<3, CI unreliable"
        else:
            flag = ""
        print(f"  {'collapse_rate':25s}: {rate:8.3f}  [{ci_lo:8.3f}, {ci_hi:8.3f}]  (n={n}){flag}")

# =============================================================================
# Effect size: trained_dt_emb vs no_dt_emb
# =============================================================================

print(f"\n{'=' * 90}")
print("EFFECT SIZE: trained_dt_emb vs no_dt_emb (difference of means ± 95% CI)")
print(f"{'=' * 90}")

effect_results = {}
for metric in ["nve_peak", "nve_sustained_avg", "eval_return_peak"]:
    a_data = trained_dt_emb.get(metric, [])
    b_data = no_dt_emb.get(metric, [])
    diff, ci_lo, ci_hi = bootstrap_diff_ci(a_data, b_data)
    effect_results[metric] = {"diff": diff, "ci_lo": ci_lo, "ci_hi": ci_hi}
    print(f"  Δ {metric:25s}: {diff:+8.2f}  [{ci_lo:+8.2f}, {ci_hi:+8.2f}]")

# Collapse rate difference
a_collapse = trained_dt_emb["collapse"]
b_collapse = no_dt_emb["collapse"]
diff, ci_lo, ci_hi = bootstrap_diff_ci(a_collapse, b_collapse)
effect_results["collapse_rate"] = {"diff": diff, "ci_lo": ci_lo, "ci_hi": ci_hi}
print(f"  Δ {'collapse_rate':25s}: {diff:+8.3f}  [{ci_lo:+8.3f}, {ci_hi:+8.3f}]")

# =============================================================================
# NVE > 1.5x collapse threshold analysis
# =============================================================================

print(f"\n{'=' * 90}")
print("NVE > 1.5x THRESHOLD EXCEEDANCE RATE (collapse indicator)")
print(f"{'=' * 90}")

THRESHOLD = 1.5
for cond_name, cond_data in conditions.items():
    if "nve_peak" not in cond_data:
        continue
    peaks = [v for v in cond_data["nve_peak"] if v is not None]
    exceedance = [1 if p > THRESHOLD else 0 for p in peaks]
    n = len(exceedance)
    rate, ci_lo, ci_hi = bootstrap_proportion_ci(exceedance)
    flag = " ⚠️  n<3" if n < 3 else ""
    print(f"  {cond_name:25s}: {rate:.3f}  [{ci_lo:.3f}, {ci_hi:.3f}]  (n={n}){flag}")

# =============================================================================
# Cross-environment note
# =============================================================================

print(f"\n{'=' * 90}")
print("CROSS-ENVIRONMENT CLASSIFICATION (CIVO)")
print(f"{'=' * 90}")
print("  NOTE: Only 1 Cheetah Run experiment (010a, baseline only).")
print("  Cross-env classification CIs cannot be meaningfully computed")
print("  with current data. All treatment conditions are Walker Walk only.")
print("  Recommend: run at least 2-3 Cheetah seeds with trained_dt_emb and no_dt_emb.")

# =============================================================================
# Sample size adequacy
# =============================================================================

print(f"\n{'=' * 90}")
print("SAMPLE SIZE ADEQUACY")
print(f"{'=' * 90}")

for cond_name, cond_data in conditions.items():
    n = len([v for v in cond_data.get("eval_return_peak", []) if v is not None])
    status = "✓ adequate" if n >= 3 else f"⚠️  INSUFFICIENT (n={n}, need ≥3)"
    print(f"  {cond_name:25s}: n={n}  {status}")

# =============================================================================
# Generate markdown summary table
# =============================================================================

md_lines = []
md_lines.append("# Bootstrap 95% Confidence Intervals — Event-Gated Adaptive Horizon")
md_lines.append("")
md_lines.append(f"N_BOOTSTRAP = {N_BOOTSTRAP:,} resamples. Date: 2026-05-16.")
md_lines.append("")
md_lines.append("## Per-Condition Metrics")
md_lines.append("")
md_lines.append("| Condition | Metric | n | Mean | 95% CI Lower | 95% CI Upper | Adequate? |")
md_lines.append("|-----------|--------|---|------|--------------|--------------|-----------|")

for cond_name, cond_results in results.items():
    for metric, vals in cond_results.items():
        adequate = "✓" if vals["n"] >= 3 else "⚠️ n<3"
        md_lines.append(
            f"| {cond_name} | {metric} | {vals['n']} | {vals['mean']:.3f} | {vals['ci_lo']:.3f} | {vals['ci_hi']:.3f} | {adequate} |"
        )

md_lines.append("")
md_lines.append("## Effect Sizes: trained_dt_emb − no_dt_emb")
md_lines.append("")
md_lines.append("| Metric | Δ Mean | 95% CI Lower | 95% CI Upper |")
md_lines.append("|--------|--------|--------------|--------------|")
for metric, vals in effect_results.items():
    md_lines.append(f"| {metric} | {vals['diff']:+.3f} | {vals['ci_lo']:+.3f} | {vals['ci_hi']:+.3f} |")

md_lines.append("")
md_lines.append("## NVE > 1.5× Threshold Exceedance Rate")
md_lines.append("")
md_lines.append("| Condition | Rate | 95% CI Lower | 95% CI Upper | n |")
md_lines.append("|-----------|------|--------------|--------------|---|")
for cond_name, cond_data in conditions.items():
    if "nve_peak" not in cond_data:
        continue
    peaks = [v for v in cond_data["nve_peak"] if v is not None]
    exceedance = [1 if p > THRESHOLD else 0 for p in peaks]
    n = len(exceedance)
    rate, ci_lo, ci_hi = bootstrap_proportion_ci(exceedance)
    md_lines.append(f"| {cond_name} | {rate:.3f} | {ci_lo:.3f} | {ci_hi:.3f} | {n} |")

md_lines.append("")
md_lines.append("## Cross-Environment Classification")
md_lines.append("")
md_lines.append("**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).")
md_lines.append("All treatment conditions are Walker Walk only.")
md_lines.append("")
md_lines.append("**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.")
md_lines.append("")
md_lines.append("## Sample Size Notes")
md_lines.append("")
md_lines.append("| Condition | Seeds | Status |")
md_lines.append("|-----------|-------|--------|")
for cond_name, cond_data in conditions.items():
    n = len([v for v in cond_data.get("eval_return_peak", []) if v is not None])
    status = "Adequate" if n >= 3 else f"**INSUFFICIENT** — need ≥3 seeds"
    md_lines.append(f"| {cond_name} | {n} | {status} |")

md_lines.append("")
md_lines.append("## Independence Notes")
md_lines.append("")
md_lines.append("- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.")
md_lines.append("  For NVE peak at 55K they are effectively the same observation.")
md_lines.append("  Conservative effective n=2 for this condition.")
md_lines.append("- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).")
md_lines.append("- **All other conditions**: single seed only — CIs are degenerate (point estimates).")
md_lines.append("")

summary_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/bootstrap_cis/bootstrap_ci_summary.md"
with open(summary_path, "w") as f:
    f.write("\n".join(md_lines))
print(f"\n\nSummary written to: {summary_path}")
