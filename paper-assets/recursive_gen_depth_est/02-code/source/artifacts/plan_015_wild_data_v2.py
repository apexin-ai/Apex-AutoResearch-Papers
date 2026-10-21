#!/usr/bin/env python3
"""Plan 015 v2: Wild-Data Calibration on OpenWebText & WikiText-103.

Validates RF depth classifiers on large-scale wild web text.
- 3 RF classifiers (Pythia nucleus, GPT-2 XL, OLMo)
- 2 wild datasets: OpenWebText (cuda:0), WikiText-103 (cuda:1)
- Feature extractor: Pythia-1.4B (consistent with training)
"""

import argparse
import json
import os
import sys
import time
import numpy as np
from collections import Counter
from threading import Thread
from scipy.stats import skew, kurtosis, entropy
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
OUTPUT_DIR = os.path.join(PROJECT_DIR, "results/plan_015_wild_data_v2")

FEATURE_FILES = {
    "pythia_nucleus": os.path.join(PROJECT_DIR, "data/features_all.jsonl"),
    "gpt2xl": os.path.join(PROJECT_DIR, "data/gpt2xl/features.jsonl"),
    "olmo": os.path.join(PROJECT_DIR, "data/olmo/features.jsonl"),
}

TRUNC_LEN = 507


# ── Feature computation (identical to training pipeline) ──

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
            "type_token_ratio", "hapax_ratio", "bigram_entropy",
            "trigram_entropy", "rep_2gram", "rep_3gram", "rep_4gram"]}
    counts = Counter(token_ids)
    ttr = len(counts) / n_tokens
    hapax = sum(1 for v in counts.values() if v == 1) / len(counts) if counts else 0.0

    def ngram_entropy_val(ids, n):
        if len(ids) < n:
            return 0.0
        ng = [tuple(ids[i:i+n]) for i in range(len(ids) - n + 1)]
        c = Counter(ng)
        total = sum(c.values())
        probs = np.array([v / total for v in c.values()])
        return float(entropy(probs))

    return {
        "type_token_ratio": ttr,
        "hapax_ratio": hapax,
        "bigram_entropy": ngram_entropy_val(token_ids, 2),
        "trigram_entropy": ngram_entropy_val(token_ids, 3),
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

    ppl = np.exp(np.clip(losses_np, 0, 500))
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


# ── Data loading ──

def load_wild_texts(dataset_name, n_target, tokenizer, trunc_len):
    """Load passages from HuggingFace streaming, filtering by min length."""
    from datasets import load_dataset

    texts = []
    skipped = 0

    if dataset_name == "openwebtext":
        configs = [
            dict(path="Skylion007/openwebtext", split="train",
                 text_field="text"),
        ]
    elif dataset_name == "wikitext":
        configs = [
            dict(path="wikitext", name="wikitext-103-raw-v1", split="train",
                 text_field="text"),
        ]
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    ds = None
    text_field = "text"

    for cfg in configs:
        try:
            kwargs = dict(streaming=True)
            if "name" in cfg:
                kwargs["name"] = cfg["name"]
            print(f"    Trying {cfg['path']} (config={cfg.get('name', 'default')})...", flush=True)
            ds = load_dataset(cfg["path"], split=cfg.get("split", "train"), **kwargs)
            text_field = cfg["text_field"]
            print(f"    OK: loaded {cfg['path']}", flush=True)
            break
        except Exception as e:
            print(f"    Failed: {e}", flush=True)
            continue

    if ds is None:
        print(f"    ERROR: all configs failed for {dataset_name}", flush=True)
        return []

    t0 = time.time()
    for sample in ds:
        if len(texts) >= n_target:
            break
        text = sample.get(text_field, "") or sample.get("text", "") or sample.get("content", "")
        if not text or not isinstance(text, str) or len(text) < 200:
            skipped += 1
            continue
        tok_ids = tokenizer.encode(text, add_special_tokens=False)
        if len(tok_ids) < trunc_len:
            skipped += 1
            continue
        texts.append(text)
        if len(texts) % 500 == 0:
            elapsed = time.time() - t0
            print(f"    {dataset_name}: {len(texts)}/{n_target} "
                  f"(skipped {skipped}, {elapsed:.0f}s)", flush=True)

    elapsed = time.time() - t0
    print(f"    {dataset_name}: collected {len(texts)} passages "
          f"(skipped {skipped}, {elapsed:.0f}s)", flush=True)
    return texts


# ── Feature extraction ──

def extract_features_on_gpu(texts, tokenizer, device, trunc_len):
    """Load Pythia-1.4B on GPU and extract 19 features per passage."""
    print(f"  Loading model on {device}...", flush=True)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, dtype=torch.float16)
    model.to(device)
    model.eval()

    features = []
    t0 = time.time()
    for i, text in enumerate(texts):
        token_ids = tokenizer.encode(text, add_special_tokens=False)[:trunc_len]
        input_ids = torch.tensor([token_ids], device=device)

        with torch.no_grad():
            logits = model(input_ids).logits

        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = input_ids[:, 1:].contiguous()
        losses = torch.nn.functional.cross_entropy(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1),
            reduction="none",
        )
        losses_np = losses.cpu().numpy()

        feat = {}
        feat.update(compute_perplexity_features(losses_np))
        feat.update(compute_lexical_features(token_ids))
        features.append(feat)

        if (i + 1) % 500 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            print(f"    {device}: {i+1}/{len(texts)} ({rate:.1f} samples/s)", flush=True)

    elapsed = time.time() - t0
    print(f"    {device}: done {len(features)} samples in {elapsed:.0f}s", flush=True)

    del model
    torch.cuda.empty_cache()
    return features


