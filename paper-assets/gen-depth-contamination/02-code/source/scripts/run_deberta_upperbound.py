#!/usr/bin/env python3
"""
DeBERTa-v3-base upper-bound baseline: 6-class ordinal depth classification.
5-fold GroupKFold (grouped by doc_id), pairwise AUC with doc-level bootstrap CI, K* determination.
Compares against existing OBD-LightGBM baselines.
"""

import gc
import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup,
)

# ─── Config ────────────────────────────────────────────────────────────────────
ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results" / "exp_deberta_upperbound"

EXPERIMENTS = {
    "wiki_pythia": DATA_DIR / "exp_wiki_pythia",
    "wiki_olmo": DATA_DIR / "exp_wiki_olmo",
    "wiki_qwen7b": DATA_DIR / "exp_wiki_qwen7b",
    "wiki_llama8b": DATA_DIR / "exp_wiki_llama8b",
    "wiki_mistral7b": DATA_DIR / "exp_wiki_mistral7b",
}

MODEL_NAME = "microsoft/deberta-v3-base"
HF_CACHE = "/root/autodl-tmp/.hf_cache"
MAX_LEN = 512
N_CLASSES = 6
N_FOLDS = 5
EPOCHS = 3
BS = 16
GRAD_ACCUM = 2
LR = 2e-5
WARMUP = 0.1
WD = 0.01
N_BOOT = 1000
THETA = 0.60
SEED = 42

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ─── Data ──────────────────────────────────────────────────────────────────────
def load_data(exp_dir):
    texts, labels, doc_ids = [], [], []
    for d in range(N_CLASSES):
        p = exp_dir / f"depth_{d}.jsonl"
        with open(p) as f:
            for line in f:
                obj = json.loads(line)
                texts.append(obj["text"])
                labels.append(d)
                doc_ids.append(obj["doc_id"])
    return texts, np.array(labels), np.array(doc_ids)


class DepthDataset(Dataset):
    def __init__(self, input_ids, attention_masks, labels):
        self.input_ids = input_ids
        self.attention_masks = attention_masks
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        return self.input_ids[i], self.attention_masks[i], self.labels[i]


def collate_fn(batch):
    ids_list, mask_list, lab_list = zip(*batch)
    mx = max(len(x) for x in ids_list)
    bsz = len(ids_list)
    ids = torch.zeros(bsz, mx, dtype=torch.long)
    masks = torch.zeros(bsz, mx, dtype=torch.long)
    for i, (x, m) in enumerate(zip(ids_list, mask_list)):
        n = len(x)
        ids[i, :n] = torch.tensor(x, dtype=torch.long)
        masks[i, :n] = torch.tensor(m, dtype=torch.long)
    labels = torch.tensor(lab_list, dtype=torch.long)
    return ids, masks, labels


