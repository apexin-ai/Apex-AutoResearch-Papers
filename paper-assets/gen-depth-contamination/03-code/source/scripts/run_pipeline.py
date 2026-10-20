"""
MVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)

Generates recursive depth chains from C4 seed data using Qwen2.5-1.5B,
extracts statistical features, and runs distinguishability analysis.

Input:  C4 validation split (streamed from HuggingFace)
Output: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt

Key deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
"""

import argparse
import json
import logging
import math
import os
import sys
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


# ---------------------------------------------------------------------------
# Utility: simple 4-gram BLEU (no nltk dependency)
# ---------------------------------------------------------------------------

def ngrams(tokens, n):
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
    """Compute sentence-level BLEU up to max_n grams with brevity penalty."""
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


# ===================================================================
# Step 2: Seed data preparation
# ===================================================================

def prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):
    """Download C4 validation, truncate to max_tokens, save as depth_0.jsonl."""
    out_path = data_dir / "depth_0.jsonl"
    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:
        log.info("depth_0.jsonl already exists with enough samples — skipping")
        return

    from datasets import load_dataset

    # Use a single validation shard to avoid slow full-tree listing on proxied networks
    hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
    C4_SHARD_URL = f"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz"
    log.info("Loading C4 validation shard (streaming) ...")
    try:
        ds = load_dataset("json", data_files=C4_SHARD_URL, split="train", streaming=True)
    except Exception as e:
        log.warning(f"Direct shard download failed ({e}), falling back to full dataset listing")
        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)

    records = []
    for i, example in enumerate(tqdm(ds, total=num_samples, desc="Sampling C4")):
        if i >= num_samples:
            break
        text = example["text"].strip()
        if not text:
            continue
        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
        truncated = tokenizer.decode(ids, skip_special_tokens=True)
        records.append({"text": truncated, "doc_id": len(records)})
        if len(records) >= num_samples:
            break

    data_dir.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    log.info(f"Saved {len(records)} seed documents to {out_path}")


# ===================================================================
# Step 3: Recursive depth chain generation
# ===================================================================

REWRITE_PROMPT = (
    "Below is a passage. Write a new passage of similar length on the same "
    "topic and in the same style.\n\n"
    "Original passage:\n{prev_text}\n\nNew passage:\n"
)


def load_jsonl(path: Path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def generate_depth_chain(
    model,
    tokenizer,
    data_dir: Path,
    max_depth: int,
    batch_size: int,
    max_new_tokens: int = 256,
    top_p: float = 0.95,
    temperature: float = 1.0,
    do_sample: bool = True,
    generation_mode: str = "rewrite",
):
    """Generate depths 1..max_depth via prompt-chain rewriting."""
    for depth in range(1, max_depth + 1):
        out_path = data_dir / f"depth_{depth}.jsonl"
        prev_path = data_dir / f"depth_{depth - 1}.jsonl"

        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):
            log.info(f"depth_{depth}.jsonl already complete — skipping")
            continue

        prev_records = load_jsonl(prev_path)
        log.info(f"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...")

        results = []
        for start in tqdm(range(0, len(prev_records), batch_size), desc=f"depth {depth}"):
            batch = prev_records[start : start + batch_size]

            if generation_mode == "rewrite":
                prompts = [REWRITE_PROMPT.format(prev_text=r["text"]) for r in batch]

                inputs = tokenizer(
                    prompts,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=512,
                ).to(model.device)

                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=max_new_tokens,
                        do_sample=do_sample,
                        top_p=top_p,
                        temperature=temperature,
                        pad_token_id=tokenizer.pad_token_id,
                    )

                for j, out_ids in enumerate(outputs):
                    prompt_len = inputs["input_ids"].shape[1]
                    generated_ids = out_ids[prompt_len:]
                    text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
                    results.append({"text": text, "doc_id": batch[j]["doc_id"]})

            else:  # continuation: batch generation with left-padding
                prefix_texts = []
                prefix_lengths = []
                for rec in batch:
                    full_ids = tokenizer.encode(rec["text"], add_special_tokens=False)
                    prefix_len = max(1, len(full_ids) // 2)
                    prefix_texts.append(tokenizer.decode(full_ids[:prefix_len], skip_special_tokens=True))
                    prefix_lengths.append(prefix_len)

                inputs = tokenizer(
                    prefix_texts,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=256,
                ).to(model.device)

                with torch.no_grad():
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=max_new_tokens,
                        do_sample=do_sample,
                        top_p=top_p,
                        temperature=temperature,
                        pad_token_id=tokenizer.pad_token_id,
                    )

                for j, out_ids in enumerate(outputs):
                    prompt_len = inputs["input_ids"].shape[1]
                    generated_ids = out_ids[prompt_len:]
                    text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
                    results.append({"text": text, "doc_id": batch[j]["doc_id"]})

            torch.cuda.empty_cache()

        with open(out_path, "w") as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log.info(f"Saved {len(results)} docs to {out_path}")


