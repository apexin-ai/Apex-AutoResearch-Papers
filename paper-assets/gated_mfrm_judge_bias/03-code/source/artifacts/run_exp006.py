"""exp-006: Judge Count Sensitivity Analysis.

Varies judge count (2, 4, 6, 8, 9) and measures how many judges G-MFRM needs
to outperform sequential/baselines on Kendall-τ vs Arena.

Usage:
  python run_exp006.py --judgment-dir /root/gated_mfrm_judge_bias/exp001/results \
                       --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
                       --output-dir /root/gated_mfrm_judge_bias/exp006/results

  python run_exp006.py --dry-run  # validate data loading only
  python run_exp006.py --help

Dependencies: numpy, scipy, pandas, matplotlib, jax, numpyro
"""

import argparse
import json
import itertools
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import kendalltau, spearmanr

sys.path.insert(0, "/root/gated_mfrm_judge_bias/exp003")
from data_loader import load_judgments, preprocess, build_indices, load_exposure


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

JUDGE_COUNTS = [2, 4, 6, 8, 9]
N_SUBSETS_PER_COUNT = 10  # max subsets to sample per judge count
SEED = 42


def compute_arena_tau(theta_dict: dict) -> dict:
    """Kendall-τ and Spearman-ρ with Arena Elo for matched models."""
    matched = [(m, theta_dict[m]) for m in theta_dict if m in ARENA_ELO]
    if len(matched) < 3:
        return {"kendall_tau": float("nan"), "spearman_rho": float("nan"),
                "n_matched": len(matched)}
    models, thetas = zip(*matched)
    elos = [ARENA_ELO[m] for m in models]
    tau, tau_p = kendalltau(thetas, elos)
    rho, rho_p = spearmanr(thetas, elos)
    return {
        "kendall_tau": float(tau),
        "kendall_p": float(tau_p),
        "spearman_rho": float(rho),
        "spearman_p": float(rho_p),
        "n_matched": len(matched),
    }


def load_full_data(judgment_dir: str, exposure_csv: str) -> tuple:
    """Load and preprocess all judgment data, returning observations + metadata."""
    records = load_judgments(judgment_dir)
    observations = preprocess(records)

    all_judges = sorted({o["judge"] for o in observations})
    all_models = sorted({o["model"] for o in observations})
    all_items = sorted({o["item_id"] for o in observations})

    return observations, all_judges, all_models, all_items


def filter_by_judges(observations: list, judge_subset: list) -> list:
    """Filter observations to only include specified judges."""
    judge_set = set(judge_subset)
    return [o for o in observations if o["judge"] in judge_set]


def build_data_dict(filtered_obs: list, exposure_csv: str, min_judges: int = 1) -> dict:
    """Build the data dict expected by G-MFRM fitting functions."""
    from collections import defaultdict

    # Filter items by minimum judge coverage
    judges_per_item = defaultdict(set)
    for o in filtered_obs:
        judges_per_item[o["item_id"]].add(o["judge"])
    valid_items = {item for item, judges in judges_per_item.items()
                   if len(judges) >= min(min_judges, len(set(o["judge"] for o in filtered_obs)))}
    filtered_obs = [o for o in filtered_obs if o["item_id"] in valid_items]

    if not filtered_obs:
        return None

    model_to_idx, item_to_idx, judge_to_idx = build_indices(filtered_obs)
    N = len(model_to_idx)
    I = len(item_to_idx)
    J = len(judge_to_idx)

    model_idx = np.array([model_to_idx[o["model"]] for o in filtered_obs], dtype=np.int32)
    item_idx = np.array([item_to_idx[o["item_id"]] for o in filtered_obs], dtype=np.int32)
    judge_idx = np.array([judge_to_idx[o["judge"]] for o in filtered_obs], dtype=np.int32)
    y = np.array([o["y"] for o in filtered_obs], dtype=np.float32)

    e_i = load_exposure(exposure_csv, item_to_idx)

    model_names = sorted(model_to_idx, key=model_to_idx.get)
    judge_names = sorted(judge_to_idx, key=judge_to_idx.get)

    return {
        "model_idx": model_idx,
        "item_idx": item_idx,
        "judge_idx": judge_idx,
        "y": y,
        "model_names": model_names,
        "judge_names": judge_names,
        "e_i": e_i,
        "N": N,
        "I": I,
        "J": J,
        "n_obs": len(y),
    }


