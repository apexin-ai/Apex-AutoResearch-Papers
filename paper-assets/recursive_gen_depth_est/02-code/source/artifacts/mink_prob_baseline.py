# Min-K% Prob ordinal depth baseline for recursive generation depth estimation.
# Computes token-level log-probs via GPT-2 Large, takes the mean of the
# bottom-K% tokens as a membership-inference score, then calibrates to 4-class
# ordinal bins (d0-d3) using three methods: equal-interval, CORAL ordinal
# regression, and threshold-based (ROC-optimal).

import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
import json
import warnings
import numpy as np
from pathlib import Path
from collections import defaultdict

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, balanced_accuracy_score
from tqdm import tqdm

warnings.filterwarnings("ignore")

# CUDA_VISIBLE_DEVICES controlled externally
DEVICE = torch.device("cuda:0")

DATA_ROOT = Path("/root/autodl-tmp/recursive_gen_depth_est/data")
OUTPUT_DIR = Path("/root/autodl-tmp/recursive_gen_depth_est/results/mink_prob_baseline")

CELL_DIRS = {
    "pythia_nucleus": DATA_ROOT,
    "pythia_temp09":  DATA_ROOT / "pythia_temp09",
    "pythia_topk50":  DATA_ROOT / "pythia_topk50",
    "olmo_nucleus":   DATA_ROOT / "olmo",
    "olmo_temp09":    DATA_ROOT / "olmo_temp09",
    "olmo_topk50":    DATA_ROOT / "olmo_topk50",
    "gpt2xl_nucleus": DATA_ROOT / "gpt2xl",
    "gpt2xl_temp09":  DATA_ROOT / "gpt2xl_temp09",
    "gpt2xl_topk50":  DATA_ROOT / "gpt2xl_topk50",
}

K_VALUES = [10, 20, 30]
N_FOLDS = 5
SEED = 42
MAX_LENGTH = 512
BATCH_SIZE = 48


def load_cell_texts(cell_dir: Path):
    """Load depth_0..depth_3 jsonl files, return (texts, labels)."""
    texts, labels = [], []
    for d in range(4):
        fpath = cell_dir / f"depth_{d}.jsonl"
        if not fpath.exists():
            raise FileNotFoundError(f"Missing {fpath}")
        with open(fpath) as f:
            for line in f:
                rec = json.loads(line)
                texts.append(rec["text"])
                labels.append(d)
    return texts, np.array(labels)


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length):
        self.encodings = tokenizer(
            texts,
            max_length=max_length,
            truncation=True,
            padding=False,
            return_attention_mask=False,
        )["input_ids"]

    def __len__(self):
        return len(self.encodings)

    def __getitem__(self, idx):
        return self.encodings[idx]


def collate_fn(batch):
    max_len = max(len(ids) for ids in batch)
    padded = []
    masks = []
    for ids in batch:
        pad_len = max_len - len(ids)
        padded.append(ids + [0] * pad_len)
        masks.append([1] * len(ids) + [0] * pad_len)
    return torch.tensor(padded, dtype=torch.long), torch.tensor(masks, dtype=torch.long)


@torch.no_grad()
def compute_token_logprobs(model, dataloader):
    """Return list of 1-D numpy arrays, each containing per-token log-probs."""
    all_logprobs = []
    for input_ids, attention_mask in tqdm(dataloader, desc="  logprob"):
        input_ids = input_ids.to(DEVICE)
        attention_mask = attention_mask.to(DEVICE)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits  # (B, T, V)

        # shift: logits[:, :-1] predicts input_ids[:, 1:]
        shift_logits = logits[:, :-1, :]
        shift_labels = input_ids[:, 1:]
        shift_mask = attention_mask[:, 1:]

        log_probs = torch.log_softmax(shift_logits, dim=-1)
        # gather the log-prob of the actual next token
        token_lp = log_probs.gather(2, shift_labels.unsqueeze(-1)).squeeze(-1)
        # mask out padding
        token_lp = token_lp * shift_mask

        for i in range(token_lp.size(0)):
            length = shift_mask[i].sum().item()
            if length > 0:
                lp = token_lp[i, :int(length)].cpu().numpy()
            else:
                lp = np.array([0.0])
            all_logprobs.append(lp)
    return all_logprobs