# ===================================================================
# Step 4: Feature extraction
# ===================================================================

def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
    """Compute 9-dim surprisal statistics per text using batched inference."""
    all_features = []
    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
        batch_texts = texts[start : start + batch_size]
        valid_mask = [bool(t.strip()) for t in batch_texts]
        valid_texts = [t for t, m in zip(batch_texts, valid_mask) if m]
        if not valid_texts:
            all_features.extend([[0.0] * 9] * len(batch_texts))
            continue
        inputs = tokenizer(
            valid_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512,
        ).to(model.device)

        with torch.no_grad():
            logits = model(**inputs).logits  # (B, T, V)

        log_probs = torch.log_softmax(logits, dim=-1)  # (B, T, V)
        input_ids = inputs["input_ids"]  # (B, T)

        valid_feats = []
        for i in range(len(valid_texts)):
            mask = inputs["attention_mask"][i].bool()
            seq_len = mask.sum().item()
            if seq_len < 3:
                valid_feats.append([0.0] * 9)
                continue

            offset = input_ids.shape[1] - seq_len
            token_ids = input_ids[i, offset:]
            token_log_probs = []
            for t in range(1, seq_len):
                lp = log_probs[i, offset + t - 1, token_ids[t]].item()
                token_log_probs.append(-lp)

            arr = np.array(token_log_probs)
            if len(arr) < 3:
                valid_feats.append([0.0] * 9)
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
            valid_feats.append(feats)

        vi = 0
        for m in valid_mask:
            if m:
                all_features.append(valid_feats[vi])
                vi += 1
            else:
                all_features.append([0.0] * 9)

        torch.cuda.empty_cache()

    return all_features


def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):
    """Compute 3-dim vocabulary diversity features: TTR, hapax ratio, self-BLEU."""
    features = []
    # tokenize all texts at word level (split on whitespace for simplicity)
    tokenized = [t.split() for t in texts]

    # pre-select indices for self-BLEU (sample up to sample_bleu texts)
    bleu_indices = list(range(len(texts)))
    if len(bleu_indices) > sample_bleu:
        rng = np.random.RandomState(42 + depth)
        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()
    bleu_set = set(bleu_indices)

    # pre-tokenize for BLEU refs
    same_depth_tokens = tokenized  # all texts from this depth

    for idx, tokens in enumerate(tqdm(tokenized, desc=f"VocabDiv d={depth}", leave=False)):
        total = len(tokens)
        if total == 0:
            features.append([0.0, 0.0, 0.0])
            continue

        unique = set(tokens)
        ttr = len(unique) / total

        freq = Counter(tokens)
        hapax = sum(1 for v in freq.values() if v == 1)
        hapax_ratio = hapax / max(len(unique), 1)

        # self-BLEU: compute for all samples (100 random refs each)
        rng_local = np.random.RandomState(idx)
        ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]
        if len(ref_pool) > bleu_refs:
            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
        bleu_scores = [
            simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool
        ]
        self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0

        features.append([ttr, hapax_ratio, self_bleu])

    return features


def compute_tail_features(texts):
    """Compute 3-dim tail-thinning features: freq kurtosis, freq entropy, low-freq ratio."""
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


SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS


def extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):
    """Extract features for all depths and save to features.csv."""
    import csv

    out_path = data_dir / "features.csv"
    expected_total = 0
    for d in range(max_depth + 1):
        p = data_dir / f"depth_{d}.jsonl"
        if p.exists():
            expected_total += sum(1 for _ in open(p))

    if out_path.exists() and sum(1 for _ in open(out_path)) - 1 >= expected_total:
        log.info("features.csv already complete — skipping")
        return

    log.info("Extracting features for all depths ...")

    # group texts by depth for self-BLEU
    depth_texts = {}
    for d in range(max_depth + 1):
        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
        depth_texts[d] = records

    rows = []
    for d in range(max_depth + 1):
        records = depth_texts[d]
        texts = [r["text"] for r in records]
        doc_ids = [r["doc_id"] for r in records]
        log.info(f"  depth {d}: {len(texts)} texts")

        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=batch_size)
        vocab = compute_vocab_diversity(
            texts, tokenizer, depth_texts, d
        )
        tail = compute_tail_features(texts)

        for i in range(len(texts)):
            row = {"doc_id": doc_ids[i], "depth": d}
            for j, col in enumerate(SURPRISAL_COLS):
                row[col] = surp[i][j]
            for j, col in enumerate(VOCAB_COLS):
                row[col] = vocab[i][j]
            for j, col in enumerate(TAIL_COLS):
                row[col] = tail[i][j]
            rows.append(row)

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved {len(rows)} feature rows to {out_path}")


# ===================================================================
# Step 5: Distinguishability analysis
# ===================================================================

