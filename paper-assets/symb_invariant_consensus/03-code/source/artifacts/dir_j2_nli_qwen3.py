#!/usr/bin/env python3
"""Dir-J2: DeBERTa-MNLI Verifier on Qwen3-14B FOLIO Traces"""

import json
import os
import time
from collections import Counter
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from scipy.stats import binom_test

FOLIO_PATH = "/root/symb_invariant_consensus/data/folio_full.json"
QWEN3_RESULTS_PATH = "/root/symb_invariant_consensus/results/dir_i3_sica_qwen3_14b/results.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/dir_j2_nli_qwen3"
MODEL_NAME = "/root/models/deberta-large-mnli"
CLASSES = ["True", "False", "Unknown"]


def parse_problem(problem_text):
    marker = "Determine whether the following conclusion is true, false, or uncertain:\n"
    if marker in problem_text:
        parts = problem_text.split(marker, 1)
        premises = parts[0].replace("Given the following premises:\n", "").strip()
        conclusion = parts[1].strip()
    else:
        premises = problem_text
        conclusion = ""
    return premises, conclusion


def mcnemar_exact(b, c):
    n = b + c
    if n == 0:
        return 1.0
    p = binom_test(min(b, c), n, 0.5)
    return p


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(FOLIO_PATH) as f:
        folio = json.load(f)
    with open(QWEN3_RESULTS_PATH) as f:
        qwen3_data = json.load(f)

    qwen3_by_id = {r["problem_id"]: r for r in qwen3_data["per_problem"]}
    gt = {q["id"]: q["answer"] for q in folio}
    total = len(gt)
    assert total == 204, f"Expected 204 problems, got {total}"

    print(f"Loading {MODEL_NAME}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    model.eval()

    id2label = model.config.id2label
    nli_to_folio = {}
    for idx, label in id2label.items():
        lu = label.upper()
        if "ENTAIL" in lu:
            nli_to_folio[idx] = "True"
        elif "CONTRA" in lu:
            nli_to_folio[idx] = "False"
        else:
            nli_to_folio[idx] = "Unknown"
    print(f"NLI->FOLIO mapping: {nli_to_folio}")

    # DeBERTa inference
    print("\n=== DeBERTa standalone inference ===")
    deberta_preds = {}
    deberta_probs = {}
    t0 = time.time()

    for i, q in enumerate(folio):
        qid = q["id"]
        premises, conclusion = parse_problem(q["problem"])
        if not conclusion:
            deberta_preds[qid] = "Unknown"
            deberta_probs[qid] = {}
            continue

        inputs = tokenizer(premises, conclusion, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.softmax(outputs.logits, dim=-1)[0]
        pred_idx = probs.argmax().item()
        pred_label = nli_to_folio[pred_idx]

        deberta_preds[qid] = pred_label
        deberta_probs[qid] = {nli_to_folio[k]: round(probs[k].item(), 4) for k in nli_to_folio}

        if (i + 1) % 50 == 0:
            print(f"  Processed {i+1}/{len(folio)}")

    elapsed = time.time() - t0
    print(f"  Inference: {elapsed:.1f}s for {len(folio)} questions")

    deberta_correct = sum(1 for qid in gt if deberta_preds.get(qid) == gt[qid])
    deberta_acc = deberta_correct / total
    print(f"  DeBERTa standalone accuracy: {deberta_acc:.4f} ({deberta_correct}/{total})")

    # SC baseline from Qwen3-14B
    sc_answers = {}
    sc_correct_set = set()
    for qid in gt:
        r = qwen3_by_id.get(qid, {})
        sc_answers[qid] = r.get("sc_answer", "Unknown")
        if r.get("sc_correct", False):
            sc_correct_set.add(qid)
    sc_correct_count = len(sc_correct_set)
    sc_acc = sc_correct_count / total
    print(f"\n  SC baseline: {sc_acc:.4f} ({sc_correct_count}/{total})")

    # Combo: SC votes + w * NLI vote
    print("\n=== Combo: SC + DeBERTa NLI ===")
    combo_results = {}
    for w in [1, 3, 5]:
        combo_preds = {}
        combo_correct = 0
        for qid in gt:
            gold = gt[qid]
            r = qwen3_by_id.get(qid, {})
            sc_dist = r.get("sc_vote_distribution", {})

            votes = Counter()
            for ans, cnt in sc_dist.items():
                if ans in CLASSES:
                    votes[ans] += cnt

            dp = deberta_preds.get(qid)
            if dp in CLASSES:
                votes[dp] += w

            combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"
            combo_preds[qid] = combo_answer
            if combo_answer == gold:
                combo_correct += 1

        combo_acc = combo_correct / total
        combo_correct_set = {qid for qid in gt if combo_preds[qid] == gt[qid]}

        # McNemar vs SC
        b = len(combo_correct_set - sc_correct_set)  # combo right, SC wrong
        c = len(sc_correct_set - combo_correct_set)  # SC right, combo wrong
        p_val = mcnemar_exact(b, c)

        combo_results[w] = {
            "accuracy": round(combo_acc, 4),
            "accuracy_pct": round(combo_acc * 100, 2),
            "correct": combo_correct,
            "total": total,
            "delta_pp": round((combo_acc - sc_acc) * 100, 2),
            "mcnemar_p": round(p_val, 6),
            "discordant_b_combo_right_sc_wrong": b,
            "discordant_c_sc_right_combo_wrong": c,
        }
        print(f"  w={w}: acc={combo_acc:.4f} ({combo_correct}/{total}), "
              f"delta={combo_results[w]['delta_pp']:+.2f}pp, "
              f"McNemar p={p_val:.4f}, discordant (b={b}, c={c})")

    print(f"\n  SC baseline: {sc_acc:.4f} ({sc_correct_count}/{total})")

    # Agreement analysis
    agree = sum(1 for qid in gt if deberta_preds.get(qid) == sc_answers.get(qid))
    disagree = total - agree
    agree_correct = sum(1 for qid in gt if deberta_preds.get(qid) == sc_answers.get(qid) == gt[qid])
    disagree_deberta_right = sum(1 for qid in gt if deberta_preds.get(qid) != sc_answers.get(qid) and deberta_preds.get(qid) == gt[qid])
    disagree_sc_right = sum(1 for qid in gt if deberta_preds.get(qid) != sc_answers.get(qid) and sc_answers.get(qid) == gt[qid])
    disagree_both_wrong = disagree - disagree_deberta_right - disagree_sc_right

    print(f"\n=== Agreement analysis ===")
    print(f"  Agreement: {agree}/{total} ({agree/total:.4f})")
    print(f"  Agree correct: {agree_correct}/{agree}")
    print(f"  Disagree: {disagree} (DeBERTa right={disagree_deberta_right}, SC right={disagree_sc_right}, both wrong={disagree_both_wrong})")

    # Save
    results = {
        "experiment": "Dir-J2: DeBERTa-MNLI Verifier on Qwen3-14B FOLIO Traces",
        "model": "Qwen3-14B (thinking mode)",
        "nli_model": MODEL_NAME,
        "n_problems": total,
        "deberta_standalone": {
            "accuracy": round(deberta_acc, 4),
            "accuracy_pct": round(deberta_acc * 100, 2),
            "correct": deberta_correct,
            "total": total,
            "inference_time_s": round(elapsed, 1),
        },
        "sc_baseline": {
            "accuracy": round(sc_acc, 4),
            "accuracy_pct": round(sc_acc * 100, 2),
            "correct": sc_correct_count,
            "total": total,
        },
        "combo_results": {f"w={w}": combo_results[w] for w in [1, 3, 5]},
        "agreement_analysis": {
            "agree": agree,
            "disagree": disagree,
            "agreement_rate": round(agree / total, 4),
            "agree_correct": agree_correct,
            "disagree_deberta_right": disagree_deberta_right,
            "disagree_sc_right": disagree_sc_right,
            "disagree_both_wrong": disagree_both_wrong,
        },
        "per_question": {
            qid: {
                "deberta_pred": deberta_preds[qid],
                "deberta_probs": deberta_probs[qid],
                "sc_answer": sc_answers.get(qid),
                "gold": gt[qid],
                "deberta_correct": deberta_preds[qid] == gt[qid],
                "sc_correct": sc_answers.get(qid) == gt[qid],
            }
            for qid in gt
        },
    }

    out = os.path.join(OUTPUT_DIR, "results.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
