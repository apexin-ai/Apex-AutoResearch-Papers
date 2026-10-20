#!/usr/bin/env python3
"""
eval_table3_unified_v7.py
Unified XGBoost hyperparameters for ALL methods in Table 3.
Fix: v6 used (100,3) for baselines vs (200,6) for ours.
Now all methods use n_estimators=200, max_depth=6, learning_rate=0.1.
"""
import json, time, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from scipy.sparse import lil_matrix, csr_matrix
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

SEED = 42
N_BOOT = 1000

# Unified hyperparameters for ALL methods
XGB_N_EST = 200
XGB_DEPTH = 6
XGB_LR = 0.1

ALL_8 = sorted(["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
                "llama-3.2-3b", "mistral-7b-v0.3"])

JSONL_PATHS = {
    "pythia-2.8b": DATA / "generations.jsonl",
    "pythia-1b":   DATA / "pythia-1b" / "generations.jsonl",
    "olmo-2-1b":   DATA / "olmo-2-1b" / "generations.jsonl",
    "qwen3-0.6b":  DATA / "qwen3-0.6b" / "generations.jsonl",
    "qwen3-1.7b":  DATA / "qwen3-1.7b" / "generations.jsonl",
    "qwen3-8b":    DATA / "qwen3-8b" / "generations.jsonl",
    "llama-3.2-3b": DATA / "llama-3.2-3b" / "generations_filtered.jsonl",
    "mistral-7b-v0.3": DATA / "mistral-7b-v0.3" / "generations_filtered.jsonl",
}

