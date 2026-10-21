"""D014 Validation 2: 8-model MMLU within-subject gradient analysis.

Per-subject Henderson I variance decomposition across 8 models.
Tests whether item heterogeneity (not format) drives variance structure.
"""

import json
import numpy as np
import pandas as pd
from itertools import combinations
from pathlib import Path
from scipy import stats

SUBJECT_CATEGORIES = {
    "abstract_algebra": "STEM",
    "college_physics": "STEM",
    "high_school_mathematics": "STEM",
    "computer_security": "STEM",
    "professional_medicine": "Other",
    "clinical_knowledge": "Other",
    "philosophy": "Humanities",
    "international_law": "Humanities",
    "world_religions": "Humanities",
    "us_foreign_policy": "Humanities",
}

MODEL_FILES = [
    "llama_mmlu.jsonl",
    "mistral_mmlu.jsonl",
    "qwen_mmlu.jsonl",
    "gemma_mmlu.jsonl",
    "deepseek_mmlu.jsonl",
    "internlm_mmlu.jsonl",
    "olmo_mmlu.jsonl",
    "yi_mmlu.jsonl",
]

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]


def load_all_models(data_dir: str) -> pd.DataFrame:
    frames = []
    for mf in MODEL_FILES:
        p = Path(data_dir) / mf
        df = pd.read_json(p, lines=True)
        model_short = mf.replace("_mmlu.jsonl", "")
        df["model"] = model_short
        frames.append(df)
    combined = pd.concat(frames, ignore_index=True)
    for f in FACETS:
        combined[f] = combined[f].astype(str)
    return combined


