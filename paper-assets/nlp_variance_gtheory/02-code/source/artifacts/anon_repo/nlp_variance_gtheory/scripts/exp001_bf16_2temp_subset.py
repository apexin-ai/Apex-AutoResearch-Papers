"""Exp-001 BF16-only x 2-temp subset analysis for W13 rebuttal.

Compare Henderson Method I variance decomposition between:
  - Full design: 3 prec x 3 temp x 6 prompt x 6 seed x 4 ordering x 200 items
  - Reduced design: bf16 x 2 temp (0.0, 0.7) x 6 prompt x 6 seed x 4 ordering x 200 items
"""

import json
import numpy as np
import pandas as pd
from itertools import combinations
from pathlib import Path

DATA_PATH = Path("./results/analysis/llama_full_259200.csv")
OUTPUT_DIR = Path("./results")
OUTPUT_PATH = OUTPUT_DIR / "exp001_bf16_2temp_comparison.json"


def henderson_i(df, facets, metric="correct"):
    for f in facets:
        df[f] = df[f].astype(str)

    y = df[metric].values.astype(np.float64)
    grand_mean = y.mean()
    SS_total = ((y - grand_mean) ** 2).sum()
    N = len(df)
    n = {f: df[f].nunique() for f in facets}

    ss = {}
    df_eff = {}
    main_means = {}

    for f in facets:
        means = df.groupby(f)[metric].mean()
        main_means[f] = means
        n_per = N // n[f]
        ss[f] = float(n_per * ((means.values - grand_mean) ** 2).sum())
        df_eff[f] = n[f] - 1

    for f1, f2 in combinations(facets, 2):
        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
        cell_means.columns = [f1, f2, "cell_mean"]
        cell_means["f1_mean"] = cell_means[f1].map(main_means[f1])
        cell_means["f2_mean"] = cell_means[f2].map(main_means[f2])
        n_per = N // (n[f1] * n[f2])
        deviations = cell_means["cell_mean"] - cell_means["f1_mean"] - cell_means["f2_mean"] + grand_mean
        key = f"{f1}:{f2}"
        ss[key] = float(n_per * (deviations ** 2).sum())
        df_eff[key] = (n[f1] - 1) * (n[f2] - 1)

    ss_explained = sum(ss.values())
    ss["residual"] = max(0.0, SS_total - ss_explained)
    df_explained = sum(df_eff.values())
    df_eff["residual"] = N - 1 - df_explained

    ms = {}
    for key in ss:
        if df_eff[key] > 0:
            ms[key] = ss[key] / df_eff[key]
        else:
            ms[key] = 0.0

    k = len(facets)
    sigma2 = {}

    sigma2["residual"] = ms["residual"]

    for f1, f2 in combinations(facets, 2):
        key = f"{f1}:{f2}"
        c = N / (n[f1] * n[f2])
        sigma2[key] = (ms[key] - ms["residual"]) / c

    for f in facets:
        interaction_ms_sum = 0.0
        for other in facets:
            if other == f:
                continue
            key = f"{f}:{other}" if f"{f}:{other}" in ms else f"{other}:{f}"
            interaction_ms_sum += ms[key]
        c_f = N / n[f]
        sigma2[f] = (ms[f] - interaction_ms_sum + (k - 2) * ms["residual"]) / c_f

    for key in sigma2:
        if sigma2[key] < 0:
            sigma2[key] = 0.0

    total_var = sum(sigma2.values())
    if total_var == 0:
        pct = {k_: 0.0 for k_ in sigma2}
    else:
        pct = {k_: round(v / total_var * 100, 4) for k_, v in sigma2.items()}

    sorted_pct = dict(sorted(pct.items(), key=lambda x: -x[1]))
    sorted_sigma2 = dict(sorted(sigma2.items(), key=lambda x: -x[1]))

    item_facet = "item_id"
    non_item_facets = [f for f in facets if f != item_facet]

    if item_facet in sigma2:
        sigma2_item = sigma2[item_facet]
        sigma2_delta = 0.0
        for f1, f2 in combinations(facets, 2):
            key = f"{f1}:{f2}" if f"{f1}:{f2}" in sigma2 else f"{f2}:{f1}"
            if item_facet in (f1, f2):
                other = f2 if f1 == item_facet else f1
                sigma2_delta += sigma2[key] / n[other]
        prod_non_item = 1
        for f in non_item_facets:
            prod_non_item *= n[f]
        sigma2_delta += sigma2["residual"] / prod_non_item

        G_item = sigma2_item / (sigma2_item + sigma2_delta) if (sigma2_item + sigma2_delta) > 0 else 0.0
    else:
        G_item = 0.0

    d_study = {}
    if item_facet in sigma2 and sigma2[item_facet] > 0:
        n_items_actual = n[item_facet]
        for ni in [25, 50, 75, 100, 150, 200, 300, 500]:
            scale = n_items_actual / ni
            G_n = sigma2_item / (sigma2_item + sigma2_delta * scale)
            d_study[str(ni)] = round(G_n, 4)

    return {
        "grand_mean": round(float(grand_mean), 4),
        "n_records": int(N),
        "n_items": int(n.get("item_id", 0)),
        "facets": facets,
        "n_levels": {k_: int(v) for k_, v in n.items()},
        "variance_components": {k_: round(v, 8) for k_, v in sorted_sigma2.items()},
        "variance_pct": sorted_pct,
        "G_item": round(float(G_item), 4),
        "d_study": d_study,
    }


