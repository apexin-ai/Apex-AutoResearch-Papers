#!/usr/bin/env python3
# Plan 015 extension: C4 web-crawl calibration supplement.
# Tests RF depth estimator on diverse web text (C4 validation) to complement WikiText-103.
# Uses Pythia-1.4B for feature extraction (same as plan_015) to match RF training features.

import argparse
import json
import os
import sys
import time
import numpy as np
from collections import Counter
from scipy.stats import skew, kurtosis, entropy, ks_2samp
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

PROJECT_DIR = "/root/autodl-tmp/recursive_gen_depth_est"
MODEL_PATH = os.path.join(PROJECT_DIR, "../models/pythia-1.4b")
FEATURES_PATH = os.path.join(PROJECT_DIR, "data/features_all.jsonl")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "results/plan_015_wild_data")
WIKI_RESULTS_PATH = os.path.join(OUTPUT_DIR, "results.json")


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
        return {
            "type_token_ratio": 0.0, "hapax_ratio": 0.0,
            "bigram_entropy": 0.0, "trigram_entropy": 0.0,
            "rep_2gram": 0.0, "rep_3gram": 0.0, "rep_4gram": 0.0,
        }
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

    ppl = np.exp(losses_np)
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
        probs = probs / probs.sum() if probs.sum() > 0 else probs
        result["entropy_of_surprisal"] = float(entropy(probs[probs > 0]))
    else:
        result["entropy_of_surprisal"] = 0.0
    return result


def extract_batch_features(model, tokenizer, texts, trunc_len, device):
    pad_id = tokenizer.pad_token_id
    encoded = []
    for text in texts:
        ids = tokenizer.encode(text, add_special_tokens=False)[:trunc_len]
        encoded.append(ids)

    max_len = max(len(e) for e in encoded)
    input_ids = []
    attention_mask = []
    for e in encoded:
        pad_len = max_len - len(e)
        input_ids.append(e + [pad_id] * pad_len)
        attention_mask.append([1] * len(e) + [0] * pad_len)

    input_ids_t = torch.tensor(input_ids, dtype=torch.long, device=device)
    attention_mask_t = torch.tensor(attention_mask, dtype=torch.long, device=device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids_t, attention_mask=attention_mask_t)
    logits = outputs.logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = input_ids_t[:, 1:].contiguous()
    loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
    per_token_loss = loss_fn(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1)
    ).view(shift_logits.size(0), shift_logits.size(1))

    results = []
    for i in range(len(texts)):
        seq_len = len(encoded[i])
        if seq_len <= 1:
            losses_np = np.array([0.0])
        else:
            losses_np = per_token_loss[i, :seq_len-1].cpu().numpy().astype(np.float64)
        feats = {}
        feats.update(compute_perplexity_features(losses_np))
        feats.update(compute_lexical_features(encoded[i]))
        results.append(feats)
    return results


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def features_to_array(features_list):
    X = np.array([[f[k] for k in FEATURE_NAMES] for f in features_list], dtype=np.float64)
    return np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)


def prepare_c4_passages(tokenizer, n_passages=5000, trunc_len=507, min_tokens=100, seed=42):
    from datasets import load_dataset

    print("Loading C4 validation split (streaming)...")
    ds = load_dataset(
        "allenai/c4", "en", split="validation", streaming=True,
        cache_dir="/root/autodl-tmp/.hf_cache",
        trust_remote_code=True,
    )

    rng = np.random.RandomState(seed)
    collected = []
    skipped_short = 0
    seen = 0

    for example in ds:
        seen += 1
        text = example.get("text", "").strip()
        if not text:
            continue

        url = example.get("url", "")
        timestamp = example.get("timestamp", "")

        ids = tokenizer.encode(text, add_special_tokens=False)
        if len(ids) < min_tokens:
            skipped_short += 1
            continue

        ids_trunc = ids[:trunc_len]
        text_trunc = tokenizer.decode(ids_trunc)

        collected.append({
            "text": text_trunc,
            "token_ids": ids_trunc,
            "original_token_count": len(ids),
            "truncated_token_count": len(ids_trunc),
            "url": url,
            "timestamp": timestamp,
        })

        if len(collected) >= n_passages * 3:
            break

        if len(collected) % 5000 == 0 and len(collected) > 0:
            print(f"  Collected {len(collected)} candidates (seen {seen}, skipped short: {skipped_short})...")

    print(f"  Total candidates: {len(collected)} (seen {seen}, skipped short: {skipped_short})")

    if len(collected) > n_passages:
        idx = rng.choice(len(collected), n_passages, replace=False)
        collected = [collected[i] for i in sorted(idx)]

    print(f"  Sampled {len(collected)} passages (trunc_len={trunc_len}, min_tokens={min_tokens})")
    return collected


