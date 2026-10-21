#!/usr/bin/env python3
"""DDR causal analysis: feature intervention, permutation importance, Granger causality.

Investigates whether generative depth *causally* drives feature drift,
beyond mere correlation.  Three analysis modules:

1. Feature intervention (counterfactual): shuffle a single feature's
   depth-association while keeping others intact, measure classifier
   degradation -> reveals causal contribution of each feature.
2. Permutation importance (model-free): per-feature permutation on the
   trained classifier -> complements LOFO with a non-retraining approach.
3. Granger-style causality: test whether depth predicts feature values
   beyond an autoregressive baseline (pooled panel regression).
"""
import argparse
import json
import os
import warnings
import numpy as np
import pandas as pd
from pathlib import Path

FEATURES = [
    "hapax_ratio", "ttr", "entropy_mean", "entropy_std",
    "entropy_min", "entropy_max", "tail_decay",
]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(
    n_estimators=200, max_depth=6, learning_rate=0.1,
    random_state=42, eval_metric="mlogloss",
)

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["label"] = df["depth"].map(CLASS_MAP)
    return df


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


# -- Module 1: Feature intervention (counterfactual) --

def feature_intervention(df: pd.DataFrame, n_repeats: int = 30, seed: int = 42):
    """Shuffle one feature's values across all rows to break its
    depth-association, retrain LOGO classifier, compare F1 to baseline.
    """
    from xgboost import XGBClassifier
    from sklearn.metrics import f1_score

    rng = np.random.RandomState(seed)
    generators = sorted(df["model_name"].unique())

    baseline_f1s = {}
    for gen in generators:
        test_df = df[df["model_name"] == gen]
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
        y_pred = clf.predict(test_df[FEATURES].values)
        baseline_f1s[gen] = f1_score(test_df["label"].values, y_pred, average="macro")

    avg_baseline = float(np.mean(list(baseline_f1s.values())))
    print(f"  Baseline avg LOGO F1: {avg_baseline:.4f}")

    results = {}
    for feat in FEATURES:
        deltas = []
        for rep in range(n_repeats):
            rep_rng = np.random.RandomState(seed + rep)
            df_int = df.copy()
            df_int[feat] = rep_rng.permutation(df_int[feat].values)

            fold_deltas = []
            for gen in generators:
                test_df = df_int[df_int["model_name"] == gen]
                train_df = df_int[df_int["model_name"] != gen]
                train_ds = downsample(train_df, "label", rep_rng)
                clf = XGBClassifier(**XGB_PARAMS)
                clf.fit(train_ds[FEATURES].values, train_ds["label"].values)
                y_pred = clf.predict(test_df[FEATURES].values)
                int_f1 = f1_score(test_df["label"].values, y_pred, average="macro")
                fold_deltas.append(baseline_f1s[gen] - int_f1)
            deltas.append(float(np.mean(fold_deltas)))

        results[feat] = {
            "mean_f1_drop": round(float(np.mean(deltas)), 4),
            "std_f1_drop": round(float(np.std(deltas)), 4),
        }
        print(f"  {feat:15s}  dF1 = {results[feat]['mean_f1_drop']:.4f} +/- {results[feat]['std_f1_drop']:.4f}")

    results["_baseline_avg_f1"] = round(avg_baseline, 4)
    return results


# -- Module 2: Permutation importance (no retraining) --

