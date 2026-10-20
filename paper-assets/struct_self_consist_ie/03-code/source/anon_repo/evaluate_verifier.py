#!/usr/bin/env python3
"""exp-019: Evaluate supervised verifier vs unsupervised baselines.

Computes selection F1, Spearman rho, and AUROC for the verifier and
all 5 unsupervised signals (LP, SJ, FK, EM, VC).

Usage:
    cd /root/autodl-tmp/struct_self_consist_ie
    python evaluate_verifier.py \
        --predictions output/exp_019_supervised_verifier/oof_predictions_ner.json \
        --data_path output/exp_012_rerun_1024/samples.jsonl \
        --subtask ner \
        --output_dir output/exp_019_supervised_verifier
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict

import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "code"))
from consistency import structural_consistency_soft_jaccard
from evaluation import per_instance_f1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Evaluate supervised verifier predictions")
    p.add_argument("--predictions", type=str, required=True,
                    help="OOF predictions JSON from train_supervised_verifier.py")
    p.add_argument("--data_path", type=str, required=True,
                    help="samples.jsonl (exp_012 format)")
    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "re"])
    p.add_argument("--output_dir", type=str, default="output/exp_019_supervised_verifier")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Per-sample unsupervised signals
# ---------------------------------------------------------------------------

def _surface_keys(sample: dict, subtask: str) -> frozenset:
    if subtask == "ner":
        return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))
    return frozenset(
        (r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])
    )


def per_sample_sj(samples: list[dict], subtask: str) -> list[float]:
    """Average pairwise soft Jaccard of each sample vs the rest."""
    n = len(samples)
    if n < 2:
        return [1.0] * n

    pairwise = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            sj = structural_consistency_soft_jaccard([samples[i], samples[j]], subtask=subtask)
            pairwise[i, j] = pairwise[j, i] = sj

    scores = []
    for i in range(n):
        vals = [pairwise[i, j] for j in range(n) if j != i]
        scores.append(float(np.mean(vals)))
    return scores


def per_sample_em(samples: list[dict], subtask: str) -> list[float]:
    """Fraction of other samples with identical surface-key sets."""
    n = len(samples)
    if n < 2:
        return [1.0] * n
    keys = [_surface_keys(s, subtask) for s in samples]
    return [
        sum(1 for j in range(n) if j != i and keys[j] == keys[i]) / (n - 1)
        for i in range(n)
    ]


def per_sample_vc(samples: list[dict], subtask: str) -> list[float]:
    """Fraction of each sample's items that appear in majority of samples."""
    n = len(samples)
    if n < 2:
        return [1.0] * n

    item_counts: Counter = Counter()
    sample_item_sets = []
    for s in samples:
        items = _surface_keys(s, subtask)
        sample_item_sets.append(items)
        for item in items:
            item_counts[item] += 1

    majority = {k for k, v in item_counts.items() if v > n / 2}

    scores = []
    for items in sample_item_sets:
        if not items and not majority:
            scores.append(1.0)
        elif not items:
            scores.append(0.0)
        else:
            scores.append(len(items & majority) / len(items))
    return scores


def per_sample_fk(samples: list[dict], subtask: str) -> list[float]:
    """Per-sample LOO Fleiss' Kappa: how much kappa drops when sample i is removed.

    Higher value = sample i is more consistent with the group.
    """
    from consistency import fleiss_kappa_surface

    n = len(samples)
    if n < 3:
        return [1.0] * n

    full_fk = fleiss_kappa_surface(samples, subtask=subtask)

    scores = []
    for i in range(n):
        loo = [samples[j] for j in range(n) if j != i]
        loo_fk = fleiss_kappa_surface(loo, subtask=subtask)
        scores.append(full_fk - loo_fk)
    return scores


# ---------------------------------------------------------------------------
# Evaluation helpers
# ---------------------------------------------------------------------------

