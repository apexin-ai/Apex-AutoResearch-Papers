# RGDS MVP result analysis: load per-generation metrics, produce figures + PASS/FAIL verdict.
# Usage: python analyze_mvp.py --results_dir ./results --output_dir ./figures
# Expects: results/{method}/gen_{i}/metrics.json for each method and generation.

import argparse
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 9,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

METHODS = ["rgds", "external_only", "uncurated"]
METHOD_LABELS = {"rgds": "RGDS (ours)", "external_only": "External-only", "uncurated": "Uncurated"}
METHOD_COLORS = {"rgds": "#2171B5", "external_only": "#E6550D", "uncurated": "#737373"}
METHOD_MARKERS = {"rgds": "o", "external_only": "s", "uncurated": "^"}


def parse_args():
    p = argparse.ArgumentParser(description="Analyze RGDS MVP results")
    p.add_argument("--results_dir", type=str, default="./results")
    p.add_argument("--output_dir", type=str, default="./figures")
    p.add_argument("--num_generations", type=int, default=4)
    return p.parse_args()


def load_metrics(results_dir, num_generations):
    """Load metrics.json for each method and generation. Returns {method: [metrics_dict_per_gen]}."""
    data = {}
    for method in METHODS:
        method_dir = Path(results_dir) / method
        if not method_dir.exists():
            continue
        all_results_path = method_dir / "all_results.json"
        if all_results_path.exists():
            with open(all_results_path) as f:
                all_res = json.load(f)
            data[method] = {
                "generations": all_res.get("generations", []),
                "rankme_gen0": all_res.get("rankme_gen0", None),
            }
            continue
        gens = []
        for g in range(num_generations):
            mpath = method_dir / f"gen_{g}" / "metrics.json"
            if mpath.exists():
                with open(mpath) as f:
                    gens.append(json.load(f))
        if gens:
            data[method] = {"generations": gens, "rankme_gen0": None}
    return data


def extract_series(data, metric_key):
    """Extract {method: (generations_list, values_list)} for a given metric."""
    series = {}
    for method, mdata in data.items():
        gens_list = mdata["generations"]
        xs = [g.get("generation", i) for i, g in enumerate(gens_list)]
        ys = [g.get(metric_key, None) for g in gens_list]
        if any(y is not None for y in ys):
            series[method] = (xs, ys)
    return series


def plot_metric(series, ylabel, title, output_path, hlines=None, rankme_gen0=None):
    """Generic line plot for a single metric across methods."""
    fig, ax = plt.subplots(figsize=(5.5, 3.8))

    for method, (xs, ys) in series.items():
        valid = [(x, y) for x, y in zip(xs, ys) if y is not None]
        if not valid:
            continue
        vx, vy = zip(*valid)
        ax.plot(vx, vy,
                color=METHOD_COLORS.get(method, "#333"),
                marker=METHOD_MARKERS.get(method, "o"),
                markersize=6, linewidth=1.8,
                label=METHOD_LABELS.get(method, method))

    if rankme_gen0 is not None:
        ax.axhline(rankme_gen0, color="#999", linestyle="--", linewidth=1, label=f"Gen-0 baseline ({rankme_gen0:.1f})")

    if hlines:
        for val, label, color in hlines:
            ax.axhline(val, color=color, linestyle=":", linewidth=1, label=label)

    ax.set_xlabel("Generation")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc="best", framealpha=0.9)
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    fig.savefig(output_path)
    plt.close(fig)
    print(f"  Saved: {output_path}")


def plot_rankme(data, output_dir):
    series = extract_series(data, "rankme")
    rankme_gen0 = None
    for mdata in data.values():
        if mdata.get("rankme_gen0") is not None:
            rankme_gen0 = mdata["rankme_gen0"]
            break

    hlines = []
    if rankme_gen0 is not None:
        tau_rank_value = rankme_gen0 * 0.5
        hlines.append((tau_rank_value, f"τ_rank threshold ({tau_rank_value:.1f})", "#D62728"))

    plot_metric(series, "RankMe (effective rank)", "RankMe Trajectory",
                Path(output_dir) / "rankme_trajectory.pdf",
                hlines=hlines, rankme_gen0=rankme_gen0)


