# exp_qwen_retrain_chain_ext: Qwen2.5-1.5B retrain-chain depth extension (depth 5-7)
#
# Continues from the depth 0-4 data produced by exp_qwen_retrain_chain.
# Each generation: fresh LoRA fine-tune on depth_d texts -> merge -> generate depth_{d+1}
#
# Input:  depth_0..4.jsonl from exp_qwen_retrain_chain (same data_dir, auto-skipped)
# Output: depth_5..7.jsonl + features.csv + pairwise_auc.json + jsd.json (5-fold CV)
# Deps:   torch, transformers, peft, lightgbm, sklearn, scipy, tqdm, numpy
# Note:   No bootstrap (GroupKFold data leakage risk). Uses 5-fold GroupKFold CV only.

import argparse
import csv
import gc
import json
import logging
import math
import os
import shutil
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import torch
from scipy import stats
from tqdm import tqdm

os.environ.setdefault("HF_HOME", "/root/autodl-tmp/.hf_cache")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config (identical to original experiment)
# ---------------------------------------------------------------------------

QWEN_MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B"
SCORER_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B"
SEED_DATA = "/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain/depth_0.jsonl"

LORA_RANK = 16
LORA_ALPHA = 32
LORA_TARGET_MODULES = ["q_proj", "k_proj", "v_proj"]
TRAIN_LR = 2e-4
TRAIN_BATCH_SIZE = 4
GRADIENT_ACCUMULATION = 4
TRAIN_EPOCHS = 1

GEN_TOP_P = 0.95
GEN_TEMPERATURE = 1.0
GEN_MAX_NEW_TOKENS = 256
GEN_BATCH_SIZE = 8

MAX_DEPTH = 7
NUM_SAMPLES = 5000

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(records, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]


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
        clipped = sum(min(cnt, ref_counts.get(ng, 0)) for ng, cnt in Counter(cand_ngrams).items())
        precisions.append(clipped / len(cand_ngrams))
    if any(p == 0 for p in precisions):
        return 0.0
    log_avg = sum(math.log(p) for p in precisions) / max_n
    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
    return bp * math.exp(log_avg)


def detect_lora_targets(model):
    module_names = {name.split(".")[-1] for name, _ in model.named_modules()}
    candidates = [
        ["q_proj", "k_proj", "v_proj"],
        ["query_key_value"],
        ["qkv_proj"],
    ]
    for target_set in candidates:
        if all(t in module_names for t in target_set):
            return target_set
    log.warning(f"Could not auto-detect LoRA targets, using default: {LORA_TARGET_MODULES}")
    return LORA_TARGET_MODULES


# ---------------------------------------------------------------------------
# Phase 1: LoRA Fine-tuning
# ---------------------------------------------------------------------------

def finetune_lora(model_id, train_texts, device="cuda:0"):
    from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForLanguageModeling
    from peft import LoraConfig, get_peft_model, TaskType
    from torch.utils.data import Dataset, DataLoader

    log.info(f"Loading base model for fine-tuning ({len(train_texts)} texts)...")
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id

    model = AutoModelForCausalLM.from_pretrained(
        model_id, torch_dtype=torch.float16, device_map={"": device}, trust_remote_code=True
    )

    targets = detect_lora_targets(model)
    log.info(f"LoRA target modules: {targets}")

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=LORA_RANK,
        lora_alpha=LORA_ALPHA,
        target_modules=targets,
        lora_dropout=0.05,
        bias="none",
    )
    model = get_peft_model(model, lora_config)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    log.info(f"Trainable: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")

    class TextDataset(Dataset):
        def __init__(self, texts, tok, max_length=256):
            self.encodings = []
            for t in texts:
                ids = tok.encode(t, add_special_tokens=True, truncation=True, max_length=max_length)
                self.encodings.append(torch.tensor(ids, dtype=torch.long))

        def __len__(self):
            return len(self.encodings)

        def __getitem__(self, idx):
            return {"input_ids": self.encodings[idx]}

    dataset = TextDataset(train_texts, tokenizer, max_length=GEN_MAX_NEW_TOKENS)
    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    dataloader = DataLoader(
        dataset, batch_size=TRAIN_BATCH_SIZE, shuffle=True, collate_fn=collator
    )

    optimizer = torch.optim.AdamW(
        [p for p in model.parameters() if p.requires_grad], lr=TRAIN_LR
    )

    model.train()
    total_loss = 0.0
    steps = 0
    optimizer.zero_grad()

    for epoch in range(TRAIN_EPOCHS):
        for batch_idx, batch in enumerate(tqdm(dataloader, desc="Fine-tuning")):
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(**batch)
            loss = outputs.loss / GRADIENT_ACCUMULATION
            loss.backward()
            total_loss += loss.item() * GRADIENT_ACCUMULATION

            if (batch_idx + 1) % GRADIENT_ACCUMULATION == 0:
                optimizer.step()
                optimizer.zero_grad()
                steps += 1

        if (batch_idx + 1) % GRADIENT_ACCUMULATION != 0:
            optimizer.step()
            optimizer.zero_grad()
            steps += 1

    avg_loss = total_loss / max(len(dataloader), 1)
    log.info(f"Fine-tuning done. Avg loss: {avg_loss:.4f}, steps: {steps}")

    model.eval()
    merged = model.merge_and_unload()
    log.info("LoRA weights merged into base model")
    return merged, tokenizer