def selection_f1_per_instance(preds_by_inst: dict, score_key: str) -> list[float]:
    """For each instance, select the sample with highest score_key, return its true_f1."""
    f1s = []
    for iid in sorted(preds_by_inst):
        ps = preds_by_inst[iid]
        best = max(ps, key=lambda x: x[score_key])
        f1s.append(best["true_f1"])
    return f1s


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # Load predictions
    with open(args.predictions) as f:
        pred_data = json.load(f)
    predictions = pred_data["predictions"]

    # Load raw instances
    instances = []
    with open(args.data_path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    inst_map = {inst["id"]: inst for inst in instances}

    # Group predictions by instance (sorted by sample_idx)
    by_inst = defaultdict(list)
    for p in predictions:
        by_inst[p["instance_id"]].append(p)
    for iid in by_inst:
        by_inst[iid].sort(key=lambda x: x["sample_idx"])

    # Compute per-sample unsupervised signals
    print(f"Computing unsupervised signals for {len(by_inst)} instances ...")
    for idx, iid in enumerate(sorted(by_inst)):
        inst = inst_map[iid]
        samples = inst["samples"]
        preds = by_inst[iid]

        sj = per_sample_sj(samples, args.subtask)
        em = per_sample_em(samples, args.subtask)
        vc = per_sample_vc(samples, args.subtask)
        fk = per_sample_fk(samples, args.subtask)

        for i, p in enumerate(preds):
            p["sj_score"] = sj[i]
            p["em_score"] = em[i]
            p["vc_score"] = vc[i]
            p["fk_score"] = fk[i]

        if (idx + 1) % 100 == 0:
            print(f"  {idx + 1}/{len(by_inst)} instances processed")

    all_preds = []
    for iid in sorted(by_inst):
        all_preds.extend(by_inst[iid])

    # --- Selection F1 ---
    signal_keys = {
        "Supervised Verifier": "predicted_score",
        "LogProb (LP)": "mean_logprob",
        "Soft Jaccard (SJ)": "sj_score",
        "Fleiss Kappa LOO (FK)": "fk_score",
        "Exact Match (EM)": "em_score",
        "Voting Conf (VC)": "vc_score",
    }

    true_f1_all = np.array([p["true_f1"] for p in all_preds])

    report = {"subtask": args.subtask, "n_instances": len(by_inst), "n_samples": len(all_preds)}
    results_table = []

    for name, key in signal_keys.items():
        scores = np.array([p[key] for p in all_preds])
        sel_f1s = selection_f1_per_instance(by_inst, key)

        rho, rho_p = spearmanr(scores, true_f1_all)
        if np.isnan(rho):
            rho, rho_p = 0.0, 1.0

        # AUROC: good/bad by median F1 threshold
        median_f1 = float(np.median(true_f1_all))
        binary = (true_f1_all > median_f1).astype(int)
        if len(set(binary)) == 2:
            auroc = float(roc_auc_score(binary, scores))
        else:
            auroc = float("nan")

        entry = {
            "method": name,
            "selection_f1": float(np.mean(sel_f1s)),
            "selection_f1_std": float(np.std(sel_f1s)),
            "spearman_rho": float(rho),
            "spearman_p": float(rho_p),
            "auroc": auroc,
        }
        results_table.append(entry)

    # Greedy baseline
    greedy_f1s = []
    for inst in instances:
        if "greedy" in inst:
            gf = per_instance_f1(inst["greedy"], inst["gold"], args.subtask)
        else:
            gf = per_instance_f1(inst["samples"][0], inst["gold"], args.subtask)
        greedy_f1s.append(gf)
    greedy_mean = float(np.mean(greedy_f1s))

    # Oracle & random
    oracle_f1s = selection_f1_per_instance(by_inst, "true_f1")
    oracle_mean = float(np.mean(oracle_f1s))
    random_mean = float(np.mean(true_f1_all))

    report["baselines"] = {
        "greedy_f1": greedy_mean,
        "oracle_f1": oracle_mean,
        "random_avg_f1": random_mean,
    }
    report["results"] = results_table

    # --- Print table ---
    print(f"\n{'='*80}")
    print(f"exp-019 Supervised Verifier Evaluation | subtask={args.subtask}")
    print(f"{'='*80}")
    print(f"Instances: {len(by_inst)}  |  Samples: {len(all_preds)}  |  Median F1: {float(np.median(true_f1_all)):.4f}")
    print(f"\nBaselines:")
    print(f"  Greedy   F1 = {greedy_mean:.4f}")
    print(f"  Random   F1 = {random_mean:.4f}")
    print(f"  Oracle   F1 = {oracle_mean:.4f}")
    print(f"\n{'Method':<28} {'Sel F1':>8} {'rho':>8} {'AUROC':>8}")
    print("-" * 56)
    for r in results_table:
        auroc_str = f"{r['auroc']:.4f}" if not np.isnan(r["auroc"]) else "  N/A "
        print(f"{r['method']:<28} {r['selection_f1']:>8.4f} {r['spearman_rho']:>8.4f} {auroc_str:>8}")
    print(f"{'='*80}\n")

    # Save report
    report_path = os.path.join(args.output_dir, f"eval_report_{args.subtask}.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Report saved -> {report_path}")


if __name__ == "__main__":
    main()