def generate_judge_subsets(all_judges: list, judge_counts: list,
                           n_subsets: int, seed: int) -> dict:
    """Generate judge subsets for each count level.

    For small counts (where C(9,k) <= n_subsets), use all combinations.
    Otherwise, sample randomly.
    """
    rng = np.random.default_rng(seed)
    subsets = {}

    for k in judge_counts:
        if k >= len(all_judges):
            subsets[k] = [list(all_judges)]
            continue

        all_combos = list(itertools.combinations(all_judges, k))
        if len(all_combos) <= n_subsets:
            subsets[k] = [list(c) for c in all_combos]
        else:
            chosen_idx = rng.choice(len(all_combos), size=n_subsets, replace=False)
            subsets[k] = [list(all_combos[i]) for i in chosen_idx]

    return subsets


def fit_raw_average_subset(data: dict) -> dict:
    """Raw average method (no MCMC, always available)."""
    N = data["N"]
    model_idx = data["model_idx"]
    y = data["y"]
    theta_hat = np.zeros(N)
    for n in range(N):
        mask = model_idx == n
        if mask.sum() > 0:
            theta_hat[n] = y[mask].mean()
    theta_hat = theta_hat - theta_hat.mean()
    return {name: float(theta_hat[i]) for i, name in enumerate(data["model_names"])}


def fit_methods_on_subset(data: dict, methods: list) -> dict:
    """Fit specified methods on a judge subset. Returns theta dicts per method."""
    results = {}

    if "raw_average" in methods:
        results["raw_average"] = fit_raw_average_subset(data)

    if "mfrm_only" in methods or "sequential" in methods or "joint_gmfrm" in methods:
        from exp003_models import fit_mfrm_only, fit_sequential, fit_joint_gmfrm

        if "mfrm_only" in methods:
            mfrm = fit_mfrm_only(data, warmup=1000, samples=2000, chains=2)
            results["mfrm_only"] = {
                name: float(mfrm["theta_hat"][i])
                for i, name in enumerate(data["model_names"])
            }

        if "sequential" in methods:
            seq = fit_sequential(data, warmup=1000, samples=2000, chains=2)
            results["sequential"] = {
                name: float(seq["theta_hat"][i])
                for i, name in enumerate(data["model_names"])
            }

        if "joint_gmfrm" in methods:
            joint = fit_joint_gmfrm(data, warmup=1000, samples=2000, chains=2)
            results["joint_gmfrm"] = {
                name: float(joint["theta_hat"][i])
                for i, name in enumerate(data["model_names"])
            }

    return results


def run_sensitivity_analysis(observations: list, all_judges: list,
                             exposure_csv: str, judge_counts: list,
                             n_subsets: int, methods: list, seed: int) -> pd.DataFrame:
    """Run full judge count sensitivity analysis."""
    subsets = generate_judge_subsets(all_judges, judge_counts, n_subsets, seed)

    rows = []
    total = sum(len(v) for v in subsets.values())
    done = 0

    for k in sorted(subsets.keys()):
        print(f"\n  Judge count = {k} ({len(subsets[k])} subsets):")
        for s_idx, judge_subset in enumerate(subsets[k]):
            done += 1
            print(f"    [{done}/{total}] Judges: {judge_subset}")

            filtered = filter_by_judges(observations, judge_subset)
            if not filtered:
                print(f"      SKIP: no observations")
                continue

            data = build_data_dict(filtered, exposure_csv, min_judges=1)
            if data is None:
                print(f"      SKIP: could not build data dict")
                continue

            print(f"      N={data['N']}, I={data['I']}, J={data['J']}, obs={data['n_obs']}")

            t0 = time.time()
            theta_dicts = fit_methods_on_subset(data, methods)
            elapsed = time.time() - t0

            for method, theta_dict in theta_dicts.items():
                corr = compute_arena_tau(theta_dict)
                rows.append({
                    "judge_count": k,
                    "subset_idx": s_idx,
                    "judges": ",".join(sorted(judge_subset)),
                    "method": method,
                    "kendall_tau": corr["kendall_tau"],
                    "spearman_rho": corr["spearman_rho"],
                    "n_matched": corr["n_matched"],
                    "n_obs": data["n_obs"],
                    "elapsed_s": round(elapsed, 1),
                })

            for method, theta_dict in theta_dicts.items():
                corr = compute_arena_tau(theta_dict)
                print(f"      {method}: τ={corr['kendall_tau']:.4f}, ρ={corr['spearman_rho']:.4f}")

    return pd.DataFrame(rows)


