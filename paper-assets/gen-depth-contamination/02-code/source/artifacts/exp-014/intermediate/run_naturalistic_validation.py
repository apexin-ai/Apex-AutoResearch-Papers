"""
exp-014: Naturalistic Validation of OBD Depth Classifier on Common Crawl Data

Input:  C4 validation shard (held-out, different from training), labeled features.csv
Output: results/exp_014_naturalistic/ with depth predictions, correlations, distributions

Deps: torch, transformers, datasets, scipy, lightgbm, sklearn, numpy, tqdm
"""

import csv
import gc
import json
import logging
import math
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from scipy import stats
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
TRAINING_FEATURES = PROJECT_ROOT / "data_exp016_qwen_base" / "features.csv"
OUT_DIR = PROJECT_ROOT / "results" / "exp_014_naturalistic"
SCORER_MODEL = "/root/autodl-tmp/.hf_cache/models/Qwen/Qwen2.5-1.5B"
NUM_CC_SAMPLES = 5000
MAX_TOKENS = 256
BATCH_SIZE = 16
SEED = 42

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]


# ── Feature extraction (replicates run_pipeline.py logic) ─────────────

def ngrams(tokens, n):
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
    if len(candidate_tokens) == 0:
        return 0.0
    precisions = []
    for n in range(1, max_n + 1):
        cand_ngrams = ngrams(candidate_tokens, n)
        ref_ngrams = ngrams(reference_tokens, n)
        if not cand_ngrams:
            precisions.append(0.0)
            continue
        ref_counts = Counter(ref_ngrams)
        clipped = 0
        cand_counts = Counter(cand_ngrams)
        for ng, cnt in cand_counts.items():
            clipped += min(cnt, ref_counts.get(ng, 0))
        precisions.append(clipped / len(cand_ngrams))
    if any(p == 0 for p in precisions):
        return 0.0
    log_avg = sum(math.log(p) for p in precisions) / max_n
    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
    return bp * math.exp(log_avg)


def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
    all_features = []
    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
        batch_texts = texts[start : start + batch_size]
        inputs = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(model.device)

        with torch.no_grad():
            logits = model(**inputs).logits

        log_probs = torch.log_softmax(logits, dim=-1)
        input_ids = inputs["input_ids"]

        for i in range(len(batch_texts)):
            mask = inputs["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 3:
                all_features.append([0.0] * 9)
                continue

            offset = input_ids.shape[1] - seq_len
            token_ids = input_ids[i, offset:]
            token_log_probs = []
            for t in range(1, seq_len):
                lp = log_probs[i, offset + t - 1, token_ids[t]].item()
                token_log_probs.append(-lp)

            arr = np.array(token_log_probs)
            if len(arr) < 3:
                all_features.append([0.0] * 9)
                continue

            d1 = np.diff(arr)
            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])

            feats = [
                float(np.mean(arr)),
                float(np.std(arr)),
                float(stats.skew(arr)),
                float(stats.kurtosis(arr)),
                float(np.mean(d1)),
                float(np.std(d1)),
                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,
                float(np.mean(d2)),
                float(np.std(d2)),
            ]
            all_features.append(feats)

        torch.cuda.empty_cache()

    return all_features


def compute_vocab_diversity(texts, sample_bleu=200, bleu_refs=100):
    features = []
    tokenized = [t.split() for t in texts]
    rng = np.random.RandomState(SEED)
    bleu_indices = list(range(len(texts)))
    if len(bleu_indices) > sample_bleu:
        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()

    for idx, tokens in enumerate(tqdm(tokenized, desc="VocabDiv", leave=False)):
        total = len(tokens)
        if total == 0:
            features.append([0.0, 0.0, 0.0])
            continue

        unique = set(tokens)
        ttr = len(unique) / total

        freq = Counter(tokens)
        hapax = sum(1 for v in freq.values() if v == 1)
        hapax_ratio = hapax / max(len(unique), 1)

        rng_local = np.random.RandomState(idx)
        ref_pool = [j for j in range(len(tokenized)) if j != idx]
        if len(ref_pool) > bleu_refs:
            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
        bleu_scores = [simple_bleu(tokens, tokenized[j]) for j in ref_pool]
        self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0

        features.append([ttr, hapax_ratio, self_bleu])

    return features


