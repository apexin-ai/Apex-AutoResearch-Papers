"""BCS MAX→MEAN fix: recompute all BCS values and re-run statistics."""
import json
import sys
from pathlib import Path

import numpy as np
import torch
from scipy import stats

BASE = Path(".")
ARTIFACTS = BASE / "artifacts"
OUTPUT_DIR = ARTIFACTS / "bcs_fix"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ====== BCS Functions ======
def compute_bcs_max(type_subset, sim_matrix, type_to_idx):
    """OLD: BCS = max pairwise cosine similarity."""
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    max_sim = float("-inf")
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            val = sim_matrix[indices[i], indices[j]].item()
            if val > max_sim:
                max_sim = val
    return max_sim

def compute_bcs_mean(type_subset, sim_matrix, type_to_idx):
    """NEW: BCS = mean pairwise cosine similarity."""
    if len(type_subset) < 2:
        return 0.0
    indices = [type_to_idx[t] for t in type_subset]
    total = 0.0
    count = 0
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            total += sim_matrix[indices[i], indices[j]].item()
            count += 1
    return total / count

# ====== Load Data ======
print("Loading 16-rel sim matrix...")
sim16 = torch.load(ARTIFACTS / "fewrel_16rel_bootstrap/relation_sim_matrix.pt", map_location="cpu")
sim_matrix_16 = sim16["sim_matrix"]
type_to_idx_16 = sim16["type_to_idx"]

print("Loading 80-rel sim matrix...")
sim80 = torch.load(ARTIFACTS / "fewrel_formal_full/relation_sim_matrix.pt", map_location="cpu")
sim_matrix_80 = sim80["sim_matrix"]
type_to_idx_80 = sim80["type_to_idx"]

# ====== 16-rel bootstrap (100 batches) ======
print("\n=== 16-rel bootstrap (100 batches) ===")
with open(ARTIFACTS / "fewrel_16rel_bootstrap/results.json") as f:
    results_16 = json.load(f)

pairs_16_old = []
pairs_16_new = []
for r in results_16:
    types = r["types"]
    old_bcs = r["bcs"]  # This was MAX
    new_bcs = compute_bcs_mean(types, sim_matrix_16, type_to_idx_16)
    pairs_16_old.append((old_bcs, r["accuracy"]))
    pairs_16_new.append((new_bcs, r["accuracy"]))

old_bcs_16 = [p[0] for p in pairs_16_old]
new_bcs_16 = [p[0] for p in pairs_16_new]
print(f"  OLD (MAX): range=[{min(old_bcs_16):.4f}, {max(old_bcs_16):.4f}], mean={np.mean(old_bcs_16):.4f}")
print(f"  NEW (MEAN): range=[{min(new_bcs_16):.4f}, {max(new_bcs_16):.4f}], mean={np.mean(new_bcs_16):.4f}")
assert np.mean(new_bcs_16) <= np.mean(old_bcs_16), "MEAN should be <= MAX"

# ====== 80-rel full (count_8_random batches from exp2/exp1) ======
print("\n=== 80-rel full (count_8_random batches) ===")
pairs_80_old = []
pairs_80_new = []
seen_keys = set()
for fname in ["eval_exp2.json", "eval_exp1.json"]:
    p = ARTIFACTS / "fewrel_formal_full" / fname
    if not p.exists():
        continue
    with open(p) as f:
        data = json.load(f)
    for key, val in data.items():
        if "count_8_random" in key and key not in seen_keys:
            seen_keys.add(key)
            types = val["batch_types"]
            old_bcs = val["bcs"]  # This was MAX
            new_bcs = compute_bcs_mean(types, sim_matrix_80, type_to_idx_80)
            pairs_80_old.append((old_bcs, val["accuracy"]))
            pairs_80_new.append((new_bcs, val["accuracy"]))

