#!/usr/bin/env python3
"""
exp-003b Analysis: Full posterior diagnostics for G-MFRM (HalfNormal prior).

Usage:
  python analyze_003b.py                              # analyze saved results
  python analyze_003b.py --refit                      # re-run MCMC for full posterior
  python analyze_003b.py --output-dir /path/to/dir    # custom output dir

Reads from:  output_003b/ (or --output-dir)
Writes to:   output_003b/analysis/
"""

import argparse
import json
import os
import sys
import warnings
from pathlib import Path

os.environ.setdefault("JAX_PLATFORMS", "cuda,cpu")
os.environ.setdefault("XLA_PYTHON_CLIENT_PREALLOCATE", "false")
os.environ.setdefault("XLA_PYTHON_CLIENT_MEM_FRACTION", "0.25")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import kendalltau, spearmanr

try:
    import arviz as az
    HAS_ARVIZ = True
except ImportError:
    HAS_ARVIZ = False
    warnings.warn("arviz not installed — convergence diagnostics will be limited")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path("/root/gated_mfrm_judge_bias")
EXP003_DIR = PROJECT_ROOT / "exp003"
DEFAULT_OUTPUT_DIR = EXP003_DIR / "output_003b"

MODEL_NAMES = [
    "gemma-2-9b", "gpt-3.5-turbo-0125", "gpt-4-0613", "gpt-4o",
    "gpt-4o-mini", "llama-3.3-70b", "qwen2.5-72b", "qwen3-8b",
]
JUDGE_NAMES = [
    "claude-opus-4.7-proxy", "claude-sonnet-4.6-proxy", "deepseek-v4-pro-proxy",
    "gemini-2.5-pro-proxy", "gpt-5.5-proxy", "llama-3.3-70b",
    "mistral-large-2", "qwen2.5-72b", "qwen3-235b-proxy",
]
ARENA_ELO = {
    "gpt-3.5-turbo-0125": 1105,
    "gpt-4-0613": 1163,
    "gemma-2-9b": 1130,
    "qwen3-8b": 1170,
    "llama-3.3-70b": 1208,
    "qwen2.5-72b": 1187,
    "gpt-4o": 1286,
    "gpt-4o-mini": 1272,
}
EXP003_BASELINES = {
    "raw_average":  {"kendall_tau": 0.786, "spearman_rho": 0.905},
    "mfrm_only":    {"kendall_tau": 0.786, "spearman_rho": 0.905},
    "sequential":   {"kendall_tau": 0.786, "spearman_rho": 0.905},
    "joint_gmfrm (horseshoe)": {"kendall_tau": 0.857, "spearman_rho": 0.952},
}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_inference_data(output_dir: Path):
    """Load ArviZ InferenceData from NetCDF / pickle / npz."""
    nc_path = output_dir / "joint_gmfrm_idata.nc"
    if nc_path.exists() and HAS_ARVIZ:
        print(f"  Loading InferenceData: {nc_path}")
        return az.from_netcdf(str(nc_path))

    pkl_path = output_dir / "mcmc_samples.pkl"
    if pkl_path.exists():
        import pickle
        print(f"  Loading pickled samples: {pkl_path}")
        with open(pkl_path, "rb") as f:
            data = pickle.load(f)
        if HAS_ARVIZ and isinstance(data, dict):
            return az.from_dict(data)
        return data

    npz_path = output_dir / "mcmc_samples.npz"
    if npz_path.exists():
        print(f"  Loading npz samples: {npz_path}")
        data = dict(np.load(str(npz_path), allow_pickle=True))
        if HAS_ARVIZ:
            return az.from_dict(data)
        return data

    return None


def load_point_estimates(output_dir: Path):
    """Load .npy point estimates + results.json."""
    result = {}
    for name in ["joint_gmfrm_theta", "joint_gmfrm_c"]:
        p = output_dir / f"{name}.npy"
        if p.exists():
            key = "theta_hat" if "theta" in name else "c_hat"
            result[key] = np.load(str(p))

    rj = output_dir / "results.json"
    if rj.exists():
        with open(rj) as f:
            result["report"] = json.load(f)

    return result


