"""Statistical analysis and visualization of experiment results.

Input: eval_exp1.json, eval_exp2.json from evaluate.py
Output: Figures (PDF/PNG), statistical summary
Dependencies: matplotlib, scipy, numpy
"""
import argparse
import json
import logging
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

logger = logging.getLogger(__name__)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "black",
    "axes.linewidth": 0.8,
    "legend.fontsize": 10,
})

COUNT_COLORS = {
    "count_3": "#2ca02c",
    "count_6": "#1f77b4",
    "count_12": "#ff7f0e",
    "count_24": "#d62728",
}


def load_eval(path: str) -> dict:
    """Load evaluation JSON."""
    with open(path, "r") as f:
        return json.load(f)


def _get_metrics(batch_metrics: dict, eval_mode: str) -> dict:
    """Get metrics dict for eval_mode with fallback."""
    result = batch_metrics.get(eval_mode)
    if result is not None:
        return result
    if eval_mode == "text_match":
        logger.debug("text_match not available, falling back to relaxed")
        return batch_metrics.get("relaxed", batch_metrics.get("exact", {}))
    return batch_metrics.get("exact", {})


def pearson_ci(r: float, n: int, alpha: float = 0.05) -> tuple:
    """95% confidence interval for Pearson r via Fisher z-transform."""
    if n < 4 or np.isnan(r):
        return (float("nan"), float("nan"))
    z = np.arctanh(r)
    se = 1.0 / math.sqrt(n - 3)
    z_crit = stats.norm.ppf(1 - alpha / 2)
    return (float(np.tanh(z - z_crit * se)), float(np.tanh(z + z_crit * se)))


