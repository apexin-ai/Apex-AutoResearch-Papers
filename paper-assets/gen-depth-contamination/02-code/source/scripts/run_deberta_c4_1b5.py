#!/usr/bin/env python3
"""
DeBERTa-v3-base on C4 1.5B-scale rewrite data: 6-class depth classification.
5-fold GroupKFold, pairwise AUC with doc-level bootstrap CI, K* determination.
Designed to run one config per GPU.
"""

import argparse
import gc
import json
import logging
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
from torch.cuda.amp import GradScaler, autocast
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score, f1_score

ROOT = Path("/root/autodl-tmp/gen-depth-contamination")

EXPERIMENTS = {
    "qwen_rw": ROOT / "data_exp016_qwen_base",
    "pythia_greedy": ROOT / "data_exp020_pythia_greedy",
    "qwen_cont256": ROOT / "data" / "exp_021_length_256",
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
N_BOOT = 10000
THETA = 0.60
SEED = 42

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


# ─── Data ─────────────────────────────────────────────────────────────────────
def load_data(exp_dir):
    texts, labels, doc_ids = [], [], []
    for d in range(N_CLASSES):
        p = exp_dir / f"depth_{d}.jsonl"
        if not p.exists():
            log.error(f"Missing: {p}")
            sys.exit(1)
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


# ─── Training ─────────────────────────────────────────────────────────────────
def train_fold(tr_ids, tr_masks, tr_labels, va_ids, va_masks, va_labels, device, fold):
    log.info(f"  Fold {fold}: train={len(tr_labels)}, val={len(va_labels)}")

    from transformers import AutoModelForSequenceClassification, get_linear_schedule_with_warmup

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
    scaler = GradScaler()

    model.train()
    for ep in range(EPOCHS):
        ep_loss = 0.0
        opt.zero_grad()
        for step, (ids, mask, lab) in enumerate(tr_dl):
            ids, mask, lab = ids.to(device), mask.to(device), lab.to(device)
            with autocast(dtype=torch.float16):
                out = model(input_ids=ids, attention_mask=mask, labels=lab)
                loss = out.loss / GRAD_ACCUM
            scaler.scale(loss).backward()
            ep_loss += out.loss.item()
            if (step + 1) % GRAD_ACCUM == 0:
                scaler.unscale_(opt)
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                scaler.step(opt)
                scaler.update()
                sched.step()
                opt.zero_grad()
            if step % 200 == 0 and step > 0:
                log.info(f"    Ep {ep+1} step {step}/{len(tr_dl)} loss={ep_loss/(step+1):.4f}")
        log.info(f"    Ep {ep+1}/{EPOCHS} avg_loss={ep_loss/len(tr_dl):.4f}")

    model.eval()
    probs_all = []
    with torch.no_grad(), autocast(dtype=torch.float16):
        for ids, mask, _ in va_dl:
            ids, mask = ids.to(device), mask.to(device)
            out = model(input_ids=ids, attention_mask=mask)
            probs_all.append(torch.softmax(out.logits.float(), dim=-1).cpu().numpy())

    del model, opt, sched, scaler
    torch.cuda.empty_cache()
    gc.collect()
    return np.concatenate(probs_all)


# ─── Evaluation ───────────────────────────────────────────────────────────────
def pairwise_auc_ci(labels, probs, doc_ids):
    rng = np.random.RandomState(SEED)
    results = {}

    for k in range(N_CLASSES - 1):
        key = f"{k}v{k+1}"
        mask = (labels == k) | (labels == k + 1)
        y = (labels[mask] == k + 1).astype(int)
        s = probs[mask][:, k + 1:].sum(axis=1)
        docs = doc_ids[mask]

        auc = float(roc_auc_score(y, s))

        # F1@0.50
        preds = (s >= 0.50).astype(int)
        f1 = float(f1_score(y, preds))

        doc2idx = {}
        for i, d in enumerate(docs):
            doc2idx.setdefault(int(d), []).append(i)
        idx_arr = [np.array(v) for v in doc2idx.values()]
        n_docs = len(idx_arr)

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
            "f1_at_050": round(f1, 4),
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


def find_lgbm_baseline(config_name):
    """Try to locate LightGBM pairwise AUC results for comparison."""
    candidates = [
        ROOT / "results" / f"exp_{config_name}" / "pairwise_auc.json",
        ROOT / "results" / f"exp_{config_name}" / "results.json",
        ROOT / "results" / f"exp_{config_name}" / "summary.json",
    ]
    # Also check experiment-specific dirs
    exp_map = {
        "qwen_rw": ["exp016", "exp_016", "exp016_qwen_base"],
        "pythia_greedy": ["exp020", "exp_020", "exp020_pythia_greedy"],
        "qwen_cont256": ["exp021", "exp_021", "exp021_length_256"],
    }
    for tag in exp_map.get(config_name, []):
        candidates.append(ROOT / "results" / tag / "pairwise_auc.json")
        candidates.append(ROOT / "results" / tag / "results.json")

    for p in candidates:
        if p.exists():
            try:
                with open(p) as f:
                    data = json.load(f)
                return data.get("mean", data.get("pairwise_auc", data))
            except (json.JSONDecodeError, KeyError):
                continue
    return None


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="DeBERTa C4 1.5B depth classification")
    parser.add_argument("--config", required=True, choices=list(EXPERIMENTS.keys()))
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default=str(ROOT / "results" / "exp_deberta_c4_1b5"))
    parser.add_argument("--dry_run", action="store_true", help="Load data + model + 1 batch, then exit")
    args = parser.parse_args()

    os.environ["HF_HOME"] = HF_CACHE
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_XET"] = "1"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

    device = torch.device(f"cuda:{args.gpu}")
    log.info(f"Device: {device} ({torch.cuda.get_device_name(args.gpu)})")

    exp_dir = EXPERIMENTS[args.config]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    log.info(f"Config: {args.config}")
    log.info(f"Data: {exp_dir}")

    from transformers import AutoTokenizer
    log.info(f"Loading tokenizer: {MODEL_NAME}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE, use_fast=False, local_files_only=True)
    log.info("Tokenizer loaded")

    texts, labels, doc_ids = load_data(exp_dir)
    N = len(texts)
    log.info(f"Loaded {N} samples ({N // N_CLASSES} docs x {N_CLASSES} depths)")

    log.info("Tokenizing...")
    enc = tokenizer(texts, truncation=True, max_length=MAX_LEN, padding=False)
    all_ids = enc["input_ids"]
    all_masks = enc["attention_mask"]
    log.info("Tokenization done")

    if args.dry_run:
        log.info("=== DRY RUN: testing model load + 1 batch ===")
        from transformers import AutoModelForSequenceClassification
        model = AutoModelForSequenceClassification.from_pretrained(
            MODEL_NAME, num_labels=N_CLASSES, cache_dir=HF_CACHE,
            local_files_only=True, torch_dtype=torch.float32,
        ).to(device)
        batch_ids = [all_ids[i] for i in range(BS)]
        batch_masks = [all_masks[i] for i in range(BS)]
        batch_labels = labels[:BS].tolist()
        ds = DepthDataset(batch_ids, batch_masks, batch_labels)
        dl = DataLoader(ds, batch_size=BS, collate_fn=collate_fn)
        ids, mask, lab = next(iter(dl))
        ids, mask, lab = ids.to(device), mask.to(device), lab.to(device)
        with autocast(dtype=torch.float16):
            out = model(input_ids=ids, attention_mask=mask, labels=lab)
        log.info(f"Forward pass OK: loss={out.loss.item():.4f}, logits shape={out.logits.shape}")
        del model
        torch.cuda.empty_cache()
        log.info("=== DRY RUN PASSED ===")
        return

    t0 = time.time()
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

    elapsed = time.time() - t0

    # Save raw OOF predictions
    npz_path = output_dir / f"{args.config}_oof.npz"
    np.savez(npz_path, doc_ids=doc_ids, true_depth=labels, pred_probs=oof)
    log.info(f"Saved OOF: {npz_path}")

    # Evaluate
    pw, kstar = pairwise_auc_ci(labels, oof, doc_ids)

    log.info(f"\nPairwise AUC ({args.config}):")
    for pair_key, v in pw.items():
        log.info(f"  {pair_key}: AUC={v['auc']:.4f} [{v['ci_lower']:.4f}, {v['ci_upper']:.4f}]  F1@0.5={v['f1_at_050']:.4f}")
    log.info(f"  K* (theta={THETA}): {kstar}")
    log.info(f"  Time: {elapsed:.0f}s")

    # LightGBM comparison
    lgbm = find_lgbm_baseline(args.config)

    exp_res = {
        "experiment": args.config,
        "model": MODEL_NAME,
        "method": "DeBERTa-v3-base fine-tuned 6-class (fp16)",
        "n_samples": N,
        "n_docs": N // N_CLASSES,
        "epochs": EPOCHS,
        "lr": LR,
        "batch_size": BS,
        "grad_accum": GRAD_ACCUM,
        "max_length": MAX_LEN,
        "n_folds": N_FOLDS,
        "n_bootstrap": N_BOOT,
        "theta": THETA,
        "kstar": kstar,
        "pairwise_auc": pw,
        "elapsed_seconds": round(elapsed, 1),
    }
    if lgbm:
        exp_res["lgbm_baseline"] = lgbm

    json_path = output_dir / f"{args.config}.json"
    with open(json_path, "w") as f:
        json.dump(exp_res, f, indent=2)
    log.info(f"Saved: {json_path}")

    # Comparison table
    log.info(f"\n{'='*80}")
    log.info(f"DeBERTa vs LightGBM — {args.config}")
    log.info(f"{'='*80}")
    hdr = f"{'Pair':<6} {'DeBERTa':>8} {'CI_lo':>7} {'CI_hi':>7} {'F1@.5':>7} {'LGBM':>7} {'Delta':>7}"
    log.info(hdr)
    log.info("-" * len(hdr))
    for pk in ["0v1", "1v2", "2v3", "3v4", "4v5"]:
        da = pw[pk]["auc"]
        cl = pw[pk]["ci_lower"]
        ch = pw[pk]["ci_upper"]
        f1 = pw[pk]["f1_at_050"]
        if lgbm and pk in lgbm:
            oa = lgbm[pk] if isinstance(lgbm[pk], (int, float)) else lgbm[pk].get("auc", lgbm[pk])
            o_str = f"{oa:.4f}"
            d_str = f"{da - oa:+.4f}"
        else:
            o_str = "   N/A"
            d_str = "   N/A"
        log.info(f"{pk:<6} {da:>8.4f} {cl:>7.4f} {ch:>7.4f} {f1:>7.4f} {o_str:>7} {d_str:>7}")
    log.info(f"  => K*(DeBERTa)={kstar}")
    log.info("Done.")


if __name__ == "__main__":
    torch.manual_seed(SEED)
    np.random.seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)
    main()
