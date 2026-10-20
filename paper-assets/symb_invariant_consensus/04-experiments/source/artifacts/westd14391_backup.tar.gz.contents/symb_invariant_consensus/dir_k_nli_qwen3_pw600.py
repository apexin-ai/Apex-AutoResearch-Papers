#!/usr/bin/env python3
"""Dir-K: DeBERTa NLI Verifier on Qwen3-14B ProofWriter-D5 (600 questions)
SC/SICA baselines from exp033_qwen3_14b_pw600_nonthinking.
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
OUTPUT_DIR = "/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter"
MODEL_NAME = "/root/autodl-tmp/models/deberta-base-mnli"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]


def parse_problem(problem_text):
    marker = "\n\nDetermine whether the following statement is true, false, or unknown:\n"
    if marker in problem_text:
        parts = problem_text.split(marker, 1)
        return parts[0].strip(), parts[1].strip()
    return problem_text, ""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load traces
    with open(TRACES_PATH) as f:
        traces = json.load(f)

    # Load PW data for problem text
    with open(PW_DATA_PATH) as f:
        pw_data = json.load(f)
    pw_by_id = {q["id"]: q for q in pw_data}

    results_list = traces["results"]
    total = len(results_list)
    print(f"Loaded {total} problems from traces")

    # Extract baselines
    gt = {}
    sc_answers = {}
    sica_answers = {}
    sc_vote_dists = {}
    for r in results_list:
        pid = r["problem_id"]
        gt[pid] = r["ground_truth"]
        sc_answers[pid] = r["sc_answer"]
        sica_answers[pid] = r["sica_answer"]
        sc_vote_dists[pid] = r["sc_vote_distribution"]

    sc_correct_n = sum(1 for pid in gt if sc_answers[pid] == gt[pid])
    sc_acc = sc_correct_n / total
    sica_correct_n = sum(1 for pid in gt if sica_answers[pid] == gt[pid])
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
            nli_to_pw[int(idx)] = "True"
        elif "CONTRA" in lu:
            nli_to_pw[int(idx)] = "False"
        else:
            nli_to_pw[int(idx)] = "Unknown"
    print(f"NLI->PW: {nli_to_pw}")

    # DeBERTa standalone
    print("\n=== DeBERTa standalone ===")
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
    print(f"DeBERTa standalone: {deberta_acc:.4f} ({deberta_correct_n}/{total}), time={elapsed:.1f}s")

    # Per-class stats
    gt_dist = Counter(gt.values())
    pred_dist = Counter(deberta_preds.values())
    per_class = {}
    for cls in CLASSES:
        n_cls = sum(1 for pid in gt if gt[pid] == cls)
        correct_cls = sum(1 for pid in gt if gt[pid] == cls and deberta_preds[pid] == cls)
        pred_cls = sum(1 for pid in gt if deberta_preds[pid] == cls)
        precision = correct_cls / pred_cls if pred_cls > 0 else 0
        recall = correct_cls / n_cls if n_cls > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        per_class[cls] = {
            "n": n_cls, "correct": correct_cls,
            "accuracy": round(correct_cls / n_cls, 4) if n_cls > 0 else 0,
            "precision": round(precision, 4), "recall": round(recall, 4), "f1": round(f1, 4)
        }

    # Complementarity
    nli_right_sc_wrong = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] != gt[pid])
    sc_right_nli_wrong = sum(1 for pid in gt if sc_answers[pid] == gt[pid] and deberta_preds[pid] != gt[pid])
    both_right = sum(1 for pid in gt if deberta_preds[pid] == gt[pid] and sc_answers[pid] == gt[pid])
    both_wrong = sum(1 for pid in gt if deberta_preds[pid] != gt[pid] and sc_answers[pid] != gt[pid])
    print(f"\nComplementarity: NLI_right_SC_wrong={nli_right_sc_wrong}, SC_right_NLI_wrong={sc_right_nli_wrong}")
    print(f"  both_right={both_right}, both_wrong={both_wrong}")

    # Combo vs SC
    print("\n=== Combo vs SC ===")
    combo_results = {}
    for weight in WEIGHTS:
        combo_correct = 0
        b, c = 0, 0
        for pid in gt:
            gold = gt[pid]
            votes = Counter()
            for label, count in sc_vote_dists[pid].items():
                if label in CLASSES:
                    votes[label] += count
            dp = deberta_preds.get(pid)
            if dp in CLASSES:
                votes[dp] += weight
            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else "Unknown"
            if combo_answer == gold:
                combo_correct += 1
            sc_is_correct = (sc_answers[pid] == gold)
            combo_is_correct = (combo_answer == gold)
            if not sc_is_correct and combo_is_correct:
                b += 1
            if sc_is_correct and not combo_is_correct:
                c += 1
        combo_acc = combo_correct / total
        delta = combo_acc - sc_acc
        n_disc = b + c
        p_val = binomtest(min(b, c), n_disc, 0.5).pvalue if n_disc > 0 else 1.0
        combo_results[weight] = {
            "accuracy": round(combo_acc, 4),
            "correct": combo_correct,
            "delta_vs_sc": round(delta, 4),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_b": b, "mcnemar_c": c,
            "mcnemar_n_discordant": n_disc,
            "mcnemar_p": round(p_val, 6)
        }
        print(f"  w={weight}: acc={combo_acc:.4f} ({combo_correct}/{total}), delta={delta:+.4f} ({delta*100:+.2f}pp), McNemar p={p_val:.4f} (b={b},c={c})")

    # Combo vs SICA
    print("\n=== Combo vs SICA ===")
    sica_combo_results = {}
    for weight in WEIGHTS:
        sica_combo_correct = 0
        b_s, c_s = 0, 0
        for pid in gt:
            gold = gt[pid]
            votes = Counter()
            for label, count in sc_vote_dists[pid].items():
                if label in CLASSES:
                    votes[label] += count
            dp = deberta_preds.get(pid)
            if dp in CLASSES:
                votes[dp] += weight
            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else "Unknown"
            if combo_answer == gold:
                sica_combo_correct += 1
            sica_is_correct = (sica_answers[pid] == gold)
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
            "delta_pp": round(sica_delta * 100, 2),
            "mcnemar_b": b_s, "mcnemar_c": c_s, "mcnemar_p": round(p_val_s, 6)
        }
        print(f"  w={weight} vs SICA: acc={sica_combo_acc:.4f}, delta={sica_delta:+.4f} ({sica_delta*100:+.2f}pp), p={p_val_s:.4f}")

    # Agreement analysis
    print("\n=== DeBERTa vs SC agreement ===")
    agree = sum(1 for pid in gt if deberta_preds.get(pid) == sc_answers.get(pid))
    disagree = total - agree
    agree_correct = sum(1 for pid in gt if deberta_preds.get(pid) == sc_answers.get(pid) == gt[pid])
    disagree_deberta = sum(1 for pid in gt if deberta_preds.get(pid) != sc_answers.get(pid) and deberta_preds.get(pid) == gt[pid])
    disagree_sc = sum(1 for pid in gt if deberta_preds.get(pid) != sc_answers.get(pid) and sc_answers.get(pid) == gt[pid])
    print(f"  Agreement: {agree/total:.4f} ({agree}/{total})")
    if agree > 0:
        print(f"  Agree accuracy: {agree_correct/agree:.4f}")
    print(f"  Disagree: DeBERTa right={disagree_deberta}, SC right={disagree_sc}")

    # SICA agreement
    print("\n=== DeBERTa vs SICA agreement ===")
    sica_agree = sum(1 for pid in gt if deberta_preds.get(pid) == sica_answers.get(pid))
    sica_disagree = total - sica_agree
    sica_agree_correct = sum(1 for pid in gt if deberta_preds.get(pid) == sica_answers.get(pid) == gt[pid])
    sica_disagree_deberta = sum(1 for pid in gt if deberta_preds.get(pid) != sica_answers.get(pid) and deberta_preds.get(pid) == gt[pid])
    sica_disagree_sica = sum(1 for pid in gt if deberta_preds.get(pid) != sica_answers.get(pid) and sica_answers.get(pid) == gt[pid])
    print(f"  Agreement: {sica_agree/total:.4f} ({sica_agree}/{total})")
    if sica_agree > 0:
        print(f"  Agree accuracy: {sica_agree_correct/sica_agree:.4f}")
    print(f"  Disagree: DeBERTa right={sica_disagree_deberta}, SICA right={sica_disagree_sica}")

    # Save results
    output = {
        "experiment": "Dir-K: DeBERTa NLI Verifier on Qwen3-14B ProofWriter-D5",
        "model": "Qwen3-14B (non-thinking mode)",
        "nli_model": MODEL_NAME,
        "nli_model_note": "deberta-base-mnli (not large); Mistral PW600 experiment used deberta-large-mnli",
        "dataset": "ProofWriter-D5-OWA",
        "n_questions": total,
        "deberta_standalone": {
            "accuracy": round(deberta_acc, 4),
            "correct": deberta_correct_n, "total": total,
            "per_class": per_class,
            "gt_distribution": dict(gt_dist),
            "pred_distribution": dict(pred_dist),
            "inference_time_s": round(elapsed, 1)
        },
        "baselines": {
            "sc": round(sc_acc, 4), "sc_correct": sc_correct_n,
            "sica": round(sica_acc, 4), "sica_correct": sica_correct_n
        },
        "complementarity": {
            "nli_right_sc_wrong": nli_right_sc_wrong,
            "sc_right_nli_wrong": sc_right_nli_wrong,
            "both_right": both_right,
            "both_wrong": both_wrong
        },
        "combo_vs_sc": {f"w{w}": combo_results[w] for w in WEIGHTS},
        "combo_vs_sica": {f"w{w}": sica_combo_results[w] for w in WEIGHTS},
        "agreement_vs_sc": {
            "agree": agree, "disagree": disagree,
            "agreement_rate": round(agree / total, 4),
            "agree_accuracy": round(agree_correct / agree, 4) if agree > 0 else 0,
            "disagree_deberta_correct": disagree_deberta,
            "disagree_sc_correct": disagree_sc
        },
        "agreement_vs_sica": {
            "agree": sica_agree, "disagree": sica_disagree,
            "agreement_rate": round(sica_agree / total, 4),
            "agree_accuracy": round(sica_agree_correct / sica_agree, 4) if sica_agree > 0 else 0,
            "disagree_deberta_correct": sica_disagree_deberta,
            "disagree_sica_correct": sica_disagree_sica
        },
        "comparison_with_mistral": {
            "note": "Mistral-7B PW600 NLI (direction_r_nli_pw600): SC 39.33%, w=3 combo 42.83% (+3.50pp, p=0.013), used deberta-large-mnli",
            "qwen3_sc_baseline": round(sc_acc, 4),
            "mistral_sc_baseline": 0.3933
        },
        "per_question": {
            pid: {
                "deberta_pred": deberta_preds[pid],
                "deberta_probs": deberta_probs[pid],
                "sc_answer": sc_answers[pid],
                "sica_answer": sica_answers[pid],
                "gold": gt[pid],
                "deberta_correct": deberta_preds[pid] == gt[pid],
                "sc_correct": sc_answers[pid] == gt[pid],
                "sica_correct": sica_answers[pid] == gt[pid]
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
