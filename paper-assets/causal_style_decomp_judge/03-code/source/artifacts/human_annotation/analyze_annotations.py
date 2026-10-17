"""Analyze human NLI gate annotations vs DeBERTa NLI decisions.

Usage:
    python analyze_annotations.py annotation_results.csv

Input CSV must have columns: sample_id, preserves_meaning
  preserves_meaning: "Yes" or "No" (human judgment)

Computes:
  - Overall human-NLI agreement rate
  - Cohen's kappa (human binary vs NLI binary)
  - Per-axis breakdown (formality vs verbosity)
  - Confusion matrix (TP/FP/TN/FN from NLI perspective)
  - Per-decision-type error rates
"""

import csv
import json
import sys
import os
from collections import Counter

def load_ground_truth(gt_path):
    with open(gt_path) as f:
        samples = json.load(f)
    return {s["sample_id"]: s for s in samples}

def load_annotations(csv_path):
    results = {}
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = row["sample_id"].strip()
            answer = row["preserves_meaning"].strip().lower()
            if answer in ("yes", "y", "1", "true"):
                results[sid] = True
            elif answer in ("no", "n", "0", "false"):
                results[sid] = False
            else:
                print(f"  WARNING: Skipping {sid}, unrecognized answer: '{answer}'")
    return results

def cohens_kappa(y1, y2):
    assert len(y1) == len(y2)
    n = len(y1)
    if n == 0:
        return float("nan")
    agree = sum(a == b for a, b in zip(y1, y2))
    p_o = agree / n
    c1 = Counter(y1)
    c2 = Counter(y2)
    p_e = sum(c1.get(k, 0) * c2.get(k, 0) for k in set(list(c1.keys()) + list(c2.keys()))) / (n * n)
    if p_e == 1.0:
        return 1.0 if p_o == 1.0 else 0.0
    return (p_o - p_e) / (1.0 - p_e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_annotations.py <annotation_results.csv>")
        print("  CSV must have columns: sample_id, preserves_meaning (Yes/No)")
        sys.exit(1)

    csv_path = sys.argv[1]
    gt_dir = os.path.dirname(os.path.abspath(__file__))
    gt_path = os.path.join(gt_dir, "annotation_samples.json")

    gt = load_ground_truth(gt_path)
    annotations = load_annotations(csv_path)

    matched = [(sid, annotations[sid], gt[sid]) for sid in annotations if sid in gt]
    if not matched:
        print("ERROR: No matching sample IDs found between annotations and ground truth.")
        sys.exit(1)

    print(f"Matched {len(matched)}/{len(gt)} samples\n")

    # Build comparison arrays
    # NLI says "pass" (preserves meaning) vs human says "Yes" (preserves meaning)
    nli_decisions = [s["nli_decision"] == "pass" for _, _, s in matched]
    human_decisions = [h for _, h, _ in matched]
    axes = [s["axis"] for _, _, s in matched]

    # Overall agreement
    agree = sum(n == h for n, h in zip(nli_decisions, human_decisions))
    total = len(matched)
    print(f"{'='*60}")
    print(f"OVERALL AGREEMENT")
    print(f"{'='*60}")
    print(f"  Agreement: {agree}/{total} = {agree/total:.1%}")
    print(f"  Cohen's kappa: {cohens_kappa(nli_decisions, human_decisions):.3f}")

    # Confusion matrix (NLI as "predicted", human as "reference")
    tp = sum(1 for n, h in zip(nli_decisions, human_decisions) if n and h)
    fp = sum(1 for n, h in zip(nli_decisions, human_decisions) if n and not h)
    fn = sum(1 for n, h in zip(nli_decisions, human_decisions) if not n and h)
    tn = sum(1 for n, h in zip(nli_decisions, human_decisions) if not n and not h)

    print(f"\n  Confusion Matrix (NLI predicted vs Human reference):")
    print(f"                    Human=Yes  Human=No")
    print(f"    NLI=pass          {tp:>5}     {fp:>5}")
    print(f"    NLI=fail          {fn:>5}     {tn:>5}")

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    print(f"\n  NLI Precision (of pass calls, how many human agrees): {precision:.1%}")
    print(f"  NLI Recall (of human-yes, how many NLI caught): {recall:.1%}")

    # Per-axis breakdown
    print(f"\n{'='*60}")
    print(f"PER-AXIS BREAKDOWN")
    print(f"{'='*60}")
    for axis in ["formality", "verbosity"]:
        idx = [i for i, a in enumerate(axes) if a == axis]
        if not idx:
            continue
        ax_nli = [nli_decisions[i] for i in idx]
        ax_human = [human_decisions[i] for i in idx]
        ax_agree = sum(n == h for n, h in zip(ax_nli, ax_human))
        ax_total = len(idx)
        ax_kappa = cohens_kappa(ax_nli, ax_human)
        print(f"  {axis}: agreement={ax_agree}/{ax_total} ({ax_agree/ax_total:.1%}), kappa={ax_kappa:.3f}")

    # Per NLI-decision breakdown
    print(f"\n{'='*60}")
    print(f"PER NLI-DECISION BREAKDOWN")
    print(f"{'='*60}")
    for dec in ["pass", "fail"]:
        is_pass = (dec == "pass")
        idx = [i for i, n in enumerate(nli_decisions) if n == is_pass]
        if not idx:
            continue
        h_agree = sum(1 for i in idx if human_decisions[i] == is_pass)
        print(f"  NLI-{dec} (n={len(idx)}): human agrees {h_agree}/{len(idx)} ({h_agree/len(idx):.1%})")

    # Disagreement details
    print(f"\n{'='*60}")
    print(f"DISAGREEMENT DETAILS")
    print(f"{'='*60}")
    disagree = [(sid, h, s) for sid, h, s in matched if (s["nli_decision"] == "pass") != h]
    if not disagree:
        print("  No disagreements!")
    else:
        for sid, human_yes, s in disagree:
            nli_dec = s["nli_decision"]
            nli_score = s["nli_score"]
            axis = s["axis"]
            h_str = "Yes" if human_yes else "No"
            print(f"  {sid} [{axis}]: NLI={nli_dec} (score={nli_score:.3f}), Human={h_str}")

    print(f"\n{'='*60}")
    print("Done.")


if __name__ == "__main__":
    main()
