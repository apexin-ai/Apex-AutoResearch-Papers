#!/usr/bin/env python3
"""D141 Task 3: Degeneracy-Capability Scatter Plot
Visualizes model capability (greedy F1) vs degeneracy rate across experiments.
"""

import json
import numpy as np
import os

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = os.path.join(BASE, "output/d141_degeneracy_scatter")
os.makedirs(OUT_DIR, exist_ok=True)

DATA_SOURCES = [
    {"label": "Qwen3-8B\nSciERC 3ep", "model": "Qwen3-8B", "dataset": "SciERC",
     "samples_path": "output/exp_029a_scierc_3epoch/samples.jsonl"},
    {"label": "Qwen3-8B\nSciERC 5ep", "model": "Qwen3-8B", "dataset": "SciERC",
     "samples_path": "output/exp_012_rerun_1024/samples.jsonl"},
    {"label": "Qwen3-8B\nSciERC 10ep", "model": "Qwen3-8B", "dataset": "SciERC",
     "samples_path": "output/exp_029b_scierc_10epoch/samples.jsonl"},
    {"label": "Qwen3-8B\nCoNLL", "model": "Qwen3-8B", "dataset": "CoNLL",
     "samples_path": "output/exp_002_conll_n16_r1024/samples.jsonl"},
    {"label": "Qwen3-8B\nFewNERD", "model": "Qwen3-8B", "dataset": "FewNERD",
     "samples_path": "output/exp_027_fewnerd_n16/samples.jsonl"},
    {"label": "Qwen3-4B\nSciERC", "model": "Qwen3-4B", "dataset": "SciERC",
     "samples_path": "output/exp_qwen3_4b_scierc_scs_inference/samples.jsonl"},
    {"label": "Qwen3-4B\nCoNLL", "model": "Qwen3-4B", "dataset": "CoNLL",
     "samples_path": "output/exp_qwen3_4b_conll_scs_inference_v2/samples.jsonl"},
    {"label": "LLaMA-3B\nSciERC", "model": "LLaMA-3B", "dataset": "SciERC",
     "samples_path": "output/exp_018_llama_scierc_seed42_r1024/samples.jsonl"},
    {"label": "LLaMA-3B\nCoNLL", "model": "LLaMA-3B", "dataset": "CoNLL",
     "samples_path": "output/exp_017_llama_conll_n16_r1024/samples.jsonl"},
    {"label": "Qwen3-8B\nFewNERD 5ep", "model": "Qwen3-8B", "dataset": "FewNERD",
     "samples_path": "output/exp_028_fewnerd_5epoch/samples.jsonl"},
]


def entity_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    if tp == 0:
        return 0.0
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    return 2 * p * r / (p + r)


def compute_from_samples(samples_path):
    greedy_f1s = []
    n_degenerate = 0
    n_total = 0

    full_path = os.path.join(BASE, samples_path)
    with open(full_path) as f:
        for line in f:
            inst = json.loads(line)
            gold_ents = inst["gold"].get("entities", [])
            if len(gold_ents) == 0:
                continue

            n_total += 1
            greedy = inst.get("greedy")
            samples = inst["samples"]

            gf1 = entity_f1(greedy.get("entities", []), gold_ents) if greedy else 0.0
            greedy_f1s.append(gf1)

            sample_f1s = [entity_f1(s.get("entities", []), gold_ents) for s in samples]
            unique_f1s = set(round(f, 8) for f in sample_f1s)
            if len(unique_f1s) <= 1:
                n_degenerate += 1

    greedy_macro = float(np.mean(greedy_f1s)) if greedy_f1s else 0.0
    degen_rate = (n_degenerate / n_total * 100) if n_total > 0 else 0.0

    return greedy_macro, degen_rate, n_total


