#!/usr/bin/env python3
"""ROC-AUC for binary (gen-1 vs gen-2+) LOGO evaluation with bootstrap CI."""
import warnings; warnings.filterwarnings('ignore')
import json, time, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from sklearn.metrics import f1_score, roc_auc_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

N_BOOT = 1000
LOGO_SEED = 789
BOOT_SEED = 42

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
          "llama-3.2-3b", "mistral-7b-v0.3"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_BASE = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                random_state=LOGO_SEED, eval_metric="logloss", verbosity=0)
XGB_OURS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                random_state=LOGO_SEED, eval_metric="logloss", verbosity=0)

FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]

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

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)
EPS = 1e-10


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


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_eval_auc(df, feat_cols, params, gens, tri_dense=None):
    """LOGO binary evaluation returning F1, ROC-AUC, and per-sample probabilities."""
    rng = np.random.RandomState(LOGO_SEED)
    label_col = "label_bin"
    preds = np.full(len(df), -1, dtype=int)
    probs = np.full(len(df), np.nan, dtype=float)

    for g in sorted(gens):
        t_f = time.time()
        tr_mask = (df["model_name"] != g).values
        te_mask = (df["model_name"] == g).values

        if "ld_score" in feat_cols and tri_dense is not None:
            ref_mask = tr_mask & (df[label_col].values == 0)
            ld_all = compute_jsd_vectorized(tri_dense, ref_mask)
            df["ld_score"] = ld_all

        train_df = df[tr_mask].copy()
        test_df = df[te_mask].copy()
        train_ds = downsample(train_df, label_col, rng)
        clf = XGBClassifier(**params)
        clf.fit(train_ds[feat_cols].values, train_ds[label_col].values)
        p = clf.predict(test_df[feat_cols].values)
        prob = clf.predict_proba(test_df[feat_cols].values)[:, 1]
        preds[te_mask] = p
        probs[te_mask] = prob
        print(f"      {g}: {te_mask.sum()} samples, {time.time()-t_f:.1f}s")

    y_true = df[label_col].values
    valid = preds >= 0
    yt, yp, yprob = y_true[valid], preds[valid], probs[valid]
    sids = df.loc[valid, "seed_id"].values
    pooled_f1 = round(float(f1_score(yt, yp, average="macro")), 4)
    auc = round(float(roc_auc_score(yt, yprob)), 4)
    return pooled_f1, auc, yt, yprob, sids


def bootstrap_ci_auc(y_true, y_prob, seed_ids, n_boot=N_BOOT, seed=BOOT_SEED):
    """Document-level bootstrap CI for ROC-AUC."""
    rng = np.random.RandomState(seed)
    unique_seeds = np.unique(seed_ids)
    n_seeds = len(unique_seeds)
    seed_idx = {}
    for i, sid in enumerate(seed_ids):
        if sid not in seed_idx:
            seed_idx[sid] = []
        seed_idx[sid].append(i)
    seed_idx = {s: np.array(v) for s, v in seed_idx.items()}
    seed_list = list(unique_seeds)

    scores = []
    for _ in range(n_boot):
        chosen = rng.choice(n_seeds, size=n_seeds, replace=True)
        idx = np.concatenate([seed_idx[seed_list[c]] for c in chosen])
        yt, yp = y_true[idx], y_prob[idx]
        if len(np.unique(yt)) < 2:
            continue
        scores.append(roc_auc_score(yt, yp))
    arr = np.array(scores)
    return [round(float(np.percentile(arr, 2.5)), 4),
            round(float(np.percentile(arr, 97.5)), 4)]


def main():
    t0 = time.time()
    print("=" * 60)
    print("ROC-AUC Baselines: Binary LOGO (gen-1 vs gen-2+)")
    print("=" * 60)

    # --- Load data ---
    print("\n[1] Loading texts...")
    text_records = []
    for model_name, path in JSONL_PATHS.items():
        if model_name not in ALL_8:
            continue
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
    text_df = text_df.reset_index(drop=True)
    print(f"  {len(text_df)} rows")

    print("\n[2] Loading detector scores + features...")
    scores_8gen = pd.read_csv(DATA / "detector_scores_8gen.csv")
    merged = text_df.merge(
        scores_8gen[["model_name", "seed_id", "depth", "avg_logprob", "fastdetectgpt", "binoculars"]],
        on=["model_name", "seed_id", "depth"], how="left")
    merged = merged.reset_index(drop=True)

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

    merged = merged.merge(feat_base[["model_name", "seed_id", "depth"] + FEAT_7],
                          on=["model_name", "seed_id", "depth"], how="left")
    merged = merged.reset_index(drop=True)
    merged["label_bin"] = merged["label"].map({0: -1, 1: 0, 2: 1})
    print(f"  Merged: {len(merged)} rows")

    # Binary subset
    bin_mask = merged["label_bin"] >= 0
    merged_bin = merged[bin_mask].copy().reset_index(drop=True)

    # Trigram matrix
    print("\n[3] Building trigram matrix (top-10K vocab)...")
    t_tri = time.time()
    tri_dense = build_trigram_dense(merged["text"].tolist(), max_vocab=10000)
    print(f"  Shape: {tri_dense.shape}, built in {time.time()-t_tri:.1f}s")
    tri_dense_bin = tri_dense[bin_mask.values]

    # --- Evaluation ---
    print("\n" + "=" * 60)
    print("LOGO Binary ROC-AUC Evaluation")
    print("=" * 60)
    results = {}

    methods = [
        ("fastdetectgpt", ["fastdetectgpt"], XGB_BASE, False),
        ("binoculars", ["binoculars"], XGB_BASE, False),
        ("avg_logprob", ["avg_logprob"], XGB_BASE, False),
        ("ld_score", ["ld_score"], XGB_BASE, True),
        ("4det_ensemble", ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"], XGB_BASE, True),
        ("7feature_ours", FEAT_7, XGB_OURS, False),
        ("combined", ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"] + FEAT_7, XGB_OURS, True),
    ]

    for name, feats, params, needs_tri in methods:
        print(f"\n  {name}...")
        td = tri_dense_bin if needs_tri else None
        f1, auc, yt, yprob, sids = logo_eval_auc(merged_bin, feats, params, ALL_8, tri_dense=td)
        ci = bootstrap_ci_auc(yt, yprob, sids)
        results[name] = {"binary_f1": f1, "roc_auc": auc, "roc_auc_ci": ci}
        print(f"    F1={f1}  AUC={auc}  CI={ci}")

    # --- Summary ---
    print("\n" + "=" * 84)
    print(f"{'Method':<18} {'Binary F1':>10} {'ROC-AUC':>10} {'95% CI':>22}")
    print("-" * 62)
    for name in ["fastdetectgpt", "binoculars", "avg_logprob", "ld_score",
                 "4det_ensemble", "7feature_ours", "combined"]:
        r = results[name]
        ci = r["roc_auc_ci"]
        print(f"{name:<18} {r['binary_f1']:>10.4f} {r['roc_auc']:>10.4f}"
              f" [{ci[0]:.4f}, {ci[1]:.4f}]")

    # Save
    with open(RESULTS / "roc_auc_baselines.json", "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {RESULTS / 'roc_auc_baselines.json'}")
    print(f"Total: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
