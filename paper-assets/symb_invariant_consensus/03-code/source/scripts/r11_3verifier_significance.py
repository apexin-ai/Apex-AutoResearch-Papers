#!/usr/bin/env python3
"""R11: 3-verifier NLI combo significance with BH correction.

Verifiers: DeBERTa-large-MNLI, RoBERTa-large-MNLI, BART-large-MNLI
Generator: Mistral-7B on ProofWriter D5-600
"""

import json
import os
import time
import torch
import numpy as np
from collections import Counter
from scipy.stats import binomtest
from transformers import AutoTokenizer, AutoModelForSequenceClassification

PW_DATA = "/root/symb_invariant_consensus/data/proofwriter_full.json"
MISTRAL_VOTES_PATH = "/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json"
OUTPUT_PATH = "/root/symb_invariant_consensus/results/r11_3verifier_combo.json"
DEVICE = "cuda:2"
CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]

NLI_MODELS = {
    "DeBERTa-large-MNLI": "/root/autodl-tmp/models/deberta-large-mnli",
    "RoBERTa-large-MNLI": "/root/autodl-tmp/models/roberta-large-mnli",
    "BART-large-MNLI": "/root/autodl-tmp/models/bart-large-mnli",
}


def split_problem(problem_text):
    marker = "Determine whether the following statement is true, false, or unknown:"
    idx = problem_text.find(marker)
    if idx == -1:
        marker2 = "Determine whether the following statement is True, False, or Unknown:"
        idx = problem_text.find(marker2)
        if idx == -1:
            return problem_text, ""
        marker = marker2
    premise = problem_text[:idx].strip()
    hypothesis = problem_text[idx + len(marker):].strip()
    return premise, hypothesis


def resolve_label_map(model):
    id2label = model.config.id2label
    actual_map = {}
    for idx, label in id2label.items():
        lu = label.upper()
        if "ENTAIL" in lu:
            actual_map[int(idx)] = "True"
        elif "CONTRA" in lu:
            actual_map[int(idx)] = "False"
        else:
            actual_map[int(idx)] = "Unknown"
    return actual_map


def mcnemar_exact(correct_a, correct_b):
    b = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)
    c = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)
    n = b + c
    if n == 0:
        return 1.0, b, c
    result = binomtest(min(b, c), n, 0.5)
    return result.pvalue, b, c


def bh_correction(p_values):
    n = len(p_values)
    if n == 0:
        return []
    sorted_indices = sorted(range(n), key=lambda i: p_values[i])
    adjusted = [0.0] * n
    for rank, idx in enumerate(sorted_indices, 1):
        adjusted[idx] = p_values[idx] * n / rank
    for i in range(n - 2, -1, -1):
        idx = sorted_indices[i]
        next_idx = sorted_indices[i + 1]
        adjusted[idx] = min(adjusted[idx], adjusted[next_idx])
    return [min(p, 1.0) for p in adjusted]


def run_nli_inference(model_name, model_path, problems, pids, device):
    print(f"\n--- {model_name} ---")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    model.to(device)
    label_map = resolve_label_map(model)
    print(f"  Labels: {model.config.id2label} -> {label_map}")

    nli_preds = {}
    nli_probs = {}
    batch_size = 16
    t0 = time.time()

    for i in range(0, len(pids), batch_size):
        batch_pids = pids[i:i + batch_size]
        premises, hypotheses = [], []
        for pid in batch_pids:
            p, h = split_problem(problems[pid])
            premises.append(p)
            hypotheses.append(h)

        inputs = tokenizer(
            premises, hypotheses,
            return_tensors="pt", truncation=True, max_length=512, padding=True
        ).to(device)

        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1).cpu().numpy()

        for j, pid in enumerate(batch_pids):
            prob_dict = {label_map[k]: float(probs[j, k]) for k in label_map}
            nli_probs[pid] = {c: round(prob_dict.get(c, 0), 6) for c in CLASSES}
            nli_preds[pid] = max(CLASSES, key=lambda x: prob_dict.get(x, 0))

    elapsed = time.time() - t0
    print(f"  Inference: {elapsed:.1f}s")

    del model
    torch.cuda.empty_cache()

    return nli_preds, nli_probs