def refit_mcmc(output_dir, warmup, samples, chains, target_accept, seed):
    """Re-run G-MFRM MCMC and return InferenceData."""
    print("  Re-fitting G-MFRM (this takes a while)...")
    import jax
    import jax.numpy as jnp
    import numpyro

    sys.path.insert(0, str(EXP003_DIR))
    from data_loader import load_data
    from models import _gmfrm_model, _run_mcmc

    data = load_data(
        str(PROJECT_ROOT / "exp001" / "results"),
        str(PROJECT_ROOT / "exp002" / "results" / "exposure_scores.csv"),
    )

    mcmc = _run_mcmc(
        _gmfrm_model, jax.random.PRNGKey(seed),
        dict(
            model_idx=jnp.array(data["model_idx"]),
            item_idx=jnp.array(data["item_idx"]),
            judge_idx=jnp.array(data["judge_idx"]),
            y=jnp.array(data["y"]),
            e=jnp.array(data["e_i"], dtype=jnp.float32),
            N=data["N"], I=data["I"], J=data["J"],
        ),
        warmup, samples, chains, target_accept,
    )

    idata = az.from_numpyro(mcmc)
    nc_path = output_dir / "joint_gmfrm_idata.nc"
    idata.to_netcdf(str(nc_path))
    print(f"  Saved InferenceData: {nc_path}")
    return idata


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _c_key(posterior):
    """Resolve the contamination parameter name (c vs c_n)."""
    for k in ("c", "c_n"):
        if k in posterior:
            return k
    return None


def _get_posterior_array(idata, key):
    """Return [total_samples, dim] from InferenceData."""
    if idata is None or not hasattr(idata, "posterior"):
        return None
    if key not in idata.posterior:
        return None
    arr = idata.posterior[key].values          # [chains, draws, ...]
    return arr.reshape(-1, *arr.shape[2:])     # [total, ...]


# ---------------------------------------------------------------------------
# 1. Convergence diagnostics
# ---------------------------------------------------------------------------

