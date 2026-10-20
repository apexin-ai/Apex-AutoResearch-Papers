"""
IRT 2PL+gamma contamination model -- PyMC MCMC fitting.

Model:
  P(y_ij = 1 | theta_j, a_i, b_i, gamma_i, e_j) = sigma(a_i (theta_j - b_i) + gamma_i e_j)

  theta_j: respondent ability          ~ N(0, 1)
  a_i: item discrimination             ~ LogNormal(0, 0.5)  [>0]
  b_i: item difficulty                  ~ N(0, 2)
  gamma_i: item contamination sens.    ~ N(0, 1)
  e_j: respondent exposure score       (known, dosage/100)

  gamma_i > 0 = contamination makes item easier (pro-contamination)

Input:
  analysis/irt_data/{benchmark}/response_matrix.csv   -- J x I binary (respondent col + item cols)
  analysis/irt_data/{benchmark}/exposure_scores.csv    -- J rows: respondent, dosage, exposure
  analysis/irt_data/{benchmark}/item_metadata.csv      -- I rows: item_id, [subject, domain,] difficulty_baseline

Output (in --output-dir):
  gamma_summary.csv           -- posterior mean/hdi for gamma_i
  gamma_histogram.png         -- distribution of gamma_i posterior means
  gamma_by_domain_boxplot.png -- per-domain gamma boxplot (if domain column exists)
  theta_summary.csv           -- respondent ability estimates
  convergence printed to stdout

Dependencies: pymc >= 5.0, arviz, numpy, pandas, matplotlib
"""

import argparse
import os
import sys
import time
import warnings

import arviz as az
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm

warnings.filterwarnings("ignore", category=FutureWarning)

PROJ_ROOT = "/root/contamcal-irt-calibration"
DATA_DIR = os.path.join(PROJ_ROOT, "analysis", "irt_data")

BENCHMARK_MAP = {
    "mmlu": "mmlu",
    "arc": "arc_challenge",
    "arc_challenge": "arc_challenge",
    "gsm8k": "gsm8k",
    "humaneval": "humaneval",
}


def load_data(benchmark, max_items=None, seed=42):
    bench_dir = os.path.join(DATA_DIR, BENCHMARK_MAP.get(benchmark, benchmark))
    if not os.path.isdir(bench_dir):
        sys.exit(f"Data directory not found: {bench_dir}")

    resp_df = pd.read_csv(os.path.join(bench_dir, "response_matrix.csv"))
    expo_df = pd.read_csv(os.path.join(bench_dir, "exposure_scores.csv"))
    meta_df = pd.read_csv(os.path.join(bench_dir, "item_metadata.csv"))

    respondents = resp_df["respondent"].values
    Y = resp_df.drop(columns=["respondent"]).values.astype(np.int8)
    J, I_total = Y.shape

    exposure = expo_df.set_index("respondent").loc[respondents, "exposure"].values.astype(np.float64)

    if max_items is not None and max_items < I_total:
        rng = np.random.default_rng(seed)
        if "domain" in meta_df.columns:
            sampled_idx = _stratified_sample(meta_df, max_items, rng)
        else:
            sampled_idx = rng.choice(I_total, size=max_items, replace=False)
        sampled_idx = np.sort(sampled_idx)
        Y = Y[:, sampled_idx]
        meta_df = meta_df.iloc[sampled_idx].reset_index(drop=True)
        print(f"Subsampled {max_items}/{I_total} items (seed={seed})")
    else:
        sampled_idx = np.arange(I_total)

    print(f"Data: {J} respondents x {Y.shape[1]} items, exposure range [{exposure.min():.2f}, {exposure.max():.2f}]")
    return Y, exposure, respondents, meta_df, sampled_idx


