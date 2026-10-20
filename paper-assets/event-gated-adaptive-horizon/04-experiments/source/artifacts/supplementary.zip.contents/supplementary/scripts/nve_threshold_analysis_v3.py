#!/usr/bin/env python3
"""NVE Threshold Analysis v3 — 35K+ window only, with 009b."""

import json
import os
import numpy as np
from collections import defaultdict

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"
ARTIFACTS = "/root/autodl-tmp/event-gated-adaptive-horizon/artifacts"

DIR_MAP = {
    "exp_001_baseline": "baseline_s1",
    "exp_006_fixed_dt2": "fixed_dt2_v1_s1",
    "exp_008a_no_subsample_dt2": "exp_008a_fixed_dt2_no_subsample",
    "exp_008d_subsample_on_h8": "exp_008d_subsample_on_h8",
    "exp_008e_v3_walker_s1": "exp_008e_v3_walker_s1",
    "exp_008e_v3_walker_s2": "exp_008e_v3_walker_s2",
    "exp_008f_no_dt_embed_subsample_on_h8": "exp_008f_no_dt_embed_subsample_on_h8",
    "exp_009b_008d_walker_s2": "exp_009b_008d_walker_s2",
}

MIN_STEP = 35000


def load_metrics(exp_id):
    dirpath = os.path.join(LOGDIR, DIR_MAP[exp_id])
    filepath = os.path.join(dirpath, "metrics.jsonl")

    eval_returns = {}
    value_means = {}

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            d = json.loads(line)
            step = d.get("step")
            if step is None:
                continue
            if "eval_return" in d:
                eval_returns[step] = d["eval_return"]
            if "value_mean" in d:
                value_means[step] = d["value_mean"]

    common_steps = sorted(set(eval_returns) & set(value_means))
    data = []
    for s in common_steps:
        data.append({
            "step": s,
            "eval_return": eval_returns[s],
            "value_mean": value_means[s],
        })
    return data


def compute_nve(exp_data, baseline_data):
    baseline_ratio = {}
    for d in baseline_data:
        if d["eval_return"] != 0:
            baseline_ratio[d["step"]] = d["value_mean"] / d["eval_return"]

    nve = {}
    for d in exp_data:
        step = d["step"]
        if step < MIN_STEP:
            continue
        if step not in baseline_ratio:
            continue
        if d["eval_return"] == 0 or baseline_ratio[step] == 0:
            continue
        exp_ratio = d["value_mean"] / d["eval_return"]
        nve[step] = exp_ratio / baseline_ratio[step]

    return nve


def classification_metrics(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)

    n = tp + tn + fp + fn
    accuracy = (tp + tn) / n if n > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "TP": tp, "TN": tn, "FP": fp, "FN": fn,
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def compute_auroc(labels, scores):
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")

    concordant = 0.0
    for i in range(len(labels)):
        if labels[i] == 1:
            for j in range(len(labels)):
                if labels[j] == 0:
                    if scores[i] > scores[j]:
                        concordant += 1.0
                    elif scores[i] == scores[j]:
                        concordant += 0.5

    return round(concordant / (n_pos * n_neg), 4)


def bootstrap_auroc(labels, scores, n_bootstrap=1000):
    rng = np.random.RandomState(42)
    n = len(labels)
    aurocs = []
    for _ in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        bl = [labels[i] for i in idx]
        bs = [scores[i] for i in idx]
        if sum(bl) == 0 or sum(bl) == len(bl):
            continue
        a = compute_auroc(bl, bs)
        if not np.isnan(a):
            aurocs.append(a)

    if len(aurocs) < 10:
        return [float("nan"), float("nan")]

    lo = float(np.percentile(aurocs, 2.5))
    hi = float(np.percentile(aurocs, 97.5))
    return [round(lo, 4), round(hi, 4)]


def run_task(task_label, positive_ids, negative_ids, thresholds, all_nve):
    all_ids = positive_ids + negative_ids
    labels = [1] * len(positive_ids) + [0] * len(negative_ids)
    scores = [all_nve[eid]["max_nve"] for eid in all_ids]

    result = {
        "label": task_label,
        "positive": positive_ids,
        "negative": negative_ids,
        "thresholds": {},
    }

    for thr in thresholds:
        preds = [1 if s >= thr else 0 for s in scores]
        metrics = classification_metrics(labels, preds)
        details = {}
        for eid, s, l, p in zip(all_ids, scores, labels, preds):
            details[eid] = {
                "max_nve_35K_plus": round(s, 4),
                "true_label": l,
                "predicted": p,
                "correct": l == p,
            }
        metrics["per_experiment"] = details
        result["thresholds"][str(thr)] = metrics

    auroc = compute_auroc(labels, scores)
    ci = bootstrap_auroc(labels, scores)
    result["auroc"] = auroc
    result["auroc_ci_95"] = ci

    return result


