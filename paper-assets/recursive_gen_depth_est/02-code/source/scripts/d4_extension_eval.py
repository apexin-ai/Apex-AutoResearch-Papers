# GPT-2 XL nucleus d4 depth extension: feature extraction + 5-class RF evaluation.
# d4 data (depth_4.jsonl) and LoRA adapter (lora_depth_3) already exist.
# This script: (1) extract d4 features using Pythia-1.4B ref, (2) 5-class RF eval.

import json
import os
import sys
import time
import numpy as np
import torch
from collections import Counter
from scipy.stats import skew, kurtosis, entropy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

SEED = 42
np.random.seed(SEED)

BASE = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_DIR = os.path.join(BASE, "data/gpt2xl")
REF_MODEL = "/root/autodl-tmp/models/pythia-1.4b"
OUTPUT_DIR = os.path.join(BASE, "results/d4_extension_gpt2xl")
EXISTING_FEATURES = os.path.join(DATA_DIR, "features.jsonl")
D4_TEXT = os.path.join(DATA_DIR, "depth_4.jsonl")
D4_FEATURES_OUT = os.path.join(OUTPUT_DIR, "features_d4.jsonl")
RESULTS_OUT = os.path.join(OUTPUT_DIR, "d4_extension_results.json")

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

BATCH_SIZE = 16
N_FOLDS = 5
N_ESTIMATORS = 200

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def compute_repetition(token_ids, n):
    if len(token_ids) < n:
        return 0.0
    ngrams = [tuple(token_ids[i:i+n]) for i in range(len(token_ids) - n + 1)]
    total = len(ngrams)
    unique = len(set(ngrams))
    return 1.0 - unique / total if total > 0 else 0.0


def compute_lexical_features(token_ids):
    total = len(token_ids)
    if total == 0:
        return {k: 0.0 for k in [
            "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
            "rep_2gram", "rep_3gram", "rep_4gram"]}

    counts = Counter(token_ids)
    unique = len(counts)
    ttr = unique / total
    hapax = sum(1 for c in counts.values() if c == 1)
    hapax_ratio = hapax / unique if unique > 0 else 0.0

    bigrams = [tuple(token_ids[i:i+2]) for i in range(total - 1)]
    if bigrams:
        bg_counts = Counter(bigrams)
        bg_freq = np.array(list(bg_counts.values()), dtype=np.float64)
        bg_freq /= bg_freq.sum()
        bg_ent = float(entropy(bg_freq))
    else:
        bg_ent = 0.0

    trigrams = [tuple(token_ids[i:i+3]) for i in range(total - 2)]
    if trigrams:
        tg_counts = Counter(trigrams)
        tg_freq = np.array(list(tg_counts.values()), dtype=np.float64)
        tg_freq /= tg_freq.sum()
        tg_ent = float(entropy(tg_freq))
    else:
        tg_ent = 0.0

    return {
        "type_token_ratio": ttr,
        "hapax_ratio": hapax_ratio,
        "bigram_entropy": bg_ent,
        "trigram_entropy": tg_ent,
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


def compute_truncation_length(texts, tokenizer):
    lengths = []
    for text in texts:
        ids = tokenizer.encode(text, add_special_tokens=False)
        lengths.append(len(ids))
    med = int(np.median(lengths))
    print(f"  n={len(lengths)}, median={med}, min={min(lengths)}, max={max(lengths)}, mean={np.mean(lengths):.0f}")
    return med


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def load_features_matrix(records):
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.clip(X, -1e10, 1e10)
    X = np.nan_to_num(X, nan=0.0, posinf=1e10, neginf=-1e10)
    return X, y


def bootstrap_ci(scores, n_boot=2000, ci=0.95):
    rng = np.random.RandomState(SEED)
    boot_means = []
    for _ in range(n_boot):
        idx = rng.choice(len(scores), len(scores), replace=True)
        boot_means.append(np.mean(np.array(scores)[idx]))
    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)
    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)
    return float(lo), float(hi)


