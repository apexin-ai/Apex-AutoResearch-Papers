"""8gen_length_confound.py — Text Length Confound Control for 8-gen LOGO."""

import json, os, glob
import numpy as np
import pandas as pd
from scipy import stats
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

SEED = 42
FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
            "tail_decay", "ttr", "hapax_ratio"]
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=SEED, eval_metric="mlogloss",
                  use_label_encoder=False)
N_BINS = 10

ROOT = "/root/gen-depth-fingerprint"
DATA_DIR = os.path.join(ROOT, "data")
RESULTS_DIR = os.path.join(ROOT, "results")

GEN_DIRS = {
    "pythia-2.8b": "pythia-2.8b-continuation",
    "pythia-1b": "pythia-1b",
    "olmo-2-1b": "olmo-2-1b",
    "qwen3-0.6b": "qwen3-0.6b",
    "qwen3-1.7b": "qwen3-1.7b",
    "qwen3-8b": "qwen3-8b",
    "llama-3.2-3b": "llama-3.2-3b",
    "mistral-7b-v0.3": "mistral-7b-v0.3",
}


def load_features():
    df_base = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
    new_gens = [
        ("llama-3.2-3b", os.path.join(DATA_DIR, "llama-3.2-3b", "features_pythia410m.jsonl")),
        ("mistral-7b-v0.3", os.path.join(DATA_DIR, "mistral-7b-v0.3", "features_pythia410m.jsonl")),
    ]
    dfs = [df_base]
    for gen_name, path in new_gens:
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen_name
                records.append(rec)
        dfs.append(pd.DataFrame(records))
    cols = ["model_name", "seed_id", "depth"] + FEATURES
    return pd.concat([d[cols] for d in dfs], ignore_index=True)


def load_word_counts():
    all_wc = []
    for model, gen_dir in GEN_DIRS.items():
        dir_path = os.path.join(DATA_DIR, gen_dir)
        shard_files = sorted(glob.glob(os.path.join(dir_path, "generations_shard[0-9].jsonl")))
        records = []
        seen = set()
        for sf in shard_files:
            with open(sf) as f:
                for line in f:
                    if not line.strip():
                        continue
                    rec = json.loads(line)
                    key = (rec["seed_id"], rec["depth"])
                    if key in seen:
                        continue
                    seen.add(key)
                    records.append({
                        "model_name": model,
                        "seed_id": rec["seed_id"],
                        "depth": rec["depth"],
                        "word_count": len(rec["text"].split()),
                    })
        print(f"  {model}: {len(records)} word counts from {len(shard_files)} shard(s)")
        all_wc.append(pd.DataFrame(records))
    return pd.concat(all_wc, ignore_index=True)


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = []
    for lbl in sorted(counts.index):
        sub = df[df[label_col] == lbl]
        parts.append(sub.sample(n=min_n, random_state=rng, replace=False))
    return pd.concat(parts, ignore_index=True)


def run_logo_binary(df, features, rng, label=""):
    generators = sorted(df["model_name"].unique())
    per_gen = {}
    for gen in generators:
        test = df[df["model_name"] == gen]
        train = df[df["model_name"] != gen]
        if len(test) == 0 or len(test["label"].unique()) < 2:
            continue
        train_ds = downsample(train, "label", rng)
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[features].values, train_ds["label"].values)
        y_pred = clf.predict(test[features].values)
        f1 = f1_score(test["label"].values, y_pred, average="binary")
        per_gen[gen] = round(float(f1), 4)
        print(f"  {label} {gen:20s}: F1={f1:.4f} (n={len(test)})")
    avg = round(float(np.mean(list(per_gen.values()))), 4)
    print(f"  {label} {'AVERAGE':20s}: F1={avg:.4f}")
    return per_gen, avg


