#!/usr/bin/env python3
"""D039 Table 3 unified evaluation (v4).

Tiered XGB: ensemble (200/6) for >=3 features, single (100/3) for 1 feature.
Same LOGO folds, pooled macro-F1, no downsample, no filter.
LD-score computed per-fold via trigram JSD with dense top-10K vocab.
"""

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

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

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

FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]

N_BOOT = 1000
SEED = 42
EPS = 1e-10

XGB_ENSEMBLE = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                    random_state=42, eval_metric="mlogloss", verbosity=0, n_jobs=-1)
XGB_SINGLE = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0, n_jobs=-1)

METHODS = {
    "7feature_ours": (["entropy_mean", "entropy_std", "entropy_max", "entropy_min",
                       "ttr", "hapax_ratio", "tail_decay"], XGB_ENSEMBLE),
    "4det_surface":  (["avg_logprob", "fastdetectgpt", "binoculars", "ld_score",
                       "ttr", "hapax_ratio"], XGB_ENSEMBLE),
    "4det_ensemble": (["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"], XGB_ENSEMBLE),
    "avg_logprob":   (["avg_logprob"], XGB_SINGLE),
    "ld_score":      (["ld_score"], XGB_SINGLE),
    "fastdetectgpt": (["fastdetectgpt"], XGB_SINGLE),
    "binoculars":    (["binoculars"], XGB_SINGLE),
}


def build_trigram_dense(texts, max_vocab=10000, n=3):
    vocab_counts = Counter()
    rows_data = []
    for t in texts:
        t_lower = t.lower()
        c = Counter(t_lower[j:j+n] for j in range(len(t_lower) - n + 1))
        vocab_counts.update(c.keys())
        rows_data.append(c)

    top_trigrams = [ng for ng, _ in vocab_counts.most_common(max_vocab)]
    vocab = {ng: i for i, ng in enumerate(top_trigrams)}
    V = len(vocab)

    mat = np.zeros((len(texts), V), dtype=np.float32)
    for i, c in enumerate(rows_data):
        total = sum(c.values())
        if total > 0:
            for ng, cnt in c.items():
                if ng in vocab:
                    mat[i, vocab[ng]] = cnt / total
    return mat


def compute_jsd_vectorized(p_norm, ref_mask):
    ref_dist = p_norm[ref_mask].mean(axis=0)
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist = ref_dist / ref_sum

    q = ref_dist[np.newaxis, :] + EPS
    q = q / q.sum()
    p = p_norm + EPS
    p = p / p.sum(axis=1, keepdims=True)

    m = 0.5 * (p + q)
    kl_pm = (p * np.log(p / m)).sum(axis=1)
    kl_qm = (q * np.log(q / m)).sum(axis=1)
    return np.sqrt(np.clip(0.5 * kl_pm + 0.5 * kl_qm, 0, None))


def logo_eval(df, feat_cols, xgb_params, gens, tri_dense=None, binary=False):
    if binary:
        mask_bin = df["label"] >= 1
        df_eval = df[mask_bin].copy().reset_index(drop=True)
        y_all = (df_eval["label"] >= 2).astype(int).values
        tri_eval = tri_dense[mask_bin.values] if tri_dense is not None else None
    else:
        df_eval = df.copy().reset_index(drop=True)
        y_all = df_eval["label"].values
        tri_eval = tri_dense

    groups = df_eval["model_name"].values
    preds = np.full(len(y_all), -1, dtype=int)
    per_gen = {}

    for g in sorted(gens):
        tr_mask = groups != g
        te_mask = groups == g
        if te_mask.sum() == 0:
            continue

        if "ld_score" in feat_cols and tri_eval is not None:
            ref_mask = tr_mask & (y_all == 0)
            ld_all = compute_jsd_vectorized(tri_eval, ref_mask)
            df_eval["ld_score"] = ld_all

        X_train = df_eval.loc[tr_mask, feat_cols].values
        y_train = y_all[tr_mask]
        X_test = df_eval.loc[te_mask, feat_cols].values
        y_test = y_all[te_mask]

        clf = XGBClassifier(**xgb_params)
        clf.fit(X_train, y_train)
        p = clf.predict(X_test)
        preds[te_mask] = p
        f1_g = round(float(f1_score(y_test, p, average="macro")), 4)
        per_gen[g] = f1_g

    valid = preds >= 0
    pooled_f1 = round(float(f1_score(y_all[valid], preds[valid], average="macro")), 4)
    return pooled_f1, per_gen, y_all[valid], preds[valid]


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        yt, yp = y_true[idx], y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(f1_score(yt, yp, average="macro"))
    arr = np.array(scores)
    return [round(float(np.percentile(arr, 2.5)), 4),
            round(float(np.percentile(arr, 97.5)), 4)]


