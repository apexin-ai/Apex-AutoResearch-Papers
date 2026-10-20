#!/usr/bin/env python3
"""LD-Score sparse trigram JSD re-run (fixing v4 vocab truncation bug)."""

import json, time, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from scipy.sparse import lil_matrix
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

SEED = 42
N_BOOT = 1000

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
          "llama-3.2-3b", "mistral-7b-v0.3"]

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                  random_state=SEED, eval_metric="logloss", verbosity=0)

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


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    return pd.DataFrame(rows)


def build_trigram_matrix(texts, n=3):
    """Build character-level trigram count matrix as sparse CSR. NO vocab truncation."""
    vocab = {}
    rows_data = []
    for t in texts:
        t_lower = t.lower()
        c = Counter(t_lower[j:j+n] for j in range(len(t_lower) - n + 1))
        for ng in c:
            if ng not in vocab:
                vocab[ng] = len(vocab)
        rows_data.append(c)

    V = len(vocab)
    mat = lil_matrix((len(texts), V), dtype=np.float64)
    for i, c in enumerate(rows_data):
        total = sum(c.values())
        if total > 0:
            for ng, cnt in c.items():
                mat[i, vocab[ng]] = cnt / total
    return mat.tocsr(), list(vocab.keys())


def compute_ld_scores_vectorized(tri_matrix, ref_mask):
    """Batched JSD against mean reference distribution."""
    ref_rows = tri_matrix[ref_mask]
    if ref_rows.shape[0] == 0:
        return np.zeros(tri_matrix.shape[0])
    ref_dist = np.asarray(ref_rows.mean(axis=0)).flatten()
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist = ref_dist / ref_sum

    h_q = -np.sum(ref_dist[ref_dist > 0] * np.log(ref_dist[ref_dist > 0]))

    n = tri_matrix.shape[0]
    scores = np.zeros(n)
    batch_size = 4000

    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        batch = tri_matrix[start:end].toarray()
        row_sums = batch.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        batch = batch / row_sums
        safe_batch = np.where(batch > 0, batch, 1.0)
        h_p = -np.sum(batch * np.log(safe_batch), axis=1)
        m = (batch + ref_dist[np.newaxis, :]) / 2.0
        safe_m = np.where(m > 0, m, 1.0)
        h_m = -np.sum(m * np.log(safe_m), axis=1)
        jsd_sq = h_m - (h_p + h_q) / 2.0
        jsd_sq = np.clip(jsd_sq, 0, None)
        scores[start:end] = np.sqrt(jsd_sq)
    return scores


def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        scores.append(f1_score(y_true[idx], y_pred[idx], average='macro'))
    return [float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))]


def logo_eval(df, tri_matrix, binary=False):
    """LOGO with per-fold LD-score recomputation from sparse trigram matrix."""
    rng = np.random.RandomState(SEED)
    label_col = "label_bin" if binary else "label"
    preds = np.full(len(df), -1, dtype=int)
    per_gen = {}

    for g in sorted(ALL_8):
        tr_mask = (df["model_name"] != g).values
        te_mask = (df["model_name"] == g).values

        # Recompute LD-score per fold: reference = depth-0 in training set
        ref_mask = tr_mask & (df[label_col].values == 0)
        ld_all = compute_ld_scores_vectorized(tri_matrix, ref_mask)
        df["ld_score"] = ld_all

        train_df = df[tr_mask].copy()
        test_df = df[te_mask].copy()
        train_ds = downsample(train_df, label_col, rng)

        clf = XGBClassifier(**XGB_PARAMS)
        clf.fit(train_ds[["ld_score"]].values, train_ds[label_col].values)
        p = clf.predict(test_df[["ld_score"]].values)

        preds[te_mask] = p
        y_test = test_df[label_col].values
        per_gen[g] = float(f1_score(y_test, p, average='macro'))

    y_true = df[label_col].values
    valid = preds >= 0
    f1 = float(f1_score(y_true[valid], preds[valid], average='macro'))
    ci = bootstrap_ci(y_true[valid], preds[valid])
    return f1, ci, per_gen, int(valid.sum())


