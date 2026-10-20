"""
DeBERTa-v3-base ordinal classifier on C4 depth chains (upper-bound baseline).
5-fold GroupKFold, pairwise AUC + bootstrap CI + F1@0.50 + K*.
"""

import json
import os
import gc
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.amp
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import GroupKFold
from sklearn.metrics import roc_auc_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, get_linear_schedule_with_warmup

os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

BASE_DIR = Path("/root/autodl-tmp/gen-depth-contamination")
DEVICE = torch.device("cuda:0")

MODEL_PATHS = [
    "/root/autodl-tmp/.hf_cache/microsoft/deberta-v3-base",
    "microsoft/deberta-v3-base",
]

EXPERIMENTS = {
    "exp_14b_c4": BASE_DIR / "data" / "exp_14b_c4",
    "exp_32b_c4": BASE_DIR / "data" / "exp_32b_c4",
}

LR = 2e-5
BATCH_SIZE = 16
EPOCHS = 3
WARMUP_RATIO = 0.1
WEIGHT_DECAY = 0.01
MAX_LENGTH = 512
N_FOLDS = 5
N_BOOTSTRAP = 10_000
THETA = 0.60
SEED = 42


def resolve_model_path():
    for p in MODEL_PATHS:
        if Path(p).is_dir() and (Path(p) / "config.json").exists():
            print(f"Using local model: {p}")
            return p
    print(f"Using HuggingFace hub: {MODEL_PATHS[-1]}")
    return MODEL_PATHS[-1]


class DepthDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx], truncation=True, max_length=self.max_length,
            padding="max_length", return_tensors="pt",
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long),
        }


def load_depth_data(data_dir):
    texts, depths, doc_ids = [], [], []
    depth_files = sorted(data_dir.glob("depth_*.jsonl"))
    for fpath in depth_files:
        depth = int(fpath.stem.split("_")[1])
        with open(fpath) as f:
            for line in f:
                rec = json.loads(line)
                texts.append(rec["text"])
                depths.append(depth)
                doc_ids.append(rec["doc_id"])
    return texts, np.array(depths), np.array(doc_ids)


def train_one_fold(train_texts, train_labels, val_texts, val_labels,
                   num_classes, tokenizer, model_path):
    train_ds = DepthDataset(train_texts, train_labels, tokenizer, MAX_LENGTH)
    val_ds = DepthDataset(val_texts, val_labels, tokenizer, MAX_LENGTH)
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True,
                              num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE * 2, shuffle=False,
                            num_workers=4, pin_memory=True)

    model = AutoModelForSequenceClassification.from_pretrained(
        model_path, num_labels=num_classes
    ).to(DEVICE)

    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    total_steps = len(train_loader) * EPOCHS
    warmup_steps = int(total_steps * WARMUP_RATIO)
    scheduler = get_linear_schedule_with_warmup(optimizer, warmup_steps, total_steps)
    scaler = torch.amp.GradScaler("cuda")

    for epoch in range(EPOCHS):
        model.train()
        total_loss, n_batches = 0.0, 0
        t0 = time.time()
        for batch in train_loader:
            optimizer.zero_grad()
            with torch.amp.autocast("cuda"):
                outputs = model(
                    input_ids=batch["input_ids"].to(DEVICE),
                    attention_mask=batch["attention_mask"].to(DEVICE),
                    labels=batch["labels"].to(DEVICE),
                )
            scaler.scale(outputs.loss).backward()
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            scaler.step(optimizer)
            scaler.update()
            scheduler.step()
            total_loss += outputs.loss.item()
            n_batches += 1
        elapsed = time.time() - t0
        print(f"    Epoch {epoch+1}/{EPOCHS}  loss={total_loss/n_batches:.4f}  "
              f"time={elapsed:.0f}s  lr={scheduler.get_last_lr()[0]:.2e}")

    model.eval()
    all_probs = []
    with torch.no_grad():
        for batch in val_loader:
            with torch.amp.autocast("cuda"):
                outputs = model(
                    input_ids=batch["input_ids"].to(DEVICE),
                    attention_mask=batch["attention_mask"].to(DEVICE),
                )
            probs = torch.softmax(outputs.logits.float(), dim=-1).cpu().numpy()
            all_probs.append(probs)

    del model, optimizer, scheduler, scaler
    gc.collect()
    torch.cuda.empty_cache()
    return np.concatenate(all_probs, axis=0)


def doc_bootstrap_auc(doc_ids, y_true, scores, n_bootstrap, rng):
    unique_docs = np.unique(doc_ids)
    doc_to_idx = {d: np.where(doc_ids == d)[0] for d in unique_docs}
    aucs = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        sampled = rng.choice(unique_docs, size=len(unique_docs), replace=True)
        idx = np.concatenate([doc_to_idx[d] for d in sampled])
        y_b, s_b = y_true[idx], scores[idx]
        if len(np.unique(y_b)) < 2:
            aucs[i] = np.nan
        else:
            aucs[i] = roc_auc_score(y_b, s_b)
    return aucs[~np.isnan(aucs)]


