#!/usr/bin/env python3
"""Generate per-document depth predictions using DeBERTa and OBD (LightGBM).

Retrains DeBERTa-v3-base 5-fold on arXiv data, collects OOF logits.
Trains 6-class LightGBM on 15D OBD features, collects OOF probabilities.
Saves predictions.npz for exp_deberta_filtering_comparison.

Usage:
    python scripts/exp_deberta_filtering_predict.py --device cuda:1
"""

import argparse
import gc
import json
import logging
import os
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import GroupKFold
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup,
)
import lightgbm as lgb

ROOT = Path("/root/autodl-tmp/gen-depth-contamination")
DATA_DIR = ROOT / "data" / "exp_024_arxiv"
OUT_DIR = ROOT / "results" / "exp_deberta_filtering_comparison"

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
SEED = 42

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def load_data(exp_dir):
    texts, labels, doc_ids = [], [], []
    for d in range(N_CLASSES):
        with open(exp_dir / f"depth_{d}.jsonl") as f:
            for line in f:
                obj = json.loads(line)
                texts.append(obj["text"])
                labels.append(d)
                doc_ids.append(obj["doc_id"])
    return texts, np.array(labels), np.array(doc_ids)


class DS(Dataset):
    def __init__(self, ids, masks, labels):
        self.ids, self.masks, self.labels = ids, masks, labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, i):
        return self.ids[i], self.masks[i], self.labels[i]


def collate(batch):
    ids_l, mask_l, lab_l = zip(*batch)
    mx = max(len(x) for x in ids_l)
    bsz = len(ids_l)
    ids = torch.zeros(bsz, mx, dtype=torch.long)
    masks = torch.zeros(bsz, mx, dtype=torch.long)
    for i, (x, m) in enumerate(zip(ids_l, mask_l)):
        n = len(x)
        ids[i, :n] = torch.tensor(x, dtype=torch.long)
        masks[i, :n] = torch.tensor(m, dtype=torch.long)
    return ids, masks, torch.tensor(lab_l, dtype=torch.long)


def train_fold(tr_ids, tr_masks, tr_labels, va_ids, va_masks, va_labels, device, fold):
    log.info(f"  Fold {fold}: train={len(tr_labels)}, val={len(va_labels)}")
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=N_CLASSES,
        cache_dir=HF_CACHE,
        local_files_only=True,
        torch_dtype=torch.float32,
    ).to(device)

    tr_dl = DataLoader(
        DS(tr_ids, tr_masks, tr_labels),
        batch_size=BS,
        shuffle=True,
        collate_fn=collate,
        num_workers=2,
        pin_memory=True,
    )
    va_dl = DataLoader(
        DS(va_ids, va_masks, va_labels),
        batch_size=BS * 2,
        collate_fn=collate,
        num_workers=2,
        pin_memory=True,
    )

    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WD)
    total_opt = (len(tr_dl) // GRAD_ACCUM) * EPOCHS
    sched = get_linear_schedule_with_warmup(opt, int(total_opt * WARMUP), total_opt)

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
        log.info(f"    Ep {ep+1}/{EPOCHS} avg_loss={ep_loss / len(tr_dl):.4f}")

    model.eval()
    all_logits = []
    with torch.no_grad():
        for ids, mask, lab in va_dl:
            ids, mask = ids.to(device), mask.to(device)
            logits = model(input_ids=ids, attention_mask=mask).logits
            all_logits.append(logits.cpu().numpy())

    del model, opt, sched, tr_dl, va_dl
    torch.cuda.empty_cache()
    gc.collect()

    return np.concatenate(all_logits)


def run_deberta_predictions(device):
    log.info("=== DeBERTa Prediction Phase ===")
    os.environ["HF_HOME"] = HF_CACHE
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

    texts, labels, doc_ids = load_data(DATA_DIR)
    N = len(texts)
    log.info(f"Loaded {N} samples")

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME, cache_dir=HF_CACHE, use_fast=False, local_files_only=True
    )
    enc = tokenizer(texts, truncation=True, max_length=MAX_LEN, padding=False)
    all_ids, all_masks = enc["input_ids"], enc["attention_mask"]

    gkf = GroupKFold(n_splits=N_FOLDS)
    oof = np.zeros((N, N_CLASSES))

    for fi, (tr_i, va_i) in enumerate(gkf.split(np.arange(N), labels, doc_ids)):
        oof[va_i] = train_fold(
            [all_ids[i] for i in tr_i],
            [all_masks[i] for i in tr_i],
            labels[tr_i].tolist(),
            [all_ids[i] for i in va_i],
            [all_masks[i] for i in va_i],
            labels[va_i].tolist(),
            device,
            fi,
        )

    deberta_preds = np.argmax(oof, axis=1)
    log.info(
        f"DeBERTa pred distribution: {np.bincount(deberta_preds, minlength=N_CLASSES).tolist()}"
    )
    log.info(f"DeBERTa accuracy: {np.mean(deberta_preds == labels):.4f}")
    return deberta_preds, oof, labels, doc_ids


