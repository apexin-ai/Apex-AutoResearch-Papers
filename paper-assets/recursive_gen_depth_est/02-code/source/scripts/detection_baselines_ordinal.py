"""
Ordinal depth resolution analysis for Binoculars / Fast-DetectGPT baselines.

Extends detection_baselines.py with:
  - Pairwise AUC (binary RF on adjacent depth pairs)
  - Monotonicity (Spearman rho)
  - Isotonic regression calibration
  - d0-binary accuracy
  - Per-depth score distributions

Usage:
  python scripts/detection_baselines_ordinal.py --gpu 0 --pilot
  python scripts/detection_baselines_ordinal.py --gpu 0  # all 9 cells
"""

import argparse
import json
import os
import time
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from sklearn.linear_model import LogisticRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score
from scipy.stats import spearmanr

GRID_CELLS = {
    "pythia_nucleus": "data/",
    "pythia_temp09": "data/pythia_temp09/",
    "pythia_topk50": "data/pythia_topk50/",
    "olmo_nucleus": "data/olmo/",
    "olmo_temp09": "data/olmo_temp09/",
    "olmo_topk50": "data/olmo_topk50/",
    "gpt2xl_nucleus": "data/gpt2xl/",
    "gpt2xl_temp09": "data/gpt2xl_temp09/",
    "gpt2xl_topk50": "data/gpt2xl_topk50/",
}

MODEL_PATHS = {
    "gpt2xl": "/root/autodl-tmp/models/gpt2-xl",
    "pythia": "/root/autodl-tmp/models/pythia-1.4b",
}

NUM_DEPTHS = 4
MAX_SEQ_LEN = 512
DEFAULT_BATCH_SIZE = 16

RF_REFERENCE = {
    "pythia_nucleus":  {"acc": 0.787, "d0v1": 0.999, "d1v2": 0.895, "d2v3": 0.760},
    "pythia_temp09":   {"acc": 0.768},
    "pythia_topk50":   {"acc": 0.689},
    "olmo_nucleus":    {"acc": 0.789},
    "olmo_temp09":     {"acc": 0.823},
    "olmo_topk50":     {"acc": 0.744},
    "gpt2xl_nucleus":  {"acc": 0.843},
    "gpt2xl_temp09":   {"acc": 0.859},
    "gpt2xl_topk50":   {"acc": 0.758},
}


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_len=512):
        self.encodings = tokenizer(
            texts, max_length=max_len, truncation=True,
            padding="max_length", return_tensors="pt"
        )

    def __len__(self):
        return self.encodings["input_ids"].shape[0]

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.encodings.items()}


def load_cell_data(data_dir, max_per_depth=5000):
    texts, labels = [], []
    for d in range(NUM_DEPTHS):
        fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
        if not os.path.exists(fpath):
            print(f"  WARNING: {fpath} not found, skipping depth {d}")
            continue
        count = 0
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                texts.append(rec["text"])
                labels.append(d)
                count += 1
                if count >= max_per_depth:
                    break
        print(f"  depth_{d}: {count} samples")
    return texts, np.array(labels)


@torch.no_grad()
def compute_log_likelihoods(model, tokenizer, texts, device, batch_size):
    dataset = TextDataset(texts, tokenizer, MAX_SEQ_LEN)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    all_ll = []
    for batch in loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits[:, :-1, :]
        targets = input_ids[:, 1:]
        mask = attention_mask[:, 1:]
        log_probs = torch.log_softmax(logits, dim=-1)
        token_ll = log_probs.gather(2, targets.unsqueeze(-1)).squeeze(-1)
        token_ll = token_ll * mask
        lengths = mask.sum(dim=1).clamp(min=1)
        mean_ll = token_ll.sum(dim=1) / lengths
        all_ll.append(mean_ll.cpu().numpy())
    return np.concatenate(all_ll)


