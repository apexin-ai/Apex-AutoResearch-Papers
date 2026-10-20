#!/usr/bin/env python3
"""Actor entropy comparison plot for rebuttal (plan_031).
Reads from pre-computed analysis JSON."""

import json
import os

ANALYSIS_FILE = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir/analysis_actor_entropy_value_calibration.json"
OUT_DIR = "/root/autodl-tmp/event-gated-adaptive-horizon/artifacts/figures"

def main():
    with open(ANALYSIS_FILE) as f:
        data = json.load(f)

    experiments = data["experiments"]

    # Select representative experiments for the plot
    plot_configs = [
        ("exp_001_baseline", "Baseline (healthy)", "#2196F3", "-"),
        ("exp_008a", "Unexposed emb (healthy)", "#4CAF50", "--"),
        ("exp_008d", "Trained dt_emb s1 (collapsed)", "#F44336", "-"),
        ("exp_006", "Fixed dt=2 (collapsed)", "#FF9800", "-"),
        ("exp_008f", "No dt_emb (healthy)", "#9C27B0", "--"),
    ]

    # Check which experiments have actor_entropy_trajectory
    available = []
    for exp_id, label, color, ls in plot_configs:
        if exp_id in experiments and "actor_entropy_trajectory" in experiments[exp_id]:
            traj = experiments[exp_id]["actor_entropy_trajectory"]
            if len(traj) > 0:
                available.append((exp_id, label, color, ls, traj))
                print(f"  {exp_id}: {len(traj)} points, "
                      f"step range [{traj[0]['step']}, {traj[-1]['step']}]")

    if len(available) < 2:
        print("ERROR: Not enough experiments with actor_entropy data for comparison plot")
        return

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1, figsize=(8, 4))

    for exp_id, label, color, ls, traj in available:
        steps = [p["step"] / 1000 for p in traj]
        entropy = [p["actor_entropy"] for p in traj]
        ax.plot(steps, entropy, label=label, color=color, linestyle=ls, linewidth=1.5, alpha=0.85)

    ax.set_xlabel("Training Step (K)", fontsize=11)
    ax.set_ylabel("Actor Entropy", fontsize=11)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', linewidth=0.5, alpha=0.5)

    # Add annotation for entropy recovery
    ax.annotate("Entropy recovery\n(re-exploration)",
                xy=(130, -5.0), xytext=(200, -3.5),
                fontsize=7, color="#2196F3", alpha=0.8,
                arrowprops=dict(arrowstyle="->", color="#2196F3", alpha=0.5))

    plt.tight_layout()

    os.makedirs(OUT_DIR, exist_ok=True)
    pdf_path = os.path.join(OUT_DIR, "actor_entropy_comparison.pdf")
    png_path = os.path.join(OUT_DIR, "actor_entropy_comparison.png")
    plt.savefig(pdf_path, dpi=150, bbox_inches='tight')
    plt.savefig(png_path, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSaved: {pdf_path}")
    print(f"Saved: {png_path}")

    # Print summary
    analysis = data.get("analysis", {}).get("actor_entropy", {})
    if analysis:
        print(f"\nKey findings:")
        print(f"  {analysis.get('finding', '')}")
        print(f"  Healthy vs collapsed: {analysis.get('healthy_vs_collapsed', '')}")
        print(f"  Baseline recovery: {analysis.get('baseline_recovery', '')}")


if __name__ == "__main__":
    main()
