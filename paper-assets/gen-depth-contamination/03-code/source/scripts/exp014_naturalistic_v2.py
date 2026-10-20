"""
exp-014 v2: Naturalistic Validation of OBD Depth Signal on FineWeb CC Data

Goal: Predict OBD depth on 50K FineWeb English docs and correlate with 9
independent quality metrics to validate depth signal's ecological validity.

Input:  FineWeb CC streaming (50K docs), exp_qwen_cont_10k/features.csv (training)
Output: data_exp014_v2/{cc_sample.jsonl, cc_features.csv, cc_predictions.csv}
        results/exp014_v2/{analysis_results.json, violin_*.pdf, depth_dist.pdf, mauve_*.pdf, run.log}

Deps: torch, transformers, datasets, scipy, lightgbm, sklearn, numpy, tqdm,
      lexical_diversity, mauve-text, matplotlib
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
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
TRAINING_FEATURES = PROJECT_ROOT / "data" / "exp_qwen_cont_10k" / "features.csv"
DATA_DIR = PROJECT_ROOT / "data_exp014_v2"
OUT_DIR = PROJECT_ROOT / "results" / "exp014_v2"
HF_CACHE = "/root/autodl-tmp/.hf_cache"
SCORER_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"
DEVICE = "cuda:1"

NUM_CC_SAMPLES = 50000
MAX_TOKENS = 256
BATCH_SIZE = 16
SEED = 42
MAX_DEPTH = 5  # depths 0..5 in training data

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

INDEPENDENT_METRICS = [
    "gpt2_ppl", "mauve_score",
    "mtld", "hdd", "trigram_rep", "quadgram_rep", "zipf_coeff",
]
OVERLAP_METRICS = ["ttr_indep", "hapax_indep"]
ALL_METRICS = INDEPENDENT_METRICS + OVERLAP_METRICS


# ═══════════════════════════════════════════════════════════════════════
# Utility functions
# ═══════════════════════════════════════════════════════════════════════

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


def timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")


# ═══════════════════════════════════════════════════════════════════════
# Phase 1: Data Sampling from FineWeb
# ═══════════════════════════════════════════════════════════════════════

def phase1_sample_data(tokenizer):
    log.info(f"{'='*60}")
    log.info(f"Phase 1: Data Sampling from FineWeb  [{timestamp()}]")
    log.info(f"{'='*60}")

    out_path = DATA_DIR / "cc_sample.jsonl"
    if out_path.exists():
        n_existing = sum(1 for _ in open(out_path))
        if n_existing >= NUM_CC_SAMPLES:
            log.info(f"cc_sample.jsonl already exists with {n_existing} samples — skipping")
            records = []
            with open(out_path) as f:
                for line in f:
                    records.append(json.loads(line))
            return records

    from datasets import load_dataset

    log.info("Loading FineWeb (streaming) ...")
    try:
        ds = load_dataset(
            "HuggingFaceFW/fineweb",
            name="CC-MAIN-2025-26",
            split="train",
            streaming=True,
            cache_dir=HF_CACHE,
        )
        log.info("Using FineWeb CC-MAIN-2025-26 subset")
    except Exception as e1:
        log.warning(f"CC-MAIN-2025-26 not available ({e1}), trying CC-MAIN-2024-51 ...")
        try:
            ds = load_dataset(
                "HuggingFaceFW/fineweb",
                name="CC-MAIN-2024-51",
                split="train",
                streaming=True,
                cache_dir=HF_CACHE,
            )
            log.info("Using FineWeb CC-MAIN-2024-51 subset")
        except Exception as e2:
            log.warning(f"CC-MAIN-2024-51 not available ({e2}), trying default ...")
            try:
                ds = load_dataset(
                    "HuggingFaceFW/fineweb",
                    name="default",
                    split="train",
                    streaming=True,
                    cache_dir=HF_CACHE,
                )
                log.info("Using FineWeb default subset")
            except Exception as e3:
                raise RuntimeError(
                    f"Failed to load FineWeb dataset after 3 attempts: "
                    f"CC-MAIN-2025-26 ({e1}), CC-MAIN-2024-51 ({e2}), default ({e3})"
                )

    records = []
    skipped_short = 0
    skipped_long = 0
    skipped_ascii = 0
    seen = 0

    for example in tqdm(ds, total=NUM_CC_SAMPLES * 3, desc="Sampling FineWeb"):
        seen += 1
        if len(records) >= NUM_CC_SAMPLES:
            break
        if seen > NUM_CC_SAMPLES * 20:
            log.warning(f"Scanned {seen} docs but only got {len(records)}, stopping")
            break

        text = example.get("text", "").strip()
        if not text:
            continue

        words = text.split()
        wc = len(words)
        if wc < 50:
            skipped_short += 1
            continue
        if wc > 1000:
            skipped_long += 1
            continue

        non_ascii = sum(1 for c in text if ord(c) > 127)
        if non_ascii / max(len(text), 1) > 0.30:
            skipped_ascii += 1
            continue

        ids = tokenizer.encode(text, add_special_tokens=False)[:MAX_TOKENS]
        truncated = tokenizer.decode(ids, skip_special_tokens=True)
        if len(truncated.split()) < 10:
            continue

        records.append({"text": truncated, "doc_id": len(records)})

        if len(records) % 10000 == 0:
            log.info(f"  Sampled {len(records)}/{NUM_CC_SAMPLES} docs (scanned {seen})")

    log.info(f"Sampled {len(records)} docs from {seen} scanned")
    log.info(f"  Skipped: short={skipped_short}, long={skipped_long}, non-ascii={skipped_ascii}")

    min_required = int(NUM_CC_SAMPLES * 0.9)
    if len(records) < min_required:
        raise RuntimeError(
            f"Only sampled {len(records)}/{NUM_CC_SAMPLES} docs (minimum {min_required}) "
            f"after scanning {seen} entries. Possible network issue or dataset exhausted."
        )

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    log.info(f"Saved to {out_path}")

    return records


# ═══════════════════════════════════════════════════════════════════════
# Phase 2: 15D Feature Extraction
# ═══════════════════════════════════════════════════════════════════════

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


def compute_vocab_diversity(texts, bleu_refs=100):
    """self-BLEU: sample 100 random docs from entire pool as universal reference."""
    features = []
    tokenized = [t.split() for t in texts]
    rng = np.random.RandomState(SEED)

    ref_indices = rng.choice(len(tokenized), min(bleu_refs, len(tokenized)), replace=False).tolist()

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

        ref_pool = [j for j in ref_indices if j != idx]
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


def phase2_extract_features(model, tokenizer, texts):
    log.info(f"{'='*60}")
    log.info(f"Phase 2: 15D Feature Extraction  [{timestamp()}]")
    log.info(f"{'='*60}")

    feat_path = DATA_DIR / "cc_features.csv"
    if feat_path.exists():
        n_existing = sum(1 for _ in open(feat_path)) - 1
        if n_existing >= len(texts):
            log.info(f"cc_features.csv already exists with {n_existing} rows — skipping")
            return feat_path

    log.info(f"Extracting surprisal features for {len(texts)} texts ...")
    surp = compute_surprisal_features(model, tokenizer, texts, batch_size=BATCH_SIZE)
    log.info(f"Surprisal done: {len(surp)} rows")

    log.info("Extracting vocab diversity features ...")
    vocab = compute_vocab_diversity(texts, bleu_refs=100)
    log.info(f"Vocab diversity done: {len(vocab)} rows")

    log.info("Extracting tail features ...")
    tail = compute_tail_features(texts)
    log.info(f"Tail features done: {len(tail)} rows")

    with open(feat_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["doc_id"] + FEAT_COLS)
        for i in range(len(texts)):
            row = [i] + surp[i] + vocab[i] + tail[i]
            writer.writerow([round(v, 8) if isinstance(v, float) else v for v in row])
    log.info(f"Features saved to {feat_path}")

    return feat_path


# ═══════════════════════════════════════════════════════════════════════
# Phase 3: OBD Depth Prediction
# ═══════════════════════════════════════════════════════════════════════

def load_features_csv(path, has_depth=True):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS] for r in rows]
    )
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]

    if has_depth:
        depths = np.array([int(r["depth"]) for r in rows])
        return X, depths, doc_ids
    return X, doc_ids


def phase3_obd_prediction(cc_feat_path):
    log.info(f"{'='*60}")
    log.info(f"Phase 3: OBD Depth Prediction  [{timestamp()}]")
    log.info(f"{'='*60}")

    pred_path = DATA_DIR / "cc_predictions.csv"
    if pred_path.exists():
        n_existing = sum(1 for _ in open(pred_path)) - 1
        if n_existing >= NUM_CC_SAMPLES * 0.9:
            log.info(f"cc_predictions.csv already exists with {n_existing} rows — skipping")
            return pred_path

    import lightgbm as lgb

    log.info(f"Loading training data from {TRAINING_FEATURES} ...")
    X_train, depths_train, _ = load_features_csv(TRAINING_FEATURES, has_depth=True)
    log.info(f"Training data: {X_train.shape[0]} rows, depths 0-{depths_train.max()}")
    for d in range(int(depths_train.max()) + 1):
        log.info(f"  depth {d}: {(depths_train == d).sum()} rows")

    log.info(f"Loading CC features from {cc_feat_path} ...")
    X_cc, cc_doc_ids = load_features_csv(cc_feat_path, has_depth=False)
    log.info(f"CC data: {X_cc.shape[0]} rows")

    K = int(depths_train.max())
    log.info(f"Training {K} binary classifiers P(Y>k) for k=0..{K-1} ...")
    binary_models = []
    for k in range(K):
        y_k = (depths_train > k).astype(int)
        clf = lgb.LGBMClassifier(
            n_estimators=300, max_depth=6, learning_rate=0.05,
            num_leaves=31, verbose=-1, n_jobs=-1, random_state=SEED,
        )
        clf.fit(X_train, y_k)
        train_acc = (clf.predict(X_train) == y_k).mean()
        log.info(f"  P(Y>{k}): train_acc={train_acc:.4f}, pos_rate={y_k.mean():.4f}")
        binary_models.append(clf)

    log.info("Predicting on CC data ...")
    exceedance_probs = np.zeros((len(cc_doc_ids), K))
    for k, clf in enumerate(binary_models):
        exceedance_probs[:, k] = clf.predict_proba(X_cc)[:, 1]

    depth_probs = np.zeros((len(cc_doc_ids), K + 1))
    depth_probs[:, 0] = 1.0 - exceedance_probs[:, 0]
    for k in range(1, K):
        depth_probs[:, k] = exceedance_probs[:, k - 1] - exceedance_probs[:, k]
    depth_probs[:, K] = exceedance_probs[:, K - 1]
    depth_probs = np.clip(depth_probs, 0, 1)
    row_sums = depth_probs.sum(axis=1, keepdims=True)
    depth_probs = depth_probs / np.maximum(row_sums, 1e-8)

    predicted_depth = depth_probs.argmax(axis=1)
    expected_depth = np.sum(depth_probs * np.arange(K + 1), axis=1)

    log.info("Predicted depth distribution on CC:")
    for d in range(K + 1):
        n = (predicted_depth == d).sum()
        log.info(f"  depth {d}: {n} ({n/len(predicted_depth)*100:.1f}%)")

    with open(pred_path, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["doc_id", "predicted_depth", "expected_depth"] + \
                 [f"depth_{d}_prob" for d in range(K + 1)]
        writer.writerow(header)
        for i in range(len(cc_doc_ids)):
            row = [
                int(cc_doc_ids[i]),
                int(predicted_depth[i]),
                round(float(expected_depth[i]), 6),
            ] + [round(float(depth_probs[i, d]), 6) for d in range(K + 1)]
            writer.writerow(row)
    log.info(f"Predictions saved to {pred_path}")

    return pred_path


# ═══════════════════════════════════════════════════════════════════════
# Phase 4: Independent Quality Metrics
# ═══════════════════════════════════════════════════════════════════════

def compute_gpt2_ppl(texts, batch_size=8):
    """GPT-2 Large perplexity (per-token cross-entropy, then exp)."""
    from transformers import GPT2LMHeadModel, GPT2TokenizerFast

    log.info("Loading GPT-2 Large ...")
    tok = GPT2TokenizerFast.from_pretrained("gpt2-large", cache_dir=HF_CACHE)
    tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = GPT2LMHeadModel.from_pretrained(
        "gpt2-large", cache_dir=HF_CACHE,
        torch_dtype=torch.float16,
    ).to(DEVICE).eval()

    ppls = []
    for start in tqdm(range(0, len(texts), batch_size), desc="GPT2-PPL"):
        batch = texts[start : start + batch_size]
        inputs = tok(
            batch, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(DEVICE)

        with torch.no_grad():
            outputs = model(**inputs, labels=inputs["input_ids"])
            logits = outputs.logits

        for i in range(len(batch)):
            mask = inputs["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                ppls.append(float("nan"))
                continue
            offset = inputs["input_ids"].shape[1] - seq_len
            shift_logits = logits[i, offset:-1, :]
            shift_labels = inputs["input_ids"][i, offset + 1:]
            loss_fn = torch.nn.CrossEntropyLoss(reduction="mean")
            loss = loss_fn(shift_logits[:seq_len - 1], shift_labels[:seq_len - 1])
            ppls.append(float(torch.exp(loss).cpu()))

        torch.cuda.empty_cache()

    del model, tok
    torch.cuda.empty_cache()
    gc.collect()
    log.info("GPT-2 Large unloaded")

    return np.array(ppls)


def compute_lexical_diversity_metrics(texts):
    """MTLD and HD-D via lexical_diversity library."""
    from lexical_diversity import lex_div as ld

    mtld_vals = []
    hdd_vals = []
    for text in tqdm(texts, desc="LexDiv"):
        tokens = ld.flemmatize(text)
        if len(tokens) < 10:
            mtld_vals.append(float("nan"))
            hdd_vals.append(float("nan"))
            continue
        try:
            mtld_vals.append(float(ld.mtld(tokens)))
        except Exception:
            mtld_vals.append(float("nan"))
        try:
            hdd_vals.append(float(ld.hdd(tokens)))
        except Exception:
            hdd_vals.append(float("nan"))

    return np.array(mtld_vals), np.array(hdd_vals)


def compute_ngram_repetition(texts, n):
    """n-gram repetition rate: fraction of n-grams that appear more than once."""
    rates = []
    for text in texts:
        tokens = text.split()
        if len(tokens) < n + 1:
            rates.append(0.0)
            continue
        grams = ngrams(tokens, n)
        freq = Counter(grams)
        repeated = sum(c - 1 for c in freq.values() if c > 1)
        rates.append(repeated / max(len(grams), 1))
    return np.array(rates)


def compute_zipf_coefficient(texts):
    """Zipf coefficient: slope of log-log rank-frequency plot."""
    coeffs = []
    for text in texts:
        tokens = text.split()
        if len(tokens) < 5:
            coeffs.append(float("nan"))
            continue
        freq = Counter(tokens)
        counts = sorted(freq.values(), reverse=True)
        ranks = np.arange(1, len(counts) + 1, dtype=float)
        counts_arr = np.array(counts, dtype=float)
        log_ranks = np.log(ranks)
        log_counts = np.log(counts_arr)
        if len(log_ranks) < 3:
            coeffs.append(float("nan"))
            continue
        slope, _, _, _, _ = stats.linregress(log_ranks, log_counts)
        coeffs.append(float(-slope))
    return np.array(coeffs)


def compute_ttr_hapax_independent(texts):
    """TTR and hapax ratio computed independently (not from OBD features)."""
    ttr_vals = []
    hapax_vals = []
    for text in texts:
        tokens = text.split()
        if len(tokens) == 0:
            ttr_vals.append(0.0)
            hapax_vals.append(0.0)
            continue
        unique = set(tokens)
        ttr_vals.append(len(unique) / len(tokens))
        freq = Counter(tokens)
        hapax = sum(1 for v in freq.values() if v == 1)
        hapax_vals.append(hapax / max(len(unique), 1))
    return np.array(ttr_vals), np.array(hapax_vals)


def compute_mauve_by_depth(texts, predicted_depths, max_per_group=5000):
    """MAUVE score per depth bin vs depth-0 group."""
    try:
        import mauve
    except ImportError:
        log.warning("mauve-text not available, skipping MAUVE computation")
        return {}

    depth0_mask = predicted_depths == 0
    depth0_texts = [texts[i] for i in range(len(texts)) if depth0_mask[i]]
    if len(depth0_texts) > max_per_group:
        rng = np.random.RandomState(SEED)
        idx = rng.choice(len(depth0_texts), max_per_group, replace=False)
        depth0_texts = [depth0_texts[i] for i in idx]

    if len(depth0_texts) < 100:
        log.warning(f"Only {len(depth0_texts)} depth-0 texts, skipping MAUVE")
        return {}

    mauve_scores = {}
    unique_depths = sorted(set(predicted_depths))
    for d in unique_depths:
        if d == 0:
            continue
        d_mask = predicted_depths == d
        d_texts = [texts[i] for i in range(len(texts)) if d_mask[i]]
        if len(d_texts) < 100:
            log.info(f"  depth {d}: only {len(d_texts)} texts, skipping MAUVE")
            continue
        if len(d_texts) > max_per_group:
            rng = np.random.RandomState(SEED + d)
            idx = rng.choice(len(d_texts), max_per_group, replace=False)
            d_texts = [d_texts[i] for i in idx]

        log.info(f"  Computing MAUVE for depth {d} ({len(d_texts)} texts) vs depth 0 ({len(depth0_texts)} texts) ...")
        try:
            result = mauve.compute_mauve(
                p_text=depth0_texts,
                q_text=d_texts,
                device_id=int(DEVICE.split(":")[-1]),
                max_text_length=256,
                verbose=False,
                seed=SEED,
            )
            mauve_scores[str(d)] = round(float(result.mauve), 6)
            log.info(f"    MAUVE(depth {d} vs depth 0) = {result.mauve:.4f}")
        except Exception as e:
            log.warning(f"    MAUVE failed for depth {d}: {e}")
            mauve_scores[str(d)] = None

    return mauve_scores


def phase4_quality_metrics(texts, predicted_depths):
    log.info(f"{'='*60}")
    log.info(f"Phase 4: Independent Quality Metrics  [{timestamp()}]")
    log.info(f"{'='*60}")

    metrics_path = DATA_DIR / "cc_quality_metrics.csv"
    mauve_path = OUT_DIR / "mauve_scores.json"

    if metrics_path.exists():
        n_existing = sum(1 for _ in open(metrics_path)) - 1
        if n_existing >= len(texts) * 0.9:
            log.info(f"cc_quality_metrics.csv already exists ({n_existing} rows) — loading")
            metrics = {}
            with open(metrics_path) as f:
                reader = csv.DictReader(f)
                for col in ALL_METRICS:
                    metrics[col] = []
                for row in reader:
                    for col in ALL_METRICS:
                        v = row.get(col, "nan")
                        metrics[col].append(float(v) if v not in ("", "nan") else float("nan"))
            metrics = {k: np.array(v) for k, v in metrics.items()}
            mauve_scores = {}
            if mauve_path.exists():
                with open(mauve_path) as f:
                    mauve_scores = json.load(f)
            return metrics, mauve_scores

    metrics = {}

    # GPU metrics
    log.info("Computing GPT-2 Large perplexity ...")
    t0 = time.time()
    metrics["gpt2_ppl"] = compute_gpt2_ppl(texts, batch_size=BATCH_SIZE)
    log.info(f"  GPT-2 PPL done in {time.time()-t0:.0f}s, median={np.nanmedian(metrics['gpt2_ppl']):.1f}")

    # MAUVE
    log.info("Computing MAUVE by depth bin ...")
    t0 = time.time()
    mauve_scores = compute_mauve_by_depth(texts, predicted_depths)
    log.info(f"  MAUVE done in {time.time()-t0:.0f}s")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(mauve_path, "w") as f:
        json.dump(mauve_scores, f, indent=2)

    # Per-doc MAUVE placeholder (MAUVE is a group metric, assign group score to each doc)
    mauve_per_doc = np.full(len(texts), float("nan"))
    for d_str, score in mauve_scores.items():
        if score is not None:
            d = int(d_str)
            mask = predicted_depths == d
            mauve_per_doc[mask] = score
    depth0_mask = predicted_depths == 0
    mauve_per_doc[depth0_mask] = 1.0  # depth-0 vs itself = 1.0
    metrics["mauve_score"] = mauve_per_doc

    # CPU metrics
    log.info("Computing lexical diversity (MTLD, HD-D) ...")
    t0 = time.time()
    metrics["mtld"], metrics["hdd"] = compute_lexical_diversity_metrics(texts)
    log.info(f"  LexDiv done in {time.time()-t0:.0f}s")

    log.info("Computing n-gram repetition rates ...")
    metrics["trigram_rep"] = compute_ngram_repetition(texts, 3)
    metrics["quadgram_rep"] = compute_ngram_repetition(texts, 4)

    log.info("Computing Zipf coefficient ...")
    metrics["zipf_coeff"] = compute_zipf_coefficient(texts)

    log.info("Computing independent TTR and hapax ratio ...")
    metrics["ttr_indep"], metrics["hapax_indep"] = compute_ttr_hapax_independent(texts)

    # Save
    with open(metrics_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["doc_id"] + ALL_METRICS)
        for i in range(len(texts)):
            row = [i] + [
                round(float(metrics[m][i]), 8)
                if not np.isnan(metrics[m][i]) else ""
                for m in ALL_METRICS
            ]
            writer.writerow(row)
    log.info(f"Quality metrics saved to {metrics_path}")

    return metrics, mauve_scores


# ═══════════════════════════════════════════════════════════════════════
# Phase 5: Analysis + Visualization
# ═══════════════════════════════════════════════════════════════════════

def cliffs_delta(x, y):
    """Cliff's delta effect size."""
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return 0.0
    more = 0
    less = 0
    for xi in x:
        for yj in y:
            if xi > yj:
                more += 1
            elif xi < yj:
                less += 1
    return (more - less) / (n1 * n2)