def permutation_importance(df: pd.DataFrame, n_repeats: int = 50, seed: int = 42):
    """Permute each feature at test time on a trained LOGO classifier.
    No retraining -- measures each feature's contribution to prediction.
    """
    from xgboost import XGBClassifier
    from sklearn.metrics import f1_score

    rng_base = np.random.RandomState(seed)
    generators = sorted(df["model_name"].unique())

    feat_importances = {f: [] for f in FEATURES}
    fold_baselines = []

    for gen in generators:
        test_df = df[df["model_name"] == gen].copy()
        train_df = df[df["model_name"] != gen]
        train_ds = downsample(train_df, "label", rng_base)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[FEATURES].values, train_ds["label"].values)

        X_test = test_df[FEATURES].values.copy()
        y_test = test_df["label"].values

        baseline_f1 = f1_score(y_test, clf.predict(X_test), average="macro")
        fold_baselines.append(baseline_f1)

        for feat_idx, feat in enumerate(FEATURES):
            drop_scores = []
            for rep in range(n_repeats):
                rng = np.random.RandomState(seed + rep)
                X_perm = X_test.copy()
                X_perm[:, feat_idx] = rng.permutation(X_perm[:, feat_idx])
                perm_f1 = f1_score(y_test, clf.predict(X_perm), average="macro")
                drop_scores.append(baseline_f1 - perm_f1)
            feat_importances[feat].append(float(np.mean(drop_scores)))

        print(f"  Fold {gen:20s}  baseline F1={baseline_f1:.4f}")

    results = {}
    avg_baseline = float(np.mean(fold_baselines))
    print(f"\n  Avg baseline F1: {avg_baseline:.4f}")
    print(f"  {'Feature':15s} {'Importance':>12s} {'Std':>10s}")
    print(f"  {'-'*40}")

    for feat in FEATURES:
        vals = feat_importances[feat]
        mean_imp = float(np.mean(vals))
        std_imp = float(np.std(vals))
        results[feat] = {
            "mean_importance": round(mean_imp, 4),
            "std_importance": round(std_imp, 4),
            "per_fold": {gen: round(v, 4) for gen, v in zip(generators, vals)},
        }
        print(f"  {feat:15s} {mean_imp:12.4f} {std_imp:10.4f}")

    results["_baseline_avg_f1"] = round(avg_baseline, 4)

    ranked = sorted(FEATURES, key=lambda f: results[f]["mean_importance"], reverse=True)
    results["_ranked"] = ranked
    print(f"\n  Ranked: {' > '.join(ranked)}")

    # Classify drifting vs stationary by median split
    importances = [results[f]["mean_importance"] for f in FEATURES]
    median_imp = float(np.median(importances))
    drifting = [f for f in ranked if results[f]["mean_importance"] >= median_imp]
    stationary = [f for f in ranked if results[f]["mean_importance"] < median_imp]
    results["_drifting_features"] = drifting
    results["_stationary_features"] = stationary
    results["_median_threshold"] = round(median_imp, 4)

    print(f"\n  Drifting  (imp >= {median_imp:.4f}): {drifting}")
    print(f"  Stationary (imp < {median_imp:.4f}): {stationary}")

    drift_avg = float(np.mean([results[f]["mean_importance"] for f in drifting])) if drifting else 0
    stat_avg = float(np.mean([results[f]["mean_importance"] for f in stationary])) if stationary else 0
    results["_group_summary"] = {
        "drifting_avg_importance": round(drift_avg, 4),
        "stationary_avg_importance": round(stat_avg, 4),
    }
    print(f"  Drifting avg importance:   {drift_avg:.4f}")
    print(f"  Stationary avg importance: {stat_avg:.4f}")

    return results


# -- Module 3: Granger-style causality on depth series --

def _ols_f_test(y, X_restr, X_full):
    """F-test for nested OLS models. Returns (F_stat, p_value, beta_full)."""
    from scipy import stats as sp_stats

    n = len(y)
    beta_r = np.linalg.lstsq(X_restr, y, rcond=None)[0]
    ss_r = float(np.sum((y - X_restr @ beta_r) ** 2))

    beta_f = np.linalg.lstsq(X_full, y, rcond=None)[0]
    ss_f = float(np.sum((y - X_full @ beta_f) ** 2))

    df1 = X_full.shape[1] - X_restr.shape[1]
    df2 = n - X_full.shape[1]

    if df2 <= 0 or ss_f <= 0:
        return np.nan, np.nan, beta_f

    f_stat = ((ss_r - ss_f) / df1) / (ss_f / df2)
    p_value = 1 - sp_stats.f.cdf(f_stat, df1, df2)

    return float(f_stat), float(p_value), beta_f


