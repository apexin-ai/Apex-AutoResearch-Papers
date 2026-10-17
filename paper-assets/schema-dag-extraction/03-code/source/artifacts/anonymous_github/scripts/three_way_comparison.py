"""Three-way BCS-accuracy comparison across pool sizes."""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ARTIFACTS = Path("./artifacts")

SOURCES = {
    "16rel_independent": {
        "path": ARTIFACTS / "fewrel_16rel_bootstrap" / "results.json",
        "format": "json_array",
        "label": "Independent 16-rel pool",
    },
    "80pool_16sub": {
        "path": ARTIFACTS / "fewrel_80pool_16sub" / "results_incremental.jsonl",
        "format": "jsonl",
        "label": "80-pool → 16-type subset",
    },
    "80rel_full": {
        "paths": [
            ARTIFACTS / "fewrel_formal_full" / "eval_exp2.json",
            ARTIFACTS / "fewrel_formal_full" / "eval_exp1.json",
        ],
        "format": "dict_count8",
        "label": "Full 80-rel pool",
    },
}


def load_json_array(path):
    with open(path) as f:
        data = json.load(f)
    return [(d["bcs"], d["accuracy"]) for d in data]


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


def load_source(name):
    cfg = SOURCES[name]
    fmt = cfg["format"]
    if fmt == "json_array":
        path = cfg["path"]
        if not path.exists():
            return None
        return load_json_array(path)
    elif fmt == "jsonl":
        path = cfg["path"]
        if not path.exists():
            return None
        pairs = load_jsonl(path)
        return pairs if pairs else None
    elif fmt == "dict_count8":
        pairs = load_dict_count8(cfg["paths"])
        return pairs if pairs else None
    return None