def convergence_diagnostics(idata, point_est):
    diag = {}
    if idata is not None and HAS_ARVIZ and hasattr(idata, "posterior"):
        print("\n  R-hat / ESS (rank-normalized split-R-hat, Vehtari et al. 2021)")
        target_vars = [v for v in ["theta", "c", "c_n", "sigma_c", "d"]
                       if v in idata.posterior]
        summary = az.summary(idata, var_names=target_vars, kind="diagnostics")

        for vn in target_vars:
            rows = [r for r in summary.index if r.startswith(vn)]
            if not rows:
                continue
            rh = summary.loc[rows, "r_hat"]
            eb = summary.loc[rows, "ess_bulk"]
            et = summary.loc[rows, "ess_tail"]
            ok = bool((rh < 1.01).all())
            diag.setdefault("rhat", {})[vn] = {
                "max": float(rh.max()), "mean": float(rh.mean()),
                "all_below_1.01": ok,
            }
            diag.setdefault("ess_bulk", {})[vn] = {
                "min": float(eb.min()), "median": float(eb.median()),
            }
            diag.setdefault("ess_tail", {})[vn] = {
                "min": float(et.min()), "median": float(et.median()),
            }
            mark = "OK" if ok else "WARN"
            print(f"    {vn:10s}  R-hat max={rh.max():.4f} [{mark}]  "
                  f"ESS_bulk min={eb.min():.0f}  ESS_tail min={et.min():.0f}")

        # Divergent transitions
        if "diverging" in idata.sample_stats:
            dv = idata.sample_stats["diverging"]
            n_div = int(dv.sum().values)
            n_tot = int(np.prod(dv.shape))
            diag["divergences"] = {"count": n_div, "total": n_tot,
                                   "pct": round(n_div / n_tot * 100, 3)}
            print(f"\n  Divergent transitions: {n_div}/{n_tot} ({diag['divergences']['pct']:.3f}%)")

        # Max tree-depth (num_steps = 2^depth - 1; NUTS default max = 1023)
        if "num_steps" in idata.sample_stats:
            ns = idata.sample_stats["num_steps"]
            n_max = int((ns >= 1023).sum().values)
            n_tot = int(np.prod(ns.shape))
            diag["max_tree_depth"] = {
                "max_num_steps": int(ns.max().values),
                "hit_1023_count": n_max,
                "hit_1023_pct": round(n_max / n_tot * 100, 2),
                "total": n_tot,
            }
            print(f"  Max tree-depth hits (1023 steps): {n_max}/{n_tot} "
                  f"({diag['max_tree_depth']['hit_1023_pct']:.2f}%)")
    else:
        # Fallback: results.json
        rpt = (point_est or {}).get("report", {})
        jg = rpt.get("convergence", {}).get("joint_gmfrm", {})
        diag["rhat"] = {"overall_max": jg.get("r_hat", float("nan"))}
        diag["ess_bulk"] = {"overall_min": jg.get("ess", float("nan"))}
        diag["divergences"] = {"count": jg.get("divergences", 0)}
        print(f"  (from results.json — per-param breakdown unavailable)")
        print(f"    R-hat max : {jg.get('r_hat', 'N/A')}")
        print(f"    ESS min   : {jg.get('ess', 'N/A')}")
        print(f"    Divergences: {jg.get('divergences', 'N/A')}")
        print(f"\n  For full diagnostics, re-run with: python analyze_003b.py --refit")

    return diag


# ---------------------------------------------------------------------------
# 2. Arena correlation
# ---------------------------------------------------------------------------

def arena_correlation(theta_hat, model_names):
    matched = [(i, m) for i, m in enumerate(model_names) if m in ARENA_ELO]
    if len(matched) < 3:
        print(f"  Only {len(matched)} models matched Arena — skipping.")
        return {}

    idx = [i for i, _ in matched]
    names = [m for _, m in matched]
    theta = theta_hat[idx]
    elo = np.array([ARENA_ELO[m] for m in names])

    tau, tau_p = kendalltau(theta, elo)
    rho, rho_p = spearmanr(theta, elo)

    result = {"kendall_tau": round(float(tau), 4),
              "kendall_p": round(float(tau_p), 4),
              "spearman_rho": round(float(rho), 4),
              "spearman_p": round(float(rho_p), 4),
              "n_matched": len(matched), "matched_models": names}

    print(f"  Kendall  tau = {tau:.4f}  (p={tau_p:.4f})")
    print(f"  Spearman rho = {rho:.4f}  (p={rho_p:.4f})")
    print(f"  N matched    = {len(matched)}")

    print(f"\n  vs exp-003 baselines:")
    print(f"    {'method':<28s}  {'tau':>7s}  {'rho':>7s}")
    print(f"    {'─'*28}  {'─'*7}  {'─'*7}")
    for m, b in EXP003_BASELINES.items():
        print(f"    {m:<28s}  {b['kendall_tau']:>7.3f}  {b['spearman_rho']:>7.3f}")
    print(f"    {'─'*28}  {'─'*7}  {'─'*7}")
    print(f"    {'003b (HalfNormal)':<28s}  {tau:>7.3f}  {rho:>7.3f}")

    return result


# ---------------------------------------------------------------------------
# 3. Parameter extraction
# ---------------------------------------------------------------------------