def main():
    print("Loading metrics...")
    all_data = {}
    for exp_id in DIR_MAP:
        all_data[exp_id] = load_metrics(exp_id)
        steps_35k = [d for d in all_data[exp_id] if d["step"] >= MIN_STEP]
        print(f"  {exp_id}: {len(all_data[exp_id])} total points, {len(steps_35k)} at 35K+")

    baseline_data = all_data["exp_001_baseline"]
    all_nve = {}

    print("\nComputing NVE (35K+ window)...")
    for exp_id in DIR_MAP:
        nve = compute_nve(all_data[exp_id], baseline_data)
        if nve:
            max_nve = max(nve.values())
            all_nve[exp_id] = {
                "max_nve": max_nve,
                "trajectory": {str(k): round(v, 6) for k, v in sorted(nve.items())},
            }
            print(f"  {exp_id}: max_nve_35K+ = {max_nve:.4f} ({len(nve)} points)")
        else:
            all_nve[exp_id] = {"max_nve": 0.0, "trajectory": {}}
            print(f"  {exp_id}: NO 35K+ data available!")

    # Task A: detect trained dt_emb presence
    task_a_pos = [
        "exp_006_fixed_dt2", "exp_008d_subsample_on_h8",
        "exp_008e_v3_walker_s1", "exp_008e_v3_walker_s2",
        "exp_009b_008d_walker_s2",
    ]
    task_a_neg = [
        "exp_001_baseline", "exp_008a_no_subsample_dt2",
        "exp_008f_no_dt_embed_subsample_on_h8",
    ]
    task_a = run_task(
        "detect trained dt_emb presence",
        task_a_pos, task_a_neg, [1.3, 1.5, 1.7, 2.0], all_nve,
    )

    # Task B1: predict CIVO collapse (009b = negative = self-corrected)
    task_b1_pos = [
        "exp_006_fixed_dt2", "exp_008d_subsample_on_h8",
        "exp_008e_v3_walker_s2",
    ]
    task_b1_neg = [
        "exp_001_baseline", "exp_008a_no_subsample_dt2",
        "exp_008f_no_dt_embed_subsample_on_h8",
        "exp_008e_v3_walker_s1", "exp_009b_008d_walker_s2",
    ]
    task_b1 = run_task(
        "predict CIVO collapse (009b=negative)",
        task_b1_pos, task_b1_neg, [1.5, 1.7, 2.0, 2.5], all_nve,
    )

    # Task B2: predict CIVO collapse (009b = positive = transient CIVO)
    task_b2_pos = [
        "exp_006_fixed_dt2", "exp_008d_subsample_on_h8",
        "exp_008e_v3_walker_s2", "exp_009b_008d_walker_s2",
    ]
    task_b2_neg = [
        "exp_001_baseline", "exp_008a_no_subsample_dt2",
        "exp_008f_no_dt_embed_subsample_on_h8",
        "exp_008e_v3_walker_s1",
    ]
    task_b2 = run_task(
        "predict CIVO collapse (009b=positive)",
        task_b2_pos, task_b2_neg, [1.5, 1.7, 2.0, 2.5], all_nve,
    )

    output = {
        "window": "35K+",
        "per_experiment": {},
        "task_a": task_a,
        "task_b1": task_b1,
        "task_b2": task_b2,
    }

    for exp_id in DIR_MAP:
        output["per_experiment"][exp_id] = {
            "max_nve_35K_plus": round(all_nve[exp_id]["max_nve"], 6),
            "nve_trajectory_35K_plus": all_nve[exp_id]["trajectory"],
            "n_points_35K_plus": len(all_nve[exp_id]["trajectory"]),
        }

    os.makedirs(ARTIFACTS, exist_ok=True)
    outpath = os.path.join(ARTIFACTS, "nve_threshold_v3.json")
    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {outpath}")

    # Readable summary
    print("\n" + "=" * 80)
    print("NVE THRESHOLD ANALYSIS v3 — 35K+ WINDOW")
    print("=" * 80)

    print("\n--- Per-Experiment max_nve (35K+) ---")
    for exp_id in sorted(all_nve, key=lambda x: all_nve[x]["max_nve"], reverse=True):
        info = all_nve[exp_id]
        n = len(info["trajectory"])
        print(f"  {exp_id:45s}  max_nve={info['max_nve']:.4f}  ({n} pts)")

    for task_key, task_data in [("Task A", task_a), ("Task B1", task_b1), ("Task B2", task_b2)]:
        print(f"\n--- {task_key}: {task_data['label']} ---")
        print(f"  AUROC = {task_data['auroc']}   95% CI = {task_data['auroc_ci_95']}")
        for thr, m in task_data["thresholds"].items():
            print(f"  thr={thr:>4s}: Acc={m['accuracy']:.4f}  P={m['precision']:.4f}  "
                  f"R={m['recall']:.4f}  F1={m['f1']:.4f}  "
                  f"(TP={m['TP']} TN={m['TN']} FP={m['FP']} FN={m['FN']})")


if __name__ == "__main__":
    main()