METHODS = {
    "avg_logprob": {"features": ["avg_logprob"]},
    "fastdetectgpt": {"features": ["fastdetectgpt"]},
    "binoculars": {"features": ["binoculars"]},
    "ld_score": {"features": ["ld_score"]},
    "entropy_mean": {"features": ["entropy_mean"]},
    "4det_ensemble": {"features": ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"]},
    "4det_surface": {"features": ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score", "ttr", "hapax_ratio"]},
    "7feature_ours": {"features": ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "ttr", "hapax_ratio", "tail_decay"]},
}


def balance_classes(df, label_col='label', seed=42):
    rng = np.random.RandomState(seed)
    min_count = df[label_col].value_counts().min()
    balanced = []
    for cls in sorted(df[label_col].unique()):
        cls_df = df[df[label_col] == cls]
        if len(cls_df) > min_count:
            cls_df = cls_df.sample(n=min_count, random_state=rng)
        balanced.append(cls_df)
    return pd.concat(balanced, ignore_index=True)


def load_data():
    det = pd.read_csv(DATA / "detector_scores_8gen.csv")
    print(f"  detector_scores_8gen: {len(det)} rows")
    feat6 = pd.read_csv(DATA / "features_all_models.csv")
    extra_feats = []
    for model, fname in [("llama-3.2-3b", "features_olmo2-1b.jsonl"),
                         ("mistral-7b-v0.3", "features_olmo2-1b.jsonl")]:
        rows = []
        with open(DATA / model / fname) as f:
            for line in f:
                rows.append(json.loads(line))
        mdf = pd.DataFrame(rows)
        mdf["model_name"] = model
        extra_feats.append(mdf)
    feat_all = pd.concat([feat6] + extra_feats, ignore_index=True)
    df = det.merge(feat_all, on=["model_name", "seed_id", "depth"], how="left")
    feature_cols = ["avg_logprob", "fastdetectgpt", "binoculars",
                    "entropy_mean", "entropy_std", "entropy_min", "entropy_max",
                    "tail_decay", "ttr", "hapax_ratio"]
    for col in feature_cols:
        if col in df.columns:
            n_nan = df[col].isna().sum()
            if n_nan > 0:
                df[col] = df[col].fillna(df[col].median())
                print(f"  WARNING: filled {n_nan} NaN in '{col}'")
    print(f"  Final merged: {len(df)} rows, {len(df['model_name'].unique())} generators")
    return df


def load_texts_aligned(df):
    text_map = {}
    for model in ALL_8:
        with open(JSONL_PATHS[model]) as f:
            for line in f:
                row = json.loads(line)
                text_map[(model, row["seed_id"], row["depth"])] = row["text"]
    texts = []
    missing = 0
    for _, r in df.iterrows():
        key = (r["model_name"], r["seed_id"], r["depth"])
        t = text_map.get(key, "")
        if not t:
            missing += 1
        texts.append(t)
    if missing > 0:
        print(f"  WARNING: {missing} rows missing text")
    return texts


def build_trigram_matrix(texts, n=3):
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
    return mat.tocsr(), vocab


def compute_ld_scores_sparse(tri_matrix, ref_mask):
    ref_rows = tri_matrix[ref_mask]
    if ref_rows.shape[0] == 0:
        return np.zeros(tri_matrix.shape[0])
    ref_dist = np.asarray(ref_rows.mean(axis=0)).flatten()
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist = ref_dist / ref_sum
    ref_pos = ref_dist > 0
    log_ref = np.zeros_like(ref_dist)
    log_ref[ref_pos] = np.log(ref_dist[ref_pos])
    h_ref = -np.sum(ref_dist[ref_pos] * log_ref[ref_pos])
    baseline_hm = h_ref / 2.0 + np.log(2) / 2.0
    n = tri_matrix.shape[0]
    scores = np.zeros(n)
    for i in range(n):
        row_start = tri_matrix.indptr[i]
        row_end = tri_matrix.indptr[i+1]
        if row_start == row_end:
            scores[i] = 0.0
            continue
        cols = tri_matrix.indices[row_start:row_end]
        p_vals = tri_matrix.data[row_start:row_end]
        p_sum = p_vals.sum()
        if p_sum > 0 and abs(p_sum - 1.0) > 1e-10:
            p_vals = p_vals / p_sum
        h_p = -np.sum(p_vals * np.log(p_vals))
        ref_at_cols = ref_dist[cols]
        m_vals = (p_vals + ref_at_cols) / 2.0
        old_contribution = 0.0
        mask_ref_pos = ref_at_cols > 0
        if mask_ref_pos.any():
            r_pos = ref_at_cols[mask_ref_pos]
            old_contribution = -np.sum(r_pos / 2.0 * np.log(r_pos / 2.0))
        m_pos = m_vals > 0
        new_contribution = -np.sum(m_vals[m_pos] * np.log(m_vals[m_pos]))
        h_m = baseline_hm - old_contribution + new_contribution
        jsd = h_m - (h_p + h_ref) / 2.0
        jsd = max(jsd, 0.0)
        scores[i] = np.sqrt(jsd)
    return scores


def precompute_ld_scores_per_fold(df, tri_matrix, generators):
    print("  Pre-computing per-fold LD-scores...")
    t0 = time.time()
    ld_cache = {}
    for task in ["binary", "multiclass"]:
        for held_out in generators:
            tr_mask = (df['model_name'] != held_out).values
            if task == "binary":
                ref_mask = tr_mask & (df['depth'] == 1).values
            else:
                ref_mask = tr_mask & (df['depth'] == 0).values
            scores = compute_ld_scores_sparse(tri_matrix, ref_mask)
            ld_cache[(task, held_out)] = scores
            elapsed = time.time() - t0
            print(f"    {task}/{held_out}: done ({elapsed:.1f}s cumulative)")
    print(f"  LD-score pre-computation total: {time.time()-t0:.1f}s")
    return ld_cache


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        scores.append(f1_score(y_true[idx], y_pred[idx], average='macro'))
    return (float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5)))


def pooled_logo_eval(df, features, task, generators, ld_cache=None):
    needs_ld = "ld_score" in features
    all_true, all_pred = [], []
    for fold_i, held_out in enumerate(generators):
        tr_mask = df['model_name'] != held_out
        te_mask = df['model_name'] == held_out
        if task == "binary":
            subset = df['depth'] >= 1
            tr_idx = tr_mask & subset
            te_idx = te_mask & subset
        else:
            tr_idx = tr_mask
            te_idx = te_mask
        train = df[tr_idx].copy()
        test = df[te_idx].copy()
        if task == "binary":
            train['label'] = (train['depth'] >= 2).astype(int)
            test['label'] = (test['depth'] >= 2).astype(int)
        else:
            train['label'] = train['depth'].clip(upper=2).astype(int)
            test['label'] = test['depth'].clip(upper=2).astype(int)
        if needs_ld:
            ld_all = ld_cache[(task, held_out)]
            train['ld_score'] = ld_all[tr_idx.values]
            test['ld_score'] = ld_all[te_idx.values]
        train_before = len(train)
        train = balance_classes(train, label_col='label', seed=SEED)
        if fold_i == 0:
            cls_dist = train['label'].value_counts().to_dict()
            print(f"    Fold 0 ({held_out}) balance: {train_before} -> {len(train)}, dist={cls_dist}")
        X_train = train[features].values
        y_train = train['label'].values
        X_test = test[features].values
        y_test = test['label'].values
        if len(train) < 100:
            print(f"    WARNING: fold {held_out} has only {len(train)} training samples after balancing")
        clf = XGBClassifier(n_estimators=XGB_N_EST, max_depth=XGB_DEPTH,
                            learning_rate=XGB_LR,
                            random_state=SEED, eval_metric='logloss', verbosity=0)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        all_true.extend(y_test.tolist())
        all_pred.extend(y_pred.tolist())
    return float(f1_score(np.array(all_true), np.array(all_pred), average='macro')), np.array(all_true), np.array(all_pred)


