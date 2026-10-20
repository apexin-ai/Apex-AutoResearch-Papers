"""Per-subject Henderson Method I G-study for MMLU (10 subjects × 20 items each)."""
import json, sys
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
DIM_ORDER = FACETS
LOCAL_MODELS = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek"]
DATA_DIR = Path("./results/exp002")
ITEMS_FILE = Path("./data/mmlu_items_exp001.json")
OUT_FILE = Path("./results/exp004_8model_analysis/mmlu_subject_level_gstudy.json")


def load_mmlu_data():
    frames = []
    for m in LOCAL_MODELS + ["olmo", "yi"]:
        path = DATA_DIR / f"{m}_mmlu.jsonl"
        if not path.exists():
            print(f"WARNING: missing {path}")
            continue
        df = pd.read_json(path, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
        df["temperature"] = df["temperature"].round(1)
        df = df[df["temperature"].isin([0.0, 0.7])]
        frames.append(df[["model", "temperature", "prompt_template", "seed",
                          "ordering", "item_id", "correct"]])
    df = pd.concat(frames, ignore_index=True)
    for f in FACETS:
        df[f] = df[f].astype(str)
    return df


def build_tensor(df, dim_levels):
    shape = [len(v) for v in dim_levels.values()]
    Y = np.full(shape, np.nan, dtype=np.float64)
    idx_maps = {name: {v: i for i, v in enumerate(vals)} for name, vals in dim_levels.items()}
    for _, row in df.iterrows():
        indices = tuple(idx_maps[name][row[name]] for name in dim_levels.keys())
        Y[indices] = row["correct"]
    n_nan = np.isnan(Y).sum()
    if n_nan > 0:
        print(f"  WARNING: {n_nan} NaN cells, filling with 0")
        Y = np.nan_to_num(Y, nan=0.0)
    return Y


def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    grand_mean = Y.mean()
    N = Y.size
    n_dims = len(dim_sizes)
    if dim_names is None:
        dim_names = DIM_ORDER[:n_dims]

    effects = {}
    for d, name in enumerate(dim_names):
        ax = tuple(i for i in range(n_dims) if i != d)
        gm = Y.mean(axis=ax)
        n_per = N // dim_sizes[d]
        ss = float(n_per * ((gm - grand_mean) ** 2).sum())
        df_eff = dim_sizes[d] - 1
        effects[name] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for (d1, n1), (d2, n2) in combinations(enumerate(zip(dim_names, dim_sizes)), 2):
        di, ni = d1, n1[1]
        dj, nj = d2, n2[1]
        name_i, name_j = n1[0], n2[0]
        ax = tuple(k for k in range(n_dims) if k != di and k != dj)
        cell_mean = Y.mean(axis=ax)
        main_i = Y.mean(axis=tuple(k for k in range(n_dims) if k != di))
        main_j = Y.mean(axis=tuple(k for k in range(n_dims) if k != dj))
        n_per = N // (ni * nj)
        interaction = cell_mean - main_i.reshape([-1 if k == 0 else 1 for k in range(cell_mean.ndim)]) \
                      - main_j.reshape([1 if k == 0 else -1 for k in range(cell_mean.ndim)]) + grand_mean
        ss = float(n_per * (interaction ** 2).sum())
        df_eff = (ni - 1) * (nj - 1)
        key = f"{name_i}:{name_j}"
        effects[key] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((Y - grand_mean) ** 2).sum())
    ss_model = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    n_levels = dict(zip(dim_names, dim_sizes))
    vc = {}

    for fi, fj in combinations(dim_names, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in dim_names:
        coeff_main = prod(n_levels[f] for f in dim_names if f != fi)
        ic = 0.0
        for fj in dim_names:
            if fj == fi:
                continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            cij = prod(n_levels[f] for f in dim_names if f not in (fi, fj))
            ic += cij * vc[ik]
        raw = (effects[fi]["ms"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    return vc, n_levels


def compute_g_item(vc, n_levels):
    non_item_facets = [f for f in FACETS if f != "item_id"]
    tau = vc.get("item_id", 0.0)
    delta = 0.0
    for comp, est in vc.items():
        if est == 0.0 or comp == "item_id":
            continue
        if comp == "residual":
            delta += est / prod(n_levels[f] for f in non_item_facets)
            continue
        parts = set(comp.split(":"))
        if "item_id" not in parts:
            continue
        other = [f for f in parts if f != "item_id"]
        delta += est / (prod(n_levels[f] for f in other) if other else 1)
    g = tau / (tau + delta) if (tau + delta) > 0 else 0.0
    return g, tau, delta


def main():
    items_meta = json.loads(ITEMS_FILE.read_text())
    subject_map = {}
    for meta in items_meta:
        item_id = meta["item_id"]; subj = meta.get("subject", "unknown")
        subject_map.setdefault(subj, []).append(item_id)
    print(f"Subjects: {sorted(subject_map.keys())}")
    print(f"Items per subject: {[(s, len(v)) for s, v in sorted(subject_map.items())]}")

    print("Loading MMLU data...")
    df = load_mmlu_data()
    print(f"  {len(df)} rows, models: {sorted(df['model'].unique())}")

    models = sorted(df["model"].unique().tolist())
    temps = sorted(df["temperature"].unique().tolist())
    prompts = sorted(df["prompt_template"].unique().tolist())
    seeds = sorted(df["seed"].unique().tolist())
    orderings = sorted(df["ordering"].unique().tolist())

    results = []
    for subj in sorted(subject_map.keys()):
        subj_items = sorted(subject_map[subj])
        subj_items_str = [str(x) for x in subj_items]
        df_subj = df[df["item_id"].isin(subj_items_str)]
        n_items = len(subj_items_str)
        print(f"\n--- {subj} ({n_items} items, {len(df_subj)} rows) ---")

        dim_levels = {
            "model": models, "temperature": temps, "prompt_template": prompts,
            "seed": seeds, "ordering": orderings, "item_id": sorted(df_subj["item_id"].unique().tolist())
        }
        dim_sizes = [len(v) for v in dim_levels.values()]
        Y = build_tensor(df_subj, dim_levels)
        print(f"  tensor shape: {Y.shape}, mean acc: {Y.mean():.4f}")

        vc, n_levels = henderson_i_from_tensor(Y, dim_sizes)
        total_var = sum(vc.values())
        g_item, tau, delta = compute_g_item(vc, n_levels)

        pct = {k: round(100 * v / total_var, 2) if total_var > 0 else 0 for k, v in vc.items()}

        print(f"  item_id%={pct.get('item_id',0):.1f}  model:item%={pct.get('model:item_id',0):.1f}  G_item={g_item:.4f}")

        results.append({
            "name": subj,
            "n_items": len(dim_levels["item_id"]),
            "mean_accuracy": round(float(Y.mean()), 4),
            "item_id_pct": pct.get("item_id", 0),
            "model_item_pct": pct.get("model:item_id", 0),
            "G_item": round(g_item, 4),
            "all_components_pct": pct,
        })

    item_pcts = [r["item_id_pct"] for r in results]
    g_items = [r["G_item"] for r in results]

    output = {
        "n_subjects": len(results),
        "items_per_subject": 20,
        "facets": {"model": len(models), "temperature": len(temps),
                   "prompt_template": len(prompts), "seed": len(seeds),
                   "ordering": len(orderings)},
        "subjects": results,
        "summary": {
            "item_id_pct_mean": round(float(np.mean(item_pcts)), 2),
            "item_id_pct_std": round(float(np.std(item_pcts, ddof=1)), 2),
            "item_id_pct_cv": round(float(np.std(item_pcts, ddof=1) / np.mean(item_pcts)), 3) if np.mean(item_pcts) > 0 else 0,
            "G_item_mean": round(float(np.mean(g_items)), 4),
            "G_item_std": round(float(np.std(g_items, ddof=1)), 4),
        },
        "comparison": {
            "full_200_item_id_pct": 37.9,
            "full_200_G_item": 0.896
        }
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(output, indent=2))
    print(f"\nSaved to {OUT_FILE}")

    print(f"\n{'='*80}")
    print(f"{'Subject':<30} {'item_id%':>10} {'model:item%':>12} {'G_item':>8}")
    print(f"{'='*80}")
    for r in results:
        print(f"{r['name']:<30} {r['item_id_pct']:>10.2f} {r['model_item_pct']:>12.2f} {r['G_item']:>8.4f}")
    print(f"{'-'*80}")
    s = output["summary"]
    print(f"{'Mean':<30} {s['item_id_pct_mean']:>10.2f} {'':>12} {s['G_item_mean']:>8.4f}")
    print(f"{'SD':<30} {s['item_id_pct_std']:>10.2f} {'':>12} {s['G_item_std']:>8.4f}")
    print(f"{'Full 200 items':<30} {output['comparison']['full_200_item_id_pct']:>10.1f} {'':>12} {output['comparison']['full_200_G_item']:>8.3f}")


if __name__ == "__main__":
    main()
