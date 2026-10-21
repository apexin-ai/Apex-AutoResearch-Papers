#!/usr/bin/env python3
"""
Plan 015: Wild-Data Calibration — WikiText-103 evaluation.

Evaluates the trained RF depth estimator on non-controlled human text (WikiText-103).
Compares predicted depth distribution against controlled d0/d1/d2/d3 synthetic data.

Output: results/plan_015_wild_data/
"""

import argparse
import json
import os
import sys
import numpy as np
from collections import Counter
from scipy.stats import skew, kurtosis, entropy
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
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
MODEL_PATH = "/root/autodl-tmp/models/pythia-1.4b"
FEATURES_PATH = os.path.join(PROJECT_DIR, "data/features_all.jsonl")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "results/plan_015_wild_data")


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


def prepare_wikitext_passages(tokenizer, n_passages=5000, trunc_len=498, seed=42):
    """Download WikiText-103 test set and segment into fixed-length passages."""
    from datasets import load_dataset

    print("Loading WikiText-103 test set...")
    ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="test",
                       cache_dir="/root/autodl-tmp/.hf_cache")

    all_tokens = []
    for item in ds:
        text = item["text"].strip()
        if not text or text.startswith("="):
            continue
        ids = tokenizer.encode(text, add_special_tokens=False)
        all_tokens.extend(ids)

    print(f"  Total tokens from WikiText-103 test: {len(all_tokens)}")

    passages = []
    for i in range(0, len(all_tokens) - trunc_len, trunc_len):
        passage_ids = all_tokens[i:i + trunc_len]
        text = tokenizer.decode(passage_ids)
        passages.append({"text": text, "token_ids": passage_ids})

    print(f"  Total passages (length {trunc_len}): {len(passages)}")

    rng = np.random.RandomState(seed)
    if len(passages) > n_passages:
        idx = rng.choice(len(passages), n_passages, replace=False)
        passages = [passages[i] for i in sorted(idx)]
    print(f"  Sampled {len(passages)} passages")

    return passages


def extract_features_for_texts(model, tokenizer, texts, trunc_len, device, batch_size=16, desc="Features"):
    """Extract 19 features for a list of texts."""
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


def features_to_array(features_list):
    X = np.array([[f[k] for k in FEATURE_NAMES] for f in features_list], dtype=np.float64)
    return np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)


def compute_calibration_table(y_true_labels, y_pred, y_prob, label_names):
    """Compute prediction distribution for each true class."""
    table = {}
    for true_label, true_name in enumerate(label_names):
        mask = (y_true_labels == true_label) if isinstance(y_true_labels, np.ndarray) else np.ones(len(y_pred), dtype=bool)
        if mask.sum() == 0:
            continue
        pred_dist = Counter(y_pred[mask])
        n = mask.sum()
        row = {
            "n_samples": int(n),
            "pred_distribution": {f"d{k}": int(v) for k, v in sorted(pred_dist.items())},
            "pred_pct": {f"d{k}": round(v / n * 100, 2) for k, v in sorted(pred_dist.items())},
            "mean_prob": {f"d{i}": round(float(y_prob[mask, i].mean()), 4) for i in range(y_prob.shape[1])},
            "std_prob": {f"d{i}": round(float(y_prob[mask, i].std()), 4) for i in range(y_prob.shape[1])},
        }
        table[true_name] = row
    return table


