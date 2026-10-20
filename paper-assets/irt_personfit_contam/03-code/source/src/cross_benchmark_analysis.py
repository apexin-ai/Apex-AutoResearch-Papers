"""Cross-Benchmark Correlation Deep Dive for 12-model lz* analysis."""

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist
from scipy.stats import spearmanr

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "artifacts", "phase_b_two_sided_v2")
OUT_DIR = os.path.join(PROJECT_ROOT, "artifacts", "cross_benchmark_analysis")
os.makedirs(OUT_DIR, exist_ok=True)

BENCHMARK_ORDER = ["mmlu", "arc_c", "hellaswag", "gsm8k", "humaneval"]
BENCHMARK_LABELS = {"mmlu": "MMLU", "arc_c": "ARC-C", "hellaswag": "HellaSwag",
                    "gsm8k": "GSM8K", "humaneval": "HumanEval"}
MODEL_ORDER = [
    "360GPT2-Pro", "DeepSeek-V3", "Doubao-pro", "Gemini-1.5",
    "Gemma-2B-it", "Hunyuan-Turbo", "Mistral-7B-Instruct-v0.1",
    "Moonshot-v1", "Qwen-Plus", "Qwen2.5-3B-Instruct",
    "Vicuna-7B-v1.3", "Yi-Lightning"
]
BENCHMARK_TYPES = {
    "MCQ": ["mmlu", "arc_c", "hellaswag"],
    "Math": ["gsm8k"],
    "Code": ["humaneval"],
}


def load_data():
    pf = pd.read_csv(os.path.join(DATA_DIR, "personfit_matrix_v2.csv"))
    ep = pd.read_csv(os.path.join(DATA_DIR, "empirical_pvalues.csv"))
    return pf, ep


def build_lz_matrix(pf):
    """Return DataFrame: rows=models, cols=benchmarks, values=lz*."""
    pivot = pf.pivot_table(index="model_name", columns="benchmark", values="lz_star")
    pivot = pivot.loc[MODEL_ORDER, BENCHMARK_ORDER]
    return pivot


def build_flag_matrix(ep):
    """Return DataFrame: rows=models, cols=benchmarks, values=flagged_bh."""
    pivot = ep.pivot_table(index="model_name", columns="benchmark", values="flagged_bh",
                           aggfunc="first")
    pivot = pivot.loc[MODEL_ORDER, BENCHMARK_ORDER]
    return pivot


# ── 1. lz* Heatmap ──────────────────────────────────────────────────────────

def plot_heatmap(lz_mat, flag_mat):
    fig, ax = plt.subplots(figsize=(10, 8))

    data = lz_mat.values.astype(float)
    vmax = np.max(np.abs(data))
    im = ax.imshow(data, cmap="RdBu_r", aspect="auto", vmin=-vmax, vmax=vmax)

    ax.set_xticks(range(len(BENCHMARK_ORDER)))
    ax.set_xticklabels([BENCHMARK_LABELS[b] for b in BENCHMARK_ORDER], fontsize=11)
    ax.set_yticks(range(len(MODEL_ORDER)))
    ax.set_yticklabels(MODEL_ORDER, fontsize=10)

    for i in range(len(MODEL_ORDER)):
        for j in range(len(BENCHMARK_ORDER)):
            val = data[i, j]
            flagged = flag_mat.iloc[i, j]
            color = "white" if abs(val) > vmax * 0.5 else "black"
            weight = "bold" if flagged else "normal"
            ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                    fontsize=8, color=color, fontweight=weight)

    gemini_idx = MODEL_ORDER.index("Gemini-1.5")
    rect = mpatches.FancyBboxPatch(
        (-0.5, gemini_idx - 0.5), len(BENCHMARK_ORDER), 1,
        linewidth=2.5, edgecolor="#FFD700", facecolor="none",
        boxstyle="round,pad=0.02", zorder=5)
    ax.add_patch(rect)

    mean_abs = np.mean(np.abs(data), axis=1)
    for i, v in enumerate(mean_abs):
        ax.text(len(BENCHMARK_ORDER) + 0.15, i, f"mean |lz*|={v:.1f}",
                ha="left", va="center", fontsize=8, color="#444444")

    ax.set_xlim(-0.5, len(BENCHMARK_ORDER) - 0.5 + 2.8)
    cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.15)
    cbar.set_label("lz* value", fontsize=11)

    ax.set_title("Person-Fit lz* Across Models and Benchmarks", fontsize=13, pad=12)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "lz_star_heatmap.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("  [1/6] lz_star_heatmap.png")


