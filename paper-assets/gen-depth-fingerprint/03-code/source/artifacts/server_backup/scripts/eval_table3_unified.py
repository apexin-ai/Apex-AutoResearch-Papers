#!/usr/bin/env python3
"""Table 3 unified evaluation: 4 methods, binary LOGO, LD-Score trigram."""

import json, time, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
          "llama-3.2-3b", "mistral-7b-v0.3"]

JSONL_PATHS = {
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "pythia-2.8b": DATA / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
    "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
    "llama-3.2-3b": DATA / "llama-3.2-3b" / "generations_filtered.jsonl",
    "mistral-7b-v0.3": DATA / "mistral-7b-v0.3" / "generations_filtered.jsonl",
}

FEAT_JSONL_PATHS = {
    "llama-3.2-3b": DATA / "llama-3.2-3b" / "features_pythia410m.jsonl",
    "mistral-7b-v0.3": DATA / "mistral-7b-v0.3" / "features_pythia410m.jsonl",
}

N_BOOT = 1000
SEED = 42

METHODS = {
    "ld_score":      (["ld_score"], 100, 3),
    "entropy_mean":  (["entropy_mean"], 100, 3),
    "4det_surface":  (["ld_score", "entropy_mean", "hapax_ratio", "ttr"], 200, 6),
    "7feature":      (["entropy_mean", "entropy_std", "entropy_max", "entropy_min",
                       "ttr", "hapax_ratio", "tail_decay"], 200, 6),
}


def ld_score_trigram(text):
    tokens = text.split()
    if len(tokens) < 3:
        return 0.0
    trigrams = [tuple(tokens[i:i+3]) for i in range(len(tokens)-2)]
    counts = Counter(trigrams)
    repeated = sum(1 for c in counts.values() if c > 1)
    return repeated / len(trigrams)


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


def load_all_data():
    print("[1] Loading features_all_models.csv (6 generators)...")
    feat = pd.read_csv(DATA / "features_all_models.csv")
    feat = feat.rename(columns={"model_name": "model"})
    print(f"  {len(feat)} rows, generators: {sorted(feat['model'].unique())}")

    # Load llama/mistral features from jsonl
    print("[2] Loading llama/mistral features...")
    for model, path in FEAT_JSONL_PATHS.items():
        df_feat = load_jsonl(path)
        df_feat["model"] = model
        # Filter to only rows present in generations_filtered
        gen_path = JSONL_PATHS[model]
        df_gen = load_jsonl(gen_path)
        valid_keys = set(zip(df_gen["seed_id"], df_gen["depth"]))
        mask = [tuple(r) in valid_keys for r in zip(df_feat["seed_id"], df_feat["depth"])]
        df_feat = df_feat[mask].reset_index(drop=True)
        df_feat = df_feat.rename(columns={"model_name": "model"} if "model_name" in df_feat.columns else {})
        if "model" not in df_feat.columns:
            df_feat["model"] = model
        feat = pd.concat([feat, df_feat[["model", "seed_id", "depth",
                                          "entropy_mean", "entropy_std", "entropy_min",
                                          "entropy_max", "tail_decay", "ttr", "hapax_ratio"]]],
                         ignore_index=True)
        print(f"  {model}: {mask.count(True)} rows added")

    print(f"  Total features: {len(feat)} rows")

    # Load text for ld_score computation
    print("[3] Loading text and computing ld_score...")
    texts_all = []
    for model in ALL_8:
        df_gen = load_jsonl(JSONL_PATHS[model])
        df_gen["model"] = model
        texts_all.append(df_gen[["model", "seed_id", "depth", "text"]])
    texts_df = pd.concat(texts_all, ignore_index=True)
    print(f"  Total texts: {len(texts_df)}")

    # Compute ld_score
    t0 = time.time()
    texts_df["ld_score"] = texts_df["text"].apply(ld_score_trigram)
    print(f"  ld_score computed in {time.time()-t0:.1f}s")

    # Merge features with text (to get ld_score)
    merged = feat.merge(texts_df[["model", "seed_id", "depth", "ld_score"]],
                        on=["model", "seed_id", "depth"], how="inner")
    print(f"[4] Merged: {len(merged)} rows")
    print(f"  Generators: {sorted(merged['model'].unique())}")
    print(f"  Per-generator counts:")
    for m in ALL_8:
        n = (merged["model"] == m).sum()
        print(f"    {m}: {n}")

    # Check for NaN
    needed = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min",
              "ttr", "hapax_ratio", "tail_decay", "ld_score"]
    na_count = merged[needed].isna().sum().sum()
    if na_count > 0:
        print(f"  WARNING: {na_count} NaN values, filling with median")
        for col in needed:
            if merged[col].isna().any():
                merged[col] = merged[col].fillna(merged[col].median())

    return merged


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        scores.append(f1_score(y_true[idx], y_pred[idx], average='macro'))
    return float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))