# ── RF training & classification ──

def load_features_jsonl(filepath):
    entries = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def train_rf(entries, n_estimators=200, seed=42):
    filtered = [e for e in entries if e["depth"] <= 3]
    X = np.array([[e[f] for f in FEATURE_NAMES] for e in filtered])
    y = np.array([e["depth"] for e in filtered])
    rf = RandomForestClassifier(n_estimators=n_estimators, random_state=seed, n_jobs=-1)
    rf.fit(X, y)
    return rf


def classify_wild(rf, features_list):
    X = np.array([[f[fname] for fname in FEATURE_NAMES] for f in features_list])
    X = np.nan_to_num(X, nan=0.0, posinf=1e30, neginf=-1e30)
    pred = rf.predict(X)
    prob = rf.predict_proba(X)
    n = len(pred)
    pred_dist = Counter(int(p) for p in pred)
    d0_rate = float((pred == 0).sum()) / n * 100
    fpr = 100.0 - d0_rate
    return {
        "n_samples": n,
        "d0_accuracy": round(d0_rate, 4),
        "fpr": round(fpr, 4),
        "pred_distribution": {f"d{d}": int(pred_dist.get(d, 0)) for d in range(4)},
        "pred_pct": {f"d{d}": round(pred_dist.get(d, 0) / n * 100, 4) for d in range(4)},
        "mean_prob": {f"d{i}": round(float(prob[:, i].mean()), 4) for i in range(min(4, prob.shape[1]))},
        "std_prob": {f"d{i}": round(float(prob[:, i].std()), 4) for i in range(min(4, prob.shape[1]))},
    }


