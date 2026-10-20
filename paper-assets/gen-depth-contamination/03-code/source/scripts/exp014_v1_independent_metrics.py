"""
exp-014 v1: Independent Quality Metrics on 5K CC docs.

Computes 6 quality metrics fully independent of OBD 15D features on the
v1 CC sample (5000 docs) with predicted depth from ordinal_pred.

Input:  results/exp_014_naturalistic/{cc_sample.jsonl, cc_predictions.csv}
Output: results/exp014_v2/cc_quality_independent.csv
"""

import csv
import gc
import json
import logging
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import stats
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
V1_DIR = PROJECT_ROOT / "results" / "exp_014_naturalistic"
OUT_DIR = PROJECT_ROOT / "results" / "exp014_v2"
HF_CACHE = "/root/autodl-tmp/.hf_cache"
DEVICE = "cuda"
SEED = 42
BATCH_SIZE = 16

METRIC_COLS = ["gpt2_ppl", "mtld", "hdd", "rep_3gram", "rep_4gram", "zipf"]


def load_texts():
    path = V1_DIR / "cc_sample.jsonl"
    if not path.exists():
        log.error(f"{path} not found")
        sys.exit(1)
    texts, doc_ids = [], []
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            texts.append(obj["text"])
            doc_ids.append(obj["doc_id"])
    log.info(f"Loaded {len(texts)} texts from {path}")
    return texts, doc_ids


def load_predictions():
    path = V1_DIR / "cc_predictions.csv"
    if not path.exists():
        log.error(f"{path} not found")
        sys.exit(1)
    with open(path) as f:
        rows = list(csv.DictReader(f))
    depths = np.array([int(r["ordinal_pred"]) for r in rows])
    log.info(f"Loaded {len(depths)} predictions, depth range [{depths.min()}, {depths.max()}]")
    return depths


def load_existing_metrics(n_texts):
    path = OUT_DIR / "cc_quality_independent.csv"
    if not path.exists():
        return {}
    with open(path) as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return {}
        cols = [c for c in reader.fieldnames if c in METRIC_COLS]
        if not cols:
            return {}
        data = {c: [] for c in cols}
        for row in reader:
            for c in cols:
                v = row.get(c, "")
                data[c].append(float(v) if v not in ("", "nan") else float("nan"))
        result = {}
        for c in cols:
            arr = np.array(data[c])
            valid_ratio = np.sum(~np.isnan(arr)) / max(len(arr), 1)
            if len(arr) == n_texts and valid_ratio > 0.5:
                result[c] = arr
                log.info(f"  Loaded existing {c}: {np.sum(~np.isnan(arr))} valid values")
    return result


# ── GPT-2 Large Perplexity ──

