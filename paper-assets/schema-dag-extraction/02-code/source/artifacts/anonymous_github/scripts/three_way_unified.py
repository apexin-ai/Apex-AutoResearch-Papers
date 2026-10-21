"""Three-way comparison with FIXED quartile boundaries (conservative bootstrap).

Difference from three_way_comparison.py: quartile boundaries are computed once
from original data, then bootstrap resamples within fixed Q1/Q4 groups.
This is more conservative (wider CIs) than re-computing boundaries per resample.
"""

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ARTIFACTS = Path("./artifacts")

def load_jsonl(path):
    pairs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            pairs.append((d["bcs"], d["accuracy"]))
    return pairs

def load_json_array(path):
    with open(path) as f:
        data = json.load(f)
    return [(d["bcs"], d["accuracy"]) for d in data]

def load_dict_count8(paths):
    pairs = []
    seen_keys = set()
    for p in paths:
        if not p.exists():
            continue
        with open(p) as f:
            data = json.load(f)
        for key, val in data.items():
            if "count_8_random" in key and key not in seen_keys:
                seen_keys.add(key)
                pairs.append((val["bcs"], val["accuracy"]))
    return pairs

def analyze_group_fixed_boundary(pairs, n_boot=10000, seed=42):
    """Bootstrap with FIXED quartile boundaries (conservative)."""
    bcs = np.array([p[0] for p in pairs])
    acc = np.array([p[1] for p in pairs])
    n = len(bcs)

    # Point estimates
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

    # FIXED quartile boundaries
    q25 = float(np.percentile(bcs, 25))
    q75 = float(np.percentile(bcs, 75))
    low_mask = bcs <= q25
    high_mask = bcs >= q75

    n_low = int(low_mask.sum())
    n_high = int(high_mask.sum())

    if n_low == 0 or n_high == 0:
        delta_q4q1 = float("nan")
        delta_ci = (float("nan"), float("nan"))
    else:
        low_accs = acc[low_mask]
        high_accs = acc[high_mask]
        delta_q4q1 = (high_accs.mean() - low_accs.mean()) * 100

        # Bootstrap within fixed groups
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
        "n_batches": n,
        "bcs_mean": float(bcs.mean()),
        "bcs_std": float(bcs.std()),
        "bcs_range": [float(bcs.min()), float(bcs.max())],
        "acc_mean": float(acc.mean()),
        "acc_std": float(acc.std()),
        "slope": float(slope),
        "slope_ci_95": list(slope_ci),
        "slope_stderr": float(stderr),
        "intercept": float(intercept),
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "delta_Q4_Q1_pp": delta_q4q1,
        "delta_Q4_Q1_ci_95": list(delta_ci),
        "bcs_q25": q25,
        "bcs_q75": q75,
        "n_low_bcs": n_low,
        "n_high_bcs": n_high,
        "bootstrap_method": "fixed_boundary",
        "n_bootstrap": n_boot,
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
    na = len(bcs_a)
    rng = np.random.RandomState(seed)

    count = 0
    for _ in range(n_perm):
        perm = rng.permutation(len(combined_bcs))
        g1_bcs, g1_acc = combined_bcs[perm[:na]], combined_acc[perm[:na]]
        g2_bcs, g2_acc = combined_bcs[perm[na:]], combined_acc[perm[na:]]
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

def main():
    # Load all three sources
    sources = {}

    # 16-rel independent
    p16 = ARTIFACTS / "fewrel_16rel_bootstrap" / "results.json"
    if p16.exists():
        sources["16rel_independent"] = load_json_array(p16)
        print(f"[OK] 16rel_independent: {len(sources['16rel_independent'])} batches")

    # 80-pool 16-sub
    p80sub = ARTIFACTS / "fewrel_80pool_16sub" / "results_incremental.jsonl"
    if p80sub.exists():
        sources["80pool_16sub"] = load_jsonl(p80sub)
        print(f"[OK] 80pool_16sub: {len(sources['80pool_16sub'])} batches")

    # 80-rel full
    p80_paths = [
        ARTIFACTS / "fewrel_formal_full" / "eval_exp2.json",
        ARTIFACTS / "fewrel_formal_full" / "eval_exp1.json",
    ]
    d80 = load_dict_count8(p80_paths)
    if d80:
        sources["80rel_full"] = d80
        print(f"[OK] 80rel_full: {len(d80)} batches")

    # Analyze each group with fixed-boundary bootstrap
    n_boot = 10000
    results = {}
    for name, pairs in sources.items():
        print(f"\nAnalyzing {name} (fixed boundary, B={n_boot})...")
        results[name] = analyze_group_fixed_boundary(pairs, n_boot=n_boot, seed=42)
        r = results[name]
        print(f"  Δ(Q4-Q1) = {r['delta_Q4_Q1_pp']:+.2f}pp  "
              f"95% CI [{r['delta_Q4_Q1_ci_95'][0]:+.2f}, {r['delta_Q4_Q1_ci_95'][1]:+.2f}]")
        print(f"  slope = {r['slope']:.4f}  CI [{r['slope_ci_95'][0]:.4f}, {r['slope_ci_95'][1]:.4f}]")
        print(f"  r = {r['pearson_r']:.4f}, p = {r['pearson_p']:.2e}")

    # Permutation tests
    perm_tests = {}
    group_names = list(sources.keys())
    for i in range(len(group_names)):
        for j in range(i + 1, len(group_names)):
            a, b = group_names[i], group_names[j]
            print(f"\nPermutation test: {a} vs {b}...")
            test = permutation_slope_test(sources[a], sources[b], n_perm=5000, seed=42)
            key = f"{a}_vs_{b}"
            perm_tests[key] = test
            sig = ("***" if test["p_value"] < 0.001 else
                   "**" if test["p_value"] < 0.01 else
                   "*" if test["p_value"] < 0.05 else "n.s.")
            print(f"  diff={test['observed_diff']:.4f}, p={test['p_value']:.4f} {sig}")

    # Save
    output = {
        "groups": results,
        "permutation_tests": perm_tests,
        "method": "fixed_boundary_bootstrap",
        "note": "Quartile boundaries fixed from original data; bootstrap resamples within fixed Q1/Q4 groups. More conservative than re-computed boundaries.",
    }
    out_path = ARTIFACTS / "three_way_comparison" / "results_unified.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {out_path}")

    # Compare with original
    orig_path = ARTIFACTS / "three_way_comparison" / "results.json"
    if orig_path.exists():
        with open(orig_path) as f:
            orig = json.load(f)
        print("\n" + "=" * 70)
        print("COMPARISON: original (re-computed) vs unified (fixed boundary)")
        print("=" * 70)
        for name in results:
            if name in orig.get("groups", {}):
                o = orig["groups"][name]
                u = results[name]
                print(f"\n{name}:")
                print(f"  Original CI: [{o['delta_Q4_Q1_ci_95'][0]:+.2f}, {o['delta_Q4_Q1_ci_95'][1]:+.2f}]")
                print(f"  Unified  CI: [{u['delta_Q4_Q1_ci_95'][0]:+.2f}, {u['delta_Q4_Q1_ci_95'][1]:+.2f}]")
                orig_crosses = o['delta_Q4_Q1_ci_95'][0] <= 0 <= o['delta_Q4_Q1_ci_95'][1]
                new_crosses = u['delta_Q4_Q1_ci_95'][0] <= 0 <= u['delta_Q4_Q1_ci_95'][1]
                print(f"  Crosses zero: {orig_crosses} → {new_crosses}")

if __name__ == "__main__":
    main()
