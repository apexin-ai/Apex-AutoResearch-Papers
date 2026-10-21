#!/usr/bin/env python3
"""LLaMA-3.1-8B ProofWriter NLI Combo using D116's DeBERTa-large predictions.

DeBERTa-large-mnli predictions are deterministic on the same 600 PW problems
regardless of generator model, so we reuse D116's per_question results directly.
"""

import json
import os
from collections import Counter
from scipy.stats import binomtest

EXP048_PATH = "/root/symb_invariant_consensus/results/exp048_llama8b_pw600/exp048_results.json"
D116_PATH = "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/exp092_llama8b_pw_nli_combo"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]


def mcnemar_test(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(EXP048_PATH) as f:
        exp048 = json.load(f)
    with open(D116_PATH) as f:
        d116 = json.load(f)

    results_list = exp048["results"]
    d116_pq = d116["per_question"]
    total = len(results_list)
    print(f"Loaded {total} problems from exp048 (LLaMA-3.1-8B PW600)")

    gt = {}
    sc_answers = {}
    sc_vote_dists = {}
    for r in results_list:
        pid = r["problem_id"]
        gt[pid] = r["ground_truth"]
        sc_answers[pid] = r["sc_answer"]
        sc_vote_dists[pid] = r["sc_vote_distribution"]

    missing = [pid for pid in gt if pid not in d116_pq]
    if missing:
        print(f"WARNING: {len(missing)} problems missing from D116!")
        for m in missing[:5]:
            print(f"  {m}")
    else:
        print("All 600 problem_ids match D116 DeBERTa predictions.")

    gold_mismatch = [pid for pid in gt if pid in d116_pq and d116_pq[pid]["gold"] != gt[pid]]
    if gold_mismatch:
        print(f"ERROR: {len(gold_mismatch)} gold label mismatches!")
        return
    print("Gold labels verified: all match.")

    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])
    sc_acc = sc_correct_n / total
    print(f"\nSC baseline (LLaMA-3.1-8B, K=12): {sc_acc:.4f} ({sc_correct_n}/{total})")

    deberta_preds = {pid: d116_pq[pid]["deberta_pred"] for pid in gt}
    deberta_probs_dict = {pid: d116_pq[pid]["deberta_probs"] for pid in gt}
    deberta_correct_n = sum(1 for pid in gt if deberta_preds[pid] == gt[pid])
    deberta_acc = deberta_correct_n / total
    print(f"DeBERTa-large standalone: {deberta_acc:.4f} ({deberta_correct_n}/{total})")
    print(f"Capability gap: {(deberta_acc - sc_acc)*100:.2f}pp")

    gt_dist = Counter(gt.values())
    pred_dist = Counter(deberta_preds.values())
    per_class = {}
    for cls in CLASSES:
        n_cls = gt_dist.get(cls, 0)
        if n_cls == 0:
            continue
        correct_cls = sum(1 for pid in gt if gt[pid] == cls and deberta_preds[pid] == cls)
        tp = correct_cls
        fp = sum(1 for pid in gt if gt[pid] != cls and deberta_preds[pid] == cls)
        fn = n_cls - correct_cls
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        per_class[cls] = {
            "n": n_cls,
            "correct": correct_cls,
            "accuracy": round(correct_cls / n_cls, 4),
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4)
        }

    nli_right_sc_wrong = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] != gt[pid])
    sc_right_nli_wrong = sum(1 for pid in gt if sc_answers[pid] == gt[pid] and deberta_preds[pid] != gt[pid])
    both_right = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] == gt[pid])
    both_wrong = sum(1 for pid in gt if deberta_preds[pid] != gt[pid] and sc_answers[pid] != gt[pid])

    print(f"\n=== Complementarity ===")
    print(f"  NLI right, SC wrong: {nli_right_sc_wrong}")
    print(f"  SC right, NLI wrong: {sc_right_nli_wrong}")
    print(f"  Both right: {both_right}")
    print(f"  Both wrong: {both_wrong}")

    combo_results = {}
    print(f"\n=== Combo Results ===")
    for w in WEIGHTS:
        combo_correct = 0
        b_count = 0
        c_count = 0
        for pid in gt:
            votes = dict(sc_vote_dists[pid])
            nli_pred = deberta_preds[pid]
            votes[nli_pred] = votes.get(nli_pred, 0) + w
            _max = max(votes.values()); combo_answer = sorted(k for k, v in votes.items() if v == _max)[0]
            combo_is_correct = combo_answer == gt[pid]
            sc_correct = sc_answers[pid] == gt[pid]
            if combo_is_correct:
                combo_correct += 1
            if combo_is_correct and not sc_correct:
                b_count += 1
            if not combo_is_correct and sc_correct:
                c_count += 1

        combo_acc = combo_correct / total
        delta = combo_acc - sc_acc
        p_val = mcnemar_test(b_count, c_count)

        combo_results[w] = {
            "accuracy": round(combo_acc, 4),
            "correct": combo_correct,
            "delta_vs_sc": round(delta, 4),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_b": b_count,
            "mcnemar_c": c_count,
            "mcnemar_n_discordant": b_count + c_count,
            "mcnemar_p": round(p_val, 4)
        }
        print(f"  w={w}: {combo_acc:.4f} ({combo_correct}/{total}), delta={delta*100:+.2f}pp, p={p_val:.4f}, discordant=[{b_count},{c_count}]")

    agree = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid])
    disagree = total - agree
    agree_correct = sum(1 for pid in gt if deberta_preds[pid] == sc_answers[pid] == gt[pid])
    disagree_deberta = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and deberta_preds[pid] == gt[pid])
    disagree_sc = sum(1 for pid in gt if deberta_preds[pid] != sc_answers[pid] and sc_answers[pid] == gt[pid])

    print(f"\n=== Agreement ===")
    if agree > 0:
        print(f"  Agree: {agree}/{total} ({agree/total:.4f}), acc={agree_correct/agree:.4f}")
    print(f"  Disagree: DeBERTa right={disagree_deberta}, SC right={disagree_sc}")

    output = {
        "experiment": "exp092: LLaMA-3.1-8B ProofWriter NLI Combo (DeBERTa-large reused from D116)",
        "verifier_model": "microsoft/deberta-large-mnli",
        "generator_model": "LLaMA-3.1-8B-Instruct",
        "dataset": "ProofWriter-D5-600",
        "n_questions": total,
        "standalone_accuracy": round(deberta_acc, 4),
        "sc_baseline": round(sc_acc, 4),
        "capability_gap_pp": round((deberta_acc - sc_acc) * 100, 2),
        "deberta_standalone": {
            "accuracy": round(deberta_acc, 4),
            "correct": deberta_correct_n,
            "total": total,
            "per_class": per_class,
            "gt_distribution": dict(gt_dist),
            "pred_distribution": dict(pred_dist),
            "note": "Reused from D116 (same 600 PW problems, NLI is generator-independent)"
        },
        "combo": {
            f"w{w}": {
                "accuracy": combo_results[w]["accuracy"],
                "delta_pp": combo_results[w]["delta_pp"],
                "mcnemar_p": combo_results[w]["mcnemar_p"],
                "discordant": [combo_results[w]["mcnemar_b"], combo_results[w]["mcnemar_c"]]
            }
            for w in WEIGHTS
        },
        "complementarity": {
            "nli_right_sc_wrong": nli_right_sc_wrong,
            "sc_right_nli_wrong": sc_right_nli_wrong,
            "both_right": both_right,
            "both_wrong": both_wrong
        },
        "combo_vs_sc_full": {f"w{w}": combo_results[w] for w in WEIGHTS},
        "agreement_vs_sc": {
            "agree": agree,
            "disagree": disagree,
            "agreement_rate": round(agree / total, 4),
            "agree_accuracy": round(agree_correct / agree, 4) if agree > 0 else 0,
            "disagree_deberta_correct": disagree_deberta,
            "disagree_sc_correct": disagree_sc
        },
        "per_question": {
            pid: {
                "deberta_pred": deberta_preds[pid],
                "deberta_probs": deberta_probs_dict[pid],
                "sc_answer": sc_answers[pid],
                "sc_vote_distribution": sc_vote_dists[pid],
                "gold": gt[pid],
                "deberta_correct": deberta_preds[pid] == gt[pid],
                "sc_correct": sc_answers[pid] == gt[pid]
            }
            for pid in gt
        }
    }

    out = os.path.join(OUTPUT_DIR, "results.json")
    with open(out, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
