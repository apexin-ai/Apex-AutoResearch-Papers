#!/usr/bin/env python3
"""LF Oracle Baseline — evaluate labeling function voting strategies without training.

Applies various LF ensemble strategies on the same test split used by the GRU probe,
using raw LF outputs from windows_labeled.jsonl (no embeddings, no training).

Input:
    --data_dir: directory containing data/windows_labeled.jsonl
    --split_info: path to checkpoints/split_info.json (from train_probe.py)

Output:
    Markdown comparison table of LF baselines vs GRU probe (test_macro_f1=0.9055).
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

LF_NAMES = ["file_diff_delta", "command_repetition", "outcome_backpropagation"]
PROBE_REF_MACRO_F1 = 0.9055


def load_windows(path: str) -> list[dict]:
    """Load all windows from JSONL, preserving file order."""
    windows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                windows.append(json.loads(line))
    return windows


def compute_prior(windows: list[dict]) -> float:
    """P(progress) from training set majority labels."""
    labels = [w["majority_label"] for w in windows]
    return sum(labels) / len(labels) if labels else 0.5


def predict_majority_vote(windows: list[dict], prior: float) -> list[int]:
    """Use majority_label directly. All test windows should be non-abstain after filtering."""
    fallback = 1 if prior >= 0.5 else 0
    return [w["majority_label"] if w["majority_label"] != -1 else fallback for w in windows]


def predict_any_stagnation(windows: list[dict], prior: float) -> list[int]:
    """Any LF votes stagnation(0) → predict stagnation."""
    fallback = 1 if prior >= 0.5 else 0
    preds = []
    for w in windows:
        vals = [w["labels"][lf] for lf in LF_NAMES]
        if 0 in vals:
            preds.append(0)
        elif any(v != -1 for v in vals):
            preds.append(1)
        else:
            preds.append(fallback)
    return preds


def predict_all_agreement(windows: list[dict], prior: float) -> list[int]:
    """Predict only when all non-abstain LFs agree; otherwise use prior."""
    fallback = 1 if prior >= 0.5 else 0
    preds = []
    for w in windows:
        active = [w["labels"][lf] for lf in LF_NAMES if w["labels"][lf] != -1]
        if active and len(set(active)) == 1:
            preds.append(active[0])
        else:
            preds.append(fallback)
    return preds


def predict_single_lf(windows: list[dict], lf_name: str, prior: float) -> list[int]:
    """Single LF as classifier; abstain → prior."""
    fallback = 1 if prior >= 0.5 else 0
    return [w["labels"][lf_name] if w["labels"][lf_name] != -1 else fallback for w in windows]


def print_table(results: list[tuple[str, dict]]):
    header = "| Method                      | Macro-F1 | Accuracy | Prec(M) | Rec(M) | F1(stag) | F1(prog) |"
    sep = "|" + "|".join(["-" * 30] + ["-" * 10] * 6) + "|"
    print(header)
    print(sep)
    for name, m in results:
        row = f"| {name:28s} |"
        for key in ["macro_f1", "accuracy", "precision_macro", "recall_macro", "f1_stagnation", "f1_progress"]:
            v = m.get(key)
            if v is None:
                row += "    —     |"
            else:
                row += f" {v:.4f}   |"
        print(row)


def main():
    parser = argparse.ArgumentParser(
        description="LF Oracle Baseline — evaluate LF voting strategies on test split"
    )
    parser.add_argument("--data_dir", required=True, help="Dir containing data/windows_labeled.jsonl")
    parser.add_argument("--split_info", required=True, help="Path to split_info.json")
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).parent))
    from baselines import compute_metrics

    # Load windows (same filtering as generate_embeddings.py)
    data_path = Path(args.data_dir) / "data" / "windows_labeled.jsonl"
    all_windows = load_windows(str(data_path))
    usable = [w for w in all_windows if w.get("majority_label", -1) != -1]
    print(f"Loaded {len(all_windows)} windows, {len(usable)} usable (non-abstain)")

    with open(args.split_info) as f:
        split_info = json.load(f)

    # Apply confidence filter (mirrors train_probe.py)
    keep_indices = split_info.get("keep_indices")
    if keep_indices is not None:
        min_conf = split_info.get("min_confidence", 0)
        print(f"Confidence filter (min_confidence={min_conf}): {len(keep_indices)}/{len(usable)} windows")
        windows = [usable[i] for i in keep_indices]
    else:
        windows = usable

    train_idx = split_info["train_indices"]
    val_idx = split_info["val_indices"]
    test_idx = split_info["test_indices"]

    train_windows = [windows[i] for i in train_idx]
    test_windows = [windows[i] for i in test_idx]

    gt = [w["majority_label"] for w in test_windows]
    prior = compute_prior(train_windows)

    print(f"Split — train: {len(train_idx)}, val: {len(val_idx)}, test: {len(test_idx)}")
    print(f"Prior P(progress) = {prior:.4f}")
    print(f"Test label distribution: {dict(Counter(gt))}")
    print()

    results = []

    # Reference row
    results.append(("GRU Probe (probe_001 ref)", {"macro_f1": PROBE_REF_MACRO_F1}))

    # LF ensemble variants
    strategies = [
        ("LF Majority Vote", predict_majority_vote(test_windows, prior)),
        ("LF Any-Stagnation", predict_any_stagnation(test_windows, prior)),
        ("LF All-Agreement", predict_all_agreement(test_windows, prior)),
    ]
    for lf in LF_NAMES:
        strategies.append((f"Single LF: {lf}", predict_single_lf(test_windows, lf, prior)))

    for name, preds in strategies:
        results.append((name, compute_metrics(gt, preds)))

    # LF coverage stats
    print("=== LF Coverage on Test Set ===")
    for lf in LF_NAMES:
        n_active = sum(1 for w in test_windows if w["labels"][lf] != -1)
        n_total = len(test_windows)
        print(f"  {lf}: {n_active}/{n_total} ({n_active / n_total * 100:.1f}%)")
    n_all_agree = sum(
        1 for w in test_windows
        if len(set(v for v in [w["labels"][lf] for lf in LF_NAMES] if v != -1)) == 1
        and any(w["labels"][lf] != -1 for lf in LF_NAMES)
    )
    print(f"  All non-abstain agree: {n_all_agree}/{len(test_windows)} ({n_all_agree / len(test_windows) * 100:.1f}%)")
    print()

    # Results table
    print("=== Results ===")
    print_table(results)

    # Summary
    lf_results = results[1:]
    best_name, best_m = max(lf_results, key=lambda x: x[1]["macro_f1"])
    print(f"\nBest LF baseline: {best_name} (Macro-F1={best_m['macro_f1']:.4f})")
    delta = PROBE_REF_MACRO_F1 - best_m["macro_f1"]
    print(f"GRU Probe vs best LF: {delta:+.4f}")

    # Save JSON results
    output_path = Path(args.data_dir) / "lf_oracle_results.json"
    json_results = {}
    for name, m in results:
        json_results[name] = {k: round(v, 4) if v is not None else None for k, v in m.items()}
    with open(output_path, "w") as f:
        json.dump(json_results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
