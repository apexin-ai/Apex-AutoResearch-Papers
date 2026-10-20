#!/usr/bin/env python3
"""7B Scorer Ablation (arXiv domain): Qwen2.5-7B vs Qwen2.5-1.5B on arXiv depth chains.

Re-extracts 15D features for Pythia-1.4B and OLMo-1B arXiv depth chains using
both Qwen2.5-1.5B-Instruct and Qwen2.5-7B as scorers, then runs OBD pairwise
classification (LightGBM 5-fold GroupKFold CV + bootstrap CI).

Generators: Pythia-1.4B (exp_025_pythia_arxiv), OLMo-1B (exp_arXiv_olmo)
  — both non-Qwen family, avoids same-family confound with Qwen scorer.
Scorers: Qwen2.5-1.5B-Instruct (baseline), Qwen2.5-7B (ablation)
Domain: arXiv
Device: cuda:0 (expects CUDA_VISIBLE_DEVICES=1 externally)

Deps: torch, transformers, scipy, lightgbm, sklearn, numpy, tqdm
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

# ── paths ──────────────────────────────────────────────────────────────────
ROOT = Path("/root/autodl-tmp/gen-depth-contamination")

SCORER_PATHS = {
    "qwen1.5b": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct",
    "qwen7b":   "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B",
}

GENERATOR_DATA = {
    "pythia_arxiv": ROOT / "data" / "exp_025_pythia_arxiv",
    "olmo_arxiv":   ROOT / "data" / "exp_arXiv_olmo",
}

OUT_DATA_ROOT = ROOT / "data" / "exp_7b_scorer_arxiv"
OUT_RESULTS   = ROOT / "results" / "exp_7b_scorer_arxiv"

MAX_DEPTH = 5
N_BOOT = 10000
THETA = 0.60
SEED = 42

SURPRISAL_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
]
VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS


# ── utility ────────────────────────────────────────────────────────────────
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


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


# ── feature extraction ─────────────────────────────────────────────────────
def compute_surprisal_features(model, tokenizer, texts, batch_size=4):
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
                token_log_probs.append(lp)

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


def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth,
                            sample_bleu=200, bleu_refs=100):
    rng = np.random.RandomState(42)
    features = []

    same_depth_records = depth_texts_map.get(depth, [])
    same_depth_tokenized = None
    if same_depth_records:
        same_depth_tokenized = [
            tokenizer.encode(r["text"], add_special_tokens=False)
            for r in same_depth_records[:sample_bleu]
        ]

    for idx, text in enumerate(texts):
        token_ids = tokenizer.encode(text, add_special_tokens=False)
        if len(token_ids) == 0:
            features.append([0.0, 0.0, 0.0])
            continue

        unique_ids = set(token_ids)
        ttr = len(unique_ids) / len(token_ids)

        id_counts = Counter(token_ids)
        hapax = sum(1 for c in id_counts.values() if c == 1)
        hapax_ratio = hapax / len(id_counts) if id_counts else 0.0

        self_bleu = 0.0
        if same_depth_tokenized and idx < sample_bleu:
            tokens = tokenizer.encode(text, add_special_tokens=False)
            candidates = [j for j in range(len(same_depth_tokenized)) if j != idx]
            if candidates:
                ref_pool = rng.choice(candidates, size=min(bleu_refs, len(candidates)),
                                      replace=False).tolist()
                bleu_scores = [
                    simple_bleu(tokens, same_depth_tokenized[j]) for j in ref_pool
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


def extract_features_for_config(model, tokenizer, data_dir, out_csv, batch_size=4):
    depth_texts = {}
    for d in range(MAX_DEPTH + 1):
        p = data_dir / f"depth_{d}.jsonl"
        if p.exists():
            depth_texts[d] = load_jsonl(p)

    rows = []
    for d in range(MAX_DEPTH + 1):
        if d not in depth_texts:
            continue
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

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
        writer.writeheader()
        writer.writerows(rows)
    log.info(f"Saved {len(rows)} rows to {out_csv}")
    return out_csv


# ── OBD analysis ───────────────────────────────────────────────────────────
def load_features(csv_path):
    with open(csv_path) as f:
        rows = list(csv.DictReader(f))
    depths = np.array([int(r["depth"]) for r in rows])
    try:
        doc_ids = np.array([int(r["doc_id"]) for r in rows])
    except ValueError:
        doc_ids = np.array([r["doc_id"] for r in rows])
    X = np.array(
        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in ALL_FEAT_COLS]
         for r in rows]
    )
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def run_obd_analysis(csv_path, label):
    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import roc_auc_score

    X, depths, doc_ids = load_features(csv_path)
    rng = np.random.RandomState(SEED)

    results = {}
    for k in range(1, MAX_DEPTH + 1):
        pair_key = f"{k-1}v{k}"
        mask = (depths == k - 1) | (depths == k)
        Xp = X[mask]
        yp = (depths[mask] == k).astype(int)
        gp = doc_ids[mask]
        if len(np.unique(yp)) < 2:
            results[pair_key] = {"auc": float("nan"), "ci_lower": 0, "ci_upper": 0, "folds": []}
            continue

        gkf = GroupKFold(n_splits=5)
        oof_proba = np.zeros(len(yp))
        fold_aucs = []
        for train_idx, test_idx in gkf.split(Xp, yp, groups=gp):
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(Xp[train_idx], yp[train_idx])
            proba = clf.predict_proba(Xp[test_idx])[:, 1]
            oof_proba[test_idx] = proba
            fold_aucs.append(roc_auc_score(yp[test_idx], proba))

        point_auc = roc_auc_score(yp, oof_proba)

        unique_docs = np.unique(gp)
        n_docs = len(unique_docs)
        doc_indices = [np.where(gp == d)[0] for d in unique_docs]
        boot_aucs = np.empty(N_BOOT)
        for b in range(N_BOOT):
            sampled = rng.randint(0, n_docs, size=n_docs)
            indices = np.concatenate([doc_indices[s] for s in sampled])
            try:
                boot_aucs[b] = roc_auc_score(yp[indices], oof_proba[indices])
            except ValueError:
                boot_aucs[b] = np.nan
        boot_aucs = boot_aucs[~np.isnan(boot_aucs)]
        ci_lower = float(np.percentile(boot_aucs, 2.5))
        ci_upper = float(np.percentile(boot_aucs, 97.5))

        results[pair_key] = {
            "auc": round(point_auc, 4),
            "ci_lower": round(ci_lower, 4),
            "ci_upper": round(ci_upper, 4),
            "folds": [round(a, 4) for a in fold_aucs],
        }
        log.info(f"  [{label}] {pair_key}: AUC={point_auc:.4f} [{ci_lower:.4f}, {ci_upper:.4f}]")

    k_star = 0
    for k in range(1, MAX_DEPTH + 1):
        pair_key = f"{k-1}v{k}"
        if results.get(pair_key, {}).get("auc", 0) > THETA:
            k_star = k

    results["k_star"] = k_star
    log.info(f"  [{label}] K* = {k_star}")
    return results


# ── model loading ──────────────────────────────────────────────────────────
def load_scorer(path, device="cuda:0"):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading scorer: {path}")
    tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        path,
        torch_dtype=torch.float16,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    log.info(f"Scorer loaded, device={model.device}, "
             f"params={sum(p.numel() for p in model.parameters())/1e9:.1f}B")
    return model, tokenizer


def unload_scorer(model):
    del model
    gc.collect()
    torch.cuda.empty_cache()
    time.sleep(2)


# ── main ───────────────────────────────────────────────────────────────────
def main():
    OUT_RESULTS.mkdir(parents=True, exist_ok=True)
    all_results = {}

    # ── Phase 1: Qwen2.5-1.5B-Instruct scorer ─────────────────────────────
    log.info("=" * 60)
    log.info("Phase 1: Qwen2.5-1.5B-Instruct scorer (arXiv)")
    log.info("=" * 60)

    model_1b5, tok_1b5 = load_scorer(SCORER_PATHS["qwen1.5b"])

    for gen_name, gen_data_dir in GENERATOR_DATA.items():
        label = f"{gen_name}__qwen1.5b"
        out_csv = OUT_DATA_ROOT / label / "features.csv"
        if out_csv.exists():
            log.info(f"[{label}] features.csv exists, skipping extraction")
        else:
            log.info(f"[{label}] Extracting features ...")
            extract_features_for_config(model_1b5, tok_1b5, gen_data_dir, out_csv,
                                        batch_size=8)
        obd = run_obd_analysis(out_csv, label)
        all_results[label] = obd

    unload_scorer(model_1b5)
    del tok_1b5
    gc.collect()

    # ── Phase 2: Qwen2.5-7B scorer ────────────────────────────────────────
    log.info("=" * 60)
    log.info("Phase 2: Qwen2.5-7B scorer (arXiv)")
    log.info("=" * 60)

    model_7b, tok_7b = load_scorer(SCORER_PATHS["qwen7b"])

    for gen_name, gen_data_dir in GENERATOR_DATA.items():
        label = f"{gen_name}__qwen7b"
        out_csv = OUT_DATA_ROOT / label / "features.csv"
        if out_csv.exists():
            log.info(f"[{label}] features.csv exists, skipping extraction")
        else:
            log.info(f"[{label}] Extracting features ...")
            extract_features_for_config(model_7b, tok_7b, gen_data_dir, out_csv,
                                        batch_size=4)
        obd = run_obd_analysis(out_csv, label)
        all_results[label] = obd

    unload_scorer(model_7b)
    del tok_7b
    gc.collect()

    # ── Phase 3: summary ──────────────────────────────────────────────────
    log.info("=" * 60)
    log.info("SUMMARY: 7B Scorer Ablation (arXiv domain)")
    log.info("=" * 60)

    with open(OUT_RESULTS / "all_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    header = f"{'Config':<30s} {'K*':>3s}  {'0v1':>18s}  {'1v2':>18s}  {'2v3':>18s}"
    log.info(header)
    log.info("-" * len(header))

    for label, res in all_results.items():
        k_star = res["k_star"]
        parts = [f"{label:<30s}", f"{k_star:>3d}"]
        for pair in ["0v1", "1v2", "2v3"]:
            r = res.get(pair, {})
            auc = r.get("auc", float("nan"))
            ci_lo = r.get("ci_lower", 0)
            ci_hi = r.get("ci_upper", 0)
            parts.append(f"{auc:.4f}[{ci_lo:.3f},{ci_hi:.3f}]")
        log.info("  ".join(parts))

    summary_lines = [
        "=" * 70,
        "7B Scorer Ablation (arXiv) — Comparison Table",
        "=" * 70,
        "",
        f"{'Config':<30s} {'K*':>3s}  {'0v1 AUC':>10s}  {'1v2 AUC':>10s}  {'2v3 AUC':>10s}",
        "-" * 70,
    ]
    for label, res in all_results.items():
        k_star = res["k_star"]
        cols = [f"{label:<30s}", f"{k_star:>3d}"]
        for pair in ["0v1", "1v2", "2v3"]:
            r = res.get(pair, {})
            auc = r.get("auc", float("nan"))
            ci_lo = r.get("ci_lower", 0)
            ci_hi = r.get("ci_upper", 0)
            cols.append(f"{auc:.4f} [{ci_lo:.3f},{ci_hi:.3f}]")
        summary_lines.append("  ".join(cols))

    summary_lines += [
        "",
        "-" * 70,
        f"Theta = {THETA}, N_boot = {N_BOOT}, 5-fold GroupKFold CV",
        "",
    ]

    for gen_name in GENERATOR_DATA:
        l1 = f"{gen_name}__qwen1.5b"
        l7 = f"{gen_name}__qwen7b"
        k1 = all_results.get(l1, {}).get("k_star", "?")
        k7 = all_results.get(l7, {}).get("k_star", "?")
        match = "MATCH" if k1 == k7 else "DIFFER"
        summary_lines.append(f"  {gen_name}: K*(1.5B)={k1}, K*(7B)={k7} -> {match}")

    summary_lines.append("")
    summary_lines.append("=" * 70)

    summary = "\n".join(summary_lines)
    with open(OUT_RESULTS / "summary.txt", "w") as f:
        f.write(summary)
    log.info(f"\n{summary}")

    log.info("Pipeline complete.")


if __name__ == "__main__":
    main()
