"""Binoculars ordinal depth baseline (Hans et al., ICML 2024).

Computes Binoculars scores using an observer model (pythia-1.4b) and a
performer model (pythia-410m), then evaluates ordinal depth classification
(d0-d3) via five methods: equal-width binning, CORAL ordinal regression,
threshold-based ROC optimization, single-feature RF, and multi-feature RF.

Input:
    --data_dir pointing to root with cell subdirectories, each containing
    depth_0.jsonl .. depth_3.jsonl.  Each JSONL record has a "text" field.

Output:
    JSON with per-cell and 9-cell-average metrics:
      {4class_acc, 4class_acc_std, d1d3_bal_acc, d1d3_bal_acc_std}
    Also saves per-cell .npz files with raw features and labels.

Dependencies: torch, transformers, scikit-learn, numpy, tqdm
"""

import argparse
import json
import os
import random
import time
import warnings
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, roc_curve
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

warnings.filterwarnings("ignore")

os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

SEED = 42
N_FOLDS = 5
MAX_LENGTH = 512
RF_N_ESTIMATORS = 200

CELL_SUBDIRS = {
    "pythia_nucleus": ".",
    "pythia_temp09":  "pythia_temp09",
    "pythia_topk50":  "pythia_topk50",
    "olmo_nucleus":   "olmo",
    "olmo_temp09":    "olmo_temp09",
    "olmo_topk50":    "olmo_topk50",
    "gpt2xl_nucleus": "gpt2xl",
    "gpt2xl_temp09":  "gpt2xl_temp09",
    "gpt2xl_topk50":  "gpt2xl_topk50",
}

MULTI_FEAT_NAMES = [
    "bino_score",
    "ppl_mean", "ppl_var", "ppl_median", "ppl_p10", "ppl_p90", "ppl_skew",
    "xppl_mean", "xppl_var", "xppl_median",
    "bino_score_median",
]


# ── Utilities ──────────────────────────────────────────────────────────────

