"""MMLU subject-level scatter: difficulty dispersion vs item_id variance share."""

import json
import sys
from itertools import combinations
from math import prod
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.config.model_paths import normalize_model_name

DATA_DIR = Path("./results/exp002")
OUT_JSON = Path("./results/exp004_8model_analysis/mmlu_subject_level_analysis.json")
OUT_PDF = Path("./results/exp004_8model_analysis/mmlu_subject_scatter.pdf")

DIM_ORDER = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
ALL_MODELS = ["llama", "mistral", "qwen", "gemma", "internlm", "deepseek", "olmo", "yi"]


def load_mmlu_data():
    frames = []
    for m in ALL_MODELS:
        path = DATA_DIR / f"{m}_mmlu.jsonl"
        if not path.exists():
            print(f"  WARNING: missing {path}")
            continue
        df = pd.read_json(path, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
        frames.append(df[["model", "temperature", "prompt_template", "seed",
                          "ordering", "item_id", "correct", "subject"]])
    df = pd.concat(frames, ignore_index=True)
    df["temperature"] = df["temperature"].round(1)
    df = df[df["temperature"].isin([0.0, 0.7])]
    for f in DIM_ORDER:
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
        Y = np.nan_to_num(Y, nan=0.0)
    return Y


def henderson_i_from_tensor(Y, dim_sizes, dim_names=None):
    if dim_names is None:
        dim_names = DIM_ORDER[:len(dim_sizes)]
    grand_mean = Y.mean()
    N = Y.size
    n_dims = len(dim_sizes)

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


def analyze_subject(df_subj, subject_name):
    items = sorted(df_subj["item_id"].unique().tolist())
    n_items = len(items)
    if n_items < 3:
        return None

    # item difficulty: mean accuracy per item across all conditions
    p_i = df_subj.groupby("item_id")["correct"].apply(lambda x: x.astype(float).mean())
    sd_pi = float(p_i.std(ddof=1))
    mean_acc = float(p_i.mean())

    # Build tensor for Henderson I
    models = sorted(df_subj["model"].unique().tolist())
    temps = sorted(df_subj["temperature"].unique().tolist())
    prompts = sorted(df_subj["prompt_template"].unique().tolist())
    seeds = sorted(df_subj["seed"].unique().tolist())
    orderings = sorted(df_subj["ordering"].unique().tolist())

    dim_levels = {
        "model": models,
        "temperature": temps,
        "prompt_template": prompts,
        "seed": seeds,
        "ordering": orderings,
        "item_id": items,
    }
    dim_sizes = [len(v) for v in dim_levels.values()]

    Y = build_tensor(df_subj, dim_levels)
    vc, n_levels = henderson_i_from_tensor(Y, dim_sizes)
    total_var = sum(vc.values())
    item_pct = vc.get("item_id", 0.0) / total_var * 100 if total_var > 0 else 0.0

    return {
        "name": subject_name,
        "n_items": n_items,
        "mean_accuracy": round(mean_acc, 4),
        "sd_pi": round(sd_pi, 4),
        "item_id_pct": round(item_pct, 2),
    }


def main():
    print("Loading MMLU data...", flush=True)
    df = load_mmlu_data()
    print(f"  {len(df)} records, models: {sorted(df['model'].unique().tolist())}", flush=True)

    # Map item_id -> subject from the data itself
    subjects = sorted(df["subject"].unique().tolist())
    print(f"  {len(subjects)} subjects", flush=True)

    results = []
    for i, subj in enumerate(subjects):
        df_subj = df[df["subject"] == subj]
        r = analyze_subject(df_subj, subj)
        if r is None:
            print(f"  [{i+1}/{len(subjects)}] {subj}: skipped (<3 items)")
            continue
        results.append(r)
        print(f"  [{i+1}/{len(subjects)}] {subj}: n={r['n_items']}, sd_pi={r['sd_pi']:.4f}, item_id%={r['item_id_pct']:.1f}%", flush=True)

    # Spearman correlation
    sd_vals = np.array([r["sd_pi"] for r in results])
    item_vals = np.array([r["item_id_pct"] for r in results])
    rho, p_val = stats.spearmanr(sd_vals, item_vals)

    # Linear regression for the plot
    slope, intercept, r_value, _, _ = stats.linregress(sd_vals, item_vals)

    print(f"\nSpearman rho={rho:.4f}, p={p_val:.4e}", flush=True)
    print(f"Linear fit: slope={slope:.2f}, intercept={intercept:.2f}, R²={r_value**2:.4f}", flush=True)

    # Save JSON
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    output = {
        "n_subjects": len(results),
        "n_subjects_excluded": len(subjects) - len(results),
        "n_items_total": 200,
        "subjects": results,
        "spearman_rho": round(rho, 4),
        "spearman_p": round(p_val, 6),
        "regression": {
            "slope": round(slope, 4),
            "intercept": round(intercept, 4),
            "r_squared": round(r_value**2, 4),
        },
    }
    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved: {OUT_JSON}", flush=True)

    # Scatter plot
    n_items_arr = np.array([r["n_items"] for r in results])
    size_scale = np.clip(n_items_arr, 2, 15) * 8

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.scatter(sd_vals, item_vals, c="#0072B2", s=size_scale, alpha=0.7,
               edgecolors="white", linewidths=0.5, zorder=3)

    x_fit = np.linspace(sd_vals.min() - 0.02, sd_vals.max() + 0.02, 100)
    y_fit = slope * x_fit + intercept
    ax.plot(x_fit, y_fit, color="#D55E00", linewidth=1.5, zorder=2)

    # Confidence band
    n = len(sd_vals)
    x_mean = sd_vals.mean()
    se_fit = np.sqrt(np.sum((item_vals - slope * sd_vals - intercept)**2) / (n - 2)) * \
             np.sqrt(1/n + (x_fit - x_mean)**2 / np.sum((sd_vals - x_mean)**2))
    ax.fill_between(x_fit, y_fit - 1.96*se_fit, y_fit + 1.96*se_fit,
                    color="grey", alpha=0.15, zorder=1)

    ax.set_xlabel("Difficulty Dispersion SD($p_i$)", fontsize=11)
    ax.set_ylabel("Item Variance Share (%)", fontsize=11)
    ax.tick_params(labelsize=10)

    # Annotation
    ax.text(0.97, 0.05,
            f"$\\rho$ = {rho:.2f}, p = {p_val:.1e}\nn = {len(results)} subjects",
            transform=ax.transAxes, fontsize=10, ha="right", va="bottom",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="grey", alpha=0.8))

    fig.tight_layout()
    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PDF, dpi=300, bbox_inches="tight")
    fig.savefig(str(OUT_PDF).replace(".pdf", ".png"), dpi=150, bbox_inches="tight")
    print(f"Figure saved: {OUT_PDF}", flush=True)
    plt.close()


if __name__ == "__main__":
    main()