def leave_one_judge_out(observations: list, all_judges: list,
                        exposure_csv: str, methods: list) -> pd.DataFrame:
    """Leave-one-judge-out analysis: fit on N-1 judges, measure impact."""
    rows = []

    # Full-judge baseline
    full_data = build_data_dict(observations, exposure_csv)
    if full_data is None:
        return pd.DataFrame()

    full_thetas = fit_methods_on_subset(full_data, methods)
    full_taus = {m: compute_arena_tau(t)["kendall_tau"] for m, t in full_thetas.items()}

    for left_out in all_judges:
        remaining = [j for j in all_judges if j != left_out]
        filtered = filter_by_judges(observations, remaining)
        data = build_data_dict(filtered, exposure_csv)
        if data is None:
            continue

        theta_dicts = fit_methods_on_subset(data, methods)
        for method, theta_dict in theta_dicts.items():
            corr = compute_arena_tau(theta_dict)
            rows.append({
                "left_out_judge": left_out,
                "method": method,
                "kendall_tau": corr["kendall_tau"],
                "tau_delta": corr["kendall_tau"] - full_taus.get(method, 0),
                "spearman_rho": corr["spearman_rho"],
                "n_obs": data["n_obs"],
            })

    return pd.DataFrame(rows)


def plot_tau_vs_judge_count(df: pd.DataFrame, output_dir: Path):
    """Plot Kendall-τ vs judge count for each method."""
    if df.empty:
        print("  No data for tau vs judge count plot")
        return

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = {
        "raw_average": "#9E9E9E",
        "mfrm_only": "#FF9800",
        "sequential": "#4CAF50",
        "joint_gmfrm": "#2196F3",
    }

    for method in df["method"].unique():
        mdf = df[df["method"] == method]
        grouped = mdf.groupby("judge_count")["kendall_tau"]
        means = grouped.mean()
        stds = grouped.std()
        counts = grouped.count()

        ax.errorbar(means.index, means.values,
                    yerr=stds.values, fmt="o-",
                    color=colors.get(method, "gray"),
                    label=method, capsize=4, markersize=6, linewidth=2)

        # Annotate with sample count
        for jc, m, n in zip(means.index, means.values, counts.values):
            ax.annotate(f"n={n}", (jc, m), textcoords="offset points",
                        xytext=(8, -12), fontsize=7, color=colors.get(method, "gray"))

    ax.set_xlabel("Number of judges", fontsize=13)
    ax.set_ylabel("Kendall τ vs Arena", fontsize=13)
    ax.set_title("Judge Count Sensitivity: τ vs Number of Judges", fontsize=14)
    ax.legend(fontsize=10)
    ax.set_xticks(sorted(df["judge_count"].unique()))
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(output_dir / "tau_vs_judge_count.png", dpi=150, bbox_inches="tight")
    fig.savefig(output_dir / "tau_vs_judge_count.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved tau_vs_judge_count.{{png,pdf}}")