def compute_tail_features(texts):
    features = []
    for text in texts:
        tokens = text.split()
        if len(tokens) < 2:
            features.append([0.0, 0.0, 0.0])
            continue
        freq = Counter(tokens)
        counts = np.array(list(freq.values()), dtype=float)

        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0
        total = counts.sum()
        probs = counts / total
        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
        low_freq_ratio = float(np.sum(counts <= 2)) / max(len(counts), 1)

        features.append([kurt, entropy, low_freq_ratio])

    return features


# ── Additional vocabulary richness metrics ────────────────────────────

def compute_extra_vocab_metrics(texts):
    """Compute additional vocab richness: Yule's K, mean word length, vocab growth rate."""
    results = []
    for text in texts:
        tokens = text.split()
        if len(tokens) < 5:
            results.append({"yules_k": 0.0, "mean_word_len": 0.0, "vocab_growth_rate": 0.0})
            continue

        freq = Counter(tokens)
        N = len(tokens)
        V = len(freq)

        # Yule's K: measure of vocabulary richness (lower = richer)
        freq_spectrum = Counter(freq.values())
        sum_fi_sq = sum(i * i * vi for i, vi in freq_spectrum.items())
        yules_k = 10000 * (sum_fi_sq - N) / (N * N) if N > 1 else 0.0

        # Mean word length
        mean_word_len = np.mean([len(w) for w in tokens]) if tokens else 0.0

        # Vocabulary growth rate (Heaps' law approximation): V = k * N^beta
        # Estimate beta from cumulative unique counts at 50% and 100%
        mid = N // 2
        if mid > 0:
            V_mid = len(set(tokens[:mid]))
            if V_mid > 0 and V > V_mid and mid > 0:
                beta = math.log(V / V_mid) / math.log(N / mid)
            else:
                beta = 0.0
        else:
            beta = 0.0

        results.append({
            "yules_k": float(yules_k),
            "mean_word_len": float(mean_word_len),
            "vocab_growth_rate": float(beta),
        })
    return results


# ── Data loading ──────────────────────────────────────────────────────

def load_training_features(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    depths = np.array([int(r["depth"]) for r in rows])
    X = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS] for r in rows]
    )
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def sample_cc_data(tokenizer, num_samples, max_tokens=256):
    import gzip
    import subprocess

    hf_endpoint = os.environ.get("HF_ENDPOINT", "https://hf-mirror.com")
    shard_file = "/root/autodl-tmp/.hf_cache/c4-validation-shard4.json.gz"

    if not os.path.exists(shard_file):
        shard_url = f"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00004-of-00008.json.gz"
        log.info(f"Downloading C4 validation shard 4 from {shard_url} ...")
        result = subprocess.run(
            ["wget", "-q", "--no-check-certificate", "-O", shard_file, shard_url],
            capture_output=True, text=True, timeout=600,
        )
        if result.returncode != 0:
            raise RuntimeError(f"wget failed: {result.stderr}")
    else:
        log.info(f"Using cached shard: {shard_file}")

    records = []
    with gzip.open(shard_file, "rt", encoding="utf-8") as f:
        for line in tqdm(f, total=num_samples, desc="Sampling CC"):
            if len(records) >= num_samples:
                break
            example = json.loads(line)
            text = example["text"].strip()
            if not text or len(text) < 50:
                continue
            ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
            truncated = tokenizer.decode(ids, skip_special_tokens=True)
            if len(truncated.split()) < 10:
                continue
            records.append({"text": truncated, "doc_id": len(records)})

    log.info(f"Sampled {len(records)} CC texts")
    return records


# ── Main experiment ───────────────────────────────────────────────────

