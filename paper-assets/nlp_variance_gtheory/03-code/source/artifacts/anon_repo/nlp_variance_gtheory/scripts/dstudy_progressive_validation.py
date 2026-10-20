"""D-study Progressive Validation (SF1).

Validates D-study extrapolation stability by running G-studies on
progressively larger item subsets and checking convergence of:
1. Variance component percentages
2. G_item (= item_id ICC)
3. D-study recommendation (min items for G>=0.80), projected from
   a common base (n_base=200) so comparisons are meaningful.
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path
from itertools import combinations

FACETS = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
METRIC = "correct"
N_BASE = 200  # common base for D-study projections


def load_data():
    dfs = []
    for i in range(4):
        path = f"results/exp001_llama/llama_shard_{i}.jsonl"
        dfs.append(pd.read_json(path, lines=True))
    df = pd.concat(dfs, ignore_index=True)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def run_gstudy(df, metric="correct"):
    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in FACETS}

    components = {}
    main_means = {}

    for f in FACETS:
        means = df.groupby(f, observed=True)[metric].mean()
        main_means[f] = means
        n_per = N // n_levels[f]
        ss = n_per * ((means.values - grand_mean) ** 2).sum()
        components[f] = ss

    for f1, f2 in combinations(FACETS, 2):
        cell_means = df.groupby([f1, f2], observed=True)[metric].mean()
        m1 = main_means[f1]
        m2 = main_means[f2]
        n_per = N // (n_levels[f1] * n_levels[f2])
        ss = 0.0
        for (l1, l2), cm in cell_means.items():
            interaction = cm - m1[l1] - m2[l2] + grand_mean
            ss += n_per * interaction ** 2
        components[f"{f1}:{f2}"] = ss

    ss_total = ((y - grand_mean) ** 2).sum()
    ss_explained = sum(components.values())
    components["residual"] = max(0.0, ss_total - ss_explained)

    total_var = sum(components.values())
    pct = {k: v / total_var * 100 for k, v in components.items()}

    return pct, total_var, n_levels


def dstudy_g(item_pct, non_item_pct, n_base, n_target):
    """G = item_pct / (item_pct + non_item_pct * n_base/n_target)"""
    return item_pct / (item_pct + non_item_pct * (n_base / n_target))


def find_min_items_g80(item_pct, non_item_pct, n_base, max_items=5000):
    """Min items for G >= 0.80, projected from n_base."""
    for ni in range(1, max_items + 1):
        g = dstudy_g(item_pct, non_item_pct, n_base, ni)
        if g >= 0.80:
            return ni
    return None


def main():
    print("Loading data...", flush=True)
    df = load_data()
    all_items = sorted(df["item_id"].unique())
    n_total = len(all_items)
    print(f"Total: {len(df)} records, {n_total} items", flush=True)

    subset_sizes = [50, 100, 150]
    seeds = [42, 123, 456]

    results = {"subsets": {}, "convergence": {}, "conclusion": ""}

    for size in subset_sizes:
        results["subsets"][str(size)] = []
        for s in seeds:
            rng = np.random.RandomState(s)
            sampled_items = sorted(rng.choice(all_items, size=size, replace=False))
            sub_df = df[df["item_id"].isin(sampled_items)].copy()

            pct, total_var, n_levels = run_gstudy(sub_df, METRIC)
            item_pct = pct.get("item_id", 0)
            non_item_pct = sum(v for k, v in pct.items() if k != "item_id")
            g_item = item_pct / 100.0

            # D-study: project from N_BASE=200 using this subset's variance ratio
            min_items = find_min_items_g80(item_pct, non_item_pct, N_BASE)

            entry = {
                "seed": s,
                "n_items": size,
                "n_records": len(sub_df),
                "item_id_pct": round(item_pct, 4),
                "components_pct": {k: round(v, 4) for k, v in sorted(pct.items(), key=lambda x: -x[1])},
                "G_item": round(g_item, 4),
                "min_items_G80": min_items,
            }
            results["subsets"][str(size)].append(entry)
            print(f"  size={size}, seed={s}: item_id={item_pct:.2f}%, G={g_item:.4f}, min_G80={min_items}", flush=True)

    # Full 200 items
    print("Running full 200 items...", flush=True)
    pct, total_var, n_levels = run_gstudy(df, METRIC)
    item_pct = pct.get("item_id", 0)
    non_item_pct = sum(v for k, v in pct.items() if k != "item_id")
    g_item = item_pct / 100.0
    min_items = find_min_items_g80(item_pct, non_item_pct, N_BASE)

    results["subsets"]["200"] = [{
        "seed": 0,
        "n_items": 200,
        "n_records": len(df),
        "item_id_pct": round(item_pct, 4),
        "components_pct": {k: round(v, 4) for k, v in sorted(pct.items(), key=lambda x: -x[1])},
        "G_item": round(g_item, 4),
        "min_items_G80": min_items,
    }]
    print(f"  size=200, seed=0: item_id={item_pct:.2f}%, G={g_item:.4f}, min_G80={min_items}", flush=True)

    # Convergence analysis
    metrics_to_track = ["item_id_pct", "G_item", "min_items_G80"]
    convergence = {}

    for metric_name in metrics_to_track:
        conv = {}
        for size in subset_sizes:
            vals = [e[metric_name] for e in results["subsets"][str(size)] if e[metric_name] is not None]
            if vals:
                conv[f"{size}_mean"] = round(float(np.mean(vals)), 4)
                conv[f"{size}_std"] = round(float(np.std(vals)), 4)
                conv[f"{size}_cv"] = round(float(np.std(vals) / np.mean(vals) * 100), 2) if np.mean(vals) != 0 else None

        val_200 = results["subsets"]["200"][0][metric_name]
        conv["200"] = val_200 if not isinstance(val_200, np.floating) else round(float(val_200), 4)

        if f"150_mean" in conv and val_200 is not None and conv["150_mean"] is not None:
            if conv["150_mean"] != 0:
                change = abs(float(val_200) - conv["150_mean"]) / conv["150_mean"] * 100
                conv["150_to_200_change_pct"] = round(change, 2)

        convergence[metric_name] = conv

    results["convergence"] = convergence

    # Conclusion: all three metrics must show <10% change from 150→200
    changes = [convergence[m].get("150_to_200_change_pct", 999) for m in metrics_to_track]
    all_converged = all(c < 10 for c in changes)
    results["conclusion"] = "converged" if all_converged else "not converged"

    out_path = Path("results/analysis/dstudy_progressive_validation.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nConvergence summary:", flush=True)
    for m, c in convergence.items():
        print(f"  {m}: {c}", flush=True)
    print(f"\nConclusion: {results['conclusion']}", flush=True)
    print(f"Saved -> {out_path}", flush=True)


if __name__ == "__main__":
    main()