def compute_reliability_diagram_data(y_true_binary, y_prob_class, n_bins=10):
    """Compute reliability diagram data for a single class (predicted prob vs actual fraction)."""
    bins = np.linspace(0, 1, n_bins + 1)
    bin_data = []
    for i in range(n_bins):
        lo, hi = bins[i], bins[i+1]
        mask = (y_prob_class >= lo) & (y_prob_class < hi)
        if i == n_bins - 1:
            mask = (y_prob_class >= lo) & (y_prob_class <= hi)
        n_in_bin = mask.sum()
        if n_in_bin == 0:
            bin_data.append({
                "bin_lo": round(lo, 2), "bin_hi": round(hi, 2),
                "mean_predicted_prob": None, "actual_fraction": None,
                "n_samples": 0
            })
        else:
            mean_pred = float(y_prob_class[mask].mean())
            actual_frac = float(y_true_binary[mask].mean())
            bin_data.append({
                "bin_lo": round(lo, 2), "bin_hi": round(hi, 2),
                "mean_predicted_prob": round(mean_pred, 4),
                "actual_fraction": round(actual_frac, 4),
                "n_samples": int(n_in_bin)
            })
    return bin_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--n_wiki_passages", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ----------------------------------------------------------------
    # Step 1: Load tokenizer and model
    # ----------------------------------------------------------------
    print(f"\nLoading tokenizer from {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Determine truncation length from training data
    print("Determining truncation length from training d0 data...")
    d0_path = os.path.join(PROJECT_DIR, "data/depth_0.jsonl")
    d0_lengths = []
    with open(d0_path) as f:
        for i, line in enumerate(f):
            if i >= 200:
                break
            rec = json.loads(line.strip())
            ids = tokenizer.encode(rec["text"], add_special_tokens=False)
            d0_lengths.append(len(ids))
    trunc_len = int(np.median(d0_lengths))
    print(f"  d0 median token length: {trunc_len} (from {len(d0_lengths)} samples)")

    print(f"\nLoading model from {MODEL_PATH}...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.float16
    ).to(device)
    model.eval()

    # ----------------------------------------------------------------
    # Step 2: Prepare WikiText-103 passages
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 2: WikiText-103 Data Preparation")
    print("="*60)
    wiki_passages = prepare_wikitext_passages(
        tokenizer, n_passages=args.n_wiki_passages, trunc_len=trunc_len, seed=args.seed
    )
    wiki_texts = [p["text"] for p in wiki_passages]

    # Save raw wiki passages
    wiki_path = os.path.join(OUTPUT_DIR, "wikitext_passages.jsonl")
    with open(wiki_path, "w") as f:
        for i, p in enumerate(wiki_passages):
            f.write(json.dumps({"text": p["text"], "sample_id": i, "source": "wikitext-103-test"}) + "\n")
    print(f"  Saved {len(wiki_passages)} passages to {wiki_path}")

    # ----------------------------------------------------------------
    # Step 3: Extract features from WikiText passages
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 3: WikiText Feature Extraction")
    print("="*60)
    wiki_features = extract_features_for_texts(
        model, tokenizer, wiki_texts, trunc_len, device,
        batch_size=args.batch_size, desc="WikiText features"
    )

    # Save wiki features
    wiki_feat_path = os.path.join(OUTPUT_DIR, "wikitext_features.jsonl")
    with open(wiki_feat_path, "w") as f:
        for i, feat in enumerate(wiki_features):
            row = {"depth": -1, "sample_id": i, "source": "wikitext-103-test"}
            row.update(feat)
            f.write(json.dumps(row) + "\n")
    print(f"  Saved features to {wiki_feat_path}")

    X_wiki = features_to_array(wiki_features)
    print(f"  WikiText feature matrix: {X_wiki.shape}")

    # Free GPU memory
    del model
    torch.cuda.empty_cache()
    print("  Model unloaded, GPU memory freed.")

    # ----------------------------------------------------------------
    # Step 4: Load controlled data and train RF
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 4: Train RF on Pythia Nucleus Data")
    print("="*60)
    print(f"Loading features from {FEATURES_PATH}...")
    X_ctrl, y_ctrl = load_features(FEATURES_PATH)
    print(f"  Controlled data: {X_ctrl.shape[0]} samples, {X_ctrl.shape[1]} features")
    print(f"  Depth distribution: {dict(Counter(y_ctrl))}")

    scaler = StandardScaler()
    X_ctrl_s = scaler.fit_transform(X_ctrl)

    # 5-fold CV to get in-sample performance estimate
    print("\n  Running 5-fold CV...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=args.seed)
    cv_accs = []
    for fold, (train_idx, val_idx) in enumerate(skf.split(X_ctrl_s, y_ctrl)):
        rf_cv = RandomForestClassifier(n_estimators=200, random_state=args.seed, n_jobs=-1)
        rf_cv.fit(X_ctrl_s[train_idx], y_ctrl[train_idx])
        pred = rf_cv.predict(X_ctrl_s[val_idx])
        acc = accuracy_score(y_ctrl[val_idx], pred)
        cv_accs.append(acc)
    print(f"  5-fold CV accuracy: {np.mean(cv_accs):.4f} ± {np.std(cv_accs):.4f}")

    # Train final RF on all controlled data
    print("\n  Training final RF (n_estimators=200, all data)...")
    rf = RandomForestClassifier(n_estimators=200, random_state=args.seed, n_jobs=-1)
    rf.fit(X_ctrl_s, y_ctrl)

    # ----------------------------------------------------------------
    # Step 5: Predictions
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 5: Predictions")
    print("="*60)

    # Predict on WikiText
    X_wiki_s = scaler.transform(X_wiki)
    wiki_pred = rf.predict(X_wiki_s)
    wiki_prob = rf.predict_proba(X_wiki_s)
    if wiki_prob.shape[1] < 4:
        full_prob = np.zeros((wiki_prob.shape[0], 4))
        for i, c in enumerate(rf.classes_):
            full_prob[:, c] = wiki_prob[:, i]
        wiki_prob = full_prob

    print(f"\n  WikiText predictions (n={len(wiki_pred)}):")
    wiki_pred_dist = Counter(wiki_pred)
    for d in range(4):
        n = wiki_pred_dist.get(d, 0)
        pct = n / len(wiki_pred) * 100
        print(f"    d{d}: {n} ({pct:.1f}%)")

    # Predict on controlled data (each depth separately)
    ctrl_pred = rf.predict(X_ctrl_s)
    ctrl_prob = rf.predict_proba(X_ctrl_s)
    if ctrl_prob.shape[1] < 4:
        full_prob = np.zeros((ctrl_prob.shape[0], 4))
        for i, c in enumerate(rf.classes_):
            full_prob[:, c] = ctrl_prob[:, i]
        ctrl_prob = full_prob

    print(f"\n  Controlled data confusion matrix:")
    cm = confusion_matrix(y_ctrl, ctrl_pred, labels=[0,1,2,3])
    cm_pct = cm.astype(float) / cm.sum(axis=1, keepdims=True) * 100
    print(f"    {'':>8s} pred_d0  pred_d1  pred_d2  pred_d3")
    for i in range(4):
        row = "    " + f"true_d{i}  "
        row += "  ".join([f"{cm_pct[i,j]:6.1f}%" for j in range(4)])
        print(row)

    # ----------------------------------------------------------------
    # Step 6: Calibration Table
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 6: Calibration Analysis")
    print("="*60)

    # WikiText as "true d0"
    wiki_true = np.zeros(len(wiki_pred), dtype=np.int64)
    cal_table = {}

    # WikiText row
    cal_table["wikitext_d0"] = {
        "n_samples": len(wiki_pred),
        "true_depth": "d0 (human, WikiText-103)",
        "pred_distribution": {f"d{k}": int(v) for k, v in sorted(Counter(wiki_pred).items())},
        "pred_pct": {f"d{k}": round(v / len(wiki_pred) * 100, 2) for k, v in sorted(Counter(wiki_pred).items())},
        "mean_prob": {f"d{i}": round(float(wiki_prob[:, i].mean()), 4) for i in range(4)},
        "std_prob": {f"d{i}": round(float(wiki_prob[:, i].std()), 4) for i in range(4)},
    }

    # Controlled data rows (per depth)
    for d in range(4):
        mask = y_ctrl == d
        pred_d = ctrl_pred[mask]
        prob_d = ctrl_prob[mask]
        dist = Counter(pred_d)
        n = mask.sum()
        cal_table[f"controlled_d{d}"] = {
            "n_samples": int(n),
            "true_depth": f"d{d} (controlled, Pythia nucleus)",
            "pred_distribution": {f"d{k}": int(v) for k, v in sorted(dist.items())},
            "pred_pct": {f"d{k}": round(v / n * 100, 2) for k, v in sorted(dist.items())},
            "mean_prob": {f"d{i}": round(float(prob_d[:, i].mean()), 4) for i in range(4)},
            "std_prob": {f"d{i}": round(float(prob_d[:, i].std()), 4) for i in range(4)},
        }

    # Print calibration table
    print("\n  Calibration Table (predicted depth distribution %):")
    print(f"  {'Source':<25s} {'n':>6s}  {'d0%':>6s} {'d1%':>6s} {'d2%':>6s} {'d3%':>6s}")
    print(f"  {'-'*25} {'-'*6}  {'-'*6} {'-'*6} {'-'*6} {'-'*6}")
    for key in ["wikitext_d0", "controlled_d0", "controlled_d1", "controlled_d2", "controlled_d3"]:
        row = cal_table[key]
        pcts = row["pred_pct"]
        print(f"  {key:<25s} {row['n_samples']:>6d}  "
              f"{pcts.get('d0', 0):>6.1f} {pcts.get('d1', 0):>6.1f} "
              f"{pcts.get('d2', 0):>6.1f} {pcts.get('d3', 0):>6.1f}")

    # ----------------------------------------------------------------
    # Step 7: Reliability Diagram Data
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 7: Reliability Diagram Data")
    print("="*60)

    # For reliability diagram: combine WikiText (true d0) + controlled data
    all_true = np.concatenate([wiki_true, y_ctrl])
    all_prob = np.vstack([wiki_prob, ctrl_prob])
    all_pred = np.concatenate([wiki_pred, ctrl_pred])
    all_source = np.array(["wikitext"] * len(wiki_pred) + ["controlled"] * len(ctrl_pred))

    reliability_data = {}
    for d in range(4):
        y_binary = (all_true == d).astype(int)
        p_class = all_prob[:, d]
        bins = compute_reliability_diagram_data(y_binary, p_class, n_bins=10)
        reliability_data[f"d{d}"] = bins

    # WikiText-only reliability (all should be d0)
    wiki_reliability = {}
    for d in range(4):
        y_binary = (wiki_true == d).astype(int)
        p_class = wiki_prob[:, d]
        bins = compute_reliability_diagram_data(y_binary, p_class, n_bins=10)
        wiki_reliability[f"d{d}"] = bins

    # ----------------------------------------------------------------
    # Step 8: Probability Distribution Statistics
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 8: Probability Distribution Statistics")
    print("="*60)

    prob_stats = {}
    # WikiText
    prob_stats["wikitext"] = {
        f"d{i}": {
            "mean": round(float(wiki_prob[:, i].mean()), 4),
            "std": round(float(wiki_prob[:, i].std()), 4),
            "median": round(float(np.median(wiki_prob[:, i])), 4),
            "p10": round(float(np.percentile(wiki_prob[:, i], 10)), 4),
            "p90": round(float(np.percentile(wiki_prob[:, i], 90)), 4),
        }
        for i in range(4)
    }
    # Controlled per depth
    for d in range(4):
        mask = y_ctrl == d
        prob_d = ctrl_prob[mask]
        prob_stats[f"controlled_d{d}"] = {
            f"d{i}": {
                "mean": round(float(prob_d[:, i].mean()), 4),
                "std": round(float(prob_d[:, i].std()), 4),
                "median": round(float(np.median(prob_d[:, i])), 4),
                "p10": round(float(np.percentile(prob_d[:, i], 10)), 4),
                "p90": round(float(np.percentile(prob_d[:, i], 90)), 4),
            }
            for i in range(4)
        }

    print("\n  WikiText predict_proba summary:")
    for i in range(4):
        s = prob_stats["wikitext"][f"d{i}"]
        print(f"    P(d{i}): mean={s['mean']:.4f}, std={s['std']:.4f}, "
              f"median={s['median']:.4f}, [p10={s['p10']:.4f}, p90={s['p90']:.4f}]")

    # ----------------------------------------------------------------
    # Step 9: Domain Shift Analysis
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 9: Domain Shift Analysis")
    print("="*60)

    # Compare WikiText d0 features vs controlled d0 features
    ctrl_d0_mask = y_ctrl == 0
    X_ctrl_d0 = X_ctrl[ctrl_d0_mask]
    domain_shift = {}
    for i, fname in enumerate(FEATURE_NAMES):
        wiki_vals = X_wiki[:, i]
        ctrl_vals = X_ctrl_d0[:, i]
        shift = {
            "wiki_mean": round(float(np.mean(wiki_vals)), 4),
            "wiki_std": round(float(np.std(wiki_vals)), 4),
            "ctrl_mean": round(float(np.mean(ctrl_vals)), 4),
            "ctrl_std": round(float(np.std(ctrl_vals)), 4),
            "diff_pct": round(abs(np.mean(wiki_vals) - np.mean(ctrl_vals)) / (abs(np.mean(ctrl_vals)) + 1e-8) * 100, 2),
        }
        domain_shift[fname] = shift

    print("\n  Feature comparison (WikiText vs Controlled d0):")
    print(f"  {'Feature':<25s} {'Wiki mean':>12s} {'Ctrl mean':>12s} {'Diff%':>8s}")
    print(f"  {'-'*25} {'-'*12} {'-'*12} {'-'*8}")
    for fname in FEATURE_NAMES:
        s = domain_shift[fname]
        print(f"  {fname:<25s} {s['wiki_mean']:>12.4f} {s['ctrl_mean']:>12.4f} {s['diff_pct']:>7.1f}%")

    # ----------------------------------------------------------------
    # Step 10: Save all results
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  Step 10: Saving Results")
    print("="*60)

    results = {
        "experiment": "plan_015_wild_data_calibration",
        "model_cell": "pythia_nucleus",
        "feature_model": "pythia-1.4b",
        "rf_config": {"n_estimators": 200, "seed": args.seed},
        "cv_accuracy": {"mean": round(float(np.mean(cv_accs)), 4), "std": round(float(np.std(cv_accs)), 4)},
        "n_wiki_passages": len(wiki_pred),
        "trunc_len": trunc_len,
        "calibration_table": cal_table,
        "probability_stats": prob_stats,
        "domain_shift": domain_shift,
        "reliability_diagram_combined": reliability_data,
        "reliability_diagram_wikitext": wiki_reliability,
        "wiki_d0_prediction_rate": round(float((wiki_pred == 0).mean() * 100), 2),
        "wiki_misclassification": {
            f"d{d}": round(float((wiki_pred == d).mean() * 100), 2) for d in range(4)
        },
        "feature_importance": {
            fname: round(float(imp), 4)
            for fname, imp in zip(FEATURE_NAMES, rf.feature_importances_)
        },
    }

    # Main results JSON
    results_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved results to {results_path}")

    # Calibration table standalone
    cal_path = os.path.join(OUTPUT_DIR, "calibration_table.json")
    with open(cal_path, "w") as f:
        json.dump(cal_table, f, indent=2)
    print(f"  Saved calibration table to {cal_path}")

    # Reliability diagram data
    rel_path = os.path.join(OUTPUT_DIR, "reliability_diagram.json")
    with open(rel_path, "w") as f:
        json.dump({"combined": reliability_data, "wikitext_only": wiki_reliability}, f, indent=2)
    print(f"  Saved reliability diagram data to {rel_path}")

    # Probability stats
    prob_path = os.path.join(OUTPUT_DIR, "probability_stats.json")
    with open(prob_path, "w") as f:
        json.dump(prob_stats, f, indent=2)
    print(f"  Saved probability stats to {prob_path}")

    # Domain shift
    shift_path = os.path.join(OUTPUT_DIR, "domain_shift.json")
    with open(shift_path, "w") as f:
        json.dump(domain_shift, f, indent=2)
    print(f"  Saved domain shift analysis to {shift_path}")

    # Per-sample predictions
    preds_path = os.path.join(OUTPUT_DIR, "wikitext_predictions.jsonl")
    with open(preds_path, "w") as f:
        for i in range(len(wiki_pred)):
            row = {
                "sample_id": i,
                "predicted_depth": int(wiki_pred[i]),
                "prob_d0": round(float(wiki_prob[i, 0]), 4),
                "prob_d1": round(float(wiki_prob[i, 1]), 4),
                "prob_d2": round(float(wiki_prob[i, 2]), 4),
                "prob_d3": round(float(wiki_prob[i, 3]), 4),
            }
            f.write(json.dumps(row) + "\n")
    print(f"  Saved per-sample predictions to {preds_path}")

    # ----------------------------------------------------------------
    # Final Summary
    # ----------------------------------------------------------------
    print("\n" + "="*60)
    print("  FINAL SUMMARY")
    print("="*60)
    print(f"\n  WikiText-103 d0 prediction rate: {results['wiki_d0_prediction_rate']:.1f}%")
    print(f"  WikiText misclassification breakdown:")
    for d in range(4):
        print(f"    Predicted d{d}: {results['wiki_misclassification'][f'd{d}']:.1f}%")
    print(f"\n  5-fold CV accuracy on controlled data: {results['cv_accuracy']['mean']:.4f} ± {results['cv_accuracy']['std']:.4f}")
    print(f"\n  All results saved to {OUTPUT_DIR}/")
    print("  Done.")


if __name__ == "__main__":
    main()