def main():
    t_start = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Step 1: Train classifier on labeled data ──
    log.info("=" * 60)
    log.info("Step 1: Training OBD classifier on labeled data")
    log.info("=" * 60)

    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import roc_auc_score, accuracy_score

    X_train, depths_train, doc_ids_train = load_training_features(TRAINING_FEATURES)
    log.info(f"Training data: {len(depths_train)} rows, depths 0-{depths_train.max()}")
    for d in range(int(depths_train.max()) + 1):
        log.info(f"  depth {d}: {(depths_train == d).sum()} rows")

    # Binary classifier: depth-0 (human) vs depth-1+ (AI-generated)
    y_binary = (depths_train >= 1).astype(int)
    log.info(f"Binary split: human={int((y_binary == 0).sum())}, AI={int((y_binary == 1).sum())}")

    clf_binary = lgb.LGBMClassifier(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
    )
    clf_binary.fit(X_train, y_binary)

    # OOF validation for the binary classifier
    gkf = GroupKFold(n_splits=5)
    oof_proba = np.zeros(len(y_binary))
    for train_idx, test_idx in gkf.split(X_train, y_binary, groups=doc_ids_train):
        clf_fold = lgb.LGBMClassifier(
            n_estimators=300, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
        )
        clf_fold.fit(X_train[train_idx], y_binary[train_idx])
        oof_proba[test_idx] = clf_fold.predict_proba(X_train[test_idx])[:, 1]
    oof_auc = roc_auc_score(y_binary, oof_proba)
    log.info(f"Binary classifier OOF AUC: {oof_auc:.4f}")

    # Ordinal classifier: predict depth 0-5
    clf_ordinal = lgb.LGBMClassifier(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
        objective="multiclass", num_class=int(depths_train.max()) + 1,
    )
    clf_ordinal.fit(X_train, depths_train)
    log.info("Ordinal classifier trained (depth 0-5)")

    # Feature importance
    importance = clf_binary.feature_importances_
    feat_imp = sorted(zip(FEAT_COLS, importance.tolist()), key=lambda x: -x[1])
    log.info("Binary classifier feature importance:")
    for name, imp in feat_imp:
        log.info(f"  {name}: {imp}")

    # ── Step 2: Load scorer model ──
    log.info("=" * 60)
    log.info("Step 2: Loading scorer model")
    log.info("=" * 60)

    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading tokenizer for {SCORER_MODEL} ...")
    tokenizer = AutoTokenizer.from_pretrained(SCORER_MODEL, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    log.info(f"Loading model {SCORER_MODEL} ...")
    model = AutoModelForCausalLM.from_pretrained(
        SCORER_MODEL,
        torch_dtype=torch.float16,
        device_map={"": "cuda:0"},
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Model loaded on {model.device}")

    # ── Step 3: Sample CC data ──
    log.info("=" * 60)
    log.info("Step 3: Sampling Common Crawl (C4 held-out shard)")
    log.info("=" * 60)

    cc_records = sample_cc_data(tokenizer, NUM_CC_SAMPLES, MAX_TOKENS)
    cc_texts = [r["text"] for r in cc_records]

    # Save sampled texts
    cc_data_path = OUT_DIR / "cc_sample.jsonl"
    with open(cc_data_path, "w") as f:
        for r in cc_records:
            f.write(json.dumps(r) + "\n")
    log.info(f"Saved {len(cc_records)} CC texts to {cc_data_path}")

    # ── Step 4: Extract 15D features for CC data ──
    log.info("=" * 60)
    log.info("Step 4: Feature extraction on CC data")
    log.info("=" * 60)

    surp = compute_surprisal_features(model, tokenizer, cc_texts, batch_size=BATCH_SIZE)
    log.info(f"Surprisal features: {len(surp)} rows")

    del model
    torch.cuda.empty_cache()
    gc.collect()
    log.info("Scorer model unloaded to free GPU memory")

    vocab = compute_vocab_diversity(cc_texts)
    log.info(f"Vocab diversity features: {len(vocab)} rows")

    tail = compute_tail_features(cc_texts)
    log.info(f"Tail features: {len(tail)} rows")

    # Assemble feature matrix
    X_cc = np.zeros((len(cc_texts), len(FEAT_COLS)))
    for i in range(len(cc_texts)):
        for j, col in enumerate(SURPRISAL_COLS):
            X_cc[i, j] = surp[i][j]
        for j, col in enumerate(VOCAB_COLS):
            X_cc[i, 9 + j] = vocab[i][j]
        for j, col in enumerate(TAIL_COLS):
            X_cc[i, 12 + j] = tail[i][j]

    # Handle NaN
    col_means = np.nanmean(X_cc, axis=0)
    for j in range(X_cc.shape[1]):
        mask = np.isnan(X_cc[:, j])
        if mask.any():
            X_cc[mask, j] = col_means[j]

    # Save CC features
    cc_feat_path = OUT_DIR / "cc_features.csv"
    with open(cc_feat_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id"] + FEAT_COLS)
        writer.writeheader()
        for i in range(len(cc_texts)):
            row = {"doc_id": i}
            for j, col in enumerate(FEAT_COLS):
                row[col] = X_cc[i, j]
            writer.writerow(row)
    log.info(f"Saved CC features to {cc_feat_path}")

    # ── Step 5: Predict depth on CC data ──
    log.info("=" * 60)
    log.info("Step 5: Depth prediction on CC data")
    log.info("=" * 60)

    binary_proba = clf_binary.predict_proba(X_cc)[:, 1]
    binary_pred = clf_binary.predict(X_cc)
    ordinal_pred = clf_ordinal.predict(X_cc)
    ordinal_proba = clf_ordinal.predict_proba(X_cc)

    log.info(f"Binary predictions: human={int((binary_pred == 0).sum())}, AI={int((binary_pred == 1).sum())}")
    log.info(f"Ordinal predictions: {dict(zip(*np.unique(ordinal_pred, return_counts=True)))}")
    log.info(f"Mean AI probability: {binary_proba.mean():.4f}")

    # ── Step 6: Compute additional vocab richness metrics ──
    log.info("=" * 60)
    log.info("Step 6: Additional vocabulary richness metrics")
    log.info("=" * 60)

    extra_metrics = compute_extra_vocab_metrics(cc_texts)
    yules_k = np.array([m["yules_k"] for m in extra_metrics])
    mean_word_len = np.array([m["mean_word_len"] for m in extra_metrics])
    vocab_growth = np.array([m["vocab_growth_rate"] for m in extra_metrics])
    log.info(f"Extra vocab metrics computed for {len(extra_metrics)} texts")

    # ── Step 7: Correlation analysis ──
    log.info("=" * 60)
    log.info("Step 7: Correlation analysis")
    log.info("=" * 60)

    # Metrics to correlate with predicted depth
    correlation_targets = {
        "ttr": X_cc[:, FEAT_COLS.index("ttr")],
        "hapax_ratio": X_cc[:, FEAT_COLS.index("hapax_ratio")],
        "freq_entropy": X_cc[:, FEAT_COLS.index("freq_entropy")],
        "low_freq_ratio": X_cc[:, FEAT_COLS.index("low_freq_ratio")],
        "self_bleu": X_cc[:, FEAT_COLS.index("self_bleu")],
        "surp_mean": X_cc[:, FEAT_COLS.index("surp_mean")],
        "surp_std": X_cc[:, FEAT_COLS.index("surp_std")],
        "yules_k": yules_k,
        "mean_word_len": mean_word_len,
        "vocab_growth_rate": vocab_growth,
    }

    # Spearman correlations with binary AI probability
    corr_with_ai_prob = {}
    for name, values in correlation_targets.items():
        rho, pval = stats.spearmanr(binary_proba, values)
        corr_with_ai_prob[name] = {"rho": round(float(rho), 4), "pval": float(pval)}
        log.info(f"  AI_prob vs {name}: rho={rho:.4f}, p={pval:.2e}")

    # Spearman correlations with ordinal predicted depth
    corr_with_depth = {}
    for name, values in correlation_targets.items():
        rho, pval = stats.spearmanr(ordinal_pred, values)
        corr_with_depth[name] = {"rho": round(float(rho), 4), "pval": float(pval)}
        log.info(f"  pred_depth vs {name}: rho={rho:.4f}, p={pval:.2e}")

    # Depth-stratified means for key metrics
    depth_stratified = {}
    for d in range(int(ordinal_pred.max()) + 1):
        mask = ordinal_pred == d
        if mask.sum() == 0:
            continue
        depth_stratified[str(d)] = {
            "count": int(mask.sum()),
            "ttr_mean": round(float(X_cc[mask, FEAT_COLS.index("ttr")].mean()), 4),
            "hapax_ratio_mean": round(float(X_cc[mask, FEAT_COLS.index("hapax_ratio")].mean()), 4),
            "freq_entropy_mean": round(float(X_cc[mask, FEAT_COLS.index("freq_entropy")].mean()), 4),
            "surp_mean_mean": round(float(X_cc[mask, FEAT_COLS.index("surp_mean")].mean()), 4),
            "yules_k_mean": round(float(yules_k[mask].mean()), 4),
            "vocab_growth_mean": round(float(vocab_growth[mask].mean()), 4),
        }
        log.info(f"  depth {d} (n={mask.sum()}): TTR={depth_stratified[str(d)]['ttr_mean']:.4f}, "
                 f"entropy={depth_stratified[str(d)]['freq_entropy_mean']:.4f}, "
                 f"surp_mean={depth_stratified[str(d)]['surp_mean_mean']:.4f}")

    # ── Step 8: Save results ──
    log.info("=" * 60)
    log.info("Step 8: Saving results")
    log.info("=" * 60)

    total_time = time.time() - t_start

    results = {
        "experiment": "exp_014_naturalistic",
        "description": "Naturalistic validation of OBD depth classifier on CC data",
        "scorer_model": SCORER_MODEL,
        "num_cc_samples": len(cc_texts),
        "training_data": str(TRAINING_FEATURES),
        "training_rows": len(depths_train),
        "binary_classifier_oof_auc": round(oof_auc, 4),
        "feature_importance": feat_imp,
        "predictions": {
            "binary": {
                "human_count": int((binary_pred == 0).sum()),
                "ai_count": int((binary_pred == 1).sum()),
                "ai_fraction": round(float((binary_pred == 1).mean()), 4),
                "mean_ai_probability": round(float(binary_proba.mean()), 4),
                "median_ai_probability": round(float(np.median(binary_proba)), 4),
            },
            "ordinal": {
                "depth_distribution": {
                    str(d): int((ordinal_pred == d).sum())
                    for d in range(int(ordinal_pred.max()) + 1)
                },
            },
        },
        "correlations": {
            "ai_probability_vs_metrics": corr_with_ai_prob,
            "predicted_depth_vs_metrics": corr_with_depth,
        },
        "depth_stratified_means": depth_stratified,
        "total_time_seconds": round(total_time, 1),
        "seed": SEED,
    }

    result_path = OUT_DIR / "naturalistic_validation_results.json"
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {result_path}")

    # Save per-sample predictions
    predictions_path = OUT_DIR / "cc_predictions.csv"
    with open(predictions_path, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["doc_id", "binary_pred", "ai_probability", "ordinal_pred"] + \
                 [f"depth_{d}_prob" for d in range(ordinal_proba.shape[1])] + \
                 ["yules_k", "mean_word_len", "vocab_growth_rate"]
        writer.writerow(header)
        for i in range(len(cc_texts)):
            row = [
                i, int(binary_pred[i]), round(float(binary_proba[i]), 6),
                int(ordinal_pred[i]),
            ] + [round(float(ordinal_proba[i, d]), 6) for d in range(ordinal_proba.shape[1])] + [
                round(float(yules_k[i]), 6),
                round(float(mean_word_len[i]), 4),
                round(float(vocab_growth[i]), 6),
            ]
            writer.writerow(row)
    log.info(f"Per-sample predictions saved to {predictions_path}")

    log.info("=" * 60)
    log.info(f"exp-014 complete in {total_time:.1f}s")
    log.info(f"Key result: {float((binary_pred == 1).mean())*100:.1f}% of CC texts predicted as AI-generated")
    log.info(f"Binary classifier OOF AUC: {oof_auc:.4f}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
