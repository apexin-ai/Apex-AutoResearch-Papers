"""DetectGPT ordinal depth baseline (Mitchell et al. 2023).

Computes perturbation discrepancy scores using T5-large (perturbation, fp16)
and GPT-2 Large (scoring, fp16), then calibrates to 4-class ordinal depth
(d0-d3) via three methods: equal-width binning, CORAL ordinal regression,
and threshold-based ROC optimization.

Usage:
    CUDA_VISIBLE_DEVICES=1 python detectgpt_baseline.py [--cells pythia_nucleus]
"""

import argparse
import json
import os
import random
import time
import warnings
from pathlib import Path

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, accuracy_score, roc_curve
from sklearn.model_selection import StratifiedKFold
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    T5ForConditionalGeneration,
    T5Tokenizer,
)

warnings.filterwarnings("ignore")

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

DATA_ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est/data")
RESULT_DIR = Path("/root/autodl-tmp/recursive_gen_depth_est/results/detectgpt_baseline")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

CELLS = [
    "gpt2xl", "gpt2xl_temp09", "gpt2xl_topk50",
    "olmo", "olmo_temp09", "olmo_topk50",
    "pythia_nucleus", "pythia_temp09", "pythia_topk50",
]
CELL_SUBDIRS = {
    "pythia_nucleus": ".",
}
CELL_DISPLAY = {
    "gpt2xl": "gpt2xl_nucleus",
    "olmo": "olmo_nucleus",
}

DEPTHS = [0, 1, 2, 3]
SAMPLES_PER_DEPTH = 200
N_PERTURBATIONS = 5
MASK_RATIO = 0.15
MAX_TOKENS = 512
N_FOLDS = 5

DEVICE = torch.device("cuda:0")
SCORING_MODEL_NAME = "openai-community/gpt2-large"
PERTURB_MODEL_NAME = "google-t5/t5-large"

T5_BATCH_SIZE = 48
T5_MAX_NEW_TOKENS = 64
SCORING_BATCH_SIZE = 32


def load_cell_data(cell_name):
    texts, labels = [], []
    subdir = CELL_SUBDIRS.get(cell_name, cell_name)
    for d in DEPTHS:
        fpath = DATA_ROOT / subdir / f"depth_{d}.jsonl"
        if not fpath.exists():
            print(f"  WARNING: {fpath} not found, skipping depth {d}")
            continue
        lines = fpath.read_text().strip().split("\n")
        random.shuffle(lines)
        sampled = lines[:SAMPLES_PER_DEPTH]
        for line in sampled:
            obj = json.loads(line)
            texts.append(obj["text"])
            labels.append(d)
    return texts, np.array(labels)


class ScoringModel:
    def __init__(self):
        print("Loading scoring model:", SCORING_MODEL_NAME)
        self.tokenizer = AutoTokenizer.from_pretrained(SCORING_MODEL_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(
            SCORING_MODEL_NAME, torch_dtype=torch.float16
        ).to(DEVICE)
        self.model.eval()
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    @torch.no_grad()
    def log_prob(self, texts, batch_size=SCORING_BATCH_SIZE):
        all_scores = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            enc = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=MAX_TOKENS,
            ).to(DEVICE)
            out = self.model(**enc)
            logits = out.logits[:, :-1, :]
            log_probs = torch.log_softmax(logits, dim=-1)
            input_ids = enc["input_ids"][:, 1:]
            attention = enc["attention_mask"][:, 1:]
            token_lps = log_probs.gather(2, input_ids.unsqueeze(-1)).squeeze(-1)
            token_lps = token_lps * attention
            lengths = attention.sum(dim=1).clamp(min=1)
            mean_lps = (token_lps.sum(dim=1) / lengths).float().cpu().numpy()
            all_scores.extend(mean_lps.tolist())
        return np.array(all_scores)