def _stratified_sample(meta_df, n, rng):
    domains = meta_df["domain"].values
    unique_domains = np.unique(domains)
    per_domain = max(1, n // len(unique_domains))
    indices = []
    for d in unique_domains:
        d_idx = np.where(domains == d)[0]
        k = min(per_domain, len(d_idx))
        indices.append(rng.choice(d_idx, size=k, replace=False))
    indices = np.concatenate(indices)
    if len(indices) < n:
        remaining = np.setdiff1d(np.arange(len(meta_df)), indices)
        extra = rng.choice(remaining, size=n - len(indices), replace=False)
        indices = np.concatenate([indices, extra])
    elif len(indices) > n:
        indices = rng.choice(indices, size=n, replace=False)
    return indices


def build_model(Y, exposure):
    J, I = Y.shape
    e_mat = np.tile(exposure[:, None], (1, I))

    with pm.Model() as model:
        theta = pm.Normal("theta", mu=0, sigma=1, shape=J)
        a = pm.LogNormal("a", mu=0, sigma=0.5, shape=I)
        b = pm.Normal("b", mu=0, sigma=2, shape=I)
        gamma = pm.Normal("gamma", mu=0, sigma=1, shape=I)

        eta = a[None, :] * (theta[:, None] - b[None, :]) + gamma[None, :] * e_mat
        pm.Bernoulli("y", logit_p=eta, observed=Y)

    return model


def fit_nuts(model, chains, tune, draws, cores, seed):
    t0 = time.time()
    with model:
        trace = pm.sample(
            draws=draws,
            tune=tune,
            chains=chains,
            cores=cores,
            random_seed=seed,
            target_accept=0.9,
            return_inferencedata=True,
            progressbar=True,
        )
    elapsed = time.time() - t0
    print(f"NUTS sampling done in {elapsed:.0f}s ({elapsed/60:.1f}min)")
    return trace


def fit_advi(model, draws, seed):
    t0 = time.time()
    with model:
        approx = pm.fit(
            n=30000,
            method="advi",
            random_seed=seed,
            progressbar=True,
        )
        trace = approx.sample(draws)
    elapsed = time.time() - t0
    print(f"ADVI fitting done in {elapsed:.0f}s ({elapsed/60:.1f}min)")
    return trace


def diagnostics(trace, method):
    if method == "nuts":
        summary = az.summary(trace, var_names=["gamma", "theta", "a", "b"], kind="diagnostics")
        print(f"\n=== Convergence Diagnostics ===")
        if "r_hat" in summary.columns:
            rhat = summary["r_hat"]
            print(f"R-hat  -- max: {rhat.max():.4f}, mean: {rhat.mean():.4f}, >1.01: {(rhat > 1.01).sum()}")
        if "ess_bulk" in summary.columns:
            ess = summary["ess_bulk"]
            print(f"ESS    -- min: {ess.min():.0f}, median: {ess.median():.0f}")

        if hasattr(trace, "sample_stats"):
            try:
                div = trace.sample_stats["diverging"]
                n_div = int(div.values.sum())
                print(f"Divergences: {n_div}")
            except (KeyError, AttributeError):
                pass
    else:
        print("\n=== ADVI (no MCMC diagnostics) ===")


def extract_gamma_summary(trace, meta_df, method):
    gamma_samples = trace.posterior["gamma"].values
    n_chains, n_draws, n_items = gamma_samples.shape
    flat = gamma_samples.reshape(-1, n_items)

    means = flat.mean(axis=0)
    q03 = np.percentile(flat, 3, axis=0)
    q97 = np.percentile(flat, 97, axis=0)

    result = meta_df.copy()
    result["gamma_mean"] = means
    result["gamma_hdi_3%"] = q03
    result["gamma_hdi_97%"] = q97
    result["gamma_sd"] = flat.std(axis=0)
    result["significant"] = ~((q03 <= 0) & (q97 >= 0))

    n_sig = result["significant"].sum()
    n_pos = ((result["gamma_mean"] > 0) & result["significant"]).sum()
    n_neg = ((result["gamma_mean"] < 0) & result["significant"]).sum()
    print(f"\ngamma summary: {n_items} items, {n_sig} significant (94% CI excludes 0)")
    print(f"  gamma>0 (pro-contamination): {n_pos},  gamma<0 (anti-contamination): {n_neg}")
    print(f"  mean(gamma): {means.mean():.4f}, std(gamma): {means.std():.4f}")
    print(f"  range: [{means.min():.4f}, {means.max():.4f}]")

    return result


def plot_gamma_histogram(gamma_df, output_dir, benchmark):
    fig, ax = plt.subplots(figsize=(8, 5))
    vals = gamma_df["gamma_mean"].values
    ax.hist(vals, bins=50, edgecolor="black", alpha=0.7, color="#4C72B0")
    ax.axvline(0, color="red", linestyle="--", linewidth=1.5, label="gamma=0")
    ax.set_xlabel("gamma (posterior mean)")
    ax.set_ylabel("Count")
    ax.set_title(f"IRT 2PL+gamma -- Item Contamination Sensitivity ({benchmark.upper()})")
    ax.legend()
    plt.tight_layout()
    path = os.path.join(output_dir, "gamma_histogram.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved: {path}")


def plot_gamma_by_domain(gamma_df, output_dir, benchmark):
    if "domain" not in gamma_df.columns:
        print("No domain column -- skipping domain boxplot")
        return
    domains = gamma_df["domain"].unique()
    if len(domains) < 2:
        return

    domain_order = gamma_df.groupby("domain")["gamma_mean"].median().sort_values().index
    fig, ax = plt.subplots(figsize=(10, 6))
    data = [gamma_df.loc[gamma_df["domain"] == d, "gamma_mean"].values for d in domain_order]
    bp = ax.boxplot(data, labels=domain_order, vert=True, patch_artist=True)
    for patch in bp["boxes"]:
        patch.set_facecolor("#A1C9F4")
    ax.axhline(0, color="red", linestyle="--", linewidth=1)
    ax.set_ylabel("gamma (posterior mean)")
    ax.set_xlabel("Domain")
    ax.set_title(f"gamma by Domain ({benchmark.upper()})")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    path = os.path.join(output_dir, "gamma_by_domain_boxplot.png")
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved: {path}")


def main():
    parser = argparse.ArgumentParser(description="Fit IRT 2PL+gamma contamination model via PyMC")
    parser.add_argument("--benchmark", required=True, choices=list(BENCHMARK_MAP.keys()),
                        help="Benchmark name")
    parser.add_argument("--max-items", type=int, default=None,
                        help="Max items to use (subsample if exceeded). Default: all.")
    parser.add_argument("--method", choices=["nuts", "advi"], default="nuts",
                        help="Inference method (default: nuts)")
    parser.add_argument("--chains", type=int, default=4)
    parser.add_argument("--tune", type=int, default=1000)
    parser.add_argument("--draws", type=int, default=2000)
    parser.add_argument("--cores", type=int, default=4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Output directory (default: analysis/irt_results/{benchmark})")
    args = parser.parse_args()

    if args.output_dir is None:
        args.output_dir = os.path.join(PROJ_ROOT, "analysis", "irt_results", args.benchmark)
    os.makedirs(args.output_dir, exist_ok=True)

    Y, exposure, respondents, meta_df, sampled_idx = load_data(
        args.benchmark, args.max_items, args.seed
    )

    print(f"\nBuilding 2PL+gamma model (method={args.method})...")
    model = build_model(Y, exposure)

    if args.method == "nuts":
        trace = fit_nuts(model, args.chains, args.tune, args.draws, args.cores, args.seed)
    else:
        trace = fit_advi(model, args.draws, args.seed)

    diagnostics(trace, args.method)

    gamma_df = extract_gamma_summary(trace, meta_df, args.method)
    csv_path = os.path.join(args.output_dir, "gamma_summary.csv")
    gamma_df.to_csv(csv_path, index=False)
    print(f"Saved: {csv_path}")

    plot_gamma_histogram(gamma_df, args.output_dir, args.benchmark)
    plot_gamma_by_domain(gamma_df, args.output_dir, args.benchmark)

    theta_samples = trace.posterior["theta"].values.reshape(-1, len(respondents))
    theta_df = pd.DataFrame({
        "respondent": respondents,
        "theta_mean": theta_samples.mean(axis=0),
        "theta_sd": theta_samples.std(axis=0),
    })
    theta_path = os.path.join(args.output_dir, "theta_summary.csv")
    theta_df.to_csv(theta_path, index=False)
    print(f"Saved: {theta_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
