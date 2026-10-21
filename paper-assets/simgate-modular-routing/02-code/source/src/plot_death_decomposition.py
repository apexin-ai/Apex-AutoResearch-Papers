"""Generate publication-quality figures from death decomposition analysis."""

import argparse
import json
import os
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

GENUINE_DET_THRESHOLD = 95.0  # death_avoidance_pct below this = genuine det signal


def shorten_task(name: str, max_len: int = 18) -> str:
    name = name.replace("measure-melting-point-", "melt-pt-")
    name = name.replace("chemistry-mix-paint-", "chem-")
    name = name.replace("change-the-state-of-matter-of", "state-change")
    name = name.replace("inclined-plane-friction-", "incl-fric-")
    name = name.replace("inclined-plane-determine-angle", "incl-angle")
    name = name.replace("power-component-renewable-vs-nonrenewable-energy", "power-renew")
    name = name.replace("power-component", "power-comp")
    name = name.replace("test-conductivity-of-unknown-substances", "cond-unknown")
    name = name.replace("test-conductivity", "cond-test")
    name = name.replace("mendelian-genetics-", "mendel-")
    name = name.replace("lifespan-longest-lived-then-shortest-lived", "lifespan-long-short")
    name = name.replace("lifespan-longest-lived", "lifespan-long")
    name = name.replace("lifespan-shortest-lived", "lifespan-short")
    name = name.replace("identify-life-stages-", "life-stage-")
    name = name.replace("find-non-living-thing", "find-nonliving")
    name = name.replace("find-living-thing", "find-living")
    name = name.replace("use-thermometer", "thermometer")
    name = name.replace("grow-fruit", "grow-fruit")
    name = name.replace("grow-plant", "grow-plant")
    name = name.replace("find-animal", "find-animal")
    name = name.replace("find-plant", "find-plant")
    if len(name) > max_len:
        name = name[:max_len - 1] + "…"
    return name


def load_data(report_path: str) -> dict:
    with open(report_path) as f:
        return json.load(f)


