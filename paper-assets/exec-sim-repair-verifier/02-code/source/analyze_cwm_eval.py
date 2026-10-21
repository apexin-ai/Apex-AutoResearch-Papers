#!/usr/bin/env python3
# analyze_cwm_eval.py — Post-hoc analysis of CWM repo-level eval predictions
# Reads predictions JSONL from eval_repo_cwm.py, computes detailed metrics,
# unparseable breakdown, CLS comparison, and error-mode analysis by input length.

import argparse
import json
import math
import sys
from collections import Counter

from sklearn.metrics import (
    accuracy_score, confusion_matrix, f1_score,
    precision_score, recall_score,
)


def load_jsonl(path):
    records = []
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"WARNING: skipping line {i}: {e}", file=sys.stderr)
    return records


def compute_metrics(labels, preds):
    acc = accuracy_score(labels, preds) * 100
    cm = confusion_matrix(labels, preds, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    support_fail = tn + fp
    support_pass = fn + tp
    majority_baseline = max(support_fail, support_pass) / len(labels) * 100

    return {
        "accuracy": round(acc, 2),
        "majority_baseline": round(majority_baseline, 2),
        "gap_vs_majority_pp": round(acc - majority_baseline, 2),
        "f1_macro": round(f1_score(labels, preds, average="macro") * 100, 2),
        "f1_fail": round(f1_score(labels, preds, pos_label=0) * 100, 2),
        "f1_pass": round(f1_score(labels, preds, pos_label=1) * 100, 2),
        "precision_fail": round(precision_score(labels, preds, pos_label=0, zero_division=0) * 100, 2),
        "precision_pass": round(precision_score(labels, preds, pos_label=1, zero_division=0) * 100, 2),
        "recall_fail": round(recall_score(labels, preds, pos_label=0, zero_division=0) * 100, 2),
        "recall_pass": round(recall_score(labels, preds, pos_label=1, zero_division=0) * 100, 2),
        "confusion_matrix": {"tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp)},
        "support": {"fail": int(support_fail), "pass": int(support_pass)},
    }


def analyze_unparseable(records):
    unparseable = [r for r in records if r.get("unparseable", False)]
    total = len(records)
    n_unparseable = len(unparseable)

    truncated_and_unparseable = sum(1 for r in unparseable if r.get("truncated", False))
    non_truncated_unparseable = n_unparseable - truncated_and_unparseable

    reasons = Counter()
    for r in unparseable:
        gt = r.get("gen_text", "")
        if r.get("truncated", False):
            reasons["truncated_input"] += 1
        elif len(gt.strip()) == 0:
            reasons["empty_output"] += 1
        elif len(gt.strip()) < 10:
            reasons["too_short"] += 1
        else:
            gt_lower = gt.lower()
            has_fail = any(k in gt_lower for k in ["error", "assert", "traceback", "exception", "fail"])
            has_pass = any(k in gt_lower for k in ["pass", "success", "completed"])
            if has_fail and has_pass:
                reasons["ambiguous_keywords"] += 1
            elif not has_fail and not has_pass:
                reasons["no_keywords"] += 1
            else:
                reasons["other"] += 1

    return {
        "total": total,
        "n_unparseable": n_unparseable,
        "unparseable_pct": round(n_unparseable / total * 100, 2) if total else 0,
        "truncated_and_unparseable": truncated_and_unparseable,
        "non_truncated_unparseable": non_truncated_unparseable,
        "reason_breakdown": dict(reasons),
    }


def analyze_by_gen_length(records):
    boundaries = [0, 50, 100, 200, 400, 800, float("inf")]
    bucket_names = ["0-49", "50-99", "100-199", "200-399", "400-799", "800+"]
    buckets = {name: [] for name in bucket_names}

    for r in records:
        gen_len = len(r.get("gen_text", ""))
        for i in range(len(boundaries) - 1):
            if boundaries[i] <= gen_len < boundaries[i + 1]:
                buckets[bucket_names[i]].append(r)
                break

    result = {}
    for name in bucket_names:
        items = buckets[name]
        if not items:
            result[name] = {"count": 0, "accuracy": None, "unparseable_pct": None}
            continue
        correct = sum(r["correct"] for r in items)
        unparseable = sum(1 for r in items if r.get("unparseable", False))
        result[name] = {
            "count": len(items),
            "accuracy": round(correct / len(items) * 100, 2),
            "unparseable_pct": round(unparseable / len(items) * 100, 2),
        }
    return result


def analyze_by_truncation(records):
    trunc = [r for r in records if r.get("truncated", False)]
    non_trunc = [r for r in records if not r.get("truncated", False)]

    def _stats(items):
        if not items:
            return {"count": 0, "accuracy": None, "unparseable_pct": None}
        return {
            "count": len(items),
            "accuracy": round(sum(r["correct"] for r in items) / len(items) * 100, 2),
            "unparseable_pct": round(sum(1 for r in items if r.get("unparseable")) / len(items) * 100, 2),
        }

    return {"truncated": _stats(trunc), "non_truncated": _stats(non_trunc)}


def build_cls_comparison(cwm_metrics, cls_results):
    rows = []
    for name, cls_m in cls_results.items():
        row = {"model": name}
        for key in ["accuracy", "f1_macro", "f1_fail", "f1_pass",
                     "precision_fail", "recall_fail", "precision_pass", "recall_pass"]:
            cls_val = cls_m.get(key)
            cwm_val = cwm_metrics.get(key)
            row[key + "_cls"] = cls_val
            row[key + "_cwm"] = cwm_val
            if cls_val is not None and cwm_val is not None:
                row[key + "_gap"] = round(cwm_val - cls_val, 2)
            else:
                row[key + "_gap"] = None
        rows.append(row)
    return rows


def load_cls_results(path):
    if path is None:
        return default_cls_results()
    with open(path) as f:
        return json.load(f)


def default_cls_results():
    return {
        "CLS_8B_s42": {
            "accuracy": 83.52, "f1_macro": None, "f1_fail": None, "f1_pass": None,
            "precision_fail": None, "recall_fail": None, "precision_pass": None, "recall_pass": None,
        },
        "CLS_4B_v5": {
            "accuracy": 83.63, "f1_macro": None, "f1_fail": None, "f1_pass": None,
            "precision_fail": None, "recall_fail": None, "precision_pass": None, "recall_pass": None,
        },
        "CLS_4B_seed123": {
            "accuracy": 75.33, "f1_macro": None, "f1_fail": None, "f1_pass": None,
            "precision_fail": None, "recall_fail": None, "precision_pass": None, "recall_pass": None,
        },
    }


def print_summary(metrics, unparseable_info, trunc_info, gen_length_info, cls_comparison, n_total):
    print("=" * 70)
    print(f"  CWM Repo-Level Eval Analysis  (n={n_total})")
    print("=" * 70)

    print(f"\n--- Core Metrics ---")
    print(f"  Accuracy:           {metrics['accuracy']:.2f}%")
    print(f"  Majority baseline:  {metrics['majority_baseline']:.2f}%  (gap: {metrics['gap_vs_majority_pp']:+.2f}pp)")
    print(f"  F1 macro:           {metrics['f1_macro']:.2f}%")
    print(f"  F1  fail/pass:      {metrics['f1_fail']:.2f}% / {metrics['f1_pass']:.2f}%")
    print(f"  Prec fail/pass:     {metrics['precision_fail']:.2f}% / {metrics['precision_pass']:.2f}%")
    print(f"  Rec  fail/pass:     {metrics['recall_fail']:.2f}% / {metrics['recall_pass']:.2f}%")

    cm = metrics["confusion_matrix"]
    print(f"\n--- Confusion Matrix ---")
    print(f"             Pred=Fail  Pred=Pass")
    print(f"  GT=Fail    {cm['tn']:>8}   {cm['fp']:>8}")
    print(f"  GT=Pass    {cm['fn']:>8}   {cm['tp']:>8}")

    print(f"\n--- Unparseable Analysis ---")
    print(f"  Total unparseable:  {unparseable_info['n_unparseable']} / {unparseable_info['total']} ({unparseable_info['unparseable_pct']:.1f}%)")
    print(f"    truncated input:  {unparseable_info['truncated_and_unparseable']}")
    print(f"    non-truncated:    {unparseable_info['non_truncated_unparseable']}")
    if unparseable_info["reason_breakdown"]:
        print(f"  Reason breakdown:")
        for reason, count in sorted(unparseable_info["reason_breakdown"].items(), key=lambda x: -x[1]):
            print(f"    {reason:25s} {count}")

    print(f"\n--- Truncation Impact ---")
    for key in ["truncated", "non_truncated"]:
        info = trunc_info[key]
        if info["count"] == 0:
            print(f"  {key:15s}  n=0")
        else:
            print(f"  {key:15s}  n={info['count']:>5}  acc={info['accuracy']:.2f}%  unparseable={info['unparseable_pct']:.1f}%")

    print(f"\n--- Accuracy by Generation Length ---")
    print(f"  {'Bucket':>10s}  {'Count':>6s}  {'Acc':>7s}  {'Unparse%':>9s}")
    for bucket, info in gen_length_info.items():
        if info["count"] == 0:
            continue
        acc_str = f"{info['accuracy']:.1f}%" if info["accuracy"] is not None else "N/A"
        unp_str = f"{info['unparseable_pct']:.1f}%" if info["unparseable_pct"] is not None else "N/A"
        print(f"  {bucket:>10s}  {info['count']:>6d}  {acc_str:>7s}  {unp_str:>9s}")

    if cls_comparison:
        print(f"\n--- CLS vs CWM Comparison ---")
        print(f"  {'Model':20s}  {'Acc_CLS':>8s}  {'Acc_CWM':>8s}  {'Gap':>7s}  {'F1m_CLS':>8s}  {'F1m_CWM':>8s}  {'F1m_Gap':>8s}")
        for row in cls_comparison:
            def _fmt(v):
                return f"{v:.2f}" if v is not None else "—"
            print(f"  {row['model']:20s}  {_fmt(row.get('accuracy_cls')):>8s}  {_fmt(row.get('accuracy_cwm')):>8s}  "
                  f"{_fmt(row.get('accuracy_gap')):>7s}  {_fmt(row.get('f1_macro_cls')):>8s}  "
                  f"{_fmt(row.get('f1_macro_cwm')):>8s}  {_fmt(row.get('f1_macro_gap')):>8s}")

    print("=" * 70)


def main():
    p = argparse.ArgumentParser(description="Analyze CWM repo-level eval predictions")
    p.add_argument("--predictions_path", required=True, help="Path to predictions JSONL from eval_repo_cwm.py")
    p.add_argument("--cls_results_json", default=None, help="Optional CLS metrics JSON for comparison (dict of model_name -> metrics)")
    p.add_argument("--output_path", default=None, help="Path to save JSON results (default: <predictions_dir>/cwm_analysis.json)")
    args = p.parse_args()

    records = load_jsonl(args.predictions_path)
    if not records:
        print("ERROR: no records loaded", file=sys.stderr)
        sys.exit(1)

    labels = [r["label"] for r in records]
    preds = [r["pred"] for r in records]

    metrics = compute_metrics(labels, preds)
    unparseable_info = analyze_unparseable(records)
    trunc_info = analyze_by_truncation(records)
    gen_length_info = analyze_by_gen_length(records)

    cls_results = load_cls_results(args.cls_results_json)
    cls_comparison = build_cls_comparison(metrics, cls_results)

    print_summary(metrics, unparseable_info, trunc_info, gen_length_info, cls_comparison, len(records))

    output = {
        "predictions_path": args.predictions_path,
        "n_instances": len(records),
        "metrics": metrics,
        "unparseable": unparseable_info,
        "truncation": trunc_info,
        "gen_length_buckets": gen_length_info,
        "cls_comparison": cls_comparison,
    }

    out_path = args.output_path
    if out_path is None:
        import os
        out_path = os.path.join(os.path.dirname(args.predictions_path) or ".", "cwm_analysis.json")

    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON results saved to: {out_path}")


if __name__ == "__main__":
    main()