def partial_corr(x, y, z):
    """Partial correlation r(x, y | z). Returns (r, p)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    z = np.asarray(z, dtype=float)
    if len(x) < 4:
        return float("nan"), float("nan")
    def _resid(a, b):
        slope, intercept = np.polyfit(b, a, 1)
        return a - (slope * b + intercept)
    return stats.pearsonr(_resid(x, z), _resid(y, z))


# ----------------------------------------------------------------------
# Exp 1: Count-Quality
# ----------------------------------------------------------------------

def analyze_exp1(eval_results: dict, output_dir: Path,
                 eval_mode: str = "relaxed"):
    """Count-Quality analysis: how does # types affect F1?"""
    count_f1s = {}
    for bid, metrics in eval_results.items():
        count_key = metrics.get("count_key", bid.split("_random")[0])
        count = int(count_key.replace("count_", ""))
        f1 = _get_metrics(metrics, eval_mode).get("f1", 0.0)
        count_f1s.setdefault(count, []).append(f1)

    counts = sorted(count_f1s.keys())
    means = [np.mean(count_f1s[c]) for c in counts]
    stds = [np.std(count_f1s[c]) for c in counts]

    logger.info("Count-Quality Table (%s):", eval_mode)
    logger.info("  %-8s %-10s %-10s %-5s", "Count", "Mean F1", "Std F1", "N")
    for c, m, s in zip(counts, means, stds):
        logger.info("  %-8d %-10.4f %-10.4f %-5d", c, m, s, len(count_f1s[c]))

    mode_label = eval_mode.replace("_", " ").title()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.errorbar(counts, means, yerr=stds, marker="o", capsize=4,
                linewidth=1.5, markersize=6, color="#2c7bb6")
    ax.set_xlabel("Number of Types in Batch")
    ax.set_ylabel(f"{mode_label} F1 Score")
    ax.set_title("Count-Quality Curve")
    ax.set_xticks(counts)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(output_dir / "fig_count_quality.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / "fig_count_quality.png", dpi=300, bbox_inches="tight")
    plt.close()
    logger.info("Saved Count-Quality figure")

    return {
        "eval_mode": eval_mode,
        "counts": counts,
        "means": means,
        "stds": stds,
        "n_per_count": [len(count_f1s[c]) for c in counts],
    }


# ----------------------------------------------------------------------
# Exp 2: Within-count Pearson r(F1, BCS)  (D003)
# ----------------------------------------------------------------------

def analyze_exp2(eval_results: dict, output_dir: Path,
                 solo_f1: dict = None, eval_mode: str = "relaxed"):
    """Within-count Pearson r(F1, BCS) analysis per D003.

    Primary: per-count correlation between relaxed F1 and BCS.
    Also reports recall vs BCS. Delta kept as supplementary only.
    Pass criteria: |r| >= 0.3 and p < 0.05.
    """
    by_count = {}
    for bid, metrics in eval_results.items():
        count_key = metrics.get("count_key", "")
        if not count_key:
            continue
        m = _get_metrics(metrics, eval_mode)
        f1 = m.get("f1", 0.0)
        recall = m.get("recall", 0.0)
        precision = m.get("precision", 0.0)

        delta_f1 = None
        if solo_f1 and "per_type_f1" in metrics:
            deltas = [solo_f1[t] - bf1
                      for t, bf1 in metrics["per_type_f1"].items()
                      if t in solo_f1]
            if deltas:
                delta_f1 = float(np.mean(deltas))

        count_num = int(count_key.replace("count_", ""))
        by_count.setdefault(count_key, []).append({
            "bid": bid,
            "bcs": metrics["bcs"],
            "f1": f1,
            "recall": recall,
            "precision": precision,
            "delta_f1": delta_f1,
            "count": count_num,
        })

    summary = {}
    mode_label = eval_mode.replace("_", " ").title()
    all_bcs, all_f1, all_recall, all_counts = [], [], [], []

    for count_key, entries in sorted(by_count.items()):
        bcs = np.array([e["bcs"] for e in entries])
        f1s = np.array([e["f1"] for e in entries])
        recalls = np.array([e["recall"] for e in entries])
        n = len(entries)

        all_bcs.extend(bcs)
        all_f1.extend(f1s)
        all_recall.extend(recalls)
        all_counts.extend([entries[0]["count"]] * n)

        if n >= 3:
            r_f1, p_f1 = stats.pearsonr(bcs, f1s)
            ci_f1 = pearson_ci(r_f1, n)
            r_rec, p_rec = stats.pearsonr(bcs, recalls)
            ci_rec = pearson_ci(r_rec, n)
        else:
            r_f1 = p_f1 = r_rec = p_rec = float("nan")
            ci_f1 = ci_rec = (float("nan"), float("nan"))

        pass_f1 = ("PASS" if (not np.isnan(r_f1) and abs(r_f1) >= 0.3
                              and p_f1 < 0.05)
                   else "FAIL")
        pass_recall = ("PASS" if (not np.isnan(r_rec) and abs(r_rec) >= 0.3
                                  and p_rec < 0.05)
                       else "FAIL")

        # t-test on top/bottom third by BCS (random batches only)
        rand = sorted([e for e in entries if "random" in e["bid"]],
                      key=lambda x: x["bcs"])
        k = max(1, len(rand) // 3)
        if k >= 2 and len(rand) >= 2 * k:
            t_stat, t_p = stats.ttest_ind(
                [e["f1"] for e in rand[-k:]],
                [e["f1"] for e in rand[:k]])
        else:
            t_stat, t_p = float("nan"), float("nan")

        # Supplementary: delta (solo - batch) correlation
        delta_sup = {}
        de = [e for e in entries if e["delta_f1"] is not None]
        if len(de) >= 3:
            r_d, p_d = stats.pearsonr([e["bcs"] for e in de],
                                      [e["delta_f1"] for e in de])
            delta_sup = {"pearson_r": r_d, "pearson_p": p_d, "n": len(de)}

        summary[count_key] = {
            "f1_vs_bcs": {
                "pearson_r": r_f1, "pearson_p": p_f1,
                "ci_95": list(ci_f1), "n": n,
                "pass_fail": pass_f1, "role": "supplementary",
            },
            "recall_vs_bcs": {
                "pearson_r": r_rec, "pearson_p": p_rec,
                "ci_95": list(ci_rec), "n": n,
                "pass_fail": pass_recall, "role": "primary",
            },
            "ttest_top_bottom_third": {"t": t_stat, "p": t_p},
            "delta_supplementary": delta_sup,
            "n_batches": n,
        }

        logger.info(
            "%s: [PRIMARY] r(recall,BCS)=%.4f (p=%.4f, CI=[%.3f,%.3f], n=%d) -> %s",
            count_key, r_rec, p_rec, ci_rec[0], ci_rec[1], n, pass_recall)
        logger.info(
            "  [supplementary] r(F1,BCS)=%.4f (p=%.4f) -> %s",
            r_f1, p_f1, pass_f1)

    # Partial correlation across counts
    if len(set(all_counts)) >= 2 and len(all_bcs) >= 6:
        pr_f1, pp_f1 = partial_corr(all_bcs, all_f1, all_counts)
        pr_rec, pp_rec = partial_corr(all_bcs, all_recall, all_counts)
        n_all = len(all_bcs)
        summary["partial_corr"] = {
            "f1_vs_bcs_controlling_count": {
                "r": pr_f1, "p": pp_f1, "n": n_all,
                "ci_95": list(pearson_ci(pr_f1, n_all)),
            },
            "recall_vs_bcs_controlling_count": {
                "r": pr_rec, "p": pp_rec, "n": n_all,
                "ci_95": list(pearson_ci(pr_rec, n_all)),
            },
        }
        logger.info("Partial r(F1,BCS|count)=%.4f (p=%.4f, n=%d)",
                     pr_f1, pp_f1, n_all)
        logger.info("Partial r(recall,BCS|count)=%.4f (p=%.4f, n=%d)",
                     pr_rec, pp_rec, n_all)

    # Visualization
    _plot_scatter(by_count, summary, output_dir, "f1",
                  f"{mode_label} F1", "exp2_analysis_f1")
    _plot_scatter(by_count, summary, output_dir, "recall",
                  f"{mode_label} Recall", "exp2_analysis_recall")

    return summary


def _plot_scatter(by_count, summary, output_dir, y_field, y_label, fname):
    """BCS vs y_field scatter with regression, per count + combined."""
    n_counts = len(by_count)
    if n_counts == 0:
        return

    fig, axes = plt.subplots(1, n_counts, figsize=(6 * n_counts, 4.5),
                             squeeze=False)
    fig2, ax2 = plt.subplots(figsize=(6, 4.5))

    for idx, (ck, entries) in enumerate(sorted(by_count.items())):
        ax = axes[0, idx]
        bcs = np.array([e["bcs"] for e in entries])
        yv = np.array([e[y_field] for e in entries])

        for e in entries:
            if "low_bcs" in e["bid"]:
                ax.scatter(e["bcs"], e[y_field], c="#2ca02c", s=80,
                           zorder=5, label="Low BCS", marker="^")
            elif "high_bcs" in e["bid"]:
                ax.scatter(e["bcs"], e[y_field], c="#d62728", s=80,
                           zorder=5, label="High BCS", marker="v")
            else:
                ax.scatter(e["bcs"], e[y_field], c="#1f77b4", s=40,
                           zorder=4, alpha=0.7)

        slope = intercept = None
        xl = None
        if len(bcs) >= 3:
            slope, intercept = np.polyfit(bcs, yv, 1)
            xl = np.linspace(bcs.min(), bcs.max(), 100)
            ax.plot(xl, slope * xl + intercept, "--", color="gray", lw=1.2)
            corr_k = "f1_vs_bcs" if y_field == "f1" else "recall_vs_bcs"
            if ck in summary and corr_k in summary[ck]:
                rv = summary[ck][corr_k]["pearson_r"]
                pv = summary[ck][corr_k]["pearson_p"]
                ax.text(0.05, 0.05, f"r={rv:.3f}, p={pv:.3f}",
                        transform=ax.transAxes, fontsize=9, va="bottom")

        ax.set_xlabel("BCS")
        ax.set_ylabel(y_label)
        cn = ck.replace("count_", "")
        ax.set_title(f"BCS vs {y_label} (n={cn} types)")
        ax.grid(True, alpha=0.3)

        handles, labels = ax.get_legend_handles_labels()
        seen, uh, ul = {}, [], []
        for hh, ll in zip(handles, labels):
            if ll not in seen:
                seen[ll] = True
                uh.append(hh)
                ul.append(ll)
        if ul:
            ax.legend(uh, ul, loc="upper right")

        # Combined plot
        c = COUNT_COLORS.get(ck, "#999999")
        ax2.scatter(bcs, yv, c=c, s=40, alpha=0.7,
                    label=ck.replace("_", "="))
        if xl is not None:
            ax2.plot(xl, slope * xl + intercept, "--", color=c,
                     lw=1.0, alpha=0.6)

    plt.figure(fig.number)
    plt.tight_layout()
    fig.savefig(output_dir / f"{fname}.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(output_dir / f"{fname}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    ax2.set_xlabel("BCS")
    ax2.set_ylabel(y_label)
    ax2.set_title(f"BCS vs {y_label} (all counts)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.figure(fig2.number)
    plt.tight_layout()
    fig2.savefig(output_dir / f"{fname}_combined.pdf", dpi=300,
                 bbox_inches="tight")
    fig2.savefig(output_dir / f"{fname}_combined.png", dpi=300,
                 bbox_inches="tight")
    plt.close(fig2)
    logger.info("Saved %s figures", fname)


# ----------------------------------------------------------------------
# Confusion analysis
# ----------------------------------------------------------------------

def analyze_confusion(predictions_path: str, data_dir: str,
                      eval_results: dict, output_dir: Path,
                      top_k: int = 20):
    """Per-type confusion rate: which types get mislabeled as which?

    Loads raw predictions and ground truth. For each overlapping span
    with wrong type, counts (gold_type, pred_type) pairs.
    """
    sys.path.insert(0, str(Path(__file__).parent))
    from few_nerd_utils import load_few_nerd

    with open(predictions_path, "r") as f:
        predictions = json.load(f)
    samples = load_few_nerd(split="test", data_dir=data_dir)

    batches = {}
    for p in predictions:
        bid = p["batch_id"]
        batches.setdefault(bid, {"entries": [], "types": set(p["batch_types"])})
        batches[bid]["entries"].append(p)

    confusion = {}

    for bid, info in batches.items():
        btypes = info["types"]
        by_sid = {}
        for p in info["entries"]:
            by_sid.setdefault(p["sample_id"], []).append(p)

        for sid, preds in by_sid.items():
            if sid >= len(samples):
                continue
            golds = [e for e in samples[sid]["entities"]
                     if e["type"] in btypes]
            pred_ents = [p for p in preds[0].get("predictions", [])
                         if p.get("type") in btypes]

            for g in golds:
                for p in pred_ents:
                    if (p.get("type") != g["type"]
                            and p.get("start", -1) < g["end"]
                            and p.get("end", -1) > g["start"]):
                        pair = (g["type"], p["type"])
                        confusion[pair] = confusion.get(pair, 0) + 1

    top = sorted(confusion.items(), key=lambda x: -x[1])[:top_k]

    logger.info("Top-%d confused type pairs:", top_k)
    logger.info("  %-35s %-35s %s", "Gold Type", "Pred Type", "Count")
    for (gt, pt), cnt in top:
        logger.info("  %-35s %-35s %d", gt, pt, cnt)

    result = {
        "top_confused_pairs": [
            {"gold_type": g, "pred_type": p, "count": c}
            for (g, p), c in top
        ],
        "total_confusions": sum(confusion.values()),
        "n_unique_pairs": len(confusion),
    }

    with open(output_dir / "confusion_analysis.json", "w") as f:
        json.dump(result, f, indent=2)
    logger.info("Saved confusion analysis")

    return result


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Analyze experiment results and generate figures")
    parser.add_argument("--results_dir", required=True,
                        help="Directory with eval_exp1.json / eval_exp2.json")
    parser.add_argument("--output_dir", default=None,
                        help="Figure output directory (default: results_dir)")
    parser.add_argument("--eval_mode", default="relaxed",
                        choices=["exact", "relaxed", "text_match"],
                        help="Metric mode (default: relaxed)")
    parser.add_argument("--predictions_path", default=None,
                        help="Raw predictions JSON for confusion analysis")
    parser.add_argument("--data_dir",
                        default="./data/parquet",
                        help="Data directory for confusion analysis")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")

    results_dir = Path(args.results_dir)
    output_dir = Path(args.output_dir) if args.output_dir else results_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    full_summary = {}

    # -- Exp 1 --
    exp1_path = results_dir / "eval_exp1.json"
    solo_f1 = None
    if exp1_path.exists():
        logger.info("=== Exp 1: Count Baseline ===")
        exp1_results = load_eval(str(exp1_path))
        full_summary["exp1"] = analyze_exp1(
            exp1_results, output_dir, eval_mode=args.eval_mode)
        solo_f1 = {}
        for bid, metrics in exp1_results.items():
            if (metrics.get("count_key") == "count_1"
                    and "per_type_f1" in metrics):
                solo_f1.update(metrics["per_type_f1"])
        if not solo_f1:
            solo_f1 = None
            logger.warning("No per-type solo F1 in exp1 count=1")
        else:
            logger.info("Loaded solo F1 for %d types", len(solo_f1))
    else:
        logger.info("No exp1 results at %s", exp1_path)

    # -- Exp 2 --
    exp2_path = results_dir / "eval_exp2.json"
    if exp2_path.exists():
        logger.info("=== Exp 2: Confusability Controlled ===")
        exp2_results = load_eval(str(exp2_path))
        full_summary["exp2"] = analyze_exp2(
            exp2_results, output_dir, solo_f1=solo_f1,
            eval_mode=args.eval_mode)

        if args.predictions_path:
            logger.info("=== Confusion Analysis ===")
            full_summary["confusion"] = analyze_confusion(
                args.predictions_path, args.data_dir,
                exp2_results, output_dir)
    else:
        logger.info("No exp2 results at %s", exp2_path)

    # -- Dry run --
    dry_path = results_dir / "eval_dry_run.json"
    if dry_path.exists():
        logger.info("=== Dry Run ===")
        dry_results = load_eval(str(dry_path))
        full_summary["dry_run"] = analyze_exp2(
            dry_results, output_dir, solo_f1=solo_f1,
            eval_mode=args.eval_mode)

    # -- Save summary --
    summary_path = output_dir / "analysis_summary.json"
    with open(summary_path, "w") as f:
        json.dump(full_summary, f, indent=2,
                  default=lambda x: (None if isinstance(x, float)
                                     and np.isnan(x) else x))
    logger.info("Saved analysis summary to %s", summary_path)


if __name__ == "__main__":
    main()