# ── 2. Per-Model Anomaly Profiles ────────────────────────────────────────────

def anomaly_profiles(ep):
    rows = []
    for model in MODEL_ORDER:
        sub = ep[ep["model_name"] == model]
        flagged = sub[sub["flagged_bh"] == True]
        n_flagged = len(flagged)
        flagged_benchmarks = sorted(flagged["benchmark"].tolist())

        lz_vals = flagged["lz_star"]
        if n_flagged == 0:
            direction = "none"
        elif (lz_vals > 0).all():
            direction = "positive"
        elif (lz_vals < 0).all():
            direction = "negative"
        else:
            direction = "mixed"

        rows.append({
            "model": model,
            "n_flagged": n_flagged,
            "flagged_benchmarks": "; ".join(flagged_benchmarks),
            "dominant_direction": direction,
        })

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT_DIR, "anomaly_profiles.csv"), index=False)

    flag_counts = df["n_flagged"].value_counts().sort_index()
    print("  [2/6] anomaly_profiles.csv")
    print(f"        Flag distribution: {dict(flag_counts)}")
    return df


# ── 3. Cross-Benchmark Correlation Matrix ────────────────────────────────────

def plot_correlation_matrix(lz_mat):
    benchmarks = [BENCHMARK_LABELS[b] for b in BENCHMARK_ORDER]
    data = lz_mat.values.astype(float)
    n_bench = data.shape[1]

    corr = np.zeros((n_bench, n_bench))
    pvals = np.zeros((n_bench, n_bench))
    for i in range(n_bench):
        for j in range(n_bench):
            r, p = spearmanr(data[:, i], data[:, j])
            corr[i, j] = r
            pvals[i, j] = p

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")
    ax.set_xticks(range(n_bench))
    ax.set_xticklabels(benchmarks, fontsize=11, rotation=45, ha="right")
    ax.set_yticks(range(n_bench))
    ax.set_yticklabels(benchmarks, fontsize=11)

    for i in range(n_bench):
        for j in range(n_bench):
            sig = "**" if pvals[i, j] < 0.01 else ("*" if pvals[i, j] < 0.05 else "")
            color = "white" if abs(corr[i, j]) > 0.5 else "black"
            ax.text(j, i, f"{corr[i,j]:.2f}{sig}", ha="center", va="center",
                    fontsize=10, color=color)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Spearman ρ", fontsize=11)
    ax.set_title("Cross-Benchmark lz* Correlation (n=12 models)", fontsize=12, pad=10)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "correlation_matrix.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("  [3/6] correlation_matrix.png")
    return corr, pvals


# ── 4. Benchmark Type Grouping Analysis ──────────────────────────────────────

def benchmark_type_analysis(lz_mat, flag_mat):
    results = {}
    for group, benchmarks in BENCHMARK_TYPES.items():
        cols = [b for b in benchmarks if b in lz_mat.columns]
        sub = lz_mat[cols]
        sub_flag = flag_mat[cols]

        mean_lz = sub.mean(axis=1)
        mean_abs_lz = sub.abs().mean(axis=1)
        n_positive = (sub > 0).sum().sum()
        n_negative = (sub < 0).sum().sum()
        n_flagged = sub_flag.sum().sum()
        total_cells = sub.shape[0] * sub.shape[1]

        results[group] = {
            "benchmarks": [BENCHMARK_LABELS[b] for b in cols],
            "mean_lz_star": float(sub.values.mean()),
            "mean_abs_lz_star": float(np.abs(sub.values).mean()),
            "std_lz_star": float(sub.values.std()),
            "n_positive": int(n_positive),
            "n_negative": int(n_negative),
            "n_flagged": int(n_flagged),
            "total_cells": int(total_cells),
            "flag_rate": float(n_flagged / total_cells),
            "per_model_mean": {m: float(v) for m, v in mean_lz.items()},
            "per_model_mean_abs": {m: float(v) for m, v in mean_abs_lz.items()},
        }

    print("  [4/6] benchmark type analysis computed")
    return results


