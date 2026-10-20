"""Two-sided person-fit detection: flag models with |lz*| > 1.96.

Input:  artifacts/phase_b_results/personfit_matrix.csv
Output: artifacts/phase_b_two_sided/
  - two_sided_flags.csv
  - model_anomaly_profile.csv
  - two_sided_summary.json
  - two_sided_heatmap.png
"""

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_CSV = os.path.join(PROJECT_DIR, "artifacts", "phase_b_results", "personfit_matrix.csv")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "artifacts", "phase_b_two_sided")

MODEL_NAMES = {
    0: "360GPT2-Pro",
    1: "DeepSeek-V3",
    2: "Doubao-pro",
    3: "Gemini-1.5",
    4: "Gemma-2B-it",
    5: "Hunyuan-Turbo",
    6: "Mistral-7B-Instruct-v0.1",
    7: "Moonshot-v1",
    8: "Qwen-Plus",
    9: "Qwen2.5-3B-Instruct",
    10: "Vicuna-7B-v1.3",
    11: "Yi-Lightning",
}

THRESHOLD = 1.96


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = pd.read_csv(INPUT_CSV)
    df["model_name"] = df["student_id"].map(MODEL_NAMES)

    # --- two_sided_flags.csv ---
    df["direction"] = np.where(
        df["lz_star"] > THRESHOLD, "positive",
        np.where(df["lz_star"] < -THRESHOLD, "negative", "normal")
    )
    df["flagged"] = df["lz_star"].abs() > THRESHOLD

    flags = df[["student_id", "model_name", "benchmark", "lz_star",
                "direction", "flagged", "theta", "accuracy"]].copy()
    flags.to_csv(os.path.join(OUTPUT_DIR, "two_sided_flags.csv"), index=False)

    # --- model_anomaly_profile.csv ---
    profiles = []
    for sid, group in df.groupby("student_id"):
        flagged_rows = group[group["flagged"]]
        profiles.append({
            "student_id": sid,
            "model_name": MODEL_NAMES[sid],
            "n_flagged": int(flagged_rows.shape[0]),
            "n_pos_flagged": int((flagged_rows["direction"] == "positive").sum()),
            "n_neg_flagged": int((flagged_rows["direction"] == "negative").sum()),
            "benchmarks_flagged": ",".join(sorted(flagged_rows["benchmark"].tolist())) if len(flagged_rows) > 0 else "",
            "mean_abs_lz_star": float(group["lz_star"].abs().mean()),
        })
    profile_df = pd.DataFrame(profiles)
    profile_df.to_csv(os.path.join(OUTPUT_DIR, "model_anomaly_profile.csv"), index=False)

    # --- two_sided_summary.json ---
    benchmarks = sorted(df["benchmark"].unique())
    summary = {
        "threshold": THRESHOLD,
        "total_cells": len(df),
        "total_flagged": int(df["flagged"].sum()),
        "total_pos_flagged": int((df["direction"] == "positive").sum()),
        "total_neg_flagged": int((df["direction"] == "negative").sum()),
        "total_normal": int((df["direction"] == "normal").sum()),
        "by_benchmark": {},
    }
    for bm in benchmarks:
        sub = df[df["benchmark"] == bm]
        summary["by_benchmark"][bm] = {
            "n_flagged": int(sub["flagged"].sum()),
            "n_pos_flagged": int((sub["direction"] == "positive").sum()),
            "n_neg_flagged": int((sub["direction"] == "negative").sum()),
            "mean_lz_star": float(sub["lz_star"].mean()),
            "std_lz_star": float(sub["lz_star"].std()),
            "flagged_models": sorted(sub[sub["flagged"]]["model_name"].tolist()),
        }
    with open(os.path.join(OUTPUT_DIR, "two_sided_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    # --- two_sided_heatmap.png ---
    model_order = [MODEL_NAMES[i] for i in range(12)]
    pivot = df.pivot(index="model_name", columns="benchmark", values="lz_star")
    pivot = pivot.reindex(index=model_order, columns=benchmarks)

    flag_pivot = df.pivot(index="model_name", columns="benchmark", values="flagged")
    flag_pivot = flag_pivot.reindex(index=model_order, columns=benchmarks)

    vmax = max(abs(pivot.values.min()), abs(pivot.values.max()))

    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(pivot.values, cmap="RdBu_r", aspect="auto",
                   vmin=-vmax, vmax=vmax)

    ax.set_xticks(range(len(benchmarks)))
    ax.set_xticklabels(benchmarks, rotation=45, ha="right", fontsize=10)
    ax.set_yticks(range(len(model_order)))
    ax.set_yticklabels(model_order, fontsize=10)

    for i in range(len(model_order)):
        for j in range(len(benchmarks)):
            val = pivot.values[i, j]
            is_flagged = flag_pivot.values[i, j]
            color = "white" if abs(val) > vmax * 0.6 else "black"
            weight = "bold" if is_flagged else "normal"
            text = f"{val:.1f}"
            if is_flagged:
                text += " *"
            ax.text(j, i, text, ha="center", va="center",
                    fontsize=7.5, color=color, fontweight=weight)

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("lz* statistic", fontsize=11)

    ax.axhline(y=-0.5, color="gray", linewidth=0.5)
    for idx in range(len(model_order)):
        ax.axhline(y=idx + 0.5, color="gray", linewidth=0.3)
    for idx in range(len(benchmarks)):
        ax.axvline(x=idx + 0.5, color="gray", linewidth=0.3)

    ax.set_title("Two-sided Person-Fit Detection: lz* Heatmap\n(* = |lz*| > 1.96)",
                 fontsize=13, pad=12)

    pos_patch = mpatches.Patch(color="#d73027", label="Positive lz* (over-consistent)")
    neg_patch = mpatches.Patch(color="#4575b4", label="Negative lz* (aberrant)")
    ax.legend(handles=[pos_patch, neg_patch], loc="upper left",
              bbox_to_anchor=(0, -0.12), ncol=2, fontsize=9, frameon=False)

    plt.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "two_sided_heatmap.png"), dpi=200,
                bbox_inches="tight")
    plt.close(fig)

    print(f"Output written to {OUTPUT_DIR}")
    print(f"  Total flagged: {summary['total_flagged']}/{summary['total_cells']} "
          f"(pos={summary['total_pos_flagged']}, neg={summary['total_neg_flagged']})")
    for bm in benchmarks:
        s = summary["by_benchmark"][bm]
        print(f"  {bm}: {s['n_flagged']} flagged (pos={s['n_pos_flagged']}, neg={s['n_neg_flagged']})")


if __name__ == "__main__":
    main()