class PerturbationModel:
    def __init__(self):
        print("Loading perturbation model:", PERTURB_MODEL_NAME)
        self.tokenizer = T5Tokenizer.from_pretrained(PERTURB_MODEL_NAME)
        self.model = T5ForConditionalGeneration.from_pretrained(
            PERTURB_MODEL_NAME, torch_dtype=torch.float16
        ).to(DEVICE)
        self.model.eval()

    def _mask_text(self, text):
        words = text.split()
        if len(words) < 5:
            return text
        n_mask = max(1, int(len(words) * MASK_RATIO))
        mask_indices = sorted(random.sample(range(len(words)), min(n_mask, len(words))))

        sentinel_id = 0
        result = []
        for i, w in enumerate(words):
            if i in mask_indices:
                result.append(f"<extra_id_{sentinel_id}>")
                sentinel_id += 1
            else:
                result.append(w)
        return " ".join(result)

    @torch.no_grad()
    def _fill_masks_batch(self, masked_texts):
        enc = self.tokenizer(
            masked_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=MAX_TOKENS,
        ).to(DEVICE)
        outputs = self.model.generate(
            **enc,
            max_new_tokens=T5_MAX_NEW_TOKENS,
            do_sample=True,
            top_p=0.96,
            num_return_sequences=1,
        )
        filled = self.tokenizer.batch_decode(outputs, skip_special_tokens=False)
        return filled

    def _reconstruct(self, original_text, masked_text, filled_text):
        words = masked_text.split()
        fills = {}
        parts = filled_text.split("<extra_id_")
        for part in parts[1:]:
            if ">" in part:
                idx_str, content = part.split(">", 1)
                try:
                    idx = int(idx_str)
                except ValueError:
                    continue
                next_sentinel = f"<extra_id_{idx + 1}>"
                if next_sentinel in content:
                    content = content[: content.index(next_sentinel)]
                content = content.replace("</s>", "").replace("<pad>", "").strip()
                fills[idx] = content

        result = []
        sentinel_id = 0
        orig_words = original_text.split()
        for w in words:
            if w.startswith("<extra_id_"):
                if sentinel_id in fills and fills[sentinel_id]:
                    result.append(fills[sentinel_id])
                else:
                    orig_idx = min(len(result), len(orig_words) - 1)
                    if 0 <= orig_idx < len(orig_words):
                        result.append(orig_words[orig_idx])
                sentinel_id += 1
            else:
                result.append(w)
        return " ".join(result)

    def perturb_all(self, texts, n_perturbations=N_PERTURBATIONS):
        n = len(texts)
        all_perturbations = [[] for _ in range(n)]

        for p_idx in range(n_perturbations):
            masked = [self._mask_text(t) for t in texts]
            for i in range(0, n, T5_BATCH_SIZE):
                batch_masked = masked[i : i + T5_BATCH_SIZE]
                batch_orig = texts[i : i + T5_BATCH_SIZE]
                filled = self._fill_masks_batch(batch_masked)
                for j, (orig, m, f) in enumerate(zip(batch_orig, batch_masked, filled)):
                    recon = self._reconstruct(orig, m, f)
                    all_perturbations[i + j].append(recon)
            print(f"    Perturbation round {p_idx+1}/{n_perturbations} done")
        return all_perturbations


def compute_discrepancy(scorer, texts, perturbations):
    orig_scores = scorer.log_prob(texts)
    n_texts = len(texts)
    n_perts = len(perturbations[0])

    flat_perts = []
    for p_list in perturbations:
        flat_perts.extend(p_list)

    pert_scores = scorer.log_prob(flat_perts)
    pert_scores = pert_scores.reshape(n_texts, n_perts)

    discrepancies = orig_scores[:, None] - pert_scores
    mean_disc = np.mean(discrepancies, axis=1)
    mean_disc = np.clip(mean_disc, -100, 100)
    return mean_disc


def method_a_equal_width(scores, labels, train_idx, test_idx):
    train_scores = scores[train_idx]
    test_scores = scores[test_idx]
    lo, hi = train_scores.min(), train_scores.max()
    if lo == hi:
        hi = lo + 1e-6
    boundaries = np.linspace(lo, hi, 5)
    preds = np.digitize(test_scores, boundaries[1:-1])
    preds = np.clip(preds, 0, 3)
    return preds


def method_b_coral(scores, labels, train_idx, test_idx):
    X_train = scores[train_idx].reshape(-1, 1)
    y_train = labels[train_idx]
    X_test = scores[test_idx].reshape(-1, 1)

    classifiers = []
    for k in range(3):
        y_binary = (y_train > k).astype(int)
        if len(np.unique(y_binary)) < 2:
            classifiers.append(None)
            continue
        clf = LogisticRegression(max_iter=1000, random_state=SEED)
        clf.fit(X_train, y_binary)
        classifiers.append(clf)

    preds = np.zeros(len(X_test), dtype=int)
    for k, clf in enumerate(classifiers):
        if clf is not None:
            prob = clf.predict_proba(X_test)
            if prob.shape[1] == 2:
                preds += (prob[:, 1] > 0.5).astype(int)
    preds = np.clip(preds, 0, 3)
    return preds


def method_c_threshold(scores, labels, train_idx, test_idx):
    train_scores = scores[train_idx]
    y_train = labels[train_idx]
    test_scores = scores[test_idx]

    thresholds = []
    for k in range(3):
        y_binary = (y_train > k).astype(int)
        if len(np.unique(y_binary)) < 2:
            thresholds.append(np.median(train_scores))
            continue
        fpr, tpr, thresh = roc_curve(y_binary, train_scores)
        j_scores = tpr - fpr
        best_idx = np.argmax(j_scores)
        thresholds.append(thresh[best_idx])

    thresholds = sorted(thresholds)
    preds = np.zeros(len(test_scores), dtype=int)
    for t in thresholds:
        preds += (test_scores >= t).astype(int)
    preds = np.clip(preds, 0, 3)
    return preds


