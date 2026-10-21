#!/usr/bin/env python3
"""8-gen LOGO baselines: per-gen held-out evaluation for 4 detectors + ensembles.

Uses pre-computed detector scores (avg_logprob, fastdetectgpt, binoculars) from
detector_scores_8gen.csv. Computes LD score on-the-fly from trigram distributions.
"""

import warnings; warnings.filterwarnings('ignore')
import json, time, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

N_BOOT = 1000
LOGO_SEED = 789
BOOT_SEED = 42
EPS = 1e-10

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
          "llama-3.2-3b", "mistral-7b-v0.3"]

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_BASE = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
                random_state=LOGO_SEED, eval_metric="mlogloss", verbosity=0)
XGB_OURS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                random_state=LOGO_SEED, eval_metric="mlogloss", verbosity=0)

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


def load_features_8gen():
    df6 = pd.read_csv(DATA / "features_all_models.csv")
    new_dfs = []
    for gen in ["llama-3.2-3b", "mistral-7b-v0.3"]:
        path = DATA / gen / "features_pythia410m.jsonl"
        rows = []
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                r["model_name"] = gen
                rows.append(r)
        new_dfs.append(pd.DataFrame(rows))
    df_new = pd.concat(new_dfs, ignore_index=True)
    return pd.concat([df6, df_new], ignore_index=True)


def load_texts():
    texts_dict = {}
    for gen, path in JSONL_PATHS.items():
        if not path.exists():
            print(f"  WARNING: {path} not found")
            continue
        with open(path) as f:
            for line in f:
                r = json.loads(line)
                sid = r.get("seed_id", r.get("id", 0))
                depth = r.get("depth", 0)
                text = r.get("text", r.get("generation", ""))
                texts_dict[(gen, sid, depth)] = text
    return texts_dict


def build_trigram_matrix(texts, max_vocab=10000):
    vocab_counts = Counter()
    rows_data = []
    for t in texts:
        t_lower = t.lower()
        c = Counter(t_lower[j:j+3] for j in range(len(t_lower) - 2))
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


def compute_ld_scores(tri_matrix, ref_mask):
    ref_dist = tri_matrix[ref_mask].mean(axis=0)
    ref_sum = ref_dist.sum()
    if ref_sum > 0:
        ref_dist = ref_dist / ref_sum
    else:
        return np.zeros(tri_matrix.shape[0])
    q = ref_dist[np.newaxis, :] + EPS
    q = q / q.sum()
    p = tri_matrix + EPS
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


def logo_eval_full(merged, tri_matrix, feat_cols, params_3class, params_binary, gens):
    """Run LOGO for both 3-class and binary in one pass.
    
    Computes LD from full data's depth-0 reference (per fold), then evaluates
    both 3-class (full data) and binary (depth>0 subset).
    """
    rng_3 = np.random.RandomState(LOGO_SEED)
    rng_b = np.random.RandomState(LOGO_SEED)

    per_gen_3class = {}
    per_gen_binary = {}
    all_yt_3, all_yp_3 = [], []
    all_yt_b, all_yp_b = [], []

    needs_ld = "ld_score" in feat_cols

    for g in sorted(gens):
        tr_mask = (merged["model_name"] != g).values
        te_mask = (merged["model_name"] == g).values

        # Compute LD using full data, depth-0 from training as reference
        if needs_ld and tri_matrix is not None:
            ref_mask = tr_mask & (merged["depth"].values == 0)
            ld_vals = compute_ld_scores(tri_matrix, ref_mask)
            df_fold = merged.copy()
            df_fold["ld_score"] = ld_vals
        else:
            df_fold = merged

        # --- 3-class ---
        tr_df_3 = downsample(df_fold[tr_mask].reset_index(drop=True), "label", rng_3)
        te_df_3 = df_fold[te_mask].reset_index(drop=True)

        X_tr = tr_df_3[feat_cols].values
        y_tr = tr_df_3["label"].values
        X_te = te_df_3[feat_cols].values
        y_te = te_df_3["label"].values

        n_classes = len(np.unique(y_tr))
        clf = XGBClassifier(num_class=n_classes if n_classes > 2 else None, **params_3class)
        clf.fit(X_tr, y_tr)
        y_pred = clf.predict(X_te)
        f1_3 = round(float(f1_score(y_te, y_pred, average="macro")), 4)
        per_gen_3class[g] = f1_3
        all_yt_3.extend(y_te.tolist())
        all_yp_3.extend(y_pred.tolist())

        # --- Binary (exclude label=0, then 1 vs 2+) ---
        bin_mask_tr = tr_mask & (merged["label"].values != 0)
        bin_mask_te = te_mask & (merged["label"].values != 0)

        df_bin_tr = df_fold[bin_mask_tr].copy()
        df_bin_te = df_fold[bin_mask_te].copy()
        df_bin_tr["label_bin"] = (df_bin_tr["label"] >= 2).astype(int)
        df_bin_te["label_bin"] = (df_bin_te["label"] >= 2).astype(int)

        df_bin_tr = downsample(df_bin_tr.reset_index(drop=True), "label_bin", rng_b)
        df_bin_te = df_bin_te.reset_index(drop=True)

        X_tr_b = df_bin_tr[feat_cols].values
        y_tr_b = df_bin_tr["label_bin"].values
        X_te_b = df_bin_te[feat_cols].values
        y_te_b = df_bin_te["label_bin"].values

        if len(np.unique(y_tr_b)) < 2:
            per_gen_binary[g] = 0.0
            continue

        clf_b = XGBClassifier(**params_binary)
        clf_b.fit(X_tr_b, y_tr_b)
        y_pred_b = clf_b.predict(X_te_b)
        f1_b = round(float(f1_score(y_te_b, y_pred_b, average="macro")), 4)
        per_gen_binary[g] = f1_b
        all_yt_b.extend(y_te_b.tolist())
        all_yp_b.extend(y_pred_b.tolist())

    avg_f1_3 = round(float(np.mean(list(per_gen_3class.values()))), 4)
    avg_f1_b = round(float(np.mean(list(per_gen_binary.values()))), 4)
    return (avg_f1_3, per_gen_3class, np.array(all_yt_3), np.array(all_yp_3),
            avg_f1_b, per_gen_binary, np.array(all_yt_b), np.array(all_yp_b))


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=BOOT_SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    if n == 0:
        return [0.0, 0.0]
    scores = []
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        s = f1_score(y_true[idx], y_pred[idx], average="macro")
        scores.append(s)
    return [round(float(np.percentile(scores, 2.5)), 4),
            round(float(np.percentile(scores, 97.5)), 4)]