old_bcs_80 = [p[0] for p in pairs_80_old]
new_bcs_80 = [p[0] for p in pairs_80_new]
print(f"  Found {len(pairs_80_old)} batches")
print(f"  OLD (MAX): range=[{min(old_bcs_80):.4f}, {max(old_bcs_80):.4f}], mean={np.mean(old_bcs_80):.4f}")
print(f"  NEW (MEAN): range=[{min(new_bcs_80):.4f}, {max(new_bcs_80):.4f}], mean={np.mean(new_bcs_80):.4f}")
assert np.mean(new_bcs_80) <= np.mean(old_bcs_80), "MEAN should be <= MAX"

# ====== 80-pool 16-sub (verify it's already MEAN) ======
print("\n=== 80-pool 16-sub (100 batches, verify MEAN) ===")
pairs_80sub = []
with open(ARTIFACTS / "fewrel_80pool_16sub/results_incremental.jsonl") as f:
    for line in f:
        if line.strip():
            d = json.loads(line)
            pairs_80sub.append((d["bcs"], d["accuracy"]))

# Verify: recompute a few BCS values from the batch config
with open(ARTIFACTS / "fewrel_80pool_16sub/batch_config.json") as f:
    bc_80sub = json.load(f)

# The 80pool_16sub uses the same 80-rel sim matrix
mismatches = 0
for batch in bc_80sub[:10]:
    types = batch["types"]
    stored_bcs = batch["bcs"]
    recomputed_mean = compute_bcs_mean(types, sim_matrix_80, type_to_idx_80)
    if abs(stored_bcs - recomputed_mean) > 0.001:
        mismatches += 1
        print(f"  MISMATCH batch {batch['batch_id']}: stored={stored_bcs:.6f}, recomputed_mean={recomputed_mean:.6f}")

if mismatches == 0:
    print("  VERIFIED: 80pool_16sub BCS matches MEAN computation ✓")
else:
    print(f"  WARNING: {mismatches}/10 mismatches!")

bcs_80sub = [p[0] for p in pairs_80sub]
print(f"  BCS: range=[{min(bcs_80sub):.4f}, {max(bcs_80sub):.4f}], mean={np.mean(bcs_80sub):.4f}")

# ====== Analysis Functions ======
def analyze_group(pairs, n_boot=10000, seed=42):
    """Full regression + quartile analysis with bootstrap CI."""
    bcs = np.array([p[0] for p in pairs])
    acc = np.array([p[1] for p in pairs])
    n = len(bcs)

    slope, intercept, r_value, p_value, stderr = stats.linregress(bcs, acc)
    pearson_r, pearson_p = stats.pearsonr(bcs, acc)

    # Bootstrap slope
    rng = np.random.RandomState(seed)
    boot_slopes = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        b, a = bcs[idx], acc[idx]
        if np.std(b) < 1e-12:
            continue
        sl, _, _, _, _ = stats.linregress(b, a)
        boot_slopes.append(sl)
    boot_slopes = np.array(boot_slopes)
    slope_ci = (float(np.percentile(boot_slopes, 2.5)),
                float(np.percentile(boot_slopes, 97.5)))

    # Fixed quartile boundaries
    q25 = float(np.percentile(bcs, 25))
    q75 = float(np.percentile(bcs, 75))
    low_mask = bcs <= q25
    high_mask = bcs >= q75
    n_low = int(low_mask.sum())
    n_high = int(high_mask.sum())

    if n_low == 0 or n_high == 0:
        delta_pp = float("nan")
        delta_ci = (float("nan"), float("nan"))
        low_acc_mean = float("nan")
        high_acc_mean = float("nan")
    else:
        low_accs = acc[low_mask]
        high_accs = acc[high_mask]
        low_acc_mean = float(low_accs.mean())
        high_acc_mean = float(high_accs.mean())
        delta_pp = (high_accs.mean() - low_accs.mean()) * 100

        rng2 = np.random.RandomState(seed)
        boot_deltas = []
        for _ in range(n_boot):
            b_lo = rng2.choice(low_accs, size=len(low_accs), replace=True)
            b_hi = rng2.choice(high_accs, size=len(high_accs), replace=True)
            boot_deltas.append((b_hi.mean() - b_lo.mean()) * 100)
        boot_deltas = np.array(boot_deltas)
        delta_ci = (float(np.percentile(boot_deltas, 2.5)),
                    float(np.percentile(boot_deltas, 97.5)))

    return {
        "n": n,
        "slope": float(slope),
        "slope_ci": list(slope_ci),
        "intercept": float(intercept),
        "r": float(pearson_r),
        "p": float(pearson_p),
        "bcs_mean": float(bcs.mean()),
        "bcs_std": float(bcs.std()),
        "bcs_range": [float(bcs.min()), float(bcs.max())],
        "bcs_q25": q25,
        "bcs_median": float(np.median(bcs)),
        "bcs_q75": q75,
        "bcs_iqr": q75 - q25,
        "acc_mean": float(acc.mean()),
        "acc_std": float(acc.std()),
        "delta_pp": delta_pp,
        "delta_ci": list(delta_ci),
        "low_bcs_mean_acc": low_acc_mean,
        "high_bcs_mean_acc": high_acc_mean,
        "n_low_bcs": n_low,
        "n_high_bcs": n_high,
    }

