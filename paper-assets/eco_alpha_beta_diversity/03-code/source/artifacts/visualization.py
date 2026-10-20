# Visualization: Hill number comparison, Baselga decomposition, cosine heatmap, rarefaction.

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

COND_COLORS = {
    "no-AI": "#1f77b4",
    "AI-editor": "#ff7f0e",
    "AI-ideas+editor": "#2ca02c",
}

def _color(cond):
    return COND_COLORS.get(cond, "#999999")


def plot_hill_comparison(hill_results, output_dir):
    """Grouped bar chart: Hill numbers (alpha, gamma, beta) by condition and q."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    metrics = ["alpha", "gamma", "beta"]
    titles = [r"$\alpha$ diversity (within-story)", r"$\gamma$ diversity (pooled)",
              r"$\beta$ diversity ($\gamma/\alpha$)"]

    for ax, metric, title in zip(axes, metrics, titles):
        q_labels = ["q=0", "q=1", "q=2"]
        conditions = sorted(hill_results["q0"].keys(),
                            key=lambda c: ["no-AI", "AI-editor", "AI-ideas+editor"].index(c)
                            if c in ["no-AI", "AI-editor", "AI-ideas+editor"] else 99)
        n_cond = len(conditions)
        bar_w = 0.8 / n_cond
        x = np.arange(len(q_labels))

        for ci, cond in enumerate(conditions):
            vals, lo_err, hi_err = [], [], []
            for q in ["q0", "q1", "q2"]:
                v = hill_results[q][cond][metric]
                ci_lo, ci_hi = hill_results[q][cond][f"{metric}_ci"]
                vals.append(v)
                lo_err.append(max(0, v - ci_lo))
                hi_err.append(max(0, ci_hi - v))
            offset = (ci - (n_cond - 1) / 2) * bar_w
            ax.bar(x + offset, vals, bar_w * 0.9, yerr=[lo_err, hi_err],
                   color=_color(cond), label=cond, capsize=3)

        ax.set_xticks(x)
        ax.set_xticklabels(q_labels)
        ax.set_title(title, fontsize=12)
        ax.set_ylabel("Effective number of species")
        if metric == "alpha":
            ax.legend(fontsize=8)

    fig.suptitle("Hill Numbers — Jost Multiplicative Partition", fontsize=14, y=1.02)
    plt.tight_layout()
    path = os.path.join(output_dir, "hill_numbers_comparison.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


def plot_baselga_decomposition(baselga_results, output_dir):
    """Stacked bar: BC_balanced + BC_gradient per condition."""
    conditions = sorted(baselga_results.keys(),
                        key=lambda c: ["no-AI", "AI-editor", "AI-ideas+editor"].index(c)
                        if c in ["no-AI", "AI-editor", "AI-ideas+editor"] else 99)
    bals = [baselga_results[c]["bc_balanced"] for c in conditions]
    gras = [baselga_results[c]["bc_gradient"] for c in conditions]

    bal_ci = [baselga_results[c]["bc_balanced_ci"] for c in conditions]
    gra_ci = [baselga_results[c]["bc_gradient_ci"] for c in conditions]

    x = np.arange(len(conditions))
    fig, ax = plt.subplots(figsize=(7, 5))

    ax.bar(x, bals, 0.5, label="Balanced variation (turnover-like)", color="#5b9bd5")
    ax.bar(x, gras, 0.5, bottom=bals, label="Abundance gradient (nestedness-like)", color="#ed7d31")

    # error bars on each component (clip to non-negative)
    for i in range(len(conditions)):
        ax.errorbar(x[i], bals[i],
                     yerr=[[max(0, bals[i] - bal_ci[i][0])], [max(0, bal_ci[i][1] - bals[i])]],
                     color="black", capsize=4, fmt="none")
        ax.errorbar(x[i], bals[i] + gras[i],
                     yerr=[[max(0, gras[i] - gra_ci[i][0])], [max(0, gra_ci[i][1] - gras[i])]],
                     color="black", capsize=4, fmt="none")

    ax.set_xticks(x)
    ax.set_xticklabels(conditions, fontsize=10)
    ax.set_ylabel("Bray-Curtis dissimilarity")
    ax.set_title("Baselga Abundance-Based Beta Decomposition", fontsize=13)
    ax.legend(fontsize=9)
    plt.tight_layout()
    path = os.path.join(output_dir, "baselga_decomposition.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


def plot_cosine_heatmap(sim_matrix, labels, output_dir):
    """Heatmap of pairwise cosine similarity, sorted by condition."""
    order = sorted(range(len(labels)),
                   key=lambda i: (["no-AI", "AI-editor", "AI-ideas+editor"].index(labels[i])
                                  if labels[i] in ["no-AI", "AI-editor", "AI-ideas+editor"] else 99, i))
    sorted_labels = [labels[i] for i in order]
    sorted_sim = sim_matrix[np.ix_(order, order)]

    fig, ax = plt.subplots(figsize=(8, 7))
    im = ax.imshow(sorted_sim, cmap="YlOrRd", vmin=0, vmax=1, aspect="auto")
    fig.colorbar(im, ax=ax, label="Cosine similarity")

    # condition boundary lines
    prev = sorted_labels[0]
    for i, lb in enumerate(sorted_labels):
        if lb != prev:
            ax.axhline(i - 0.5, color="white", linewidth=1.5)
            ax.axvline(i - 0.5, color="white", linewidth=1.5)
            prev = lb

    ax.set_title("Pairwise Cosine Similarity (TF-IDF)", fontsize=13)
    ax.set_xlabel("Stories (sorted by condition)")
    ax.set_ylabel("Stories (sorted by condition)")

    # legend-like text
    cond_starts = {}
    for i, lb in enumerate(sorted_labels):
        if lb not in cond_starts:
            cond_starts[lb] = i
    for lb, start in cond_starts.items():
        count = sorted_labels.count(lb)
        ax.text(start + count / 2, -2, lb, ha="center", fontsize=8, fontweight="bold")

    plt.tight_layout()
    path = os.path.join(output_dir, "cosine_similarity_heatmap.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


def plot_rarefaction(original, rarefied, output_dir):
    """Side-by-side: original vs rarefied Hill numbers."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    metrics = ["alpha", "gamma", "beta"]
    titles = [r"$\alpha$ (rarefied)", r"$\gamma$ (rarefied)", r"$\beta$ (rarefied)"]

    conditions = sorted(
        set(list(original["q0"].keys())) & set(list(rarefied["q0"].keys())),
        key=lambda c: ["no-AI", "AI-editor", "AI-ideas+editor"].index(c)
        if c in ["no-AI", "AI-editor", "AI-ideas+editor"] else 99
    )
    q_labels = ["q=0", "q=1", "q=2"]

    for ax, metric, title in zip(axes, metrics, titles):
        n_cond = len(conditions)
        bar_w = 0.35 / n_cond
        x = np.arange(len(q_labels))

        for ci, cond in enumerate(conditions):
            orig_vals, rare_vals = [], []
            for q in ["q0", "q1", "q2"]:
                orig_vals.append(original[q][cond][metric])
                rare_vals.append(rarefied[q][cond][metric])
            offset = (ci - (n_cond - 1) / 2) * bar_w * 2.5
            ax.bar(x + offset - bar_w * 0.55, orig_vals, bar_w,
                   color=_color(cond), alpha=0.4, edgecolor=_color(cond))
            ax.bar(x + offset + bar_w * 0.55, rare_vals, bar_w,
                   color=_color(cond), alpha=1.0, label=cond if metric == "alpha" else None)

        ax.set_xticks(x)
        ax.set_xticklabels(q_labels)
        ax.set_title(title, fontsize=12)
        ax.set_ylabel("Effective number of species")
        if metric == "alpha":
            ax.legend(fontsize=8, title="solid=rarefied, faint=original")

    min_wc = rarefied.get("min_word_count", "?")
    fig.suptitle(f"Rarefaction Sensitivity Check (rarefied to {min_wc} words)", fontsize=14, y=1.02)
    plt.tight_layout()
    path = os.path.join(output_dir, "rarefaction_curves.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


def plot_multi_cutoff_rarefaction(multi_cutoff_results, output_dir):
    """Line plot: alpha and beta trends across cutoff sizes for each condition."""
    cutoffs_sorted = sorted(multi_cutoff_results.keys(), key=int)
    cutoff_vals = [int(c) for c in cutoffs_sorted]

    conditions = None
    for c in cutoffs_sorted:
        conditions = sorted(
            multi_cutoff_results[c]["q1"].keys(),
            key=lambda x: ["no-AI", "AI-editor", "AI-ideas+editor"].index(x)
            if x in ["no-AI", "AI-editor", "AI-ideas+editor"] else 99
        )
        break

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    for qi, q in enumerate(["q0", "q1", "q2"]):
        ax_a = axes[0, qi]
        ax_b = axes[1, qi]

        for cond in conditions:
            alphas, betas = [], []
            a_lo, a_hi, b_lo, b_hi = [], [], [], []
            valid_cutoffs = []
            for c in cutoffs_sorted:
                r = multi_cutoff_results[c][q].get(cond, {})
                a = r.get("alpha", float("nan"))
                b = r.get("beta", float("nan"))
                if np.isnan(a):
                    continue
                valid_cutoffs.append(int(c))
                alphas.append(a)
                betas.append(b)
                aci = r.get("alpha_ci", [a, a])
                bci = r.get("beta_ci", [b, b])
                a_lo.append(aci[0]); a_hi.append(aci[1])
                b_lo.append(bci[0]); b_hi.append(bci[1])

            color = _color(cond)
            ax_a.plot(valid_cutoffs, alphas, "o-", color=color, label=cond, markersize=4)
            ax_a.fill_between(valid_cutoffs, a_lo, a_hi, color=color, alpha=0.15)
            ax_b.plot(valid_cutoffs, betas, "o-", color=color, label=cond, markersize=4)
            ax_b.fill_between(valid_cutoffs, b_lo, b_hi, color=color, alpha=0.15)

        ax_a.set_title(f"α diversity ({q})", fontsize=11)
        ax_b.set_title(f"β diversity ({q})", fontsize=11)
        ax_b.set_xlabel("Rarefaction cutoff (words)")
        if qi == 0:
            ax_a.set_ylabel("Effective species")
            ax_b.set_ylabel("β = γ/α")
            ax_a.legend(fontsize=7)

    fig.suptitle("Multi-Cutoff Rarefaction Sensitivity", fontsize=14, y=1.01)
    plt.tight_layout()
    path = os.path.join(output_dir, "multi_cutoff_rarefaction.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")