@torch.no_grad()
def compute_fast_detectgpt_scores(model, tokenizer, texts, device, batch_size):
    dataset = TextDataset(texts, tokenizer, MAX_SEQ_LEN)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)
    all_scores = []
    for batch in loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits[:, :-1, :]
        targets = input_ids[:, 1:]
        mask = attention_mask[:, 1:].float()
        log_probs = torch.log_softmax(logits, dim=-1)
        probs = torch.softmax(logits, dim=-1)
        token_ll = log_probs.gather(2, targets.unsqueeze(-1)).squeeze(-1)
        entropy = -(probs * log_probs).sum(dim=-1)
        discrepancy = token_ll + entropy
        discrepancy = discrepancy * mask
        lengths = mask.sum(dim=1).clamp(min=1)
        mean_d = (discrepancy * mask).sum(dim=1) / lengths
        sum_sq = ((discrepancy - mean_d.unsqueeze(1)) ** 2 * mask).sum(dim=1)
        std_d = (sum_sq / lengths.clamp(min=2)).sqrt().clamp(min=1e-8)
        score = mean_d / std_d
        all_scores.append(score.cpu().numpy())
    return np.concatenate(all_scores)


def pairwise_auc(scores, labels, pair):
    d_lo, d_hi = pair
    mask = (labels == d_lo) | (labels == d_hi)
    if mask.sum() < 10:
        return None
    X = scores[mask].reshape(-1, 1)
    y = (labels[mask] == d_hi).astype(int)
    if len(np.unique(y)) < 2:
        return None
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    aucs = []
    for tr, te in skf.split(X, y):
        rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        rf.fit(X[tr], y[tr])
        prob = rf.predict_proba(X[te])[:, 1]
        aucs.append(roc_auc_score(y[te], prob))
    return round(np.mean(aucs), 4)


def pairwise_auc_combined(bino_scores, fdgpt_scores, labels, pair):
    d_lo, d_hi = pair
    mask = (labels == d_lo) | (labels == d_hi)
    if mask.sum() < 10:
        return None
    X = np.column_stack([bino_scores[mask], fdgpt_scores[mask]])
    y = (labels[mask] == d_hi).astype(int)
    if len(np.unique(y)) < 2:
        return None
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    aucs = []
    for tr, te in skf.split(X, y):
        rf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
        rf.fit(X[tr], y[tr])
        prob = rf.predict_proba(X[te])[:, 1]
        aucs.append(roc_auc_score(y[te], prob))
    return round(np.mean(aucs), 4)


def compute_monotonicity(scores, labels):
    rho, pval = spearmanr(scores, labels)
    return round(rho, 4), round(pval, 6)


def isotonic_cv(scores, labels, n_splits=5):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    accs = []
    for tr, te in skf.split(scores, labels):
        iso = IsotonicRegression(y_min=0, y_max=NUM_DEPTHS - 1, out_of_bounds="clip")
        iso.fit(scores[tr], labels[tr].astype(float))
        preds = np.round(iso.predict(scores[te])).astype(int)
        preds = np.clip(preds, 0, NUM_DEPTHS - 1)
        accs.append(accuracy_score(labels[te], preds))
    return round(np.mean(accs), 4), round(np.std(accs), 4)


def d0_binary_accuracy(scores, labels):
    binary = (labels >= 1).astype(int)
    if len(np.unique(binary)) < 2:
        return None, None
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    accs, aucs = [], []
    for tr, te in skf.split(scores, binary):
        thresh = np.median(scores[tr][labels[tr] == 0])
        higher_is_gen = np.mean(scores[tr][labels[tr] >= 1]) > np.mean(scores[tr][labels[tr] == 0])
        if higher_is_gen:
            preds = (scores[te] > thresh).astype(int)
        else:
            preds = (scores[te] < thresh).astype(int)
        accs.append(accuracy_score(binary[te], preds))
        if higher_is_gen:
            aucs.append(roc_auc_score(binary[te], scores[te]))
        else:
            aucs.append(roc_auc_score(binary[te], -scores[te]))
    return round(np.mean(accs), 4), round(np.mean(aucs), 4)