def permutation_slope_test(pairs_a, pairs_b, n_perm=5000, seed=42):
    bcs_a = np.array([p[0] for p in pairs_a])
    acc_a = np.array([p[1] for p in pairs_a])
    bcs_b = np.array([p[0] for p in pairs_b])
    acc_b = np.array([p[1] for p in pairs_b])

    slope_a = stats.linregress(bcs_a, acc_a).slope
    slope_b = stats.linregress(bcs_b, acc_b).slope
    obs_diff = abs(slope_a - slope_b)

    combined_bcs = np.concatenate([bcs_a, bcs_b])
    combined_acc = np.concatenate([acc_a, acc_b])
    n_a = len(bcs_a)
    rng = np.random.RandomState(seed)
    count = 0
    for _ in range(n_perm):
        perm = rng.permutation(len(combined_bcs))
        g1_bcs = combined_bcs[perm[:n_a]]
        g1_acc = combined_acc[perm[:n_a]]
        g2_bcs = combined_bcs[perm[n_a:]]
        g2_acc = combined_acc[perm[n_a:]]
        if np.std(g1_bcs) < 1e-12 or np.std(g2_bcs) < 1e-12:
            continue
        s1 = stats.linregress(g1_bcs, g1_acc).slope
        s2 = stats.linregress(g2_bcs, g2_acc).slope
        if abs(s1 - s2) >= obs_diff:
            count += 1
    return {
        "slope_a": float(slope_a),
        "slope_b": float(slope_b),
        "observed_diff": float(obs_diff),
        "p_value": (count + 1) / (n_perm + 1),
        "n_permutations": n_perm,
    }

# ====== Run Analysis ======
print("\n" + "=" * 70)
print("REGRESSION ANALYSIS (NEW: MEAN BCS)")
print("=" * 70)

reg_new_16 = analyze_group(pairs_16_new, n_boot=10000, seed=42)
print(f"\n16rel: slope={reg_new_16['slope']:.4f} CI{reg_new_16['slope_ci']}, r={reg_new_16['r']:.4f}, p={reg_new_16['p']:.2e}")
print(f"  Δ(Q4-Q1)={reg_new_16['delta_pp']:+.2f}pp CI[{reg_new_16['delta_ci'][0]:+.2f}, {reg_new_16['delta_ci'][1]:+.2f}]")

reg_new_80sub = analyze_group(pairs_80sub, n_boot=10000, seed=42)
print(f"\n80pool_16sub: slope={reg_new_80sub['slope']:.4f} CI{reg_new_80sub['slope_ci']}, r={reg_new_80sub['r']:.4f}, p={reg_new_80sub['p']:.2e}")
print(f"  Δ(Q4-Q1)={reg_new_80sub['delta_pp']:+.2f}pp CI[{reg_new_80sub['delta_ci'][0]:+.2f}, {reg_new_80sub['delta_ci'][1]:+.2f}]")