def mink_score(token_logprobs: np.ndarray, k_pct: int) -> float:
    """Mean of the bottom k% log-probs (most surprising tokens)."""
    n = max(1, int(len(token_logprobs) * k_pct / 100))
    sorted_lp = np.sort(token_logprobs)
    return float(np.clip(np.mean(sorted_lp[:n]), -100, 0))


def calibrate_equal_interval(scores_train, labels_train, scores_test):
    """Method A: divide train score range into 4 equal-width bins."""
    smin, smax = scores_train.min(), scores_train.max()
    eps = 1e-8
    width = (smax - smin + eps) / 4
    # bin 0 = most negative (most machine-like), bin 3 = least negative
    # but depth 0 = human = highest score, depth 3 = most recursive = lowest score
    # so invert: highest score → d0, lowest → d3
    preds = np.clip(3 - ((scores_test - smin) / width).astype(int), 0, 3)
    return preds


def calibrate_threshold(scores_train, labels_train, scores_test):
    """Method C: find 3 optimal thresholds via brute-force on train set."""
    # We need 3 thresholds t1 < t2 < t3 such that:
    # score <= t1 → d3, t1 < score <= t2 → d2, t2 < score <= t3 → d1, score > t3 → d0
    sorted_unique = np.sort(np.unique(scores_train))
    if len(sorted_unique) < 4:
        return np.zeros(len(scores_test), dtype=int)

    # Use percentile-based grid search for efficiency
    percentiles = np.percentile(scores_train, np.arange(5, 100, 5))

    best_acc = -1
    best_thresholds = None

    for i, t1 in enumerate(percentiles):
        for j, t2 in enumerate(percentiles[i+1:], i+1):
            for t3 in percentiles[j+1:]:
                pred = np.zeros(len(scores_train), dtype=int)
                pred[scores_train <= t1] = 3
                pred[(scores_train > t1) & (scores_train <= t2)] = 2
                pred[(scores_train > t2) & (scores_train <= t3)] = 1
                pred[scores_train > t3] = 0
                acc = accuracy_score(labels_train, pred)
                if acc > best_acc:
                    best_acc = acc
                    best_thresholds = (t1, t2, t3)

    t1, t2, t3 = best_thresholds
    pred_test = np.zeros(len(scores_test), dtype=int)
    pred_test[scores_test <= t1] = 3
    pred_test[(scores_test > t1) & (scores_test <= t2)] = 2
    pred_test[(scores_test > t2) & (scores_test <= t3)] = 1
    pred_test[scores_test > t3] = 0
    return pred_test


class CoralOrdinal(nn.Module):
    """Simple CORAL ordinal regression: shared linear → K-1 biases."""
    def __init__(self, n_classes=4):
        super().__init__()
        self.linear = nn.Linear(1, 1, bias=False)
        self.biases = nn.Parameter(torch.zeros(n_classes - 1))

    def forward(self, x):
        # x: (N, 1)
        return self.linear(x) + self.biases  # (N, K-1)


def calibrate_coral(scores_train, labels_train, scores_test):
    """Method B: CORAL ordinal regression (1-D input → 4-class)."""
    X_tr = torch.tensor(scores_train, dtype=torch.float32).unsqueeze(1)
    y_tr = torch.tensor(labels_train, dtype=torch.long)
    X_te = torch.tensor(scores_test, dtype=torch.float32).unsqueeze(1)

    # ordinal labels: for class k, cumulative label[j] = 1 if k > j
    # depth 0 is "human" (highest score), depth 3 is most recursive (lowest score)
    # CORAL expects ordinal: y_ordinal[i, j] = 1 if label > j
    n_classes = 4
    y_ordinal = torch.zeros(len(y_tr), n_classes - 1)
    for j in range(n_classes - 1):
        y_ordinal[:, j] = (y_tr > j).float()

    model = CoralOrdinal(n_classes)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.BCEWithLogitsLoss()

    model.train()
    for _ in range(200):
        logits = model(X_tr)
        loss = criterion(logits, y_ordinal)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        logits_te = model(X_te)
        probs = torch.sigmoid(logits_te)  # (N, K-1)
        # predicted class = number of thresholds exceeded
        preds = (probs > 0.5).sum(dim=1).numpy().astype(int)
        preds = np.clip(preds, 0, 3)
    return preds