def main():
    t0 = time.time()
    print("=" * 70)
    print("8-gen LOGO Baselines Evaluation (v2 - fixed LD binary)")
    print("=" * 70)

    # --- Load & merge data ---
    print("\n[1] Loading detector scores...")
    det_df = pd.read_csv(DATA / "detector_scores_8gen.csv")
    print(f"  {len(det_df)} rows, gens={sorted(det_df['model_name'].unique())}")

    print("[2] Loading 7-feature data...")
    feat_df = load_features_8gen()
    print(f"  {len(feat_df)} rows")

    print("[3] Merging...")
    merged = det_df.merge(feat_df, on=["model_name", "seed_id", "depth"], how="inner")
    merged["label"] = merged["label"].map(lambda x: CLASS_MAP.get(int(x), int(x)))
    print(f"  merged: {len(merged)} rows, labels={sorted(merged['label'].unique())}")

    print("[4] Loading texts for LD...")
    texts_dict = load_texts()
    texts_list = []
    for _, row in merged.iterrows():
        key = (row["model_name"], int(row["seed_id"]), int(row["depth"]))
        texts_list.append(texts_dict.get(key, ""))
    print(f"  {len(texts_list)} texts matched")

    print("[5] Building trigram matrix...")
    tri_matrix = build_trigram_matrix(texts_list)
    print(f"  shape: {tri_matrix.shape}")

    # --- Evaluate ---
    print("\n" + "=" * 70)
    print("LOGO Evaluation (8-fold)")
    print("=" * 70)

    results = {}

    # Single detectors
    single_dets = {
        "avg_logprob": ["avg_logprob"],
        "fastdetectgpt": ["fastdetectgpt"],
        "binoculars": ["binoculars"],
        "ld_score": ["ld_score"],
    }

    for name, feats in single_dets.items():
        print(f"\n  {name}...")
        use_tri = tri_matrix if "ld_score" in feats else None
        (f1_3, pg3, yt3, yp3,
         f1_b, pgb, ytb, ypb) = logo_eval_full(merged, use_tri, feats, XGB_BASE, XGB_BASE, ALL_8)
        ci3 = bootstrap_ci(yt3, yp3)
        cib = bootstrap_ci(ytb, ypb)
        results[name] = {
            "3class_f1": f1_3, "3class_ci95": ci3, "per_gen_3class": pg3,
            "binary_f1": f1_b, "binary_ci95": cib, "per_gen_binary": pgb,
        }
        print(f"    3class={f1_3} CI={ci3}  binary={f1_b} CI={cib}")

    # 4det_ensemble (XGB 100/3)
    print(f"\n  4det_ensemble...")
    ens_feats = ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"]
    (f1_3, pg3, yt3, yp3,
     f1_b, pgb, ytb, ypb) = logo_eval_full(merged, tri_matrix, ens_feats, XGB_BASE, XGB_BASE, ALL_8)
    ci3 = bootstrap_ci(yt3, yp3)
    cib = bootstrap_ci(ytb, ypb)
    results["4det_ensemble"] = {
        "3class_f1": f1_3, "3class_ci95": ci3, "per_gen_3class": pg3,
        "binary_f1": f1_b, "binary_ci95": cib, "per_gen_binary": pgb,
    }
    print(f"    3class={f1_3} CI={ci3}  binary={f1_b} CI={cib}")

    # 4det_surface (XGB 200/6)
    print(f"\n  4det_surface...")
    surf_feats = ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score", "ttr", "hapax_ratio"]
    (f1_3, pg3, yt3, yp3,
     f1_b, pgb, ytb, ypb) = logo_eval_full(merged, tri_matrix, surf_feats, XGB_OURS, XGB_OURS, ALL_8)
    ci3 = bootstrap_ci(yt3, yp3)
    cib = bootstrap_ci(ytb, ypb)
    results["4det_surface"] = {
        "3class_f1": f1_3, "3class_ci95": ci3, "per_gen_3class": pg3,
        "binary_f1": f1_b, "binary_ci95": cib, "per_gen_binary": pgb,
    }
    print(f"    3class={f1_3} CI={ci3}  binary={f1_b} CI={cib}")

    # 7feature_ours (XGB 200/6)
    print(f"\n  7feature_ours...")
    (f1_3, pg3, yt3, yp3,
     f1_b, pgb, ytb, ypb) = logo_eval_full(merged, None, FEAT_7, XGB_OURS, XGB_OURS, ALL_8)
    ci3 = bootstrap_ci(yt3, yp3)
    cib = bootstrap_ci(ytb, ypb)
    results["7feature_ours"] = {
        "3class_f1": f1_3, "3class_ci95": ci3, "per_gen_3class": pg3,
        "binary_f1": f1_b, "binary_ci95": cib, "per_gen_binary": pgb,
    }
    print(f"    3class={f1_3} CI={ci3}  binary={f1_b} CI={cib}")

    # --- Format & save ---
    output = {
        "method": "LOGO",
        "n_generators": 8,
        "generators": ALL_8,
        "baselines": {},
        "ensembles": {},
        "7feature_ours": {},
        "config": {
            "xgb_n_estimators_baseline": 100, "xgb_max_depth_baseline": 3,
            "xgb_n_estimators_ours": 200, "xgb_max_depth_ours": 6,
            "bootstrap_n": N_BOOT, "logo_seed": LOGO_SEED,
        }
    }

    for name in ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"]:
        r = results[name]
        output["baselines"][name] = {
            "3class_f1": r["3class_f1"], "3class_ci95": r["3class_ci95"],
            "binary_f1": r["binary_f1"], "binary_ci95": r["binary_ci95"],
            "per_gen": {g: {"3class_f1": r["per_gen_3class"][g],
                           "binary_f1": r["per_gen_binary"][g]} for g in ALL_8}
        }

    for name in ["4det_ensemble", "4det_surface"]:
        r = results[name]
        output["ensembles"][name] = {
            "3class_f1": r["3class_f1"], "3class_ci95": r["3class_ci95"],
            "binary_f1": r["binary_f1"], "binary_ci95": r["binary_ci95"],
            "per_gen": {g: {"3class_f1": r["per_gen_3class"][g],
                           "binary_f1": r["per_gen_binary"][g]} for g in ALL_8}
        }

    r = results["7feature_ours"]
    output["7feature_ours"] = {
        "3class_f1": r["3class_f1"], "3class_ci95": r["3class_ci95"],
        "binary_f1": r["binary_f1"], "binary_ci95": r["binary_ci95"],
        "per_gen": {g: {"3class_f1": r["per_gen_3class"][g],
                       "binary_f1": r["per_gen_binary"][g]} for g in ALL_8}
    }

    # Summary table
    print("\n" + "=" * 90)
    print(f"{'Method':<20} {'3class-F1':>10} {'3class-CI':>22} {'Binary-F1':>10} {'Binary-CI':>22}")
    print("-" * 90)
    for name in ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score",
                 "4det_ensemble", "4det_surface", "7feature_ours"]:
        r = results[name]
        print(f"{name:<20} {r['3class_f1']:>10.4f} [{r['3class_ci95'][0]:.4f}, {r['3class_ci95'][1]:.4f}]"
              f" {r['binary_f1']:>10.4f} [{r['binary_ci95'][0]:.4f}, {r['binary_ci95'][1]:.4f}]")

    out_path = RESULTS / "8gen_logo_baselines.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