def run_analysis(data_dir: Path, results_dir: Path, max_depth: int):
    """Pairwise AUC, JSD, K*, ordinal classification, feature importance."""
    import csv

    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score

    results_dir.mkdir(parents=True, exist_ok=True)

    # load features
    feat_path = data_dir / "features.csv"
    log.info(f"Loading features from {feat_path} ...")
    with open(feat_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # build arrays
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    feat_matrix = np.array(
        [[float(r[c]) if r[c] != "" and r[c] != "nan" else np.nan for c in ALL_FEAT_COLS] for r in rows]
    )
    # fill NaN with column mean for classification
    col_means = np.nanmean(feat_matrix, axis=0)
    for j in range(feat_matrix.shape[1]):
        mask = np.isnan(feat_matrix[:, j])
        feat_matrix[mask, j] = col_means[j]

    # --- Pairwise AUC ---
    log.info("Computing pairwise AUC ...")
    pairwise_auc = {}
    pairwise_auc_folds = {}
    for k in range(1, max_depth + 1):
        mask = (depths == k - 1) | (depths == k)
        X = feat_matrix[mask]
        y = (depths[mask] == k).astype(int)
        if len(np.unique(y)) < 2:
            pairwise_auc[f"{k-1}v{k}"] = float("nan")
            continue

        gkf = GroupKFold(n_splits=5)
        groups = doc_ids[mask]
        fold_aucs = []
        for train_idx, test_idx in gkf.split(X, y, groups=groups):
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(X[train_idx], y[train_idx])
            proba = clf.predict_proba(X[test_idx])[:, 1]
            fold_aucs.append(roc_auc_score(y[test_idx], proba))
        auc_mean = float(np.mean(fold_aucs))
        auc_std = float(np.std(fold_aucs))
        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
        pairwise_auc_folds[f"{k-1}v{k}"] = [round(a, 4) for a in fold_aucs]
        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f} ± {auc_std:.4f}  folds={[round(a,4) for a in fold_aucs]}")

    with open(results_dir / "pairwise_auc.json", "w") as f:
        json.dump({"mean": pairwise_auc, "per_fold": pairwise_auc_folds}, f, indent=2)

    # --- JSD ---
    log.info("Computing pairwise JSD ...")
    pairwise_jsd = {}
    for k in range(1, max_depth + 1):
        mask_prev = depths == k - 1
        mask_curr = depths == k
        feat_prev = feat_matrix[mask_prev]
        feat_curr = feat_matrix[mask_curr]

        jsds_per_feat = []
        for j in range(feat_matrix.shape[1]):
            a = feat_prev[:, j]
            b = feat_curr[:, j]
            # histogram-based JSD
            lo = min(a.min(), b.min())
            hi = max(a.max(), b.max())
            if hi - lo < 1e-12:
                jsds_per_feat.append(0.0)
                continue
            bins = np.linspace(lo, hi, 51)
            p_hist = np.histogram(a, bins=bins, density=True)[0] + 1e-12
            q_hist = np.histogram(b, bins=bins, density=True)[0] + 1e-12
            p_hist /= p_hist.sum()
            q_hist /= q_hist.sum()
            m = 0.5 * (p_hist + q_hist)
            jsd = 0.5 * np.sum(p_hist * np.log2(p_hist / m)) + 0.5 * np.sum(q_hist * np.log2(q_hist / m))
            jsds_per_feat.append(float(jsd))

        jsd_mean = float(np.mean(jsds_per_feat))
        pairwise_jsd[f"{k-1}v{k}"] = round(jsd_mean, 6)
        log.info(f"  JSD({k-1} vs {k}) = {jsd_mean:.6f}")

    with open(results_dir / "jsd.json", "w") as f:
        json.dump(pairwise_jsd, f, indent=2)

    # --- K* ---
    k_star = 0
    for k in range(1, max_depth + 1):
        key = f"{k-1}v{k}"
        if pairwise_auc.get(key, 0) > 0.60:
            k_star = k

    # --- Ordinal classification ---
    log.info("Running ordinal LightGBM classification ...")
    gkf_ord = GroupKFold(n_splits=5)
    all_preds = np.zeros_like(depths, dtype=float)
    all_true = depths.copy()

    importances = np.zeros(len(ALL_FEAT_COLS))
    for train_idx, test_idx in gkf_ord.split(feat_matrix, depths, groups=doc_ids):
        clf = lgb.LGBMClassifier(
            n_estimators=300, max_depth=8, learning_rate=0.05,
            num_leaves=63, verbose=-1, n_jobs=-1,
            num_class=max_depth + 1,
            objective="multiclass",
        )
        clf.fit(feat_matrix[train_idx], depths[train_idx])
        preds = clf.predict(feat_matrix[test_idx])
        all_preds[test_idx] = preds
        importances += clf.feature_importances_

    importances /= 5.0
    mae = float(mean_absolute_error(all_true, all_preds))
    accuracy = float(accuracy_score(all_true, all_preds.astype(int)))
    log.info(f"  Ordinal MAE = {mae:.4f}, Accuracy = {accuracy:.4f}, K* = {k_star}")

    ordinal_results = {"mae": round(mae, 4), "accuracy": round(accuracy, 4), "k_star": k_star}
    with open(results_dir / "ordinal_results.json", "w") as f:
        json.dump(ordinal_results, f, indent=2)

    # --- Feature importance ---
    feat_imp = sorted(
        [{"feature": ALL_FEAT_COLS[i], "importance": float(importances[i])} for i in range(len(ALL_FEAT_COLS))],
        key=lambda x: x["importance"],
        reverse=True,
    )[:10]
    with open(results_dir / "feature_importance.json", "w") as f:
        json.dump(feat_imp, f, indent=2)

    # --- Summary ---
    summary_lines = [
        "=" * 60,
        "MVP Pilot Saturation Study — Results Summary",
        "=" * 60,
        "",
        "Pairwise AUC (adjacent depths):",
    ]
    for k in range(1, max_depth + 1):
        key = f"{k-1}v{k}"
        folds = pairwise_auc_folds.get(key, [])
        std = float(np.std(folds)) if folds else 0.0
        summary_lines.append(f"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')} ± {std:.4f}  folds={folds}")
    summary_lines += [
        "",
        "Pairwise JSD (adjacent depths):",
    ]
    for k in range(1, max_depth + 1):
        key = f"{k-1}v{k}"
        summary_lines.append(f"  depth {k-1} vs {k}: JSD = {pairwise_jsd.get(key, 'N/A')}")
    summary_lines += [
        "",
        f"K* (max depth with AUC > 0.60): {k_star}",
        "",
        f"Ordinal Classification (6-class, 5-fold CV):",
        f"  MAE = {mae:.4f}",
        f"  Accuracy = {accuracy:.4f}",
        "",
        "Top-10 Feature Importance:",
    ]
    for fi in feat_imp:
        summary_lines.append(f"  {fi['feature']:20s} {fi['importance']:.1f}")
    summary_lines.append("")
    summary_lines.append("=" * 60)

    summary_text = "\n".join(summary_lines)
    with open(results_dir / "summary.txt", "w") as f:
        f.write(summary_text)
    log.info(f"\n{summary_text}")