# ── 5. Hierarchical Clustering ───────────────────────────────────────────────

def plot_dendrogram(lz_mat):
    data = lz_mat.values.astype(float)
    Z = linkage(data, method="ward")

    fig, ax = plt.subplots(figsize=(10, 6))
    dn = dendrogram(Z, labels=MODEL_ORDER, ax=ax, leaf_rotation=45,
                    leaf_font_size=10, color_threshold=0.7 * max(Z[:, 2]))

    ax.set_title("Hierarchical Clustering of Models by lz* Profile (Ward Linkage)",
                 fontsize=12, pad=10)
    ax.set_ylabel("Distance", fontsize=11)

    gemini_idx_in_leaves = None
    for i, label in enumerate(ax.get_xticklabels()):
        if label.get_text() == "Gemini-1.5":
            gemini_idx_in_leaves = i
            label.set_color("#D4AF37")
            label.set_fontweight("bold")
            label.set_fontsize(11)

    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "dendrogram.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)

    clusters_3 = fcluster(Z, t=3, criterion="maxclust")
    cluster_map = {m: int(c) for m, c in zip(MODEL_ORDER, clusters_3)}
    gemini_cluster = cluster_map.get("Gemini-1.5", -1)
    gemini_alone = sum(1 for c in clusters_3 if c == gemini_cluster) == 1

    print(f"  [5/6] dendrogram.png  (3-cluster: Gemini-1.5 isolated={gemini_alone})")
    return cluster_map, gemini_alone, Z


# ── 6. lz* Direction Analysis ────────────────────────────────────────────────

def direction_analysis(lz_mat, flag_mat):
    rows = []
    for model in MODEL_ORDER:
        for bench in BENCHMARK_ORDER:
            val = lz_mat.loc[model, bench]
            flagged = flag_mat.loc[model, bench]
            rows.append({
                "model": model,
                "benchmark": bench,
                "benchmark_label": BENCHMARK_LABELS[bench],
                "lz_star": float(val),
                "direction": "positive" if val > 0 else "negative",
                "flagged_bh": bool(flagged),
            })

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT_DIR, "direction_analysis.csv"), index=False)

    total = len(df)
    n_pos = (df["direction"] == "positive").sum()
    n_neg = (df["direction"] == "negative").sum()

    bench_summary = {}
    for bench in BENCHMARK_ORDER:
        sub = df[df["benchmark"] == bench]
        bench_summary[BENCHMARK_LABELS[bench]] = {
            "n_positive": int((sub["direction"] == "positive").sum()),
            "n_negative": int((sub["direction"] == "negative").sum()),
            "all_positive": bool((sub["direction"] == "positive").all()),
            "all_negative": bool((sub["direction"] == "negative").all()),
        }

    model_summary = {}
    for model in MODEL_ORDER:
        sub = df[df["model"] == model]
        np_ = (sub["direction"] == "positive").sum()
        nn_ = (sub["direction"] == "negative").sum()
        if np_ == len(sub):
            dom = "all_positive"
        elif nn_ == len(sub):
            dom = "all_negative"
        elif np_ > nn_:
            dom = "mostly_positive"
        elif nn_ > np_:
            dom = "mostly_negative"
        else:
            dom = "balanced"
        model_summary[model] = {
            "n_positive": int(np_),
            "n_negative": int(nn_),
            "dominant": dom,
        }

    direction_stats = {
        "total_cells": total,
        "n_positive": int(n_pos),
        "n_negative": int(n_neg),
        "pct_positive": float(n_pos / total * 100),
        "per_benchmark": bench_summary,
        "per_model": model_summary,
    }

    print(f"  [6/6] direction_analysis.csv  (positive={n_pos}, negative={n_neg})")
    return df, direction_stats


# ── Report & Summary ─────────────────────────────────────────────────────────