def plot_scatter(report: dict, output_dir: str):
    tasks = report["per_task"]

    death_rate_diffs = []
    deltas = []
    labels = []
    is_genuine = []
    is_outlier = []

    for t in tasks:
        drd = t["int_death_rate"] - t["det_death_rate"]
        death_rate_diffs.append(drd * 100)
        deltas.append(t["delta_full"])
        labels.append(t["task"])
        daf = t["death_avoidance_fraction"]
        genuine = daf is not None and (daf * 100) < GENUINE_DET_THRESHOLD
        is_genuine.append(genuine)
        is_outlier.append(t["task"] == "measure-melting-point-unknown-substance")

    x = np.array(death_rate_diffs)
    y = np.array(deltas)
    genuine_mask = np.array(is_genuine)
    outlier_mask = np.array(is_outlier)
    normal_mask = ~genuine_mask & ~outlier_mask

    fig, ax = plt.subplots(figsize=(6.5, 5))

    ax.scatter(x[normal_mask], y[normal_mask], c="#2166ac", s=40, zorder=3,
               edgecolors="white", linewidths=0.5, label="Death-dominated")
    if genuine_mask.any():
        ax.scatter(x[genuine_mask & ~outlier_mask], y[genuine_mask & ~outlier_mask],
                   c="#b2182b", marker="D", s=50, zorder=4,
                   edgecolors="white", linewidths=0.5, label="Genuine det signal")
    if outlier_mask.any():
        ax.scatter(x[outlier_mask], y[outlier_mask],
                   c="#b2182b", marker="D", s=70, zorder=5,
                   edgecolors="black", linewidths=1.2)

    # Regression line
    slope, intercept = np.polyfit(x, y, 1)
    x_line = np.linspace(x.min() - 2, x.max() + 2, 100)
    ax.plot(x_line, slope * x_line + intercept, color="#666666",
            linewidth=1.2, linestyle="--", zorder=2)

    # Correlation annotation
    corr = report["aggregate"]["correlation_death_rate_diff_vs_delta"]
    r_val = corr["pearson_r"]
    p_val = corr["p_value"]
    p_str = f"p < 0.001" if p_val < 0.001 else f"p = {p_val:.3f}"
    ax.text(0.05, 0.95, f"r = {r_val:.3f}, {p_str}\nn = {corr['n_tasks']} tasks",
            transform=ax.transAxes, fontsize=9, verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#cccccc", alpha=0.9))

    # Annotate outlier
    for i, (xi, yi) in enumerate(zip(x, y)):
        if is_outlier[i]:
            ax.annotate(shorten_task(labels[i]),
                        (xi, yi), textcoords="offset points",
                        xytext=(8, -12), fontsize=7.5, color="#b2182b",
                        fontstyle="italic",
                        arrowprops=dict(arrowstyle="-", color="#b2182b",
                                        linewidth=0.6))
        elif is_genuine[i]:
            ax.annotate(shorten_task(labels[i]),
                        (xi, yi), textcoords="offset points",
                        xytext=(8, 5), fontsize=7, color="#b2182b", alpha=0.8)

    ax.set_xlabel("Death rate difference (Internal − Deterministic, %pts)", fontsize=10)
    ax.set_ylabel("Δ score (Deterministic − Internal)", fontsize=10)
    ax.axhline(0, color="#cccccc", linewidth=0.5, zorder=1)
    ax.axvline(0, color="#cccccc", linewidth=0.5, zorder=1)
    ax.legend(fontsize=8.5, loc="lower right", framealpha=0.9)
    ax.tick_params(labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig1_death_scatter.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[Fig 1] Scatter plot saved to {output_dir}/fig1_death_scatter.{{pdf,png}}")


def plot_label_distribution(report: dict, output_dir: str):
    tasks = report["per_task"]
    task_names = [shorten_task(t["task"]) for t in tasks]
    det_pref = [t["label_distribution"]["det-preferred"] for t in tasks]
    int_pref = [t["label_distribution"]["internal-preferred"] for t in tasks]
    no_pref = [t["label_distribution"]["no-preference"] for t in tasks]

    # Sort by det-preferred fraction descending
    n_eps = [t["n_episodes"] for t in tasks]
    det_frac = [d / n if n > 0 else 0 for d, n in zip(det_pref, n_eps)]
    order = np.argsort(det_frac)[::-1]

    task_names = [task_names[i] for i in order]
    det_pref = [det_pref[i] for i in order]
    int_pref = [int_pref[i] for i in order]
    no_pref = [no_pref[i] for i in order]
    n_eps = [n_eps[i] for i in order]

    # Normalize to fractions
    det_frac_sorted = [d / n for d, n in zip(det_pref, n_eps)]
    int_frac_sorted = [ip / n for ip, n in zip(int_pref, n_eps)]
    no_frac_sorted = [np_ / n for np_, n in zip(no_pref, n_eps)]

    fig, ax = plt.subplots(figsize=(7, 6.5))
    y_pos = np.arange(len(task_names))

    ax.barh(y_pos, det_frac_sorted, color="#2166ac", label="Det-preferred", height=0.7)
    left = np.array(det_frac_sorted)
    ax.barh(y_pos, int_frac_sorted, left=left, color="#b2182b",
            label="Internal-preferred", height=0.7)
    left2 = left + np.array(int_frac_sorted)
    ax.barh(y_pos, no_frac_sorted, left=left2, color="#d9d9d9",
            label="No preference", height=0.7)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(task_names, fontsize=7.5)
    ax.set_xlabel("Episode fraction", fontsize=10)
    ax.set_xlim(0, 1.0)
    ax.invert_yaxis()
    ax.legend(fontsize=8, loc="lower right", framealpha=0.9)
    ax.tick_params(labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Aggregate bar at bottom
    agg = report["aggregate"]
    total = agg["n_episodes"]
    agg_ld = agg["label_distribution"]

    fig.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig2_label_distribution.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[Fig 2] Label distribution saved to {output_dir}/fig2_label_distribution.{{pdf,png}}")


def plot_death_avoidance_bar(report: dict, output_dir: str):
    """Bar chart of death_avoidance_fraction per task, highlighting outliers."""
    tasks = [t for t in report["per_task"]
             if t["death_avoidance_fraction"] is not None]
    tasks_sorted = sorted(tasks, key=lambda t: t["death_avoidance_fraction"])

    names = [shorten_task(t["task"]) for t in tasks_sorted]
    fracs = [t["death_avoidance_fraction"] * 100 for t in tasks_sorted]
    colors = ["#b2182b" if f < GENUINE_DET_THRESHOLD else "#2166ac" for f in fracs]

    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    y_pos = np.arange(len(names))
    ax.barh(y_pos, fracs, color=colors, height=0.7, edgecolor="white", linewidth=0.3)

    ax.axvline(GENUINE_DET_THRESHOLD, color="#999999", linewidth=0.8,
               linestyle=":", zorder=1)
    ax.text(GENUINE_DET_THRESHOLD - 1, len(names) - 0.5,
            f"{GENUINE_DET_THRESHOLD:.0f}%", fontsize=7.5, color="#999999",
            ha="right", va="bottom")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=7.5)
    ax.set_xlabel("Death avoidance fraction (%)", fontsize=10)
    ax.set_xlim(0, 105)
    ax.tick_params(labelsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    legend_elements = [
        Line2D([0], [0], color="#2166ac", lw=8, label="Death-dominated (≥95%)"),
        Line2D([0], [0], color="#b2182b", lw=8, label="Genuine det signal (<95%)"),
    ]
    ax.legend(handles=legend_elements, fontsize=8, loc="lower right", framealpha=0.9)

    fig.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig3_death_avoidance.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[Fig 3] Death avoidance bar saved to {output_dir}/fig3_death_avoidance.{{pdf,png}}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True,
                        help="Path to death_decomposition_report.json")
    parser.add_argument("--output_dir", required=True,
                        help="Directory to save figures")
    args = parser.parse_args()

    report = load_data(args.report)
    os.makedirs(args.output_dir, exist_ok=True)

    plot_scatter(report, args.output_dir)
    plot_label_distribution(report, args.output_dir)
    plot_death_avoidance_bar(report, args.output_dir)


if __name__ == "__main__":
    main()