def extract_parameters(idata, point_est, model_names, judge_names):
    params = {}
    full = idata is not None and HAS_ARVIZ and hasattr(idata, "posterior")

    # θ
    if full and "theta" in idata.posterior:
        arr = _get_posterior_array(idata, "theta")
        mu = arr.mean(0)
        lo = np.percentile(arr, 2.5, axis=0)
        hi = np.percentile(arr, 97.5, axis=0)
        params["theta"] = _param_table(model_names, mu, lo, hi, "model")
        _print_param("theta_n (model ability)", model_names, mu, lo, hi)
    elif point_est and "theta_hat" in point_est:
        mu = point_est["theta_hat"]
        params["theta"] = _param_table(model_names, mu, label="model")
        _print_param("theta_n (point est.)", model_names, mu)

    # c
    ck = _c_key(idata.posterior) if full else None
    if full and ck:
        arr = _get_posterior_array(idata, ck)
        mu = arr.mean(0)
        lo = np.percentile(arr, 2.5, axis=0)
        hi = np.percentile(arr, 97.5, axis=0)
        params["c"] = _param_table(model_names, mu, lo, hi, "model")
        _print_param("c_n (contamination)", model_names, mu, lo, hi)
    elif point_est and "c_hat" in point_est:
        mu = point_est["c_hat"]
        params["c"] = _param_table(model_names, mu, label="model")
        _print_param("c_n (point est.)", model_names, mu)

    # d
    if full and "d" in idata.posterior:
        arr = _get_posterior_array(idata, "d")
        mu = arr.mean(0)
        lo = np.percentile(arr, 2.5, axis=0)
        hi = np.percentile(arr, 97.5, axis=0)
        params["d"] = _param_table(judge_names, mu, lo, hi, "judge")
        _print_param("d_j (judge severity)", judge_names, mu, lo, hi)
    elif point_est and "report" in point_est:
        dv = (point_est["report"].get("parameters", {})
              .get("joint_gmfrm", {}).get("d_values", {}))
        if dv:
            names = list(dv.keys())
            mu = np.array([dv[n] for n in names])
            params["d"] = _param_table(names, mu, label="judge")
            _print_param("d_j (point est.)", names, mu)

    # sigma_c
    if full and "sigma_c" in idata.posterior:
        arr = _get_posterior_array(idata, "sigma_c").flatten()
        mu_s = float(arr.mean())
        lo_s = float(np.percentile(arr, 2.5))
        hi_s = float(np.percentile(arr, 97.5))
        params["sigma_c"] = {"mean": mu_s, "ci_lo": lo_s, "ci_hi": hi_s}
        print(f"\n  sigma_c: {mu_s:.4f} [{lo_s:.4f}, {hi_s:.4f}]")

    return params


def _param_table(names, mu, lo=None, hi=None, label="name"):
    order = np.argsort(-mu)
    rows = []
    for i in order:
        row = {label: names[i], "mean": round(float(mu[i]), 4)}
        if lo is not None:
            row["ci_lo"] = round(float(lo[i]), 4)
            row["ci_hi"] = round(float(hi[i]), 4)
        rows.append(row)
    return rows


def _print_param(title, names, mu, lo=None, hi=None):
    order = np.argsort(-mu)
    has_ci = lo is not None
    print(f"\n  {title}:")
    for i in order:
        if has_ci:
            print(f"    {names[i]:<30s} {mu[i]:>7.3f}  [{lo[i]:>7.3f}, {hi[i]:>7.3f}]")
        else:
            print(f"    {names[i]:<30s} {mu[i]:>7.3f}")


# ---------------------------------------------------------------------------
# 4. Visualizations
# ---------------------------------------------------------------------------