def lr_4class_cv(scores, labels, n_splits=5):
    X = scores.reshape(-1, 1) if scores.ndim == 1 else scores
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    accs = []
    for tr, te in skf.split(X, labels):
        clf = LogisticRegression(max_iter=1000, random_state=42)
        clf.fit(X[tr], labels[tr])
        accs.append(accuracy_score(labels[te], clf.predict(X[te])))
    return round(np.mean(accs), 4), round(np.std(accs), 4)


def analyze_cell(cell_name, data_dir, model_obs, model_perf, tok_obs, tok_perf,
                 device, batch_size, scores_dir):
    print(f"\n{'='*60}")
    print(f"  {cell_name}")
    print(f"{'='*60}")

    texts, labels = load_cell_data(data_dir)
    if len(texts) == 0:
        return None
    n = len(texts)
    print(f"  Total: {n} samples, depths: {np.bincount(labels)}")

    cache_path = os.path.join(scores_dir, f"{cell_name}_scores.npz")
    if os.path.exists(cache_path):
        print(f"  Loading cached scores from {cache_path}")
        cached = np.load(cache_path)
        bino_scores = cached["bino"]
        fdgpt_scores = cached["fdgpt"]
    else:
        t0 = time.time()
        print("  Computing LL (observer: gpt2-xl)...")
        ll_obs = compute_log_likelihoods(model_obs, tok_obs, texts, device, batch_size)
        print(f"    {time.time()-t0:.1f}s")

        t1 = time.time()
        print("  Computing LL (performer: pythia-1.4b)...")
        ll_perf = compute_log_likelihoods(model_perf, tok_perf, texts, device, batch_size)
        print(f"    {time.time()-t1:.1f}s")

        t2 = time.time()
        print("  Computing Fast-DetectGPT scores...")
        fdgpt_scores = compute_fast_detectgpt_scores(model_obs, tok_obs, texts, device, batch_size)
        print(f"    {time.time()-t2:.1f}s")

        bino_scores = (-ll_obs) / np.clip(-ll_perf, 1e-8, None)

        np.savez(cache_path, bino=bino_scores, fdgpt=fdgpt_scores, labels=labels)
        print(f"  Scores cached to {cache_path}")

    result = {"cell": cell_name, "n_samples": n}
    pairs = [(0, 1), (1, 2), (2, 3)]
    pair_names = ["d0v1", "d1v2", "d2v3"]

    # --- Binoculars ---
    bino_lr_acc, bino_lr_std = lr_4class_cv(bino_scores, labels)
    bino_iso_acc, bino_iso_std = isotonic_cv(bino_scores, labels)
    bino_rho, bino_rho_p = compute_monotonicity(bino_scores, labels)
    bino_d0_acc, bino_d0_auc = d0_binary_accuracy(bino_scores, labels)
    bino_pairwise = {}
    for pname, pair in zip(pair_names, pairs):
        bino_pairwise[pname] = pairwise_auc(bino_scores, labels, pair)

    result["binoculars"] = {
        "lr_4class_acc": bino_lr_acc,
        "lr_4class_std": bino_lr_std,
        "isotonic_acc": bino_iso_acc,
        "isotonic_std": bino_iso_std,
        "spearman_rho": bino_rho,
        "spearman_p": bino_rho_p,
        "d0_binary_acc": bino_d0_acc,
        "d0_binary_auc": bino_d0_auc,
        "pairwise_auc": bino_pairwise,
        "score_stats": {
            f"d{d}": {"mean": round(float(bino_scores[labels == d].mean()), 4),
                      "std": round(float(bino_scores[labels == d].std()), 4),
                      "median": round(float(np.median(bino_scores[labels == d])), 4)}
            for d in range(NUM_DEPTHS)
        }
    }

    # --- Fast-DetectGPT ---
    fdgpt_lr_acc, fdgpt_lr_std = lr_4class_cv(fdgpt_scores, labels)
    fdgpt_iso_acc, fdgpt_iso_std = isotonic_cv(fdgpt_scores, labels)
    fdgpt_rho, fdgpt_rho_p = compute_monotonicity(fdgpt_scores, labels)
    fdgpt_d0_acc, fdgpt_d0_auc = d0_binary_accuracy(fdgpt_scores, labels)
    fdgpt_pairwise = {}
    for pname, pair in zip(pair_names, pairs):
        fdgpt_pairwise[pname] = pairwise_auc(fdgpt_scores, labels, pair)

    result["fast_detectgpt"] = {
        "lr_4class_acc": fdgpt_lr_acc,
        "lr_4class_std": fdgpt_lr_std,
        "isotonic_acc": fdgpt_iso_acc,
        "isotonic_std": fdgpt_iso_std,
        "spearman_rho": fdgpt_rho,
        "spearman_p": fdgpt_rho_p,
        "d0_binary_acc": fdgpt_d0_acc,
        "d0_binary_auc": fdgpt_d0_auc,
        "pairwise_auc": fdgpt_pairwise,
        "score_stats": {
            f"d{d}": {"mean": round(float(fdgpt_scores[labels == d].mean()), 4),
                      "std": round(float(fdgpt_scores[labels == d].std()), 4),
                      "median": round(float(np.median(fdgpt_scores[labels == d])), 4)}
            for d in range(NUM_DEPTHS)
        }
    }

    # --- Combined (2-feature) ---
    X_comb = np.column_stack([bino_scores, fdgpt_scores])
    comb_lr_acc, comb_lr_std = lr_4class_cv(X_comb, labels)
    comb_pairwise = {}
    for pname, pair in zip(pair_names, pairs):
        comb_pairwise[pname] = pairwise_auc_combined(bino_scores, fdgpt_scores, labels, pair)

    result["combined"] = {
        "lr_4class_acc": comb_lr_acc,
        "lr_4class_std": comb_lr_std,
        "pairwise_auc": comb_pairwise,
    }

    # Print summary
    print(f"\n  {cell_name} results:")
    print(f"    Binoculars  LR-4cls: {bino_lr_acc:.4f}  Iso: {bino_iso_acc:.4f}  "
          f"rho: {bino_rho:.4f}  d0-bin: {bino_d0_acc}")
    print(f"    FastDetGPT  LR-4cls: {fdgpt_lr_acc:.4f}  Iso: {fdgpt_iso_acc:.4f}  "
          f"rho: {fdgpt_rho:.4f}  d0-bin: {fdgpt_d0_acc}")
    print(f"    Combined    LR-4cls: {comb_lr_acc:.4f}")
    print(f"    Pairwise AUC (Bino):  d0v1={bino_pairwise['d0v1']}  "
          f"d1v2={bino_pairwise['d1v2']}  d2v3={bino_pairwise['d2v3']}")
    print(f"    Pairwise AUC (FDGPT): d0v1={fdgpt_pairwise['d0v1']}  "
          f"d1v2={fdgpt_pairwise['d1v2']}  d2v3={fdgpt_pairwise['d2v3']}")
    print(f"    Pairwise AUC (Comb):  d0v1={comb_pairwise['d0v1']}  "
          f"d1v2={comb_pairwise['d1v2']}  d2v3={comb_pairwise['d2v3']}")

    return result