# ─── Training ──────────────────────────────────────────────────────────────────
def train_fold(tr_ids, tr_masks, tr_labels, va_ids, va_masks, va_labels, device, fold):
    log.info(f"  Fold {fold}: train={len(tr_labels)}, val={len(va_labels)}")

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, num_labels=N_CLASSES, cache_dir=HF_CACHE,
        local_files_only=True, torch_dtype=torch.float32,
    ).to(device)

    tr_ds = DepthDataset(tr_ids, tr_masks, tr_labels)
    va_ds = DepthDataset(va_ids, va_masks, va_labels)
    tr_dl = DataLoader(
        tr_ds, batch_size=BS, shuffle=True,
        collate_fn=collate_fn, num_workers=2, pin_memory=True,
    )
    va_dl = DataLoader(
        va_ds, batch_size=BS * 2,
        collate_fn=collate_fn, num_workers=2, pin_memory=True,
    )

    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WD)
    total_opt_steps = (len(tr_dl) // GRAD_ACCUM) * EPOCHS
    sched = get_linear_schedule_with_warmup(opt, int(total_opt_steps * WARMUP), total_opt_steps)

    model.train()
    for ep in range(EPOCHS):
        ep_loss = 0.0
        opt.zero_grad()
        for step, (ids, mask, lab) in enumerate(tr_dl):
            ids, mask, lab = ids.to(device), mask.to(device), lab.to(device)
            out = model(input_ids=ids, attention_mask=mask, labels=lab)
            (out.loss / GRAD_ACCUM).backward()
            ep_loss += out.loss.item()
            if (step + 1) % GRAD_ACCUM == 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                opt.step()
                sched.step()
                opt.zero_grad()
            if step % 200 == 0 and step > 0:
                log.info(f"    Ep {ep+1} step {step}/{len(tr_dl)} loss={ep_loss/(step+1):.4f}")
        log.info(f"    Ep {ep+1}/{EPOCHS} avg_loss={ep_loss/len(tr_dl):.4f}")

    model.eval()
    probs_all = []
    with torch.no_grad():
        for ids, mask, _ in va_dl:
            ids, mask = ids.to(device), mask.to(device)
            out = model(input_ids=ids, attention_mask=mask)
            probs_all.append(torch.softmax(out.logits, dim=-1).cpu().numpy())

    del model, opt, sched
    torch.cuda.empty_cache()
    gc.collect()
    return np.concatenate(probs_all)


# ─── Evaluation ────────────────────────────────────────────────────────────────
def pairwise_auc_ci(labels, probs, doc_ids):
    rng = np.random.RandomState(SEED)
    results = {}

    for k in range(N_CLASSES - 1):
        key = f"{k}v{k+1}"
        mask = (labels == k) | (labels == k + 1)
        y = (labels[mask] == k + 1).astype(int)
        s = probs[mask][:, k + 1 :].sum(axis=1)
        docs = doc_ids[mask]

        auc = float(roc_auc_score(y, s))

        doc2idx = {}
        for i, d in enumerate(docs):
            doc2idx.setdefault(int(d), []).append(i)
        uq = list(doc2idx.keys())
        idx_arr = [np.array(v) for v in doc2idx.values()]
        n_docs = len(uq)

        boots = []
        for _ in range(N_BOOT):
            si = rng.randint(0, n_docs, n_docs)
            idx = np.concatenate([idx_arr[j] for j in si])
            try:
                boots.append(roc_auc_score(y[idx], s[idx]))
            except ValueError:
                continue
        boots = np.array(boots)
        ci_lo = float(np.percentile(boots, 2.5))
        ci_hi = float(np.percentile(boots, 97.5))

        results[key] = {
            "auc": round(auc, 4),
            "ci_lower": round(ci_lo, 4),
            "ci_upper": round(ci_hi, 4),
            "ci_lower_above_theta": bool(ci_lo > THETA),
            "boot_mean": round(float(boots.mean()), 4),
            "boot_std": round(float(boots.std()), 4),
        }

    kstar = -1
    for k in range(N_CLASSES - 1):
        if results[f"{k}v{k+1}"]["ci_lower_above_theta"]:
            kstar = k
        else:
            break
    return results, kstar


def load_obd(name):
    p = ROOT / "results" / f"exp_{name}" / "pairwise_auc.json"
    if p.exists():
        with open(p) as f:
            data = json.load(f)
        return data.get("mean", data)
    return None


# ─── Main ──────────────────────────────────────────────────────────────────────
def main():
    os.environ["HF_HOME"] = HF_CACHE
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

    device = torch.device("cuda:0")
    log.info(f"Device: {device} ({torch.cuda.get_device_name(0)})")

    log.info(f"Loading tokenizer: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE, use_fast=False, local_files_only=True)
    log.info("Tokenizer loaded")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    all_res = {}

    for exp_name, exp_dir in EXPERIMENTS.items():
        log.info(f"\n{'='*60}\n{exp_name}\n{'='*60}")
        t0 = time.time()

        texts, labels, doc_ids = load_data(exp_dir)
        N = len(texts)
        log.info(f"Loaded {N} samples ({N // N_CLASSES} docs x {N_CLASSES} depths)")

        log.info("Tokenizing...")
        enc = tokenizer(texts, truncation=True, max_length=MAX_LEN, padding=False)
        all_ids = enc["input_ids"]
        all_masks = enc["attention_mask"]

        gkf = GroupKFold(n_splits=N_FOLDS)
        oof = np.zeros((N, N_CLASSES))

        for fi, (tr_i, va_i) in enumerate(gkf.split(np.arange(N), labels, doc_ids)):
            tr_ids_f = [all_ids[i] for i in tr_i]
            tr_masks_f = [all_masks[i] for i in tr_i]
            va_ids_f = [all_ids[i] for i in va_i]
            va_masks_f = [all_masks[i] for i in va_i]

            oof[va_i] = train_fold(
                tr_ids_f, tr_masks_f, labels[tr_i].tolist(),
                va_ids_f, va_masks_f, labels[va_i].tolist(),
                device, fi,
            )

        pw, kstar = pairwise_auc_ci(labels, oof, doc_ids)
        elapsed = time.time() - t0

        log.info(f"\nPairwise AUC ({exp_name}):")
        for pair_key, v in pw.items():
            log.info(f"  {pair_key}: {v['auc']:.4f} [{v['ci_lower']:.4f}, {v['ci_upper']:.4f}]")
        log.info(f"  K* (theta={THETA}): {kstar}")
        log.info(f"  Time: {elapsed:.0f}s")

        obd = load_obd(exp_name)
        exp_res = {
            "experiment": exp_name,
            "model": MODEL_NAME,
            "method": "DeBERTa-v3-base fine-tuned 6-class",
            "n_samples": N,
            "epochs": EPOCHS,
            "lr": LR,
            "batch_size": BS,
            "max_length": MAX_LEN,
            "theta": THETA,
            "kstar": kstar,
            "pairwise_auc": pw,
            "elapsed_seconds": round(elapsed, 1),
        }
        if obd:
            exp_res["obd_baseline"] = obd

        all_res[exp_name] = exp_res
        with open(RESULTS_DIR / f"{exp_name}.json", "w") as f:
            json.dump(exp_res, f, indent=2)
        log.info(f"Saved: {RESULTS_DIR / f'{exp_name}.json'}")

    with open(RESULTS_DIR / "summary.json", "w") as f:
        json.dump(all_res, f, indent=2)

    # Comparison table
    log.info(f"\n{'='*80}")
    log.info("DeBERTa vs OBD-LightGBM Comparison")
    log.info(f"{'='*80}")
    hdr = f"{'Experiment':<18} {'Pair':<6} {'DeBERTa':>8} {'CI_lo':>7} {'CI_hi':>7} {'OBD':>7} {'Delta':>7}"
    log.info(hdr)
    log.info("-" * len(hdr))
    for name, r in all_res.items():
        obd = r.get("obd_baseline", {})
        for pk in ["0v1", "1v2", "2v3", "3v4", "4v5"]:
            da = r["pairwise_auc"][pk]["auc"]
            cl = r["pairwise_auc"][pk]["ci_lower"]
            ch = r["pairwise_auc"][pk]["ci_upper"]
            oa = obd.get(pk)
            d_str = f"{da - oa:+.4f}" if oa else "   N/A"
            o_str = f"{oa:.4f}" if oa else "   N/A"
            log.info(f"{name:<18} {pk:<6} {da:>8.4f} {cl:>7.4f} {ch:>7.4f} {o_str:>7} {d_str:>7}")
        log.info(f"  => K*(DeBERTa)={r['kstar']}")
        log.info("-" * len(hdr))

    log.info("All done.")


if __name__ == "__main__":
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)
    main()
