import json
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations

FACETS = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
SAMPLES = {
    "sample1": "results/exp001b/sample1/all_results.jsonl",
    "sample2": "results/exp001b/sample2/all_results.jsonl",
    "sample3": "results/exp001b/sample3/all_results.jsonl",
}
BASELINE_PATH = "results/analysis/llama_single_model_gstudy.json"
OUTPUT_PATH = "results/analysis/exp001b_resampling_gstudy.json"


def run_gstudy(df, metric="correct"):
    facets = FACETS
    for f in facets:
        df[f] = df[f].astype(str)

    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()
    N = len(df)
    n = {f: df[f].nunique() for f in facets}

    components = {}
    main_means = {}

    for f in facets:
        means = df.groupby(f)[metric].mean()
        main_means[f] = means
        n_per = N // n[f]
        ss = float(n_per * ((means.values - grand_mean) ** 2).sum())
        components[f] = ss

    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, "cell_mean"]
        cell_means["f1_mean"] = cell_means[f1].map(main_means[f1])
        cell_means["f2_mean"] = cell_means[f2].map(main_means[f2])
        n_per = N // (n[f1] * n[f2])
        deviations = cell_means["cell_mean"] - cell_means["f1_mean"] - cell_means["f2_mean"] + grand_mean
        ss = float(n_per * (deviations ** 2).sum())
        components[f"{f1}:{f2}"] = ss

    ss_explained = sum(components.values())
    components["residual"] = max(0.0, SS_total - ss_explained)

    total_var = sum(components.values())
    pct = {k: round(v / total_var * 100, 4) for k, v in components.items()}
    sorted_pct = dict(sorted(pct.items(), key=lambda x: -x[1]))

    G_item = pct.get("item_id", 0) / 100

    item_pct = pct.get("item_id", 0)
    n_items_actual = n["item_id"]
    non_item_pct = sum(v for k, v in pct.items() if k != "item_id")

    d_study = {}
    for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
        G_n = item_pct / (item_pct + non_item_pct * (n_items_actual / ni))
        d_study[str(ni)] = round(G_n, 4)

    min_items_g80 = None
    for ni in range(1, 2001):
        G_n = item_pct / (item_pct + non_item_pct * (n_items_actual / ni))
        if G_n >= 0.80:
            min_items_g80 = ni
            break

    return {
        "grand_mean": round(float(grand_mean), 4),
        "components_pct": sorted_pct,
        "G_item": round(float(G_item), 4),
        "total_variance": round(float(total_var), 4),
        "n_records": int(N),
        "n_items": int(n["item_id"]),
        "n_conditions": int(N // n["item_id"]),
        "n_levels": {k: int(v) for k, v in n.items()},
        "d_study": d_study,
        "min_items_g80": min_items_g80,
    }


def compute_stability(sample_results, keys):
    stability = {}
    for key in keys:
        values = []
        for s in ["sample1", "sample2", "sample3"]:
            v = sample_results[s]["components_pct"].get(key, 0.0)
            values.append(v)
        mean_v = np.mean(values)
        std_v = np.std(values, ddof=1)
        cv = (std_v / mean_v * 100) if mean_v > 0 else float("inf")
        stability[key.replace(":", "_") + "_pct"] = {
            "values": [round(v, 4) for v in values],
            "mean": round(float(mean_v), 4),
            "std": round(float(std_v), 4),
            "cv": round(float(cv), 2),
        }
    g_values = [sample_results[s]["G_item"] for s in ["sample1", "sample2", "sample3"]]
    mean_g = np.mean(g_values)
    std_g = np.std(g_values, ddof=1)
    cv_g = (std_g / mean_g * 100) if mean_g > 0 else float("inf")
    stability["G_item"] = {
        "values": [round(v, 4) for v in g_values],
        "mean": round(float(mean_g), 4),
        "std": round(float(std_g), 4),
        "cv": round(float(cv_g), 2),
    }
    return stability


def main():
    with open(BASELINE_PATH) as f:
        baseline = json.load(f)

    sample_results = {}
    for name, path in SAMPLES.items():
        print(f"\n{'='*60}")
        print(f"Processing {name}: {path}")
        df = pd.read_json(path, lines=True)
        print(f"  Loaded {len(df)} records")
        result = run_gstudy(df, metric="correct")
        sample_results[name] = result
        print(f"  grand_mean={result['grand_mean']}, G_item={result['G_item']}")
        print(f"  Top components:")
        for k, v in list(result["components_pct"].items())[:8]:
            print(f"    {k:30s}: {v:7.2f}%")

    stability_keys = [
        "item_id",
        "prompt_template:item_id",
        "seed:item_id",
        "temperature:item_id",
        "ordering:item_id",
    ]
    stability = compute_stability(sample_results, stability_keys)

    bl_item_pct = baseline["correct"]["components_pct"].get("item_id", 0)
    resamp_item_pcts = [sample_results[s]["components_pct"].get("item_id", 0)
                        for s in ["sample1", "sample2", "sample3"]]
    resamp_mean = float(np.mean(resamp_item_pcts))

    comparison = {
        "exp001_item_id_pct": bl_item_pct,
        "resampling_mean_item_id_pct": round(resamp_mean, 4),
        "delta": round(resamp_mean - bl_item_pct, 4),
        "note": "exp-001 baseline has 6 facets (incl. precision); exp001b has 5 facets (no precision). ~4% precision:item_id variance redistributed.",
    }

    output = {
        "baseline": baseline["correct"],
        "sample1": sample_results["sample1"],
        "sample2": sample_results["sample2"],
        "sample3": sample_results["sample3"],
        "stability": stability,
        "comparison_with_exp001": comparison,
    }

    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {OUTPUT_PATH}")

    # Summary table
    print("\n" + "=" * 100)
    print("SUMMARY COMPARISON TABLE")
    print("=" * 100)

    bl = baseline["correct"]
    header = f"{'Metric':<25} {'exp-001(6f)':>12} {'Sample1':>10} {'Sample2':>10} {'Sample3':>10} {'Mean±Std':>14} {'CV%':>8}"
    print(header)
    print("-" * len(header))

    rows = [
        ("item_id%", "item_id"),
        ("prompt×item%", "prompt_template:item_id"),
        ("seed×item%", "seed:item_id"),
        ("temp×item%", "temperature:item_id"),
        ("order×item%", "ordering:item_id"),
        ("residual%", "residual"),
    ]
    for label, key in rows:
        bl_val = bl["components_pct"].get(key, 0)
        vals = [sample_results[s]["components_pct"].get(key, 0) for s in ["sample1", "sample2", "sample3"]]
        mean_v = np.mean(vals)
        std_v = np.std(vals, ddof=1)
        cv = (std_v / mean_v * 100) if mean_v > 0 else 0
        print(f"{label:<25} {bl_val:>12.2f} {vals[0]:>10.2f} {vals[1]:>10.2f} {vals[2]:>10.2f} {mean_v:>7.2f}±{std_v:<5.2f} {cv:>7.1f}%")

    # G_item row
    bl_g = bl["G_coefficient"]
    g_vals = [sample_results[s]["G_item"] for s in ["sample1", "sample2", "sample3"]]
    g_mean = np.mean(g_vals)
    g_std = np.std(g_vals, ddof=1)
    g_cv = (g_std / g_mean * 100) if g_mean > 0 else 0
    print(f"{'G_item':<25} {bl_g:>12.4f} {g_vals[0]:>10.4f} {g_vals[1]:>10.4f} {g_vals[2]:>10.4f} {g_mean:>7.4f}±{g_std:<5.4f} {g_cv:>7.1f}%")

    # min items for G>=0.80
    bl_d = baseline["correct"].get("d_study_correct", baseline.get("d_study_correct", {}))
    min_items = [sample_results[s]["min_items_g80"] for s in ["sample1", "sample2", "sample3"]]
    min_str = [str(m) if m else ">2000" for m in min_items]
    print(f"{'min_items(G≥0.80)':<25} {'N/A':>12} {min_str[0]:>10} {min_str[1]:>10} {min_str[2]:>10}")

    print("\n" + "=" * 100)
    print("STABILITY ASSESSMENT")
    print("=" * 100)
    all_stable = True
    for key, info in stability.items():
        status = "STABLE" if info["cv"] < 10 else "UNSTABLE"
        if info["cv"] >= 10:
            all_stable = False
        print(f"  {key:<25}: CV = {info['cv']:>6.2f}%  [{status}]  values = {info['values']}")

    print(f"\nOverall: {'ALL STABLE (CV < 10%)' if all_stable else 'SOME COMPONENTS UNSTABLE (CV >= 10%)'}")
    print("DONE")


if __name__ == "__main__":
    main()