def load_all_data():
    print("[1] Loading texts from JSONL...")
    text_records = []
    for model_name in ALL_8:
        path = JSONL_PATHS[model_name]
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                text_records.append({
                    "model_name": model_name,
                    "seed_id": rec.get("seed_id", rec.get("id")),
                    "depth": rec["depth"],
                    "text": rec["text"],
                })
    text_df = pd.DataFrame(text_records)
    text_df["label"] = text_df["depth"].map(CLASS_MAP)
    print(f"  Texts: {len(text_df)} rows")

    print("[2] Loading detector scores...")
    scores_8gen = pd.read_csv(DATA / "detector_scores_8gen.csv")
    merged = text_df.merge(
        scores_8gen[["model_name", "seed_id", "depth", "avg_logprob", "fastdetectgpt", "binoculars"]],
        on=["model_name", "seed_id", "depth"], how="left")
    print(f"  Detector scores: {scores_8gen.shape[0]} rows")

    print("[3] Loading 7-feature data...")
    feat_base = pd.read_csv(DATA / "features_all_models.csv")
    for gen in ["llama-3.2-3b", "mistral-7b-v0.3"]:
        feat_path = DATA / gen / "features_pythia410m.jsonl"
        records = []
        with open(feat_path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen
                records.append(rec)
        feat_base = pd.concat([feat_base, pd.DataFrame(records)], ignore_index=True)
    print(f"  Features: {len(feat_base)} rows")

    print("[4] Merging...")
    merged = merged.merge(feat_base[["model_name", "seed_id", "depth"] + FEAT_7],
                          on=["model_name", "seed_id", "depth"], how="left")
    merged = merged.reset_index(drop=True)

    needed = FEAT_7 + ["avg_logprob", "fastdetectgpt", "binoculars"]
    na_counts = merged[needed].isna().sum()
    na_any = na_counts[na_counts > 0]
    if len(na_any) > 0:
        print(f"  NaN: {dict(na_any)}")
    before = len(merged)
    merged = merged.dropna(subset=needed).reset_index(drop=True)
    if len(merged) < before:
        print(f"  Dropped {before - len(merged)} NaN rows, kept {len(merged)}")
    else:
        print(f"  Merged: {len(merged)} rows, no NaN")
    return merged


def main():
    t0 = time.time()
    print("=" * 70)
    print("D039 Table 3 Unified Evaluation (v4)")
    print("Tiered XGB | Pooled LOGO | No downsample | Dense top-10K trigrams")
    print("=" * 70)

    merged = load_all_data()

    print(f"\n[5] Building dense trigram matrix (top-10K)...")
    t_tri = time.time()
    tri_dense = build_trigram_dense(merged["text"].tolist(), max_vocab=10000)
    print(f"  Shape: {tri_dense.shape}, {tri_dense.nbytes/1e6:.0f}MB, built in {time.time()-t_tri:.1f}s")

    print(f"\n{'='*70}")
    print("LOGO Evaluation")
    print(f"{'='*70}")

    results = {}
    for name, (feats, xgb_params) in METHODS.items():
        use_tri = tri_dense if "ld_score" in feats else None
        config_name = "200/6" if xgb_params is XGB_ENSEMBLE else "100/3"

        t_m = time.time()
        print(f"\n  {name} ({config_name}, {len(feats)} features)...")

        f1_3c, pg_3c, yt_3c, yp_3c = logo_eval(merged, feats, xgb_params, ALL_8,
                                                  tri_dense=use_tri, binary=False)
        ci_3c = bootstrap_ci(yt_3c, yp_3c)
        print(f"    3-class F1={f1_3c} CI={ci_3c}")

        f1_bin, pg_bin, yt_bin, yp_bin = logo_eval(merged, feats, xgb_params, ALL_8,
                                                    tri_dense=use_tri, binary=True)
        ci_bin = bootstrap_ci(yt_bin, yp_bin)
        print(f"    Binary  F1={f1_bin} CI={ci_bin}")
        print(f"    ({time.time()-t_m:.1f}s)")

        results[name] = {
            "3class_f1": f1_3c,
            "3class_ci95": ci_3c,
            "3class_per_gen": pg_3c,
            "binary_f1": f1_bin,
            "binary_ci95": ci_bin,
            "binary_per_gen": pg_bin,
            "features": feats,
            "n_samples_3class": int(len(yt_3c)),
            "n_samples_binary": int(len(yt_bin)),
            "xgb_config": config_name,
        }

    print(f"\n{'='*93}")
    print(f"{'Method':<18} {'Config':<7} {'3class-F1':>10} {'3class-CI':>22} {'Binary-F1':>10} {'Binary-CI':>22}")
    print("-" * 93)
    for name in ["avg_logprob", "ld_score", "fastdetectgpt", "binoculars",
                 "4det_ensemble", "4det_surface", "7feature_ours"]:
        r = results[name]
        print(f"{name:<18} {r['xgb_config']:<7} {r['3class_f1']:>10.4f} "
              f"[{r['3class_ci95'][0]:.4f}, {r['3class_ci95'][1]:.4f}] "
              f"{r['binary_f1']:>10.4f} [{r['binary_ci95'][0]:.4f}, {r['binary_ci95'][1]:.4f}]")

    output = {
        "method": "pooled_logo",
        "n_generators": 8,
        "generators": ALL_8,
        "xgb_params": {
            "ensemble": {"n_estimators": 200, "max_depth": 6, "random_state": 42},
            "single": {"n_estimators": 100, "max_depth": 3, "random_state": 42},
        },
        "total_samples": {
            "3class": int(results["7feature_ours"]["n_samples_3class"]),
            "binary": int(results["7feature_ours"]["n_samples_binary"]),
        },
        "results": results,
        "notes": "D039 unified v4. Tiered XGB: ensemble(200/6) for >=3 features, single(100/3) for 1 feature. Dense top-10K trigram vocab. Same LOGO folds, pooled macro-F1, no downsample.",
    }

    out_path = RESULTS / "8gen_table3_unified.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
