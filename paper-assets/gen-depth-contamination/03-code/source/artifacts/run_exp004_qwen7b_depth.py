"""exp-004 Cross-scale validation: does K*=2 hold for Qwen2.5-7B base?

Runs the same depth-chain → feature extraction → OBD classification → pairwise AUC
pipeline as the 1.5B pilot (run_pipeline.py), but on the 7B model to test whether
the saturation boundary K*=2 is scale-invariant.

Input:  C4 validation split (streamed) or existing data/depth_0.jsonl
Output: data_exp004/depth_{0..K}.jsonl, data_exp004/features.csv,
        results_exp004/*.json + summary.txt

Key params:
  --n_docs        Number of documents (default 5000; use 10 for dry-run)
  --max_depth     Maximum depth (default 5)
  --batch_size    Generation batch size (default 1 for 7B memory safety)
  --quantize      Enable 4-bit quantization via bitsandbytes (preliminary only)
  --device        Target device (default cuda:0)

Dependencies: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
              Optional: bitsandbytes (for --quantize 4bit)
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
# Constants
# ---------------------------------------------------------------------------

REWRITE_PROMPT = (
    "Below is a passage. Write a new passage of similar length on the same "
    "topic and in the same style.\n\n"
    "Original passage:\n{prev_text}\n\nNew passage:\n"
)

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS

# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

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


def load_jsonl(path: Path):
    with open(path) as f:
        return [json.loads(line) for line in f]


# ---------------------------------------------------------------------------
# Model loading (fp16 or 4-bit)
# ---------------------------------------------------------------------------

def load_model_and_tokenizer(model_path, quantize=None, device="cuda:0"):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading tokenizer from {model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    load_kwargs = dict(trust_remote_code=True)

    if quantize == "4bit":
        from transformers import BitsAndBytesConfig
        log.info("Loading model in 4-bit quantization mode ...")
        load_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
        )
        load_kwargs["device_map"] = "auto"
    else:
        log.info("Loading model in fp16 ...")
        load_kwargs["torch_dtype"] = torch.float16
        load_kwargs["device_map"] = "auto"

    model = AutoModelForCausalLM.from_pretrained(model_path, **load_kwargs)
    model.eval()

    vram_mb = torch.cuda.memory_allocated() / 1024**2
    log.info(f"Model loaded. VRAM used: {vram_mb:.0f} MB")
    return model, tokenizer


# ===================================================================
# Step 2: Seed data
# ===================================================================

def prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):
    out_path = data_dir / "depth_0.jsonl"
    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:
        log.info("depth_0.jsonl already exists with enough samples — skipping")
        return

    from datasets import load_dataset

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
# Step 3: Recursive depth chain generation (with OOM protection)
# ===================================================================

def generate_depth_chain(
    model, tokenizer, data_dir: Path, max_depth: int, batch_size: int,
    max_new_tokens: int = 256, top_p: float = 0.95, temperature: float = 1.0,
    do_sample: bool = True,
):
    for depth in range(1, max_depth + 1):
        out_path = data_dir / f"depth_{depth}.jsonl"
        prev_path = data_dir / f"depth_{depth - 1}.jsonl"

        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):
            log.info(f"depth_{depth}.jsonl already complete — skipping")
            continue

        prev_records = load_jsonl(prev_path)
        log.info(f"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...")

        results = []
        current_bs = batch_size

        for start in tqdm(range(0, len(prev_records), current_bs), desc=f"depth {depth}"):
            batch = prev_records[start : start + current_bs]
            prompts = [REWRITE_PROMPT.format(prev_text=r["text"]) for r in batch]

            try:
                inputs = tokenizer(
                    prompts, return_tensors="pt", padding=True,
                    truncation=True, max_length=512,
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

            except torch.cuda.OutOfMemoryError:
                torch.cuda.empty_cache()
                if current_bs > 1:
                    current_bs = max(1, current_bs // 2)
                    log.warning(f"OOM! Reducing batch_size to {current_bs}, retrying ...")
                    # Re-process this batch with smaller size
                    for sub_start in range(0, len(batch), current_bs):
                        sub_batch = batch[sub_start : sub_start + current_bs]
                        sub_prompts = [REWRITE_PROMPT.format(prev_text=r["text"]) for r in sub_batch]
                        inputs = tokenizer(
                            sub_prompts, return_tensors="pt", padding=True,
                            truncation=True, max_length=512,
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
                            results.append({"text": text, "doc_id": sub_batch[j]["doc_id"]})
                        torch.cuda.empty_cache()
                else:
                    log.error(f"OOM even at batch_size=1! Skipping doc_id={batch[0]['doc_id']}")
                    results.append({"text": "", "doc_id": batch[0]["doc_id"]})

            torch.cuda.empty_cache()

        with open(out_path, "w") as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log.info(f"Saved {len(results)} docs to {out_path}")
        torch.cuda.empty_cache()


# ===================================================================
# Step 4: Feature extraction
# ===================================================================

def compute_surprisal_features(model, tokenizer, texts, batch_size=1):
    all_features = []
    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
        batch_texts = texts[start : start + batch_size]

        try:
            inputs = tokenizer(
                batch_texts, return_tensors="pt", padding=True,
                truncation=True, max_length=512,
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

        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            log.warning(f"OOM in surprisal at batch {start}, padding with zeros")
            for _ in batch_texts:
                all_features.append([0.0] * 9)

        torch.cuda.empty_cache()

    return all_features


def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):
    features = []
    tokenized = [t.split() for t in texts]

    bleu_indices = list(range(len(texts)))
    if len(bleu_indices) > sample_bleu:
        rng = np.random.RandomState(42 + depth)
        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()

    same_depth_tokens = tokenized

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


def extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):
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
        vocab = compute_vocab_diversity(texts, tokenizer, depth_texts, d)
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

        torch.cuda.empty_cache()

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved {len(rows)} feature rows to {out_path}")


# ===================================================================
# Step 5: Distinguishability analysis
# ===================================================================

def run_analysis(data_dir: Path, results_dir: Path, max_depth: int):
    import csv

    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score

    results_dir.mkdir(parents=True, exist_ok=True)

    feat_path = data_dir / "features.csv"
    log.info(f"Loading features from {feat_path} ...")
    with open(feat_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    feat_matrix = np.array(
        [[float(r[c]) if r[c] != "" and r[c] != "nan" else np.nan for c in ALL_FEAT_COLS] for r in rows]
    )
    feat_matrix = np.nan_to_num(feat_matrix, nan=0.0)

    # --- Pairwise AUC ---
    log.info("Running pairwise AUC (adjacent depths) ...")
    pairwise_auc = {}
    pairwise_auc_folds = {}

    for k in range(1, max_depth + 1):
        mask = (depths == k - 1) | (depths == k)
        X = feat_matrix[mask]
        y = (depths[mask] == k).astype(int)
        groups = doc_ids[mask]

        if len(np.unique(y)) < 2 or len(np.unique(groups)) < 5:
            pairwise_auc[f"{k-1}v{k}"] = "N/A"
            pairwise_auc_folds[f"{k-1}v{k}"] = []
            continue

        gkf = GroupKFold(n_splits=5)
        fold_aucs = []
        for train_idx, test_idx in gkf.split(X, y, groups=groups):
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(X[train_idx], y[train_idx])
            probs = clf.predict_proba(X[test_idx])[:, 1]
            auc = roc_auc_score(y[test_idx], probs)
            fold_aucs.append(round(auc, 4))

        mean_auc = round(float(np.mean(fold_aucs)), 4)
        pairwise_auc[f"{k-1}v{k}"] = mean_auc
        pairwise_auc_folds[f"{k-1}v{k}"] = fold_aucs
        log.info(f"  AUC({k-1} vs {k}) = {mean_auc} (folds: {fold_aucs})")

    with open(results_dir / "pairwise_auc.json", "w") as f:
        json.dump({"mean": pairwise_auc, "folds": pairwise_auc_folds}, f, indent=2)

    # --- Pairwise JSD ---
    log.info("Computing pairwise JSD ...")
    pairwise_jsd = {}
    for k in range(1, max_depth + 1):
        mask_a = depths == k - 1
        mask_b = depths == k
        jsds_per_feat = []
        for fi in range(feat_matrix.shape[1]):
            a = feat_matrix[mask_a, fi]
            b = feat_matrix[mask_b, fi]
            bins = np.linspace(
                min(a.min(), b.min()) - 1e-8,
                max(a.max(), b.max()) + 1e-8,
                50,
            )
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
        "exp-004 Cross-Scale Validation (Qwen2.5-7B) — Results Summary",
        "=" * 60,
        "",
        "Pairwise AUC (adjacent depths):",
    ]
    for k in range(1, max_depth + 1):
        key = f"{k-1}v{k}"
        folds = pairwise_auc_folds.get(key, [])
        std = float(np.std(folds)) if folds else 0.0
        summary_lines.append(f"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')} +/- {std:.4f}  folds={folds}")
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
        f"Ordinal Classification ({max_depth+1}-class, 5-fold CV):",
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
    parser = argparse.ArgumentParser(description="exp-004: Cross-scale validation (Qwen2.5-7B)")
    parser.add_argument("--model_path", type=str,
                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct")
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/data_exp004")
    parser.add_argument("--results_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/results_exp004")
    parser.add_argument("--n_docs", type=int, default=5000,
                        help="Number of seed documents (use 10 for dry-run)")
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--batch_size", type=int, default=1,
                        help="Generation batch size (default 1 for 7B memory safety)")
    parser.add_argument("--feat_batch_size", type=int, default=1,
                        help="Feature extraction batch size")
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--do_sample", action="store_true", default=True)
    parser.add_argument("--no_sample", dest="do_sample", action="store_false")
    parser.add_argument("--quantize", type=str, default=None, choices=["4bit"],
                        help="Quantization mode (4bit via bitsandbytes)")
    parser.add_argument("--device", type=str, default="cuda:0")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    results_dir = Path(args.results_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    log.info(f"Model: {args.model_path}")
    log.info(f"Quantize: {args.quantize or 'None (fp16)'}")
    log.info(f"Data dir: {data_dir}")
    log.info(f"Samples: {args.n_docs}, Max depth: {args.max_depth}")
    log.info(f"Batch sizes: gen={args.batch_size}, feat={args.feat_batch_size}")

    model, tokenizer = load_model_and_tokenizer(
        args.model_path, quantize=args.quantize, device=args.device,
    )

    # Step 2
    log.info("=" * 40 + " Step 2: Seed Data " + "=" * 40)
    prepare_seed_data(tokenizer, data_dir, args.n_docs)

    # Step 3
    log.info("=" * 40 + " Step 3: Depth Chain " + "=" * 40)
    generate_depth_chain(
        model, tokenizer, data_dir, args.max_depth, args.batch_size,
        top_p=args.top_p, temperature=args.temperature, do_sample=args.do_sample,
    )

    # Step 4
    log.info("=" * 40 + " Step 4: Feature Extraction " + "=" * 40)
    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)

    # Step 5
    log.info("=" * 40 + " Step 5: Analysis " + "=" * 40)
    run_analysis(data_dir, results_dir, args.max_depth)

    log.info("Pipeline complete.")


if __name__ == "__main__":
    main()