def main():
    t0 = time.time()
    print("=" * 60)
    print("Table 3 Unified V7 — ALL methods use identical XGBoost config")
    print(f"  n_estimators={XGB_N_EST}, max_depth={XGB_DEPTH}, learning_rate={XGB_LR}")
    print("=" * 60)

    print("\n[1] Loading features...")
    df = load_data()
    generators = sorted(df['model_name'].unique())
    print(f"  Generators: {generators}")

    print("\n[2] Loading texts & building trigram matrix...")
    texts = load_texts_aligned(df)
    print(f"  Texts loaded: {len(texts)}")
    t1 = time.time()
    tri_matrix, vocab = build_trigram_matrix(texts)
    print(f"  Trigram matrix: {tri_matrix.shape}, nnz={tri_matrix.nnz}, vocab={len(vocab)}, {time.time()-t1:.1f}s")

    print("\n[3] Pre-computing LD-scores (16 folds)...")
    ld_cache = precompute_ld_scores_per_fold(df, tri_matrix, generators)

    print("\n[4] Running evaluations...")
    results = {}
    for method_name, config in METHODS.items():
        t_m = time.time()
        features = config['features']
        needs_ld = "ld_score" in features
        print(f"\n  --- {method_name} (est={XGB_N_EST}, depth={XGB_DEPTH}, lr={XGB_LR}) ---")
        binary_f1, bt, bp = pooled_logo_eval(
            df, features, "binary", generators, ld_cache if needs_ld else None)
        multi_f1, mt, mp = pooled_logo_eval(
            df, features, "multiclass", generators, ld_cache if needs_ld else None)
        b_ci = bootstrap_ci(bt, bp)
        m_ci = bootstrap_ci(mt, mp)
        results[method_name] = {
            "binary_f1": round(binary_f1, 4),
            "binary_ci_lo": round(b_ci[0], 4),
            "binary_ci_hi": round(b_ci[1], 4),
            "multiclass_f1": round(multi_f1, 4),
            "multiclass_ci_lo": round(m_ci[0], 4),
            "multiclass_ci_hi": round(m_ci[1], 4),
            "n_test_binary": int(len(bt)),
            "n_test_multiclass": int(len(mt))
        }
        print(f"  {method_name}: binary={binary_f1:.4f} [{b_ci[0]:.4f},{b_ci[1]:.4f}], "
              f"multi={multi_f1:.4f} [{m_ci[0]:.4f},{m_ci[1]:.4f}] ({time.time()-t_m:.1f}s)")

    output = {
        "methods": results,
        "meta": {
            "protocol": "pooled LOGO 8-fold, per-fold class-balanced training",
            "binary_task": "gen_depth==1 vs gen_depth>=2 (exclude depth=0)",
            "multiclass_task": "gen_depth==0 vs gen_depth==1 vs gen_depth>=2",
            "seed": SEED,
            "bootstrap_n": N_BOOT,
            "bootstrap_method": "percentile (2.5%, 97.5%)",
            "n_total_rows": len(df),
            "n_binary_rows": int((df['depth'] >= 1).sum()),
            "generators": generators,
            "class_balancing": "per-fold downsample to min class in train set",
            "hyperparams_unified": {
                "n_estimators": XGB_N_EST,
                "max_depth": XGB_DEPTH,
                "learning_rate": XGB_LR,
                "note": "identical for ALL methods"
            },
            "ld_score_impl": "char trigram JSD (sparse CSR, full vocab, no truncation). Per-fold ref = training depth-1 (binary) / depth-0 (3class).",
            "trigram_vocab_size": len(vocab),
            "xgb_eval_metric": "logloss",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "fix_note": "v7 fixes v6 hyperparameter inconsistency: v6 used (100,3) for baselines vs (200,6) for ours"
        }
    }
    out_path = RESULTS / "8gen_table3_v7_unified.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