def evaluate_cell(cell_name, scorer, perturber):
    display = CELL_DISPLAY.get(cell_name, cell_name)
    print(f"\n{'='*60}")
    print(f"Processing cell: {display} (dir: {cell_name})")
    print(f"{'='*60}")

    texts, labels = load_cell_data(cell_name)
    print(f"  Loaded {len(texts)} passages, depth distribution: {np.bincount(labels)}")

    if len(texts) == 0:
        return None

    t0 = time.time()
    print("  Generating perturbations...")
    all_perturbations = perturber.perturb_all(texts, n_perturbations=N_PERTURBATIONS)
    t1 = time.time()
    print(f"  Perturbation done in {t1-t0:.1f}s")

    print("  Computing discrepancy scores...")
    scores = compute_discrepancy(scorer, texts, all_perturbations)
    t2 = time.time()
    print(f"  Scoring done in {t2-t1:.1f}s")
    print(f"  Score stats: mean={scores.mean():.4f}, std={scores.std():.4f}, "
          f"min={scores.min():.4f}, max={scores.max():.4f}")

    np.savez(
        RESULT_DIR / f"{display}_scores.npz",
        scores=scores,
        labels=labels,
    )

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    methods = {
        "methodA": method_a_equal_width,
        "methodB": method_b_coral,
        "methodC": method_c_threshold,
    }

    results = {}
    for method_name, method_fn in methods.items():
        fold_acc4 = []
        fold_bal_d1d3 = []

        for fold, (train_idx, test_idx) in enumerate(skf.split(scores, labels)):
            preds = method_fn(scores, labels, train_idx, test_idx)
            y_true = labels[test_idx]

            acc4 = accuracy_score(y_true, preds)
            fold_acc4.append(acc4)

            mask_d1d3 = y_true >= 1
            if mask_d1d3.sum() > 0:
                bal = balanced_accuracy_score(y_true[mask_d1d3], preds[mask_d1d3])
            else:
                bal = 0.0
            fold_bal_d1d3.append(bal)

        mean_acc4 = float(np.mean(fold_acc4))
        mean_bal = float(np.mean(fold_bal_d1d3))
        std_acc4 = float(np.std(fold_acc4))
        std_bal = float(np.std(fold_bal_d1d3))

        results[method_name] = {
            "4class_acc": round(mean_acc4, 4),
            "4class_acc_std": round(std_acc4, 4),
            "d1d3_bal_acc": round(mean_bal, 4),
            "d1d3_bal_acc_std": round(std_bal, 4),
        }
        print(f"  {method_name}: 4-class acc={mean_acc4:.4f}+-{std_acc4:.4f}, "
              f"d1-d3 bal_acc={mean_bal:.4f}+-{std_bal:.4f}")

    return results


def main():
    parser = argparse.ArgumentParser(description="DetectGPT ordinal depth baseline")
    parser.add_argument("--cells", nargs="+", default=None,
                        help="Subset of cells to run (default: all 9)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output JSON path (default: RESULT_DIR/detectgpt_results.json)")
    args = parser.parse_args()

    cells_to_run = args.cells if args.cells else CELLS
    out_path = Path(args.output) if args.output else RESULT_DIR / "detectgpt_results.json"

    print("=" * 60)
    print("DetectGPT Ordinal Depth Baseline")
    print(f"Device: {DEVICE}")
    print(f"Cells: {cells_to_run}")
    print(f"Samples per depth per cell: {SAMPLES_PER_DEPTH}")
    print(f"Perturbations per passage: {N_PERTURBATIONS}")
    print(f"T5 batch size: {T5_BATCH_SIZE}, max_new_tokens: {T5_MAX_NEW_TOKENS}")
    print("=" * 60)

    scorer = ScoringModel()
    perturber = PerturbationModel()

    all_results = {}
    if out_path.exists():
        with open(out_path) as f:
            all_results = json.load(f)
        all_results.pop("summary", None)
        print(f"Loaded {len(all_results)} existing cell results from {out_path}")

    for cell in cells_to_run:
        cell_results = evaluate_cell(cell, scorer, perturber)
        if cell_results is not None:
            display = CELL_DISPLAY.get(cell, cell)
            all_results[display] = cell_results

            with open(out_path, "w") as f:
                json.dump(all_results, f, indent=2)
            print(f"  [SAVED] {display} → {out_path}")

    summary_acc4 = []
    summary_bal = []
    for cell_name, cell_res in all_results.items():
        for method_name, metrics in cell_res.items():
            summary_acc4.append(metrics["4class_acc"])
            summary_bal.append(metrics["d1d3_bal_acc"])

    all_results["summary"] = {
        "mean_4class_acc": round(float(np.mean(summary_acc4)), 4) if summary_acc4 else 0,
        "mean_d1d3_bal_acc": round(float(np.mean(summary_bal)), 4) if summary_bal else 0,
        "n_cells": len(cells_to_run),
        "n_cells_total": len(all_results) - 1,
        "samples_per_depth": SAMPLES_PER_DEPTH,
        "n_perturbations": N_PERTURBATIONS,
        "scoring_model": SCORING_MODEL_NAME,
        "perturbation_model": PERTURB_MODEL_NAME,
    }

    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nResults saved to {out_path}")
    print(f"Summary: mean 4-class acc = {all_results['summary']['mean_4class_acc']:.4f}, "
          f"mean d1-d3 bal_acc = {all_results['summary']['mean_d1d3_bal_acc']:.4f}")


if __name__ == "__main__":
    main()