def granger_causality(df: pd.DataFrame, max_lag: int = 2):
    """Pooled panel Granger test: does depth predict feature values
    beyond autoregressive baseline?

    Per-seed depth chains have only T=5 points -- individual Granger tests
    are infeasible. We pool across all seeds (~995 per generator) for the
    panel regression.

    Restricted:  f_t ~ intercept + f_{t-1}
    Full:        f_t ~ intercept + f_{t-1} + depth_t
    """
    from scipy import stats as sp_stats

    print("  WARNING: Depth chains have only T=5 points per seed.")
    print("  Per-seed Granger tests have negligible statistical power.")
    print("  Primary results use pooled panel regression across seeds.\n")

    # Build lagged panel: for each (model, seed), sort by depth, create lags
    records = []
    for (model, sid), grp in df.groupby(["model_name", "seed_id"]):
        grp = grp.sort_values("depth")
        if len(grp) < 2:
            continue
        depths = grp["depth"].values
        feats = grp[FEATURES].values
        for t in range(1, len(grp)):
            rec = {"model_name": model, "seed_id": sid, "depth_t": int(depths[t])}
            for lag in range(1, min(max_lag + 1, t + 1)):
                for fi, fname in enumerate(FEATURES):
                    rec[f"{fname}_lag{lag}"] = feats[t - lag, fi]
            for fi, fname in enumerate(FEATURES):
                rec[f"{fname}_t"] = feats[t, fi]
            records.append(rec)

    panel = pd.DataFrame(records)
    n_chains = df.groupby(["model_name", "seed_id"]).ngroups
    print(f"  Panel: {len(panel)} obs from {n_chains} seed chains")

    effective_lag = 1  # T=5 makes lag>1 unreliable
    if max_lag > 1:
        print(f"  Requested max_lag={max_lag}, but using lag={effective_lag} (T=5 constraint)")
    print()

    # -- Overall pooled test --
    generators = sorted(df["model_name"].unique())

    print(f"  {'Feature':15s} {'F-stat':>10s} {'p-value':>12s} {'R2_full':>8s} {'R2_rest':>8s} {'dR2':>8s} {'Sig':>5s}")
    print(f"  {'-'*70}")

    results = {}
    for feat in FEATURES:
        y = panel[f"{feat}_t"].values
        lag_col = f"{feat}_lag1"
        if lag_col not in panel.columns:
            results[feat] = {"error": "missing lag column"}
            continue

        x_lag = panel[lag_col].values
        n = len(y)
        X_restr = np.column_stack([np.ones(n), x_lag])
        X_full = np.column_stack([np.ones(n), x_lag, panel["depth_t"].values])

        f_stat, p_value, beta_f = _ols_f_test(y, X_restr, X_full)

        ss_tot = float(np.sum((y - np.mean(y)) ** 2))
        ss_r = float(np.sum((y - X_restr @ np.linalg.lstsq(X_restr, y, rcond=None)[0]) ** 2))
        ss_f = float(np.sum((y - X_full @ beta_f) ** 2))
        r2_restr = 1 - ss_r / ss_tot if ss_tot > 0 else 0
        r2_full = 1 - ss_f / ss_tot if ss_tot > 0 else 0

        sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""

        results[feat] = {
            "F_stat": round(f_stat, 4),
            "p_value": p_value,
            "p_value_str": f"{p_value:.2e}",
            "r2_restricted": round(r2_restr, 4),
            "r2_full": round(r2_full, 4),
            "delta_r2": round(r2_full - r2_restr, 4),
            "significant_005": p_value < 0.05,
            "depth_coefficient": round(float(beta_f[-1]), 6),
            "n_obs": n,
        }
        print(f"  {feat:15s} {f_stat:10.2f} {p_value:12.2e} {r2_full:8.4f} {r2_restr:8.4f} {r2_full - r2_restr:8.4f} {sig:>5s}")

    # -- Per-generator pooled test --
    print(f"\n  Per-generator pooled Granger (lag={effective_lag}):")
    per_gen_results = {}
    for gen in generators:
        gen_panel = panel[panel["model_name"] == gen]
        gen_res = {}
        for feat in FEATURES:
            y = gen_panel[f"{feat}_t"].values
            lag_col = f"{feat}_lag1"
            if lag_col not in gen_panel.columns:
                continue
            x_lag = gen_panel[lag_col].values
            n = len(y)
            X_restr = np.column_stack([np.ones(n), x_lag])
            X_full = np.column_stack([np.ones(n), x_lag, gen_panel["depth_t"].values])

            f_stat, p_value, beta_f = _ols_f_test(y, X_restr, X_full)
            if np.isnan(f_stat):
                continue
            gen_res[feat] = {
                "F_stat": round(f_stat, 2),
                "p_value": p_value,
                "depth_coef": round(float(beta_f[-1]), 6),
            }
        per_gen_results[gen] = gen_res

    # -- Fisher's method: combine per-generator p-values --
    print(f"\n  Fisher's combined p-values across {len(generators)} generators:")
    fisher_results = {}
    for feat in FEATURES:
        p_vals = []
        for gen in generators:
            if gen in per_gen_results and feat in per_gen_results[gen]:
                p = per_gen_results[gen][feat]["p_value"]
                p_clipped = np.clip(p, 1e-300, 1 - 1e-15)
                p_vals.append(p_clipped)
        if len(p_vals) >= 2:
            chi2_stat = -2 * np.sum(np.log(p_vals))
            combined_p = 1 - sp_stats.chi2.cdf(chi2_stat, 2 * len(p_vals))
            fisher_results[feat] = {
                "chi2": round(float(chi2_stat), 2),
                "combined_p": float(combined_p),
                "n_generators": len(p_vals),
            }
            sig = "***" if combined_p < 0.001 else "**" if combined_p < 0.01 else "*" if combined_p < 0.05 else ""
            print(f"    {feat:15s}  chi2={chi2_stat:8.2f}  p={combined_p:.2e}  {sig}")

    results["_per_generator"] = per_gen_results
    results["_fisher_combined"] = fisher_results
    results["_panel_size"] = len(panel)
    results["_effective_lag"] = effective_lag
    results["_power_warning"] = (
        "Per-seed depth chains have only T=5 points. "
        "Pooled panel regression aggregates across ~995 seeds per generator, "
        "providing adequate power for the overall test. "
        "Individual per-seed Granger tests are infeasible (df_residual ~ 1)."
    )

    return results