def set_seed(seed=SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_cell_texts(cell_dir, max_samples=0):
    """Load depth_0..3.jsonl from cell_dir. Returns (texts, labels)."""
    texts, labels = [], []
    for d in range(4):
        fpath = cell_dir / f"depth_{d}.jsonl"
        if not fpath.exists():
            raise FileNotFoundError(f"Missing {fpath}")
        lines = [ln for ln in fpath.read_text().strip().split("\n") if ln.strip()]
        if 0 < max_samples < len(lines):
            rng = np.random.RandomState(SEED + d)
            idx = rng.choice(len(lines), max_samples, replace=False)
            lines = [lines[i] for i in sorted(idx)]
        for line in lines:
            rec = json.loads(line)
            texts.append(rec["text"])
            labels.append(d)
    return texts, np.array(labels, dtype=np.int64)


def _skewness(x):
    """Sample skewness without scipy."""
    if len(x) < 3:
        return 0.0
    m = np.mean(x)
    s = np.std(x, ddof=0)
    if s < 1e-12:
        return 0.0
    return float(np.mean(((x - m) / s) ** 3))


# ── Binoculars scorer ─────────────────────────────────────────────────────

class BinocularsScorer:
    """Compute Binoculars features using observer and performer LMs.

    Core formula (Hans et al. 2024):
        score = PPL(x; performer) / H(observer, performer)
    where PPL is standard per-token CE against actual tokens, and H is the
    cross-entropy between the observer's softmax distribution and the
    performer's logits at each position.
    """

    def __init__(self, observer_name, performer_name, device,
                 max_length=MAX_LENGTH):
        self.device = device
        self.max_length = max_length

        print(f"Loading tokenizer: {observer_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(observer_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.pad_token_id = self.tokenizer.pad_token_id

        print(f"Loading observer:  {observer_name}")
        self.observer = AutoModelForCausalLM.from_pretrained(
            observer_name, torch_dtype=torch.float16,
        ).to(device).eval()

        print(f"Loading performer: {performer_name}")
        self.performer = AutoModelForCausalLM.from_pretrained(
            performer_name, torch_dtype=torch.float16,
        ).to(device).eval()

        self.ce_loss_fn = nn.CrossEntropyLoss(reduction="none")
        self.softmax_fn = nn.Softmax(dim=-1)

    @torch.no_grad()
    def compute_features(self, texts, batch_size=8):
        """Compute per-sample Binoculars-derived features.

        For each text, runs both models and extracts:
          - Standard Binoculars score (ppl_mean / xppl_mean)
          - Token-level statistics of PPL and cross-entropy

        Returns dict mapping feature name -> np.array of shape (n_samples,).
        """
        feats = {k: [] for k in MULTI_FEAT_NAMES}

        for i in tqdm(range(0, len(texts), batch_size),
                      desc="  Binoculars scoring"):
            batch = texts[i:i + batch_size]
            enc = self.tokenizer(
                batch,
                max_length=self.max_length,
                truncation=True,
                padding=True,
                return_tensors="pt",
                return_attention_mask=True,
            ).to(self.device)

            obs_logits = self.observer(**enc).logits
            perf_logits = self.performer(**enc).logits

            # ── Per-token perplexity: performer predicts next token ──
            shifted_perf = perf_logits[:, :-1, :].contiguous().float()
            shifted_labels = enc.input_ids[:, 1:].contiguous()
            shifted_mask = enc.attention_mask[:, 1:].contiguous().bool()
            ppl_tok = self.ce_loss_fn(
                shifted_perf.transpose(1, 2), shifted_labels,
            )  # (B, T-1)

            # ── Per-token cross-entropy: observer dist vs performer logits ──
            # No shift — matches original Binoculars implementation.
            B, T, V = obs_logits.shape
            obs_probs = self.softmax_fn(obs_logits.float()).reshape(-1, V)
            perf_flat = perf_logits.float().reshape(-1, V)
            xppl_tok = self.ce_loss_fn(perf_flat, obs_probs).reshape(B, T)
            full_mask = (enc.input_ids != self.pad_token_id)

            # ── Extract per-sample statistics ──
            for b in range(len(batch)):
                pv = ppl_tok[b][shifted_mask[b]].cpu().numpy()
                xv = xppl_tok[b][full_mask[b]].cpu().numpy()

                if len(pv) < 2 or len(xv) < 2:
                    for k in MULTI_FEAT_NAMES:
                        feats[k].append(0.0)
                    continue

                pm = float(np.mean(pv))
                xm = float(np.mean(xv))
                p_med = float(np.median(pv))
                x_med = float(np.median(xv))

                feats["bino_score"].append(
                    pm / xm if xm > 1e-8 else 0.0)
                feats["ppl_mean"].append(pm)
                feats["ppl_var"].append(float(np.var(pv)))
                feats["ppl_median"].append(p_med)
                feats["ppl_p10"].append(float(np.percentile(pv, 10)))
                feats["ppl_p90"].append(float(np.percentile(pv, 90)))
                feats["ppl_skew"].append(_skewness(pv))
                feats["xppl_mean"].append(xm)
                feats["xppl_var"].append(float(np.var(xv)))
                feats["xppl_median"].append(x_med)
                feats["bino_score_median"].append(
                    p_med / x_med if x_med > 1e-8 else 0.0)

            del obs_logits, perf_logits, shifted_perf, obs_probs
            del perf_flat, ppl_tok, xppl_tok
            torch.cuda.empty_cache()

        return {k: np.array(v, dtype=np.float64) for k, v in feats.items()}


# ── Calibration methods (matching detectgpt/mink baselines) ────────────────

def calibrate_equal_width(s_tr, y_tr, s_te):
    """Equal-width binning. Tries both score directions, picks better."""
    lo, hi = s_tr.min(), s_tr.max()
    if hi - lo < 1e-12:
        return np.zeros(len(s_te), dtype=int)
    width = (hi - lo + 1e-8) / 4

    best_preds, best_acc = None, -1
    for ascending in [True, False]:
        if ascending:
            p_tr = np.clip(((s_tr - lo) / width).astype(int), 0, 3)
            p_te = np.clip(((s_te - lo) / width).astype(int), 0, 3)
        else:
            p_tr = np.clip(3 - ((s_tr - lo) / width).astype(int), 0, 3)
            p_te = np.clip(3 - ((s_te - lo) / width).astype(int), 0, 3)
        acc = accuracy_score(y_tr, p_tr)
        if acc > best_acc:
            best_acc, best_preds = acc, p_te
    return best_preds


class _CoralOrdinal(nn.Module):
    """CORAL ordinal regression: shared linear + per-boundary biases."""

    def __init__(self, n_classes=4):
        super().__init__()
        self.linear = nn.Linear(1, 1, bias=False)
        self.biases = nn.Parameter(torch.zeros(n_classes - 1))

    def forward(self, x):
        return self.linear(x) + self.biases  # (N, K-1)


def calibrate_coral(s_tr, y_tr, s_te):
    """CORAL ordinal regression (1-D score -> 4-class)."""
    X_tr = torch.tensor(s_tr, dtype=torch.float32).unsqueeze(1)
    X_te = torch.tensor(s_te, dtype=torch.float32).unsqueeze(1)

    y_ord = torch.zeros(len(y_tr), 3)
    for j in range(3):
        y_ord[:, j] = (torch.tensor(y_tr) > j).float()

    model = _CoralOrdinal()
    opt = torch.optim.Adam(model.parameters(), lr=0.01)
    crit = nn.BCEWithLogitsLoss()

    model.train()
    for _ in range(300):
        loss = crit(model(X_tr), y_ord)
        opt.zero_grad()
        loss.backward()
        opt.step()

    model.eval()
    with torch.no_grad():
        probs = torch.sigmoid(model(X_te))
        preds = (probs > 0.5).sum(dim=1).numpy().astype(int)
    return np.clip(preds, 0, 3)


def calibrate_threshold(s_tr, y_tr, s_te):
    """ROC-optimal thresholds for each depth boundary.

    Tries both score directions to handle unknown monotonicity.
    """
    best_preds_test, best_acc = None, -1

    for flip in [False, True]:
        st = -s_tr if flip else s_tr.copy()
        ste = -s_te if flip else s_te.copy()

        thresholds = []
        for boundary in range(1, 4):
            y_bin = (y_tr >= boundary).astype(int)
            if len(np.unique(y_bin)) < 2:
                thresholds.append(np.median(st))
                continue
            fpr, tpr, thresh = roc_curve(y_bin, st)
            best_idx = np.argmax(tpr - fpr)
            thresholds.append(thresh[best_idx])

        thresholds = sorted(thresholds)
        p_tr = np.zeros(len(st), dtype=int)
        for t in thresholds:
            p_tr += (st >= t).astype(int)
        p_tr = np.clip(p_tr, 0, 3)
        acc = accuracy_score(y_tr, p_tr)

        if acc > best_acc:
            best_acc = acc
            p_te = np.zeros(len(ste), dtype=int)
            for t in thresholds:
                p_te += (ste >= t).astype(int)
            best_preds_test = np.clip(p_te, 0, 3)

    return best_preds_test


# ── RF classifiers ─────────────────────────────────────────────────────────

def rf_single_feature(s_tr, y_tr, s_te):
    """RF with Binoculars score as sole feature."""
    clf = RandomForestClassifier(
        n_estimators=RF_N_ESTIMATORS, random_state=SEED, n_jobs=-1,
    )
    clf.fit(s_tr.reshape(-1, 1), y_tr)
    return clf.predict(s_te.reshape(-1, 1))


def rf_multi_feature(X_tr, y_tr, X_te):
    """RF with 11 Binoculars-derived features."""
    scaler = StandardScaler()
    Xtr = np.nan_to_num(scaler.fit_transform(X_tr), nan=0.0, posinf=0.0,
                        neginf=0.0)
    Xte = np.nan_to_num(scaler.transform(X_te), nan=0.0, posinf=0.0,
                        neginf=0.0)
    clf = RandomForestClassifier(
        n_estimators=RF_N_ESTIMATORS, random_state=SEED, n_jobs=-1,
    )
    clf.fit(Xtr, y_tr)
    return clf.predict(Xte)


# ── 5-fold CV evaluation ──────────────────────────────────────────────────

def evaluate_cell(features, labels):
    """Run 5-fold StratifiedKFold CV for all five methods.

    Args:
        features: dict of feature arrays (each shape (n,))
        labels: int array of depth labels

    Returns:
        dict of method -> {4class_acc, 4class_acc_std,
                           d1d3_bal_acc, d1d3_bal_acc_std}
    """
    scores = features["bino_score"]
    X_multi = np.column_stack([features[k] for k in MULTI_FEAT_NAMES])

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)

    METHODS = [
        ("equal_width", True),
        ("coral",       True),
        ("threshold",   True),
        ("RF_single",   True),
        ("RF_multi",    False),
    ]

    results = {}
    for method_name, uses_score_only in METHODS:
        fold_acc4, fold_bal = [], []

        for train_idx, test_idx in skf.split(scores, labels):
            s_tr = scores[train_idx]
            s_te = scores[test_idx]
            y_tr = labels[train_idx]
            y_te = labels[test_idx]

            if method_name == "equal_width":
                preds = calibrate_equal_width(s_tr, y_tr, s_te)
            elif method_name == "coral":
                preds = calibrate_coral(s_tr, y_tr, s_te)
            elif method_name == "threshold":
                preds = calibrate_threshold(s_tr, y_tr, s_te)
            elif method_name == "RF_single":
                preds = rf_single_feature(s_tr, y_tr, s_te)
            elif method_name == "RF_multi":
                preds = rf_multi_feature(
                    X_multi[train_idx], y_tr, X_multi[test_idx])

            fold_acc4.append(accuracy_score(y_te, preds))

            mask = y_te >= 1
            if mask.sum() > 0:
                fold_bal.append(
                    balanced_accuracy_score(y_te[mask], preds[mask]))
            else:
                fold_bal.append(0.0)

        results[method_name] = {
            "4class_acc":       round(float(np.mean(fold_acc4)), 4),
            "4class_acc_std":   round(float(np.std(fold_acc4)), 4),
            "d1d3_bal_acc":     round(float(np.mean(fold_bal)), 4),
            "d1d3_bal_acc_std": round(float(np.std(fold_bal)), 4),
        }

    return results


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Binoculars ordinal depth baseline (Hans et al. 2024)")
    parser.add_argument(
        "--data_dir", type=str, required=True,
        help="Root data dir with cell subdirs containing depth_0..3.jsonl")
    parser.add_argument(
        "--observer_model", type=str, default="EleutherAI/pythia-1.4b",
        help="Observer model (larger, default: pythia-1.4b)")
    parser.add_argument(
        "--performer_model", type=str, default="EleutherAI/pythia-410m",
        help="Performer model (smaller, default: pythia-410m)")
    parser.add_argument(
        "--output_path", type=str, required=True,
        help="Output JSON path for results")
    parser.add_argument(
        "--gpu", type=int, default=0, help="GPU device ID")
    parser.add_argument(
        "--max_samples", type=int, default=0,
        help="Max samples per depth (0 = use all, >0 for debugging)")
    parser.add_argument(
        "--batch_size", type=int, default=8,
        help="Batch size for model inference (default: 8)")
    args = parser.parse_args()

    set_seed()
    data_root = Path(args.data_dir)
    device = torch.device(f"cuda:{args.gpu}")

    print("=" * 60)
    print("Binoculars Ordinal Depth Baseline")
    print(f"  Observer:  {args.observer_model}")
    print(f"  Performer: {args.performer_model}")
    print(f"  Device:    {device}")
    print(f"  Data root: {data_root}")
    print(f"  Max samples/depth: {args.max_samples or 'all (5000)'}")
    print(f"  Batch size: {args.batch_size}")
    print("=" * 60)

    scorer = BinocularsScorer(
        args.observer_model, args.performer_model,
        device, max_length=MAX_LENGTH,
    )

    all_results = {}
    cell_times = {}

    for cell_name, subdir in CELL_SUBDIRS.items():
        cell_dir = data_root / subdir if subdir != "." else data_root
        if not (cell_dir / "depth_0.jsonl").exists():
            print(f"\nSkipping {cell_name}: "
                  f"{cell_dir}/depth_0.jsonl not found")
            continue

        print(f"\n{'=' * 60}")
        print(f"Cell: {cell_name}  ({cell_dir})")
        print(f"{'=' * 60}")

        t0 = time.time()
        texts, labels = load_cell_texts(
            cell_dir, max_samples=args.max_samples)
        print(f"  Loaded {len(texts)} samples, "
              f"depths: {np.bincount(labels).tolist()}")

        features = scorer.compute_features(texts, batch_size=args.batch_size)
        bino = features["bino_score"]
        print(f"  Binoculars score: mean={bino.mean():.4f}, "
              f"std={bino.std():.4f}, "
              f"min={bino.min():.4f}, max={bino.max():.4f}")

        out_dir = Path(args.output_path).parent
        out_dir.mkdir(parents=True, exist_ok=True)
        np.savez(
            out_dir / f"{cell_name}_bino_features.npz",
            **features, labels=labels,
        )

        cell_results = evaluate_cell(features, labels)
        elapsed = time.time() - t0
        cell_times[cell_name] = round(elapsed, 1)

        for method, m in cell_results.items():
            print(f"  {method:12s}: "
                  f"acc={m['4class_acc']:.4f}+/-{m['4class_acc_std']:.4f}  "
                  f"d1d3_bal={m['d1d3_bal_acc']:.4f}"
                  f"+/-{m['d1d3_bal_acc_std']:.4f}")

        all_results[cell_name] = cell_results

        with open(args.output_path, "w") as f:
            json.dump(all_results, f, indent=2)

    # ── 9-cell average ──
    if all_results:
        avg = defaultdict(lambda: defaultdict(list))
        for cell_res in all_results.values():
            for method, metrics in cell_res.items():
                for k, v in metrics.items():
                    avg[method][k].append(v)

        all_results["__9cell_average__"] = {}
        for method, ml in avg.items():
            all_results["__9cell_average__"][method] = {
                k: round(float(np.mean(v)), 4) for k, v in ml.items()
            }

        all_results["__meta__"] = {
            "observer": args.observer_model,
            "performer": args.performer_model,
            "max_samples_per_depth": args.max_samples or "all",
            "n_folds": N_FOLDS,
            "rf_n_estimators": RF_N_ESTIMATORS,
            "multi_features": MULTI_FEAT_NAMES,
            "cell_times_sec": cell_times,
            "total_time_sec": round(sum(cell_times.values()), 1),
        }

    with open(args.output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {args.output_path}")

    # ── Summary table ──
    print(f"\n{'=' * 60}")
    print("9-Cell Average Summary")
    print(f"{'=' * 60}")
    if "__9cell_average__" in all_results:
        for method, m in all_results["__9cell_average__"].items():
            print(f"  {method:12s}: "
                  f"acc={m['4class_acc']:.4f}  "
                  f"d1d3_bal={m['d1d3_bal_acc']:.4f}")


if __name__ == "__main__":
    main()