def plot_leave_one_out(df: pd.DataFrame, output_dir: Path):
    """Plot leave-one-judge-out residual analysis."""
    if df.empty:
        print("  No data for leave-one-out plot")
        return

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    methods = df["method"].unique()
    colors = {
        "raw_average": "#9E9E9E",
        "mfrm_only": "#FF9800",
        "sequential": "#4CAF50",
        "joint_gmfrm": "#2196F3",
    }

    # Panel A: τ for each leave-out
    ax = axes[0]
    judges = sorted(df["left_out_judge"].unique())
    x = np.arange(len(judges))
    width = 0.8 / len(methods)

    for i, method in enumerate(methods):
        mdf = df[df["method"] == method]
        taus = [mdf[mdf["left_out_judge"] == j]["kendall_tau"].values[0]
                if len(mdf[mdf["left_out_judge"] == j]) > 0 else np.nan
                for j in judges]
        ax.bar(x + i * width - 0.4 + width / 2, taus, width,
               label=method, color=colors.get(method, "gray"), alpha=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(judges, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Kendall τ (without judge)", fontsize=11)
    ax.set_title("(a) Leave-one-judge-out: τ", fontsize=13)
    ax.legend(fontsize=8)

    # Panel B: Δτ (change from full set)
    ax = axes[1]
    for i, method in enumerate(methods):
        mdf = df[df["method"] == method]
        deltas = [mdf[mdf["left_out_judge"] == j]["tau_delta"].values[0]
                  if len(mdf[mdf["left_out_judge"] == j]) > 0 else np.nan
                  for j in judges]
        ax.bar(x + i * width - 0.4 + width / 2, deltas, width,
               label=method, color=colors.get(method, "gray"), alpha=0.8)

    ax.set_xticks(x)
    ax.set_xticklabels(judges, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("Δτ (vs full judge set)", fontsize=11)
    ax.set_title("(b) Leave-one-judge-out: Δτ", fontsize=13)
    ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
    ax.legend(fontsize=8)

    plt.tight_layout()
    fig.savefig(output_dir / "leave_one_out.png", dpi=150, bbox_inches="tight")
    fig.savefig(output_dir / "leave_one_out.pdf", bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved leave_one_out.{{png,pdf}}")


def find_crossover_point(df: pd.DataFrame) -> dict:
    """Find the minimum judge count where joint_gmfrm beats sequential."""
    if df.empty or "joint_gmfrm" not in df["method"].values:
        return {"crossover": None, "note": "insufficient data"}

    crossover = None
    for k in sorted(df["judge_count"].unique()):
        jdf = df[(df["judge_count"] == k) & (df["method"] == "joint_gmfrm")]
        sdf = df[(df["judge_count"] == k) & (df["method"] == "sequential")]

        if jdf.empty or sdf.empty:
            continue

        j_mean = jdf["kendall_tau"].mean()
        s_mean = sdf["kendall_tau"].mean()

        if j_mean > s_mean:
            crossover = k
            break

    return {
        "crossover_judge_count": crossover,
        "note": f"joint_gmfrm first beats sequential at {crossover} judges"
               if crossover else "joint_gmfrm never beats sequential in tested range",
    }


def main():
    parser = argparse.ArgumentParser(
        description="exp-006: Judge Count Sensitivity Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python run_exp006.py --dry-run           # validate data loading
  python run_exp006.py --methods raw_average  # fast CPU-only run
  python run_exp006.py --methods raw_average mfrm_only sequential joint_gmfrm  # full run (GPU)
  python run_exp006.py --judge-counts 4 6 9   # specific counts only""",
    )
    parser.add_argument("--judgment-dir", default="/root/gated_mfrm_judge_bias/exp001/results")
    parser.add_argument("--exposure-csv", default="/root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv")
    parser.add_argument("--output-dir", default="/root/gated_mfrm_judge_bias/exp006/results")
    parser.add_argument("--judge-counts", type=int, nargs="+", default=JUDGE_COUNTS,
                        help="Judge counts to test (default: 2 4 6 8 9)")
    parser.add_argument("--n-subsets", type=int, default=N_SUBSETS_PER_COUNT,
                        help="Max subsets per judge count (default: 10)")
    parser.add_argument("--methods", nargs="+",
                        default=["raw_average"],
                        choices=["raw_average", "mfrm_only", "sequential", "joint_gmfrm"],
                        help="Methods to evaluate (default: raw_average only for CPU)")
    parser.add_argument("--run-loocv", action="store_true",
                        help="Also run leave-one-judge-out analysis")
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--dry-run", action="store_true",
                        help="Only validate imports and data loading")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("exp-006: Judge Count Sensitivity Analysis")
    print("=" * 60)

    # Load data
    print("\n[1/4] Loading judgment data...")
    observations, all_judges, all_models, all_items = load_full_data(
        args.judgment_dir, args.exposure_csv)
    print(f"  Observations: {len(observations)}")
    print(f"  Judges ({len(all_judges)}): {all_judges}")
    print(f"  Models ({len(all_models)}): {all_models}")
    print(f"  Items: {len(all_items)}")

    # Generate subsets
    print(f"\n[2/4] Generating judge subsets...")
    subsets = generate_judge_subsets(all_judges, args.judge_counts, args.n_subsets, args.seed)
    for k, subs in sorted(subsets.items()):
        print(f"  k={k}: {len(subs)} subsets")

    if args.dry_run:
        print("\n[DRY RUN] Data loading OK. Summary:")
        print(f"  Would test {sum(len(v) for v in subsets.values())} subsets × {len(args.methods)} methods")
        print(f"  Methods: {args.methods}")
        if any(m in args.methods for m in ["mfrm_only", "sequential", "joint_gmfrm"]):
            print("  NOTE: MCMC methods require GPU (JAX+CUDA). Use --methods raw_average for CPU-only.")
        return

    # Run sensitivity analysis
    print(f"\n[3/4] Running sensitivity analysis (methods: {args.methods})...")
    if any(m in args.methods for m in ["mfrm_only", "sequential", "joint_gmfrm"]):
        sys.path.insert(0, "/root/gated_mfrm_judge_bias/exp003")
        import exp003_models  # noqa: verify import

    df = run_sensitivity_analysis(
        observations, all_judges, args.exposure_csv,
        args.judge_counts, args.n_subsets, args.methods, args.seed)

    # Save results
    csv_path = output_dir / "sensitivity_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"\n  Saved {csv_path} ({len(df)} rows)")

    # Crossover analysis
    crossover = find_crossover_point(df)
    print(f"\n  Crossover analysis: {crossover}")

    # Leave-one-out
    loocv_df = pd.DataFrame()
    if args.run_loocv:
        print("\n  Running leave-one-judge-out analysis...")
        loocv_df = leave_one_judge_out(observations, all_judges,
                                       args.exposure_csv, args.methods)
        if not loocv_df.empty:
            loocv_path = output_dir / "leave_one_out_results.csv"
            loocv_df.to_csv(loocv_path, index=False)
            print(f"  Saved {loocv_path}")

    # Plots
    print(f"\n[4/4] Generating plots...")
    plot_tau_vs_judge_count(df, output_dir)
    if not loocv_df.empty:
        plot_leave_one_out(loocv_df, output_dir)

    # Save summary
    summary = {
        "judge_counts_tested": sorted(df["judge_count"].unique().tolist()) if not df.empty else [],
        "methods": args.methods,
        "n_subsets_per_count": args.n_subsets,
        "total_evaluations": len(df),
        "crossover": crossover,
    }

    if not df.empty:
        # Per-count summary
        summary["per_count"] = {}
        for k in sorted(df["judge_count"].unique()):
            kdf = df[df["judge_count"] == k]
            summary["per_count"][int(k)] = {}
            for method in kdf["method"].unique():
                mdf = kdf[kdf["method"] == method]
                summary["per_count"][int(k)][method] = {
                    "mean_tau": float(mdf["kendall_tau"].mean()),
                    "std_tau": float(mdf["kendall_tau"].std()),
                    "n_subsets": len(mdf),
                }

    results_path = output_dir / "results.json"
    with open(results_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Saved {results_path}")

    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if not df.empty:
        for k in sorted(df["judge_count"].unique()):
            kdf = df[df["judge_count"] == k]
            line = f"  k={k}:"
            for method in sorted(kdf["method"].unique()):
                mdf = kdf[kdf["method"] == method]
                line += f"  {method}={mdf['kendall_tau'].mean():.4f}±{mdf['kendall_tau'].std():.4f}"
            print(line)
    print(f"\n  {crossover['note']}")


if __name__ == "__main__":
    main()