reg_new_80 = analyze_group(pairs_80_new, n_boot=10000, seed=42)
print(f"\n80rel: slope={reg_new_80['slope']:.4f} CI{reg_new_80['slope_ci']}, r={reg_new_80['r']:.4f}, p={reg_new_80['p']:.2e}")
print(f"  Δ(Q4-Q1)={reg_new_80['delta_pp']:+.2f}pp CI[{reg_new_80['delta_ci'][0]:+.2f}, {reg_new_80['delta_ci'][1]:+.2f}]")

# OLD analysis for comparison
print("\n" + "=" * 70)
print("REGRESSION ANALYSIS (OLD: MAX BCS)")
print("=" * 70)

reg_old_16 = analyze_group(pairs_16_old, n_boot=10000, seed=42)
print(f"\n16rel: slope={reg_old_16['slope']:.4f} CI{reg_old_16['slope_ci']}, r={reg_old_16['r']:.4f}, p={reg_old_16['p']:.2e}")

reg_old_80 = analyze_group(pairs_80_old, n_boot=10000, seed=42)
print(f"\n80rel: slope={reg_old_80['slope']:.4f} CI{reg_old_80['slope_ci']}, r={reg_old_80['r']:.4f}, p={reg_old_80['p']:.2e}")

# Permutation test: 16rel vs 80pool slopes
print("\n" + "=" * 70)
print("PERMUTATION TESTS (NEW BCS)")
print("=" * 70)

perm_16_vs_80sub = permutation_slope_test(pairs_16_new, pairs_80sub, n_perm=5000, seed=42)
print(f"\n16rel vs 80pool_16sub: diff={perm_16_vs_80sub['observed_diff']:.4f}, p={perm_16_vs_80sub['p_value']:.4f}")

perm_16_vs_80 = permutation_slope_test(pairs_16_new, pairs_80_new, n_perm=5000, seed=42)
print(f"16rel vs 80rel: diff={perm_16_vs_80['observed_diff']:.4f}, p={perm_16_vs_80['p_value']:.4f}")

perm_80sub_vs_80 = permutation_slope_test(pairs_80sub, pairs_80_new, n_perm=5000, seed=42)
print(f"80pool_16sub vs 80rel: diff={perm_80sub_vs_80['observed_diff']:.4f}, p={perm_80sub_vs_80['p_value']:.4f}")

# ====== Practical magnitude (IQR-based gap for 16-rel) ======
bcs_16_new = np.array([p[0] for p in pairs_16_new])
acc_16 = np.array([p[1] for p in pairs_16_new])
iqr_16 = float(np.percentile(bcs_16_new, 75) - np.percentile(bcs_16_new, 25))
gap_pp = reg_new_16["slope"] * iqr_16 * 100
# CI
rng = np.random.RandomState(42)
n = len(bcs_16_new)
boot_gaps = []
for _ in range(10000):
    idx = rng.randint(0, n, size=n)
    b, a = bcs_16_new[idx], acc_16[idx]
    if np.std(b) < 1e-12:
        continue
    sl = stats.linregress(b, a).slope
    iq = float(np.percentile(b, 75) - np.percentile(b, 25))
    boot_gaps.append(sl * iq * 100)
boot_gaps = np.array(boot_gaps)
gap_ci = [float(np.percentile(boot_gaps, 2.5)), float(np.percentile(boot_gaps, 97.5))]

print(f"\nPractical magnitude (16-rel): IQR={iqr_16:.4f}, gap={gap_pp:+.2f}pp CI[{gap_ci[0]:+.2f}, {gap_ci[1]:+.2f}]")

