#!/usr/bin/env python3
"""Direction R: DeBERTa NLI Verifier for ProofWriter-D5 (600 questions)
Replicates FOLIO R experiment on ProofWriter to strengthen statistical evidence.
SC/SICA baselines from exp046_mistral_7b_pw600.
"""

import argparse
import json
import os
import time
from collections import Counter
from scipy.stats import binomtest
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

PW_DATA_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
EXP046_PATH = "/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/direction_r_nli_pw600"
MODEL_NAME = "/root/models/deberta-large-mnli"
CLASSES = ["True", "False", "Unknown"]


def parse_problem(problem_text):
    marker = "\n\nDetermine whether the following statement is true, false, or unknown:\n"
    if marker in problem_text:
        parts = problem_text.split(marker, 1)
        premises = parts[0].strip()
        conclusion = parts[1].strip()
    else:
        premises = problem_text
        conclusion = ""
    return premises, conclusion


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=0, help="Limit to first N questions (0=all)")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(PW_DATA_PATH) as f:
        pw_data = json.load(f)
    with open(EXP046_PATH) as f:
        exp046 = json.load(f)

    exp046_by_id = {r["problem_id"]: r for r in exp046["results"]}

    gt = {q["id"]: q["answer"] for q in pw_data}
    if args.n > 0:
        pw_data = pw_data[:args.n]
        gt = {q["id"]: q["answer"] for q in pw_data}

    total = len(gt)
    print(f"Dataset: {total} questions")

    # SC and SICA answers from exp046
    sc_answers = {}
    sica_answers = {}
    sc_vote_dists = {}
    for qid in gt:
        r = exp046_by_id.get(qid)
        if r:
            sc_answers[qid] = r["sc_answer"]
            sica_answers[qid] = r["sica_answer"]
            sc_vote_dists[qid] = r.get("sc_vote_distribution", {})
        else:
            sc_answers[qid] = None
            sica_answers[qid] = None
            sc_vote_dists[qid] = {}

    sc_correct_n = sum(1 for qid in gt if sc_answers.get(qid) == gt[qid])
    sc_acc = sc_correct_n / total
    sica_correct_n = sum(1 for qid in gt if sica_answers.get(qid) == gt[qid])
    sica_acc = sica_correct_n / total
    print(f"SC baseline: {sc_acc:.4f} ({sc_correct_n}/{total})")
    print(f"SICA baseline: {sica_acc:.4f} ({sica_correct_n}/{total})")

    # Load DeBERTa
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
            nli_to_pw[idx] = "True"
        elif "CONTRA" in lu:
            nli_to_pw[idx] = "False"
        else:
            nli_to_pw[idx] = "Unknown"
    print(f"NLI->PW: {nli_to_pw}")

    # === DeBERTa standalone ===
    print("\n=== DeBERTa standalone ===")
    deberta_preds = {}
    deberta_probs = {}
    t0 = time.time()

    for i, q in enumerate(pw_data):
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
        pred_label = nli_to_pw[pred_idx]

        deberta_preds[qid] = pred_label
        deberta_probs[qid] = {nli_to_pw[k]: round(probs[k].item(), 4) for k in nli_to_pw}

        if (i + 1) % 50 == 0 or (i + 1) == len(pw_data):
            print(f"  Processed {i+1}/{len(pw_data)}")

    elapsed = time.time() - t0
    print(f"  Inference: {elapsed:.1f}s for {len(pw_data)} questions")

    deberta_correct_n = sum(1 for qid in gt if deberta_preds.get(qid) == gt[qid])
    deberta_acc = deberta_correct_n / total
    print(f"  DeBERTa accuracy: {deberta_acc:.4f} ({deberta_correct_n}/{total})")

    # Per-class breakdown for DeBERTa
    per_class = {}
    for cls in CLASSES:
        ids_cls = [qid for qid in gt if gt[qid] == cls]
        n_cls = len(ids_cls)
        tp = sum(1 for qid in ids_cls if deberta_preds.get(qid) == cls)
        fp = sum(1 for qid in gt if gt[qid] != cls and deberta_preds.get(qid) == cls)
        fn = n_cls - tp
        p = tp / (tp + fp) if (tp + fp) > 0 else 0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0
        per_class[cls] = {
            "n": n_cls, "correct": tp,
            "accuracy": round(tp / n_cls, 4) if n_cls > 0 else 0,
            "precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4)
        }
    print(f"  Per-class: { {c: per_class[c]['accuracy'] for c in CLASSES} }")

    gt_dist = dict(Counter(gt.values()))
    pred_dist = dict(Counter(deberta_preds.values()))

    # === Complementarity analysis ===
    print("\n=== Complementarity ===")
    nli_right_sc_wrong = sum(1 for qid in gt if deberta_preds.get(qid) == gt[qid] and sc_answers.get(qid) != gt[qid])
    sc_right_nli_wrong = sum(1 for qid in gt if sc_answers.get(qid) == gt[qid] and deberta_preds.get(qid) != gt[qid])
    both_right = sum(1 for qid in gt if deberta_preds.get(qid) == gt[qid] and sc_answers.get(qid) == gt[qid])
    both_wrong = sum(1 for qid in gt if deberta_preds.get(qid) != gt[qid] and sc_answers.get(qid) != gt[qid])
    print(f"  NLI correct & SC wrong: {nli_right_sc_wrong}")
    print(f"  SC correct & NLI wrong: {sc_right_nli_wrong}")
    print(f"  Both correct: {both_right}")
    print(f"  Both wrong: {both_wrong}")

    # === Combo: DeBERTa vote added to SC votes ===
    print("\n=== Combo (DeBERTa + SC votes) ===")
    combo_results = {}
    for weight in [1, 3]:
        combo_correct = 0
        combo_preds = {}
        # McNemar: b = SC correct & combo wrong, c = SC wrong & combo correct
        b_count = 0
        c_count = 0
        for qid in gt:
            gold = gt[qid]
            dist = sc_vote_dists.get(qid, {})
            votes = Counter()
            for label, count in dist.items():
                if label in CLASSES:
                    votes[label] += count

            dp = deberta_preds.get(qid)
            if dp in CLASSES:
                votes[dp] += weight

            combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"
            combo_preds[qid] = combo_answer

            if combo_answer == gold:
                combo_correct += 1

            sc_is_correct = (sc_answers.get(qid) == gold)
            combo_is_correct = (combo_answer == gold)
            if sc_is_correct and not combo_is_correct:
                b_count += 1
            if not sc_is_correct and combo_is_correct:
                c_count += 1

        combo_acc = combo_correct / total
        delta = combo_acc - sc_acc
        n_disc = b_count + c_count
        p_val = binomtest(min(b_count, c_count), n_disc, 0.5).pvalue if n_disc > 0 else 1.0

        combo_results[weight] = {
            "accuracy": round(combo_acc, 4),
            "correct": combo_correct,
            "delta_vs_sc": round(delta, 4),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_b": b_count,
            "mcnemar_c": c_count,
            "mcnemar_n_discordant": n_disc,
            "mcnemar_p": round(p_val, 6)
        }
        sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
        print(f"  w={weight}: acc={combo_acc:.4f} ({combo_correct}/{total}), "
              f"delta={delta:+.4f} ({delta*100:+.2f}pp), "
              f"McNemar b={b_count} c={c_count} p={p_val:.4f} {sig}")

    print(f"\n  SC baseline: {sc_acc:.4f}")
    print(f"  SICA baseline: {sica_acc:.4f}")

    # === SICA combo ===
    print("\n=== Bonus: SICA combo ===")
    sica_combo_results = {}
    for weight in [1, 3]:
        sica_combo_correct = 0
        b_s = 0
        c_s = 0
        for qid in gt:
            gold = gt[qid]
            dist = sc_vote_dists.get(qid, {})
            votes = Counter()
            for label, count in dist.items():
                if label in CLASSES:
                    votes[label] += count
            dp = deberta_preds.get(qid)
            if dp in CLASSES:
                votes[dp] += weight
            combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"
            if combo_answer == gold:
                sica_combo_correct += 1
            sica_is_correct = (sica_answers.get(qid) == gold)
            combo_is_correct = (combo_answer == gold)
            if sica_is_correct and not combo_is_correct:
                b_s += 1
            if not sica_is_correct and combo_is_correct:
                c_s += 1
        sica_combo_acc = sica_combo_correct / total
        sica_delta = sica_combo_acc - sica_acc
        n_disc_s = b_s + c_s
        p_val_s = binomtest(min(b_s, c_s), n_disc_s, 0.5).pvalue if n_disc_s > 0 else 1.0
        sica_combo_results[weight] = {
            "accuracy": round(sica_combo_acc, 4),
            "delta_vs_sica": round(sica_delta, 4),
            "mcnemar_b": b_s, "mcnemar_c": c_s, "mcnemar_p": round(p_val_s, 6)
        }
        print(f"  w={weight} vs SICA: acc={sica_combo_acc:.4f}, delta={sica_delta:+.4f}, p={p_val_s:.4f}")

    # === DeBERTa vs SICA agreement ===
    print("\n=== DeBERTa vs SICA agreement ===")
    sica_agree = sum(1 for qid in gt if deberta_preds.get(qid) == sica_answers.get(qid))
    sica_disagree = total - sica_agree
    sica_agree_correct = sum(1 for qid in gt if deberta_preds.get(qid) == sica_answers.get(qid) == gt[qid])
    sica_disagree_deberta = sum(1 for qid in gt if deberta_preds.get(qid) != sica_answers.get(qid) and deberta_preds.get(qid) == gt[qid])
    sica_disagree_sica = sum(1 for qid in gt if deberta_preds.get(qid) != sica_answers.get(qid) and sica_answers.get(qid) == gt[qid])
    print(f"  Agreement: {sica_agree/total:.4f} ({sica_agree}/{total})")
    if sica_agree > 0:
        print(f"  Agree accuracy: {sica_agree_correct/sica_agree:.4f}")
    print(f"  Disagree: DeBERTa right={sica_disagree_deberta}, SICA right={sica_disagree_sica}")

    # Save results
    results = {
        "dataset": "ProofWriter-D5-OWA",
        "n_questions": total,
        "model": MODEL_NAME,
        "deberta_standalone": {
            "accuracy": round(deberta_acc, 4),
            "correct": deberta_correct_n, "total": total,
            "per_class": per_class,
            "gt_distribution": gt_dist,
            "pred_distribution": pred_dist,
            "inference_time_s": round(elapsed, 1)
        },
        "baselines": {"sc": round(sc_acc, 4), "sica": round(sica_acc, 4)},
        "complementarity": {
            "nli_right_sc_wrong": nli_right_sc_wrong,
            "sc_right_nli_wrong": sc_right_nli_wrong,
            "both_right": both_right,
            "both_wrong": both_wrong
        },
        "combo_vs_sc": {
            f"w{w}": combo_results[w] for w in [1, 3]
        },
        "combo_vs_sica": {
            f"w{w}": sica_combo_results[w] for w in [1, 3]
        },
        "deberta_sica_agreement": {
            "agree": sica_agree, "disagree": sica_disagree,
            "agree_accuracy": round(sica_agree_correct / sica_agree, 4) if sica_agree > 0 else 0,
            "disagree_deberta_correct": sica_disagree_deberta,
            "disagree_sica_correct": sica_disagree_sica
        },
        "per_question": {
            qid: {
                "deberta_pred": deberta_preds[qid],
                "deberta_probs": deberta_probs[qid],
                "sc_answer": sc_answers.get(qid),
                "sica_answer": sica_answers.get(qid),
                "gold": gt[qid],
                "deberta_correct": deberta_preds[qid] == gt[qid],
                "sc_correct": sc_answers.get(qid) == gt[qid],
                "sica_correct": sica_answers.get(qid) == gt[qid]
            }
            for qid in gt
        }
    }

    out = os.path.join(OUTPUT_DIR, "results.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")


if __name__ == "__main__":
    main()