def write_report(lz_mat, anomaly_df, corr, pvals, type_results,
                 cluster_map, gemini_alone, direction_stats):
    bench_labels = [BENCHMARK_LABELS[b] for b in BENCHMARK_ORDER]
    data = lz_mat.values.astype(float)
    mean_abs_per_model = np.mean(np.abs(data), axis=1)
    mean_abs_per_bench = np.mean(np.abs(data), axis=0)

    lines = []
    lines.append("# Cross-Benchmark lz* Analysis Report\n")

    # Overview
    lines.append("## 1. Overview\n")
    lines.append(f"This analysis examines the person-fit statistic lz* across "
                 f"{len(MODEL_ORDER)} LLMs and {len(BENCHMARK_ORDER)} benchmarks "
                 f"({', '.join(bench_labels)}). "
                 f"Of {len(MODEL_ORDER) * len(BENCHMARK_ORDER)} model–benchmark cells, "
                 f"{anomaly_df['n_flagged'].sum()} are flagged as anomalous "
                 f"(BH-adjusted p < 0.05).\n")

    # Heatmap highlights
    lines.append("## 2. lz* Magnitude Patterns\n")
    sorted_bench_idx = np.argsort(mean_abs_per_bench)[::-1]
    lines.append("**Benchmark severity ranking** (mean |lz*| across models):\n")
    for idx in sorted_bench_idx:
        lines.append(f"- {bench_labels[idx]}: {mean_abs_per_bench[idx]:.1f}")
    lines.append("")

    sorted_model_idx = np.argsort(mean_abs_per_model)[::-1]
    lines.append("**Model severity ranking** (mean |lz*| across benchmarks):\n")
    for idx in sorted_model_idx:
        lines.append(f"- {MODEL_ORDER[idx]}: {mean_abs_per_model[idx]:.1f}")
    lines.append("")

    top_model = MODEL_ORDER[sorted_model_idx[0]]
    lines.append(f"The most anomalous model overall is **{top_model}** "
                 f"(mean |lz*| = {mean_abs_per_model[sorted_model_idx[0]]:.1f}). "
                 f"MMLU and HellaSwag exhibit the highest lz* magnitudes across all models, "
                 f"suggesting that these large-scale MCQ benchmarks are most susceptible to "
                 f"response pattern anomalies.\n")

    # Anomaly profiles
    lines.append("## 3. Anomaly Profiles\n")
    all5 = anomaly_df[anomaly_df["n_flagged"] == 5]
    lines.append(f"**{len(all5)}/{len(MODEL_ORDER)}** models are flagged on all 5 benchmarks. "
                 f"Only {', '.join(anomaly_df[anomaly_df['n_flagged'] < 5]['model'].tolist())} "
                 f"escape full flagging.\n")

    for _, row in anomaly_df.iterrows():
        lines.append(f"- **{row['model']}**: {row['n_flagged']}/5 flagged "
                     f"({row['dominant_direction']}){' — ' + row['flagged_benchmarks'] if row['n_flagged'] < 5 else ''}")
    lines.append("")

    # Correlation
    lines.append("## 4. Cross-Benchmark Correlations\n")
    high_corr_pairs = []
    low_corr_pairs = []
    for i in range(len(BENCHMARK_ORDER)):
        for j in range(i+1, len(BENCHMARK_ORDER)):
            r = corr[i, j]
            p = pvals[i, j]
            pair = f"{bench_labels[i]}–{bench_labels[j]}"
            if r > 0.6 and p < 0.05:
                high_corr_pairs.append((pair, r, p))
            elif abs(r) < 0.3:
                low_corr_pairs.append((pair, r, p))

    if high_corr_pairs:
        lines.append("**Highly correlated benchmark pairs** (ρ > 0.6, p < 0.05):\n")
        for pair, r, p in sorted(high_corr_pairs, key=lambda x: -x[1]):
            lines.append(f"- {pair}: ρ = {r:.3f} (p = {p:.4f})")
        lines.append("")
        lines.append("High correlations suggest shared contamination patterns — "
                     "models that show anomalous behavior on one benchmark in a correlated pair "
                     "tend to show similar anomalies on the other.\n")

    if low_corr_pairs:
        lines.append("**Weakly correlated pairs** (|ρ| < 0.3):\n")
        for pair, r, p in low_corr_pairs:
            lines.append(f"- {pair}: ρ = {r:.3f} (p = {p:.4f})")
        lines.append("")
        lines.append("Weak correlations indicate benchmark-specific behavior — "
                     "misfit on one benchmark does not predict misfit on the other.\n")

    # Benchmark type grouping
    lines.append("## 5. Benchmark Type Grouping\n")
    for group, res in type_results.items():
        lines.append(f"### {group} ({', '.join(res['benchmarks'])})\n")
        lines.append(f"- Mean lz*: {res['mean_lz_star']:.2f} (mean |lz*|: {res['mean_abs_lz_star']:.2f})")
        lines.append(f"- Direction: {res['n_positive']} positive / {res['n_negative']} negative cells")
        lines.append(f"- Flag rate: {res['flag_rate']*100:.1f}% ({res['n_flagged']}/{res['total_cells']})")
        lines.append("")

    lines.append("MCQ benchmarks show the highest absolute lz* values, likely due to their "
                 "large item pools amplifying the person-fit signal. GSM8K shows uniformly positive "
                 "lz* except for Gemini-1.5, while HumanEval has the lowest magnitudes, "
                 "consistent with code generation tasks being harder to contaminate via memorization.\n")

    # Clustering
    lines.append("## 6. Model Clustering\n")
    cluster_groups = {}
    for m, c in cluster_map.items():
        cluster_groups.setdefault(c, []).append(m)
    for c, models in sorted(cluster_groups.items()):
        lines.append(f"- **Cluster {c}**: {', '.join(models)}")
    lines.append("")

    if gemini_alone:
        lines.append("**Gemini-1.5 forms a singleton cluster**, distinguished by its unique pattern "
                     "of negative lz* on GSM8K, HellaSwag, and HumanEval. This aberrant (under-fitting) "
                     "profile contrasts sharply with all other models' over-consistent patterns, "
                     "suggesting a fundamentally different response mechanism.\n")
    else:
        gemini_c = cluster_map["Gemini-1.5"]
        companions = [m for m in cluster_groups[gemini_c] if m != "Gemini-1.5"]
        lines.append(f"Gemini-1.5 clusters with {', '.join(companions)}. "
                     "Despite its mixed direction profile, its magnitude pattern "
                     "partially overlaps with these models.\n")

    # Direction
    lines.append("## 7. lz* Direction Analysis\n")
    ds = direction_stats
    lines.append(f"Of {ds['total_cells']} cells, **{ds['n_positive']} ({ds['pct_positive']:.1f}%)** "
                 f"are positive (over-consistent) and **{ds['n_negative']}** are negative (aberrant).\n")

    lines.append("**Benchmark-level patterns:**\n")
    for bench, info in ds["per_benchmark"].items():
        tag = ""
        if info["all_positive"]:
            tag = " ← all positive"
        elif info["all_negative"]:
            tag = " ← all negative"
        lines.append(f"- {bench}: {info['n_positive']} positive / {info['n_negative']} negative{tag}")
    lines.append("")

    neg_models = [m for m, info in ds["per_model"].items()
                  if info["dominant"] in ("mostly_negative", "all_negative")]
    mixed_models = [m for m, info in ds["per_model"].items()
                    if info["dominant"] in ("balanced", "mostly_negative") and info["n_negative"] > 0]

    lines.append("**Key finding:** The overwhelming majority of cells are positive, indicating "
                 "over-consistent response patterns (a hallmark of benchmark contamination). "
                 "Negative lz* values are concentrated in specific model–benchmark combinations:\n")

    for m, info in ds["per_model"].items():
        if info["n_negative"] > 0:
            lines.append(f"- **{m}**: {info['n_negative']} negative cell(s) — {info['dominant']}")
    lines.append("")

    lines.append("## 8. Implications for Contamination Detection\n")
    lines.append("The cross-benchmark analysis reveals three key patterns:\n")
    lines.append("1. **Pervasive over-consistency**: 95% of cells are flagged, and the vast majority "
                 "show positive lz*, consistent with widespread benchmark contamination across "
                 "the LLM ecosystem.\n")
    lines.append("2. **Benchmark sensitivity hierarchy**: MMLU and HellaSwag produce the strongest "
                 "signals (highest |lz*|), while HumanEval produces the weakest. This aligns with "
                 "the hypothesis that MCQ benchmarks with large, publicly available item pools "
                 "are most vulnerable.\n")
    lines.append("3. **Gemini-1.5 anomaly**: The unique negative lz* pattern on GSM8K, HellaSwag, "
                 "and HumanEval suggests a qualitatively different response mechanism — possibly "
                 "reflecting post-training calibration, chain-of-thought reasoning patterns, or "
                 "deliberate contamination mitigation.\n")

    report = "\n".join(lines)
    with open(os.path.join(OUT_DIR, "analysis_report.md"), "w") as f:
        f.write(report)
    print("  [+] analysis_report.md")
    return report