def plot_traces(idata, out, model_names, judge_names):
    if idata is None or not HAS_ARVIZ or not hasattr(idata, "posterior"):
        print("  Trace plots require full MCMC samples — skipped.")
        return
    posterior = idata.posterior
    n_chains = posterior.dims["chain"]

    def _trace_grid(key, names, fname, title):
        if key not in posterior:
            return
        vals = posterior[key].values   # [chains, draws, dim]
        n = vals.shape[-1]
        fig, axes = plt.subplots(n, 2, figsize=(14, max(2.2 * n, 4)),
                                 squeeze=False)
        for i in range(n):
            for ch in range(n_chains):
                axes[i, 0].plot(vals[ch, :, i], alpha=0.55, lw=0.4)
                axes[i, 1].hist(vals[ch, :, i], bins=50, alpha=0.45, density=True)
            axes[i, 0].set_ylabel(names[i] if i < len(names) else str(i),
                                  fontsize=7, rotation=0, ha="right")
            for ax in axes[i]:
                ax.tick_params(labelsize=6)
        axes[0, 0].set_title(f"Trace — {title}", fontsize=10)
        axes[0, 1].set_title("Marginal density", fontsize=10)
        plt.tight_layout()
        plt.savefig(out / fname, dpi=150, bbox_inches="tight")
        plt.close()

    _trace_grid("theta", model_names, "trace_theta.png", "theta (model ability)")

    ck = _c_key(posterior)
    if ck:
        _trace_grid(ck, model_names, "trace_c.png", "c_n (contamination)")

    _trace_grid("d", judge_names, "trace_d.png", "d_j (judge severity)")

    # sigma_c (scalar)
    if "sigma_c" in posterior:
        vals = posterior["sigma_c"].values  # [chains, draws]
        fig, axes = plt.subplots(1, 2, figsize=(12, 3))
        for ch in range(n_chains):
            axes[0].plot(vals[ch], alpha=0.55, lw=0.5, label=f"chain {ch}")
            axes[1].hist(vals[ch], bins=50, alpha=0.45, density=True)
        axes[0].set_title("Trace — sigma_c")
        axes[1].set_title("Marginal density — sigma_c")
        axes[0].legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(out / "trace_sigma_c.png", dpi=150, bbox_inches="tight")
        plt.close()

    print("  Saved: trace_theta.png, trace_c.png, trace_d.png, trace_sigma_c.png")


def plot_posterior_densities(idata, out, model_names, judge_names):
    if idata is None or not HAS_ARVIZ or not hasattr(idata, "posterior"):
        print("  Posterior density plots require full MCMC samples — skipped.")
        return
    posterior = idata.posterior

    ck = _c_key(posterior)
    if ck:
        arr = _get_posterior_array(idata, ck)
        mu = arr.mean(0)
        order = np.argsort(-mu)
        fig, ax = plt.subplots(figsize=(10, 5.5))
        cmap = plt.cm.RdYlGn_r(np.linspace(0.15, 0.85, len(model_names)))
        for rank, i in enumerate(order):
            ax.hist(arr[:, i], bins=80, alpha=0.55, density=True,
                    color=cmap[rank], label=model_names[i])
        ax.set_xlabel("c_n")
        ax.set_ylabel("Density")
        ax.set_title("Posterior of c_n (contamination susceptibility)")
        ax.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(out / "posterior_c.png", dpi=150)
        plt.close()

    if "d" in posterior:
        arr = _get_posterior_array(idata, "d")
        mu = arr.mean(0)
        order = np.argsort(-mu)
        fig, ax = plt.subplots(figsize=(10, 5.5))
        cmap = plt.cm.coolwarm(np.linspace(0.1, 0.9, len(judge_names)))
        for rank, i in enumerate(order):
            ax.hist(arr[:, i], bins=80, alpha=0.55, density=True,
                    color=cmap[rank], label=judge_names[i])
        ax.set_xlabel("d_j")
        ax.set_ylabel("Density")
        ax.set_title("Posterior of d_j (judge severity)")
        ax.legend(fontsize=7)
        plt.tight_layout()
        plt.savefig(out / "posterior_d.png", dpi=150)
        plt.close()

    print("  Saved: posterior_c.png, posterior_d.png")