def logo_eval(df, features, n_estimators, max_depth):
    """Leave-One-Generator-Out, binary: gen1 vs gen2+, exclude depth=0."""
    # Filter: depth >= 1
    df_bin = df[df["depth"] >= 1].copy()
    df_bin["label"] = (df_bin["depth"] >= 2).astype(int)

    all_y_true = []
    all_y_pred = []

    for held_out in ALL_8:
        test_mask = df_bin["model"] == held_out
        train_mask = ~test_mask

        X_train = df_bin.loc[train_mask, features].values
        y_train = df_bin.loc[train_mask, "label"].values
        X_test = df_bin.loc[test_mask, features].values
        y_test = df_bin.loc[test_mask, "label"].values

        if len(X_test) == 0:
            continue

        clf = XGBClassifier(
            n_estimators=n_estimators, max_depth=max_depth,
            learning_rate=0.1, random_state=SEED,
            use_label_encoder=False, eval_metric='logloss',
            verbosity=0, n_jobs=-1
        )
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        all_y_true.extend(y_test)
        all_y_pred.extend(y_pred)

    y_true = np.array(all_y_true)
    y_pred = np.array(all_y_pred)
    f1 = float(f1_score(y_true, y_pred, average='macro'))
    ci_lower, ci_upper = bootstrap_ci(y_true, y_pred)
    return f1, ci_lower, ci_upper, len(y_true)


def main():
    t0 = time.time()
    print("=" * 60)
    print("Table 3 Unified Evaluation")
    print("Binary (gen1 vs gen2+) | Pooled LOGO 8-fold | Tiered XGB")
    print("=" * 60)

    merged = load_all_data()

    print(f"\n{'='*60}")
    print("LOGO Evaluation")
    print(f"{'='*60}")

    results = {}
    for name, (feats, n_est, max_d) in METHODS.items():
        print(f"\n  {name} (n_est={n_est}, max_depth={max_d}, {len(feats)} features)...")
        f1, ci_lo, ci_hi, n = logo_eval(merged, feats, n_est, max_d)
        print(f"    F1={f1:.4f}  CI=[{ci_lo:.4f}, {ci_hi:.4f}]  n={n}")
        results[name] = {"f1": round(f1, 4), "ci_lower": round(ci_lo, 4), "ci_upper": round(ci_hi, 4)}

    # Summary
    print(f"\n{'='*60}")
    print(f"{'Method':<15} {'F1':>8} {'CI':>22}")
    print("-" * 50)
    for name in ["ld_score", "entropy_mean", "4det_surface", "7feature"]:
        r = results[name]
        print(f"{name:<15} {r['f1']:>8.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]")

    # Save
    n_bin = merged[merged["depth"] >= 1].shape[0]
    output = {
        "ld_score": results["ld_score"],
        "entropy_mean": results["entropy_mean"],
        "4det_surface": results["4det_surface"],
        "7feature": results["7feature"],
        "meta": {
            "n_samples": int(n_bin),
            "n_generators": 8,
            "task": "binary (gen1 vs gen2+)",
            "protocol": "pooled LOGO 8-fold",
            "hyperparams": {
                "single": {"n_estimators": 100, "max_depth": 3},
                "ensemble": {"n_estimators": 200, "max_depth": 6}
            },
            "random_state": 42,
            "bootstrap_n": 1000
        }
    }

    out_path = RESULTS / "8gen_table3_unified.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