def cliffs_delta_fast(x, y):
    """Cliff's delta using vectorized approach for large arrays."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) == 0 or len(y) == 0:
        return 0.0
    if len(x) * len(y) > 5_000_000:
        rng = np.random.RandomState(SEED)
        if len(x) > 2000:
            x = rng.choice(x, 2000, replace=False)
        if len(y) > 2000:
            y = rng.choice(y, 2000, replace=False)
    more = np.sum(x[:, None] > y[None, :])
    less = np.sum(x[:, None] < y[None, :])
    return float(more - less) / (len(x) * len(y))


def phase5_analysis(texts, predicted_depths, expected_depths, metrics, mauve_scores):
    log.info(f"{'='*60}")
    log.info(f"Phase 5: Analysis + Visualization  [{timestamp()}]")
    log.info(f"{'='*60}")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    # ── 5.1 Correlation analysis ──
    log.info("5.1 Correlation analysis (Spearman ρ + Kendall τ, Bonferroni corrected) ...")
    n_tests = len(ALL_METRICS)
    alpha = 0.05 / n_tests

    corr_results = {}
    for m in ALL_METRICS:
        vals = metrics[m]
        valid = ~np.isnan(vals) & ~np.isnan(expected_depths)
        if valid.sum() < 30:
            log.info(f"  {m}: too few valid samples ({valid.sum()})")
            continue

        rho, p_rho = stats.spearmanr(expected_depths[valid], vals[valid])
        tau, p_tau = stats.kendalltau(expected_depths[valid], vals[valid])

        corr_results[m] = {
            "spearman_rho": round(float(rho), 4),
            "spearman_p": float(p_rho),
            "spearman_sig": p_rho < alpha,
            "kendall_tau": round(float(tau), 4),
            "kendall_p": float(p_tau),
            "kendall_sig": p_tau < alpha,
            "n_valid": int(valid.sum()),
        }
        sig_marker = "***" if p_rho < alpha else ""
        log.info(f"  {m}: ρ={rho:.4f} (p={p_rho:.2e}{sig_marker}), τ={tau:.4f} (p={p_tau:.2e})")

    results["correlations"] = corr_results

    # ── 5.2 Stratified analysis ──
    log.info("5.2 Stratified analysis by predicted depth bin ...")
    depth_bins = {0: "0", 1: "1", 2: "2"}
    high_mask = predicted_depths >= 3
    stratified = {}

    for bin_label in ["0", "1", "2", "3+"]:
        if bin_label == "3+":
            mask = predicted_depths >= 3
        else:
            mask = predicted_depths == int(bin_label)
        n = mask.sum()
        if n == 0:
            continue
        bin_stats = {"count": int(n)}
        for m in ALL_METRICS:
            vals = metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) == 0:
                continue
            bin_stats[m] = {
                "mean": round(float(np.mean(valid)), 6),
                "median": round(float(np.median(valid)), 6),
                "std": round(float(np.std(valid)), 6),
            }
        stratified[bin_label] = bin_stats
        log.info(f"  depth {bin_label} (n={n})")

    results["stratified"] = stratified

    # ── 5.3 Statistical tests ──
    log.info("5.3 Statistical tests (Kruskal-Wallis, Mann-Whitney U, Cliff's delta) ...")
    stat_tests = {}
    groups_by_metric = {}
    bin_labels = ["0", "1", "2", "3+"]

    for m in ALL_METRICS:
        groups = []
        used_labels = []
        for bl in bin_labels:
            if bl == "3+":
                mask = predicted_depths >= 3
            else:
                mask = predicted_depths == int(bl)
            vals = metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) >= 5:
                groups.append(valid)
                used_labels.append(bl)

        if len(groups) < 2:
            continue

        groups_by_metric[m] = (groups, used_labels)

        kw_stat, kw_p = stats.kruskal(*groups)

        pairwise = {}
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                pair_key = f"{used_labels[i]}_vs_{used_labels[j]}"
                u_stat, u_p = stats.mannwhitneyu(groups[i], groups[j], alternative="two-sided")
                cd = cliffs_delta_fast(groups[i], groups[j])
                pairwise[pair_key] = {
                    "mann_whitney_U": float(u_stat),
                    "p_value": float(u_p),
                    "cliffs_delta": round(float(cd), 4),
                    "effect_size": (
                        "large" if abs(cd) >= 0.474 else
                        "medium" if abs(cd) >= 0.33 else
                        "small" if abs(cd) >= 0.147 else
                        "negligible"
                    ),
                }

        stat_tests[m] = {
            "kruskal_wallis": {"statistic": round(float(kw_stat), 4), "p_value": float(kw_p)},
            "pairwise": pairwise,
        }
        log.info(f"  {m}: KW H={kw_stat:.2f}, p={kw_p:.2e}")

    results["statistical_tests"] = stat_tests

    # ── 5.4 Bootstrap CI for Spearman ρ ──
    log.info("5.4 Bootstrap CI for Spearman ρ (1000 resamples) ...")
    rng = np.random.RandomState(SEED)
    n_bootstrap = 1000
    bootstrap_results = {}

    for m in ALL_METRICS:
        vals = metrics[m]
        valid = ~np.isnan(vals) & ~np.isnan(expected_depths)
        if valid.sum() < 30:
            continue

        ed_valid = expected_depths[valid]
        m_valid = vals[valid]
        n_valid = len(ed_valid)

        boot_rhos = []
        for _ in range(n_bootstrap):
            idx = rng.randint(0, n_valid, n_valid)
            rho_b, _ = stats.spearmanr(ed_valid[idx], m_valid[idx])
            if not np.isnan(rho_b):
                boot_rhos.append(rho_b)

        if len(boot_rhos) < 100:
            continue

        boot_rhos = np.array(boot_rhos)
        ci_low = float(np.percentile(boot_rhos, 2.5))
        ci_high = float(np.percentile(boot_rhos, 97.5))
        bootstrap_results[m] = {
            "rho_mean": round(float(boot_rhos.mean()), 4),
            "ci_95_low": round(ci_low, 4),
            "ci_95_high": round(ci_high, 4),
            "ci_width": round(ci_high - ci_low, 4),
        }
        log.info(f"  {m}: ρ={boot_rhos.mean():.4f} [{ci_low:.4f}, {ci_high:.4f}]")

    results["bootstrap_ci"] = bootstrap_results

    # ── 5.5 Length-controlled analysis ──
    log.info("5.5 Length-controlled analysis (by text length quartile) ...")
    lengths = np.array([len(t.split()) for t in texts])
    quartiles = np.percentile(lengths, [25, 50, 75])
    q_labels = [
        f"Q1(≤{int(quartiles[0])})",
        f"Q2({int(quartiles[0]+1)}-{int(quartiles[1])})",
        f"Q3({int(quartiles[1]+1)}-{int(quartiles[2])})",
        f"Q4(>{int(quartiles[2])})",
    ]
    q_masks = [
        lengths <= quartiles[0],
        (lengths > quartiles[0]) & (lengths <= quartiles[1]),
        (lengths > quartiles[1]) & (lengths <= quartiles[2]),
        lengths > quartiles[2],
    ]

    length_controlled = {}
    for qi, (ql, qm) in enumerate(zip(q_labels, q_masks)):
        n_q = qm.sum()
        if n_q < 30:
            continue
        q_results = {"n": int(n_q), "length_range": ql}
        for m in ALL_METRICS:
            vals = metrics[m][qm]
            ed = expected_depths[qm]
            valid = ~np.isnan(vals) & ~np.isnan(ed)
            if valid.sum() < 20:
                continue
            rho, p = stats.spearmanr(ed[valid], vals[valid])
            q_results[m] = {"spearman_rho": round(float(rho), 4), "p_value": float(p)}
        length_controlled[ql] = q_results
        log.info(f"  {ql} (n={n_q})")

    results["length_controlled"] = length_controlled

    # ── 5.6 Visualizations ──
    log.info("5.6 Generating visualizations ...")

    # Depth distribution histogram
    fig, ax = plt.subplots(figsize=(8, 5))
    max_d = int(predicted_depths.max())
    bins_edges = np.arange(-0.5, max_d + 1.5, 1)
    ax.hist(predicted_depths, bins=bins_edges, edgecolor="black", alpha=0.7, color="#4C72B0")
    ax.set_xlabel("Predicted Depth", fontsize=13)
    ax.set_ylabel("Count", fontsize=13)
    ax.set_title("Distribution of Predicted Depth on FineWeb CC Data", fontsize=14)
    ax.set_xticks(range(max_d + 1))
    for d in range(max_d + 1):
        n = (predicted_depths == d).sum()
        ax.text(d, n + len(texts) * 0.005, str(n), ha="center", fontsize=10)
    plt.tight_layout()
    fig.savefig(OUT_DIR / "depth_distribution.pdf", dpi=150)
    fig.savefig(OUT_DIR / "depth_distribution.png", dpi=150)
    plt.close(fig)
    log.info("  Saved depth_distribution.pdf/png")

    # Violin plot: 3x3 grid of quality metrics by depth bin
    plot_metrics = [m for m in ALL_METRICS if m != "mauve_score"]
    n_plot = min(len(plot_metrics), 9)
    nrows = 3
    ncols = 3
    fig, axes = plt.subplots(nrows, ncols, figsize=(15, 12))
    axes_flat = axes.flatten()

    for idx in range(n_plot):
        m = plot_metrics[idx]
        ax = axes_flat[idx]
        data_for_violin = []
        labels = []
        for bl in bin_labels:
            if bl == "3+":
                mask = predicted_depths >= 3
            else:
                mask = predicted_depths == int(bl)
            vals = metrics[m][mask]
            valid = vals[~np.isnan(vals)]
            if len(valid) > 0:
                if len(valid) > 5000:
                    rng_v = np.random.RandomState(SEED)
                    valid = rng_v.choice(valid, 5000, replace=False)
                data_for_violin.append(valid)
                labels.append(bl)

        if len(data_for_violin) >= 2:
            parts = ax.violinplot(data_for_violin, showmeans=True, showmedians=True)
            ax.set_xticks(range(1, len(labels) + 1))
            ax.set_xticklabels([f"d={l}" for l in labels])
            for pc in parts.get("bodies", []):
                pc.set_alpha(0.6)
        ax.set_title(m, fontsize=11)
        ax.set_xlabel("Predicted Depth")

    for idx in range(n_plot, len(axes_flat)):
        axes_flat[idx].set_visible(False)

    fig.suptitle("Quality Metrics by Predicted Depth Bin", fontsize=14, y=1.01)
    plt.tight_layout()
    fig.savefig(OUT_DIR / "violin_quality_metrics.pdf", dpi=150, bbox_inches="tight")
    fig.savefig(OUT_DIR / "violin_quality_metrics.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info("  Saved violin_quality_metrics.pdf/png")

    # MAUVE by depth bin bar chart
    if mauve_scores:
        fig, ax = plt.subplots(figsize=(8, 5))
        depth_keys = sorted(mauve_scores.keys(), key=int)
        x_labels = [f"d={k}" for k in depth_keys]
        y_vals = [mauve_scores[k] if mauve_scores[k] is not None else 0.0 for k in depth_keys]
        bars = ax.bar(range(len(depth_keys)), y_vals, color="#4C72B0", edgecolor="black", alpha=0.8)
        ax.set_xticks(range(len(depth_keys)))
        ax.set_xticklabels(x_labels)
        ax.set_xlabel("Predicted Depth Bin", fontsize=13)
        ax.set_ylabel("MAUVE Score", fontsize=13)
        ax.set_title("MAUVE Score by Predicted Depth (vs. Depth-0 Reference)", fontsize=14)
        ax.set_ylim(0, 1.05)
        for bar, val in zip(bars, y_vals):
            if val > 0:
                ax.text(bar.get_x() + bar.get_width() / 2, val + 0.01,
                        f"{val:.3f}", ha="center", fontsize=10)
        plt.tight_layout()
        fig.savefig(OUT_DIR / "mauve_by_depth.pdf", dpi=150)
        fig.savefig(OUT_DIR / "mauve_by_depth.png", dpi=150)
        plt.close(fig)
        log.info("  Saved mauve_by_depth.pdf/png")

    # ── 5.7 Summary ──
    results["mauve_scores"] = mauve_scores
    results["depth_distribution"] = {
        str(d): int((predicted_depths == d).sum())
        for d in range(int(predicted_depths.max()) + 1)
    }
    results["num_samples"] = len(texts)
    results["experiment"] = "exp_014_naturalistic_v2"

    result_path = OUT_DIR / "analysis_results.json"
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log.info(f"Analysis results saved to {result_path}")

    return results


# ═══════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════

def main():
    t_total = time.time()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    os.environ["HF_HOME"] = HF_CACHE
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ.setdefault("REQUESTS_CA_BUNDLE", "/etc/ssl/certs/ca-certificates.crt")
    os.environ.setdefault("SSL_CERT_FILE", "/etc/ssl/certs/ca-certificates.crt")

    log.info(f"exp-014 v2 Naturalistic Validation — start [{timestamp()}]")
    log.info(f"Device: {DEVICE}, NUM_CC_SAMPLES: {NUM_CC_SAMPLES}")

    # ── Load scorer model (needed for Phase 1 tokenizer + Phase 2 features) ──
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info("Loading Qwen tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(
        SCORER_MODEL, cache_dir=HF_CACHE, trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    # ── Phase 1: Data Sampling ──
    t0 = time.time()
    records = phase1_sample_data(tokenizer)
    texts = [r["text"] for r in records]
    log.info(f"Phase 1 done in {time.time()-t0:.0f}s — {len(texts)} texts")

    cc_sample_path = DATA_DIR / "cc_sample.jsonl"
    if not cc_sample_path.exists() or cc_sample_path.stat().st_size == 0:
        raise RuntimeError(f"Phase 1 output missing or empty: {cc_sample_path}")

    # ── Phase 2: Feature Extraction (needs GPU model) ──
    t0 = time.time()
    log.info(f"Loading scorer model {SCORER_MODEL} on {DEVICE} ...")
    model = AutoModelForCausalLM.from_pretrained(
        SCORER_MODEL,
        cache_dir=HF_CACHE,
        torch_dtype=torch.float16,
        device_map={"": DEVICE},
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Model loaded on {model.device}")

    feat_path = phase2_extract_features(model, tokenizer, texts)
    log.info(f"Phase 2 done in {time.time()-t0:.0f}s")

    if not Path(feat_path).exists() or Path(feat_path).stat().st_size == 0:
        raise RuntimeError(f"Phase 2 output missing or empty: {feat_path}")

    del model
    torch.cuda.empty_cache()
    gc.collect()
    log.info("Scorer model unloaded")

    # ── Phase 3: OBD Depth Prediction ──
    t0 = time.time()
    pred_path = phase3_obd_prediction(feat_path)
    log.info(f"Phase 3 done in {time.time()-t0:.0f}s")

    if not Path(pred_path).exists() or Path(pred_path).stat().st_size == 0:
        raise RuntimeError(f"Phase 3 output missing or empty: {pred_path}")

    # Load predictions
    with open(pred_path) as f:
        pred_rows = list(csv.DictReader(f))
    predicted_depths = np.array([int(r["predicted_depth"]) for r in pred_rows])
    expected_depths = np.array([float(r["expected_depth"]) for r in pred_rows])

    # ── Phase 4: Quality Metrics ──
    t0 = time.time()
    metrics, mauve_scores = phase4_quality_metrics(texts, predicted_depths)
    log.info(f"Phase 4 done in {time.time()-t0:.0f}s")

    # ── Phase 5: Analysis + Visualization ──
    t0 = time.time()
    results = phase5_analysis(texts, predicted_depths, expected_depths, metrics, mauve_scores)
    log.info(f"Phase 5 done in {time.time()-t0:.0f}s")

    total = time.time() - t_total
    log.info(f"{'='*60}")
    log.info(f"exp-014 v2 complete in {total:.0f}s ({total/3600:.1f}h)  [{timestamp()}]")
    log.info(f"Depth distribution: { {str(d): int((predicted_depths==d).sum()) for d in range(int(predicted_depths.max())+1)} }")
    log.info(f"Key correlations:")
    for m in ALL_METRICS:
        if m in results.get("correlations", {}):
            r = results["correlations"][m]
            log.info(f"  {m}: ρ={r['spearman_rho']:.4f} (p={r['spearman_p']:.2e})")
    log.info(f"{'='*60}")


if __name__ == "__main__":
    main()
