#!/usr/bin/env python3
"""8-gen LOGO evaluation for 4 detector baselines + ensembles.

Optimized: vectorized LD score computation using scipy sparse + numpy.
"""

import json, time, os, sys
import numpy as np
import pandas as pd
from collections import Counter
from pathlib import Path
from scipy.spatial.distance import jensenshannon
from scipy.sparse import lil_matrix, csr_matrix
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

ROOT = Path("/root/gen-depth-fingerprint")
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

DEVICE = "cuda:0"
MAX_LEN = 512
N_BOOT = 1000
LOGO_SEED = 789
BOOT_SEED = 42

PYTHIA_410M = "/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f/"
PYTHIA_1B = "/root/autodl-tmp/models/pythia-1b/EleutherAI/pythia-1b/"

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
          "llama-3.2-3b", "mistral-7b-v0.3"]

CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}

XGB_PARAMS = dict(n_estimators=100, max_depth=3, learning_rate=0.1,
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


# ================================================================
# Detector score computation
# ================================================================

def compute_fdg_logprob(texts, model, tokenizer, device, bs=16):
    import torch
    import torch.nn.functional as F
    fdg, lp = [], []
    for i in range(0, len(texts), bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            logits = model(**enc).logits
        log_p = F.log_softmax(logits[:, :-1], dim=-1)
        tgt = enc["input_ids"][:, 1:]
        mask = enc["attention_mask"][:, 1:].bool()
        actual = log_p.gather(2, tgt.unsqueeze(-1)).squeeze(-1)
        expected = (log_p.exp() * log_p).sum(-1)
        curv = actual - expected
        for j in range(len(batch)):
            m = mask[j]
            if m.sum() < 2:
                fdg.append(0.0); lp.append(0.0); continue
            c = curv[j][m]
            mc, sc = c.mean().item(), c.std().item()
            fdg.append(mc / (sc + 1e-8) if sc > 1e-8 else mc)
            lp.append(actual[j][m].mean().item())
        if (i // bs) % 200 == 0:
            print(f"  FDG+LP: {min(i+bs,len(texts))}/{len(texts)}")
    return fdg, lp


def compute_binoculars(texts, observer, performer, tokenizer, device, bs=8):
    import torch
    import torch.nn.functional as F
    scores = []
    for i in range(0, len(texts), bs):
        batch = texts[i:i+bs]
        enc = tokenizer(batch, return_tensors="pt", truncation=True,
                        max_length=MAX_LEN, padding=True).to(device)
        with torch.no_grad():
            o_logits = observer(**enc).logits[:, :-1].contiguous()
            p_logits = performer(**enc).logits[:, :-1].contiguous()
        ids = enc["input_ids"][:, 1:].contiguous()
        mask = enc["attention_mask"][:, 1:].float()
        o_ce = torch.nn.functional.cross_entropy(
            o_logits.view(-1, o_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)
        p_ce = torch.nn.functional.cross_entropy(
            p_logits.view(-1, p_logits.size(-1)), ids.view(-1), reduction="none").view(ids.shape)
        for j in range(len(batch)):
            m = mask[j]
            if m.sum() < 2:
                scores.append(0.0); continue
            o_val = (o_ce[j] * m).sum() / m.sum()
            p_val = (p_ce[j] * m).sum() / m.sum()
            scores.append((o_val / (p_val + 1e-8)).item())
        if (i // bs) % 200 == 0:
            print(f"  Bino: {min(i+bs,len(texts))}/{len(texts)}")
    return scores


# ================================================================
# Vectorized LD score (trigram JSD)
# ================================================================

def build_trigram_matrix(texts, n=3):
    """Build trigram count matrix as sparse CSR. Returns (matrix, vocab_list)."""
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
    """Batched JSD: JSD(P,Q) = sqrt(H(M) - (H(P)+H(Q))/2)."""
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


# ================================================================
# Evaluation
# ================================================================

def downsample(df, label_col, rng):
    counts = df[label_col].value_counts()
    min_n = counts.min()
    parts = [df[df[label_col] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(counts.index)]
    return pd.concat(parts, ignore_index=True)


def logo_eval(df, feat_cols, params, gens, tri_matrix=None, binary=False):
    """LOGO evaluation. If 'ld_score' in feat_cols, compute per-fold using tri_matrix."""
    rng = np.random.RandomState(LOGO_SEED)
    label_col = "label_bin" if binary else "label"
    preds = np.full(len(df), -1, dtype=int)
    per_gen = {}

    for g in sorted(gens):
        tr_mask = (df["model_name"] != g).values
        te_mask = (df["model_name"] == g).values

        if "ld_score" in feat_cols and tri_matrix is not None:
            ref_mask = tr_mask & (df[label_col].values == 0)
            ld_all = compute_ld_scores_vectorized(tri_matrix, ref_mask)
            df["ld_score"] = ld_all

        train_df = df[tr_mask].copy()
        test_df = df[te_mask].copy()
        train_ds = downsample(train_df, label_col, rng)
        clf = XGBClassifier(**params)
        clf.fit(train_ds[feat_cols].values, train_ds[label_col].values)
        p = clf.predict(test_df[feat_cols].values)
        preds[te_mask] = p
        f1 = f1_score(test_df[label_col].values, p, average="macro")
        per_gen[g] = round(float(f1), 4)

    y_true = df[label_col].values
    valid = preds >= 0
    pooled_f1 = round(float(f1_score(y_true[valid], preds[valid], average="macro")), 4)
    return pooled_f1, per_gen, y_true[valid], preds[valid]


def bootstrap_ci(y_true, y_pred, n_boot=N_BOOT, seed=BOOT_SEED):
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


# ================================================================
# Main
# ================================================================

def main():
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    t0 = time.time()
    print("=" * 60)
    print("8-gen Baselines: 4 detectors + ensemble LOGO")
    print("=" * 60)

    # --- Step 1: Load existing 6-gen scores ---
    print("\n[1] Loading existing detector scores...")
    scores_6gen = pd.read_csv(DATA / "detector_scores_all.csv")
    print(f"  6-gen scores: {len(scores_6gen)} rows, gens={sorted(scores_6gen['model_name'].unique())}")

    # --- Step 2: Compute scores for new generators ---
    new_gens = ["llama-3.2-3b", "mistral-7b-v0.3"]
    new_texts = {}
    for gen in new_gens:
        path = JSONL_PATHS[gen]
        records = []
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                records.append({
                    "model_name": gen,
                    "seed_id": rec.get("seed_id", rec.get("id")),
                    "depth": rec["depth"],
                    "text": rec["text"],
                })
        new_texts[gen] = records
        print(f"  {gen}: {len(records)} texts")

    all_new_texts = []
    for gen in new_gens:
        all_new_texts.extend(new_texts[gen])
    texts_list = [r["text"] for r in all_new_texts]

    # Check if 8gen scores already exist
    scores_8gen_path = DATA / "detector_scores_8gen.csv"
    if scores_8gen_path.exists():
        print(f"\n[2-5] Loading pre-computed 8gen scores from {scores_8gen_path}")
        scores_8gen = pd.read_csv(scores_8gen_path)
    else:
        print(f"\n[2] Loading Pythia-410M (observer)...")
        tokenizer = AutoTokenizer.from_pretrained(PYTHIA_410M)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        observer = AutoModelForCausalLM.from_pretrained(PYTHIA_410M, torch_dtype=torch.float16)
        observer.to(DEVICE).eval()
        print(f"  Observer loaded on {DEVICE}")

        print(f"\n[3] Computing avg_logprob + fastdetectgpt...")
        fdg_scores, lp_scores = compute_fdg_logprob(texts_list, observer, tokenizer, DEVICE, bs=16)

        print(f"\n[4] Loading Pythia-1B (performer)...")
        performer = AutoModelForCausalLM.from_pretrained(PYTHIA_1B, torch_dtype=torch.float16)
        performer.to(DEVICE).eval()
        print(f"  Performer loaded on {DEVICE}")

        print(f"\n[5] Computing binoculars...")
        bino_scores = compute_binoculars(texts_list, observer, performer, tokenizer, DEVICE, bs=8)

        del observer, performer
        torch.cuda.empty_cache()
        print(f"  Models freed")

        new_scores_df = pd.DataFrame(all_new_texts)
        new_scores_df["label"] = new_scores_df["depth"].map(CLASS_MAP)
        new_scores_df["avg_logprob"] = lp_scores
        new_scores_df["fastdetectgpt"] = fdg_scores
        new_scores_df["binoculars"] = bino_scores
        new_scores_df = new_scores_df[["model_name", "seed_id", "depth", "label",
                                        "avg_logprob", "fastdetectgpt", "binoculars"]]

        scores_8gen = pd.concat([scores_6gen, new_scores_df], ignore_index=True)
        scores_8gen.to_csv(scores_8gen_path, index=False)
        print(f"  8-gen scores saved: {len(scores_8gen)} rows")

    # --- Step 3: Load texts for LD + surface features ---
    print("\n[6] Loading all texts for LD score...")
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
    print(f"  Text loaded: {len(text_df)} rows")

    # Merge detector scores onto text_df
    merged = text_df.merge(
        scores_8gen[["model_name", "seed_id", "depth", "avg_logprob", "fastdetectgpt", "binoculars"]],
        on=["model_name", "seed_id", "depth"], how="left")
    merged = merged.reset_index(drop=True)
    print(f"  Merged: {len(merged)} rows, NaN in avg_logprob: {merged['avg_logprob'].isna().sum()}")

    # Load 7-feature data
    print("\n[7] Loading 7-feature data...")
    feat_base = pd.read_csv(DATA / "features_all_models.csv")
    for gen in new_gens:
        feat_path = DATA / gen / "features_pythia410m.jsonl"
        records = []
        with open(feat_path) as f:
            for line in f:
                rec = json.loads(line)
                rec["model_name"] = gen
                records.append(rec)
        feat_base = pd.concat([feat_base, pd.DataFrame(records)], ignore_index=True)
    feat_base["label"] = feat_base["depth"].map(CLASS_MAP)

    # Merge surface features
    merge_cols = ["model_name", "seed_id", "depth"]
    feat_cols_to_merge = [c for c in FEAT_7 + ["ttr", "hapax_ratio"] if c not in merged.columns]
    if feat_cols_to_merge:
        merged = merged.merge(
            feat_base[merge_cols + FEAT_7],
            on=merge_cols, how="left")
    merged = merged.reset_index(drop=True)

    # Binary label
    merged["label_bin"] = merged["label"].map({0: -1, 1: 0, 2: 1})

    # Build trigram matrix (vectorized)
    print("\n[8] Building trigram matrix (vectorized)...")
    t_tri = time.time()
    tri_matrix, _ = build_trigram_matrix(merged["text"].tolist())
    print(f"  Matrix shape: {tri_matrix.shape}, built in {time.time()-t_tri:.1f}s")

    # Binary subset
    bin_mask = merged["label_bin"] >= 0
    merged_bin = merged[bin_mask].copy().reset_index(drop=True)
    tri_matrix_bin = tri_matrix[bin_mask.values]

    # --- Step 4: LOGO Evaluation ---
    print("\n" + "=" * 60)
    print("LOGO Evaluation (8 generators)")
    print("=" * 60)

    results = {}

    # Single detectors (3-class)
    single_dets = {
        "avg_logprob": ["avg_logprob"],
        "fastdetectgpt": ["fastdetectgpt"],
        "binoculars": ["binoculars"],
        "ld_score": ["ld_score"],
    }

    for name, feats in single_dets.items():
        print(f"\n  {name} (3-class)...")
        use_tri = tri_matrix if "ld_score" in feats else None
        avg_f1, per_gen, yt, yp = logo_eval(merged, feats, XGB_PARAMS, ALL_8, tri_matrix=use_tri)
        ci = bootstrap_ci(yt, yp)
        results[name] = {"3class_f1": avg_f1, "3class_ci": ci, "per_gen_3class": per_gen}
        print(f"    3-class F1={avg_f1} CI={ci}")

    # Single detectors (binary)
    for name, feats in single_dets.items():
        print(f"\n  {name} (binary)...")
        use_tri = tri_matrix_bin if "ld_score" in feats else None
        avg_f1, per_gen, yt, yp = logo_eval(merged_bin, feats, XGB_PARAMS, ALL_8,
                                             tri_matrix=use_tri, binary=True)
        ci = bootstrap_ci(yt, yp)
        results[name]["binary_f1"] = avg_f1
        results[name]["binary_ci"] = ci
        results[name]["per_gen_binary"] = per_gen
        print(f"    Binary F1={avg_f1} CI={ci}")

    # Ensembles (3-class)
    print("\n  4det_ensemble (3-class)...")
    ens_feats = ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score"]
    avg_f1, per_gen, yt, yp = logo_eval(merged, ens_feats, XGB_PARAMS, ALL_8, tri_matrix=tri_matrix)
    ci = bootstrap_ci(yt, yp)
    results["4det_ensemble"] = {"3class_f1": avg_f1, "3class_ci": ci, "per_gen_3class": per_gen}
    print(f"    3-class F1={avg_f1} CI={ci}")

    print("\n  4det_surface (3-class)...")
    surf_feats = ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score", "ttr", "hapax_ratio"]
    avg_f1, per_gen, yt, yp = logo_eval(merged, surf_feats, XGB_PARAMS, ALL_8, tri_matrix=tri_matrix)
    ci = bootstrap_ci(yt, yp)
    results["4det_surface"] = {"3class_f1": avg_f1, "3class_ci": ci, "per_gen_3class": per_gen}
    print(f"    3-class F1={avg_f1} CI={ci}")

    print("\n  7feature_ours (3-class)...")
    avg_f1, per_gen, yt, yp = logo_eval(merged, FEAT_7, XGB_PARAMS, ALL_8)
    ci = bootstrap_ci(yt, yp)
    results["7feature_ours"] = {"3class_f1": avg_f1, "3class_ci": ci, "per_gen_3class": per_gen}
    print(f"    3-class F1={avg_f1} CI={ci}")

    # Ensembles (binary)
    print("\n  4det_ensemble (binary)...")
    avg_f1, per_gen, yt, yp = logo_eval(merged_bin, ens_feats, XGB_PARAMS, ALL_8,
                                         tri_matrix=tri_matrix_bin, binary=True)
    ci = bootstrap_ci(yt, yp)
    results["4det_ensemble"]["binary_f1"] = avg_f1
    results["4det_ensemble"]["binary_ci"] = ci
    results["4det_ensemble"]["per_gen_binary"] = per_gen
    print(f"    Binary F1={avg_f1} CI={ci}")

    print("\n  4det_surface (binary)...")
    avg_f1, per_gen, yt, yp = logo_eval(merged_bin, surf_feats, XGB_PARAMS, ALL_8,
                                         tri_matrix=tri_matrix_bin, binary=True)
    ci = bootstrap_ci(yt, yp)
    results["4det_surface"]["binary_f1"] = avg_f1
    results["4det_surface"]["binary_ci"] = ci
    results["4det_surface"]["per_gen_binary"] = per_gen
    print(f"    Binary F1={avg_f1} CI={ci}")

    print("\n  7feature_ours (binary)...")
    avg_f1, per_gen, yt, yp = logo_eval(merged_bin, FEAT_7, XGB_PARAMS, ALL_8, binary=True)
    ci = bootstrap_ci(yt, yp)
    results["7feature_ours"]["binary_f1"] = avg_f1
    results["7feature_ours"]["binary_ci"] = ci
    results["7feature_ours"]["per_gen_binary"] = per_gen
    print(f"    Binary F1={avg_f1} CI={ci}")

    # --- Summary ---
    print("\n" + "=" * 70)
    print(f"{'Method':<20} {'3class-F1':>10} {'3class-CI':>22} {'Binary-F1':>10} {'Binary-CI':>22}")
    print("-" * 86)
    for name in ["avg_logprob", "fastdetectgpt", "binoculars", "ld_score",
                 "4det_ensemble", "4det_surface", "7feature_ours"]:
        r = results[name]
        print(f"{name:<20} {r['3class_f1']:>10.4f} [{r['3class_ci'][0]:.4f}, {r['3class_ci'][1]:.4f}]"
              f" {r['binary_f1']:>10.4f} [{r['binary_ci'][0]:.4f}, {r['binary_ci'][1]:.4f}]")

    # --- Save ---
    out_path = RESULTS / "8gen_baselines.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")
    print(f"Total time: {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
