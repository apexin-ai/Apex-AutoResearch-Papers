#!/usr/bin/env python3
"""Generate Cinelli-Hazlett sensitivity contour plots for K=3, K=5, K=7."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "paper" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ATTACKS_ORDER = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
ATTACK_LABELS = {
    "prompt_injection": "PromptInj",
    "sycophancy": "Sycoph",
    "score_manipulation": "ScoreManip",
    "verbosity_bias": "Verbose",
    "position_bias": "Position",
    "authority_bias": "Authority",
}
BENCHMARKS = ["mmlu", "arc_challenge"]
BENCH_LABELS = {"mmlu": "MMLU", "arc_challenge": "ARC"}

DATA = [
    # K=3 mmlu
    {"K":3,"benchmark":"mmlu","attack":"prompt_injection","dof":452,"beta_keff":63.841,"se_keff":5.102,"eta_partial_r2_treatment":0.5416,"eta_partial_r2_outcome":0.00994,"keff_rv":0.4403},
    {"K":3,"benchmark":"mmlu","attack":"sycophancy","dof":452,"beta_keff":12.965,"se_keff":0.8612,"eta_partial_r2_treatment":0.2427,"eta_partial_r2_outcome":0.01395,"keff_rv":0.5005},
    {"K":3,"benchmark":"mmlu","attack":"score_manipulation","dof":452,"beta_keff":20.922,"se_keff":1.5671,"eta_partial_r2_treatment":0.6194,"eta_partial_r2_outcome":0.000105,"keff_rv":0.4610},
    {"K":3,"benchmark":"mmlu","attack":"verbosity_bias","dof":452,"beta_keff":8.9995,"se_keff":1.0117,"eta_partial_r2_treatment":0.3565,"eta_partial_r2_outcome":0.1176,"keff_rv":0.3399},
    {"K":3,"benchmark":"mmlu","attack":"position_bias","dof":452,"beta_keff":6.0978,"se_keff":1.3229,"eta_partial_r2_treatment":0.4258,"eta_partial_r2_outcome":0.3268,"keff_rv":0.1946},
    {"K":3,"benchmark":"mmlu","attack":"authority_bias","dof":452,"beta_keff":8.3222,"se_keff":0.5657,"eta_partial_r2_treatment":0.3551,"eta_partial_r2_outcome":0.000645,"keff_rv":0.4928},
    # K=3 arc_challenge
    {"K":3,"benchmark":"arc_challenge","attack":"prompt_injection","dof":452,"beta_keff":45.314,"se_keff":3.056,"eta_partial_r2_treatment":0.4299,"eta_partial_r2_outcome":0.01697,"keff_rv":0.4954},
    {"K":3,"benchmark":"arc_challenge","attack":"sycophancy","dof":452,"beta_keff":4.1185,"se_keff":0.3493,"eta_partial_r2_treatment":0.3985,"eta_partial_r2_outcome":0.00416,"keff_rv":0.4217},
    {"K":3,"benchmark":"arc_challenge","attack":"score_manipulation","dof":452,"beta_keff":16.852,"se_keff":0.8683,"eta_partial_r2_treatment":0.7528,"eta_partial_r2_outcome":0.1264,"keff_rv":0.5868},
    {"K":3,"benchmark":"arc_challenge","attack":"verbosity_bias","dof":452,"beta_keff":12.005,"se_keff":0.8107,"eta_partial_r2_treatment":0.5372,"eta_partial_r2_outcome":0.000470,"keff_rv":0.4950},
    {"K":3,"benchmark":"arc_challenge","attack":"position_bias","dof":452,"beta_keff":12.431,"se_keff":2.7514,"eta_partial_r2_treatment":0.8168,"eta_partial_r2_outcome":0.003303,"keff_rv":0.1911},
    {"K":3,"benchmark":"arc_challenge","attack":"authority_bias","dof":452,"beta_keff":3.3118,"se_keff":0.2917,"eta_partial_r2_treatment":0.4548,"eta_partial_r2_outcome":0.01997,"keff_rv":0.4102},
    # K=5 mmlu
    {"K":5,"benchmark":"mmlu","attack":"prompt_injection","dof":3000,"beta_keff":3.2709,"se_keff":0.09677,"eta_partial_r2_treatment":0.3789,"eta_partial_r2_outcome":0.1764,"keff_rv":0.4554},
    {"K":5,"benchmark":"mmlu","attack":"sycophancy","dof":3000,"beta_keff":1.9660,"se_keff":0.09899,"eta_partial_r2_treatment":0.1064,"eta_partial_r2_outcome":0.1346,"keff_rv":0.3028},
    {"K":5,"benchmark":"mmlu","attack":"score_manipulation","dof":3000,"beta_keff":2.7424,"se_keff":0.12856,"eta_partial_r2_treatment":0.5966,"eta_partial_r2_outcome":0.00335,"keff_rv":0.3209},
    {"K":5,"benchmark":"mmlu","attack":"verbosity_bias","dof":3000,"beta_keff":2.2246,"se_keff":0.15119,"eta_partial_r2_treatment":0.1196,"eta_partial_r2_outcome":0.2057,"keff_rv":0.2350},
    {"K":5,"benchmark":"mmlu","attack":"position_bias","dof":3000,"beta_keff":0.04445,"se_keff":0.005784,"eta_partial_r2_treatment":0.2720,"eta_partial_r2_outcome":0.09019,"keff_rv":0.1308},
    {"K":5,"benchmark":"mmlu","attack":"authority_bias","dof":3000,"beta_keff":0.4786,"se_keff":0.13233,"eta_partial_r2_treatment":0.2770,"eta_partial_r2_outcome":0.03089,"keff_rv":0.06389},
    # K=5 arc_challenge
    {"K":5,"benchmark":"arc_challenge","attack":"prompt_injection","dof":3000,"beta_keff":6.3866,"se_keff":0.3031,"eta_partial_r2_treatment":0.6964,"eta_partial_r2_outcome":0.000618,"keff_rv":0.3178},
    {"K":5,"benchmark":"arc_challenge","attack":"sycophancy","dof":3000,"beta_keff":-3.5767,"se_keff":0.6001,"eta_partial_r2_treatment":0.5548,"eta_partial_r2_outcome":0.06319,"keff_rv":0.1031},
    {"K":5,"benchmark":"arc_challenge","attack":"score_manipulation","dof":3000,"beta_keff":6.5715,"se_keff":0.5500,"eta_partial_r2_treatment":0.8002,"eta_partial_r2_outcome":0.000160,"keff_rv":0.1957},
    {"K":5,"benchmark":"arc_challenge","attack":"verbosity_bias","dof":3000,"beta_keff":4.4592,"se_keff":0.5599,"eta_partial_r2_treatment":0.6416,"eta_partial_r2_outcome":0.03377,"keff_rv":0.1352},
    {"K":5,"benchmark":"arc_challenge","attack":"position_bias","dof":3000,"beta_keff":0.17674,"se_keff":0.006240,"eta_partial_r2_treatment":0.7785,"eta_partial_r2_outcome":0.04005,"keff_rv":0.4004},
    {"K":5,"benchmark":"arc_challenge","attack":"authority_bias","dof":3000,"beta_keff":6.6904,"se_keff":0.6097,"eta_partial_r2_treatment":0.5086,"eta_partial_r2_outcome":0.01212,"keff_rv":0.1813},
    # K=7 mmlu
    {"K":7,"benchmark":"mmlu","attack":"prompt_injection","dof":6432,"beta_keff":3.5871,"se_keff":0.05918,"eta_partial_r2_treatment":0.2889,"eta_partial_r2_outcome":0.1259,"keff_rv":0.5223},
    {"K":7,"benchmark":"mmlu","attack":"sycophancy","dof":6432,"beta_keff":2.3067,"se_keff":0.08005,"eta_partial_r2_treatment":0.07658,"eta_partial_r2_outcome":0.07813,"keff_rv":0.3005},
    {"K":7,"benchmark":"mmlu","attack":"score_manipulation","dof":6432,"beta_keff":3.0119,"se_keff":0.07441,"eta_partial_r2_treatment":0.5147,"eta_partial_r2_outcome":0.004490,"keff_rv":0.3932},
    {"K":7,"benchmark":"mmlu","attack":"verbosity_bias","dof":6432,"beta_keff":2.3799,"se_keff":0.12880,"eta_partial_r2_treatment":0.07840,"eta_partial_r2_outcome":0.19468,"keff_rv":0.2054},
    {"K":7,"benchmark":"mmlu","attack":"position_bias","dof":6432,"beta_keff":0.06094,"se_keff":0.003271,"eta_partial_r2_treatment":0.17939,"eta_partial_r2_outcome":0.07282,"keff_rv":0.2069},
    {"K":7,"benchmark":"mmlu","attack":"authority_bias","dof":6432,"beta_keff":0.05153,"se_keff":0.13483,"eta_partial_r2_treatment":0.2005,"eta_partial_r2_outcome":0.01071,"keff_rv":0.00475},
    # K=7 arc_challenge
    {"K":7,"benchmark":"arc_challenge","attack":"prompt_injection","dof":6432,"beta_keff":6.4995,"se_keff":0.18305,"eta_partial_r2_treatment":0.6287,"eta_partial_r2_outcome":0.004348,"keff_rv":0.3554},
    {"K":7,"benchmark":"arc_challenge","attack":"sycophancy","dof":6432,"beta_keff":-5.2117,"se_keff":0.52169,"eta_partial_r2_treatment":0.5355,"eta_partial_r2_outcome":0.06494,"keff_rv":0.1170},
    {"K":7,"benchmark":"arc_challenge","attack":"score_manipulation","dof":6432,"beta_keff":6.3605,"se_keff":0.44028,"eta_partial_r2_treatment":0.7166,"eta_partial_r2_outcome":0.000887,"keff_rv":0.1646},
    {"K":7,"benchmark":"arc_challenge","attack":"verbosity_bias","dof":6432,"beta_keff":6.7582,"se_keff":0.46578,"eta_partial_r2_treatment":0.5994,"eta_partial_r2_outcome":0.02815,"keff_rv":0.1653},
    {"K":7,"benchmark":"arc_challenge","attack":"position_bias","dof":6432,"beta_keff":0.12162,"se_keff":0.002730,"eta_partial_r2_treatment":0.7051,"eta_partial_r2_outcome":0.04571,"keff_rv":0.4223},
    {"K":7,"benchmark":"arc_challenge","attack":"authority_bias","dof":6432,"beta_keff":8.2118,"se_keff":0.51911,"eta_partial_r2_treatment":0.5138,"eta_partial_r2_outcome":0.002988,"keff_rv":0.1787},
]


def adjusted_beta(beta_hat, se, dof, Rd, Ry):
    """Cinelli-Hazlett adjusted estimate under hypothetical confounding."""
    bias = se * np.sqrt(dof) * np.sqrt(Rd * Ry / (1 - Rd + 1e-12))
    return beta_hat - np.sign(beta_hat) * bias


def plot_contour_panel(ax, d):
    """Plot a single sensitivity contour on the given axes."""
    beta = d["beta_keff"]
    se = d["se_keff"]
    dof = d["dof"]
    eta_Rd = d["eta_partial_r2_treatment"]
    eta_Ry = d["eta_partial_r2_outcome"]
    rv = d["keff_rv"]

    N = 200
    Rd = np.linspace(0.001, 0.99, N)
    Ry = np.linspace(0.001, 0.99, N)
    Rd_g, Ry_g = np.meshgrid(Rd, Ry)
    Z = adjusted_beta(beta, se, dof, Rd_g, Ry_g)

    cmap = LinearSegmentedColormap.from_list(
        "blue_white", ["#b3d4f7", "#d9ecfb", "#eef5fc", "#ffffff"], N=256
    )

    abs_beta = abs(beta)
    if abs_beta > 1:
        step = max(1, round(abs_beta / 6))
        max_level = int(abs_beta) + step
        levels_fill = np.arange(-max_level, max_level + step, step).astype(float)
    else:
        step = round(abs_beta / 5, 3) or 0.01
        max_level = abs_beta + step * 3
        levels_fill = np.arange(-max_level, max_level + step, step)

    levels_fill = sorted(set(levels_fill))
    if len(levels_fill) < 3:
        levels_fill = np.linspace(-abs_beta * 2, abs_beta * 2, 12)

    ax.contourf(Rd_g, Ry_g, Z, levels=levels_fill, cmap=cmap, extend="both")

    contour_levels = [l for l in levels_fill if l != 0]
    if contour_levels:
        cs = ax.contour(
            Rd_g, Ry_g, Z, levels=contour_levels,
            colors="0.55", linewidths=0.6, linestyles="solid"
        )
        ax.clabel(cs, inline=True, fontsize=6, fmt="%.4g")

    cs0 = ax.contour(
        Rd_g, Ry_g, Z, levels=[0.0],
        colors="#c0392b", linewidths=1.8, linestyles="solid"
    )
    ax.clabel(cs0, inline=True, fontsize=7, fmt="%.0f")

    rv_Rd = np.linspace(rv * 0.01, min(rv * 3, 0.99), 200)
    rv_Ry_line = rv**2 / rv_Rd
    mask = rv_Ry_line < 0.99
    if mask.any():
        ax.plot(rv_Rd[mask], rv_Ry_line[mask], color="#e67e22",
                linewidth=1.0, linestyle="--", alpha=0.8)

    ax.plot(eta_Rd, eta_Ry, marker="D", color="#c0392b", markersize=5,
            markeredgecolor="white", markeredgewidth=0.6, zorder=5)
    label_x = eta_Rd + 0.03
    label_y = eta_Ry + 0.03
    if label_x > 0.85:
        label_x = eta_Rd - 0.08
    if label_y > 0.85:
        label_y = eta_Ry - 0.06
    ax.annotate(
        r"$\eta_{\max}$", (eta_Rd, eta_Ry),
        xytext=(label_x, label_y), fontsize=7,
        color="#c0392b", fontweight="bold",
        arrowprops=dict(arrowstyle="-", color="#c0392b", lw=0.5)
        if abs(label_x - eta_Rd) > 0.05 else None,
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel(r"$R^2_{D \sim Z | X}$", fontsize=8)
    ax.set_ylabel(r"$R^2_{Y \sim Z | D,X}$", fontsize=8)
    ax.tick_params(labelsize=7)

    for spine in ax.spines.values():
        spine.set_linewidth(0.5)
        spine.set_color("0.4")

    info = f"$\\beta$={beta:.2g}\nRV={rv:.2f}"
    ax.text(
        0.97, 0.97, info, transform=ax.transAxes,
        fontsize=6, va="top", ha="right",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="0.7", alpha=0.9),
    )


def make_figure(K):
    """Create 4x3 multi-panel contour figure for a given K."""
    conditions = [d for d in DATA if d["K"] == K]
    cond_map = {(d["benchmark"], d["attack"]): d for d in conditions}

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 10,
        "axes.labelsize": 8,
    })

    fig, axes = plt.subplots(4, 3, figsize=(13.5, 16))
    fig.suptitle(f"Cinelli–Hazlett Sensitivity Analysis: K={K}",
                 fontsize=14, fontweight="bold", y=0.995)

    for row_idx, bench in enumerate(BENCHMARKS):
        for col_idx, atk in enumerate(ATTACKS_ORDER):
            ax_row = row_idx * 2 + (col_idx // 3)
            ax_col = col_idx % 3

            grid_row = row_idx * 2 + (col_idx >= 3)
            grid_col = col_idx % 3 if col_idx < 3 else col_idx - 3

            ax = axes[grid_row, grid_col]
            key = (bench, atk)
            if key in cond_map:
                d = cond_map[key]
                plot_contour_panel(ax, d)
                ax.set_title(
                    f"{BENCH_LABELS[bench]} × {ATTACK_LABELS[atk]}",
                    fontsize=9, fontweight="bold", pad=4,
                )

    fig.tight_layout(rect=[0, 0, 1, 0.98])

    for fmt in ("pdf", "png"):
        path = OUT_DIR / f"fig_sensitivity_contour_K{K}.{fmt}"
        fig.savefig(path, dpi=300, bbox_inches="tight",
                    facecolor="white", edgecolor="none")
        print(f"Saved: {path}")
    plt.close(fig)


if __name__ == "__main__":
    for K in (3, 5, 7):
        print(f"\n--- Generating K={K} ---")
        make_figure(K)
    print("\nDone.")