def plot_perplexity(data, output_dir):
    series = extract_series(data, "held_out_perplexity")
    plot_metric(series, "Held-out Perplexity", "Downstream Perplexity",
                Path(output_dir) / "perplexity_trajectory.pdf")


def plot_rare_ngram(data, output_dir):
    series = extract_series(data, "rare_ngram_survival")
    plot_metric(series, "Rare N-gram Survival", "Rare N-gram Survival Rate",
                Path(output_dir) / "rare_ngram_trajectory.pdf")


def plot_knn(data, output_dir):
    series = extract_series(data, "knn_probe_accuracy")
    hlines = [(0.6, "τ_knn = 0.6", "#D62728")]
    plot_metric(series, "k-NN Probe Accuracy", "k-NN Probe Accuracy (Rare vs Common)",
                Path(output_dir) / "knn_trajectory.pdf", hlines=hlines)


def plot_rank_correlation(data, output_dir):
    series = extract_series(data, "rank_correlation")
    plot_metric(series, "Spearman ρ", "Rank Correlation (Internal vs Contriever)",
                Path(output_dir) / "rank_correlation_trajectory.pdf")


def pass_fail_analysis(data):
    """Determine PASS/FAIL based on MVP criteria."""
    print("\n" + "=" * 60)
    print("PASS/FAIL ANALYSIS")
    print("=" * 60)

    verdict = {"pass": True, "reasons": []}

    # --- Criterion 1: RankMe monotonic decline check ---
    if "rgds" in data:
        rankme_vals = [g.get("rankme") for g in data["rgds"]["generations"] if g.get("rankme") is not None]
        if len(rankme_vals) >= 2:
            declines = sum(1 for i in range(1, len(rankme_vals)) if rankme_vals[i] < rankme_vals[i - 1])
            total_steps = len(rankme_vals) - 1
            monotonic_decline = declines == total_steps
            near_monotonic = declines >= total_steps * 0.7

            print(f"\n1. RankMe decline check:")
            print(f"   Values: {[f'{v:.2f}' for v in rankme_vals]}")
            print(f"   Declining steps: {declines}/{total_steps}")
            if monotonic_decline:
                print(f"   ⚠️  Monotonic decline detected — representation collapse risk")
                verdict["reasons"].append(f"RankMe monotonically declining ({declines}/{total_steps} steps)")
                verdict["pass"] = False
            elif near_monotonic:
                print(f"   ⚠️  Near-monotonic decline ({declines}/{total_steps}) — borderline")
                verdict["reasons"].append(f"RankMe near-monotonic decline ({declines}/{total_steps} steps)")
            else:
                print(f"   ✅ RankMe stable or recovering")
        else:
            print("\n1. RankMe decline check: insufficient data")

    # --- Criterion 2: RGDS vs external_only perplexity improvement ≥ 5% ---
    if "rgds" in data and "external_only" in data:
        rgds_ppls = [g.get("held_out_perplexity") for g in data["rgds"]["generations"]]
        ext_ppls = [g.get("held_out_perplexity") for g in data["external_only"]["generations"]]

        print(f"\n2. Downstream perplexity (RGDS vs External-only):")
        print(f"   RGDS PPL:     {[f'{v:.2f}' if v else 'N/A' for v in rgds_ppls]}")
        print(f"   External PPL: {[f'{v:.2f}' if v else 'N/A' for v in ext_ppls]}")

        improvements = []
        for i in range(len(rgds_ppls)):
            if rgds_ppls[i] is not None and ext_ppls[i] is not None and ext_ppls[i] > 0:
                imp = (ext_ppls[i] - rgds_ppls[i]) / ext_ppls[i] * 100
                improvements.append(imp)

        if improvements:
            # Use gen 1-3 (skip gen 0 which has identical starting point)
            later_improvements = improvements[1:] if len(improvements) > 1 else improvements
            avg_improvement = np.mean(later_improvements)
            print(f"   Per-gen improvements: {[f'{v:.2f}%' for v in improvements]}")
            print(f"   Avg improvement (gen 1+): {avg_improvement:.2f}%")

            if avg_improvement >= 5.0:
                print(f"   ✅ PASS: ≥5% improvement ({avg_improvement:.2f}%)")
            else:
                print(f"   ❌ FAIL: <5% improvement ({avg_improvement:.2f}%)")
                verdict["pass"] = False
                verdict["reasons"].append(f"Avg PPL improvement {avg_improvement:.2f}% < 5% threshold")
        else:
            print("   Insufficient data for comparison")
    else:
        missing = [m for m in ["rgds", "external_only"] if m not in data]
        print(f"\n2. Downstream perplexity: missing methods {missing}")
        verdict["pass"] = False
        verdict["reasons"].append(f"Missing methods for PPL comparison: {missing}")

    # --- Criterion 3: k-NN probe stays above τ_knn ---
    if "rgds" in data:
        knn_vals = [g.get("knn_probe_accuracy") for g in data["rgds"]["generations"] if g.get("knn_probe_accuracy") is not None]
        print(f"\n3. k-NN probe accuracy (RGDS):")
        print(f"   Values: {[f'{v:.4f}' for v in knn_vals]}")
        below_threshold = [v for v in knn_vals if v < 0.6]
        if below_threshold:
            print(f"   ⚠️  {len(below_threshold)} values below τ_knn=0.6")
        else:
            print(f"   ✅ All above τ_knn=0.6")

    # --- Overall verdict ---
    print(f"\n{'=' * 60}")
    if verdict["pass"]:
        print("🟢 OVERALL VERDICT: PASS")
        print("   RGDS demonstrates representation-grounded selection advantage")
    else:
        print("🔴 OVERALL VERDICT: FAIL")
        for r in verdict["reasons"]:
            print(f"   - {r}")
    print("=" * 60)

    return verdict