# ====== Build output ======
output = {
    "fix_summary": {
        "16rel_batches_affected": 100,
        "80rel_batches_affected": len(pairs_80_old),
        "80pool_16sub_batches_affected": 0,
        "old_definition": "MAX pairwise SCS",
        "new_definition": "MEAN pairwise SCS",
    },
    "bcs_comparison": {
        "16rel": {
            "old_range": [min(old_bcs_16), max(old_bcs_16)],
            "new_range": [min(new_bcs_16), max(new_bcs_16)],
            "old_mean": float(np.mean(old_bcs_16)),
            "new_mean": float(np.mean(new_bcs_16)),
        },
        "80rel": {
            "old_range": [min(old_bcs_80), max(old_bcs_80)],
            "new_range": [min(new_bcs_80), max(new_bcs_80)],
            "old_mean": float(np.mean(old_bcs_80)),
            "new_mean": float(np.mean(new_bcs_80)),
        },
    },
    "regression_new": {
        "16rel": {k: reg_new_16[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
        "80pool_16sub": {k: reg_new_80sub[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
        "80rel": {k: reg_new_80[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
    },
    "regression_old": {
        "16rel": {k: reg_old_16[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
        "80pool_16sub": {k: reg_new_80sub[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
        "80rel": {k: reg_old_80[k] for k in ["slope", "slope_ci", "r", "p", "n"]},
    },
    "permutation_test": {
        "16rel_vs_80pool_16sub": perm_16_vs_80sub,
        "16rel_vs_80rel": perm_16_vs_80,
        "80pool_16sub_vs_80rel": perm_80sub_vs_80,
    },
    "quartile_analysis": {
        "16rel": {
            "delta_pp": reg_new_16["delta_pp"],
            "ci": reg_new_16["delta_ci"],
            "low_bcs_mean_acc": reg_new_16["low_bcs_mean_acc"],
            "high_bcs_mean_acc": reg_new_16["high_bcs_mean_acc"],
            "n_low": reg_new_16["n_low_bcs"],
            "n_high": reg_new_16["n_high_bcs"],
        },
        "80pool_16sub": {
            "delta_pp": reg_new_80sub["delta_pp"],
            "ci": reg_new_80sub["delta_ci"],
            "low_bcs_mean_acc": reg_new_80sub["low_bcs_mean_acc"],
            "high_bcs_mean_acc": reg_new_80sub["high_bcs_mean_acc"],
            "n_low": reg_new_80sub["n_low_bcs"],
            "n_high": reg_new_80sub["n_high_bcs"],
        },
        "80rel": {
            "delta_pp": reg_new_80["delta_pp"],
            "ci": reg_new_80["delta_ci"],
            "low_bcs_mean_acc": reg_new_80["low_bcs_mean_acc"],
            "high_bcs_mean_acc": reg_new_80["high_bcs_mean_acc"],
            "n_low": reg_new_80["n_low_bcs"],
            "n_high": reg_new_80["n_high_bcs"],
        },
    },
    "bcs_distribution": {
        "16rel": {
            "min": reg_new_16["bcs_range"][0], "max": reg_new_16["bcs_range"][1],
            "q25": reg_new_16["bcs_q25"], "median": reg_new_16["bcs_median"],
            "q75": reg_new_16["bcs_q75"], "iqr": reg_new_16["bcs_iqr"],
        },
        "80pool_16sub": {
            "min": reg_new_80sub["bcs_range"][0], "max": reg_new_80sub["bcs_range"][1],
            "q25": reg_new_80sub["bcs_q25"], "median": reg_new_80sub["bcs_median"],
            "q75": reg_new_80sub["bcs_q75"], "iqr": reg_new_80sub["bcs_iqr"],
        },
        "80rel": {
            "min": reg_new_80["bcs_range"][0], "max": reg_new_80["bcs_range"][1],
            "q25": reg_new_80["bcs_q25"], "median": reg_new_80["bcs_median"],
            "q75": reg_new_80["bcs_q75"], "iqr": reg_new_80["bcs_iqr"],
        },
    },
    "practical_magnitude": {
        "iqr": iqr_16,
        "gap_pp": gap_pp,
        "ci": gap_ci,
    },
}

with open(OUTPUT_DIR / "bcs_fix_results.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nSaved results to {OUTPUT_DIR / 'bcs_fix_results.json'}")

# Also save to exp_docred_confusability for reference
alt_path = ARTIFACTS / "exp_docred_confusability" / "bcs_fix_results.json"
alt_path.parent.mkdir(parents=True, exist_ok=True)
with open(alt_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"Also saved to {alt_path}")
