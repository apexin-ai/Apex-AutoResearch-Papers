"""Within-MMLU Subject-Level Gradient (4 models, bf16-only, Henderson Method I)

Uses pre-balanced cross_model_4way_bf16.csv from exp-001 data.
Output: results/exp001_analysis/within_mmlu_subject_gradient_4model.json
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]

STEM = {"abstract_algebra", "college_physics", "computer_security", "high_school_mathematics"}
HUMANITIES = {"international_law", "philosophy", "world_religions"}

MODEL_DISPLAY = {
    "llama-3.1-8b-instruct": "Llama-3.1-8B",
    "gemma-2-9b-it": "Gemma-2-9B",
    "mistral-7b-instruct-v0.3": "Mistral-7B",
    "qwen3-8b": "Qwen3-8B",
}


def compute_henderson_i(df, response, facets):
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects = {}

    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}

    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        interaction_contrib = 0.0
        for fj in facets:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in facets if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels, effects


def compute_g_item(vc, n_levels):
    """G coefficient for item_id as object of measurement.
    
    sigma_delta = sum of all item-involving interactions / their non-item divisors
                + residual / product of ALL non-item facet levels.
    """
    sigma_tau = vc.get("item_id", 0)

    non_item_facets = [f for f in FACETS if f != "item_id"]
    n_non_item_product = prod(n_levels[f] for f in non_item_facets)

    sigma_delta = 0.0
    for key, est in vc.items():
        if key == "item_id":
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(n_levels[f] for f in other) if other else 1
            sigma_delta += est / divisor
        elif key == "residual":
            sigma_delta += est / n_non_item_product

    g = sigma_tau / (sigma_tau + sigma_delta) if (sigma_tau + sigma_delta) > 0 else 0.0
    return round(g, 4), round(sigma_tau, 10), round(sigma_delta, 10)


def analyze_subject(df_subj):
    vc, n_levels, effects = compute_henderson_i(df_subj, "correct", FACETS)
    total_var = sum(vc.values())

    item_pct = vc.get("item_id", 0) / total_var * 100 if total_var > 0 else 0
    mi_key = "model:item_id"
    mi_pct = vc.get(mi_key, 0) / total_var * 100 if total_var > 0 else 0
    g_item, sigma_tau, sigma_delta = compute_g_item(vc, n_levels)
    accuracy = float(df_subj["correct"].mean())

    return {
        "n_records": len(df_subj),
        "n_items": int(n_levels["item_id"]),
        "accuracy": round(accuracy, 4),
        "item_id_pct": round(item_pct, 2),
        "model_item_pct": round(mi_pct, 2),
        "g_item": g_item,
        "total_variance": round(total_var, 8),
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "variance_components": {
            k: {"estimate": round(v, 10), "pct": round(v / total_var * 100, 2) if total_var > 0 else 0}
            for k, v in sorted(vc.items(), key=lambda x: -x[1])
        },
    }


def main():
    t0 = time.time()

    csv_path = "./results/analysis/cross_model_4way_bf16.csv"
    print(f"Loading {csv_path}...")
    df = pd.read_csv(csv_path, low_memory=False)
    print(f"Loaded {len(df)} records ({time.time()-t0:.1f}s)")

    for f in FACETS:
        df[f] = df[f].astype(str)

    models_raw = sorted(df["model"].unique())
    print(f"Models: {models_raw}")
    subjects = sorted(df["subject"].unique())
    print(f"Subjects ({len(subjects)}): {subjects}")

    results = {}
    for subj in subjects:
        df_subj = df[df["subject"] == subj].reset_index(drop=True)
        print(f"\n--- {subj} ({len(df_subj)} obs) ---", flush=True)
        r = analyze_subject(df_subj)
        results[subj] = r
        print(f"  item_id%={r['item_id_pct']:.2f}  model:item%={r['model_item_pct']:.2f}  "
              f"G_item={r['g_item']:.4f}  acc={r['accuracy']:.4f}")

    print(f"\n--- ALL SUBJECTS MERGED ({len(df)} obs) ---", flush=True)
    all_result = analyze_subject(df)
    print(f"  item_id%={all_result['item_id_pct']:.2f}  model:item%={all_result['model_item_pct']:.2f}  "
          f"G_item={all_result['g_item']:.4f}")

    item_pcts = {s: results[s]["item_id_pct"] for s in subjects}
    sorted_subjects = sorted(subjects, key=lambda s: -item_pcts[s])
    stem_pcts = [item_pcts[s] for s in subjects if s in STEM]
    hum_pcts = [item_pcts[s] for s in subjects if s in HUMANITIES]

    models_display = [MODEL_DISPLAY.get(m, m) for m in models_raw]

    output = {
        "analysis": "within_mmlu_subject_gradient_4model",
        "models": models_display,
        "design": "bf16-only balanced subset across 4 models",
        "facets": FACETS,
        "data_source": "cross_model_4way_bf16.csv (derived from exp-001 4-model JSONL)",
        "subjects": {s: results[s] for s in sorted_subjects},
        "all_subjects_baseline": all_result,
        "gradient_summary": {
            "max_item_id_pct": round(max(item_pcts.values()), 2),
            "min_item_id_pct": round(min(item_pcts.values()), 2),
            "range": round(max(item_pcts.values()) - min(item_pcts.values()), 2),
            "stem_mean": round(float(np.mean(stem_pcts)), 2) if stem_pcts else None,
            "humanities_mean": round(float(np.mean(hum_pcts)), 2) if hum_pcts else None,
            "stem_subjects": sorted(STEM),
            "humanities_subjects": sorted(HUMANITIES),
            "ranking_by_item_id_pct": sorted_subjects,
        },
    }

    out_path = Path("./results/exp001_analysis/within_mmlu_subject_gradient_4model.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(out_path), "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'='*70}")
    print(f"{'Subject':<25} {'item_id%':>9} {'m:item%':>8} {'G_item':>7} {'acc':>6}")
    print("-" * 70)
    for s in sorted_subjects:
        r = results[s]
        cat = "STEM" if s in STEM else ("HUM" if s in HUMANITIES else "OTHER")
        print(f"{s:<25} {r['item_id_pct']:>8.2f}% {r['model_item_pct']:>7.2f}% {r['g_item']:>7.4f} {r['accuracy']:>6.4f}  [{cat}]")
    print("-" * 70)
    print(f"{'ALL MERGED':<25} {all_result['item_id_pct']:>8.2f}% {all_result['model_item_pct']:>7.2f}% {all_result['g_item']:>7.4f}")
    print(f"\nSTEM mean item_id%: {np.mean(stem_pcts):.2f}%")
    print(f"Humanities mean item_id%: {np.mean(hum_pcts):.2f}%")
    print(f"\nDone in {time.time()-t0:.1f}s -> {out_path}")


if __name__ == "__main__":
    main()