def main():
    print("Loading data...", flush=True)
    df = pd.read_csv(DATA_PATH)
    print(f"Total records: {len(df)}", flush=True)
    print(f"Precisions: {sorted(df['precision'].unique())}", flush=True)
    print(f"Temperatures: {sorted(df['temperature'].unique())}", flush=True)

    print("\n" + "=" * 60, flush=True)
    print("FULL DESIGN: 3 prec x 3 temp x 6 prompt x 6 seed x 4 ord x 200 items", flush=True)
    full_facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
    full_result = henderson_i(df.copy(), full_facets)
    print(f"  N = {full_result['n_records']}", flush=True)
    print(f"  Grand mean = {full_result['grand_mean']}", flush=True)
    print(f"  G_item = {full_result['G_item']}", flush=True)
    print("  Variance components (%):", flush=True)
    for comp, p in full_result["variance_pct"].items():
        if p >= 0.01:
            print(f"    {comp:30s}: {p:7.2f}%", flush=True)

    print("\n" + "=" * 60, flush=True)
    print("REDUCED DESIGN: bf16 x 2 temp (0.0, 0.7) x 6 prompt x 6 seed x 4 ord x 200 items", flush=True)
    df_reduced = df[(df["precision"] == "bf16") & (df["temperature"].isin([0.0, 0.7]))].copy()
    reduced_facets = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
    reduced_result = henderson_i(df_reduced, reduced_facets)
    print(f"  N = {reduced_result['n_records']}", flush=True)
    print(f"  Grand mean = {reduced_result['grand_mean']}", flush=True)
    print(f"  G_item = {reduced_result['G_item']}", flush=True)
    print("  Variance components (%):", flush=True)
    for comp, p in reduced_result["variance_pct"].items():
        if p >= 0.01:
            print(f"    {comp:30s}: {p:7.2f}%", flush=True)

    print("\n" + "=" * 60, flush=True)
    print("COMPARISON", flush=True)

    item_pct_full = full_result["variance_pct"].get("item_id", 0)
    item_pct_reduced = reduced_result["variance_pct"].get("item_id", 0)
    item_pct_diff = item_pct_reduced - item_pct_full

    g_full = full_result["G_item"]
    g_reduced = reduced_result["G_item"]
    g_diff = g_reduced - g_full

    shared_keys = set()
    for k in reduced_result["variance_pct"]:
        if k in full_result["variance_pct"]:
            shared_keys.add(k)
    max_diff = 0.0
    max_diff_comp = ""
    for k in shared_keys:
        diff = abs(reduced_result["variance_pct"][k] - full_result["variance_pct"][k])
        if diff > max_diff:
            max_diff = diff
            max_diff_comp = k

    threshold = 5.0
    confounding = abs(item_pct_diff) >= threshold

    print(f"  item_id%  full={item_pct_full:.2f}%  reduced={item_pct_reduced:.2f}%  diff={item_pct_diff:+.2f}pp", flush=True)
    print(f"  G_item    full={g_full:.4f}     reduced={g_reduced:.4f}     diff={g_diff:+.4f}", flush=True)
    print(f"  Max component diff: {max_diff_comp} = {max_diff:.2f}pp", flush=True)
    conclusion = "reduced design introduces significant confounding" if confounding else "reduced design does not introduce significant confounding"
    print(f"  Conclusion: {conclusion}", flush=True)

    print("\n" + "=" * 60, flush=True)
    print("SIDE-BY-SIDE COMPARISON TABLE", flush=True)
    print(f"{'Component':30s} | {'Full (%)':>10s} | {'Reduced (%)':>12s} | {'Diff (pp)':>10s}", flush=True)
    print("-" * 70, flush=True)
    all_comps = set(list(full_result["variance_pct"].keys()) + list(reduced_result["variance_pct"].keys()))
    rows = []
    for comp in all_comps:
        v_full = full_result["variance_pct"].get(comp, None)
        v_red = reduced_result["variance_pct"].get(comp, None)
        if v_full is not None and v_red is not None:
            rows.append((comp, v_full, v_red, v_red - v_full))
        elif v_full is not None:
            rows.append((comp, v_full, None, None))
        else:
            rows.append((comp, None, v_red, None))
    rows.sort(key=lambda x: -(x[1] or 0))
    for comp, v_full, v_red, diff in rows:
        f_str = f"{v_full:10.2f}" if v_full is not None else f"{'N/A':>10s}"
        r_str = f"{v_red:12.2f}" if v_red is not None else f"{'N/A':>12s}"
        d_str = f"{diff:+10.2f}" if diff is not None else f"{'N/A':>10s}"
        print(f"{comp:30s} | {f_str} | {r_str} | {d_str}", flush=True)

    output = {
        "full_design": {
            "n_records": full_result["n_records"],
            "facets": full_result["facets"],
            "n_levels": full_result["n_levels"],
            "variance_components": full_result["variance_components"],
            "variance_pct": full_result["variance_pct"],
            "G_item": full_result["G_item"],
            "grand_mean": full_result["grand_mean"],
            "d_study": full_result["d_study"],
        },
        "reduced_design": {
            "n_records": reduced_result["n_records"],
            "facets": reduced_result["facets"],
            "n_levels": reduced_result["n_levels"],
            "variance_components": reduced_result["variance_components"],
            "variance_pct": reduced_result["variance_pct"],
            "G_item": reduced_result["G_item"],
            "grand_mean": reduced_result["grand_mean"],
            "d_study": reduced_result["d_study"],
        },
        "comparison": {
            "item_id_pct_full": round(item_pct_full, 2),
            "item_id_pct_reduced": round(item_pct_reduced, 2),
            "item_id_pct_diff": round(item_pct_diff, 2),
            "G_item_full": round(g_full, 4),
            "G_item_reduced": round(g_reduced, 4),
            "G_item_diff": round(g_diff, 4),
            "max_component_pct_diff": round(max_diff, 2),
            "max_component_pct_diff_name": max_diff_comp,
            "conclusion": conclusion,
        },
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {OUTPUT_PATH}", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