def main():
    print("Loading features...")
    feat_df = load_features()
    print(f"Features: {len(feat_df)} rows, {feat_df['model_name'].nunique()} generators")

    print("\nLoading word counts from generation files...")
    wc_df = load_word_counts()

    df = feat_df.merge(wc_df, on=["model_name", "seed_id", "depth"], how="left")
    n_miss = df["word_count"].isna().sum()
    print(f"\nMerged: {len(df)} rows, {n_miss} missing word_count")
    df = df.dropna(subset=["word_count"])
    df["word_count"] = df["word_count"].astype(int)

    # Depth classes
    df["depth_class"] = df["depth"].apply(
        lambda d: "gen_0" if d == 0 else ("gen_1" if d == 1 else "gen_2plus"))

    results = {}

    # ---- Step 1: Length distribution by depth ----
    print("\n" + "=" * 60)
    print("Step 1: Text length distribution by depth class")
    print("=" * 60)
    length_stats = {}
    for dc in ["gen_0", "gen_1", "gen_2plus"]:
        sub = df[df["depth_class"] == dc]["word_count"]
        length_stats[dc] = {
            "mean": round(float(sub.mean()), 2),
            "median": round(float(sub.median()), 2),
            "std": round(float(sub.std()), 2),
            "min": int(sub.min()),
            "max": int(sub.max()),
            "n": int(len(sub)),
        }
        print(f"  {dc:10s}: mean={sub.mean():.1f}, median={sub.median():.0f}, "
              f"std={sub.std():.1f}, n={len(sub)}")

    # Per-generator
    length_per_gen = {}
    for model in sorted(df["model_name"].unique()):
        ms = {}
        msub = df[df["model_name"] == model]
        for dc in ["gen_0", "gen_1", "gen_2plus"]:
            sub = msub[msub["depth_class"] == dc]["word_count"]
            if len(sub) > 0:
                ms[dc] = {"mean": round(float(sub.mean()), 2),
                          "std": round(float(sub.std()), 2),
                          "n": int(len(sub))}
        length_per_gen[model] = ms

    # Kruskal-Wallis across depth classes
    groups = [df[df["depth_class"] == dc]["word_count"].values
              for dc in ["gen_0", "gen_1", "gen_2plus"]]
    H, p_kw = stats.kruskal(*groups)
    print(f"\n  Kruskal-Wallis: H={H:.2f}, p={p_kw:.2e}")

    results["length_stats_by_depth"] = length_stats
    results["length_stats_per_generator"] = length_per_gen
    results["kruskal_wallis"] = {"H": round(float(H), 4), "p": float(p_kw)}

    # ---- Step 2: Feature-length correlations ----
    print("\n" + "=" * 60)
    print("Step 2: Feature-length correlations (pooled)")
    print("=" * 60)
    corr_results = {}
    for feat in FEATURES:
        pr, pp = stats.pearsonr(df["word_count"], df[feat])
        sr, sp = stats.spearmanr(df["word_count"], df[feat])
        corr_results[feat] = {
            "pearson_r": round(float(pr), 4),
            "pearson_p": float(pp),
            "spearman_rho": round(float(sr), 4),
            "spearman_p": float(sp),
        }
        print(f"  {feat:15s}: pearson r={pr:+.4f} (p={pp:.2e}), "
              f"spearman ρ={sr:+.4f} (p={sp:.2e})")
    results["feature_length_correlations"] = corr_results

    # ---- Step 3: Length-matched comparison ----
    print("\n" + "=" * 60)
    print("Step 3: Length-matched LOGO (binary: gen-1 vs gen-2+)")
    print("=" * 60)

    # Binary subset
    df_binary = df[df["depth"] >= 1].copy()
    df_binary["label"] = (df_binary["depth"] >= 2).astype(int)

    rng = np.random.RandomState(SEED)

    # Create decile bins on word_count
    df_binary["length_bin"] = pd.qcut(
        df_binary["word_count"], q=N_BINS, labels=False, duplicates="drop")

    # Stratified subsample: equalize label counts within each bin
    matched_parts = []
    for b in sorted(df_binary["length_bin"].unique()):
        bin_data = df_binary[df_binary["length_bin"] == b]
        counts = bin_data["label"].value_counts()
        if len(counts) < 2:
            continue
        min_n = counts.min()
        for lbl in [0, 1]:
            sub = bin_data[bin_data["label"] == lbl]
            matched_parts.append(sub.sample(n=min_n, random_state=rng, replace=False))

    df_matched = pd.concat(matched_parts, ignore_index=True)

    print(f"\n  Total matched: {len(df_matched)} (from {len(df_binary)} binary rows)")
    for lbl, name in [(0, "gen-1"), (1, "gen-2+")]:
        sub = df_matched[df_matched["label"] == lbl]
        print(f"    {name}: n={len(sub)}, word_count mean={sub['word_count'].mean():.1f}, "
              f"std={sub['word_count'].std():.1f}")

    # Verify length distributions match (KS test)
    ks_stat, ks_p = stats.ks_2samp(
        df_matched[df_matched["label"] == 0]["word_count"],
        df_matched[df_matched["label"] == 1]["word_count"])
    print(f"    KS test (gen-1 vs gen-2+ lengths): stat={ks_stat:.4f}, p={ks_p:.4f}")

    # Run matched LOGO
    print("\n  --- Length-matched binary LOGO ---")
    matched_per_gen, avg_matched = run_logo_binary(
        df_matched, FEATURES, rng, label="[matched]")

    # Run original (unmatched) LOGO
    print("\n  --- Original (unmatched) binary LOGO ---")
    orig_per_gen, avg_original = run_logo_binary(
        df_binary, FEATURES, rng, label="[original]")

    f1_drop = round(avg_original - avg_matched, 4)

    # ---- Step 4: Judgment ----
    if abs(f1_drop) < 0.02:
        conclusion = "length_not_confound"
    else:
        conclusion = "length_is_confound"

    print("\n" + "=" * 60)
    print("Step 4: Judgment")
    print("=" * 60)
    print(f"  Original binary F1: {avg_original}")
    print(f"  Matched  binary F1: {avg_matched}")
    print(f"  F1 drop:            {f1_drop}")
    print(f"  Conclusion:         {conclusion}")

    # Per-gen comparison
    print("\n  Per-generator comparison:")
    for gen in sorted(set(list(orig_per_gen.keys()) + list(matched_per_gen.keys()))):
        o = orig_per_gen.get(gen, float('nan'))
        m = matched_per_gen.get(gen, float('nan'))
        d = round(o - m, 4) if not (np.isnan(o) or np.isnan(m)) else "N/A"
        print(f"    {gen:20s}: orig={o:.4f}, matched={m:.4f}, drop={d}")

    # Also run 5-fold stratified CV on matched data as supplementary
    print("\n  --- 5-fold Stratified CV on matched data (supplementary) ---")
    from sklearn.model_selection import StratifiedKFold
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    fold_f1s = []
    X_m = df_matched[FEATURES].values
    y_m = df_matched["label"].values
    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(X_m, y_m)):
        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(X_m[train_idx], y_m[train_idx])
        y_pred = clf.predict(X_m[test_idx])
        f1 = f1_score(y_m[test_idx], y_pred, average="binary")
        fold_f1s.append(float(f1))
    cv_mean = round(float(np.mean(fold_f1s)), 4)
    cv_std = round(float(np.std(fold_f1s)), 4)
    print(f"  5-fold CV F1: {cv_mean} ± {cv_std}")

    # Build output
    n_per_depth = {
        "gen_1": int((df_matched["label"] == 0).sum()),
        "gen_2plus": int((df_matched["label"] == 1).sum()),
    }

    results["length_matched_eval"] = {
        "n_samples_matched": int(len(df_matched)),
        "n_per_depth": n_per_depth,
        "ks_test_matched_lengths": {"stat": round(float(ks_stat), 4), "p": round(float(ks_p), 4)},
        "per_generator_matched": matched_per_gen,
        "per_generator_original": orig_per_gen,
        "binary_f1_matched": avg_matched,
        "binary_f1_original": avg_original,
        "f1_drop": f1_drop,
        "conclusion": conclusion,
        "supplementary_5fold_cv": {
            "mean_f1": cv_mean,
            "std_f1": cv_std,
            "fold_f1s": [round(x, 4) for x in fold_f1s],
        },
    }

    results["meta"] = {
        "n_quantile_bins": N_BINS,
        "matching_method": "stratified_subsample_by_length_decile",
        "xgb_params": {"n_estimators": 200, "max_depth": 6},
        "seed": SEED,
        "protocol": "pooled LOGO 8-fold binary",
        "n_generators": len(sorted(df["model_name"].unique())),
        "generators": sorted(df["model_name"].unique()),
    }

    os.makedirs(RESULTS_DIR, exist_ok=True)
    out_path = os.path.join(RESULTS_DIR, "8gen_length_confound.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
