# Anonymous submission — EMNLP 2026 ARR
"""8gen_length_confound.py -- Text Length Confound Control for 8-gen LOGO."""

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

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "..", "data")
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

    df["depth_class"] = df["depth"].apply(
        lambda d: "gen_0" if d == 0 else ("gen_1" if d == 1 else "gen_2plus"))

    results = {}
    rng = np.random.RandomState(SEED)

    # Step 1: Length stats
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
            "n": int(len(sub)),
        }
        print(f"  {dc:10s}: mean={sub.mean():.1f}, median={sub.median():.0f}, std={sub.std():.1f}")

    groups = [df[df["depth_class"] == dc]["word_count"].values
              for dc in ["gen_0", "gen_1", "gen_2plus"]]
    H, p_kw = stats.kruskal(*groups)
    print(f"\n  Kruskal-Wallis: H={H:.2f}, p={p_kw:.2e}")
    results["length_stats_by_depth"] = length_stats
    results["kruskal_wallis"] = {"H": round(float(H), 4), "p": float(p_kw)}

    # Step 2: Feature-length correlations
    print("\n" + "=" * 60)
    print("Step 2: Feature-length correlations (pooled)")
    print("=" * 60)
    corr_results = {}
    for feat in FEATURES:
        sr, sp = stats.spearmanr(df["word_count"], df[feat])
        corr_results[feat] = {"spearman_rho": round(float(sr), 4), "spearman_p": float(sp)}
        print(f"  {feat:20s}: rho={sr:.4f}, p={sp:.2e}")
    results["feature_length_correlations"] = corr_results

    # Step 3: Length-matched LOGO
    print("\n" + "=" * 60)
    print("Step 3: Length-matched binary LOGO")
    print("=" * 60)
    df_binary = df[df["depth"] >= 1].copy()
    df_binary["label"] = (df_binary["depth"] >= 2).astype(int)

    df_binary["length_bin"] = pd.qcut(df_binary["word_count"], q=N_BINS, labels=False, duplicates="drop")

    matched_parts = []
    for bin_val in sorted(df_binary["length_bin"].unique()):
        bin_df = df_binary[df_binary["length_bin"] == bin_val]
        n_per_label = bin_df["label"].value_counts().min()
        if n_per_label == 0:
            continue
        for lbl in [0, 1]:
            sub = bin_df[bin_df["label"] == lbl]
            matched_parts.append(sub.sample(n=n_per_label, random_state=rng, replace=False))
    df_matched = pd.concat(matched_parts, ignore_index=True)

    print(f"  Matched: {len(df_matched)} samples")
    for name, sub in [("gen-1", df_matched[df_matched["label"] == 0]),
                      ("gen-2+", df_matched[df_matched["label"] == 1])]:
        print(f"    {name}: n={len(sub)}, word_count mean={sub['word_count'].mean():.1f}")

    ks_stat, ks_p = stats.ks_2samp(
        df_matched[df_matched["label"] == 0]["word_count"],
        df_matched[df_matched["label"] == 1]["word_count"])
    print(f"    KS test: stat={ks_stat:.4f}, p={ks_p:.4f}")

    print("\n  --- Length-matched binary LOGO ---")
    matched_per_gen, avg_matched = run_logo_binary(df_matched, FEATURES, rng, label="[matched]")

    print("\n  --- Original (unmatched) binary LOGO ---")
    orig_per_gen, avg_original = run_logo_binary(df_binary, FEATURES, rng, label="[original]")

    f1_drop = round(avg_original - avg_matched, 4)
    conclusion = "length_not_confound" if abs(f1_drop) < 0.02 else "length_is_confound"

    print(f"\n  Original binary F1: {avg_original}")
    print(f"  Matched  binary F1: {avg_matched}")
    print(f"  F1 drop:            {f1_drop}")
    print(f"  Conclusion:         {conclusion}")

    results["length_matched_eval"] = {
        "n_samples_matched": int(len(df_matched)),
        "ks_test_matched_lengths": {"stat": round(float(ks_stat), 4), "p": round(float(ks_p), 4)},
        "binary_f1_matched": avg_matched,
        "binary_f1_original": avg_original,
        "f1_drop": f1_drop,
        "conclusion": conclusion,
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