# ---------------------------------------------------------------------------
# Phase 2: Text Generation (continuation mode)
# ---------------------------------------------------------------------------

def generate_texts(model, tokenizer, input_texts, device="cuda:0"):
    log.info(f"Generating {len(input_texts)} texts (nucleus p={GEN_TOP_P}, T={GEN_TEMPERATURE})...")
    tokenizer.padding_side = "left"
    results = []

    for start in tqdm(range(0, len(input_texts), GEN_BATCH_SIZE), desc="Generating"):
        batch_texts = input_texts[start:start + GEN_BATCH_SIZE]

        prefix_texts = []
        for text in batch_texts:
            ids = tokenizer.encode(text, add_special_tokens=False)
            prefix_len = max(1, len(ids) // 2)
            prefix_texts.append(tokenizer.decode(ids[:prefix_len], skip_special_tokens=True))

        inputs = tokenizer(
            prefix_texts, return_tensors="pt", padding=True, truncation=True, max_length=256
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=GEN_MAX_NEW_TOKENS,
                do_sample=True,
                top_p=GEN_TOP_P,
                temperature=GEN_TEMPERATURE,
                pad_token_id=tokenizer.pad_token_id,
            )

        for j, out_ids in enumerate(outputs):
            prompt_len = inputs["input_ids"].shape[1]
            generated_ids = out_ids[prompt_len:]
            text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
            results.append(text)

        torch.cuda.empty_cache()

    return results


# ---------------------------------------------------------------------------
# Phase 3: Feature extraction
# ---------------------------------------------------------------------------

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS


def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
    features = []
    tokenizer.padding_side = "left"

    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
        batch_texts = texts[start:start + batch_size]
        inputs = tokenizer(
            batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=512
        ).to(model.device)

        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits

        for j in range(len(batch_texts)):
            ids = inputs["input_ids"][j]
            attn = inputs["attention_mask"][j]
            valid_len = attn.sum().item()
            if valid_len < 3:
                features.append([0.0] * 9)
                continue

            valid_logits = logits[j, :valid_len - 1]
            valid_targets = ids[1:valid_len]

            log_probs = torch.log_softmax(valid_logits.float(), dim=-1)
            token_surprisals = -log_probs.gather(1, valid_targets.unsqueeze(1)).squeeze(1)
            surp = token_surprisals.cpu().numpy()

            if len(surp) < 2:
                features.append([0.0] * 9)
                continue

            s_mean = float(np.mean(surp))
            s_std = float(np.std(surp))
            s_skew = float(stats.skew(surp)) if len(surp) >= 3 else 0.0
            s_kurt = float(stats.kurtosis(surp)) if len(surp) >= 4 else 0.0

            d1 = np.diff(surp)
            d1_mean = float(np.mean(d1)) if len(d1) > 0 else 0.0
            d1_std = float(np.std(d1)) if len(d1) > 0 else 0.0
            d1_skew = float(stats.skew(d1)) if len(d1) >= 3 else 0.0

            d2 = np.diff(d1)
            d2_mean = float(np.mean(d2)) if len(d2) > 0 else 0.0
            d2_std = float(np.std(d2)) if len(d2) > 0 else 0.0

            features.append([s_mean, s_std, s_skew, s_kurt, d1_mean, d1_std, d1_skew, d2_mean, d2_std])

        torch.cuda.empty_cache()

    return features


def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, bleu_refs=100):
    same_depth_tokens = [tokenizer.encode(t, add_special_tokens=False) for t in texts]
    features = []

    for idx, tokens in enumerate(tqdm(same_depth_tokens, desc=f"Vocab d={depth}", leave=False)):
        total = len(tokens)
        if total == 0:
            features.append([0.0, 0.0, 0.0])
            continue

        ttr = len(set(tokens)) / total
        freq = Counter(tokens)
        hapax_ratio = sum(1 for v in freq.values() if v == 1) / max(len(set(tokens)), 1)

        rng_local = np.random.RandomState(idx)
        ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]
        if len(ref_pool) > bleu_refs:
            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
        bleu_scores = [simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool]
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
        total_count = counts.sum()
        probs = counts / total_count
        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
        low_freq_ratio = float(np.sum(counts <= 2)) / max(len(counts), 1)
        features.append([kurt, entropy, low_freq_ratio])
    return features