def extract_features_for_texts(model, tokenizer, texts, trunc_len, device, batch_size=16, desc="Features"):
    all_features = []
    for start in tqdm(range(0, len(texts), batch_size), desc=desc, unit="batch"):
        end = min(start + batch_size, len(texts))
        batch_texts = texts[start:end]
        try:
            batch_feats = extract_batch_features(model, tokenizer, batch_texts, trunc_len, device)
            all_features.extend(batch_feats)
        except Exception as e:
            print(f"\n[WARN] Batch error at {start}-{end}: {e}")
            for _ in range(end - start):
                all_features.append({k: 0.0 for k in FEATURE_NAMES})
    return all_features


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--n_passages", type=int, default=5000)
    parser.add_argument("--trunc_len", type=int, default=507)
    parser.add_argument("--min_tokens", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ── Step 1: Load tokenizer & model ──
    print(f"\nLoading tokenizer from {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading model from {MODEL_PATH}...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.float16
    ).to(device)
    model.eval()

    # ── Step 2: Download & sample C4 passages ──
    print("\n" + "="*60)
    print("  Step 2: C4 Data Preparation")
    print("="*60)
    t0 = time.time()
    c4_passages = prepare_c4_passages(
        tokenizer, n_passages=args.n_passages, trunc_len=args.trunc_len,
        min_tokens=args.min_tokens, seed=args.seed,
    )
    print(f"  C4 download took {time.time()-t0:.0f}s")
    c4_texts = [p["text"] for p in c4_passages]

    c4_path = os.path.join(OUTPUT_DIR, "c4_passages.jsonl")
    with open(c4_path, "w") as f:
        for i, p in enumerate(c4_passages):
            row = {
                "text": p["text"],
                "sample_id": i,
                "source": "c4-en-validation",
                "url": p.get("url", ""),
                "original_token_count": p.get("original_token_count", 0),
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"  Saved {len(c4_passages)} passages to {c4_path}")

    # ── Step 3: Extract features ──
    print("\n" + "="*60)
    print("  Step 3: C4 Feature Extraction (Pythia-1.4B)")
    print("="*60)
    t0 = time.time()
    c4_features = extract_features_for_texts(
        model, tokenizer, c4_texts, args.trunc_len, device,
        batch_size=args.batch_size, desc="C4 features"
    )
    print(f"  Feature extraction took {time.time()-t0:.0f}s")

    c4_feat_path = os.path.join(OUTPUT_DIR, "c4_features.jsonl")
    with open(c4_feat_path, "w") as f:
        for i, feat in enumerate(c4_features):
            row = {"depth": -1, "sample_id": i, "source": "c4-en-validation"}
            row.update(feat)
            f.write(json.dumps(row) + "\n")
    print(f"  Saved features to {c4_feat_path}")

    X_c4 = features_to_array(c4_features)
    print(f"  C4 feature matrix: {X_c4.shape}")

    del model
    torch.cuda.empty_cache()
    print("  Model unloaded.")

    # ── Step 4: Train RF on controlled data ──
    print("\n" + "="*60)
    print("  Step 4: Train RF on Pythia Nucleus Controlled Data")
    print("="*60)
    X_ctrl, y_ctrl = load_features(FEATURES_PATH)
    print(f"  Controlled: {X_ctrl.shape[0]} samples, depth dist: {dict(Counter(y_ctrl))}")

    scaler = StandardScaler()
    X_ctrl_s = scaler.fit_transform(X_ctrl)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=args.seed)
    cv_accs = []
    for fold, (train_idx, val_idx) in enumerate(skf.split(X_ctrl_s, y_ctrl)):
        rf_cv = RandomForestClassifier(n_estimators=200, random_state=args.seed, n_jobs=-1)
        rf_cv.fit(X_ctrl_s[train_idx], y_ctrl[train_idx])
        pred = rf_cv.predict(X_ctrl_s[val_idx])
        cv_accs.append(accuracy_score(y_ctrl[val_idx], pred))
    print(f"  5-fold CV accuracy: {np.mean(cv_accs):.4f} +/- {np.std(cv_accs):.4f}")

    rf = RandomForestClassifier(n_estimators=200, random_state=args.seed, n_jobs=-1)
    rf.fit(X_ctrl_s, y_ctrl)

    # ── Step 5: Predict on C4 ──
    print("\n" + "="*60)
    print("  Step 5: C4 Predictions")
    print("="*60)
    X_c4_s = scaler.transform(X_c4)
    c4_pred = rf.predict(X_c4_s)
    c4_prob = rf.predict_proba(X_c4_s)
    if c4_prob.shape[1] < 4:
        full_prob = np.zeros((c4_prob.shape[0], 4))
        for i, c in enumerate(rf.classes_):
            full_prob[:, c] = c4_prob[:, i]
        c4_prob = full_prob

    c4_pred_dist = Counter(int(x) for x in c4_pred)
    n_c4 = len(c4_pred)
    print(f"\n  C4 predictions (n={n_c4}):")
    for d in range(4):
        n = c4_pred_dist.get(d, 0)
        pct = n / n_c4 * 100
        print(f"    d{d}: {n} ({pct:.1f}%)")

    print(f"\n  C4 mean predict_proba:")
    for d in range(4):
        print(f"    P(d{d}): {c4_prob[:, d].mean():.4f} +/- {c4_prob[:, d].std():.4f}")

    # ── Step 6: Feature comparison ──
    print("\n" + "="*60)
    print("  Step 6: Feature Distribution Analysis")
    print("="*60)

    ctrl_d0_mask = y_ctrl == 0
    X_ctrl_d0 = X_ctrl[ctrl_d0_mask]

    # Load WikiText features for 3-way comparison
    wiki_feat_path = os.path.join(OUTPUT_DIR, "wikitext_features.jsonl")
    X_wiki = None
    if os.path.exists(wiki_feat_path):
        X_wiki, _ = load_features(wiki_feat_path)
        print(f"  Loaded WikiText features: {X_wiki.shape}")

    feature_stats = {}
    print(f"\n  {'Feature':<25s} {'C4 mean':>12s} {'Wiki mean':>12s} {'Ctrl-d0 mean':>12s} {'C4-Ctrl diff%':>14s}")
    print(f"  {'-'*25} {'-'*12} {'-'*12} {'-'*12} {'-'*14}")
    for i, fname in enumerate(FEATURE_NAMES):
        c4_vals = X_c4[:, i]
        ctrl_vals = X_ctrl_d0[:, i]
        wiki_vals = X_wiki[:, i] if X_wiki is not None else None

        stat = {
            "c4_mean": float(np.mean(c4_vals)),
            "c4_std": float(np.std(c4_vals)),
            "ctrl_d0_mean": float(np.mean(ctrl_vals)),
            "ctrl_d0_std": float(np.std(ctrl_vals)),
            "diff_pct": abs(np.mean(c4_vals) - np.mean(ctrl_vals)) / (abs(np.mean(ctrl_vals)) + 1e-8) * 100,
        }
        if wiki_vals is not None:
            stat["wiki_mean"] = float(np.mean(wiki_vals))
            stat["wiki_std"] = float(np.std(wiki_vals))

        # KS test: C4 vs controlled d0
        ks_stat, ks_p = ks_2samp(c4_vals, ctrl_vals)
        stat["ks_stat"] = float(ks_stat)
        stat["ks_pvalue"] = float(ks_p)

        feature_stats[fname] = stat

        wiki_mean_str = f"{stat.get('wiki_mean', 0):.4f}" if wiki_vals is not None else "N/A"
        print(f"  {fname:<25s} {stat['c4_mean']:>12.4f} {wiki_mean_str:>12s} {stat['ctrl_d0_mean']:>12.4f} {stat['diff_pct']:>13.1f}%")

    # ── Step 7: Analyze d1+ misclassifications ──
    print("\n" + "="*60)
    print("  Step 7: d1+ Misclassification Analysis")
    print("="*60)

    misclassified_mask = c4_pred > 0
    n_misclassified = misclassified_mask.sum()
    print(f"  {n_misclassified}/{n_c4} passages predicted as d1+ ({n_misclassified/n_c4*100:.2f}%)")

    misclass_analysis = {}
    if n_misclassified > 0:
        X_mis = X_c4[misclassified_mask]
        X_correct = X_c4[~misclassified_mask]
        print(f"\n  Feature comparison: d1+ predicted vs d0 predicted:")
        print(f"  {'Feature':<25s} {'d1+ mean':>12s} {'d0 mean':>12s} {'diff%':>8s}")
        print(f"  {'-'*25} {'-'*12} {'-'*12} {'-'*8}")
        for i, fname in enumerate(FEATURE_NAMES):
            mis_mean = float(np.mean(X_mis[:, i]))
            cor_mean = float(np.mean(X_correct[:, i])) if len(X_correct) > 0 else 0
            diff = abs(mis_mean - cor_mean) / (abs(cor_mean) + 1e-8) * 100
            misclass_analysis[fname] = {
                "d1plus_mean": mis_mean,
                "d0_mean": cor_mean,
                "diff_pct": diff,
            }
            if diff > 20:
                print(f"  {fname:<25s} {mis_mean:>12.4f} {cor_mean:>12.4f} {diff:>7.1f}%")

        # Show sample texts of misclassified passages
        mis_indices = np.where(misclassified_mask)[0][:10]
        print(f"\n  Sample misclassified passages (first {len(mis_indices)}):")
        for idx in mis_indices:
            text_preview = c4_passages[idx]["text"][:120].replace("\n", " ")
            print(f"    [{idx}] pred=d{c4_pred[idx]} P(d0)={c4_prob[idx,0]:.3f} | {text_preview}...")

    # ── Step 8: Build calibration table (C4 + WikiText + controlled) ──
    print("\n" + "="*60)
    print("  Step 8: Combined Calibration Table")
    print("="*60)

    cal_table = {}

    # C4 row
    cal_table["c4_web"] = {
        "n_samples": n_c4,
        "true_depth": "d0 (human, C4 web crawl)",
        "pred_distribution": {f"d{k}": int(v) for k, v in sorted(c4_pred_dist.items())},
        "pred_pct": {f"d{k}": round(v / n_c4 * 100, 2) for k, v in sorted(c4_pred_dist.items())},
        "mean_prob": {f"d{i}": round(float(c4_prob[:, i].mean()), 4) for i in range(4)},
    }

    # WikiText row (from previous results)
    if os.path.exists(WIKI_RESULTS_PATH):
        wiki_results = json.load(open(WIKI_RESULTS_PATH))
        wiki_cal = wiki_results.get("calibration_table", {}).get("wikitext_d0", {})
        if wiki_cal:
            cal_table["wikitext"] = wiki_cal

    # Controlled rows
    ctrl_pred = rf.predict(X_ctrl_s)
    ctrl_prob = rf.predict_proba(X_ctrl_s)
    if ctrl_prob.shape[1] < 4:
        full_prob = np.zeros((ctrl_prob.shape[0], 4))
        for ci, c in enumerate(rf.classes_):
            full_prob[:, c] = ctrl_prob[:, ci]
        ctrl_prob = full_prob

    for d in range(4):
        mask = y_ctrl == d
        pred_d = ctrl_pred[mask]
        prob_d = ctrl_prob[mask]
        dist = Counter(int(x) for x in pred_d)
        n = int(mask.sum())
        cal_table[f"controlled_d{d}"] = {
            "n_samples": n,
            "true_depth": f"d{d} (controlled, Pythia nucleus)",
            "pred_distribution": {f"d{k}": int(v) for k, v in sorted(dist.items())},
            "pred_pct": {f"d{k}": round(v / n * 100, 2) for k, v in sorted(dist.items())},
            "mean_prob": {f"d{i}": round(float(prob_d[:, i].mean()), 4) for i in range(4)},
        }

    # Print calibration table
    print(f"\n  {'Source':<25s} {'n':>6s}  {'d0%':>6s} {'d1%':>6s} {'d2%':>6s} {'d3%':>6s}  {'P(d0)':>6s}")
    print(f"  {'-'*25} {'-'*6}  {'-'*6} {'-'*6} {'-'*6} {'-'*6}  {'-'*6}")
    row_order = ["c4_web"]
    if "wikitext" in cal_table:
        row_order.append("wikitext")
    row_order += [f"controlled_d{d}" for d in range(4)]
    for key in row_order:
        row = cal_table[key]
        pcts = row["pred_pct"]
        mp = row["mean_prob"]
        print(f"  {key:<25s} {row['n_samples']:>6d}  "
              f"{pcts.get('d0', 0):>6.1f} {pcts.get('d1', 0):>6.1f} "
              f"{pcts.get('d2', 0):>6.1f} {pcts.get('d3', 0):>6.1f}  "
              f"{mp.get('d0', 0):>6.4f}")

    # ── Step 9: Save all results ──
    print("\n" + "="*60)
    print("  Step 9: Saving Results")
    print("="*60)

    c4_d0_rate = round(float((c4_pred == 0).mean() * 100), 2)

    results = {
        "experiment": "plan_015_c4_supplement",
        "data_source": "allenai/c4 (en, validation)",
        "model_cell": "pythia_nucleus",
        "feature_model": "pythia-1.4b",
        "rf_config": {"n_estimators": 200, "seed": args.seed},
        "cv_accuracy": {"mean": round(float(np.mean(cv_accs)), 4), "std": round(float(np.std(cv_accs)), 4)},
        "n_c4_passages": n_c4,
        "trunc_len": args.trunc_len,
        "min_tokens": args.min_tokens,
        "c4_d0_prediction_rate": c4_d0_rate,
        "c4_prediction_distribution": {f"d{d}": int(c4_pred_dist.get(d, 0)) for d in range(4)},
        "c4_prediction_pct": {f"d{d}": round(c4_pred_dist.get(d, 0) / n_c4 * 100, 2) for d in range(4)},
        "c4_mean_prob": {f"d{i}": round(float(c4_prob[:, i].mean()), 4) for i in range(4)},
        "c4_std_prob": {f"d{i}": round(float(c4_prob[:, i].std()), 4) for i in range(4)},
        "calibration_table": cal_table,
        "feature_stats": {k: {kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in v.items()} for k, v in feature_stats.items()},
        "n_misclassified_d1plus": int(n_misclassified),
        "misclassification_analysis": misclass_analysis if n_misclassified > 0 else {},
        "feature_importance": {
            fname: round(float(imp), 4)
            for fname, imp in zip(FEATURE_NAMES, rf.feature_importances_)
        },
    }

    # Comparison with WikiText
    if os.path.exists(WIKI_RESULTS_PATH):
        wiki_r = json.load(open(WIKI_RESULTS_PATH))
        results["comparison_with_wikitext"] = {
            "wikitext_d0_rate": wiki_r.get("wiki_d0_prediction_rate", None),
            "c4_d0_rate": c4_d0_rate,
            "wikitext_n": wiki_r.get("n_wiki_passages", None),
            "c4_n": n_c4,
        }

    results_path = os.path.join(OUTPUT_DIR, "c4_calibration.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved {results_path}")

    # Per-sample predictions
    preds_path = os.path.join(OUTPUT_DIR, "c4_predictions.jsonl")
    with open(preds_path, "w") as f:
        for i in range(n_c4):
            row = {
                "sample_id": i,
                "predicted_depth": int(c4_pred[i]),
                "prob_d0": round(float(c4_prob[i, 0]), 4),
                "prob_d1": round(float(c4_prob[i, 1]), 4),
                "prob_d2": round(float(c4_prob[i, 2]), 4),
                "prob_d3": round(float(c4_prob[i, 3]), 4),
            }
            f.write(json.dumps(row) + "\n")
    print(f"  Saved {preds_path}")

    # ── Final Summary ──
    print("\n" + "="*60)
    print("  FINAL SUMMARY")
    print("="*60)
    print(f"\n  C4 web-crawl d0 prediction rate: {c4_d0_rate:.1f}%")
    print(f"  C4 prediction breakdown:")
    for d in range(4):
        n = c4_pred_dist.get(d, 0)
        print(f"    d{d}: {n} ({n/n_c4*100:.1f}%)")
    if os.path.exists(WIKI_RESULTS_PATH):
        print(f"\n  WikiText-103 d0 rate (for reference): {wiki_r.get('wiki_d0_prediction_rate', 'N/A')}%")
    print(f"  5-fold CV accuracy: {np.mean(cv_accs):.4f} +/- {np.std(cv_accs):.4f}")
    print(f"  All results saved to {OUTPUT_DIR}/")
    print("  Done.")


if __name__ == "__main__":
    main()
