#!/usr/bin/env python3
"""Scaling curve plots: signal ρ, degeneracy, construction ΔF1 vs model size."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# ─── DATA ────────────────────────────────────────────────────────────────────
# Keys: (model_size_B, regime, dataset) → dict of metrics
# regime: "ft" or "zs"
# Fill None for missing; plotting skips None entries.

DATA = {
    # ── Qwen3-4B FT ──
    (4, "ft", "SciERC"):    {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": 10.4, "construction_lp_delta": None,
                              "greedy_f1": 0.662, "oracle_f1": None},
    (4, "ft", "FewNERD"):   {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (4, "ft", "CoNLL"):     {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},

    # ── Qwen3-7B FT (placeholder) ──
    (7, "ft", "SciERC"):    {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (7, "ft", "FewNERD"):   {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (7, "ft", "CoNLL"):     {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},

    # ── Qwen3-8B FT ── (values from tab:scale_comparison unless noted)
    (8, "ft", "SciERC"):    {"lp_rho": 0.205, "sj_rho": 0.360, "vc_rho": 0.379,
                              "degen": 17.8, "construction_lp_delta": 1.02,  # tab:entity_construction, multi-seed mean
                              "greedy_f1": 0.644, "oracle_f1": None},
    (8, "ft", "FewNERD"):   {"lp_rho": 0.220, "sj_rho": None, "vc_rho": None,
                              "degen": 13.0, "construction_lp_delta": 1.40,  # tab:entity_construction, multi-seed mean; degen=3-seed mean per paper
                              "greedy_f1": 0.748, "oracle_f1": None},
    (8, "ft", "CoNLL"):     {"lp_rho": 0.302, "sj_rho": None, "vc_rho": None,
                              "degen": 61.7, "construction_lp_delta": -0.39,  # tab:entity_construction; degen=N=8 3-seed mean per paper
                              "greedy_f1": 0.908, "oracle_f1": None},

    # ── Qwen3-14B FT (placeholder) ──
    (14, "ft", "SciERC"):   {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (14, "ft", "FewNERD"):  {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (14, "ft", "CoNLL"):    {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},

    # ── Qwen3-32B FT (placeholder) ──
    (32, "ft", "SciERC"):   {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (32, "ft", "FewNERD"):  {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},
    (32, "ft", "CoNLL"):    {"lp_rho": None, "sj_rho": None, "vc_rho": None,
                              "degen": None, "construction_lp_delta": None,
                              "greedy_f1": None, "oracle_f1": None},

    # ── Qwen3-72B ZS ──
    (72, "zs", "SciERC"):   {"lp_rho": 0.081, "sj_rho": 0.217, "vc_rho": 0.277,
                              "degen": 21.0, "construction_lp_delta": 1.53,
                              "greedy_f1": 0.399, "oracle_f1": None},
    (72, "zs", "FewNERD"):  {"lp_rho": 0.119, "sj_rho": 0.345, "vc_rho": 0.416,
                              "degen": 46.2, "construction_lp_delta": -0.20,
                              "greedy_f1": 0.628, "oracle_f1": None},
    (72, "zs", "CoNLL"):    {"lp_rho": -0.002, "sj_rho": 0.304, "vc_rho": 0.297,
                              "degen": 67.7, "construction_lp_delta": -0.37,
                              "greedy_f1": 0.712, "oracle_f1": None},
}

# ─── STYLE ───────────────────────────────────────────────────────────────────

DATASETS = ["SciERC", "FewNERD", "CoNLL"]
REGIMES = {"ft": ("Fine-tuned", "-", "o"), "zs": ("Zero-shot", "--", "s")}

# Colorblind-safe palette (Okabe-Ito inspired)
SIGNAL_COLORS = {"lp_rho": "#0072B2", "sj_rho": "#D55E00", "vc_rho": "#009E73"}
SIGNAL_LABELS = {"lp_rho": "LP ρ", "sj_rho": "SJ ρ", "vc_rho": "VC ρ"}
SIGNAL_MARKERS = {"lp_rho": "o", "sj_rho": "^", "vc_rho": "D"}

DATASET_COLORS = {"SciERC": "#0072B2", "FewNERD": "#D55E00", "CoNLL": "#009E73"}
DATASET_MARKERS = {"SciERC": "o", "FewNERD": "^", "CoNLL": "D"}

ALL_SIZES = sorted({k[0] for k in DATA.keys()})

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 8,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "legend.fontsize": 7,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "lines.linewidth": 1.3,
    "lines.markersize": 5,
    "axes.linewidth": 0.6,
    "grid.linewidth": 0.4,
    "grid.alpha": 0.3,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
})


def _extract(dataset, regime, metric):
    """Return (sizes, values) for non-None entries."""
    sizes, vals = [], []
    for sz in ALL_SIZES:
        key = (sz, regime, dataset)
        if key in DATA and DATA[key].get(metric) is not None:
            sizes.append(sz)
            vals.append(DATA[key][metric])
    return np.array(sizes), np.array(vals)


def _fmt_xticks(ax):
    ax.set_xscale("log")
    ax.set_xticks(ALL_SIZES)
    ax.get_xaxis().set_major_formatter(mticker.FuncFormatter(
        lambda x, _: f"{int(x)}B" if x == int(x) else f"{x}B"))
    ax.get_xaxis().set_minor_formatter(mticker.NullFormatter())
    ax.set_xlim(ALL_SIZES[0] * 0.65, ALL_SIZES[-1] * 1.5)
    ax.tick_params(axis="x", which="minor", bottom=False)
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha("right")


# ─── FIGURE A: Signal ρ vs Model Size ────────────────────────────────────────

def plot_signal_rho(outdir: Path):
    fig, axes = plt.subplots(1, 3, figsize=(6.75, 2.2), sharey=True)

    for ax, ds in zip(axes, DATASETS):
        for signal in ["lp_rho", "sj_rho", "vc_rho"]:
            for regime, (rlabel, lstyle, _) in REGIMES.items():
                sx, sy = _extract(ds, regime, signal)
                if len(sx) == 0:
                    continue
                label = f"{SIGNAL_LABELS[signal]} ({rlabel})"
                ax.plot(sx, sy, color=SIGNAL_COLORS[signal],
                        linestyle=lstyle, marker=SIGNAL_MARKERS[signal],
                        label=label, zorder=3)

        ax.set_title(ds)
        _fmt_xticks(ax)
        ax.set_xlabel("Model Size")
        ax.axhline(0, color="grey", lw=0.5, ls=":")
        ax.grid(True, axis="y")

    axes[0].set_ylabel("Spearman ρ")

    handles, labels = [], []
    for ax in axes:
        h, l = ax.get_legend_handles_labels()
        for hi, li in zip(h, l):
            if li not in labels:
                handles.append(hi)
                labels.append(li)
    fig.legend(handles, labels, loc="upper center", ncol=3,
               bbox_to_anchor=(0.5, 1.13), frameon=False)

    fig.tight_layout(rect=[0, 0, 1, 0.92])
    for ext in ("pdf", "png"):
        fig.savefig(outdir / f"scaling_signal_rho.{ext}")
    plt.close(fig)
    print(f"  → scaling_signal_rho.pdf/png")


# ─── FIGURE B: Degeneracy vs Model Size ──────────────────────────────────────

def plot_degeneracy(outdir: Path):
    fig, ax = plt.subplots(figsize=(3.25, 2.2))

    for ds in DATASETS:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            sx, sy = _extract(ds, regime, "degen")
            if len(sx) == 0:
                continue
            label = f"{ds} ({rlabel})"
            ax.plot(sx, sy, color=DATASET_COLORS[ds],
                    linestyle=lstyle, marker=DATASET_MARKERS[ds],
                    label=label, zorder=3)

    _fmt_xticks(ax)
    ax.set_xlabel("Model Size")
    ax.set_ylabel("Degeneracy Rate (%)")
    ax.grid(True, axis="y")
    ax.legend(loc="best", framealpha=0.9)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(outdir / f"scaling_degeneracy.{ext}")
    plt.close(fig)
    print(f"  → scaling_degeneracy.pdf/png")


# ─── FIGURE C: Construction ΔF1 vs Model Size ────────────────────────────────

def plot_construction_delta(outdir: Path):
    fig, ax = plt.subplots(figsize=(3.25, 2.2))

    ax.axhline(0, color="grey", lw=0.8, ls="-", zorder=1)
    ax.axhspan(0, 10, color="#c8e6c9", alpha=0.25, zorder=0)
    ax.axhspan(-5, 0, color="#ffcdd2", alpha=0.25, zorder=0)

    for ds in DATASETS:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            sx, sy = _extract(ds, regime, "construction_lp_delta")
            if len(sx) == 0:
                continue
            label = f"{ds} ({rlabel})"
            ax.plot(sx, sy, color=DATASET_COLORS[ds],
                    linestyle=lstyle, marker=DATASET_MARKERS[ds],
                    label=label, zorder=3)

    _fmt_xticks(ax)
    ax.set_xlabel("Model Size")
    ax.set_ylabel("LP-weighted Construction ΔF1 (pp)")
    ax.grid(True, axis="y")
    ax.legend(loc="best", framealpha=0.9)

    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(outdir / f"scaling_construction_delta.{ext}")
    plt.close(fig)
    print(f"  → scaling_construction_delta.pdf/png")


# ─── COMBINED (single PDF for draft review) ──────────────────────────────────

def plot_combined(outdir: Path):
    fig = plt.figure(figsize=(6.75, 6.0))
    gs = fig.add_gridspec(3, 3, hspace=0.55, wspace=0.30,
                          left=0.08, right=0.97, top=0.90, bottom=0.07)

    # Row 1: Signal ρ (3 subplots)
    for col, ds in enumerate(DATASETS):
        ax = fig.add_subplot(gs[0, col])
        for signal in ["lp_rho", "sj_rho", "vc_rho"]:
            for regime, (rlabel, lstyle, _) in REGIMES.items():
                sx, sy = _extract(ds, regime, signal)
                if len(sx) == 0:
                    continue
                ax.plot(sx, sy, color=SIGNAL_COLORS[signal],
                        linestyle=lstyle, marker=SIGNAL_MARKERS[signal],
                        label=f"{SIGNAL_LABELS[signal]} ({rlabel})", zorder=3)
        ax.set_title(ds)
        _fmt_xticks(ax)
        ax.axhline(0, color="grey", lw=0.5, ls=":")
        ax.grid(True, axis="y")
        if col == 0:
            ax.set_ylabel("Spearman ρ")
        if col == 1:
            ax.set_xlabel("Model Size")

    # Row 1 legend
    h_sig, l_sig = [], []
    for signal in ["lp_rho", "sj_rho", "vc_rho"]:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            lab = f"{SIGNAL_LABELS[signal]} ({rlabel})"
            if lab not in l_sig:
                line = plt.Line2D([], [], color=SIGNAL_COLORS[signal],
                                  linestyle=lstyle, marker=SIGNAL_MARKERS[signal],
                                  markersize=4, lw=1.2)
                h_sig.append(line)
                l_sig.append(lab)
    fig.legend(h_sig, l_sig, loc="upper center", ncol=3,
               bbox_to_anchor=(0.5, 0.99), frameon=False, fontsize=6.5)

    # Row 2: Degeneracy
    ax_dg = fig.add_subplot(gs[1, 0:2])
    for ds in DATASETS:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            sx, sy = _extract(ds, regime, "degen")
            if len(sx) == 0:
                continue
            ax_dg.plot(sx, sy, color=DATASET_COLORS[ds],
                       linestyle=lstyle, marker=DATASET_MARKERS[ds],
                       label=f"{ds} ({rlabel})", zorder=3)
    _fmt_xticks(ax_dg)
    ax_dg.set_xlabel("Model Size")
    ax_dg.set_ylabel("Degeneracy Rate (%)")
    ax_dg.grid(True, axis="y")
    ax_dg.legend(loc="best", framealpha=0.9, fontsize=6.5)

    # Row 2 right: empty or greedy F1 bonus
    ax_f1 = fig.add_subplot(gs[1, 2])
    for ds in DATASETS:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            sx, sy = _extract(ds, regime, "greedy_f1")
            if len(sx) == 0:
                continue
            ax_f1.plot(sx, sy * 100, color=DATASET_COLORS[ds],
                       linestyle=lstyle, marker=DATASET_MARKERS[ds],
                       label=f"{ds} ({rlabel})", zorder=3)
    _fmt_xticks(ax_f1)
    ax_f1.set_xlabel("Model Size")
    ax_f1.set_ylabel("Greedy F1 (%)")
    ax_f1.grid(True, axis="y")
    ax_f1.legend(loc="best", framealpha=0.9, fontsize=6.5)

    # Row 3: Construction ΔF1
    ax_cd = fig.add_subplot(gs[2, 0:2])
    ax_cd.axhline(0, color="grey", lw=0.8, ls="-", zorder=1)
    ax_cd.axhspan(0, 10, color="#c8e6c9", alpha=0.2, zorder=0)
    ax_cd.axhspan(-5, 0, color="#ffcdd2", alpha=0.2, zorder=0)
    for ds in DATASETS:
        for regime, (rlabel, lstyle, _) in REGIMES.items():
            sx, sy = _extract(ds, regime, "construction_lp_delta")
            if len(sx) == 0:
                continue
            ax_cd.plot(sx, sy, color=DATASET_COLORS[ds],
                       linestyle=lstyle, marker=DATASET_MARKERS[ds],
                       label=f"{ds} ({rlabel})", zorder=3)
    _fmt_xticks(ax_cd)
    ax_cd.set_xlabel("Model Size")
    ax_cd.set_ylabel("Construction ΔF1 (pp)")
    ax_cd.grid(True, axis="y")
    ax_cd.legend(loc="best", framealpha=0.9, fontsize=6.5)

    for ext in ("pdf", "png"):
        fig.savefig(outdir / f"scaling_curve_draft.{ext}")
    plt.close(fig)
    print(f"  → scaling_curve_draft.pdf/png")


# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    outdir = Path(__file__).parent
    print("Generating scaling curve plots...")
    plot_signal_rho(outdir)
    plot_degeneracy(outdir)
    plot_construction_delta(outdir)
    plot_combined(outdir)
    print("Done.")
