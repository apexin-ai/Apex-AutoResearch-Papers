#!/usr/bin/env python3
"""R11 Q3: 3-verifier BH analysis using canonical NLI predictions.

Loads DeBERTa per-question data from D116, runs RoBERTa/BART inference
using canonical models already on server, computes individual + ensemble
combos, McNemar tests, and BH correction.

Canonical expectations (from nli_multi_verifier_recomputed.json):
  SC baseline: 39.33% (236/600) [alphabetical tiebreaking]
  DeBERTa-large standalone: 55.0% (330/600)
  RoBERTa-large standalone: 37.67% (226/600)
  BART-large standalone: 46.17% (277/600)
"""

import json
import os
import sys
import time
import torch
import numpy as np
from collections import Counter
from scipy.stats import binomtest
from transformers import AutoTokenizer, AutoModelForSequenceClassification

PW_DATA = "/root/symb_invariant_consensus/data/proofwriter_full.json"
SC_VOTES = "/root/symb_invariant_consensus/data/mistral_pw600_sc_votes.json"
D116_PATH = "/root/symb_invariant_consensus/results/d116_qwen3_pw_deberta_large/results.json"
OUTPUT_PATH = "/root/symb_invariant_consensus/results/r11_3verifier_canonical.json"

MODELS = {
    "DeBERTa-large-MNLI": "/root/autodl-tmp/models/deberta-large-mnli",
    "RoBERTa-large-MNLI": "/root/autodl-tmp/models/roberta-large-mnli",
    "BART-large-MNLI": "/root/autodl-tmp/models/bart-large-mnli",
}

CLASSES = ["True", "False", "Unknown"]
WEIGHTS = [1, 3, 5]

CANONICAL_STANDALONE = {
    "DeBERTa-large-MNLI": (0.55, 330),
    "RoBERTa-large-MNLI": (0.3767, 226),
    "BART-large-MNLI": (0.4617, 277),
}


def map_nli_label(label_str):
    lu = label_str.upper()
    if "ENTAIL" in lu:
        return "True"
    if "CONTRA" in lu:
        return "False"
    return "Unknown"


def parse_problem(problem_text):
    for marker in [
        "\n\nDetermine whether the following statement is true, false, or unknown:\n",
        "Determine whether the following statement is true, false, or unknown:",
        "Determine whether the following statement is True, False, or Unknown:",
    ]:
        if marker in problem_text:
            parts = problem_text.split(marker, 1)
            return parts[0].strip(), parts[1].strip()
    return problem_text, ""


def sc_answer_alpha(votes_dict):
    if not votes_dict:
        return None
    max_count = max(votes_dict.values())
    tied = [c for c in CLASSES if votes_dict.get(c, 0) == max_count]
    return sorted(tied)[0]


def combo_answer_alpha(sc_votes, nli_probs, w):
    combined = {}
    for c in CLASSES:
        combined[c] = sc_votes.get(c, 0) + w * nli_probs.get(c, 0.0)
    max_score = max(combined.values())
    tied = [c for c in CLASSES if abs(combined[c] - max_score) < 1e-9]
    return sorted(tied)[0]


def ensemble_combo_answer_alpha(sc_votes, nli_probs_list, w):
    n_verifiers = len(nli_probs_list)
    combined = {}
    for c in CLASSES:
        avg_prob = sum(p.get(c, 0.0) for p in nli_probs_list) / n_verifiers
        combined[c] = sc_votes.get(c, 0) + w * avg_prob
    max_score = max(combined.values())
    tied = [c for c in CLASSES if abs(combined[c] - max_score) < 1e-9]
    return sorted(tied)[0]


def mcnemar_exact_2sided(b, c):
    n = b + c
    if n == 0:
        return 1.0
    return binomtest(min(b, c), n, 0.5).pvalue


def bh_correction(p_values):
    n = len(p_values)
    if n == 0:
        return []
    ranked_indices = sorted(range(n), key=lambda i: p_values[i])
    adjusted = [0.0] * n
    for rank_idx, orig_idx in enumerate(ranked_indices):
        adjusted[orig_idx] = p_values[orig_idx] * n / (rank_idx + 1)
    for i in range(n - 2, -1, -1):
        idx_curr = ranked_indices[i]
        idx_next = ranked_indices[i + 1]
        adjusted[idx_curr] = min(adjusted[idx_curr], adjusted[idx_next])
    return [min(p, 1.0) for p in adjusted]


