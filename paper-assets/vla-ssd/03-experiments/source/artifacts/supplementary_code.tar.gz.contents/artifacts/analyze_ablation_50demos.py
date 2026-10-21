"""4-condition ablation analysis: baseline / control8 / ablate_all24 / ablate_all32.

Inputs:
  - /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json
    (baseline, ablate_all24, ablate_all32)
  - /root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos_control8.json
    (ablate_control8)

Outputs:
  - Prints 4-condition × 3-layer summary table + bootstrap Δ CI + specificity check
  - /root/autodl-tmp/vla-ssd/results/figures/fig_ablation_4condition_bar.pdf
  - /root/autodl-tmp/vla-ssd/results/figures/fig_ablation_3layer_grouped.pdf
  - /root/autodl-tmp/vla-ssd/results/l1_head_ablation/ablation_50demos_combined.json

Dependencies: numpy, matplotlib (available in /root/miniconda3/bin/python3.12)
"""

import json
import os
import sys
import numpy as np

RESULTS_DIR = "/root/autodl-tmp/vla-ssd/results/l1_head_ablation"
FIGURES_DIR = "/root/autodl-tmp/vla-ssd/results/figures"
MAIN_FILE = os.path.join(RESULTS_DIR, "action_probe_50demos.json")
CONTROL_FILE = os.path.join(RESULTS_DIR, "action_probe_50demos_control8.json")
LAYERS = ["L1", "L8", "L13"]
CONDITIONS = ["baseline", "ablate_control8", "ablate_all24", "ablate_all32"]
DISPLAY_NAMES = {"baseline": "baseline", "ablate_control8": "control8",
                 "ablate_all24": "all24", "ablate_all32": "all32"}
COLORS = {"baseline": "#888888", "ablate_control8": "#6BAED6",
           "ablate_all24": "#E6550D", "ablate_all32": "#D62728"}
N_BOOTSTRAP = 10000
SEED = 42


def load_data():
    if not os.path.exists(MAIN_FILE):
        print("waiting for main experiment")
        sys.exit(0)
    with open(MAIN_FILE) as f:
        main_data = json.load(f)
    with open(CONTROL_FILE) as f:
        control_data = json.load(f)
    return main_data, control_data


def extract_per_task(data, condition, layer):
    """Extract per-task R² values as a numpy array."""
    detailed = data["detailed_results"][condition][layer]
    task_r2 = detailed["per_task_R2"]
    return np.array(list(task_r2.values()))


def extract_mean(data, condition, layer):
    return data["detailed_results"][condition][layer]["mean_R2"]


def bootstrap_diff_ci(vals_a, vals_b, n_boot=N_BOOTSTRAP, seed=SEED):
    """Bootstrap CI for mean(vals_a) - mean(vals_b), task-level resampling."""
    rng = np.random.default_rng(seed)
    n = len(vals_a)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        diffs[i] = vals_a[idx].mean() - vals_b[idx].mean()
    obs_diff = vals_a.mean() - vals_b.mean()
    ci_lo = np.percentile(diffs, 2.5)
    ci_hi = np.percentile(diffs, 97.5)
    p_value = np.mean(diffs >= 0) if obs_diff < 0 else np.mean(diffs <= 0)
    p_value = min(p_value * 2, 1.0)  # two-sided
    return obs_diff, ci_lo, ci_hi, p_value


def bootstrap_ci(vals, n_boot=N_BOOTSTRAP, seed=SEED):
    """Bootstrap CI for the mean of vals."""
    rng = np.random.default_rng(seed)
    n = len(vals)
    means = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        means[i] = vals[idx].mean()
    return np.percentile(means, 2.5), np.percentile(means, 97.5)


def make_bar_chart_l1(means, cis, save_path):
    """Single-layer (L1) 4-condition bar chart."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "serif", "font.size": 9,
                         "axes.linewidth": 0.8, "xtick.major.width": 0.6,
                         "ytick.major.width": 0.6})

    fig, ax = plt.subplots(figsize=(4.0, 3.2))
    x = np.arange(4)
    labels = ["Baseline", "Control-8", "All-24", "All-32"]
    colors = [COLORS["baseline"], COLORS["ablate_control8"],
              COLORS["ablate_all24"], COLORS["ablate_all32"]]
    bar_vals = [means["baseline"]["L1"], means["ablate_control8"]["L1"],
                means["ablate_all24"]["L1"], means["ablate_all32"]["L1"]]
    errs_lo = [bar_vals[i] - cis[c]["L1"][0]
               for i, c in enumerate(CONDITIONS)]
    errs_hi = [cis[c]["L1"][1] - bar_vals[i]
               for i, c in enumerate(CONDITIONS)]

    ax.bar(x, bar_vals, color=colors, width=0.6, edgecolor="black", linewidth=0.5,
           yerr=[errs_lo, errs_hi], capsize=4, error_kw={"linewidth": 0.8})
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Action Probe R² (Layer 1)")
    ax.set_ylim(0, max(bar_vals) * 1.15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    fig.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")


def make_grouped_bar_chart(means, cis, save_path):
    """3-layer × 4-condition grouped bar chart."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.family": "serif", "font.size": 9,
                         "axes.linewidth": 0.8, "xtick.major.width": 0.6,
                         "ytick.major.width": 0.6})

    fig, ax = plt.subplots(figsize=(6.0, 3.5))
    n_groups = 3
    n_bars = 4
    width = 0.18
    x = np.arange(n_groups)
    labels_cond = ["Baseline", "Control-8", "All-24", "All-32"]
    colors = [COLORS["baseline"], COLORS["ablate_control8"],
              COLORS["ablate_all24"], COLORS["ablate_all32"]]

    for i, cond in enumerate(CONDITIONS):
        vals = [means[cond][L] for L in LAYERS]
        lo = [means[cond][L] - cis[cond][L][0] for L in LAYERS]
        hi = [cis[cond][L][1] - means[cond][L] for L in LAYERS]
        offset = (i - 1.5) * width
        ax.bar(x + offset, vals, width=width, color=colors[i],
               edgecolor="black", linewidth=0.4, label=labels_cond[i],
               yerr=[lo, hi], capsize=3, error_kw={"linewidth": 0.6})

    ax.set_xticks(x)
    ax.set_xticklabels(["Layer 1", "Layer 8", "Layer 13"])
    ax.set_ylabel("Action Probe R²")
    ax.set_ylim(0, max(means[c][L] for c in CONDITIONS for L in LAYERS) * 1.12)
    ax.legend(frameon=False, fontsize=8, ncol=4, loc="upper left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    fig.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")