def sc_answer(votes):
    if not votes:
        return None
    return max(CLASSES, key=lambda x: votes.get(x, 0))


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    pw = json.load(open(PW_DATA))
    gt = {p["id"]: p["answer"] for p in pw}
    problems = {p["id"]: p["problem"] for p in pw}
    pids = sorted(gt.keys())
    n = len(pids)
    print(f"Loaded {n} ProofWriter problems")

    raw_votes = json.load(open(MISTRAL_VOTES_PATH))
    mistral_votes = {pid: {"True": v[0], "False": v[1], "Unknown": v[2]} for pid, v in raw_votes.items()}
    mistral_sc = {pid: sc_answer(mistral_votes.get(pid, {})) for pid in pids}
    sc_correct = [mistral_sc[pid] == gt[pid] for pid in pids]
    sc_acc = sum(sc_correct) / n
    print(f"Mistral SC baseline: {sum(sc_correct)}/{n} = {sc_acc:.4f}")

    results = {
        "task": "R11: 3-verifier NLI combo BH-corrected significance",
        "generator": "Mistral-7B-Instruct-v0.3",
        "dataset": "ProofWriter-D5-600",
        "n": n,
        "sc_baseline": round(sc_acc, 4),
        "sc_correct_count": sum(sc_correct),
        "verifiers": {},
        "three_verifier_combo": {},
    }

    all_nli_probs = {}
    all_nli_preds = {}
    all_p_values = []
    p_value_labels = []

    for model_name, model_path in NLI_MODELS.items():
        nli_preds, nli_probs_dict = run_nli_inference(model_name, model_path, problems, pids, DEVICE)
        all_nli_probs[model_name] = nli_probs_dict
        all_nli_preds[model_name] = nli_preds

        nli_correct = [nli_preds[pid] == gt[pid] for pid in pids]
        nli_acc = sum(nli_correct) / n

        verifier_result = {
            "model_path": model_path,
            "standalone_accuracy": round(nli_acc, 4),
            "standalone_correct": sum(nli_correct),
            "combo": {},
        }

        for w in WEIGHTS:
            combo_answers = []
            for pid in pids:
                sv = mistral_votes.get(pid, {})
                np_ = nli_probs_dict[pid]
                combined = {c: sv.get(c, 0) + w * np_.get(c, 0) for c in CLASSES}
                combo_answers.append(max(CLASSES, key=lambda x: combined[x]))

            combo_correct = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]
            combo_acc = sum(combo_correct) / n
            delta = combo_acc - sc_acc
            p, b, c = mcnemar_exact(sc_correct, combo_correct)

            verifier_result["combo"][f"w{w}"] = {
                "accuracy": round(combo_acc, 4),
                "correct": sum(combo_correct),
                "delta_pp": round(delta * 100, 2),
                "mcnemar_b": b,
                "mcnemar_c": c,
                "mcnemar_p": round(p, 6),
            }
            all_p_values.append(p)
            p_value_labels.append(f"{model_name}_w{w}")

        results["verifiers"][model_name] = verifier_result
        print(f"\n  {model_name}: standalone={nli_acc:.4f}")
        for w in WEIGHTS:
            r = verifier_result["combo"][f"w{w}"]
            print(f"    w{w}: acc={r['accuracy']:.4f} Δ={r['delta_pp']:+.2f}pp p={r['mcnemar_p']:.6f} (b={r['mcnemar_b']},c={r['mcnemar_c']})")

    # 3-verifier combined combo: average NLI probs from all 3 verifiers
    print("\n=== 3-Verifier Combined Combo ===")
    model_names = list(NLI_MODELS.keys())
    for w in WEIGHTS:
        combo_answers = []
        for pid in pids:
            sv = mistral_votes.get(pid, {})
            avg_nli = {}
            for c in CLASSES:
                avg_nli[c] = sum(all_nli_probs[mn][pid][c] for mn in model_names) / len(model_names)
            combined = {c: sv.get(c, 0) + w * avg_nli[c] for c in CLASSES}
            combo_answers.append(max(CLASSES, key=lambda x: combined[x]))

        combo_correct = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]
        combo_acc = sum(combo_correct) / n
        delta = combo_acc - sc_acc
        p, b, c_val = mcnemar_exact(sc_correct, combo_correct)

        results["three_verifier_combo"][f"w{w}"] = {
            "accuracy": round(combo_acc, 4),
            "correct": sum(combo_correct),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_b": b,
            "mcnemar_c": c_val,
            "mcnemar_p": round(p, 6),
        }
        all_p_values.append(p)
        p_value_labels.append(f"3verifier_avg_w{w}")
        print(f"  w{w}: acc={combo_acc:.4f} Δ={delta*100:+.2f}pp p={p:.6f} (b={b},c={c_val})")

    # 3-verifier majority vote combo: each verifier casts 1 vote, then add to SC
    print("\n=== 3-Verifier Majority Vote Combo ===")
    results["three_verifier_majority"] = {}
    for w in WEIGHTS:
        combo_answers = []
        for pid in pids:
            sv = mistral_votes.get(pid, {})
            nli_votes = {c: 0 for c in CLASSES}
            for mn in model_names:
                pred = all_nli_preds[mn][pid]
                nli_votes[pred] += 1
            combined = {c: sv.get(c, 0) + w * nli_votes[c] for c in CLASSES}
            combo_answers.append(max(CLASSES, key=lambda x: combined[x]))

        combo_correct = [ca == gt[pid] for ca, pid in zip(combo_answers, pids)]
        combo_acc = sum(combo_correct) / n
        delta = combo_acc - sc_acc
        p, b, c_val = mcnemar_exact(sc_correct, combo_correct)

        results["three_verifier_majority"][f"w{w}"] = {
            "accuracy": round(combo_acc, 4),
            "correct": sum(combo_correct),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_b": b,
            "mcnemar_c": c_val,
            "mcnemar_p": round(p, 6),
        }
        all_p_values.append(p)
        p_value_labels.append(f"3verifier_majority_w{w}")
        print(f"  w{w}: acc={combo_acc:.4f} Δ={delta*100:+.2f}pp p={p:.6f} (b={b},c={c_val})")

    # BH correction on all p-values
    adjusted = bh_correction(all_p_values)
    bh_results = []
    for i, (label, raw_p, adj_p) in enumerate(zip(p_value_labels, all_p_values, adjusted)):
        bh_results.append({
            "test": label,
            "raw_p": round(raw_p, 6),
            "bh_adjusted_p": round(adj_p, 6),
            "significant_005": adj_p < 0.05,
            "significant_010": adj_p < 0.10,
        })
        sig = "*" if adj_p < 0.05 else ("†" if adj_p < 0.10 else "")
        print(f"  {label}: raw={raw_p:.6f} BH={adj_p:.6f} {sig}")

    results["bh_correction"] = {
        "n_tests": len(all_p_values),
        "method": "Benjamini-Hochberg",
        "results": bh_results,
    }

    n_sig_005 = sum(1 for r in bh_results if r["significant_005"])
    n_sig_010 = sum(1 for r in bh_results if r["significant_010"])
    results["summary"] = {
        "n_significant_005": n_sig_005,
        "n_significant_010": n_sig_010,
        "n_tests": len(all_p_values),
        "conclusion": f"{n_sig_005}/{len(all_p_values)} tests significant at BH-corrected α=0.05"
    }

    # Save per-question data for reproducibility
    per_question = {}
    for pid in pids:
        pq = {
            "gold": gt[pid],
            "mistral_sc": mistral_sc[pid],
            "sc_correct": sc_correct[pids.index(pid)],
        }
        for mn in model_names:
            short = mn.split("-")[0].lower()
            pq[f"{short}_pred"] = all_nli_preds[mn][pid]
            pq[f"{short}_correct"] = all_nli_preds[mn][pid] == gt[pid]
            pq[f"{short}_probs"] = all_nli_probs[mn][pid]
        per_question[pid] = pq
    results["per_question"] = per_question

    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
