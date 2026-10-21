#!/usr/bin/env python3
"""Plot scaling curves: degeneracy, headroom, LP delta, construction delta vs model size."""

import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Data ──────────────────────────────────────────────────────────────
# Each entry: (model, family, size_b, dataset, regime,
#              greedy_f1, oracle_f1, headroom_pp, degen_pct, lp_delta_pp, constr_delta_pp)

DATA = [
    # Fine-tuned, FewNERD
    {"model": "Qwen3-8B",     "family": "Qwen3",  "size": 8,  "dataset": "FewNERD", "regime": "ft",
     "greedy": 0.7481, "oracle": 0.8739, "headroom": 12.58, "degen": 12.69, "lp_delta": 1.38, "constr_delta": None},
    {"model": "LLaMA-3.1-8B", "family": "LLaMA",  "size": 8,  "dataset": "FewNERD", "regime": "ft",
     "greedy": 0.7842, "oracle": 0.8843, "headroom": 10.01, "degen": 23.36, "lp_delta": 0.36, "constr_delta": None},

    # Fine-tuned, SciERC
    {"model": "Qwen3-4B",     "family": "Qwen3",  "size": 4,  "dataset": "SciERC",  "regime": "ft",
     "greedy": 0.6622, "oracle": 0.7925, "headroom": 13.03, "degen": 10.4,  "lp_delta": None, "constr_delta": None},

    # Zero-shot
    {"model": "Qwen2.5-72B",  "family": "Qwen2.5","size": 72, "dataset": "SciERC",  "regime": "zs",
     "greedy": 0.399,  "oracle": 0.549,  "headroom": 15.0,  "degen": None,  "lp_delta": None, "constr_delta": None},

    # === PLACEHOLDER: uncomment and fill as experiments complete ===
    # {"model": "Qwen2.5-7B",  "family": "Qwen2.5","size": 7,  "dataset": "FewNERD", "regime": "ft",
    #  "greedy": None, "oracle": None, "headroom": None, "degen": None, "lp_delta": None, "constr_delta": None},
    # {"model": "Qwen2.5-14B", "family": "Qwen2.5","size": 14, "dataset": "FewNERD", "regime": "ft",
    #  "greedy": None, "oracle": None, "headroom": None, "degen": None, "lp_delta": None, "constr_delta": None},
    # {"model": "Qwen2.5-32B", "family": "Qwen2.5","size": 32, "dataset": "FewNERD", "regime": "ft",
    #  "greedy": None, "oracle": None, "headroom": None, "degen": None, "lp_delta": None, "constr_delta": None},
]


def load_data_from_json(path: str) -> list[dict]:
    with open(path) as f:
        raw = json.load(f)
    out = []
    for r in raw:
        regime_raw = r.get("regime", "ft")
        if regime_raw.startswith("fine"):
            regime = "ft"
        elif regime_raw.startswith("zero"):
            regime = "zs"
        else:
            regime = regime_raw
        out.append({
            "model":  r.get("model", ""),
            "family": r.get("family", ""),
            "size":   r.get("size_b") or r.get("size", 0),
            "dataset": r.get("dataset", ""),
            "regime": regime,
            "greedy": r.get("greedy_f1") or r.get("greedy"),
            "oracle": r.get("oracle_f1") or r.get("oracle"),
            "headroom": r.get("headroom_pp") or r.get("headroom"),
            "degen":  r.get("degen_pct") or r.get("degen"),
            "lp_delta": r.get("lp_delta_pp") or r.get("lp_delta"),
            "constr_delta": r.get("constr_delta_pp") or r.get("constr_delta"),
        })
    return out


# ── Style ─────────────────────────────────────────────────────────────

FAMILY_STYLE = {
    "Qwen2.5": {"color": "#2166ac", "linestyle": "-",  "linewidth": 1.6},
    "Qwen3":   {"color": "#4393c3", "linestyle": "-",  "linewidth": 1.6},
    "LLaMA":   {"color": "#b2182b", "linestyle": "--", "linewidth": 1.4},
}

REGIME_MARKER = {
    "ft": {"marker": "o", "markersize": 6},
    "zs": {"marker": "^", "markersize": 7},
}

DEFAULT_FAMILY = {"color": "#666666", "linestyle": "-.", "linewidth": 1.2}
DEFAULT_REGIME = {"marker": "s", "markersize": 5}


