#!/usr/bin/env python3
"""Table 4 unified grid search: all methods x {n_est:[100,200]} x {max_depth:[3,6]}
8-gen LOGO, class-balanced downsampling, pooled F1.
"""
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
    "avg_logprob":     ["avg_logprob"],
    "fastdetectgpt":   ["fastdetectgpt"],
    "binoculars":      ["binoculars"],
    "ld_score":        ["ld_score"],
    "4det_ensemble":   ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"],
    "4det_surface":    ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score", "ttr", "hapax_ratio"],
    "7feature_ours":   ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "ttr", "hapax_ratio", "tail_decay"],
}

GRID = [(ne, md) for ne in [100, 200] for md in [3, 6]]


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
    print(f"  Loaded: {len(df)} rows, {len(df['model_name'].unique())} generators")
    return df


def load_texts_aligned(df):
    text_map = {}
    for model in ALL_8:
        with open(JSONL_PATHS[model]) as f:
            for line in f:
                row = json.loads(line)
                text_map[(model, row["seed_id"], row["depth"])] = row["text"]
    texts = []
    for _, r in df.iterrows():
        key = (r["model_name"], r["seed_id"], r["depth"])
        texts.append(text_map.get(key, ""))
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
        p_vals = tri_matrix.data[row_start:row_end].copy()
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


def precompute_ld_scores(df, tri_matrix, generators):
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
    print(f"  LD-score done: {time.time()-t0:.1f}s")
    return ld_cache


def pooled_logo_eval(df, features, n_estimators, max_depth, task, generators, ld_cache=None):
    needs_ld = "ld_score" in features
    all_true, all_pred = [], []
    for held_out in generators:
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
        train = balance_classes(train, label_col='label', seed=SEED)
        X_train = train[features].values
        y_train = train['label'].values
        X_test = test[features].values
        y_test = test['label'].values
        clf = XGBClassifier(n_estimators=n_estimators, max_depth=max_depth,
                            learning_rate=0.1, random_state=SEED,
                            eval_metric='logloss', verbosity=0)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        all_true.extend(y_test.tolist())
        all_pred.extend(y_pred.tolist())
    return float(f1_score(np.array(all_true), np.array(all_pred), average='macro'))


def main():
    t0 = time.time()
    print("=" * 60)
    print("Table 4 Grid Search: 7 methods x 4 configs x {binary,3class}")
    print("=" * 60)

    print("\n[1] Loading data...")
    df = load_data()
    generators = sorted(df['model_name'].unique())
    print(f"  Generators: {generators}")

    print("\n[2] Loading texts & trigram matrix...")
    texts = load_texts_aligned(df)
    tri_matrix, vocab = build_trigram_matrix(texts)
    print(f"  Trigram: {tri_matrix.shape}, vocab={len(vocab)}")

    print("\n[3] Pre-computing LD-scores...")
    ld_cache = precompute_ld_scores(df, tri_matrix, generators)

    print("\n[4] Grid search...")
    results = {}
    total_evals = len(METHODS) * len(GRID) * 2
    done = 0
    for method_name, features in METHODS.items():
        needs_ld = "ld_score" in features
        method_results = {}
        for n_est, md in GRID:
            config_key = f"est{n_est}_md{md}"
            t_c = time.time()
            binary_f1 = pooled_logo_eval(
                df, features, n_est, md, "binary", generators,
                ld_cache if needs_ld else None)
            multi_f1 = pooled_logo_eval(
                df, features, n_est, md, "multiclass", generators,
                ld_cache if needs_ld else None)
            done += 2
            method_results[config_key] = {
                "n_estimators": n_est,
                "max_depth": md,
                "binary_f1": round(binary_f1, 4),
                "multiclass_f1": round(multi_f1, 4),
            }
            print(f"  [{done}/{total_evals}] {method_name} {config_key}: "
                  f"binary={binary_f1:.4f}, multi={multi_f1:.4f} ({time.time()-t_c:.1f}s)")

        best_multi = max(method_results.values(), key=lambda x: x["multiclass_f1"])
        best_binary = max(method_results.values(), key=lambda x: x["binary_f1"])
        results[method_name] = {
            "features": features,
            "configs": method_results,
            "best_multiclass": {
                "config": f"est{best_multi['n_estimators']}_md{best_multi['max_depth']}",
                "multiclass_f1": best_multi["multiclass_f1"],
                "binary_f1": best_multi["binary_f1"],
            },
            "best_binary": {
                "config": f"est{best_binary['n_estimators']}_md{best_binary['max_depth']}",
                "binary_f1": best_binary["binary_f1"],
                "multiclass_f1": best_binary["multiclass_f1"],
            },
        }

    output = {
        "methods": results,
        "meta": {
            "protocol": "pooled LOGO 8-fold, per-fold class-balanced training",
            "binary_task": "depth>=1, y=(depth>=2)",
            "multiclass_task": "depth clipped to {0,1,2}",
            "grid": [{"n_estimators": ne, "max_depth": md} for ne, md in GRID],
            "learning_rate": 0.1,
            "seed": SEED,
            "generators": generators,
            "n_rows": len(df),
            "ld_score_note": "per-fold ref: train depth-1 (binary) / depth-0 (3class)",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_time_s": round(time.time() - t0, 1),
        }
    }
    out_path = RESULTS / "table4_grid_search.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")

    print("\n" + "=" * 60)
    print("SUMMARY (best multiclass config per method)")
    print("=" * 60)
    for m, r in results.items():
        bm = r["best_multiclass"]
        bb = r["best_binary"]
        print(f"  {m:20s}  best_3class={bm['multiclass_f1']:.4f} ({bm['config']})"
              f"  best_binary={bb['binary_f1']:.4f} ({bb['config']})")


if __name__ == "__main__":
    main()