# ===================================================================
# Main
# ===================================================================

def main():
    parser = argparse.ArgumentParser(description="MVP Pilot Saturation Study Pipeline")
    parser.add_argument("--model_path", type=str,
                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/data")
    parser.add_argument("--results_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/results")
    parser.add_argument("--num_samples", type=int, default=5000)
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--feat_batch_size", type=int, default=8,
                        help="Batch size for surprisal feature extraction (uses more VRAM)")
    parser.add_argument("--top_p", type=float, default=0.95,
                        help="Nucleus sampling top-p (default: 0.95)")
    parser.add_argument("--temperature", type=float, default=1.0,
                        help="Sampling temperature (default: 1.0)")
    parser.add_argument("--do_sample", action="store_true", default=True,
                        help="Use sampling (default: True)")
    parser.add_argument("--no_sample", dest="do_sample", action="store_false",
                        help="Use greedy decoding")
    parser.add_argument("--generation_mode", type=str, default="rewrite",
                        choices=["rewrite", "continuation"],
                        help="Generation mode: 'rewrite' (instruct prompt) or 'continuation' (truncate+continue, for base models)")
    parser.add_argument("--skip_generation", action="store_true",
                        help="Skip seed data prep and depth chain generation (steps 2-3)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed for reproducibility (torch + numpy + random)")
    parser.add_argument("--dtype", type=str, default="fp16",
                        choices=["fp16", "bf16", "fp32"],
                        help="Model dtype: fp16 (default), bf16 (needed for Gemma-2), fp32")
    args = parser.parse_args()

    if args.seed is not None:
        import random
        torch.manual_seed(args.seed)
        np.random.seed(args.seed)
        random.seed(args.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(args.seed)
        log.info(f"Random seed set to {args.seed}")

    data_dir = Path(args.data_dir)
    results_dir = Path(args.results_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    log.info(f"Model: {args.model_path}")
    log.info(f"Data dir: {data_dir}")
    log.info(f"Samples: {args.num_samples}, Max depth: {args.max_depth}")
    log.info(f"Decoding: do_sample={args.do_sample}, top_p={args.top_p}, temperature={args.temperature}")
    log.info(f"Generation mode: {args.generation_mode}")
    log.info(f"Seed: {args.seed}")

    # Load model + tokenizer
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info("Loading tokenizer ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    dtype_map = {"fp16": torch.float16, "bf16": torch.bfloat16, "fp32": torch.float32}
    torch_dtype = dtype_map[args.dtype]
    log.info(f"Loading model (dtype={args.dtype}) ...")
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch_dtype,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Model loaded on {model.device}")

    if not args.skip_generation:
        # Step 2
        log.info("=" * 40 + " Step 2: Seed Data " + "=" * 40)
        prepare_seed_data(tokenizer, data_dir, args.num_samples)

        # Step 3
        log.info("=" * 40 + " Step 3: Depth Chain " + "=" * 40)
        generate_depth_chain(model, tokenizer, data_dir, args.max_depth, args.batch_size, top_p=args.top_p, temperature=args.temperature, do_sample=args.do_sample, generation_mode=args.generation_mode)
    else:
        log.info("Skipping generation (steps 2-3)")

    # Step 4
    log.info("=" * 40 + " Step 4: Feature Extraction " + "=" * 40)
    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)

    # Step 5
    log.info("=" * 40 + " Step 5: Analysis " + "=" * 40)
    run_analysis(data_dir, results_dir, args.max_depth)

    log.info("Pipeline complete.")


if __name__ == "__main__":
    main()