def evaluate_cell(scores, labels, k_pct):
    """Run 5-fold CV for all 3 calibration methods at given K%."""
    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)

    results = {}
    for method_name, calibrate_fn in [
        ("methodA", calibrate_equal_interval),
        ("methodB", calibrate_coral),
        ("methodC", calibrate_threshold),
    ]:
        fold_acc4, fold_bal_d1d3 = [], []

        for train_idx, test_idx in skf.split(scores, labels):
            s_train, s_test = scores[train_idx], scores[test_idx]
            y_train, y_test = labels[train_idx], labels[test_idx]

            preds = calibrate_fn(s_train, y_train, s_test)
            fold_acc4.append(accuracy_score(y_test, preds))

            # d1-d3 balanced accuracy (exclude d0)
            mask = y_test > 0
            if mask.sum() > 0:
                fold_bal_d1d3.append(balanced_accuracy_score(y_test[mask], preds[mask]))
            else:
                fold_bal_d1d3.append(0.0)

        key = f"K{k_pct}_{method_name}"
        results[key] = {
            "4class_acc": round(float(np.mean(fold_acc4)), 4),
            "d1d3_bal_acc": round(float(np.mean(fold_bal_d1d3)), 4),
        }
    return results


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading GPT-2 XL...")
    tokenizer = GPT2TokenizerFast.from_pretrained("/root/autodl-tmp/models/gpt2-xl")
    tokenizer.pad_token = tokenizer.eos_token
    model = GPT2LMHeadModel.from_pretrained("/root/autodl-tmp/models/gpt2-xl").to(DEVICE)
    model.eval()

    all_results = {}

    for cell_name, cell_dir in CELL_DIRS.items():
        print(f"\n{'='*60}")
        print(f"Processing cell: {cell_name}")
        print(f"{'='*60}")

        texts, labels = load_cell_texts(cell_dir)
        print(f"  Loaded {len(texts)} passages (depths: {np.bincount(labels)})")

        dataset = TextDataset(texts, tokenizer, MAX_LENGTH)
        dataloader = DataLoader(
            dataset, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn
        )

        token_logprobs_list = compute_token_logprobs(model, dataloader)

        cell_results = {}
        for k_pct in K_VALUES:
            print(f"  Computing Min-K={k_pct}% scores...")
            scores = np.array([mink_score(lp, k_pct) for lp in token_logprobs_list])

            # save raw scores
            score_path = OUTPUT_DIR / f"{cell_name}_K{k_pct}_scores.npy"
            np.save(score_path, scores)

            print(f"  Evaluating K={k_pct}%...")
            k_results = evaluate_cell(scores, labels, k_pct)
            cell_results.update(k_results)

            for key, vals in k_results.items():
                print(f"    {key}: acc={vals['4class_acc']:.4f}  d1d3_bal={vals['d1d3_bal_acc']:.4f}")

        all_results[cell_name] = cell_results

    # Compute 9-cell averages
    summary = defaultdict(lambda: {"4class_acc": [], "d1d3_bal_acc": []})
    for cell_name, cell_res in all_results.items():
        for key, vals in cell_res.items():
            summary[key]["4class_acc"].append(vals["4class_acc"])
            summary[key]["d1d3_bal_acc"].append(vals["d1d3_bal_acc"])

    all_results["__9cell_average__"] = {}
    for key, lists in summary.items():
        all_results["__9cell_average__"][key] = {
            "4class_acc": round(float(np.mean(lists["4class_acc"])), 4),
            "d1d3_bal_acc": round(float(np.mean(lists["d1d3_bal_acc"])), 4),
        }

    out_path = OUTPUT_DIR / "mink_prob_results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print(f"\n{'='*60}")
    print("9-CELL AVERAGE RESULTS")
    print(f"{'='*60}")
    print(f"{'Config':<20} {'4-class Acc':>12} {'d1-d3 BalAcc':>14}")
    print("-" * 48)
    for key in sorted(all_results["__9cell_average__"].keys()):
        v = all_results["__9cell_average__"][key]
        print(f"{key:<20} {v['4class_acc']:>12.4f} {v['d1d3_bal_acc']:>14.4f}")


if __name__ == "__main__":
    main()
