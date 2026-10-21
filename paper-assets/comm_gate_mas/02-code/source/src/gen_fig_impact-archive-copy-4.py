"""
Generate fig_impact.pdf: violin + box + strip plot of remove-ablation
semantic similarity by function type.

Input: Qwen2.5-7B round-robin GSM8K impact + annotation data
Output: artifacts/paper/figures/fig_impact.pdf
"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "artifacts" / "paper" / "figures"))
import paper_style

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
from scipy import stats

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMPACT_PATH = os.path.join(BASE, "outputs/full_scale/qwen_round_robin/local_impact/impact.jsonl")
ANN_PATH = os.path.join(BASE, "outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl")
OUT_PATH = os.path.join(BASE, "artifacts/paper/figures/fig_impact.pdf")

LABEL_MAP = {
    "acknowledgment": "ACK",
    "information_provision": "INFO",
    "verification": "VERIF",
    "reasoning_guidance": "REASON",
}

OI_COLORS = {
    "acknowledgment":       paper_style.FUNC_COLORS['ACK'],
    "information_provision": paper_style.FUNC_COLORS['INFO'],
    "verification":          paper_style.FUNC_COLORS['VERIF'],
    "reasoning_guidance":    paper_style.FUNC_COLORS['REASON'],
}

KEEP_TYPES = list(LABEL_MAP.keys())


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def add_significance_bracket(ax, x1, x2, y, p, h=0.018):
    ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], color='#444444', linewidth=0.9)
    if p < 0.001:
        label = '***'
    elif p < 0.01:
        label = '**'
    elif p < 0.05:
        label = '*'
    else:
        label = 'ns'
    ax.text((x1+x2)/2, y+h+0.006, label, ha='center', va='bottom',
            fontsize=7.5, color='#444444')


def main():
    impact = pd.DataFrame(load_jsonl(IMPACT_PATH))
    annotations = pd.DataFrame(load_jsonl(ANN_PATH))

    impact["remove_semantic_similarity"] = impact["remove"].apply(lambda x: x["semantic_similarity"])
    annotations["ann_type"] = annotations["annotation_a"].apply(lambda x: x["type"])

    df = impact.merge(
        annotations[["task_id", "message_index", "ann_type"]],
        on=["task_id", "message_index"],
        how="inner",
    )
    df = df[df["message_index"] != 0].reset_index(drop=True)
    df = df[df["ann_type"].isin(KEEP_TYPES)].reset_index(drop=True)

    order = df.groupby("ann_type")["remove_semantic_similarity"].median().sort_values().index.tolist()
    counts = df.groupby("ann_type").size()

    paper_style.apply_style()

    fig, ax = plt.subplots(figsize=(paper_style.TEXTWIDTH, 4.0))

    palette = [OI_COLORS[t] for t in order]
    bp_data = [df[df["ann_type"] == t]["remove_semantic_similarity"].values for t in order]
    positions = list(range(len(order)))

    # Layer 1: Violin (distribution shape)
    vp = ax.violinplot(bp_data, positions=positions, showextrema=False, widths=0.55)
    for i, body in enumerate(vp['bodies']):
        # Clip violin to data range (no KDE extrapolation beyond min/max)
        vertices = body.get_paths()[0].vertices
        data_min, data_max = bp_data[i].min(), bp_data[i].max()
        vertices[:, 1] = np.clip(vertices[:, 1], data_min, data_max)
        body.set_facecolor(palette[i])
        body.set_alpha(0.15)
        body.set_edgecolor(palette[i])
        body.set_linewidth(0.5)

    # Layer 2: Jittered strip (raw data)
    np.random.seed(42)
    for i, (data, color) in enumerate(zip(bp_data, palette)):
        jitter = np.random.normal(0, 0.05, len(data))
        ax.scatter(positions[i] + jitter, data, color=color, alpha=0.2,
                   s=3, zorder=2, edgecolors='none', rasterized=False)

    # Layer 3: Boxplot (quartiles)
    bp = ax.boxplot(
        bp_data,
        positions=positions,
        widths=0.22,
        patch_artist=True,
        showfliers=False,
        medianprops=dict(color='#222222', linewidth=2.0),
        whiskerprops=dict(linewidth=1.3, color='#555555'),
        capprops=dict(linewidth=1.3, color='#555555'),
    )
    for patch, color in zip(bp['boxes'], palette):
        patch.set_facecolor(color)
        patch.set_alpha(0.78)
        patch.set_edgecolor(color)
        patch.set_linewidth(1.3)

    # Layer 4: Median value annotations
    for i, data in enumerate(bp_data):
        median_val = np.median(data)
        ax.text(positions[i] + 0.20, median_val + 0.01, f'{median_val:.2f}',
                fontsize=7.5, color='#333333', va='bottom', ha='left',
                fontweight='bold')

    # X labels
    short_labels = [LABEL_MAP[t] for t in order]
    ax.set_xticks(positions)
    ax.set_xticklabels(short_labels, fontweight='medium')

    # Sample size annotations
    for i, t in enumerate(order):
        ax.text(i, -0.09, f"n={counts[t]}",
                ha="center", va="top", fontsize=8.5, color="#666666",
                transform=ax.get_xaxis_transform())

    ax.set_xlabel("")
    ax.set_ylabel("Remove-Ablation Similarity")
    ax.set_ylim(-0.02, 1.28)
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.2))
    ax.grid(True, axis='y', alpha=0.08, zorder=0)

    # Significance brackets: ACK vs each other type (Mann-Whitney U)
    ack_data = df[df["ann_type"] == "acknowledgment"]["remove_semantic_similarity"].values
    ack_idx = order.index("acknowledgment")

    bracket_targets = ["information_provision", "verification", "reasoning_guidance"]
    y_starts = [1.03, 1.09, 1.16]
    for target, y_start in zip(bracket_targets, y_starts):
        x2 = order.index(target)
        other_data = bp_data[x2]
        _, p = stats.mannwhitneyu(ack_data, other_data, alternative='two-sided')
        add_significance_bracket(ax, ack_idx, x2, y_start, p)

    # "Higher impact" arrow
    ax.annotate("Higher impact", xy=(0.02, -0.17), xycoords="axes fraction",
                fontsize=9, fontstyle="italic", color="#888888", ha="left", va="top")
    ax.annotate("", xy=(-0.02, -0.15), xytext=(0.20, -0.15),
                xycoords="axes fraction",
                arrowprops=dict(arrowstyle="->", color="#888888", lw=1.0))

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    fig.savefig(OUT_PATH, bbox_inches="tight", dpi=300)
    fig.savefig(OUT_PATH.replace(".pdf", ".png"), bbox_inches="tight", dpi=300)
    plt.close(fig)

    print(f"Saved: {OUT_PATH}")
    print(f"\nTotal n={len(df)}")
    for t in order:
        g = df[df["ann_type"] == t]["remove_semantic_similarity"]
        print(f"  {LABEL_MAP[t]:8s} ({t:25s}): n={len(g):4d}, mean={g.mean():.3f}, median={g.median():.3f}")


if __name__ == "__main__":
    main()
