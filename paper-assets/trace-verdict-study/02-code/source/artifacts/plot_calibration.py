"""Generate reliability diagram and calibration summary from per-condition JSON files."""

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

CALIB_DIR = "/root/autodl-tmp/trace-verdict-study-checkpoints/calibration"
CONDITIONS = ["no_trace", "full_trace", "exception_only", "vota"]
DISPLAY_NAMES = {
    "no_trace": "No Trace",
    "full_trace": "Full Trace",
    "exception_only": "Exception Only",
    "vota": "VOTA",
}
COLORS = {
    "no_trace": "#E74C3C",
    "full_trace": "#3498DB",
    "exception_only": "#F39C12",
    "vota": "#2ECC71",
}
MARKERS = {
    "no_trace": "s",
    "full_trace": "D",
    "exception_only": "^",
    "vota": "o",
}


def load_results():
    results = {}
    for cond in CONDITIONS:
        path = os.path.join(CALIB_DIR, f"{cond}_calibration.json")
        if not os.path.exists(path):
            print(f"[WARN] Missing: {path}")
            continue
        with open(path) as f:
            results[cond] = json.load(f)
    return results


def plot_reliability_diagram(results, output_dir):
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 5))

    ax.plot([0.5, 1.0], [0.5, 1.0], "k--", linewidth=1, alpha=0.5, label="Perfect calibration")

    for cond in CONDITIONS:
        if cond not in results:
            continue
        data = results[cond]
        bins = data["reliability_diagram"]

        confs = []
        accs = []
        sizes = []
        for b in bins:
            if b["count"] > 0:
                confs.append(b["mean_confidence"])
                accs.append(b["accuracy"])
                sizes.append(b["count"])

        if not confs:
            continue

        ece = data["ece"]
        label = f"{DISPLAY_NAMES[cond]} (ECE={ece:.3f})"

        ax.plot(confs, accs, color=COLORS[cond], marker=MARKERS[cond],
                markersize=7, linewidth=1.8, label=label, zorder=3)

    ax.set_xlim(0.5, 1.0)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel("Mean Confidence", fontsize=13)
    ax.set_ylabel("Accuracy", fontsize=13)
    ax.set_title("Reliability Diagram", fontsize=14, fontweight="bold")
    ax.legend(fontsize=10, loc="lower right", framealpha=0.9)
    ax.tick_params(labelsize=11)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.1))
    ax.grid(True, alpha=0.3)
    ax.set_aspect("auto")

    fig.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, "reliability_diagram.pdf")
    png_path = os.path.join(output_dir, "reliability_diagram.png")
    fig.savefig(pdf_path, bbox_inches="tight", dpi=300)
    fig.savefig(png_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {pdf_path}")
    print(f"Saved: {png_path}")


def write_combined_metrics(results, output_dir):
    summary = {}
    for cond in CONDITIONS:
        if cond not in results:
            continue
        d = results[cond]
        summary[cond] = {
            "display_name": DISPLAY_NAMES[cond],
            "n_samples": d["n_samples"],
            "accuracy": d["accuracy"],
            "ece": d["ece"],
            "brier_score": d["brier_score"],
            "per_class": d["per_class"],
        }

    path = os.path.join(output_dir, "calibration_metrics.json")
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {path}")

    print("\n=== Calibration Summary ===")
    print(f"{'Condition':<18} {'Acc':>7} {'ECE':>8} {'Brier':>8}")
    print("-" * 45)
    for cond in CONDITIONS:
        if cond not in summary:
            continue
        s = summary[cond]
        print(f"{s['display_name']:<18} {s['accuracy']:>7.4f} {s['ece']:>8.4f} {s['brier_score']:>8.4f}")


def main():
    results = load_results()
    if not results:
        print("No calibration results found.")
        sys.exit(1)

    output_dir = CALIB_DIR
    plot_reliability_diagram(results, output_dir)
    write_combined_metrics(results, output_dir)


if __name__ == "__main__":
    main()
