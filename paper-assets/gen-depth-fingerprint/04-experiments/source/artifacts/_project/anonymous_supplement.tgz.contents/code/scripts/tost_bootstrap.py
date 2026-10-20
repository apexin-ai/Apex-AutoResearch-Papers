#!/usr/bin/env python3
"""Bootstrap resampling layer over TOST equivalence test."""
import argparse
import json
import numpy as np
import pandas as pd
from scipy import stats


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--data-path", default="../data/features_all_models.csv")
    p.add_argument("--margin", type=float, default=0.20, help="Cohen's d equivalence bound")
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--n-bootstrap", type=int, default=1000)
    p.add_argument("--base-seed", type=int, default=42)
    p.add_argument("--features", nargs="+",
                   default=["entropy_std", "entropy_max", "entropy_min", "tail_decay"],
                   help="Features to test")
    p.add_argument("--output", default="../results/tost_bootstrap.json")
    p.add_argument("--dry-run", action="store_true", help="Run only 10 bootstraps for verification")
    return p.parse_args()


def run_tost(x1: np.ndarray, x2: np.ndarray, d_bound: float, alpha: float):
    """Parametric TOST on two groups. Returns dict with p_tost and metadata."""
    n1, n2 = len(x1), len(x2)
    s1, s2 = x1.std(ddof=1), x2.std(ddof=1)
    pooled_sd = np.sqrt(((n1 - 1) * s1**2 + (n2 - 1) * s2**2) / (n1 + n2 - 2))

    if pooled_sd == 0:
        return {"p_tost": 0.0, "observed_d": 0.0, "equivalent": True}

    delta = d_bound * pooled_sd
    diff = x1.mean() - x2.mean()
    se = pooled_sd * np.sqrt(1 / n1 + 1 / n2)
    dof = n1 + n2 - 2
    cohens_d = diff / pooled_sd

    t_lower = (diff + delta) / se
    p_lower = 1 - stats.t.cdf(t_lower, dof)
    t_upper = (diff - delta) / se
    p_upper = stats.t.cdf(t_upper, dof)
    p_tost = max(p_lower, p_upper)

    return {
        "p_tost": float(p_tost),
        "observed_d": float(cohens_d),
        "equivalent": bool(p_tost < alpha),
    }


def stratified_bootstrap(df: pd.DataFrame, depth_col: str, rng: np.random.Generator):
    """Resample with replacement, stratified by depth level."""
    parts = []
    for _, group in df.groupby(depth_col):
        idx = rng.choice(len(group), size=len(group), replace=True)
        parts.append(group.iloc[idx])
    return pd.concat(parts, ignore_index=True)


def main():
    args = parse_args()
    n_boot = 10 if args.dry_run else args.n_bootstrap

    df = pd.read_csv(args.data_path)
    depth_col = "depth" if "depth" in df.columns else "generation"
    print(f"Data: {len(df)} rows, depth col={depth_col}, depths={sorted(df[depth_col].unique())}")
    print(f"Bootstrap: n={n_boot}, seed={args.base_seed}, margin(d)={args.margin}, alpha={args.alpha}")
    print(f"Features: {args.features}")

    results = {
        "config": {
            "n_bootstrap": n_boot,
            "base_seed": args.base_seed,
            "margin_d": args.margin,
            "alpha": args.alpha,
            "dry_run": args.dry_run,
        },
        "features": {},
    }

    for feat in args.features:
        if feat not in df.columns:
            print(f"  {feat}: COLUMN NOT FOUND, skipping")
            continue

        p_values = np.zeros(n_boot)
        d_values = np.zeros(n_boot)

        for i in range(n_boot):
            rng = np.random.default_rng(args.base_seed + i)
            boot_df = stratified_bootstrap(df, depth_col, rng)
            gen1 = boot_df[boot_df[depth_col] == 1][feat].dropna().values.astype(float)
            gen2p = boot_df[boot_df[depth_col] >= 2][feat].dropna().values.astype(float)
            res = run_tost(gen1, gen2p, args.margin, args.alpha)
            p_values[i] = res["p_tost"]
            d_values[i] = res["observed_d"]

        p_sorted = np.sort(p_values)
        rejection_rate = float(np.mean(p_values < args.alpha))

        results["features"][feat] = {
            "n_bootstrap": int(n_boot),
            "median_p": round(float(np.median(p_values)), 6),
            "mean_p": round(float(np.mean(p_values)), 6),
            "p_ci_95": [round(float(np.percentile(p_values, 2.5)), 6),
                        round(float(np.percentile(p_values, 97.5)), 6)],
            "rejection_rate": round(rejection_rate, 4),
            "median_d": round(float(np.median(d_values)), 4),
            "d_ci_95": [round(float(np.percentile(d_values, 2.5)), 4),
                        round(float(np.percentile(d_values, 97.5)), 4)],
            "margin_d": args.margin,
        }

        tag = f"reject {rejection_rate:.1%}" if rejection_rate > 0.5 else f"fail {1-rejection_rate:.1%}"
        print(f"  {feat:15s} | median_p={np.median(p_values):.2e} | {tag}")

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {args.output}")


if __name__ == "__main__":
    main()