def run_nli_inference(model_name, model_path, pw_data, device):
    print(f"\n{'='*60}")
    print(f"Loading {model_name}: {model_path}")

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.to(device)
    model.eval()

    id2label = model.config.id2label
    nli_to_pw = {int(k): map_nli_label(v) for k, v in id2label.items()}
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
            probs_all[qid] = {"True": 0.0, "False": 0.0, "Unknown": 1.0}
            continue

        inputs = tokenizer(premises, conclusion, return_tensors="pt",
                           truncation=True, max_length=512).to(device)
        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1)[0]

        prob_dict = {}
        for idx in nli_to_pw:
            label = nli_to_pw[idx]
            if label in prob_dict:
                prob_dict[label] += probs[idx].item()
            else:
                prob_dict[label] = probs[idx].item()

        for c in CLASSES:
            prob_dict.setdefault(c, 0.0)
        probs_all[qid] = {c: round(prob_dict[c], 6) for c in CLASSES}
        preds[qid] = max(CLASSES, key=lambda x: prob_dict.get(x, 0))

        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(pw_data)} ({time.time()-t0:.1f}s)")

    elapsed = time.time() - t0
    print(f"  Done: {elapsed:.1f}s")

    del model
    torch.cuda.empty_cache()

    return preds, probs_all


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    with open(PW_DATA) as f:
        pw_data = json.load(f)
    with open(SC_VOTES) as f:
        sc_votes_raw = json.load(f)

    gt = {q["id"]: q["answer"] for q in pw_data}
    pids = sorted(gt.keys())
    n = len(pids)
    print(f"Dataset: {n} questions")

    sc_votes = {}
    for pid in pids:
        v = sc_votes_raw.get(pid, [0, 0, 0])
        sc_votes[pid] = {"True": v[0], "False": v[1], "Unknown": v[2]}

    sc_answers = {pid: sc_answer_alpha(sc_votes[pid]) for pid in pids}
    sc_correct = {pid: (sc_answers[pid] == gt[pid]) for pid in pids}
    sc_n_correct = sum(sc_correct.values())
    sc_acc = sc_n_correct / n
    print(f"SC baseline: {sc_n_correct}/{n} = {sc_acc:.4f} ({sc_acc*100:.2f}%)")
    assert sc_n_correct == 236, f"SC baseline mismatch: {sc_n_correct} != 236"

    print("\n=== Loading DeBERTa predictions from D116 (no re-inference) ===")
    with open(D116_PATH) as f:
        d116 = json.load(f)

    deberta_probs = {}
    deberta_preds = {}
    for pid, qdata in d116["per_question"].items():
        deberta_preds[pid] = qdata["deberta_pred"]
        deberta_probs[pid] = {c: qdata["deberta_probs"].get(c, 0.0) for c in CLASSES}

    deberta_correct_n = sum(1 for pid in pids if deberta_preds.get(pid) == gt[pid])
    print(f"  DeBERTa standalone: {deberta_correct_n}/{n} = {deberta_correct_n/n:.4f}")
    exp_acc, exp_n = CANONICAL_STANDALONE["DeBERTa-large-MNLI"]
    assert deberta_correct_n == exp_n, f"DeBERTa standalone mismatch: {deberta_correct_n} != {exp_n}"
    print(f"  Matches canonical ({exp_n})")

    all_verifier_probs = {"DeBERTa-large-MNLI": deberta_probs}
    all_verifier_preds = {"DeBERTa-large-MNLI": deberta_preds}

    for model_name in ["RoBERTa-large-MNLI", "BART-large-MNLI"]:
        model_path = MODELS[model_name]
        preds, probs = run_nli_inference(model_name, model_path, pw_data, device)
        all_verifier_preds[model_name] = preds
        all_verifier_probs[model_name] = probs

        correct_n = sum(1 for pid in pids if preds.get(pid) == gt[pid])
        exp_acc, exp_n = CANONICAL_STANDALONE[model_name]
        print(f"  {model_name} standalone: {correct_n}/{n} = {correct_n/n:.4f}")
        if correct_n != exp_n:
            print(f"  WARNING: expected {exp_n}, got {correct_n}")
            print(f"  Proceeding with actual predictions (model is canonical)")
        else:
            print(f"  Matches canonical ({exp_n})")

    print("\n=== Computing individual verifier combos ===")

    all_tests = []
    per_verifier_results = {}

    for vname in ["DeBERTa-large-MNLI", "RoBERTa-large-MNLI", "BART-large-MNLI"]:
        vprobs = all_verifier_probs[vname]
        vpreds = all_verifier_preds[vname]

        standalone_n = sum(1 for pid in pids if vpreds.get(pid) == gt[pid])
        standalone_acc = standalone_n / n

        combo_results = {}
        for w in WEIGHTS:
            b_count = 0
            c_count = 0
            combo_answers = {}

            for pid in pids:
                ca = combo_answer_alpha(sc_votes[pid], vprobs.get(pid, {}), w)
                combo_answers[pid] = ca
                combo_is_correct = (ca == gt[pid])
                sc_is_correct = sc_correct[pid]
                if sc_is_correct and not combo_is_correct:
                    b_count += 1
                if not sc_is_correct and combo_is_correct:
                    c_count += 1

            combo_n_correct = sum(1 for pid in pids if combo_answers[pid] == gt[pid])
            combo_acc = combo_n_correct / n
            delta_pp = round((combo_acc - sc_acc) * 100, 2)
            p_val = mcnemar_exact_2sided(b_count, c_count)

            combo_results[f"w{w}"] = {
                "accuracy": round(combo_acc, 4),
                "correct": combo_n_correct,
                "delta_pp": delta_pp,
                "mcnemar_b": b_count,
                "mcnemar_c": c_count,
                "mcnemar_p": p_val,
            }
            all_tests.append((f"{vname}_w{w}", p_val))

            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
            print(f"  {vname} w={w}: {combo_acc:.4f} ({combo_n_correct}), "
                  f"d={delta_pp:+.2f}pp, b={b_count} c={c_count} p={p_val:.6f} {sig}")

        per_verifier_results[vname] = {
            "standalone_acc": round(standalone_acc, 4),
            "standalone_correct": standalone_n,
            "combo": combo_results,
        }

    print("\n=== Computing 3-verifier ensemble combo ===")

    ensemble_results = {}
    verifier_names = ["DeBERTa-large-MNLI", "RoBERTa-large-MNLI", "BART-large-MNLI"]

    for w in WEIGHTS:
        b_count = 0
        c_count = 0
        combo_answers = {}

        for pid in pids:
            probs_list = [all_verifier_probs[v].get(pid, {}) for v in verifier_names]
            ca = ensemble_combo_answer_alpha(sc_votes[pid], probs_list, w)
            combo_answers[pid] = ca
            combo_is_correct = (ca == gt[pid])
            sc_is_correct = sc_correct[pid]
            if sc_is_correct and not combo_is_correct:
                b_count += 1
            if not sc_is_correct and combo_is_correct:
                c_count += 1

        combo_n_correct = sum(1 for pid in pids if combo_answers[pid] == gt[pid])
        combo_acc = combo_n_correct / n
        delta_pp = round((combo_acc - sc_acc) * 100, 2)
        p_val = mcnemar_exact_2sided(b_count, c_count)

        ensemble_results[f"w{w}"] = {
            "accuracy": round(combo_acc, 4),
            "correct": combo_n_correct,
            "delta_pp": delta_pp,
            "mcnemar_b": b_count,
            "mcnemar_c": c_count,
            "mcnemar_p": p_val,
        }
        all_tests.append((f"ensemble_3v_w{w}", p_val))

        sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""
        print(f"  Ensemble w={w}: {combo_acc:.4f} ({combo_n_correct}), "
              f"d={delta_pp:+.2f}pp, b={b_count} c={c_count} p={p_val:.6f} {sig}")

    print("\n=== BH correction ===")
    test_labels = [t[0] for t in all_tests]
    raw_pvals = [t[1] for t in all_tests]
    adjusted_pvals = bh_correction(raw_pvals)

    n_sig_005 = sum(1 for p in adjusted_pvals if p < 0.05)
    n_sig_010 = sum(1 for p in adjusted_pvals if p < 0.10)

    bh_results = []
    for i, (label, raw_p) in enumerate(all_tests):
        adj_p = adjusted_pvals[i]
        sig = adj_p < 0.05
        bh_results.append({
            "test": label,
            "raw_p": round(raw_p, 8),
            "bh_adjusted_p": round(adj_p, 8),
            "significant_005": sig,
        })
        marker = "Y" if sig else " "
        print(f"  [{marker}] {label:<30} raw={raw_p:.6f}  adj={adj_p:.6f}")

    print(f"\n  {n_sig_005}/{len(all_tests)} significant at BH alpha=0.05")
    print(f"  {n_sig_010}/{len(all_tests)} significant at BH alpha=0.10")

    output = {
        "task": "R11 Q3: 3-verifier canonical BH analysis",
        "generator": "Mistral-7B-Instruct-v0.3",
        "dataset": "ProofWriter-D5-600",
        "n": n,
        "sc_baseline": {
            "accuracy": round(sc_acc, 4),
            "correct": sc_n_correct,
            "n": n,
            "tiebreaking": "alphabetical",
        },
        "per_verifier": per_verifier_results,
        "ensemble_3verifier": ensemble_results,
        "bh_correction": {
            "n_tests": len(all_tests),
            "method": "Benjamini-Hochberg",
            "all_raw_p": [round(p, 8) for p in raw_pvals],
            "all_adjusted_p": [round(p, 8) for p in adjusted_pvals],
            "n_significant_005": n_sig_005,
            "n_significant_010": n_sig_010,
            "results": bh_results,
        },
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