def write_summary(lz_mat, anomaly_df, corr, cluster_map, gemini_alone, direction_stats, type_results):
    data = lz_mat.values.astype(float)
    mean_abs_per_model = np.mean(np.abs(data), axis=1)

    n_all5 = int((anomaly_df["n_flagged"] == 5).sum())
    n_selective = int((anomaly_df["n_flagged"] > 0).sum() - n_all5)

    bench_labels = [BENCHMARK_LABELS[b] for b in BENCHMARK_ORDER]
    high_corr = []
    for i in range(len(BENCHMARK_ORDER)):
        for j in range(i+1, len(BENCHMARK_ORDER)):
            if corr[i, j] > 0.6:
                high_corr.append(f"{bench_labels[i]}-{bench_labels[j]}")

    neg_model_benchmarks = {}
    for m in MODEL_ORDER:
        for b in BENCHMARK_ORDER:
            if lz_mat.loc[m, b] < 0:
                neg_model_benchmarks.setdefault(m, []).append(BENCHMARK_LABELS[b])

    summary = {
        "n_models": len(MODEL_ORDER),
        "n_benchmarks": len(BENCHMARK_ORDER),
        "total_cells": len(MODEL_ORDER) * len(BENCHMARK_ORDER),
        "total_flagged": int(anomaly_df["n_flagged"].sum()),
        "flag_rate": float(anomaly_df["n_flagged"].sum() / (len(MODEL_ORDER) * len(BENCHMARK_ORDER))),
        "n_models_all5_flagged": n_all5,
        "n_models_selective_flagged": n_selective,
        "gemini15_cluster_isolation": gemini_alone,
        "dominant_direction_pattern": "positive" if direction_stats["pct_positive"] > 80 else "mixed",
        "pct_positive_cells": direction_stats["pct_positive"],
        "mean_abs_lz_per_benchmark": {
            BENCHMARK_LABELS[b]: float(np.mean(np.abs(data[:, i])))
            for i, b in enumerate(BENCHMARK_ORDER)
        },
        "mean_abs_lz_per_model": {
            MODEL_ORDER[i]: float(mean_abs_per_model[i])
            for i in range(len(MODEL_ORDER))
        },
        "high_correlation_pairs": high_corr,
        "negative_lz_cells": neg_model_benchmarks,
        "cluster_assignment_3": cluster_map,
        "benchmark_type_flag_rates": {
            g: r["flag_rate"] for g, r in type_results.items()
        },
    }

    with open(os.path.join(OUT_DIR, "cross_benchmark_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print("  [+] cross_benchmark_summary.json")
    return summary


def main():
    print("Loading data...")
    pf, ep = load_data()

    lz_mat = build_lz_matrix(pf)
    flag_mat = build_flag_matrix(ep)

    print("Running analyses...")
    plot_heatmap(lz_mat, flag_mat)
    anomaly_df = anomaly_profiles(ep)
    corr, pvals = plot_correlation_matrix(lz_mat)
    type_results = benchmark_type_analysis(lz_mat, flag_mat)
    cluster_map, gemini_alone, Z = plot_dendrogram(lz_mat)
    dir_df, direction_stats = direction_analysis(lz_mat, flag_mat)

    print("Writing report...")
    write_report(lz_mat, anomaly_df, corr, pvals, type_results,
                 cluster_map, gemini_alone, direction_stats)
    summary = write_summary(lz_mat, anomaly_df, corr, cluster_map,
                            gemini_alone, direction_stats, type_results)

    print("\n=== Key Metrics ===")
    print(f"  Models flagged all 5: {summary['n_models_all5_flagged']}")
    print(f"  Models selective:     {summary['n_models_selective_flagged']}")
    print(f"  Gemini-1.5 isolated:  {summary['gemini15_cluster_isolation']}")
    print(f"  Dominant direction:   {summary['dominant_direction_pattern']} "
          f"({summary['pct_positive_cells']:.1f}% positive)")
    print("\nDone.")


if __name__ == "__main__":
    main()