def main():
    t0 = time.time()
    print("=" * 60)
    print("LD-Score Sparse Trigram JSD — Fixed Re-run")
    print("=" * 60)

    # Load all texts
    print("\n[1] Loading texts...")
    all_rows = []
    for model in ALL_8:
        df = load_jsonl(JSONL_PATHS[model])
        df["model_name"] = model
        all_rows.append(df[["model_name", "seed_id", "depth", "text"]])
    merged = pd.concat(all_rows, ignore_index=True)
    print(f"  Total: {len(merged)} rows, generators: {sorted(merged['model_name'].unique())}")

    # Map labels
    merged["label"] = merged["depth"].map(CLASS_MAP)
    merged["label_bin"] = (merged["depth"] >= 2).astype(int)

    # Build sparse trigram matrix (full vocab, NO truncation)
    print("\n[2] Building sparse trigram matrix (full vocab)...")
    t1 = time.time()
    tri_matrix, vocab_list = build_trigram_matrix(merged["text"].tolist())
    print(f"  Shape: {tri_matrix.shape}, nnz: {tri_matrix.nnz}, vocab: {len(vocab_list)}")
    print(f"  Built in {time.time()-t1:.1f}s")

    # Binary evaluation (depth>=1 only, label: 1 vs 2+)
    print("\n[3] Binary LOGO (gen1 vs gen2+, exclude depth=0)...")
    merged_bin = merged[merged["depth"] >= 1].copy().reset_index(drop=True)
    # Rebuild trigram matrix for binary subset
    tri_matrix_bin, _ = build_trigram_matrix(merged_bin["text"].tolist())
    # For binary: label_bin = 0 if depth==1, 1 if depth>=2
    merged_bin["label_bin"] = (merged_bin["depth"] >= 2).astype(int)
    # Reference for binary LOGO: label_bin==0 (i.e. depth==1)
    bin_f1, bin_ci, bin_per_gen, n_bin = logo_eval(merged_bin, tri_matrix_bin, binary=True)
    print(f"  Binary F1={bin_f1:.4f} CI=[{bin_ci[0]:.4f}, {bin_ci[1]:.4f}] n={n_bin}")

    # 3-class evaluation (all depths, label: 0/1/2+)
    print("\n[4] 3-class LOGO (depth 0/1/2+)...")
    tri_3c = tri_matrix  # full dataset
    three_f1, three_ci, three_per_gen, n_3c = logo_eval(merged, tri_3c, binary=False)
    print(f"  3-class F1={three_f1:.4f} CI=[{three_ci[0]:.4f}, {three_ci[1]:.4f}] n={n_3c}")

    # Per-generator results
    print("\n  Per-generator binary F1:")
    for g in sorted(bin_per_gen.keys()):
        print(f"    {g}: {bin_per_gen[g]:.4f}")

    # Save
    output = {
        "ld_score_sparse": {
            "binary_f1": round(bin_f1, 4),
            "binary_ci": [round(x, 4) for x in bin_ci],
            "three_class_f1": round(three_f1, 4),
            "three_class_ci": [round(x, 4) for x in three_ci],
            "per_generator_binary": {g: round(v, 4) for g, v in bin_per_gen.items()},
            "per_generator_3class": {g: round(v, 4) for g, v in three_per_gen.items()}
        },
        "meta": {
            "implementation": "character-level trigram JSD (sparse CSR, full vocab, no truncation). Per-fold reference = mean trigram distribution of depth-0 (binary) or label-0 (3class) training samples.",
            "n_samples_binary": n_bin,
            "n_samples_3class": n_3c,
            "xgb_params": {"n_estimators": 100, "max_depth": 3, "learning_rate": 0.1},
            "seed": SEED,
            "bootstrap_n": N_BOOT,
            "protocol": "pooled LOGO 8-fold",
            "vocab_size": len(vocab_list),
            "trigram_type": "character-level (n=3)",
            "downsampling": "per-fold class-balanced (min-class)"
        }
    }

    out_path = RESULTS / "8gen_ldscore_sparse_fixed.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
