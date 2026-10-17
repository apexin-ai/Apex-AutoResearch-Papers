#!/usr/bin/env python3
"""Plan 015: Comprehensive Wild-Data Calibration.

Consolidates C4 10K, FineWeb 10K, and RedPajama 10K results.
- Extracts RedPajama 10K features (GPU)
- Loads existing C4/FineWeb 10K features (CSV)
- Trains RF on controlled data
- Unified threshold sweep across all datasets
- KS statistics for feature distribution shift
- Outputs comprehensive_results.json
"""

import gzip
import json
import os
import sys
import time
import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import skew, kurtosis, entropy, ks_2samp
from sklearn.ensemble import RandomForestClassifier
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
for k in ("REQUESTS_CA_BUNDLE", "SSL_CERT_FILE"):
    os.environ.setdefault(k, "/etc/ssl/certs/ca-certificates.crt")

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

PROJECT_DIR = "/root/autodl-tmp/recursive_gen_depth_est"
MODEL_PATH = "/root/autodl-tmp/models/pythia-1.4b"
TRAIN_FEATURES = os.path.join(PROJECT_DIR, "data/features_all.jsonl")
REDPAJAMA_GZ = os.path.join(PROJECT_DIR, "data/redpajama_en_head.json.gz")
C4_CSV = os.path.join(PROJECT_DIR, "results/wild_features/c4_10k_features.csv")
FW_CSV = os.path.join(PROJECT_DIR, "results/wild_features/fineweb_10k_features.csv")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "results/wild_data_calibration_comprehensive")
TRUNC_LEN = 507
N_REDPAJAMA = 10000
BATCH_SIZE = 16
SEED = 42

THRESHOLDS_LOW = [0.05, 0.10, 0.12, 0.15, 0.18, 0.20, 0.25]
THRESHOLDS_HIGH = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.99]


def compute_repetition(token_ids, n):
    if len(token_ids) < n:
        return 0.0
    ngrams = [tuple(token_ids[i:i+n]) for i in range(len(token_ids) - n + 1)]
    total = len(ngrams)
    unique = len(set(ngrams))
    return 1.0 - unique / total if total > 0 else 0.0


def compute_lexical_features(token_ids):
    n_tokens = len(token_ids)
    if n_tokens == 0:
        return {k: 0.0 for k in [
            "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
            "rep_2gram", "rep_3gram", "rep_4gram"]}
    counts = Counter(token_ids)
    ttr = len(counts) / n_tokens
    hapax = sum(1 for v in counts.values() if v == 1) / len(counts) if counts else 0.0

    def ngram_entropy(ids, n):
        if len(ids) < n:
            return 0.0
        ngrams = [tuple(ids[i:i+n]) for i in range(len(ids) - n + 1)]
        c = Counter(ngrams)
        total = sum(c.values())
        probs = np.array([v / total for v in c.values()])
        return float(entropy(probs))

    return {
        "type_token_ratio": ttr,
        "hapax_ratio": hapax,
        "bigram_entropy": ngram_entropy(token_ids, 2),
        "trigram_entropy": ngram_entropy(token_ids, 3),
        "rep_2gram": compute_repetition(token_ids, 2),
        "rep_3gram": compute_repetition(token_ids, 3),
        "rep_4gram": compute_repetition(token_ids, 4),
    }