def get_style(d: dict) -> dict:
    fam = FAMILY_STYLE.get(d["family"], DEFAULT_FAMILY)
    reg = REGIME_MARKER.get(d["regime"], DEFAULT_REGIME)
    return {**fam, **reg}


def plot_panel(ax, data: list[dict], metric_key: str, ylabel: str, fmt_func=None):
    """Plot one metric panel. Only includes points where metric is not None."""
    points = [(d, d[metric_key]) for d in data if d.get(metric_key) is not None]
    if not points:
        ax.text(0.5, 0.5, "No data", transform=ax.transAxes, ha="center", va="center",
                fontsize=8, color="#999999")
        ax.set_ylabel(ylabel, fontsize=8)
        return

    plotted_labels = set()
    for d, val in points:
        style = get_style(d)
        label_key = f"{d['family']} ({d['regime'].upper()})"
        label = label_key if label_key not in plotted_labels else None
        if label:
            plotted_labels.add(label_key)

        ax.plot(d["size"], val,
                color=style["color"], marker=style["marker"],
                markersize=style["markersize"], linestyle="none",
                markeredgecolor="white", markeredgewidth=0.5,
                label=label, zorder=5)

        offset_y = 0.3 if metric_key in ("headroom", "degen") else 0.08
        fmt_val = fmt_func(val) if fmt_func else f"{val:.1f}"
        ax.annotate(fmt_val, (d["size"], val),
                    textcoords="offset points", xytext=(4, 5),
                    fontsize=6.5, color=style["color"])

    # Connect same-family same-regime same-dataset points with lines
    groups = {}
    for d, val in points:
        key = (d["family"], d["regime"], d["dataset"])
        groups.setdefault(key, []).append((d["size"], val, d))
    for key, pts in groups.items():
        if len(pts) < 2:
            continue
        pts.sort(key=lambda x: x[0])
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        style = get_style(pts[0][2])
        ax.plot(xs, ys, color=style["color"], linestyle=style["linestyle"],
                linewidth=style["linewidth"] * 0.7, zorder=3, alpha=0.6)

    ax.set_xscale("log")
    ax.set_xticks([4, 7, 8, 14, 32, 72])
    ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.tick_params(axis="both", labelsize=7)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.grid(True, alpha=0.2, linewidth=0.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    data_path = os.path.join(SCRIPT_DIR, "scaling_results.json")
    if os.path.exists(data_path):
        data = load_data_from_json(data_path)
    else:
        data = DATA

    fig, axes = plt.subplots(1, 4, figsize=(11.5, 2.8))
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.18, top=0.88, wspace=0.35)

    plot_panel(axes[0], data, "degen",        "Degeneracy (%)",           lambda v: f"{v:.1f}%")
    plot_panel(axes[1], data, "headroom",     "Oracle headroom (pp)",     lambda v: f"{v:.1f}")
    plot_panel(axes[2], data, "lp_delta",     "LP selection $\\Delta$ (pp)", lambda v: f"{v:.2f}")
    plot_panel(axes[3], data, "constr_delta", "Construction $\\Delta$ (pp)", lambda v: f"{v:.2f}")

    axes[0].set_xlabel("Model size (B params)", fontsize=8)
    axes[1].set_xlabel("Model size (B params)", fontsize=8)
    axes[2].set_xlabel("Model size (B params)", fontsize=8)
    axes[3].set_xlabel("Model size (B params)", fontsize=8)

    handles, labels = [], []
    for ax in axes:
        h, l = ax.get_legend_handles_labels()
        for hi, li in zip(h, l):
            if li not in labels:
                handles.append(hi)
                labels.append(li)
    if handles:
        fig.legend(handles, labels, loc="upper center", ncol=len(labels),
                   fontsize=7, frameon=False, bbox_to_anchor=(0.5, 1.0))

    panel_labels = ["(a)", "(b)", "(c)", "(d)"]
    for ax, pl in zip(axes, panel_labels):
        ax.set_title(pl, fontsize=8, fontweight="bold", pad=8)

    out_pdf = os.path.join(SCRIPT_DIR, "scaling_curve.pdf")
    out_png = os.path.join(SCRIPT_DIR, "scaling_curve.png")
    fig.savefig(out_pdf, bbox_inches="tight", dpi=300)
    fig.savefig(out_png, bbox_inches="tight", dpi=200)
    print(f"Saved: {out_pdf}")
    print(f"Saved: {out_png}")
    plt.close(fig)


if __name__ == "__main__":
    main()
