#!/usr/bin/env python3
"""Dir-J3: Multi-NLI-Verifier Comparison on ProofWriter-D5 (600 questions).
Compare DeBERTa / RoBERTa / BART NLI verifiers on Mistral-7B SC traces.
"""

import json
import os
import time
from collections import Counter
from scipy.stats import binomtest
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

PW_DATA_PATH = "/root/symb_invariant_consensus/data/proofwriter_full.json"
EXP046_PATH = "/root/symb_invariant_consensus/results/exp046_mistral_7b_pw600/exp046_results.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/dir_j3_nli_multi_verifier"
CLASSES = ["True", "False", "Unknown"]

MODELS = [
    {"name": "DeBERTa-MNLI", "hf_id": "/root/models/deberta-large-mnli"},
    {"name": "RoBERTa-MNLI", "hf_id": "roberta-large-mnli"},
    {"name": "BART-MNLI",    "hf_id": "facebook/bart-large-mnli"},
]

WEIGHTS = [1, 3, 5]


def parse_problem(problem_text):
    marker = "\n\nDetermine whether the following statement is true, false, or unknown:\n"
    if marker in problem_text:
        parts = problem_text.split(marker, 1)
        return parts[0].strip(), parts[1].strip()
    return problem_text, ""


def map_nli_label(label_str):
    lu = label_str.upper()
    if "ENTAIL" in lu:
        return "True"
    if "CONTRA" in lu:
        return "False"
    return "Unknown"