def extract_all_features(scorer_path, data_dir, max_depth, device="cuda:0"):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    out_path = data_dir / "features.csv"
    log.info(f"Loading scorer from {scorer_path}...")
    tokenizer = AutoTokenizer.from_pretrained(scorer_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        scorer_path, torch_dtype=torch.float16, device_map={"": device}, trust_remote_code=True
    )
    model.eval()

    depth_texts = {}
    for d in range(max_depth + 1):
        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
        depth_texts[d] = [r["text"] for r in records]

    rows = []
    for d in range(max_depth + 1):
        texts = depth_texts[d]
        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
        doc_ids = [r["doc_id"] for r in records]
        log.info(f"  Extracting features depth {d}: {len(texts)} texts")

        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=8)
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

    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved {len(rows)} feature rows to {out_path}")

    del model
    torch.cuda.empty_cache()
    gc.collect()


# ---------------------------------------------------------------------------
# Phase 4: Analysis (5-fold GroupKFold CV only, no bootstrap)
# ---------------------------------------------------------------------------

def run_analysis(data_dir, results_dir, max_depth):
    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import roc_auc_score

    results_dir.mkdir(parents=True, exist_ok=True)
    feat_path = data_dir / "features.csv"
    log.info(f"Loading features from {feat_path}...")

    with open(feat_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    feat_matrix = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in ALL_FEAT_COLS] for r in rows]
    )
    col_means = np.nanmean(feat_matrix, axis=0)
    for j in range(feat_matrix.shape[1]):
        mask = np.isnan(feat_matrix[:, j])
        feat_matrix[mask, j] = col_means[j]

    # Pairwise AUC with 5-fold GroupKFold
    log.info("Computing pairwise AUC (5-fold GroupKFold CV)...")
    AUC_THRESHOLD = 0.60
    pairwise_auc = {}
    pairwise_auc_folds = {}
    pairwise_auc_ci = {}
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
        ci_lo = auc_mean - 1.96 * auc_std / np.sqrt(len(fold_aucs))
        ci_hi = auc_mean + 1.96 * auc_std / np.sqrt(len(fold_aucs))
        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
        pairwise_auc_folds[f"{k-1}v{k}"] = [round(a, 4) for a in fold_aucs]
        pairwise_auc_ci[f"{k-1}v{k}"] = {
            "mean": round(auc_mean, 4),
            "std": round(auc_std, 4),
            "ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
        }
        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f} +/- {auc_std:.4f}  CI=[{ci_lo:.4f}, {ci_hi:.4f}]")

    with open(results_dir / "pairwise_auc.json", "w") as f:
        json.dump({"mean": pairwise_auc, "per_fold": pairwise_auc_folds, "ci": pairwise_auc_ci}, f, indent=2)

    # JSD
    log.info("Computing pairwise JSD...")
    pairwise_jsd = {}
    for k in range(1, max_depth + 1):
        feat_prev = feat_matrix[depths == k - 1]
        feat_curr = feat_matrix[depths == k]
        jsds = []
        for j in range(feat_matrix.shape[1]):
            a, b = feat_prev[:, j], feat_curr[:, j]
            lo, hi = min(a.min(), b.min()), max(a.max(), b.max())
            if hi - lo < 1e-12:
                jsds.append(0.0)
                continue
            bins = np.linspace(lo, hi, 51)
            p = np.histogram(a, bins=bins, density=True)[0] + 1e-12
            q = np.histogram(b, bins=bins, density=True)[0] + 1e-12
            p, q = p / p.sum(), q / q.sum()
            m = 0.5 * (p + q)
            jsd = 0.5 * np.sum(p * np.log2(p / m)) + 0.5 * np.sum(q * np.log2(q / m))
            jsds.append(float(jsd))
        pairwise_jsd[f"{k-1}v{k}"] = round(float(np.mean(jsds)), 6)
        log.info(f"  JSD({k-1} vs {k}) = {np.mean(jsds):.6f}")

    with open(results_dir / "jsd.json", "w") as f:
        json.dump(pairwise_jsd, f, indent=2)

    # K* determination
    k_star = 0
    for k in range(1, max_depth + 1):
        if pairwise_auc.get(f"{k-1}v{k}", 0) > AUC_THRESHOLD:
            k_star = k
    log.info(f"K* = {k_star}")

    # Summary
    summary = {
        "experiment": "exp_qwen_retrain_chain_ext",
        "model": QWEN_MODEL_PATH,
        "scorer": SCORER_PATH,
        "protocol": "retrain-chain (independent LoRA per generation, merge before next)",
        "lora_config": {"rank": LORA_RANK, "alpha": LORA_ALPHA, "target_modules": LORA_TARGET_MODULES},
        "decoding": {"top_p": GEN_TOP_P, "temperature": GEN_TEMPERATURE},
        "max_depth": max_depth,
        "num_samples": NUM_SAMPLES,
        "k_star": k_star,
        "auc_threshold": AUC_THRESHOLD,
        "pairwise_auc": pairwise_auc,
        "pairwise_auc_ci": pairwise_auc_ci,
        "pairwise_jsd": pairwise_jsd,
        "analysis_method": "5-fold GroupKFold CV (no bootstrap)",
    }
    with open(results_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    log.info(f"Summary saved. K*={k_star}")

    return summary


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Qwen2.5-1.5B retrain-chain depth extension (5-7)")
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_retrain_chain")
    parser.add_argument("--results_dir", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/results/exp_qwen_retrain_chain_ext")
    parser.add_argument("--log_file", type=str,
                        default="/root/autodl-tmp/gen-depth-contamination/logs/exp_qwen_retrain_chain_ext.log")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--max_depth", type=int, default=MAX_DEPTH)
    parser.add_argument("--skip_generation", action="store_true", help="Skip to evaluation only")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    results_dir = Path(args.results_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    log_path = Path(args.log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(log_path)
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
    logging.getLogger().addHandler(fh)

    log.info("=" * 60)
    log.info("exp_qwen_retrain_chain_ext: depth extension (5-7)")
    log.info(f"Model: {QWEN_MODEL_PATH}")
    log.info(f"Scorer: {SCORER_PATH}")
    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}, target={LORA_TARGET_MODULES}")
    log.info(f"Decoding: nucleus p={GEN_TOP_P}, T={GEN_TEMPERATURE}")
    log.info(f"Data dir: {data_dir}")
    log.info(f"Max depth: {args.max_depth}")
    log.info("=" * 60)

    if not args.skip_generation:
        seed_dest = data_dir / "depth_0.jsonl"
        if not seed_dest.exists():
            log.info(f"Copying seed data from {SEED_DATA}")
            shutil.copy2(SEED_DATA, seed_dest)
        log.info(f"Seed data: {sum(1 for _ in open(seed_dest))} docs")

        for d in range(args.max_depth):
            log.info("=" * 40 + f" Generation {d} -> {d+1} " + "=" * 40)
            out_path = data_dir / f"depth_{d+1}.jsonl"

            if out_path.exists() and sum(1 for _ in open(out_path)) >= NUM_SAMPLES:
                log.info(f"depth_{d+1}.jsonl already exists ({sum(1 for _ in open(out_path))} docs), skipping")
                continue

            train_records = load_jsonl(data_dir / f"depth_{d}.jsonl")
            train_texts = [r["text"] for r in train_records]
            log.info(f"Training on {len(train_texts)} texts from depth_{d}")

            model, tokenizer = finetune_lora(QWEN_MODEL_PATH, train_texts, device=args.device)

            generated_texts = generate_texts(model, tokenizer, train_texts, device=args.device)

            records = [{"text": t, "doc_id": i} for i, t in enumerate(generated_texts)]
            save_jsonl(records, out_path)
            log.info(f"Saved {len(records)} docs to {out_path}")

            del model, tokenizer
            torch.cuda.empty_cache()
            gc.collect()
            log.info(f"Generation {d}->{d+1} complete, memory released")

    # Feature extraction (re-extract all depths 0-7)
    log.info("=" * 40 + " Feature Extraction " + "=" * 40)
    extract_all_features(SCORER_PATH, data_dir, args.max_depth, device=args.device)

    # Analysis (5-fold GroupKFold CV, no bootstrap)
    log.info("=" * 40 + " Analysis " + "=" * 40)
    summary = run_analysis(data_dir, results_dir, args.max_depth)

    log.info("=" * 60)
    log.info(f"DONE. K*={summary['k_star']}")
    log.info(f"Results: {results_dir}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