def compute_ss(df, response, facets):
    grand_mean = df[response].mean()
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}
    effects = {}

    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per_group = N // n_levels[f]
        ss = float(n_per_group * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per_cell = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cell_mean in cell_means.items():
            interaction = cell_mean - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per_cell * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        key = f"{fi}:{fj}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}
    return effects, n_levels


def estimate_variance_components(effects, facets, n_levels):
    vc = {}
    ms_res = effects["residual"]["ms"]

    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        divisor = 1
        for fk in facets:
            if fk not in (fi, fj):
                divisor *= n_levels[fk]
        raw = (effects[key]["ms"] - ms_res) / divisor
        vc[key] = max(0.0, raw)

    for f in facets:
        interaction_contribution = 0.0
        for fi, fj in combinations(facets, 2):
            key = f"{fi}:{fj}"
            if f in (fi, fj):
                other = fj if f == fi else fi
                coeff = 1
                for fk in facets:
                    if fk != f and fk != other:
                        coeff *= n_levels[fk]
                interaction_contribution += coeff * vc[key]
        divisor = 1
        for fk in facets:
            if fk != f:
                divisor *= n_levels[fk]
        raw = (effects[f]["ms"] - interaction_contribution - ms_res) / divisor
        vc[f] = max(0.0, raw)

    vc["residual"] = max(0.0, ms_res)
    return vc


def compute_g_item(vc, n_levels):
    """D-study G coefficient for item generalizability.
    
    G = sigma2(item) / [sigma2(item) + sigma2(delta)]
    sigma2(delta) = sum of sigma2(f:item)/n_f for all f != item
                  + sigma2(residual) / prod(n_f for f != item)
    """
    sigma2_item = vc.get("item_id", 0)
    
    other_facets = [f for f in FACETS if f != "item_id"]
    sigma2_delta = 0.0
    
    for f in other_facets:
        key_a = f"item_id:{f}"
        key_b = f"{f}:item_id"
        interaction_var = vc.get(key_a, vc.get(key_b, 0))
        sigma2_delta += interaction_var / n_levels[f]
    
    prod_n = 1
    for f in other_facets:
        prod_n *= n_levels[f]
    sigma2_delta += vc.get("residual", 0) / prod_n
    
    denom = sigma2_item + sigma2_delta
    return sigma2_item / denom if denom > 0 else 0


def compute_item_heterogeneity(df):
    """std(p) across items: std of per-item mean accuracy."""
    item_means = df.groupby("item_id")["correct"].mean()
    return float(item_means.std())


def analyze_subject(df_subject, subject_name):
    n_levels_check = {f: df_subject[f].nunique() for f in FACETS}
    n_obs = len(df_subject)
    expected = 1
    for v in n_levels_check.values():
        expected *= v
    if n_obs != expected:
        print(f"  WARNING: {subject_name} not balanced: {n_obs} obs vs expected {expected}")
        print(f"    levels: {n_levels_check}")

    effects, n_levels = compute_ss(df_subject, "correct", FACETS)
    vc = estimate_variance_components(effects, FACETS, n_levels)
    total = sum(vc.values())

    pct = {k: v / total * 100 if total > 0 else 0 for k, v in vc.items()}
    item_pct = pct.get("item_id", 0)
    model_item_pct = pct.get("model:item_id", 0)

    G_item = compute_g_item(vc, n_levels)

    std_p = compute_item_heterogeneity(df_subject)
    accuracy = float(df_subject["correct"].mean())

    return {
        "subject": subject_name,
        "category": SUBJECT_CATEGORIES.get(subject_name, "Unknown"),
        "n_obs": n_obs,
        "n_items": n_levels.get("item_id", 0),
        "n_models": n_levels.get("model", 0),
        "accuracy": round(accuracy, 4),
        "item_id_pct": round(item_pct, 2),
        "model_item_pct": round(model_item_pct, 2),
        "model_pct": round(pct.get("model", 0), 2),
        "residual_pct": round(pct.get("residual", 0), 2),
        "G_item": round(G_item, 4),
        "std_p": round(std_p, 4),
        "variance_components": {k: round(v, 8) for k, v in sorted(vc.items(), key=lambda x: -x[1])},
        "pct_components": {k: round(v, 2) for k, v in sorted(pct.items(), key=lambda x: -x[1])},
    }


def main():
    data_dir = "./results/exp002"
    output_dir = Path("./results/exp004_8model_analysis")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading 8-model MMLU data...")
    df = load_all_models(data_dir)
    print(f"Total observations: {len(df)}")
    print(f"Models: {sorted(df['model'].unique())}")
    print(f"Subjects: {sorted(df['subject'].unique())}")

    subjects = sorted(df["subject"].unique())
    results = []

    for subj in subjects:
        print(f"\n--- {subj} ({SUBJECT_CATEGORIES.get(subj, '?')}) ---")
        df_subj = df[df["subject"] == subj].copy()
        r = analyze_subject(df_subj, subj)
        results.append(r)
        print(f"  item_id%={r['item_id_pct']:.1f}  model×item%={r['model_item_pct']:.1f}  "
              f"G_item={r['G_item']:.3f}  std(p)={r['std_p']:.4f}  acc={r['accuracy']:.3f}")

    # Spearman correlation: std_p vs item_id_pct
    std_ps = [r["std_p"] for r in results]
    item_pcts = [r["item_id_pct"] for r in results]
    rho, pval = stats.spearmanr(std_ps, item_pcts)

    # STEM vs Humanities
    stem = [r for r in results if r["category"] == "STEM"]
    hum = [r for r in results if r["category"] == "Humanities"]
    other = [r for r in results if r["category"] == "Other"]

    stem_item_mean = np.mean([r["item_id_pct"] for r in stem])
    hum_item_mean = np.mean([r["item_id_pct"] for r in hum])
    other_item_mean = np.mean([r["item_id_pct"] for r in other]) if other else None

    stem_stdp_mean = np.mean([r["std_p"] for r in stem])
    hum_stdp_mean = np.mean([r["std_p"] for r in hum])

    stem_G_mean = np.mean([r["G_item"] for r in stem])
    hum_G_mean = np.mean([r["G_item"] for r in hum])

    stem_mi_mean = np.mean([r["model_item_pct"] for r in stem])
    hum_mi_mean = np.mean([r["model_item_pct"] for r in hum])

    # 4-model comparison
    comparison_4model = {
        "STEM_mean_item_pct": 27.9,
        "Humanities_mean_item_pct": 48.4,
        "note": "From memory.md 4-model results"
    }

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\nSpearman rho(std_p, item_id%): {rho:.4f}  p={pval:.4f}")
    print(f"\nSTEM mean:  item_id%={stem_item_mean:.1f}  m×i%={stem_mi_mean:.1f}  "
          f"std(p)={stem_stdp_mean:.4f}  G_item={stem_G_mean:.4f}  (4-model item_id%: 27.9)")
    print(f"Hum mean:   item_id%={hum_item_mean:.1f}  m×i%={hum_mi_mean:.1f}  "
          f"std(p)={hum_stdp_mean:.4f}  G_item={hum_G_mean:.4f}  (4-model item_id%: 48.4)")
    if other_item_mean is not None:
        print(f"Other mean: item_id%={other_item_mean:.1f}")

    # Subject-level table
    print("\n" + "-" * 95)
    print(f"{'Subject':<28} {'Cat':<6} {'item_id%':>8} {'m×i%':>8} {'std_p':>8} {'G_item':>8} {'acc':>6}")
    print("-" * 95)
    for r in sorted(results, key=lambda x: -x["item_id_pct"]):
        print(f"{r['subject']:<28} {r['category']:<6} {r['item_id_pct']:>8.1f} {r['model_item_pct']:>8.1f} "
              f"{r['std_p']:>8.4f} {r['G_item']:>8.4f} {r['accuracy']:>6.3f}")

    output = {
        "experiment": "D014_validation2",
        "analysis": "8model_mmlu_subject_gradient",
        "n_models": 8,
        "n_subjects": len(results),
        "facets": FACETS,
        "subjects": results,
        "spearman": {
            "rho": round(float(rho), 4),
            "p_value": round(float(pval), 4),
            "variables": ["std_p (item difficulty heterogeneity)", "item_id% (Henderson I)"],
            "n": len(results),
        },
        "group_summary": {
            "STEM": {
                "subjects": [r["subject"] for r in stem],
                "mean_item_pct": round(float(stem_item_mean), 2),
                "mean_model_item_pct": round(float(stem_mi_mean), 2),
                "mean_std_p": round(float(stem_stdp_mean), 4),
                "mean_G_item": round(float(stem_G_mean), 4),
            },
            "Humanities": {
                "subjects": [r["subject"] for r in hum],
                "mean_item_pct": round(float(hum_item_mean), 2),
                "mean_model_item_pct": round(float(hum_mi_mean), 2),
                "mean_std_p": round(float(hum_stdp_mean), 4),
                "mean_G_item": round(float(hum_G_mean), 4),
            },
            "Other": {
                "subjects": [r["subject"] for r in other],
                "mean_item_pct": round(float(other_item_mean), 2) if other_item_mean else None,
            },
        },
        "comparison_4model": comparison_4model,
        "delta_vs_4model": {
            "STEM_item_pct_change": round(float(stem_item_mean) - 27.9, 2),
            "Humanities_item_pct_change": round(float(hum_item_mean) - 48.4, 2),
        },
    }

    out_path = output_dir / "mmlu_subject_gradient_8model.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n-> {out_path}")


if __name__ == "__main__":
    main()