def run_nli_model(model_name, hf_id, pw_data, gt, device):
    print(f"\n{'='*60}")
    print(f"Loading {model_name}: {hf_id}")
    try:
        tokenizer = AutoTokenizer.from_pretrained(hf_id)
        model = AutoModelForSequenceClassification.from_pretrained(hf_id)
    except Exception as e:
        print(f"FAILED to load {model_name}: {e}")
        return None

    model.to(device)
    model.eval()

    id2label = model.config.id2label
    nli_to_pw = {idx: map_nli_label(lbl) for idx, lbl in id2label.items()}
    print(f"  id2label: {id2label}")
    print(f"  nli_to_pw: {nli_to_pw}")

    preds = {}
    probs_all = {}
    t0 = time.time()

    for i, q in enumerate(pw_data):
        qid = q["id"]
        premises, conclusion = parse_problem(q["problem"])
        if not conclusion:
            preds[qid] = "Unknown"
            probs_all[qid] = {}
            continue

        inputs = tokenizer(premises, conclusion, return_tensors="pt",
                           truncation=True, max_length=512).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1)[0]
        pred_idx = probs.argmax().item()
        preds[qid] = nli_to_pw[pred_idx]
        probs_all[qid] = {nli_to_pw[k]: round(probs[k].item(), 4) for k in id2label}

        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(pw_data)} done ({time.time()-t0:.0f}s)")

    elapsed = time.time() - t0
    print(f"  Inference done: {elapsed:.1f}s")

    del model
    torch.cuda.empty_cache() if torch.cuda.is_available() else None

    correct = sum(1 for qid in gt if preds.get(qid) == gt[qid])
    acc = correct / len(gt)
    print(f"  Standalone accuracy: {acc:.4f} ({correct}/{len(gt)})")

    per_class = {}
    for cls in CLASSES:
        n = sum(1 for qid in gt if gt[qid] == cls)
        c = sum(1 for qid in gt if gt[qid] == cls and preds.get(qid) == cls)
        per_class[cls] = {"n": n, "correct": c, "accuracy": round(c/n, 4) if n > 0 else 0}

    pred_dist = Counter(preds.values())

    return {
        "model_name": model_name,
        "hf_id": hf_id,
        "standalone_accuracy": round(acc, 4),
        "standalone_correct": correct,
        "per_class": per_class,
        "pred_distribution": dict(pred_dist),
        "inference_time_s": round(elapsed, 1),
        "preds": preds,
        "probs": probs_all,
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    with open(PW_DATA_PATH) as f:
        pw_data = json.load(f)
    with open(EXP046_PATH) as f:
        exp046 = json.load(f)

    gt = {q["id"]: q["answer"] for q in pw_data}
    total = len(gt)
    print(f"Dataset: {total} questions")

    exp046_by_id = {r["problem_id"]: r for r in exp046["results"]}
    sc_answers = {}
    sc_vote_dists = {}
    for qid in gt:
        r = exp046_by_id.get(qid)
        if r:
            sc_answers[qid] = r["sc_answer"]
            sc_vote_dists[qid] = r.get("sc_vote_distribution", {})
        else:
            sc_answers[qid] = None
            sc_vote_dists[qid] = {}

    sc_correct_n = sum(1 for qid in gt if sc_answers.get(qid) == gt[qid])
    sc_acc = sc_correct_n / total
    print(f"SC baseline: {sc_acc:.4f} ({sc_correct_n}/{total})")

    all_model_results = []

    for m in MODELS:
        result = run_nli_model(m["name"], m["hf_id"], pw_data, gt, device)
        if result is None:
            all_model_results.append({
                "model_name": m["name"], "hf_id": m["hf_id"],
                "status": "FAILED", "error": "model load failed"
            })
            continue

        preds = result["preds"]

        nli_right_sc_wrong = sum(1 for qid in gt if preds.get(qid) == gt[qid] and sc_answers.get(qid) != gt[qid])
        sc_right_nli_wrong = sum(1 for qid in gt if sc_answers.get(qid) == gt[qid] and preds.get(qid) != gt[qid])
        both_right = sum(1 for qid in gt if preds.get(qid) == gt[qid] and sc_answers.get(qid) == gt[qid])
        both_wrong = total - nli_right_sc_wrong - sc_right_nli_wrong - both_right

        combo_results = {}
        for w in WEIGHTS:
            combo_correct = 0
            b_count = 0
            c_count = 0
            for qid in gt:
                gold = gt[qid]
                votes = Counter()
                dist = sc_vote_dists.get(qid, {})
                for label, count in dist.items():
                    if label in CLASSES:
                        votes[label] += count
                dp = preds.get(qid)
                if dp in CLASSES:
                    votes[dp] += w
                combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"

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

            combo_results[f"w{w}"] = {
                "accuracy": round(combo_acc, 4),
                "correct": combo_correct,
                "delta_vs_sc": round(delta, 4),
                "delta_pp": round(delta * 100, 2),
                "mcnemar_b": b_count,
                "mcnemar_c": c_count,
                "mcnemar_n_discordant": n_disc,
                "mcnemar_p": round(p_val, 6),
            }

        result_entry = {
            "model_name": result["model_name"],
            "hf_id": result["hf_id"],
            "status": "OK",
            "standalone_accuracy": result["standalone_accuracy"],
            "standalone_correct": result["standalone_correct"],
            "per_class": result["per_class"],
            "pred_distribution": result["pred_distribution"],
            "inference_time_s": result["inference_time_s"],
            "complementarity": {
                "nli_right_sc_wrong": nli_right_sc_wrong,
                "sc_right_nli_wrong": sc_right_nli_wrong,
                "both_right": both_right,
                "both_wrong": both_wrong,
            },
            "combo_vs_sc": combo_results,
        }
        all_model_results.append(result_entry)

        print(f"\n  Combo results for {result['model_name']}:")
        for w in WEIGHTS:
            r = combo_results[f"w{w}"]
            print(f"    w={w}: acc={r['accuracy']:.4f}, Δ={r['delta_pp']:+.2f}pp, p={r['mcnemar_p']:.4f}")

    # Summary table
    print(f"\n{'='*80}")
    print("SUMMARY TABLE")
    print(f"{'='*80}")
    print(f"SC baseline: {sc_acc:.4f} ({sc_correct_n}/{total})")
    print()
    header = f"{'Verifier':<16} {'w':>3} {'Combo Acc':>10} {'SC Acc':>8} {'Δ (pp)':>8} {'McNemar p':>10}"
    print(header)
    print("-" * len(header))
    for mr in all_model_results:
        if mr.get("status") != "OK":
            print(f"{mr['model_name']:<16}  FAILED: {mr.get('error','')}")
            continue
        for w in WEIGHTS:
            r = mr["combo_vs_sc"][f"w{w}"]
            sig = "*" if r["mcnemar_p"] < 0.05 else ""
            print(f"{mr['model_name']:<16} {w:>3} {r['accuracy']:>10.4f} {sc_acc:>8.4f} {r['delta_pp']:>+8.2f} {r['mcnemar_p']:>9.4f}{sig}")

    print(f"\n{'='*80}")
    print("STANDALONE NLI ACCURACY")
    print(f"{'='*80}")
    for mr in all_model_results:
        if mr.get("status") != "OK":
            continue
        print(f"  {mr['model_name']:<16}: {mr['standalone_accuracy']:.4f}")
        for cls in CLASSES:
            pc = mr['per_class'][cls]
            print(f"    {cls:<10}: {pc['accuracy']:.4f} ({pc['correct']}/{pc['n']})")

    output = {
        "experiment": "dir_j3_nli_multi_verifier",
        "dataset": "ProofWriter-D5-OWA",
        "n_questions": total,
        "sc_baseline": {"accuracy": round(sc_acc, 4), "correct": sc_correct_n},
        "weights_tested": WEIGHTS,
        "device": device,
        "models": all_model_results,
    }

    out_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