def main():
    main_data, control_data = load_data()

    # Merge into unified structure
    all_data = {
        "detailed_results": {
            **{k: main_data["detailed_results"][k] for k in ["baseline", "ablate_all24", "ablate_all32"]},
            "ablate_control8": control_data["detailed_results"]["ablate_control8"]
        }
    }

    # Extract means and per-task values
    means = {}
    task_vals = {}
    cis = {}
    for cond in CONDITIONS:
        means[cond] = {}
        task_vals[cond] = {}
        cis[cond] = {}
        for layer in LAYERS:
            means[cond][layer] = extract_mean(all_data, cond, layer)
            task_vals[cond][layer] = extract_per_task(all_data, cond, layer)
            cis[cond][layer] = bootstrap_ci(task_vals[cond][layer])

    # Print summary table
    print("\n=== 50-demo Ablation Results (4 conditions × 3 layers) ===\n")
    print(f"{'Layer':<6} | {'baseline':<10} | {'control8':<10} | {'all24':<10} | {'all32':<10}")
    print("-" * 60)
    for layer in LAYERS:
        print(f"{layer:<6} | {means['baseline'][layer]:<10.4f} | "
              f"{means['ablate_control8'][layer]:<10.4f} | "
              f"{means['ablate_all24'][layer]:<10.4f} | "
              f"{means['ablate_all32'][layer]:<10.4f}")

    # Bootstrap Δ vs baseline
    print("\n=== Bootstrap Δ vs baseline (95% CI) ===")
    diff_results = {}
    for cond in ["ablate_all24", "ablate_all32", "ablate_control8"]:
        diff_results[cond] = {}
        for layer in LAYERS:
            d, lo, hi, p = bootstrap_diff_ci(
                task_vals[cond][layer], task_vals["baseline"][layer])
            diff_results[cond][layer] = {"delta": d, "ci_lo": lo, "ci_hi": hi, "p": p}
            name = DISPLAY_NAMES[cond]
            print(f"{name} {layer}:  Δ={d:+.4f} [{lo:.4f}, {hi:.4f}] p={p:.4f}")

    # Specificity check: all24 vs control8
    print("\n=== Specificity Check ===")
    spec_results = {}
    for layer in LAYERS:
        d, lo, hi, p = bootstrap_diff_ci(
            task_vals["ablate_all24"][layer], task_vals["ablate_control8"][layer])
        spec_results[layer] = {"delta": d, "ci_lo": lo, "ci_hi": hi, "p": p}
        print(f"all24 vs control8 {layer}: Δ={d:+.4f} [{lo:.4f}, {hi:.4f}] p={p:.4f}")

    # Generate figures
    make_bar_chart_l1(means, cis,
                      os.path.join(FIGURES_DIR, "fig_ablation_4condition_bar.pdf"))
    make_grouped_bar_chart(means, cis,
                           os.path.join(FIGURES_DIR, "fig_ablation_3layer_grouped.pdf"))

    # Save combined JSON
    output = {
        "means": {c: {L: float(means[c][L]) for L in LAYERS} for c in CONDITIONS},
        "bootstrap_ci": {c: {L: {"ci_lo": float(cis[c][L][0]),
                                  "ci_hi": float(cis[c][L][1])}
                             for L in LAYERS} for c in CONDITIONS},
        "diff_vs_baseline": {c: {L: {k: float(v) for k, v in diff_results[c][L].items()}
                                 for L in LAYERS}
                             for c in ["ablate_all24", "ablate_all32", "ablate_control8"]},
        "specificity_all24_vs_control8": {L: {k: float(v) for k, v in spec_results[L].items()}
                                          for L in LAYERS},
        "metadata": {
            "n_bootstrap": N_BOOTSTRAP,
            "seed": SEED,
            "conditions": CONDITIONS,
            "layers": LAYERS,
            "source_files": [MAIN_FILE, CONTROL_FILE]
        }
    }
    out_path = os.path.join(RESULTS_DIR, "ablation_50demos_combined.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