def compute_perplexity_features(losses_np):
    if len(losses_np) == 0:
        return {k: 0.0 for k in [
            "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
            "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
            "mean_surprisal", "var_surprisal", "entropy_of_surprisal"]}

    ppl = np.exp(np.clip(losses_np, None, 30))
    result = {
        "mean_ppl": float(np.mean(ppl)),
        "var_ppl": float(np.var(ppl)),
        "skewness_ppl": float(skew(ppl)) if len(ppl) > 2 else 0.0,
        "kurtosis_ppl": float(kurtosis(ppl)) if len(ppl) > 3 else 0.0,
        "p10_ppl": float(np.percentile(ppl, 10)),
        "p25_ppl": float(np.percentile(ppl, 25)),
        "p50_ppl": float(np.percentile(ppl, 50)),
        "p75_ppl": float(np.percentile(ppl, 75)),
        "p90_ppl": float(np.percentile(ppl, 90)),
    }
    surprisal = losses_np
    result["mean_surprisal"] = float(np.mean(surprisal))
    result["var_surprisal"] = float(np.var(surprisal))

    if len(surprisal) > 1 and surprisal.max() > surprisal.min():
        n_bins = min(50, max(10, len(surprisal) // 5))
        hist, _ = np.histogram(surprisal, bins=n_bins, density=True)
        bin_width = (surprisal.max() - surprisal.min()) / n_bins
        probs = hist * bin_width
        probs = probs[probs > 0]
        result["entropy_of_surprisal"] = float(entropy(probs))
    else:
        result["entropy_of_surprisal"] = 0.0

    return result


def extract_features_batch(texts, tokenizer, model, device, trunc_len=TRUNC_LEN, batch_size=BATCH_SIZE):
    all_features = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Extracting features"):
        batch_texts = texts[i:i+batch_size]
        encodings = tokenizer(
            batch_texts, return_tensors="pt", truncation=True,
            max_length=trunc_len, padding=True
        ).to(device)

        with torch.no_grad():
            outputs = model(**encodings)
            logits = outputs.logits

        for j in range(len(batch_texts)):
            input_ids = encodings["input_ids"][j]
            attn_mask = encodings["attention_mask"][j]
            valid_len = attn_mask.sum().item()

            if valid_len < 10:
                continue

            token_logits = logits[j, :valid_len-1, :].float()
            target_ids = input_ids[1:valid_len]

            loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
            losses = loss_fct(token_logits, target_ids)
            losses_np = losses.cpu().float().numpy()
            token_ids_list = input_ids[:valid_len].cpu().tolist()

            ppl_feats = compute_perplexity_features(losses_np)
            lex_feats = compute_lexical_features(token_ids_list)

            feat_row = {}
            feat_row.update(ppl_feats)
            feat_row.update(lex_feats)
            for k, v in feat_row.items():
                if not np.isfinite(v):
                    feat_row[k] = 0.0
            all_features.append(feat_row)

    return all_features


def load_redpajama(path, n_samples=10000, min_len=200):
    print(f"  Loading RedPajama V2 from {path}...")
    texts = []
    with gzip.open(path, "rt") as f:
        for line in f:
            rec = json.loads(line)
            text = rec.get("raw_content", "")
            if len(text) >= min_len:
                texts.append(text)
            if len(texts) >= n_samples:
                break
    print(f"  Loaded {len(texts)} passages (>={min_len} chars)")
    return texts


def train_rf(features_path, seed=SEED):
    print(f"  Loading training data from {features_path}...")
    data = []
    with open(features_path) as f:
        for line in f:
            data.append(json.loads(line))
    print(f"  Loaded {len(data)} controlled samples")

    X = np.array([[d[fn] for fn in FEATURE_NAMES] for d in data])
    y = np.array([d["depth"] for d in data])

    np.random.seed(seed)
    rf = RandomForestClassifier(n_estimators=200, random_state=seed, n_jobs=-1)
    rf.fit(X, y)
    print(f"  RF trained: classes={rf.classes_.tolist()}")

    ctrl_d0_mask = y == 0
    X_ctrl_d0 = X[ctrl_d0_mask]
    return rf, X, y, X_ctrl_d0


def predict_dataset(rf, X, name):
    preds = rf.predict(X)
    probs = rf.predict_proba(X)
    classes = rf.classes_.tolist()

    dist = Counter(preds)
    n = len(preds)

    pred_dist = {f"d{c}": int(dist.get(c, 0)) for c in classes}
    pred_pct = {f"d{c}": round(100 * dist.get(c, 0) / n, 2) for c in classes}

    mean_prob = {}
    std_prob = {}
    for i, c in enumerate(classes):
        mean_prob[f"d{c}"] = round(float(np.mean(probs[:, i])), 4)
        std_prob[f"d{c}"] = round(float(np.std(probs[:, i])), 4)

    fpr = round(100 * (1 - dist.get(0, 0) / n), 2)

    return {
        "n_samples": n,
        "pred_distribution": pred_dist,
        "pred_pct": pred_pct,
        "mean_prob": mean_prob,
        "std_prob": std_prob,
        "fpr": fpr,
        "d0_rate": round(100 * dist.get(0, 0) / n, 2),
    }, probs


def threshold_sweep_low(probs, rf_classes, thresholds=THRESHOLDS_LOW):
    """Low-threshold sweep: classify as d1+ only if P(d0) < threshold."""
    results = []
    d0_idx = list(rf_classes).index(0)
    p_d0 = probs[:, d0_idx]
    n = len(p_d0)

    for t in thresholds:
        n_d1plus = int(np.sum(p_d0 < t))
        fpr = round(100 * n_d1plus / n, 2)
        coverage = round((n - n_d1plus) / n, 4)
        results.append({
            "threshold": t,
            "fpr": fpr,
            "n_d1plus": n_d1plus,
            "coverage": coverage,
        })
    return results


def threshold_sweep_high(probs, rf_classes, thresholds=THRESHOLDS_HIGH):
    """High-threshold sweep: only classify as d1+ if max(P(d1+)) > threshold."""
    results = []
    d0_idx = list(rf_classes).index(0)
    p_d0 = probs[:, d0_idx]
    p_d1plus_max = np.max(np.delete(probs, d0_idx, axis=1), axis=1)
    n = len(p_d0)

    for t in thresholds:
        is_d1plus = p_d1plus_max > t
        n_d1plus = int(np.sum(is_d1plus))
        fpr = round(100 * n_d1plus / n, 2)
        coverage = round(np.sum(p_d0 > t) / n, 4)
        results.append({
            "threshold": t,
            "fpr": fpr,
            "n_d1plus": n_d1plus,
            "coverage_d0_confident": coverage,
        })
    return results


def compute_ks_stats(X_wild, X_ctrl_d0):
    """KS statistics between wild features and controlled d0 features."""
    ks_results = {}
    for i, fn in enumerate(FEATURE_NAMES):
        stat, pval = ks_2samp(X_wild[:, i], X_ctrl_d0[:, i])
        ks_results[fn] = {
            "ks_stat": round(float(stat), 4),
            "ks_pvalue": float(pval),
            "wild_mean": round(float(np.mean(X_wild[:, i])), 4),
            "ctrl_d0_mean": round(float(np.mean(X_ctrl_d0[:, i])), 4),
        }
    return ks_results


def compute_p_d0_distribution(probs, rf_classes):
    d0_idx = list(rf_classes).index(0)
    p_d0 = probs[:, d0_idx]
    percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    return {
        f"p{p}": round(float(np.percentile(p_d0, p)), 4) for p in percentiles
    }


def main():
    t0 = time.time()
    np.random.seed(SEED)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    # === Step 1: Train RF ===
    print("\n" + "="*60)
    print("  Step 1: Training RF classifier")
    print("="*60)
    rf, X_train, y_train, X_ctrl_d0 = train_rf(TRAIN_FEATURES)

    # === Step 2: Load existing C4 and FineWeb 10K features ===
    print("\n" + "="*60)
    print("  Step 2: Loading existing C4/FineWeb 10K features")
    print("="*60)

    c4_df = pd.read_csv(C4_CSV)
    X_c4 = c4_df[FEATURE_NAMES].values
    print(f"  C4 10K: {len(X_c4)} samples loaded")

    fw_df = pd.read_csv(FW_CSV)
    X_fw = fw_df[FEATURE_NAMES].values
    print(f"  FineWeb 10K: {len(X_fw)} samples loaded")

    # Sanitize
    X_c4 = np.nan_to_num(X_c4, nan=0.0, posinf=0.0, neginf=0.0)
    X_fw = np.nan_to_num(X_fw, nan=0.0, posinf=0.0, neginf=0.0)

    # === Step 3: Extract RedPajama 10K features ===
    print("\n" + "="*60)
    print("  Step 3: Extracting RedPajama 10K features")
    print("="*60)

    rp_texts = load_redpajama(REDPAJAMA_GZ, n_samples=N_REDPAJAMA)

    print("  Loading Pythia-1.4B...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16).to(device)
    model.eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    t_feat_start = time.time()
    rp_features = extract_features_batch(rp_texts, tokenizer, model, device)
    t_feat_end = time.time()
    print(f"  RedPajama features extracted: {len(rp_features)} samples in {t_feat_end - t_feat_start:.1f}s")

    X_rp = np.array([[f[fn] for fn in FEATURE_NAMES] for f in rp_features])
    X_rp = np.nan_to_num(X_rp, nan=0.0, posinf=0.0, neginf=0.0)

    # Save features
    rp_feat_path = os.path.join(OUTPUT_DIR, "redpajama_10k_features.jsonl")
    with open(rp_feat_path, "w") as f:
        for feat in rp_features:
            f.write(json.dumps(feat) + "\n")
    print(f"  Saved to {rp_feat_path}")

    # Free GPU memory
    del model
    torch.cuda.empty_cache()

    # === Step 4: Predictions ===
    print("\n" + "="*60)
    print("  Step 4: RF predictions on all datasets")
    print("="*60)

    c4_results, c4_probs = predict_dataset(rf, X_c4, "C4 10K")
    fw_results, fw_probs = predict_dataset(rf, X_fw, "FineWeb 10K")
    rp_results, rp_probs = predict_dataset(rf, X_rp, "RedPajama 10K")

    print(f"  C4 10K: d0={c4_results['d0_rate']}%, FPR={c4_results['fpr']}%")
    print(f"  FineWeb 10K: d0={fw_results['d0_rate']}%, FPR={fw_results['fpr']}%")
    print(f"  RedPajama 10K: d0={rp_results['d0_rate']}%, FPR={rp_results['fpr']}%")

    # Save predictions
    for name, probs_arr, X_arr in [("c4", c4_probs, X_c4), ("fineweb", fw_probs, X_fw), ("redpajama", rp_probs, X_rp)]:
        pred_path = os.path.join(OUTPUT_DIR, f"{name}_10k_predictions.jsonl")
        classes = rf.classes_.tolist()
        with open(pred_path, "w") as f:
            for idx in range(len(probs_arr)):
                rec = {f"p_d{c}": round(float(probs_arr[idx, i]), 4) for i, c in enumerate(classes)}
                rec["pred"] = int(classes[np.argmax(probs_arr[idx])])
                f.write(json.dumps(rec) + "\n")

    # === Step 5: Threshold sweep ===
    print("\n" + "="*60)
    print("  Step 5: Threshold sweep")
    print("="*60)

    sweep_results = {}
    for name, probs_arr in [("c4_10k", c4_probs), ("fineweb_10k", fw_probs), ("redpajama_10k", rp_probs)]:
        sweep_results[name] = {
            "low_threshold": threshold_sweep_low(probs_arr, rf.classes_),
            "high_threshold": threshold_sweep_high(probs_arr, rf.classes_),
            "p_d0_distribution": compute_p_d0_distribution(probs_arr, rf.classes_),
        }
        print(f"  {name}: sweep done")

    # === Step 6: KS statistics ===
    print("\n" + "="*60)
    print("  Step 6: Feature distribution shift (KS test)")
    print("="*60)

    ks_results = {}
    for name, X_wild in [("c4_10k", X_c4), ("fineweb_10k", X_fw), ("redpajama_10k", X_rp)]:
        ks_results[name] = compute_ks_stats(X_wild, X_ctrl_d0)
        n_sig = sum(1 for v in ks_results[name].values() if v["ks_pvalue"] < 0.01)
        print(f"  {name}: {n_sig}/{len(FEATURE_NAMES)} features significantly shifted (p<0.01)")

    # === Step 7: Controlled test set performance ===
    print("\n" + "="*60)
    print("  Step 7: Controlled test set performance")
    print("="*60)

    from sklearn.model_selection import cross_val_predict
    cv_probs = cross_val_predict(rf, X_train, y_train, cv=5, method="predict_proba")
    cv_preds = rf.classes_[np.argmax(cv_probs, axis=1)]
    from sklearn.metrics import balanced_accuracy_score, classification_report
    bal_acc = balanced_accuracy_score(y_train, cv_preds)
    print(f"  5-fold CV balanced accuracy: {bal_acc:.4f}")

    ctrl_sweep = []
    d0_idx = list(rf.classes_).index(0)
    for t in THRESHOLDS_LOW:
        p_d0_cv = cv_probs[:, d0_idx]
        is_d1plus_pred = p_d0_cv < t
        is_d1plus_true = y_train > 0

        mask_confident = ~is_d1plus_pred | is_d1plus_true | (p_d0_cv >= t)
        d1plus_mask = y_train > 0
        d1plus_detected = is_d1plus_pred & d1plus_mask
        d1plus_recall = d1plus_detected.sum() / d1plus_mask.sum() if d1plus_mask.sum() > 0 else 0

        d0_mask = y_train == 0
        d0_kept = (~is_d1plus_pred) & d0_mask
        d0_recall = d0_kept.sum() / d0_mask.sum() if d0_mask.sum() > 0 else 0

        ctrl_sweep.append({
            "threshold": t,
            "d0_recall": round(float(d0_recall), 4),
            "d1plus_recall": round(float(d1plus_recall), 4),
        })

    # === Step 8: Compile comprehensive results ===
    print("\n" + "="*60)
    print("  Step 8: Compiling comprehensive results")
    print("="*60)

    elapsed = time.time() - t0
    comprehensive = {
        "experiment": "wild_data_calibration_015_comprehensive",
        "feature_model": "pythia-1.4b",
        "rf_config": {"n_estimators": 200, "seed": SEED},
        "trunc_len": TRUNC_LEN,
        "cv_balanced_accuracy": round(bal_acc, 4),
        "elapsed_seconds": round(elapsed, 1),
        "datasets": {
            "c4_10k": c4_results,
            "fineweb_10k": fw_results,
            "redpajama_10k": rp_results,
        },
        "threshold_sweep": sweep_results,
        "controlled_threshold_sweep": ctrl_sweep,
        "feature_shift_ks": ks_results,
        "summary": {
            "base_fpr": {
                "c4_10k": c4_results["fpr"],
                "fineweb_10k": fw_results["fpr"],
                "redpajama_10k": rp_results["fpr"],
            },
            "fpr_at_threshold": {},
            "note": "FPR = fraction of known-human text predicted as d1+. Lower is better.",
            "c004_disclaimer": "These FPR values reflect OOD false positives, not real AI content prevalence. See C004.",
        },
    }

    # Extract FPR at key thresholds for summary
    for t in [0.10, 0.15, 0.20]:
        key = f"P(d0)<{t}"
        comprehensive["summary"]["fpr_at_threshold"][key] = {}
        for ds_name in ["c4_10k", "fineweb_10k", "redpajama_10k"]:
            for entry in sweep_results[ds_name]["low_threshold"]:
                if abs(entry["threshold"] - t) < 0.001:
                    comprehensive["summary"]["fpr_at_threshold"][key][ds_name] = entry["fpr"]

    out_path = os.path.join(OUTPUT_DIR, "comprehensive_results.json")
    with open(out_path, "w") as f:
        json.dump(comprehensive, f, indent=2)
    print(f"\n  Results saved to {out_path}")
    print(f"  Total time: {elapsed:.1f}s")

    # Quick summary table
    print("\n" + "="*60)
    print("  SUMMARY")
    print("="*60)
    print(f"  {'Dataset':<20} {'N':>6} {'d0%':>8} {'FPR%':>8}")
    print(f"  {'-'*42}")
    for name, res in comprehensive["datasets"].items():
        print(f"  {name:<20} {res['n_samples']:>6} {res['d0_rate']:>7.2f}% {res['fpr']:>7.2f}%")

    print(f"\n  Threshold sweep (P(d0) < T → classify as d1+):")
    print(f"  {'T':<8} {'C4 FPR':>10} {'FW FPR':>10} {'RP FPR':>10}")
    print(f"  {'-'*38}")
    for t in [0.05, 0.10, 0.15, 0.20, 0.25]:
        c4_fpr = fw_fpr = rp_fpr = "-"
        for ds, label in [("c4_10k", "c4_fpr"), ("fineweb_10k", "fw_fpr"), ("redpajama_10k", "rp_fpr")]:
            for entry in sweep_results[ds]["low_threshold"]:
                if abs(entry["threshold"] - t) < 0.001:
                    if ds == "c4_10k": c4_fpr = f"{entry['fpr']}%"
                    elif ds == "fineweb_10k": fw_fpr = f"{entry['fpr']}%"
                    else: rp_fpr = f"{entry['fpr']}%"
        print(f"  {t:<8} {c4_fpr:>10} {fw_fpr:>10} {rp_fpr:>10}")


if __name__ == "__main__":
    main()
