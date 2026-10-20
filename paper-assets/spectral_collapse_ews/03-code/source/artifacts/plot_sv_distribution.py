"""Visualize singular value distributions: Gen 0 vs Gen 2 (Pythia-410M, r=0)."""
import sys
sys.path.insert(0, "/root/spectral_collapse_ews")

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from artifacts.visual_design_language_v2 import apply_style, COLORS, LINES, FONTS, FIGSIZE, style_axes

apply_style()


def main():
    with open("/root/spectral_collapse_ews/results/sv_distributions.json") as f:
        data = json.load(f)

    sv0 = np.array(data["gen_0"]["singular_values"])
    sv2 = np.array(data["gen_2"]["singular_values"])
    ranks = np.arange(1, len(sv0) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.6))

    # --- Panel (a): Full SV distribution (log scale) ---
    ax1.semilogy(ranks, sv0, color=COLORS["baseline"], **LINES["data"],
                 label=f"Gen 0 ($r_{{\\mathrm{{eff}}}}$={data['gen_0']['effective_rank']:.0f})")
    ax1.semilogy(ranks, sv2, color=COLORS["r0"], **LINES["data"],
                 label=f"Gen 2 ($r_{{\\mathrm{{eff}}}}$={data['gen_2']['effective_rank']:.0f})")

    ax1.set_xlabel("Singular value index $i$", **FONTS["axis_label"])
    ax1.set_ylabel("$\\sigma_i$ (log scale)", **FONTS["axis_label"])
    style_axes(ax1)

    ax1.annotate(
        f"$\\sigma_1$: {sv0[0]:.0f} → {sv2[0]:.0f}\n({(sv2[0]-sv0[0])/sv0[0]*100:.0f}%)",
        xy=(1, sv0[0]), xytext=(60, -10), textcoords="offset points",
        fontsize=6, color=COLORS["annotation"],
        arrowprops=dict(arrowstyle="->", color=COLORS["annotation"], lw=0.5,
                        connectionstyle="arc3,rad=0.15"),
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.85),
    )

    tail_start = max(len(sv0) - 100, 0)
    tail_mean_0 = np.mean(sv0[tail_start:])
    tail_mean_2 = np.mean(sv2[tail_start:])
    ax1.annotate(
        f"tail mean: {tail_mean_0:.1f} → {tail_mean_2:.1f}\n(+{(tail_mean_2-tail_mean_0)/tail_mean_0*100:.0f}%)",
        xy=(len(sv0) - 50, tail_mean_2), xytext=(-80, 30), textcoords="offset points",
        fontsize=6, color=COLORS["annotation"],
        arrowprops=dict(arrowstyle="->", color=COLORS["annotation"], lw=0.5,
                        connectionstyle="arc3,rad=-0.15"),
        bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.85),
    )

    ax1.legend(**{k: v for k, v in {
        "frameon": False, "fontsize": 6.5, "loc": "upper right",
        "handlelength": 1.5, "handletextpad": 0.4,
    }.items()})

    ax1.text(-0.14, 1.05, "(a)", transform=ax1.transAxes, **FONTS["panel_label"])

    # --- Panel (b): Normalized SV (cumulative energy) ---
    energy0 = np.cumsum(sv0**2) / np.sum(sv0**2)
    energy2 = np.cumsum(sv2**2) / np.sum(sv2**2)

    ax2.plot(ranks, energy0, color=COLORS["baseline"], **LINES["data"], label="Gen 0")
    ax2.plot(ranks, energy2, color=COLORS["r0"], **LINES["data"], label="Gen 2")

    for threshold in [0.90, 0.99]:
        k0 = np.searchsorted(energy0, threshold) + 1
        k2 = np.searchsorted(energy2, threshold) + 1
        ax2.axhline(y=threshold, **LINES["reference"], color=COLORS["light_ref"])
        ax2.text(len(sv0) * 0.55, threshold + 0.005,
                 f"{threshold*100:.0f}%: $k$={k0} → {k2}",
                 fontsize=5.5, color=COLORS["annotation"])

    ax2.set_xlabel("Singular value index $i$", **FONTS["axis_label"])
    ax2.set_ylabel("Cumulative energy fraction", **FONTS["axis_label"])
    ax2.set_ylim(0, 1.05)
    style_axes(ax2)

    ax2.legend(**{k: v for k, v in {
        "frameon": False, "fontsize": 6.5, "loc": "lower right",
        "handlelength": 1.5, "handletextpad": 0.4,
    }.items()})

    ax2.text(-0.14, 1.05, "(b)", transform=ax2.transAxes, **FONTS["panel_label"])

    plt.tight_layout(w_pad=2.0)
    out_pdf = "/root/spectral_collapse_ews/artifacts/sv_distribution_comparison.pdf"
    out_png = "/root/spectral_collapse_ews/artifacts/sv_distribution_comparison.png"
    fig.savefig(out_pdf)
    fig.savefig(out_png, dpi=200)
    print(f"Saved: {out_pdf}")
    print(f"Saved: {out_png}")
    plt.close()


if __name__ == "__main__":
    main()