def bootstrap_slope(bcs, acc, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(bcs)
    slopes = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        b, a = bcs[idx], acc[idx]
        if np.std(b) < 1e-12:
            continue
        sl, _, _, _, _ = stats.linregress(b, a)
        slopes.append(sl)
    slopes = np.array(slopes)
    return slopes


def analyze_group(pairs, n_boot=1000):
    bcs = np.array([p[0] for p in pairs])
    acc = np.array([p[1] for p in pairs])

    slope, intercept, r_value, p_value, stderr = stats.linregress(bcs, acc)
    pearson_r, pearson_p = stats.pearsonr(bcs, acc)

    boot_slopes = bootstrap_slope(bcs, acc, n_boot=n_boot)
    slope_ci = (float(np.percentile(boot_slopes, 2.5)), float(np.percentile(boot_slopes, 97.5)))

    q25, q75 = np.percentile(bcs, 25), np.percentile(bcs, 75)
    low_mask = bcs <= q25
    high_mask = bcs >= q75
    if low_mask.sum() == 0 or high_mask.sum() == 0:
        delta_q4q1 = float("nan")
        delta_ci = (float("nan"), float("nan"))
    else:
        low_acc = acc[low_mask].mean()
        high_acc = acc[high_mask].mean()
        delta_q4q1 = (high_acc - low_acc) * 100

        deltas_boot = []
        rng = np.random.RandomState(42)
        for _ in range(n_boot):
            idx = rng.randint(0, len(bcs), size=len(bcs))
            b_b, a_b = bcs[idx], acc[idx]
            q25_b, q75_b = np.percentile(b_b, 25), np.percentile(b_b, 75)
            lo = a_b[b_b <= q25_b]
            hi = a_b[b_b >= q75_b]
            if len(lo) > 0 and len(hi) > 0:
                deltas_boot.append((hi.mean() - lo.mean()) * 100)
        deltas_boot = np.array(deltas_boot)
        delta_ci = (float(np.percentile(deltas_boot, 2.5)), float(np.percentile(deltas_boot, 97.5)))

    return {
        "n_batches": len(pairs),
        "bcs_mean": float(bcs.mean()),
        "bcs_std": float(bcs.std()),
        "bcs_range": [float(bcs.min()), float(bcs.max())],
        "acc_mean": float(acc.mean()),
        "acc_std": float(acc.std()),
        "slope": float(slope),
        "slope_ci_95": slope_ci,
        "slope_stderr": float(stderr),
        "intercept": float(intercept),
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "delta_Q4_Q1_pp": float(delta_q4q1),
        "delta_Q4_Q1_ci_95": delta_ci,
        "bcs_q25": float(q25),
        "bcs_q75": float(q75),
        "n_low_bcs": int(low_mask.sum()),
        "n_high_bcs": int(high_mask.sum()),
        "_boot_slopes": boot_slopes,
    }


def permutation_slope_test(pairs_a, pairs_b, n_perm=5000, seed=42):
    """Test H0: slope_a == slope_b via permutation."""
    bcs_a = np.array([p[0] for p in pairs_a])
    acc_a = np.array([p[1] for p in pairs_a])
    bcs_b = np.array([p[0] for p in pairs_b])
    acc_b = np.array([p[1] for p in pairs_b])

    slope_a = stats.linregress(bcs_a, acc_a).slope
    slope_b = stats.linregress(bcs_b, acc_b).slope
    observed_diff = abs(slope_a - slope_b)

    all_bcs = np.concatenate([bcs_a, bcs_b])
    all_acc = np.concatenate([acc_a, acc_b])
    n_a = len(bcs_a)
    rng = np.random.RandomState(seed)

    count = 0
    for _ in range(n_perm):
        perm = rng.permutation(len(all_bcs))
        g1_bcs, g1_acc = all_bcs[perm[:n_a]], all_acc[perm[:n_a]]
        g2_bcs, g2_acc = all_bcs[perm[n_a:]], all_acc[perm[n_a:]]
        s1 = stats.linregress(g1_bcs, g1_acc).slope
        s2 = stats.linregress(g2_bcs, g2_acc).slope
        if abs(s1 - s2) >= observed_diff:
            count += 1

    return {
        "slope_a": float(slope_a),
        "slope_b": float(slope_b),
        "observed_diff": float(observed_diff),
        "p_value": float((count + 1) / (n_perm + 1)),
        "n_permutations": n_perm,
    }


def print_markdown_table(results):
    headers = ["Metric", *[SOURCES[k]["label"] for k in results]]
    rows = [
        ("N batches", *[str(results[k]["n_batches"]) for k in results]),
        ("BCS range", *[f'[{results[k]["bcs_range"][0]:.3f}, {results[k]["bcs_range"][1]:.3f}]' for k in results]),
        ("BCS mean±std", *[f'{results[k]["bcs_mean"]:.3f}±{results[k]["bcs_std"]:.3f}' for k in results]),
        ("Slope", *[f'{results[k]["slope"]:.4f}' for k in results]),
        ("Slope 95% CI", *[f'[{results[k]["slope_ci_95"][0]:.4f}, {results[k]["slope_ci_95"][1]:.4f}]' for k in results]),
        ("Pearson r", *[f'{results[k]["pearson_r"]:.4f}' for k in results]),
        ("Pearson p", *[f'{results[k]["pearson_p"]:.2e}' for k in results]),
        ("Δ(Q4-Q1) pp", *[f'{results[k]["delta_Q4_Q1_pp"]:.2f}' for k in results]),
        ("Δ CI 95%", *[f'[{results[k]["delta_Q4_Q1_ci_95"][0]:.2f}, {results[k]["delta_Q4_Q1_ci_95"][1]:.2f}]' for k in results]),
        ("Acc mean±std", *[f'{results[k]["acc_mean"]:.4f}±{results[k]["acc_std"]:.4f}' for k in results]),
    ]

    col_widths = [max(len(str(row[i])) for row in [headers] + rows) for i in range(len(headers))]
    def fmt_row(row):
        return "| " + " | ".join(str(c).ljust(w) for c, w in zip(row, col_widths)) + " |"

    print(fmt_row(headers))
    print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    for row in rows:
        print(fmt_row(row))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Dry-run: load available data, skip missing")
    parser.add_argument("--n-boot", type=int, default=1000)
    parser.add_argument("--n-perm", type=int, default=5000)
    args = parser.parse_args()

    loaded = {}
    for name in SOURCES:
        data = load_source(name)
        if data is not None:
            loaded[name] = data
            print(f"[OK] {SOURCES[name]['label']}: {len(data)} batches loaded")
        else:
            print(f"[SKIP] {SOURCES[name]['label']}: data not found")

    if not loaded:
        print("\nNo data available. Exiting.")
        sys.exit(1)

    if args.check:
        print(f"\n--check mode: {len(loaded)}/3 sources available. Dry-run complete.")
        for name, pairs in loaded.items():
            bcs_vals = [p[0] for p in pairs]
            acc_vals = [p[1] for p in pairs]
            print(f"  {name}: BCS [{min(bcs_vals):.3f}, {max(bcs_vals):.3f}], "
                  f"Acc [{min(acc_vals):.3f}, {max(acc_vals):.3f}]")
        sys.exit(0)

    if len(loaded) < 2:
        print("\nNeed at least 2 sources for comparison. Only 1 available.")
        sys.exit(1)

    results = {}
    for name, pairs in loaded.items():
        print(f"\nAnalyzing {SOURCES[name]['label']}...")
        res = analyze_group(pairs, n_boot=args.n_boot)
        results[name] = res

    print("\n" + "=" * 80)
    print("THREE-WAY BCS-ACCURACY COMPARISON")
    print("=" * 80 + "\n")
    print_markdown_table(results)

    perm_tests = {}
    group_names = list(loaded.keys())
    for i in range(len(group_names)):
        for j in range(i + 1, len(group_names)):
            a, b = group_names[i], group_names[j]
            print(f"\nPermutation test: {SOURCES[a]['label']} vs {SOURCES[b]['label']}...")
            test = permutation_slope_test(loaded[a], loaded[b], n_perm=args.n_perm)
            key = f"{a}_vs_{b}"
            perm_tests[key] = test
            sig = "***" if test["p_value"] < 0.001 else "**" if test["p_value"] < 0.01 else "*" if test["p_value"] < 0.05 else "n.s."
            print(f"  slope_a={test['slope_a']:.4f}, slope_b={test['slope_b']:.4f}, "
                  f"diff={test['observed_diff']:.4f}, p={test['p_value']:.4f} {sig}")

    output_dir = ARTIFACTS / "three_way_comparison"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = {
        "groups": {k: {kk: vv for kk, vv in v.items() if kk != "_boot_slopes"} for k, v in results.items()},
        "permutation_tests": perm_tests,
    }
    out_path = output_dir / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