def main():
    data_points = []

    for ds in DATA_SOURCES:
        sp = ds["samples_path"]
        full_path = os.path.join(BASE, sp)
        if not os.path.exists(full_path):
            print(f"WARNING: {full_path} not found, skipping {ds['label']}")
            continue

        print(f"Computing: {ds['label'].replace(chr(10), ' ')} ({sp})...")
        gf1, drate, n = compute_from_samples(sp)
        print(f"  greedy_f1={gf1:.4f}, degeneracy={drate:.2f}%, n={n}")

        data_points.append({
            "label": ds["label"],
            "label_short": ds["label"].replace("\n", " "),
            "model": ds["model"],
            "dataset": ds["dataset"],
            "greedy_f1": round(gf1, 4),
            "degeneracy_pct": round(drate, 4),
            "n_instances": n,
        })

    with open(os.path.join(OUT_DIR, "data_points.json"), "w") as f:
        json.dump(data_points, f, indent=2)

    from scipy.stats import spearmanr
    x = [dp["greedy_f1"] for dp in data_points]
    y = [dp["degeneracy_pct"] for dp in data_points]
    rho, p_val = spearmanr(x, y)

    print(f"\nSpearman rho={rho:.4f}, p={p_val:.4f}")
    print(f"N data points: {len(data_points)}")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 6))

    dataset_colors = {"SciERC": "#2196F3", "CoNLL": "#4CAF50", "FewNERD": "#FF9800"}
    model_markers = {"Qwen3-8B": "o", "Qwen3-4B": "s", "LLaMA-3B": "^"}

    for dp in data_points:
        color = dataset_colors.get(dp["dataset"], "gray")
        marker = model_markers.get(dp["model"], "o")
        ax.scatter(dp["greedy_f1"], dp["degeneracy_pct"],
                   c=color, marker=marker, s=120, zorder=5,
                   edgecolors="black", linewidths=0.5)

        offset_x, offset_y = 8, 4
        if dp["degeneracy_pct"] > 80:
            offset_y = -12
        if dp["greedy_f1"] > 0.9:
            offset_x = -8
            ha = "right"
        else:
            ha = "left"

        ax.annotate(dp["label_short"], (dp["greedy_f1"], dp["degeneracy_pct"]),
                    textcoords="offset points", xytext=(offset_x, offset_y),
                    fontsize=7.5, ha=ha, va="bottom")

    if len(x) >= 3:
        z = np.polyfit(x, y, 1)
        xline = np.linspace(min(x) - 0.02, max(x) + 0.02, 100)
        yline = np.polyval(z, xline)
        ax.plot(xline, yline, "--", color="gray", alpha=0.5, linewidth=1)

    ax.set_xlabel("Greedy F1 (macro)", fontsize=12)
    ax.set_ylabel("Degeneracy Rate (%)", fontsize=12)
    ax.set_title(f"Capability vs Degeneracy (Spearman $\\rho$={rho:.3f}, p={p_val:.3f})", fontsize=13)

    from matplotlib.lines import Line2D
    dataset_handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                              markersize=8, label=d, markeredgecolor="black", markeredgewidth=0.5)
                       for d, c in dataset_colors.items()]
    model_handles = [Line2D([0], [0], marker=m, color="w", markerfacecolor="gray",
                            markersize=8, label=mod, markeredgecolor="black", markeredgewidth=0.5)
                     for mod, m in model_markers.items()]
    ax.legend(handles=dataset_handles + model_handles, loc="upper left",
              fontsize=9, framealpha=0.8)

    ax.tick_params(labelsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "scatter_plot.png"), dpi=300, bbox_inches="tight")
    print(f"Scatter plot saved to {OUT_DIR}/scatter_plot.png")

    lines = ["# D141 Task 3: Degeneracy-Capability Scatter Plot\n\n"]
    lines.append("## Data Points\n\n")
    lines.append("| Label | Model | Dataset | Greedy F1 | Degeneracy (%) | N |\n")
    lines.append("|-------|-------|---------|-----------|----------------|---|\n")
    for dp in sorted(data_points, key=lambda d: d["greedy_f1"]):
        lines.append(f"| {dp['label_short']} | {dp['model']} | {dp['dataset']} | {dp['greedy_f1']:.4f} | {dp['degeneracy_pct']:.2f} | {dp['n_instances']} |\n")

    lines.append(f"\n## Correlation\n\n")
    lines.append(f"- Spearman rho = {rho:.4f}\n")
    lines.append(f"- p-value = {p_val:.4f}\n")
    lines.append(f"- N = {len(data_points)} data points\n\n")

    if rho > 0.3 and p_val < 0.05:
        verdict = "Positive correlation supports the 'capability trap' hypothesis: higher-performing models (on a given dataset) tend to have higher degeneracy rates, reducing the headroom for LP selection to improve over greedy."
    elif rho > 0 and p_val < 0.05:
        verdict = "Weak positive correlation. Some evidence for capability trap but not conclusive."
    elif p_val >= 0.05:
        verdict = "No statistically significant correlation between capability and degeneracy."
    else:
        verdict = "Unexpected negative correlation. Does not support capability trap hypothesis."

    lines.append(f"## Conclusion\n\n{verdict}\n")

    with open(os.path.join(OUT_DIR, "report.md"), "w") as f:
        f.writelines(lines)

    print(f"Report saved to {OUT_DIR}/report.md")

    for dp in sorted(data_points, key=lambda d: d["greedy_f1"]):
        print(f"  {dp['label_short']:30s} F1={dp['greedy_f1']:.4f}  degen={dp['degeneracy_pct']:6.2f}%")


if __name__ == "__main__":
    main()