def compute_gpt2_ppl(texts):
    import torch
    from transformers import GPT2LMHeadModel, GPT2TokenizerFast

    log.info("Loading GPT-2 Large ...")
    tok = GPT2TokenizerFast.from_pretrained("gpt2-large", cache_dir=HF_CACHE)
    model = GPT2LMHeadModel.from_pretrained("gpt2-large", cache_dir=HF_CACHE).eval().to(DEVICE)
    tok.pad_token = tok.eos_token
    tok.padding_side = "left"

    ppls = []
    for i in tqdm(range(0, len(texts), BATCH_SIZE), desc="GPT2-PPL"):
        batch = texts[i : i + BATCH_SIZE]
        inputs = tok(
            batch, return_tensors="pt", padding=True,
            truncation=True, max_length=512,
        ).to(DEVICE)

        with torch.no_grad():
            outputs = model(**inputs, labels=inputs["input_ids"])
            logits = outputs.logits

        for j in range(len(batch)):
            mask = inputs["attention_mask"][j].bool()
            seq_len = mask.sum().item()
            if seq_len < 2:
                ppls.append(float("nan"))
                continue
            offset = inputs["input_ids"].shape[1] - seq_len
            shift_logits = logits[j, offset:-1, :]
            shift_labels = inputs["input_ids"][j, offset + 1 :]
            loss_fn = torch.nn.CrossEntropyLoss(reduction="mean")
            loss = loss_fn(shift_logits[: seq_len - 1], shift_labels[: seq_len - 1])
            ppls.append(float(torch.exp(loss).cpu()))

        if (i // BATCH_SIZE) % 200 == 0:
            torch.cuda.empty_cache()

    del model, tok
    torch.cuda.empty_cache()
    gc.collect()
    log.info(f"GPT-2 Large unloaded, median PPL = {np.nanmedian(ppls):.1f}")
    return np.array(ppls)


# ── Lexical Diversity (MTLD + HD-D) ──

def compute_lexdiv(texts):
    from lexical_diversity import lex_div as ld

    mtld_vals, hdd_vals = [], []
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


# ── N-gram Repetition Rate ──

def compute_ngram_rep(texts, n):
    rates = []
    for text in texts:
        tokens = text.split()
        if len(tokens) < n + 1:
            rates.append(0.0)
            continue
        grams = [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
        freq = Counter(grams)
        repeated = sum(c - 1 for c in freq.values() if c > 1)
        rates.append(repeated / len(grams))
    return np.array(rates)


# ── Zipf Coefficient ──

def compute_zipf(texts):
    coeffs = []
    for text in texts:
        tokens = text.lower().split()
        if len(tokens) < 5:
            coeffs.append(float("nan"))
            continue
        freq = Counter(tokens)
        counts = sorted(freq.values(), reverse=True)
        if len(counts) < 3:
            coeffs.append(float("nan"))
            continue
        ranks = np.arange(1, len(counts) + 1, dtype=float)
        log_r = np.log(ranks)
        log_f = np.log(np.array(counts, dtype=float))
        slope, _, _, _, _ = stats.linregress(log_r, log_f)
        coeffs.append(float(-slope))
    return np.array(coeffs)


# ── Save metrics incrementally ──

def save_metrics(metrics_dict, doc_ids):
    path = OUT_DIR / "cc_quality_independent.csv"
    n = len(doc_ids)
    cols = [c for c in METRIC_COLS if c in metrics_dict]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["doc_id"] + cols)
        for i in range(n):
            row = [doc_ids[i]]
            for c in cols:
                v = metrics_dict[c][i]
                row.append("" if np.isnan(v) else f"{v:.6f}")
            writer.writerow(row)
    log.info(f"Saved {len(cols)} metrics x {n} rows to {path}")


def main():
    t_total = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    os.environ["HF_HOME"] = HF_CACHE
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ.setdefault("REQUESTS_CA_BUNDLE", "/etc/ssl/certs/ca-certificates.crt")
    os.environ.setdefault("SSL_CERT_FILE", "/etc/ssl/certs/ca-certificates.crt")

    log.info("=" * 60)
    log.info("exp-014 v1: Independent Quality Metrics (5K CC docs)")
    log.info("=" * 60)

    texts, doc_ids = load_texts()
    predicted_depths = load_predictions()
    n = len(texts)
    assert len(predicted_depths) == n, f"Mismatch: {n} texts vs {len(predicted_depths)} predictions"

    existing = load_existing_metrics(n)
    needed = [c for c in METRIC_COLS if c not in existing]
    if not needed:
        log.info("All 6 metrics already computed — done")
    else:
        log.info(f"Need to compute: {needed}")

    metrics = dict(existing)

    if "gpt2_ppl" in needed:
        log.info("Computing GPT-2 Large perplexity ...")
        t0 = time.time()
        metrics["gpt2_ppl"] = compute_gpt2_ppl(texts)
        log.info(f"  Done in {time.time()-t0:.0f}s")
        save_metrics(metrics, doc_ids)

    if "mtld" in needed or "hdd" in needed:
        log.info("Computing MTLD + HD-D ...")
        t0 = time.time()
        mtld, hdd = compute_lexdiv(texts)
        if "mtld" in needed:
            metrics["mtld"] = mtld
        if "hdd" in needed:
            metrics["hdd"] = hdd
        log.info(f"  Done in {time.time()-t0:.0f}s")
        save_metrics(metrics, doc_ids)

    if "rep_3gram" in needed:
        log.info("Computing 3-gram repetition rate ...")
        t0 = time.time()
        metrics["rep_3gram"] = compute_ngram_rep(texts, 3)
        log.info(f"  Done in {time.time()-t0:.0f}s")
        save_metrics(metrics, doc_ids)

    if "rep_4gram" in needed:
        log.info("Computing 4-gram repetition rate ...")
        t0 = time.time()
        metrics["rep_4gram"] = compute_ngram_rep(texts, 4)
        log.info(f"  Done in {time.time()-t0:.0f}s")
        save_metrics(metrics, doc_ids)

    if "zipf" in needed:
        log.info("Computing Zipf coefficient ...")
        t0 = time.time()
        metrics["zipf"] = compute_zipf(texts)
        log.info(f"  Done in {time.time()-t0:.0f}s")
        save_metrics(metrics, doc_ids)

    total = time.time() - t_total
    log.info("=" * 60)
    log.info(f"Independent metrics done in {total:.0f}s ({total/3600:.1f}h)")
    for c in METRIC_COLS:
        if c in metrics:
            arr = metrics[c]
            valid = np.sum(~np.isnan(arr))
            log.info(f"  {c}: median={np.nanmedian(arr):.4f}, valid={valid}/{n}")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