def run_obd_predictions():
    log.info("=== OBD (LightGBM) Prediction Phase ===")
    df = pd.read_csv(DATA_DIR / "features.csv")
    feature_cols = [c for c in df.columns if c not in ("doc_id", "depth")]
    X = df[feature_cols].values
    y = df["depth"].values
    doc_ids = df["doc_id"].values

    gkf = GroupKFold(n_splits=N_FOLDS)
    oof_probs = np.zeros((len(y), N_CLASSES))

    for fi, (tr_i, va_i) in enumerate(gkf.split(np.arange(len(y)), y, doc_ids)):
        clf = lgb.LGBMClassifier(
            objective="multiclass",
            num_class=N_CLASSES,
            learning_rate=0.1,
            num_leaves=31,
            min_child_samples=20,
            n_estimators=200,
            verbose=-1,
            random_state=SEED,
        )
        clf.fit(X[tr_i], y[tr_i])
        oof_probs[va_i] = clf.predict_proba(X[va_i])
        log.info(f"  Fold {fi}: train={len(tr_i)}, val={len(va_i)}")

    obd_preds = np.argmax(oof_probs, axis=1)
    log.info(
        f"OBD pred distribution: {np.bincount(obd_preds, minlength=N_CLASSES).tolist()}"
    )
    log.info(f"OBD accuracy: {np.mean(obd_preds == y):.4f}")
    return obd_preds, oof_probs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:1")
    args = parser.parse_args()

    device = torch.device(args.device)
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    t0 = time.time()

    deberta_preds, deberta_probs, true_depths, doc_ids = run_deberta_predictions(
        device
    )
    obd_preds, obd_probs = run_obd_predictions()

    out_path = OUT_DIR / "predictions.npz"
    np.savez(
        out_path,
        doc_ids=doc_ids,
        true_depths=true_depths,
        deberta_preds=deberta_preds,
        deberta_probs=deberta_probs,
        obd_preds=obd_preds,
        obd_probs=obd_probs,
    )
    log.info(f"Saved predictions to {out_path}")

    elapsed = time.time() - t0
    log.info(f"\n=== Summary (elapsed {elapsed:.0f}s) ===")
    for d in range(N_CLASSES):
        mask = true_depths == d
        n = mask.sum()
        deb_acc = np.mean(deberta_preds[mask] == d)
        obd_acc = np.mean(obd_preds[mask] == d)
        log.info(
            f"  Depth {d} (n={n}): DeBERTa recall={deb_acc:.3f}, OBD recall={obd_acc:.3f}"
        )
    log.info(f"Overall DeBERTa acc={np.mean(deberta_preds == true_depths):.4f}")
    log.info(f"Overall OBD acc={np.mean(obd_preds == true_depths):.4f}")
    log.info("Done.")


if __name__ == "__main__":
    main()