# -- Module 4: Mediation analysis --

def mediation_analysis(df: pd.DataFrame):
    """Test whether drifting features mediate the effect of depth on
    classifier predictions (Baron & Kenny / bootstrap mediation).
    """
    raise NotImplementedError("Mediation analysis not yet implemented")


def main():
    parser = argparse.ArgumentParser(
        description="DDR causal analysis for gen-depth fingerprint"
    )
    parser.add_argument(
        "--data-path",
        default=str(DATA_DIR / "features_8gen.csv"),
    )
    parser.add_argument(
        "--module",
        choices=["intervention", "permutation", "granger", "mediation", "all"],
        default="all",
    )
    parser.add_argument("--n-repeats", type=int, default=30)
    parser.add_argument("--max-lag", type=int, default=2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--output",
        default=str(RESULTS_DIR / "ddr_causal_analysis.json"),
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Run on subset (2 seeds per generator) for quick validation",
    )
    args = parser.parse_args()

    df = load_data(args.data_path)
    print(f"Loaded {len(df)} rows, {df['model_name'].nunique()} generators")
    print(f"Depths: {sorted(df['depth'].unique())}")
    print(f"Features: {FEATURES}\n")

    if args.dry_run:
        sub_frames = []
        for gen in df["model_name"].unique():
            gen_df = df[df["model_name"] == gen]
            seeds = sorted(gen_df["seed_id"].unique())[:2]
            sub_frames.append(gen_df[gen_df["seed_id"].isin(seeds)])
        df = pd.concat(sub_frames, ignore_index=True)
        print(f"[DRY RUN] Subsampled to {len(df)} rows\n")

    results = {}

    if args.module in ("intervention", "all"):
        print("=== Feature Intervention ===")
        results["intervention"] = feature_intervention(
            df, n_repeats=args.n_repeats, seed=args.seed
        )

    if args.module in ("permutation", "all"):
        print("\n=== Permutation Importance ===")
        results["permutation"] = permutation_importance(
            df, n_repeats=args.n_repeats, seed=args.seed
        )

    if args.module in ("granger", "all"):
        print("\n=== Granger Causality ===")
        results["granger"] = granger_causality(df, max_lag=args.max_lag)

    if args.module in ("mediation", "all"):
        print("\n=== Mediation Analysis ===")
        results["mediation"] = mediation_analysis(df)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved: {args.output}")


if __name__ == "__main__":
    main()
