"""
Detection-based baselines for recursive generation depth estimation.

Computes Binoculars and Fast-DetectGPT continuous scores on 3x3 grid data,
then calibrates to 4-class ordinal prediction via LR and optimal binning.

Models used:
  - Binoculars: gpt2-xl (observer) + pythia-1.4b (performer)
  - Fast-DetectGPT: gpt2-xl (scoring model)

Usage:
  python scripts/detection_baselines.py --gpu 0
  python scripts/detection_baselines.py --gpu 0 --pilot  # only pythia_nucleus
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
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

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
BATCH_SIZE = 16


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
def compute_log_likelihoods(model, tokenizer, texts, device, batch_size=BATCH_SIZE):
    """Compute per-sample mean log-likelihood (negative cross-entropy)."""
    dataset = TextDataset(texts, tokenizer, MAX_SEQ_LEN)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=False)

    all_ll = []
    for batch in loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits[:, :-1, :]  # shift
        targets = input_ids[:, 1:]  # shift
        mask = attention_mask[:, 1:]

        log_probs = torch.log_softmax(logits, dim=-1)
        token_ll = log_probs.gather(2, targets.unsqueeze(-1)).squeeze(-1)
        token_ll = token_ll * mask

        lengths = mask.sum(dim=1).clamp(min=1)
        mean_ll = token_ll.sum(dim=1) / lengths
        all_ll.append(mean_ll.cpu().numpy())

    return np.concatenate(all_ll)


@torch.no_grad()
def compute_fast_detectgpt_scores(model, tokenizer, texts, device, batch_size=BATCH_SIZE):
    """
    Compute Fast-DetectGPT score: normalized discrepancy between
    actual token log-prob and expected log-prob under model's own distribution.
    score_i = log p(x_i|x_{<i}) + H(p(·|x_{<i}))
    Final score = mean(score_i) / std(score_i)
    """
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

        discrepancy = token_ll + entropy  # log p(x_i) - (-H) = log p(x_i) + H
        discrepancy = discrepancy * mask

        lengths = mask.sum(dim=1).clamp(min=1)
        mean_d = (discrepancy * mask).sum(dim=1) / lengths

        sum_sq = ((discrepancy - mean_d.unsqueeze(1)) ** 2 * mask).sum(dim=1)
        std_d = (sum_sq / lengths.clamp(min=2)).sqrt().clamp(min=1e-8)

        score = mean_d / std_d
        all_scores.append(score.cpu().numpy())

    return np.concatenate(all_scores)


def optimal_binning(scores, labels, n_bins=4):
    """Cut scores into n_bins using training quantiles, return accuracy."""
    thresholds = np.quantile(scores, [i / n_bins for i in range(1, n_bins)])
    preds = np.digitize(scores, thresholds)
    return accuracy_score(labels, preds), preds


def lr_calibration_cv(scores, labels, n_splits=5, seed=42):
    """5-fold CV logistic regression on single score feature."""
    X = scores.reshape(-1, 1)
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    accs = []
    all_preds = np.zeros_like(labels)

    for train_idx, test_idx in skf.split(X, labels):
        clf = LogisticRegression(max_iter=1000, random_state=seed, multi_class="multinomial")
        clf.fit(X[train_idx], labels[train_idx])
        preds = clf.predict(X[test_idx])
        all_preds[test_idx] = preds
        accs.append(accuracy_score(labels[test_idx], preds))

    return np.mean(accs), np.std(accs), all_preds


def run_cell(cell_name, data_dir, model_obs, model_perf, tok_obs, tok_perf, device):
    """Run all scoring methods on one cell."""
    print(f"\n{'='*60}")
    print(f"  Processing: {cell_name}")
    print(f"{'='*60}")

    texts, labels = load_cell_data(data_dir)
    if len(texts) == 0:
        return None
    n = len(texts)
    print(f"  Total: {n} samples, depths: {np.bincount(labels)}")

    t0 = time.time()
    print("  Computing log-likelihoods (observer: gpt2-xl)...")
    ll_obs = compute_log_likelihoods(model_obs, tok_obs, texts, device)
    print(f"    Done in {time.time()-t0:.1f}s")

    t1 = time.time()
    print("  Computing log-likelihoods (performer: pythia-1.4b)...")
    ll_perf = compute_log_likelihoods(model_perf, tok_perf, texts, device)
    print(f"    Done in {time.time()-t1:.1f}s")

    t2 = time.time()
    print("  Computing Fast-DetectGPT scores (gpt2-xl)...")
    fdgpt_scores = compute_fast_detectgpt_scores(model_obs, tok_obs, texts, device)
    print(f"    Done in {time.time()-t2:.1f}s")

    # Binoculars score: CE_observer / CE_performer = (-ll_obs) / (-ll_perf)
    ce_obs = -ll_obs
    ce_perf = -ll_perf
    bino_scores = ce_obs / np.clip(ce_perf, 1e-8, None)

    results = {"cell": cell_name, "n_samples": n}

    # Binoculars calibration
    bino_bin_acc, _ = optimal_binning(bino_scores, labels)
    bino_lr_acc, bino_lr_std, _ = lr_calibration_cv(bino_scores, labels)
    results["binoculars"] = {
        "binning_acc": round(bino_bin_acc, 4),
        "lr_acc_mean": round(bino_lr_acc, 4),
        "lr_acc_std": round(bino_lr_std, 4),
        "score_stats": {
            f"d{d}": {"mean": round(float(bino_scores[labels == d].mean()), 4),
                      "std": round(float(bino_scores[labels == d].std()), 4)}
            for d in range(NUM_DEPTHS)
        }
    }

    # Fast-DetectGPT calibration
    fdgpt_bin_acc, _ = optimal_binning(fdgpt_scores, labels)
    fdgpt_lr_acc, fdgpt_lr_std, _ = lr_calibration_cv(fdgpt_scores, labels)
    results["fast_detectgpt"] = {
        "binning_acc": round(fdgpt_bin_acc, 4),
        "lr_acc_mean": round(fdgpt_lr_acc, 4),
        "lr_acc_std": round(fdgpt_lr_std, 4),
        "score_stats": {
            f"d{d}": {"mean": round(float(fdgpt_scores[labels == d].mean()), 4),
                      "std": round(float(fdgpt_scores[labels == d].std()), 4)}
            for d in range(NUM_DEPTHS)
        }
    }

    # Combined (both scores as 2-feature input)
    X_combined = np.column_stack([bino_scores, fdgpt_scores])
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    comb_accs = []
    for train_idx, test_idx in skf.split(X_combined, labels):
        clf = LogisticRegression(max_iter=1000, random_state=42, multi_class="multinomial")
        clf.fit(X_combined[train_idx], labels[train_idx])
        comb_accs.append(accuracy_score(labels[test_idx], clf.predict(X_combined[test_idx])))
    results["combined_lr_acc"] = round(np.mean(comb_accs), 4)

    print(f"\n  Results for {cell_name}:")
    print(f"    Binoculars  — Binning: {bino_bin_acc:.4f}, LR: {bino_lr_acc:.4f}")
    print(f"    FastDetect  — Binning: {fdgpt_bin_acc:.4f}, LR: {fdgpt_lr_acc:.4f}")
    print(f"    Combined LR — {np.mean(comb_accs):.4f}")

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--pilot", action="store_true", help="Only run pythia_nucleus")
    parser.add_argument("--batch_size", type=int, default=BATCH_SIZE)
    parser.add_argument("--output_dir", default="results/detection_baselines")
    args = parser.parse_args()

    global BATCH_SIZE
    BATCH_SIZE = args.batch_size

    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    print("Loading models...")
    t0 = time.time()

    tok_obs = AutoTokenizer.from_pretrained(MODEL_PATHS["gpt2xl"])
    tok_obs.pad_token = tok_obs.eos_token
    model_obs = AutoModelForCausalLM.from_pretrained(
        MODEL_PATHS["gpt2xl"], torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  gpt2-xl loaded in {time.time()-t0:.1f}s")

    t1 = time.time()
    tok_perf = AutoTokenizer.from_pretrained(MODEL_PATHS["pythia"])
    tok_perf.pad_token = tok_perf.eos_token
    model_perf = AutoModelForCausalLM.from_pretrained(
        MODEL_PATHS["pythia"], torch_dtype=torch.float16
    ).to(device).eval()
    print(f"  pythia-1.4b loaded in {time.time()-t1:.1f}s")

    cells = {"pythia_nucleus": GRID_CELLS["pythia_nucleus"]} if args.pilot else GRID_CELLS
    all_results = {}
    start = time.time()

    for cell_name, data_dir in cells.items():
        result = run_cell(cell_name, data_dir, model_obs, model_perf, tok_obs, tok_perf, device)
        if result:
            all_results[cell_name] = result

    elapsed = time.time() - start

    # RF reference values from baseline_battery_9cell
    rf_reference = {
        "pythia_nucleus": 0.7813, "pythia_temp09": 0.7677, "pythia_topk50": 0.687,
        "olmo_nucleus": 0.7877, "olmo_temp09": 0.827, "olmo_topk50": 0.737,
        "gpt2xl_nucleus": 0.8397, "gpt2xl_temp09": 0.8527, "gpt2xl_topk50": 0.754,
    }

    # Summary table
    print(f"\n\n{'='*80}")
    print("  COMPARISON TABLE: 4-class Accuracy (LR calibration)")
    print(f"{'='*80}")
    print(f"  {'Cell':<18} {'RF(19feat)':<12} {'Bino-LR':<12} {'FDG-LR':<12} {'Combined':<12}")
    print(f"  {'-'*18} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")

    bino_accs, fdgpt_accs, comb_accs = [], [], []
    for cell_name in cells:
        if cell_name not in all_results:
            continue
        r = all_results[cell_name]
        rf = rf_reference.get(cell_name, 0)
        b = r["binoculars"]["lr_acc_mean"]
        f = r["fast_detectgpt"]["lr_acc_mean"]
        c = r["combined_lr_acc"]
        print(f"  {cell_name:<18} {rf:<12.4f} {b:<12.4f} {f:<12.4f} {c:<12.4f}")
        bino_accs.append(b)
        fdgpt_accs.append(f)
        comb_accs.append(c)

    if bino_accs:
        rf_vals = [rf_reference[c] for c in cells if c in all_results]
        print(f"  {'-'*18} {'-'*12} {'-'*12} {'-'*12} {'-'*12}")
        print(f"  {'MEAN':<18} {np.mean(rf_vals):<12.4f} {np.mean(bino_accs):<12.4f} "
              f"{np.mean(fdgpt_accs):<12.4f} {np.mean(comb_accs):<12.4f}")

    summary = {
        "experiment": "detection_baselines_001",
        "plan_id": "plan_018",
        "hypothesis": "Binoculars/Fast-DetectGPT continuous scores cannot be effectively "
                      "calibrated to ordinal depth because they capture real-vs-synthetic "
                      "boundary rather than depth gradient; calibrated 4-class acc < 45%",
        "models": {
            "observer": "gpt2-xl (local)",
            "performer": "pythia-1.4b (local)",
            "fast_detectgpt_scorer": "gpt2-xl (local)"
        },
        "per_cell": all_results,
        "summary": {
            "mean_binoculars_lr_acc": round(np.mean(bino_accs), 4) if bino_accs else None,
            "mean_fast_detectgpt_lr_acc": round(np.mean(fdgpt_accs), 4) if fdgpt_accs else None,
            "mean_combined_lr_acc": round(np.mean(comb_accs), 4) if comb_accs else None,
            "mean_rf_reference": round(np.mean(rf_vals), 4) if bino_accs else None,
        },
        "elapsed_seconds": round(elapsed, 1),
        "pilot_mode": args.pilot,
    }

    out_path = os.path.join(args.output_dir, "summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  Results saved to {out_path}")


if __name__ == "__main__":
    main()