def plot_theta_vs_elo(theta_hat, model_names, out, theta_ci=None):
    matched = [(i, m) for i, m in enumerate(model_names) if m in ARENA_ELO]
    if len(matched) < 3:
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    for i, name in matched:
        elo = ARENA_ELO[name]
        if theta_ci is not None:
            ax.errorbar(elo, theta_hat[i],
                        yerr=[[theta_hat[i] - theta_ci[i, 0]],
                              [theta_ci[i, 1] - theta_hat[i]]],
                        fmt="o", capsize=4, capthick=1.5, ms=8, zorder=5)
        else:
            ax.scatter(elo, theta_hat[i], s=80, zorder=5)
        ax.annotate(name, (elo, theta_hat[i]),
                    textcoords="offset points", xytext=(6, 6), fontsize=8)

    elo_arr = np.array([ARENA_ELO[m] for _, m in matched])
    th_arr = theta_hat[[i for i, _ in matched]]
    z = np.polyfit(elo_arr, th_arr, 1)
    xs = np.linspace(elo_arr.min() - 20, elo_arr.max() + 20, 100)
    ax.plot(xs, np.polyval(z, xs), "--", alpha=0.4, color="gray")

    ax.set_xlabel("Arena Elo")
    ax.set_ylabel("theta (G-MFRM ability)")
    ax.set_title("theta vs Arena Elo (exp-003b, HalfNormal prior)")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out / "theta_vs_elo.png", dpi=150)
    plt.close()
    print("  Saved: theta_vs_elo.png")


