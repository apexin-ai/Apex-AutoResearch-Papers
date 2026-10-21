"""
cross_ref_analysis.py — Cross-family reference model analysis.

Evaluates whether the depth signal is robust to the choice of reference model
by comparing Spearman correlations, entropy drift, and LOGO classification
across three reference models (Pythia-410M, OLMo-2-1B, Qwen3-0.6B).
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder


FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay", "ttr", "hapax_ratio"]
DEPTH_BINS = {0: "gen-0", 1: "gen-1"}


def assign_class(depth):
    if depth == 0:
        return "gen-0"
    elif depth == 1:
        return "gen-1"
    else:
        return "gen-2+"


def spearman_with_ci(feature_values, depth_values, n_bootstrap=1000, seed=42):
    rng = np.random.RandomState(seed)
    rho, p = spearmanr(feature_values, depth_values)
    n = len(feature_values)
    rhos = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        r, _ = spearmanr(feature_values[idx], depth_values[idx])
        rhos.append(r)
    ci_low, ci_high = np.percentile(rhos, [2.5, 97.5])
    return float(rho), float(p), float(ci_low), float(ci_high)


def compute_spearman_table(df, ref_name):
    print(f"\n{'='*70}")
    print(f"Spearman rho (individual-level) -- Reference: {ref_name}")
    print(f"{'='*70}")
    header = f"{'Generator':<15} {'Feature':<15} {'rho':>8} {'p':>10} {'CI_low':>8} {'CI_high':>8}"
    print(header)
    print("-" * len(header))

    results = {}
    for gen in sorted(df["model_name"].unique()):
        gdf = df[df["model_name"] == gen]
        results[gen] = {}
        for feat in FEATURES:
            rho, p, ci_lo, ci_hi = spearman_with_ci(gdf[feat].values, gdf["depth"].values)
            results[gen][feat] = {"rho": rho, "p": p, "ci_low": ci_lo, "ci_high": ci_hi}
            sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
            print(f"{gen:<15} {feat:<15} {rho:>8.4f} {p:>10.2e} {ci_lo:>8.4f} {ci_hi:>8.4f} {sig}")
    return results


def compute_entropy_drift(df, ref_name):
    print(f"\n{'='*70}")
    print(f"entropy_mean drift by depth -- Reference: {ref_name}")
    print(f"{'='*70}")
    header = f"{'Generator':<15} {'depth_0':>10} {'depth_1':>10} {'depth_2+':>10} {'drift(0->2+)':>12}"
    print(header)
    print("-" * len(header))

    results = {}
    for gen in sorted(df["model_name"].unique()):
        gdf = df[df["model_name"] == gen]
        d0 = gdf[gdf["depth"] == 0]["entropy_mean"].mean()
        d1 = gdf[gdf["depth"] == 1]["entropy_mean"].mean()
        d2p = gdf[gdf["depth"] >= 2]["entropy_mean"].mean()
        drift = d2p - d0
        results[gen] = {"depth_0": float(d0), "depth_1": float(d1), "depth_2+": float(d2p), "drift": float(drift)}
        print(f"{gen:<15} {d0:>10.4f} {d1:>10.4f} {d2p:>10.4f} {drift:>12.4f}")
    return results


def logo_classification(df, ref_name, n_bootstrap=1000, seed=42):
    print(f"\n{'='*70}")
    print(f"LOGO 3-class classification -- Reference: {ref_name}")
    print(f"{'='*70}")

    df = df.copy()
    df["class"] = df["depth"].apply(assign_class)
    le = LabelEncoder()
    le.fit(["gen-0", "gen-1", "gen-2+"])

    generators = sorted(df["model_name"].unique())
    fold_f1s = []

    for held_out in generators:
        train_df = df[df["model_name"] != held_out]
        test_df = df[df["model_name"] == held_out]

        min_count = train_df["class"].value_counts().min()
        train_balanced = pd.concat([g.sample(n=min_count, random_state=seed) for _, g in train_df.groupby("class")])
        X_train = train_balanced[FEATURES].values
        y_train = le.transform(train_balanced["class"])
        X_test = test_df[FEATURES].values
        y_test = le.transform(test_df["class"])

        clf = XGBClassifier(
            n_estimators=200, max_depth=6, learning_rate=0.1,
            random_state=seed, eval_metric="mlogloss",
            use_label_encoder=False,
        )
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        f1 = f1_score(y_test, y_pred, average="macro")
        fold_f1s.append(f1)
        print(f"  Held-out: {held_out:<15} macro-F1: {f1:.4f}")

    avg_f1 = np.mean(fold_f1s)

    rng = np.random.RandomState(seed)
    boot_f1s = []
    fold_arr = np.array(fold_f1s)
    for _ in range(n_bootstrap):
        idx = rng.choice(len(fold_arr), len(fold_arr), replace=True)
        boot_f1s.append(fold_arr[idx].mean())
    ci_lo, ci_hi = np.percentile(boot_f1s, [2.5, 97.5])

    print(f"\n  Avg macro-F1: {avg_f1:.4f}  95% CI: [{ci_lo:.4f}, {ci_hi:.4f}]")

    return {
        "avg_macro_f1": float(avg_f1),
        "ci_low": float(ci_lo),
        "ci_high": float(ci_hi),
        "per_fold": {gen: float(f1) for gen, f1 in zip(generators, fold_f1s)},
    }


def main():
    project_root = Path(__file__).resolve().parent.parent

    refs = {}
    paths = {
        "pythia-410m": project_root / "data" / "features_all_models.csv",
        "olmo-2-1b": project_root / "data" / "features_ref_olmo.csv",
        "qwen3-0.6b": project_root / "data" / "features_ref_qwen.csv",
    }

    for name, path in paths.items():
        if not path.exists():
            print(f"[SKIP] {path} not found")
            continue
        df = pd.read_csv(path)
        print(f"Loaded {name}: {df.shape} -- generators: {sorted(df['model_name'].unique())}")
        refs[name] = df

    if len(refs) < 2:
        print("Need at least 2 reference results for comparison")
        sys.exit(1)

    all_results = {}

    for ref_name, df in refs.items():
        spearman = compute_spearman_table(df, ref_name)
        drift = compute_entropy_drift(df, ref_name)
        logo = logo_classification(df, ref_name)
        all_results[ref_name] = {
            "spearman": spearman,
            "entropy_drift": drift,
            "logo": logo,
        }

    print(f"\n{'='*70}")
    print("CROSS-REFERENCE COMPARISON SUMMARY")
    print(f"{'='*70}")

    print("\nentropy_mean drift (depth 0 -> 2+) across references:")
    header = f"{'Generator':<15}" + "".join(f" {r:>15}" for r in all_results.keys())
    print(header)
    print("-" * len(header))
    generators = sorted(set().union(*[r["entropy_drift"].keys() for r in all_results.values()]))
    for gen in generators:
        vals = []
        for ref_name in all_results:
            d = all_results[ref_name]["entropy_drift"].get(gen, {})
            vals.append(f" {d.get('drift', float('nan')):>15.4f}")
        print(f"{gen:<15}" + "".join(vals))

    print("\nLOGO macro-F1 across references:")
    for ref_name in all_results:
        logo = all_results[ref_name]["logo"]
        print(f"  {ref_name:<15} avg F1: {logo['avg_macro_f1']:.4f}  CI: [{logo['ci_low']:.4f}, {logo['ci_high']:.4f}]")

    print("\nConsistency verdict:")
    pythia_drifts = all_results.get("pythia-410m", {}).get("entropy_drift", {})
    for ref_name in all_results:
        if ref_name == "pythia-410m":
            continue
        ref_drifts = all_results[ref_name]["entropy_drift"]
        same_sign = 0
        total = 0
        for gen in generators:
            pd_val = pythia_drifts.get(gen, {}).get("drift")
            rd_val = ref_drifts.get(gen, {}).get("drift")
            if pd_val is not None and rd_val is not None:
                total += 1
                if (pd_val < 0) == (rd_val < 0):
                    same_sign += 1
        print(f"  {ref_name} vs pythia-410m: {same_sign}/{total} generators show same drift direction")

    out_path = project_root / "data" / "cross_ref_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