# ── Main ──

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_passages", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--trunc_len", type=int, default=TRUNC_LEN)
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    t_start = time.time()

    print("=" * 60)
    print("  Plan 015 v2: Wild-Data Calibration")
    print("  OpenWebText (cuda:0) & WikiText-103 (cuda:1)")
    print("=" * 60)
    print(f"  n_passages: {args.n_passages}")
    print(f"  trunc_len:  {args.trunc_len}")
    print(f"  model:      {MODEL_PATH}")
    print(f"  output:     {OUTPUT_DIR}")
    n_gpus = torch.cuda.device_count()
    for i in range(n_gpus):
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
    sys.stdout.flush()

    # ── Step 1: Tokenizer ──
    print("\n" + "=" * 60)
    print("  Step 1: Loading Tokenizer")
    print("=" * 60, flush=True)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print(f"  vocab_size={tokenizer.vocab_size}", flush=True)

    # ── Step 2: Train 3 RF classifiers ──
    print("\n" + "=" * 60)
    print("  Step 2: Training 3 RF Classifiers")
    print("=" * 60, flush=True)

    classifiers = {}
    for name, fpath in FEATURE_FILES.items():
        entries = load_features_jsonl(fpath)
        filtered = [e for e in entries if e["depth"] <= 3]
        depth_counts = Counter(e["depth"] for e in filtered)
        rf = train_rf(filtered, n_estimators=200, seed=args.seed)
        classifiers[name] = rf
        print(f"  {name}: {dict(sorted(depth_counts.items()))}, "
              f"{rf.n_estimators} trees", flush=True)

    # ── Step 3: Load wild data (sequential, network-bound) ──
    print("\n" + "=" * 60)
    print("  Step 3: Loading Wild Data (HuggingFace streaming)")
    print("=" * 60, flush=True)

    wild_texts = {}
    for ds_name in ["openwebtext", "wikitext"]:
        print(f"\n  --- {ds_name} ---", flush=True)
        wild_texts[ds_name] = load_wild_texts(
            ds_name, args.n_passages, tokenizer, args.trunc_len)

    # ── Step 4: Extract features (dual GPU parallel) ──
    print("\n" + "=" * 60)
    print("  Step 4: Feature Extraction (Dual GPU)")
    print("=" * 60, flush=True)

    wild_features = {}
    errors = {}

    def run_extraction(ds_name, gpu_id):
        try:
            device = f"cuda:{gpu_id}"
            texts = wild_texts[ds_name]
            if not texts:
                wild_features[ds_name] = []
                return
            feats = extract_features_on_gpu(texts, tokenizer, device, args.trunc_len)
            wild_features[ds_name] = feats
        except Exception as e:
            import traceback
            errors[ds_name] = traceback.format_exc()
            wild_features[ds_name] = []

    threads = []
    gpu_map = {"openwebtext": 0, "wikitext": 1}
    for ds_name, gpu_id in gpu_map.items():
        t = Thread(target=run_extraction, args=(ds_name, gpu_id))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    for ds_name, err in errors.items():
        print(f"  ERROR in {ds_name}:\n{err}", flush=True)

    # ── Step 5: Classification ──
    print("\n" + "=" * 60)
    print("  Step 5: Classification Results")
    print("=" * 60, flush=True)

    all_reports = {}
    for ds_name, features in wild_features.items():
        if not features:
            print(f"  Skipping {ds_name} (no features)", flush=True)
            continue

        print(f"\n  --- {ds_name.upper()} ({len(features)} passages) ---", flush=True)
        ds_reports = {}
        for clf_name, rf in classifiers.items():
            report = classify_wild(rf, features)
            report["dataset"] = ds_name
            report["classifier"] = clf_name
            ds_reports[clf_name] = report
            print(f"    {clf_name:20s}  d0={report['d0_accuracy']:6.2f}%  "
                  f"FPR={report['fpr']:6.2f}%  P(d0)={report['mean_prob']['d0']:.4f}",
                  flush=True)

        all_reports[ds_name] = ds_reports

    # ── Step 6: Cross-model consistency ──
    print("\n" + "=" * 60)
    print("  Step 6: Cross-Model FPR Consistency")
    print("=" * 60, flush=True)

    consistency = {}
    for ds_name, ds_reports in all_reports.items():
        fprs = {c: r["fpr"] for c, r in ds_reports.items()}
        vals = list(fprs.values())
        consistency[ds_name] = {
            "per_classifier": fprs,
            "mean_fpr": round(float(np.mean(vals)), 4),
            "std_fpr": round(float(np.std(vals)), 4),
            "max_fpr": round(float(np.max(vals)), 4),
        }
        print(f"  {ds_name}: mean_FPR={consistency[ds_name]['mean_fpr']:.4f} "
              f"+/- {consistency[ds_name]['std_fpr']:.4f}  "
              f"(max={consistency[ds_name]['max_fpr']:.4f})", flush=True)
        for c, v in fprs.items():
            print(f"    {c}: {v:.4f}%", flush=True)

    # ── Step 7: Save results ──
    print("\n" + "=" * 60)
    print("  Step 7: Saving Results")
    print("=" * 60, flush=True)

    elapsed_total = time.time() - t_start

    results = {
        "experiment": "wild_data_calibration_002",
        "feature_model": "pythia-1.4b",
        "rf_config": {"n_estimators": 200, "seed": args.seed},
        "trunc_len": args.trunc_len,
        "n_passages_requested": args.n_passages,
        "elapsed_seconds": round(elapsed_total, 1),
        "datasets": {},
        "cross_model_consistency": consistency,
        "classifier_cells": list(FEATURE_FILES.keys()),
    }

    for ds_name, ds_reports in all_reports.items():
        results["datasets"][ds_name] = {
            "n_passages_loaded": len(wild_texts.get(ds_name, [])),
            "n_features_extracted": len(wild_features.get(ds_name, [])),
            "reports": ds_reports,
        }

    results_path = os.path.join(OUTPUT_DIR, "calibration_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved {results_path}", flush=True)

    for ds_name, features in wild_features.items():
        if not features:
            continue
        feat_path = os.path.join(OUTPUT_DIR, f"{ds_name}_features.jsonl")
        with open(feat_path, "w") as f:
            for i, feat in enumerate(features):
                row = {"sample_id": i}
                row.update(feat)
                f.write(json.dumps(row) + "\n")
        print(f"  Saved {feat_path} ({len(features)} rows)", flush=True)

    # ── Final summary table ──
    print("\n" + "=" * 60)
    print("  FINAL SUMMARY")
    print("=" * 60)
    print(f"\n  {'Dataset':<15s} {'Classifier':<20s} {'N':>6s} "
          f"{'d0%':>8s} {'FPR%':>8s} {'P(d0)':>8s}")
    print(f"  {'-'*15} {'-'*20} {'-'*6} {'-'*8} {'-'*8} {'-'*8}")

    for ds_name, ds_reports in all_reports.items():
        for clf_name, r in ds_reports.items():
            print(f"  {ds_name:<15s} {clf_name:<20s} {r['n_samples']:>6d} "
                  f"{r['d0_accuracy']:>8.2f} {r['fpr']:>8.2f} "
                  f"{r['mean_prob']['d0']:>8.4f}")

    print(f"\n  Per-depth breakdown:")
    for ds_name, ds_reports in all_reports.items():
        for clf_name, r in ds_reports.items():
            pcts = r["pred_pct"]
            print(f"    {ds_name}/{clf_name}: "
                  f"d0={pcts['d0']:.2f}% d1={pcts['d1']:.2f}% "
                  f"d2={pcts['d2']:.2f}% d3={pcts['d3']:.2f}%")

    print(f"\n  Total time: {elapsed_total:.0f}s")
    print(f"  Results: {OUTPUT_DIR}/")
    print("  Done.", flush=True)


if __name__ == "__main__":
    main()
