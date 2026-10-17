"""W2 Domain Bias Validation — three sub-experiments to demonstrate
depth signal is not a domain artifact from Wikipedia seed text.

Sub-exp A: d1-d3 only 3-class RF (all 9 cells)
Sub-exp B: Seed-stratified LOGO 10-fold on d1-d3
Sub-exp C: Negative control — predict seed group vs depth from features
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import time

ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est")
OUT_DIR = ROOT / "results" / "w2_domain_bias"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = {
    "pythia_nucleus095": "data/features_all.jsonl",
    "pythia_temp09": "data/pythia_temp09/features.jsonl",
    "pythia_topk50": "results/pythia_topk50/features.jsonl",
    "gpt2xl_nucleus095": "data/gpt2xl/features.jsonl",
    "gpt2xl_temp09": "results/gpt2xl_temp09/features.jsonl",
    "gpt2xl_topk50": "results/gpt2xl_topk50/features.jsonl",
    "olmo_nucleus095": "data/olmo/features.jsonl",
    "olmo_temp09": "results/olmo_temp09/features.jsonl",
    "olmo_topk50": "results/olmo_topk50/features.jsonl",
}

RF_PARAMS = dict(n_estimators=200, random_state=42, n_jobs=-1)
N_SEED_GROUPS = 10
SEED = 42


def load_features(rel_path):
    rows = []
    with open(ROOT / rel_path) as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    return df


def clean_X(X):
    X = np.array(X, dtype=np.float64)
    bad = np.isinf(X) | np.isnan(X) | (np.abs(X) > 1e15)
    if bad.any():
        X[bad] = np.nan
        for col in range(X.shape[1]):
            mask = np.isnan(X[:, col])
            if mask.any():
                finite = X[~mask, col]
                X[mask, col] = np.median(finite) if len(finite) > 0 else 0.0
    X = np.clip(X, -1e15, 1e15)
    return X


# ── Sub-exp A: d1-d3 only 3-class classification ──

def subexp_a(df, cell_name):
    df_syn = df[df["depth"].isin([1, 2, 3])].copy()
    X = clean_X(df_syn[FEATURES].values)
    y = df_syn["depth"].values

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    fold_accs = []
    fold_reports = []
    for train_idx, test_idx in skf.split(X, y):
        rf = RandomForestClassifier(**RF_PARAMS)
        rf.fit(X[train_idx], y[train_idx])
        preds = rf.predict(X[test_idx])
        fold_accs.append(accuracy_score(y[test_idx], preds))

    # full 4-class for comparison
    X_full = clean_X(df[FEATURES].values)
    y_full = df["depth"].values
    full_accs = []
    for train_idx, test_idx in skf.split(X_full, y_full):
        rf = RandomForestClassifier(**RF_PARAMS)
        rf.fit(X_full[train_idx], y_full[train_idx])
        full_accs.append(accuracy_score(y_full[test_idx], y_full[test_idx]))

    # per-class report on last fold for d1-d3
    rf_final = RandomForestClassifier(**RF_PARAMS)
    rf_final.fit(X, y)
    report = classification_report(y, rf_final.predict(X), output_dict=True)

    return {
        "cell": cell_name,
        "d1d3_acc_mean": float(np.mean(fold_accs)),
        "d1d3_acc_std": float(np.std(fold_accs)),
        "d1d3_n_samples": len(df_syn),
        "chance_3class": 1/3,
        "per_class_recall": {
            str(k): round(v["recall"], 4)
            for k, v in report.items() if k in ["1", "2", "3"]
        },
    }


# ── Sub-exp B: Seed-stratified LOGO on d1-d3 ──

def subexp_b(df, cell_name):
    df_syn = df[df["depth"].isin([1, 2, 3])].copy()

    if "sample_id" in df_syn.columns:
        seed_ids = df_syn["sample_id"].values
    else:
        seed_ids = np.arange(len(df_syn))
        depth_counts = df_syn.groupby("depth").size()
        n_per_depth = depth_counts.iloc[0]
        idx = 0
        for d in sorted(df_syn["depth"].unique()):
            mask = df_syn["depth"] == d
            n = mask.sum()
            seed_ids[df_syn.index[mask]] = np.arange(n)
            idx += n

    n_seeds = len(np.unique(seed_ids))
    group_size = n_seeds // N_SEED_GROUPS
    seed_to_group = {}
    unique_seeds = np.sort(np.unique(seed_ids))
    for i, sid in enumerate(unique_seeds):
        seed_to_group[sid] = min(i // group_size, N_SEED_GROUPS - 1)

    groups = np.array([seed_to_group[s] for s in seed_ids])

    X = clean_X(df_syn[FEATURES].values)
    y = df_syn["depth"].values

    fold_accs = []
    for g in range(N_SEED_GROUPS):
        test_mask = groups == g
        train_mask = ~test_mask
        if test_mask.sum() == 0 or train_mask.sum() == 0:
            continue
        rf = RandomForestClassifier(**RF_PARAMS)
        rf.fit(X[train_mask], y[train_mask])
        acc = accuracy_score(y[test_mask], rf.predict(X[test_mask]))
        fold_accs.append(acc)

    return {
        "cell": cell_name,
        "logo_acc_mean": float(np.mean(fold_accs)),
        "logo_acc_std": float(np.std(fold_accs)),
        "logo_acc_min": float(np.min(fold_accs)),
        "logo_acc_max": float(np.max(fold_accs)),
        "n_folds": len(fold_accs),
        "n_seeds": n_seeds,
    }


# ── Sub-exp C: Negative control — seed group prediction vs depth ──

def subexp_c(df, cell_name):
    df_syn = df[df["depth"].isin([1, 2, 3])].copy()

    if "sample_id" in df_syn.columns:
        seed_ids = df_syn["sample_id"].values
    else:
        seed_ids = np.zeros(len(df_syn), dtype=int)
        for d in sorted(df_syn["depth"].unique()):
            mask = (df_syn["depth"] == d).values
            seed_ids[mask] = np.arange(mask.sum())

    n_seeds = len(np.unique(seed_ids))
    group_size = max(1, n_seeds // N_SEED_GROUPS)
    unique_seeds = np.sort(np.unique(seed_ids))
    seed_to_group = {}
    for i, sid in enumerate(unique_seeds):
        seed_to_group[sid] = min(i // group_size, N_SEED_GROUPS - 1)

    groups = np.array([seed_to_group[s] for s in seed_ids])

    X = clean_X(df_syn[FEATURES].values)
    y_depth = df_syn["depth"].values

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

    # Task 1: predict depth (should work well)
    depth_accs = cross_val_score(
        RandomForestClassifier(**RF_PARAMS), X, y_depth, cv=skf, scoring="accuracy"
    )

    # Task 2: predict seed group (should be ~chance)
    group_accs = cross_val_score(
        RandomForestClassifier(**RF_PARAMS), X, groups, cv=skf, scoring="accuracy"
    )

    # Task 3: within each depth, predict seed group
    per_depth_group_accs = {}
    for d in [1, 2, 3]:
        mask = y_depth == d
        X_d = X[mask]
        g_d = groups[mask]
        if len(np.unique(g_d)) < 2:
            continue
        skf_d = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
        try:
            accs = cross_val_score(
                RandomForestClassifier(**RF_PARAMS), X_d, g_d, cv=skf_d, scoring="accuracy"
            )
            per_depth_group_accs[str(d)] = float(np.mean(accs))
        except ValueError:
            per_depth_group_accs[str(d)] = None

    return {
        "cell": cell_name,
        "depth_pred_acc": float(np.mean(depth_accs)),
        "depth_pred_std": float(np.std(depth_accs)),
        "seed_group_pred_acc": float(np.mean(group_accs)),
        "seed_group_pred_std": float(np.std(group_accs)),
        "chance_seed_group": 1.0 / N_SEED_GROUPS,
        "per_depth_seed_group_pred": per_depth_group_accs,
    }


def main():
    results = {"subexp_a": [], "subexp_b": [], "subexp_c": []}
    t0 = time.time()

    for cell_name, rel_path in CELLS.items():
        fpath = ROOT / rel_path
        if not fpath.exists():
            print(f"SKIP {cell_name}: {fpath} not found")
            continue
        print(f"\n{'='*60}")
        print(f"Processing {cell_name}")
        print(f"{'='*60}")

        df = load_features(rel_path)
        print(f"  Loaded {len(df)} rows, depths: {sorted(df['depth'].unique())}")

        print("  [A] d1-d3 3-class classification...")
        res_a = subexp_a(df, cell_name)
        results["subexp_a"].append(res_a)
        print(f"      acc={res_a['d1d3_acc_mean']:.4f} ± {res_a['d1d3_acc_std']:.4f}")

        print("  [B] Seed-stratified LOGO...")
        res_b = subexp_b(df, cell_name)
        results["subexp_b"].append(res_b)
        print(f"      LOGO acc={res_b['logo_acc_mean']:.4f} ± {res_b['logo_acc_std']:.4f} (range {res_b['logo_acc_min']:.4f}–{res_b['logo_acc_max']:.4f})")

        print("  [C] Negative control (seed group vs depth)...")
        res_c = subexp_c(df, cell_name)
        results["subexp_c"].append(res_c)
        print(f"      depth_pred={res_c['depth_pred_acc']:.4f}, seed_group_pred={res_c['seed_group_pred_acc']:.4f} (chance={res_c['chance_seed_group']:.2f})")

    elapsed = time.time() - t0
    results["elapsed_seconds"] = elapsed

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    print("\n[A] d1-d3 3-class accuracy (chance=33.3%):")
    for r in results["subexp_a"]:
        print(f"  {r['cell']:25s}  {r['d1d3_acc_mean']*100:5.1f}% ± {r['d1d3_acc_std']*100:4.1f}%")
    a_accs = [r["d1d3_acc_mean"] for r in results["subexp_a"]]
    print(f"  {'MEAN':25s}  {np.mean(a_accs)*100:5.1f}%")

    print("\n[B] Seed-stratified LOGO accuracy (d1-d3):")
    for r in results["subexp_b"]:
        print(f"  {r['cell']:25s}  {r['logo_acc_mean']*100:5.1f}% ± {r['logo_acc_std']*100:4.1f}%  (range {r['logo_acc_min']*100:.1f}–{r['logo_acc_max']*100:.1f}%)")
    b_accs = [r["logo_acc_mean"] for r in results["subexp_b"]]
    print(f"  {'MEAN':25s}  {np.mean(b_accs)*100:5.1f}%")

    print("\n[C] Negative control — depth vs seed group prediction:")
    print(f"  {'Cell':25s}  {'Depth':>8s}  {'SeedGrp':>8s}  {'Chance':>8s}  {'Ratio':>8s}")
    for r in results["subexp_c"]:
        ratio = r["depth_pred_acc"] / max(r["seed_group_pred_acc"], 0.01)
        print(f"  {r['cell']:25s}  {r['depth_pred_acc']*100:7.1f}%  {r['seed_group_pred_acc']*100:7.1f}%  {r['chance_seed_group']*100:7.1f}%  {ratio:7.1f}x")

    print(f"\nTotal elapsed: {elapsed:.1f}s")

    out_path = OUT_DIR / "w2_domain_bias_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
