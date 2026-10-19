"""
Analyze cross-lingual probe transfer results: generate plots + pass/fail judgment.

Reads transfer_results.csv (from transfer_eval.py) and train_metrics.csv (from train_probe.py).

Outputs:
  1. auroc_by_layer.png   — layer-depth vs AUROC, one line per language
  2. method_comparison.png — zero-shot vs mean-shift AUROC side-by-side
  3. summary.txt          — pass/fail judgment against ROADMAP criteria

Pass criteria (Director-specified):
  P1: English probe AUROC >= 0.60 AND ECE < 0.15
  P2: Zero-shot transfer AUROC >= 0.58 AND permutation p < 0.05 (>= 3/5 languages)
  P3: Layer-depth effect max-min AUROC >= 5pp
  P4: Mean-shift delta_AUROC >= 2pp (>= 3/5 languages)
Fail criteria:
  F1: English AUROC < 0.60
  F2: >= 3/5 languages zero-shot AUROC < 0.53
  F3: max-min layer AUROC < 3pp

Usage:
  python analyze_results.py \
    --transfer_csv ./results/transfer_results.csv \
    --train_csv ./probes/train_metrics.csv \
    --output_dir ./results
"""

import argparse
import os

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--transfer_csv", default="./results/transfer_results.csv")
    p.add_argument("--train_csv", default="./probes/train_metrics.csv")
    p.add_argument("--output_dir", default="./results")
    return p.parse_args()


def plot_auroc_by_layer(df_transfer, df_train, output_dir):
    """Line plot: layer depth vs AUROC, one line per language + English train."""
    fig, ax = plt.subplots(figsize=(10, 6))

    if df_train is not None and not df_train.empty:
        ax.plot(df_train["layer"], df_train["auroc"], "k-o", linewidth=2.5,
                markersize=7, label="en (train)", zorder=10)

    df_zs = df_transfer[df_transfer["method"] == "zero_shot"]
    languages = sorted(df_zs["language"].unique())
    cmap = plt.cm.Set2
    for i, lang in enumerate(languages):
        sub = df_zs[df_zs["language"] == lang].sort_values("layer")
        ax.plot(sub["layer"], sub["auroc"], "-s", color=cmap(i),
                linewidth=1.5, markersize=5, label=f"{lang} (zero-shot)")

    ax.axhline(0.5, color="gray", linestyle="--", alpha=0.5, label="chance")
    ax.axhline(0.60, color="red", linestyle=":", alpha=0.5, label="P1 threshold (0.60)")
    ax.axhline(0.58, color="orange", linestyle=":", alpha=0.5, label="P2 threshold (0.58)")

    ax.set_xlabel("Transformer Layer Index", fontsize=12)
    ax.set_ylabel("AUROC", fontsize=12)
    ax.set_title("Correctness Probe: Layer Depth vs. AUROC", fontsize=14)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.4, 1.0)

    path = os.path.join(output_dir, "auroc_by_layer.png")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved {path}")


