#!/usr/bin/env python3
"""D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli
Replaces deberta-base-mnli (Dir-K) with deberta-large-mnli to match Dir-J3 (Mistral combo).
"""

import json
import os
import time
from collections import Counter
from scipy.stats import binomtest
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

TRACES_PATH = "/root/symb_invariant_consensus/results/exp033_qwen3_14b_pw600_nonthinking/results.json"
PW_DATA_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large"
MODEL_NAME = "/root/autodl-tmp/models/deberta-large-mnli"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]


def parse_problem(problem_text):
    marker = "\n\nDetermine whether the following statement is true, false, or unknown:\n"
    if marker in problem_text:
        parts = problem_text.split(marker, 1)
        return parts[0].strip(), parts[1].strip()
    return problem_text, ""


def mcnemar_test(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(TRACES_PATH) as f:
        traces = json.load(f)
    with open(PW_DATA_PATH) as f:
        pw_data = json.load(f)
    pw_by_id = {q["id"]: q for q in pw_data}

    results_list = traces["results"]
    total = len(results_list)
    print(f"Loaded {total} problems from traces")

    gt = {}
    sc_answers = {}
    sc_vote_dists = {}
    for r in results_list:
        pid = r["problem_id"]
        gt[pid] = r["ground_truth"]
        sc_answers[pid] = r["sc_answer"]
        sc_vote_dists[pid] = r["sc_vote_distribution"]

    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])
    sc_acc = sc_correct_n / total
    print(f"SC baseline: {sc_acc:.4f} ({sc_correct_n}/{total})")

    # Load DeBERTa-large-mnli
    print(f"\nLoading {MODEL_NAME}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()

    id2label = model.config.id2label
    print(f"Label mapping: {id2label}")
    nli_to_pw = {}
    for idx, label in id2label.items():
        lu = label.upper()
        if "ENTAIL" in lu:
            nli_to_pw[int(idx)] = "True"
        elif "CONTRA" in lu:
            nli_to_pw[int(idx)] = "False"
        else:
            nli_to_pw[int(idx)] = "Unknown"
    print(f"NLI->PW: {nli_to_pw}")

    # DeBERTa standalone
    print("\n=== DeBERTa-large standalone ===")
    deberta_preds = {}
    deberta_probs = {}
    t0 = time.time()

    problem_ids = list(gt.keys())
    for i, pid in enumerate(problem_ids):
        q = pw_by_id.get(pid)
        if not q:
            deberta_preds[pid] = "Unknown"
            deberta_probs[pid] = {}
            continue

        premises, conclusion = parse_problem(q["problem"])
        if not conclusion:
            deberta_preds[pid] = "Unknown"
            deberta_probs[pid] = {}
            continue

        inputs = tokenizer(premises, conclusion, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.softmax(outputs.logits, dim=-1)[0]
        pred_idx = probs.argmax().item()
        pred_label = nli_to_pw[pred_idx]

        deberta_preds[pid] = pred_label
        deberta_probs[pid] = {nli_to_pw[k]: round(probs[k].item(), 4) for k in nli_to_pw}

        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{total} done...")

    elapsed = time.time() - t0
    deberta_correct_n = sum(1 for pid in gt if deberta_preds[pid] == gt[pid])
    deberta_acc = deberta_correct_n / total
    print(f"DeBERTa-large standalone: {deberta_acc:.4f} ({deberta_correct_n}/{total}) in {elapsed:.1f}s")

    # Per-class stats
    gt_dist = Counter(gt.values())
    pred_dist = Counter(deberta_preds.values())
    per_class = {}
    for cls in CLASSES:
        n = sum(1 for pid in gt if gt[pid] == cls)
        correct = sum(1 for pid in gt if gt[pid] == cls and deberta_preds[pid] == cls)
        pred_n = sum(1 for pid in gt if deberta_preds[pid] == cls)
        precision = correct / pred_n if pred_n > 0 else 0
        recall = correct / n if n > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        per_class[cls] = {
            "n": n, "correct": correct, "accuracy": round(correct / n, 4) if n > 0 else 0,
            "precision": round(precision, 4), "recall": round(recall, 4), "f1": round(f1, 4)
        }

    # Complementarity
    nli_right_sc_wrong = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] != gt[pid])
    sc_right_nli_wrong = sum(1 for pid in gt if sc_answers[pid] == gt[pid] and deberta_preds[pid] != gt[pid])
    both_right = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] == gt[pid])
    both_wrong = sum(1 for pid in gt if deberta_preds[pid] != gt[pid] and sc_answers[pid] != gt[pid])
    print(f"\nComplementarity: NLI_right_SC_wrong={nli_right_sc_wrong}, SC_right_NLI_wrong={sc_right_nli_wrong}")
    print(f"  Both right={both_right}, Both wrong={both_wrong}")

    # Combo: SC + w * NLI
    print("\n=== Combo (SC + w*NLI) ===")
    combo_results = {}
    for w in WEIGHTS:
        combo_correct = 0
        b_count = 0
        c_count = 0

        for pid in gt:
            votes = dict(sc_vote_dists[pid])
            nli_pred = deberta_preds[pid]
            votes[nli_pred] = votes.get(nli_pred, 0) + w

            combo_answer = max(votes, key=votes.get)
            gold = gt[pid]
            sc_correct = sc_answers[pid] == gold
            combo_is_correct = combo_answer == gold

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

    # Agreement analysis
    agree = sum(1 for pid in gt if deberta_preds.get(pid) == sc_answers.get(pid))
    disagree = total - agree
    agree_correct = sum(1 for pid in gt if deberta_preds.get(pid) == sc_answers.get(pid) == gt[pid])
    disagree_deberta = sum(1 for pid in gt if deberta_preds.get(pid) != sc_answers.get(pid) and deberta_preds.get(pid) == gt[pid])
    disagree_sc = sum(1 for pid in gt if deberta_preds.get(pid) != sc_answers.get(pid) and sc_answers.get(pid) == gt[pid])

    print(f"\n=== Agreement ===")
    if agree > 0:
        print(f"  Agree: {agree}/{total} ({agree/total:.4f}), acc={agree_correct/agree:.4f}")
    print(f"  Disagree: DeBERTa right={disagree_deberta}, SC right={disagree_sc}")

    # Save results
    output = {
        "experiment": "D116: Qwen3-14B ProofWriter combo with DeBERTa-large-mnli",
        "verifier_model": "microsoft/deberta-large-mnli",
        "generator_model": "Qwen3-14B (non-thinking mode)",
        "dataset": "ProofWriter-D5-600",
        "n_questions": total,
        "standalone_accuracy": round(deberta_acc, 4),
        "sc_baseline": round(sc_acc, 4),
        "deberta_standalone": {
            "accuracy": round(deberta_acc, 4),
            "correct": deberta_correct_n, "total": total,
            "per_class": per_class,
            "gt_distribution": dict(gt_dist),
            "pred_distribution": dict(pred_dist),
            "inference_time_s": round(elapsed, 1)
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
            "agree": agree, "disagree": disagree,
            "agreement_rate": round(agree / total, 4),
            "agree_accuracy": round(agree_correct / agree, 4) if agree > 0 else 0,
            "disagree_deberta_correct": disagree_deberta,
            "disagree_sc_correct": disagree_sc
        },
        "per_question": {
            pid: {
                "deberta_pred": deberta_preds[pid],
                "deberta_probs": deberta_probs[pid],
                "sc_answer": sc_answers[pid],
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