# === Phase 1: Feature extraction for d4 ===
def phase1_extract_d4_features():
    print("=" * 60)
    print("Phase 1: Extract d4 features using Pythia-1.4B reference")
    print("=" * 60)

    if os.path.exists(D4_FEATURES_OUT):
        n_lines = sum(1 for _ in open(D4_FEATURES_OUT))
        if n_lines >= 4900:
            print(f"  d4 features already exist ({n_lines} lines), skipping extraction.")
            return

    d4_records = load_jsonl(D4_TEXT)
    print(f"  Loaded {len(d4_records)} d4 texts")
    d4_texts = [r["text"] for r in d4_records]

    print(f"  Loading tokenizer from {REF_MODEL} ...")
    tokenizer = AutoTokenizer.from_pretrained(REF_MODEL)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Compute truncation length from d0-d3 to match existing features
    print("  Computing truncation length from d0-d3 ...")
    d0d3_medians = []
    for d in range(4):
        fpath = os.path.join(DATA_DIR, f"depth_{d}.jsonl")
        recs = load_jsonl(fpath)
        lens = [len(tokenizer.encode(r["text"], add_special_tokens=False)) for r in recs]
        med = int(np.median(lens))
        d0d3_medians.append(med)
        print(f"    Depth {d}: n={len(lens)}, median={med}")
        del recs

    d4_lens = [len(tokenizer.encode(t, add_special_tokens=False)) for t in d4_texts]
    print(f"    Depth 4: n={len(d4_lens)}, median={int(np.median(d4_lens))}")

    trunc_len = min(d0d3_medians)
    print(f"  Truncation length (min d0-d3 median): {trunc_len}")

    print(f"  Loading model from {REF_MODEL} ...")
    model = AutoModelForCausalLM.from_pretrained(
        REF_MODEL, torch_dtype=torch.float16
    ).to(DEVICE)
    model.eval()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_f = open(D4_FEATURES_OUT, "w")
    sample_id = 0

    t0 = time.time()
    for start in tqdm(range(0, len(d4_texts), BATCH_SIZE), desc="d4 features", unit="batch"):
        end = min(start + BATCH_SIZE, len(d4_texts))
        batch_texts = d4_texts[start:end]
        try:
            batch_feats = extract_batch_features(model, tokenizer, batch_texts, trunc_len, DEVICE)
        except Exception as e:
            print(f"\n[WARN] Batch error at samples {start}-{end}: {e}")
            continue

        for feat in batch_feats:
            row = {"depth": 4, "sample_id": sample_id}
            row.update(feat)
            out_f.write(json.dumps(row) + "\n")
            sample_id += 1

    out_f.close()
    elapsed = time.time() - t0
    print(f"  Extracted {sample_id} d4 features in {elapsed:.1f}s -> {D4_FEATURES_OUT}")

    del model
    torch.cuda.empty_cache()


