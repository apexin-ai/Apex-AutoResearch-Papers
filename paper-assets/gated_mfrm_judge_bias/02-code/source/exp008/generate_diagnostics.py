#!/usr/bin/env python3
"""Generate exp-003b MCMC diagnostic plots for paper appendix.

Outputs: trace plots, forest plots, (PPC if available)
All PDFs saved to artifacts/exp003b_diagnostics/
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import os
import arviz as az

# ─── Config ───
NC_PATH = "/root/gated_mfrm_judge_bias/exp003/output_003b/joint_gmfrm_idata.nc"
OUT_DIR = "/root/gated_mfrm_judge_bias/artifacts/exp003b_diagnostics"

MODEL_NAMES = [
    "gemma-2-9b", "gpt-3.5-turbo-0125", "gpt-4-0613", "gpt-4o",
    "gpt-4o-mini", "llama-3.3-70b", "qwen2.5-72b", "qwen3-8b",
]
JUDGE_NAMES = [
    "claude-opus-4.7-proxy", "claude-sonnet-4.6-proxy", "deepseek-v4-pro-proxy",
    "gemini-2.5-pro-proxy", "gpt-5.5-proxy", "llama-3.3-70b",
    "mistral-large-2", "qwen2.5-72b", "qwen3-235b-proxy",
]
THETA_SELECT = ["gpt-4o", "qwen2.5-72b", "gpt-3.5-turbo-0125", "gemma-2-9b"]
N_B_SELECT = 6
CHAIN_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]


def setup_style():
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update({
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 9,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })


def trace_plot(samples, names, suptitle, filename):
    """Trace + marginal density plot.

    samples: (n_chains, n_draws, n_params) or (n_chains, n_draws)
    """
    if samples.ndim == 2:
        samples = samples[:, :, np.newaxis]
    if isinstance(names, str):
        names = [names]

    n_chains, n_draws, n_params = samples.shape
    fig, axes = plt.subplots(
        n_params, 2, figsize=(13, 2.6 * n_params + 0.8),
        squeeze=False, gridspec_kw={"width_ratios": [3.5, 1]},
    )

    for i in range(n_params):
        ax_t, ax_d = axes[i]
        for ch in range(n_chains):
            vals = samples[ch, :, i]
            ax_t.plot(vals, alpha=0.45, lw=0.25, color=CHAIN_COLORS[ch],
                      rasterized=True)
            ax_d.hist(vals, bins=60, alpha=0.3, density=True,
                      color=CHAIN_COLORS[ch], orientation="horizontal")
            from scipy.stats import gaussian_kde
            try:
                kde = gaussian_kde(vals)
                grid = np.linspace(vals.min(), vals.max(), 200)
                ax_d.plot(kde(grid), grid, color=CHAIN_COLORS[ch],
                          lw=1.0, alpha=0.8)
            except Exception:
                pass

        ax_t.set_ylabel(names[i], fontsize=9)
        ax_d.set_ylabel("")
        ax_d.tick_params(labelleft=False)

        if i == 0:
            handles = [plt.Line2D([0], [0], color=c, lw=1.5)
                       for c in CHAIN_COLORS[:n_chains]]
            ax_t.legend(handles, [f"Chain {c}" for c in range(n_chains)],
                        fontsize=7, ncol=4, loc="upper right",
                        framealpha=0.7)
        if i < n_params - 1:
            ax_t.tick_params(labelbottom=False)
        else:
            ax_t.set_xlabel("Draw", fontsize=9)

    fig.suptitle(suptitle, fontsize=13, fontweight="bold", y=1.005)
    fig.tight_layout()
    _save(fig, filename)


def forest_plot(samples, names, suptitle, filename, hdi_prob=0.94):
    """Forest plot with HDI bars and posterior means.

    samples: (n_chains, n_draws, n_params)
    """
    n_params = len(names)
    flat = samples.reshape(-1, n_params)

    means = flat.mean(axis=0)
    alpha = 1 - hdi_prob
    lo = np.percentile(flat, 100 * alpha / 2, axis=0)
    hi = np.percentile(flat, 100 * (1 - alpha / 2), axis=0)

    order = np.argsort(means)

    fig, ax = plt.subplots(figsize=(8, max(0.45 * n_params + 1.2, 3.5)))
    y_pos = np.arange(n_params)

    for rank, orig_idx in enumerate(order):
        ax.plot([lo[orig_idx], hi[orig_idx]], [rank, rank],
                color="#4878d0", lw=2.8, solid_capstyle="round", alpha=0.85)
        ax.plot(means[orig_idx], rank, "o", color="#222222",
                markersize=4.5, zorder=5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([names[i] for i in order], fontsize=9)
    ax.set_xlabel("Posterior estimate", fontsize=10)
    ax.axvline(0, color="gray", ls="--", lw=0.8, alpha=0.5)
    ax.set_title(f"{suptitle}\n(● = mean, bar = {int(hdi_prob*100)}% CI)",
                 fontsize=11, fontweight="bold")
    ax.margins(y=0.06)
    fig.tight_layout()
    _save(fig, filename)


def _save(fig, filename):
    path = os.path.join(OUT_DIR, filename)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    kb = os.path.getsize(path) / 1024
    print(f"  {filename}: {kb:.1f} KB")


# ─── Main ───
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    setup_style()

    print("Loading InferenceData...")
    raw = az.from_netcdf(NC_PATH)
    post = raw["posterior"].ds
    print(f"  Posterior vars: {list(post.data_vars)}")
    print(f"  Chains={post.sizes['chain']}, Draws={post.sizes['draw']}")

    c = post["c"].values              # (4, 4000, 8)
    d = post["d"].values              # (4, 4000, 9)
    theta = post["theta"].values      # (4, 4000, 8)
    b = post["b"].values              # (4, 4000, 176)
    sigma_c = post["sigma_c"].values  # (4, 4000)

    # Select representative b items (2 low, 2 mid, 2 high difficulty)
    b_mean = b.mean(axis=(0, 1))
    order = np.argsort(b_mean)
    n_b = len(order)
    b_idx = np.concatenate([
        order[:2],
        order[n_b // 2 - 1 : n_b // 2 + 1],
        order[-2:],
    ])
    b_names = [f"item {i} ($\\bar{{b}}$={b_mean[i]:.2f})" for i in b_idx]

    # Theta subset
    theta_idx = [MODEL_NAMES.index(m) for m in THETA_SELECT]

    # ── Trace plots ──
    print("\n=== Trace Plots ===")
    trace_plot(c, MODEL_NAMES,
               r"$c_n$ (contamination level)", "trace_cn.pdf")
    trace_plot(d, JUDGE_NAMES,
               r"$d_j$ (judge severity)", "trace_dj.pdf")
    trace_plot(sigma_c, r"$\sigma_c$",
               r"$\sigma_c$ (contamination spread)", "trace_sigma_c.pdf")
    trace_plot(theta[:, :, theta_idx], THETA_SELECT,
               r"$\theta_n$ (model ability — selected)", "trace_theta.pdf")
    trace_plot(b[:, :, b_idx], b_names,
               r"$b_i$ (item difficulty — selected)", "trace_b.pdf")

    # ── PPC ──
    print("\n=== Posterior Predictive Check ===")
    if "posterior_predictive" in raw.children:
        print("  posterior_predictive found — generating PPC plot")
        pp = raw["posterior_predictive"].ds
        obs = raw["observed_data"].ds["obs"].values
        pp_var = list(pp.data_vars)[0]
        pp_samples = pp[pp_var].values.reshape(-1, obs.shape[0])
        fig, ax = plt.subplots(figsize=(10, 5))
        for i in range(min(100, pp_samples.shape[0])):
            ax.hist(pp_samples[i], bins=50, alpha=0.02, density=True,
                    color="#4878d0", histtype="step")
        ax.hist(obs, bins=50, density=True, color="#d62728", lw=2,
                histtype="step", label="Observed")
        ax.legend(fontsize=10)
        ax.set_title("Posterior Predictive Check", fontsize=12, fontweight="bold")
        ax.set_xlabel("Score")
        fig.tight_layout()
        _save(fig, "ppc.pdf")
    else:
        print("  SKIPPED: no posterior_predictive group in InferenceData")

    # ── Forest plots ──
    print("\n=== Forest Plots ===")
    forest_plot(c, MODEL_NAMES,
                r"$c_n$ (contamination level)", "forest_cn.pdf")
    forest_plot(d, JUDGE_NAMES,
                r"$d_j$ (judge severity)", "forest_dj.pdf")

    # ── Summary ──
    print("\n=== All output files ===")
    total = 0
    for f in sorted(os.listdir(OUT_DIR)):
        sz = os.path.getsize(os.path.join(OUT_DIR, f))
        total += sz
        print(f"  {f}: {sz/1024:.1f} KB")
    print(f"  TOTAL: {total/1024:.1f} KB")


if __name__ == "__main__":
    main()