def plot_c_bar(c_hat, model_names, out, c_ci=None):
    order = np.argsort(-c_hat)
    names_s = [model_names[i] for i in order]
    c_s = c_hat[order]

    fig, ax = plt.subplots(figsize=(10, 5))
    cmap = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(model_names)))
    ax.bar(range(len(c_s)), c_s, color=cmap)

    if c_ci is not None:
        ci_s = c_ci[order]
        yerr = np.array([c_s - ci_s[:, 0], ci_s[:, 1] - c_s])
        ax.errorbar(range(len(c_s)), c_s, yerr=yerr,
                    fmt="none", capsize=4, capthick=1.5, color="black")

    ax.set_xticks(range(len(c_s)))
    ax.set_xticklabels(names_s, rotation=45, ha="right", fontsize=9)
    ax.set_ylabel("c_n (contamination susceptibility)")
    ax.set_title("Contamination Susceptibility Ranking (exp-003b)")
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(out / "c_ranking.png", dpi=150)
    plt.close()
    print("  Saved: c_ranking.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="exp-003b analysis: full G-MFRM posterior diagnostics")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--refit", action="store_true",
                        help="Re-run MCMC for full posterior (~2h on GPU)")
    parser.add_argument("--warmup", type=int, default=4000)
    parser.add_argument("--samples", type=int, default=4000)
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--target-accept", type=float, default=0.95)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    analysis_dir = output_dir / "analysis"
    analysis_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("exp-003b Analysis — G-MFRM (HalfNormal prior)")
    print("=" * 60)
    print(f"  Output dir  : {output_dir}")
    print(f"  Analysis dir: {analysis_dir}")

    # ── Check availability ──
    has_results = ((output_dir / "results.json").exists() or
                   (output_dir / "joint_gmfrm_theta.npy").exists())
    has_idata = (output_dir / "joint_gmfrm_idata.nc").exists()

    if not has_results and not has_idata and not args.refit:
        print(f"\n  No results found in {output_dir}.")
        print("  Waiting for exp-003b to complete. Check progress:")
        print("    tail -1 /tmp/exp003b.log")
        sys.exit(1)

    # ── Step 1: Load ──
    hdr("Loading data")
    idata = None
    point_est = None

    if args.refit:
        assert HAS_ARVIZ, "arviz required for --refit"
        idata = refit_mcmc(output_dir, args.warmup, args.samples,
                           args.chains, args.target_accept, args.seed)
    else:
        idata = load_inference_data(output_dir)
        point_est = load_point_estimates(output_dir)

    full = idata is not None and HAS_ARVIZ and hasattr(idata, "posterior")
    mode = "full" if full else "partial"
    if full:
        print("  Full posterior samples loaded.")
    else:
        print("  Point estimates only — some diagnostics unavailable.")
        print("  To get full posterior, run:  python analyze_003b.py --refit")

    # Resolve names from report if possible
    rpt = (point_est or {}).get("report", {}).get("data_summary", {})
    model_names = rpt.get("model_names", MODEL_NAMES)
    judge_names = rpt.get("judge_names", JUDGE_NAMES)

    # ── Step 2: Convergence ──
    hdr("Convergence Diagnostics")
    diag = convergence_diagnostics(idata, point_est)

    # ── Step 3: Extract theta / c ──
    theta_hat, theta_ci = _extract_vec(idata, "theta", point_est, "theta_hat",
                                       len(model_names))
    ck = _c_key(idata.posterior) if full else None
    c_hat, c_ci = _extract_vec(idata, ck, point_est, "c_hat",
                               len(model_names))

    # ── Step 4: Arena correlation ──
    hdr("Arena Elo Correlation")
    arena = arena_correlation(theta_hat, model_names) if theta_hat is not None else {}

    # ── Step 5: Parameter profiles ──
    hdr("Parameter Profiles")
    params = extract_parameters(idata, point_est, model_names, judge_names)

    # ── Step 6: Plots ──
    hdr("Visualizations")
    plot_traces(idata, analysis_dir, model_names, judge_names)
    plot_posterior_densities(idata, analysis_dir, model_names, judge_names)
    if theta_hat is not None:
        plot_theta_vs_elo(theta_hat, model_names, analysis_dir, theta_ci)
    if c_hat is not None:
        plot_c_bar(c_hat, model_names, analysis_dir, c_ci)

    # ── Step 7: Save summary ──
    hdr("Summary")
    summary = {
        "experiment": "exp-003b",
        "model": "G-MFRM (HalfNormal prior)",
        "mcmc_config": {"warmup": 4000, "samples": 4000,
                        "chains": 4, "target_accept": 0.95},
        "analysis_mode": mode,
        "convergence": _jsonable(diag),
        "arena_correlation": arena,
        "parameters": _jsonable(params),
        "exp003_baselines": EXP003_BASELINES,
    }
    spath = analysis_dir / "summary.json"
    with open(spath, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"  Saved: {spath}")

    # Final console summary
    print(f"\n  Mode: {mode}")
    if "rhat" in diag:
        rh = diag["rhat"]
        if isinstance(rh, dict) and any(isinstance(v, dict) for v in rh.values()):
            max_rh = max(v.get("max", 0) for v in rh.values() if isinstance(v, dict))
            print(f"  R-hat max: {max_rh:.4f}")
    if arena:
        print(f"  Arena tau={arena['kendall_tau']:.3f}, rho={arena['spearman_rho']:.3f}")
    n_plots = len(list(analysis_dir.glob("*.png")))
    print(f"  Plots: {n_plots} PNGs in {analysis_dir}")
    print(f"  JSON:  {spath}")


# ── Utilities ──

def hdr(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def _extract_vec(idata, idata_key, point_est, pe_key, n):
    """Return (mean, ci_array_or_None) for a vector parameter."""
    full = (idata is not None and HAS_ARVIZ and hasattr(idata, "posterior")
            and idata_key and idata_key in idata.posterior)
    if full:
        arr = _get_posterior_array(idata, idata_key)
        mu = arr.mean(0)
        ci = np.column_stack([np.percentile(arr, 2.5, axis=0),
                              np.percentile(arr, 97.5, axis=0)])
        return mu, ci
    if point_est and pe_key in point_est:
        return point_est[pe_key], None
    return None, None


def _jsonable(obj):
    """Make nested dicts/arrays JSON-safe."""
    if isinstance(obj, dict):
        return {k: _jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_jsonable(v) for v in obj]
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating, np.float64)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


if __name__ == "__main__":
    main()