def print_comparison_table(all_results, cells):
    print(f"\n\n{'='*110}")
    print("  COMPARISON TABLE")
    print(f"{'='*110}")

    header = (f"  {'Cell':<16} {'Method':<14} {'4cls-Acc':<10} {'d0v1':<8} "
              f"{'d1v2':<8} {'d2v3':<8} {'Spearman':<10} {'d0-bin':<8}")
    print(header)
    print(f"  {'-'*106}")

    for cell_name in cells:
        if cell_name not in all_results:
            continue
        r = all_results[cell_name]
        ref = RF_REFERENCE.get(cell_name, {})

        # RF reference
        rf_acc = ref.get("acc", "")
        rf_d0v1 = ref.get("d0v1", "")
        rf_d1v2 = ref.get("d1v2", "")
        rf_d2v3 = ref.get("d2v3", "")
        print(f"  {cell_name:<16} {'RF-19feat':<14} {rf_acc:<10} "
              f"{rf_d0v1:<8} {rf_d1v2:<8} {rf_d2v3:<8} {'-1.0':<10} {'—':<8}")

        # Binoculars
        b = r["binoculars"]
        print(f"  {'':<16} {'Bino-LR':<14} {b['lr_4class_acc']:<10.4f} "
              f"{b['pairwise_auc']['d0v1']:<8} {b['pairwise_auc']['d1v2']:<8} "
              f"{b['pairwise_auc']['d2v3']:<8} {b['spearman_rho']:<10.4f} "
              f"{b['d0_binary_acc']:<8}")

        # Fast-DetectGPT
        f = r["fast_detectgpt"]
        print(f"  {'':<16} {'FDGPT-LR':<14} {f['lr_4class_acc']:<10.4f} "
              f"{f['pairwise_auc']['d0v1']:<8} {f['pairwise_auc']['d1v2']:<8} "
              f"{f['pairwise_auc']['d2v3']:<8} {f['spearman_rho']:<10.4f} "
              f"{f['d0_binary_acc']:<8}")

        # Combined
        c = r["combined"]
        print(f"  {'':<16} {'Combined':<14} {c['lr_4class_acc']:<10.4f} "
              f"{c['pairwise_auc']['d0v1']:<8} {c['pairwise_auc']['d1v2']:<8} "
              f"{c['pairwise_auc']['d2v3']:<8} {'—':<10} {'—':<8}")

        print(f"  {'-'*106}")

    # Averages
    bino_accs = [all_results[c]["binoculars"]["lr_4class_acc"] for c in cells if c in all_results]
    fdgpt_accs = [all_results[c]["fast_detectgpt"]["lr_4class_acc"] for c in cells if c in all_results]
    comb_accs = [all_results[c]["combined"]["lr_4class_acc"] for c in cells if c in all_results]
    rf_accs = [RF_REFERENCE[c]["acc"] for c in cells if c in all_results]

    if bino_accs:
        print(f"\n  Mean 4-class Acc:  RF={np.mean(rf_accs):.4f}  "
              f"Bino={np.mean(bino_accs):.4f}  FDGPT={np.mean(fdgpt_accs):.4f}  "
              f"Combined={np.mean(comb_accs):.4f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--batch_size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--output_dir", default="results/detection_baselines_ordinal")
    args = parser.parse_args()

    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)
    scores_dir = os.path.join(args.output_dir, "scores")
    os.makedirs(scores_dir, exist_ok=True)

    print("Loading models...")
    t0 = time.time()
    tok_obs = AutoTokenizer.from_pretrained(MODEL_PATHS["gpt2xl"])
    tok_obs.pad_token = tok_obs.eos_token
    model_obs = AutoModelForCausalLM.from_pretrained(
        MODEL_PATHS["gpt2xl"], torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  gpt2-xl loaded ({time.time()-t0:.1f}s)")

    t1 = time.time()
    tok_perf = AutoTokenizer.from_pretrained(MODEL_PATHS["pythia"])
    tok_perf.pad_token = tok_perf.eos_token
    model_perf = AutoModelForCausalLM.from_pretrained(
        MODEL_PATHS["pythia"], torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  pythia-1.4b loaded ({time.time()-t1:.1f}s)")

    cells = {"pythia_nucleus": GRID_CELLS["pythia_nucleus"]} if args.pilot else GRID_CELLS
    all_results = {}
    start = time.time()

    for cell_name, data_dir in cells.items():
        r = analyze_cell(cell_name, data_dir, model_obs, model_perf,
                         tok_obs, tok_perf, device, args.batch_size, scores_dir)
        if r:
            all_results[cell_name] = r

    elapsed = time.time() - start
    print_comparison_table(all_results, cells)

    summary = {
        "experiment": "detection_baselines_ordinal",
        "plan_id": "plan_018",
        "per_cell": all_results,
        "elapsed_seconds": round(elapsed, 1),
        "pilot_mode": args.pilot,
    }

    out_path = os.path.join(args.output_dir, "results.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