def plot_method_comparison(df_transfer, output_dir):
    """Grouped bar chart: zero-shot vs mean-shift AUROC per language (best layer)."""
    languages = sorted(df_transfer["language"].unique())

    zs_best, ms_best = [], []
    for lang in languages:
        sub_zs = df_transfer[(df_transfer["language"] == lang) & (df_transfer["method"] == "zero_shot")]
        sub_ms = df_transfer[(df_transfer["language"] == lang) & (df_transfer["method"] == "mean_shift")]
        zs_best.append(sub_zs["auroc"].max() if not sub_zs.empty else 0)
        ms_best.append(sub_ms["auroc"].max() if not sub_ms.empty else 0)

    x = np.arange(len(languages))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    bars1 = ax.bar(x - width / 2, zs_best, width, label="Zero-shot", color="#5B9BD5")
    bars2 = ax.bar(x + width / 2, ms_best, width, label="Mean-shift", color="#ED7D31")

    ax.set_xlabel("Language", fontsize=12)
    ax.set_ylabel("Best AUROC (across layers)", fontsize=12)
    ax.set_title("Zero-shot vs Mean-shift Transfer", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(languages)
    ax.legend()
    ax.axhline(0.58, color="orange", linestyle=":", alpha=0.5)
    ax.set_ylim(0.4, 1.0)
    ax.grid(True, axis="y", alpha=0.3)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            ax.annotate(f"{h:.2f}", xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=8)

    path = os.path.join(output_dir, "method_comparison.png")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved {path}")


def pass_fail_judgment(df_transfer, df_train):
    """Evaluate Director-specified pass/fail criteria. Returns (verdict_lines, overall_pass)."""
    lines = []
    passes = []
    fails = []

    # --- Pass criteria ---

    # P1: English probe AUROC >= 0.60 AND ECE < 0.15
    if df_train is not None and not df_train.empty:
        best_en_auroc = df_train["auroc"].max()
        best_en_ece = df_train.loc[df_train["auroc"].idxmax(), "ece"]
        p1 = best_en_auroc >= 0.60 and best_en_ece < 0.15
        lines.append(f"P1  English AUROC >= 0.60 & ECE < 0.15:  AUROC={best_en_auroc:.4f} ECE={best_en_ece:.4f}  {'PASS' if p1 else 'FAIL'}")
    else:
        p1 = False
        best_en_auroc = 0
        lines.append("P1  English AUROC >= 0.60 & ECE < 0.15:  NO DATA  FAIL")
    passes.append(p1)

    # P2: Zero-shot AUROC >= 0.58 AND p < 0.05 for >= 3/5 languages
    df_zs = df_transfer[df_transfer["method"] == "zero_shot"]
    languages = sorted(df_zs["language"].unique())
    p2_details = []
    lang_pass_count = 0
    for lang in languages:
        sub = df_zs[df_zs["language"] == lang]
        if sub.empty:
            p2_details.append(f"  {lang}: NO DATA")
            continue
        best_row = sub.loc[sub["auroc"].idxmax()]
        best_auroc = best_row["auroc"]
        best_p = best_row.get("p_value", 1.0)
        lang_ok = best_auroc >= 0.58 and (best_p < 0.05 if not np.isnan(best_p) else False)
        if lang_ok:
            lang_pass_count += 1
        p2_details.append(f"  {lang}: AUROC={best_auroc:.4f} p={best_p:.4f} {'ok' if lang_ok else 'x'}")
    p2 = lang_pass_count >= 3
    lines.append(f"P2  Zero-shot AUROC >= 0.58 & p < 0.05 (>= 3/5):  {lang_pass_count}/{len(languages)}  {'PASS' if p2 else 'FAIL'}")
    lines.extend(p2_details)
    passes.append(p2)

    # P3: Layer-depth effect max-min >= 5pp
    if df_train is not None and not df_train.empty:
        delta = df_train["auroc"].max() - df_train["auroc"].min()
        p3 = delta >= 0.05
        lines.append(f"P3  Layer-depth delta >= 5pp:  delta={delta:.4f}  {'PASS' if p3 else 'FAIL'}")
    else:
        p3 = False
        delta = 0
        lines.append("P3  Layer-depth delta >= 5pp:  NO DATA  FAIL")
    passes.append(p3)

    # P4: Mean-shift ΔAUROC >= 2pp for >= 3/5 languages
    improved_count = 0
    p4_details = []
    for lang in languages:
        zs_sub = df_zs[df_zs["language"] == lang]
        ms_sub = df_transfer[(df_transfer["language"] == lang) & (df_transfer["method"] == "mean_shift")]
        zs_best = zs_sub["auroc"].max() if not zs_sub.empty else 0
        ms_best = ms_sub["auroc"].max() if not ms_sub.empty else 0
        delta_ms = ms_best - zs_best
        lang_ok = delta_ms >= 0.02
        if lang_ok:
            improved_count += 1
        p4_details.append(f"  {lang}: zs={zs_best:.4f} ms={ms_best:.4f} Δ={delta_ms:+.4f} {'ok' if lang_ok else 'x'}")
    p4 = improved_count >= 3
    lines.append(f"P4  Mean-shift Δ >= 2pp (>= 3/5):  {improved_count}/{len(languages)}  {'PASS' if p4 else 'FAIL'}")
    lines.extend(p4_details)
    passes.append(p4)

    # --- Fail criteria (hard stops) ---
    lines.append("\n--- Hard Fail Checks ---")

    # F1: English AUROC < 0.60
    f1 = best_en_auroc < 0.60
    lines.append(f"F1  English AUROC < 0.60:  {best_en_auroc:.4f}  {'!! HARD FAIL' if f1 else 'ok'}")
    fails.append(f1)

    # F2: >= 3/5 languages zero-shot AUROC < 0.53
    low_count = 0
    for lang in languages:
        sub = df_zs[df_zs["language"] == lang]
        best = sub["auroc"].max() if not sub.empty else 0
        if best < 0.53:
            low_count += 1
    f2 = low_count >= 3
    lines.append(f"F2  >= 3/5 langs zero-shot < 0.53:  {low_count}/{len(languages)}  {'!! HARD FAIL' if f2 else 'ok'}")
    fails.append(f2)

    # F3: max-min layer AUROC < 3pp
    f3 = delta < 0.03
    lines.append(f"F3  Layer delta < 3pp:  {delta:.4f}  {'!! HARD FAIL' if f3 else 'ok'}")
    fails.append(f3)

    any_hard_fail = any(fails)
    overall_pass = all(passes) and not any_hard_fail

    if any_hard_fail:
        lines.append(f"\nOVERALL: HARD FAIL — fundamental assumptions not supported")
    elif overall_pass:
        lines.append(f"\nOVERALL: PASS — proceed to full experiments")
    else:
        lines.append(f"\nOVERALL: PARTIAL — some criteria not met, review before proceeding")
    return lines, overall_pass


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    df_transfer = pd.read_csv(args.transfer_csv)
    df_transfer = df_transfer.dropna(subset=["auroc"])

    df_train = None
    if os.path.exists(args.train_csv):
        df_train = pd.read_csv(args.train_csv)

    plot_auroc_by_layer(df_transfer, df_train, args.output_dir)
    plot_method_comparison(df_transfer, args.output_dir)

    verdict_lines, overall = pass_fail_judgment(df_transfer, df_train)

    print("\n" + "=" * 60)
    print("  MVP Pass/Fail Judgment")
    print("=" * 60)
    for line in verdict_lines:
        print(f"  {line}")
    print("=" * 60)

    summary_path = os.path.join(args.output_dir, "summary.txt")
    with open(summary_path, "w") as f:
        f.write("MVP Pass/Fail Judgment\n")
        f.write("=" * 50 + "\n")
        for line in verdict_lines:
            f.write(line + "\n")

    # Per-language detail table
    with open(summary_path, "a") as f:
        f.write("\n\nDetailed Results by Language\n")
        f.write("-" * 50 + "\n")
        languages = sorted(df_transfer["language"].unique())
        for lang in languages:
            f.write(f"\n--- {lang} ---\n")
            sub = df_transfer[df_transfer["language"] == lang].sort_values(["method", "layer"])
            f.write(sub.to_string(index=False))
            f.write("\n")

    print(f"\nSummary saved to {summary_path}")


if __name__ == "__main__":
    main()