def pairwise_analysis(depths, doc_ids, oof_probs, num_classes, rng):
    max_depth = num_classes - 1
    results = {}

    for k in range(max_depth):
        pair = f"{k}v{k+1}"
        mask = (depths == k) | (depths == k + 1)
        d_sub, did_sub, probs_sub = depths[mask], doc_ids[mask], oof_probs[mask]

        binary_score = probs_sub[:, k+1:].sum(axis=1)
        y_binary = (d_sub == k + 1).astype(int)

        if len(np.unique(y_binary)) < 2:
            continue

        auc = roc_auc_score(y_binary, binary_score)
        boot_aucs = doc_bootstrap_auc(did_sub, y_binary, binary_score, n_bootstrap=N_BOOTSTRAP, rng=rng)
        ci_lo = float(np.percentile(boot_aucs, 2.5))
        ci_hi = float(np.percentile(boot_aucs, 97.5))

        pred_binary = (binary_score >= 0.50).astype(int)
        f1 = f1_score(y_binary, pred_binary)

        results[pair] = {
            "auc": round(auc, 4),
            "ci_lower": round(ci_lo, 4),
            "ci_upper": round(ci_hi, 4),
            "f1_at_050": round(f1, 4),
            "n_samples": int(mask.sum()),
        }
        print(f"  {pair}: AUC={auc:.4f} [{ci_lo:.4f}, {ci_hi:.4f}]  F1@0.50={f1:.4f}")

    k_star = -1
    for k in range(max_depth):
        pair = f"{k}v{k+1}"
        if pair in results and results[pair]["ci_lower"] > THETA:
            k_star = k
        else:
            break

    return results, k_star


def main():
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    model_path = resolve_model_path()
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    results_dir = BASE_DIR / "results" / "exp_deberta_c4"
    results_dir.mkdir(parents=True, exist_ok=True)

    summary = {}

    for exp_name, data_dir in EXPERIMENTS.items():
        print(f"\n{'='*70}")
        print(f"  Config: {exp_name}")
        print(f"{'='*70}")

        if not data_dir.exists():
            print(f"  SKIP: {data_dir} not found")
            continue

        texts, depths, doc_ids = load_depth_data(data_dir)
        num_classes = int(depths.max()) + 1
        n_docs = len(np.unique(doc_ids))
        print(f"  Samples={len(texts)}  classes={num_classes} (depth 0-{num_classes-1})  docs={n_docs}")

        gkf = GroupKFold(n_splits=N_FOLDS)
        oof_probs = np.zeros((len(texts), num_classes))
        rng = np.random.default_rng(SEED)

        t_start = time.time()
        for fold, (train_idx, val_idx) in enumerate(gkf.split(texts, depths, groups=doc_ids)):
            print(f"\n  Fold {fold+1}/{N_FOLDS}  train={len(train_idx)} val={len(val_idx)}")
            fold_probs = train_one_fold(
                [texts[i] for i in train_idx], depths[train_idx].tolist(),
                [texts[i] for i in val_idx], depths[val_idx].tolist(),
                num_classes, tokenizer, model_path,
            )
            oof_probs[val_idx] = fold_probs

        train_time = time.time() - t_start
        print(f"\n  Training done in {train_time/60:.1f} min")

        npz_path = results_dir / f"{exp_name}_oof.npz"
        np.savez(npz_path, doc_ids=doc_ids, depths=depths, oof_probs=oof_probs)
        print(f"  OOF saved: {npz_path}")

        print(f"\n  Pairwise analysis (bootstrap={N_BOOTSTRAP}):")
        pairwise, k_star = pairwise_analysis(depths, doc_ids, oof_probs, num_classes, rng)

        config_result = {
            "config": exp_name,
            "n_samples": len(texts),
            "num_classes": num_classes,
            "n_docs": n_docs,
            "train_time_min": round(train_time / 60, 1),
            "pairwise": pairwise,
            "k_star": k_star,
            "hyperparams": {
                "model": "microsoft/deberta-v3-base",
                "lr": LR, "batch_size": BATCH_SIZE, "epochs": EPOCHS,
                "warmup_ratio": WARMUP_RATIO, "weight_decay": WEIGHT_DECAY,
                "max_length": MAX_LENGTH, "n_folds": N_FOLDS,
                "n_bootstrap": N_BOOTSTRAP, "theta": THETA, "seed": SEED,
            },
        }

        json_path = results_dir / f"{exp_name}_results.json"
        with open(json_path, "w") as f:
            json.dump(config_result, f, indent=2)
        print(f"  Results: {json_path}")
        summary[exp_name] = config_result

    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"{'Config':<15} {'Depths':>6} {'Samples':>8} {'K*':>4} {'Time':>7}  Pairwise AUCs")
    print("-" * 90)
    for name, res in summary.items():
        pw = res["pairwise"]
        auc_str = "  ".join(f"{k}:{v['auc']:.3f}" for k, v in sorted(pw.items()))
        print(f"{name:<15} {res['num_classes']:>6} {res['n_samples']:>8} {res['k_star']:>4} "
              f"{res['train_time_min']:>5.1f}m  {auc_str}")

    summary_path = results_dir / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nFull summary: {summary_path}")


if __name__ == "__main__":
    main()