# === Phase 2: 5-class RF evaluation ===
def phase2_evaluate():
    print("\n" + "=" * 60)
    print("Phase 2: 5-class RF evaluation (d0-d4)")
    print("=" * 60)

    # Load existing d0-d3 features
    d0d3_records = load_jsonl(EXISTING_FEATURES)
    print(f"  Loaded {len(d0d3_records)} d0-d3 features")

    # Load d4 features
    d4_records = load_jsonl(D4_FEATURES_OUT)
    print(f"  Loaded {len(d4_records)} d4 features")

    all_records = d0d3_records + d4_records
    X, y = load_features_matrix(all_records)
    labels = sorted(np.unique(y))
    print(f"  Total: {len(y)} samples, classes={labels}")
    for d in labels:
        print(f"    d{d}: {np.sum(y == d)} samples")

    # 5-fold CV
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    fold_accs = []
    all_preds = np.zeros(len(y), dtype=np.int64)
    all_probs = np.zeros((len(y), len(labels)), dtype=np.float64)
    importances = np.zeros(X.shape[1])

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        rf = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=SEED, n_jobs=-1)
        rf.fit(X[train_idx], y[train_idx])
        preds = rf.predict(X[test_idx])
        probs = rf.predict_proba(X[test_idx])
        acc = np.mean(preds == y[test_idx])
        fold_accs.append(acc)
        all_preds[test_idx] = preds
        all_probs[test_idx] = probs
        importances += rf.feature_importances_
        print(f"    Fold {fold_i+1}: acc={acc:.4f}")

    importances /= N_FOLDS
    mean_acc = float(np.mean(fold_accs))
    ci_lo, ci_hi = bootstrap_ci(fold_accs)

    print(f"\n  5-class accuracy: {mean_acc:.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")

    # Per-class recall
    per_class_recall = {}
    for d in labels:
        mask = (y == d)
        per_class_recall[f"d{d}"] = round(float(np.mean(all_preds[mask] == d)), 4)
    print(f"  Per-class recall: {per_class_recall}")

    # d3 vs d4 pairwise AUC
    d3v4_auc = None
    mask_34 = np.isin(y, [3, 4])
    if mask_34.sum() > 0:
        yt = (y[mask_34] == 4).astype(int)
        d4_idx = list(labels).index(4)
        yp = all_probs[mask_34, d4_idx]
        if len(np.unique(yt)) == 2:
            d3v4_auc = float(roc_auc_score(yt, yp))
    print(f"  d3 vs d4 AUC: {d3v4_auc}")

    # All pairwise AUCs
    pairwise_aucs = {}
    for i, di in enumerate(labels):
        for j, dj in enumerate(labels):
            if di >= dj:
                continue
            mask_ij = np.isin(y, [di, dj])
            if mask_ij.sum() > 0:
                yt = (y[mask_ij] == dj).astype(int)
                dj_idx = list(labels).index(dj)
                yp = all_probs[mask_ij, dj_idx]
                if len(np.unique(yt)) == 2:
                    auc = float(roc_auc_score(yt, yp))
                    pairwise_aucs[f"d{di}v{dj}"] = round(auc, 4)

    # Feature trends
    feature_trends = {}
    for feat_name in ["p90_ppl", "var_surprisal", "mean_ppl"]:
        feat_idx = FEATURE_NAMES.index(feat_name)
        trend = {}
        for d in labels:
            mask = (y == d)
            vals = X[mask, feat_idx]
            trend[f"d{d}"] = round(float(np.mean(vals)), 4)
        feature_trends[feat_name] = trend
        vals_str = ", ".join([f"d{d}={trend[f'd{d}']:.2f}" for d in labels])
        print(f"  {feat_name} trend: {vals_str}")

    # Check monotonicity
    for feat_name in ["p90_ppl", "var_surprisal", "mean_ppl"]:
        vals = [feature_trends[feat_name][f"d{d}"] for d in labels]
        diffs = [vals[i+1] - vals[i] for i in range(len(vals)-1)]
        monotonic = all(d > 0 for d in diffs) or all(d < 0 for d in diffs)
        print(f"    {feat_name} monotonic: {monotonic}")

    # Top features
    top_idx = np.argsort(importances)[::-1][:5]
    top_features = [(FEATURE_NAMES[i], round(float(importances[i]), 4)) for i in top_idx]

    results = {
        "d3v4_auc": round(d3v4_auc, 4) if d3v4_auc else None,
        "rf_5class_acc": round(mean_acc, 4),
        "rf_5class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "fold_accs": [round(a, 4) for a in fold_accs],
        "per_class_recall": per_class_recall,
        "pairwise_aucs": pairwise_aucs,
        "feature_trends": feature_trends,
        "top_features": top_features,
        "n_samples": int(len(y)),
        "class_dist": {f"d{d}": int(np.sum(y == d)) for d in labels},
        "seed": SEED,
        "n_estimators": N_ESTIMATORS,
        "n_folds": N_FOLDS,
        "ref_model": "pythia-1.4b",
    }

    with open(RESULTS_OUT, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Results saved to {RESULTS_OUT}")
    print(json.dumps(results, indent=2))

    return results


if __name__ == "__main__":
    t_start = time.time()
    print(f"Device: {DEVICE}")
    print(f"d4 text: {D4_TEXT}")
    print(f"Existing features: {EXISTING_FEATURES}")
    print(f"Output dir: {OUTPUT_DIR}")

    phase1_extract_d4_features()
    phase2_evaluate()

    print(f"\nTotal time: {time.time() - t_start:.1f}s")