def print_summary_table(data):
    """Print markdown summary table of all methods × generations × metrics."""
    print("\n## Summary Table\n")
    metrics = ["held_out_perplexity", "rankme", "knn_probe_accuracy", "rare_ngram_survival", "rank_correlation"]
    headers = ["Method", "Gen", "PPL↓", "RankMe↑", "k-NN↑", "Rare↑", "Corr↑"]
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["---"] * len(headers)) + " |")

    for method in METHODS:
        if method not in data:
            continue
        for g in data[method]["generations"]:
            gen = g.get("generation", "?")
            ppl = f"{g['held_out_perplexity']:.2f}" if g.get("held_out_perplexity") else "—"
            rankme = f"{g['rankme']:.2f}" if g.get("rankme") else "—"
            knn = f"{g['knn_probe_accuracy']:.4f}" if g.get("knn_probe_accuracy") else "—"
            rare = f"{g['rare_ngram_survival']:.4f}" if g.get("rare_ngram_survival") else "—"
            corr = f"{g['rank_correlation']:.4f}" if g.get("rank_correlation") else "—"
            label = METHOD_LABELS.get(method, method)
            print(f"| {label} | {gen} | {ppl} | {rankme} | {knn} | {rare} | {corr} |")


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    print("Loading metrics...")
    data = load_metrics(args.results_dir, args.num_generations)

    if not data:
        print(f"ERROR: No metrics found in {args.results_dir}/")
        print(f"Expected: {{results_dir}}/{{method}}/gen_{{i}}/metrics.json")
        sys.exit(1)

    found = list(data.keys())
    print(f"Found methods: {found}")
    for method in found:
        n_gens = len(data[method]["generations"])
        print(f"  {method}: {n_gens} generations")

    print("\nGenerating figures...")
    plot_rankme(data, args.output_dir)
    plot_perplexity(data, args.output_dir)
    plot_rare_ngram(data, args.output_dir)
    plot_knn(data, args.output_dir)
    plot_rank_correlation(data, args.output_dir)

    print_summary_table(data)
    verdict = pass_fail_analysis(data)

    verdict_path = Path(args.output_dir) / "verdict.json"
    with open(verdict_path, "w") as f:
        json.dump(verdict, f, indent=2)
    print(f"\nVerdict saved to {verdict_path}")

    return 0 if verdict["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
