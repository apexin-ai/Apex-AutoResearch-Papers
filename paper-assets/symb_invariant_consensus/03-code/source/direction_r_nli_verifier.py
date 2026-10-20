#!/usr/bin/env python3
"""Direction R: External NLI Verifier for FOLIO logical reasoning.

Uses an encoder-only NLI model (architecturally independent from decoder-only LLMs)
as an external verifier to break confirmation bias in self-consistency.
"""

import argparse
import json
import os
import re
import time
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def parse_problem(problem_text):
    """Extract premises and hypothesis from FOLIO problem text."""
    m = re.search(
        r"Given the following premises:\n(.+?)\n\nDetermine whether the following conclusion is true, false, or uncertain:\n(.+)",
        problem_text,
        re.DOTALL,
    )
    if m:
        return m.group(1).strip(), m.group(2).strip()
    # fallback: split on "Determine"
    parts = problem_text.split("Determine whether the following conclusion is true, false, or uncertain:")
    if len(parts) == 2:
        premises = parts[0].replace("Given the following premises:", "").strip()
        hypothesis = parts[1].strip()
        return premises, hypothesis
    return problem_text, ""


def load_nli_model(model_name, device):
    """Load NLI model and tokenizer."""
    print(f"Loading NLI model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.to(device)
    model.eval()
    # detect label mapping
    id2label = model.config.id2label
    print(f"  Labels: {id2label}")
    return model, tokenizer, id2label


def nli_predict(model, tokenizer, id2label, premise, hypothesis, device):
    """Run NLI inference, return (label, probs_dict)."""
    inputs = tokenizer(
        premise, hypothesis,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True,
    ).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0]
    pred_idx = probs.argmax().item()
    pred_label = id2label[pred_idx]
    probs_dict = {id2label[i]: round(probs[i].item(), 4) for i in range(len(id2label))}
    return pred_label, probs_dict


# Map NLI labels to FOLIO answer space
NLI_TO_FOLIO = {
    "entailment": "True",
    "ENTAILMENT": "True",
    "contradiction": "False",
    "CONTRADICTION": "False",
    "neutral": "Unknown",
    "NEUTRAL": "Unknown",
    # some models use LABEL_0, etc.
    "LABEL_0": "contradiction",  # will be remapped
    "LABEL_1": "neutral",
    "LABEL_2": "entailment",
}


def map_nli_to_folio(nli_label):
    """Map NLI label to FOLIO answer (True/False/Unknown)."""
    mapped = NLI_TO_FOLIO.get(nli_label, nli_label)
    # handle double mapping for LABEL_x
    if mapped in NLI_TO_FOLIO:
        mapped = NLI_TO_FOLIO[mapped]
    return mapped


def sc_majority(answers):
    """Get SC majority vote from answer list."""
    valid = [a for a in answers if a in ("True", "False", "Unknown")]
    if not valid:
        return "Unknown"
    c = Counter(valid)
    return c.most_common(1)[0][0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="cross-encoder/nli-deberta-v3-base")
    parser.add_argument("--data", default="data/folio_full.json")
    parser.add_argument("--traces-dir", default="results/exp033_mistral_7b_folio204/")
    parser.add_argument("--output", default="results/direction_r_nli_small/results.json")
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    # Load data
    with open(args.data) as f:
        data = json.load(f)
    print(f"Loaded {len(data)} problems")

    # Load SC traces
    sc_matrix_path = os.path.join(args.traces_dir, "sc_answer_matrix.json")
    with open(sc_matrix_path) as f:
        sc_matrix = json.load(f)
    print(f"Loaded SC traces for {len(sc_matrix)} problems")

    # Load NLI model
    model, tokenizer, id2label = load_nli_model(args.model, device)

    # Run NLI on each problem
    results = []
    nli_correct = 0
    sc_correct = 0
    verifier_correct = 0
    combo_correct = 0
    total = 0

    label_stats = {"True": {"total": 0, "nli_correct": 0, "sc_correct": 0},
                   "False": {"total": 0, "nli_correct": 0, "sc_correct": 0},
                   "Unknown": {"total": 0, "nli_correct": 0, "sc_correct": 0}}

    t0 = time.time()

    for item in data:
        pid = item["id"]
        gt = item["answer"]
        premises, hypothesis = parse_problem(item["problem"])

        if not hypothesis:
            print(f"  WARNING: could not parse hypothesis for {pid}")
            continue

        # NLI prediction
        nli_label, nli_probs = nli_predict(model, tokenizer, id2label, premises, hypothesis, device)
        nli_answer = map_nli_to_folio(nli_label)

        # SC majority from traces
        sc_data = sc_matrix.get(pid, {})
        sc_answers = sc_data.get("answers", [])
        sc_vote = sc_majority(sc_answers)

        # Strategy 1: NLI standalone
        nli_is_correct = (nli_answer == gt)

        # Strategy 2: NLI-as-verifier
        # If NLI agrees with SC → keep SC; if disagrees → use NLI
        if nli_answer == sc_vote:
            verifier_answer = sc_vote  # agreement → high confidence
        else:
            verifier_answer = nli_answer  # disagreement → trust external verifier

        # Strategy 3: NLI-SICA-combo
        # Add NLI prediction as extra vote(s) to SC traces
        augmented_answers = list(sc_answers) + [nli_answer]
        combo_answer = sc_majority(augmented_answers)

        sc_is_correct = (sc_vote == gt)
        verifier_is_correct = (verifier_answer == gt)
        combo_is_correct = (combo_answer == gt)

        total += 1
        nli_correct += int(nli_is_correct)
        sc_correct += int(sc_is_correct)
        verifier_correct += int(verifier_is_correct)
        combo_correct += int(combo_is_correct)

        if gt in label_stats:
            label_stats[gt]["total"] += 1
            label_stats[gt]["nli_correct"] += int(nli_is_correct)
            label_stats[gt]["sc_correct"] += int(sc_is_correct)

        results.append({
            "id": pid,
            "ground_truth": gt,
            "premises_len": len(premises),
            "hypothesis_len": len(hypothesis),
            "nli_raw_label": nli_label,
            "nli_probs": nli_probs,
            "nli_answer": nli_answer,
            "sc_vote": sc_vote,
            "sc_distribution": dict(Counter(a for a in sc_answers if a in ("True", "False", "Unknown"))),
            "verifier_answer": verifier_answer,
            "combo_answer": combo_answer,
            "nli_correct": nli_is_correct,
            "sc_correct": sc_is_correct,
            "verifier_correct": verifier_is_correct,
            "combo_correct": combo_is_correct,
        })

    elapsed = time.time() - t0

    # Summary
    nli_acc = nli_correct / total if total > 0 else 0
    sc_acc = sc_correct / total if total > 0 else 0
    verifier_acc = verifier_correct / total if total > 0 else 0
    combo_acc = combo_correct / total if total > 0 else 0

    summary = {
        "model": args.model,
        "n_problems": total,
        "elapsed_seconds": round(elapsed, 1),
        "sc_baseline": {"accuracy": round(sc_acc, 4), "correct": sc_correct},
        "nli_standalone": {
            "accuracy": round(nli_acc, 4),
            "correct": nli_correct,
            "delta_vs_sc": round(nli_acc - sc_acc, 4),
        },
        "nli_as_verifier": {
            "accuracy": round(verifier_acc, 4),
            "correct": verifier_correct,
            "delta_vs_sc": round(verifier_acc - sc_acc, 4),
            "strategy": "agree→keep_SC, disagree→use_NLI",
        },
        "nli_sica_combo": {
            "accuracy": round(combo_acc, 4),
            "correct": combo_correct,
            "delta_vs_sc": round(combo_acc - sc_acc, 4),
            "strategy": "NLI_as_extra_vote_in_SC",
        },
        "per_label": {},
    }

    for label in ("True", "False", "Unknown"):
        s = label_stats[label]
        if s["total"] > 0:
            summary["per_label"][label] = {
                "total": s["total"],
                "nli_acc": round(s["nli_correct"] / s["total"], 4),
                "sc_acc": round(s["sc_correct"] / s["total"], 4),
                "nli_correct": s["nli_correct"],
                "sc_correct": s["sc_correct"],
            }

    # Disagreement analysis
    agree_count = sum(1 for r in results if r["nli_answer"] == r["sc_vote"])
    disagree_count = total - agree_count
    disagree_nli_right = sum(1 for r in results if r["nli_answer"] != r["sc_vote"] and r["nli_correct"])
    disagree_sc_right = sum(1 for r in results if r["nli_answer"] != r["sc_vote"] and r["sc_correct"])
    disagree_both_wrong = disagree_count - disagree_nli_right - disagree_sc_right

    summary["disagreement_analysis"] = {
        "agree": agree_count,
        "disagree": disagree_count,
        "disagree_nli_right": disagree_nli_right,
        "disagree_sc_right": disagree_sc_right,
        "disagree_both_wrong": disagree_both_wrong,
    }

    # Print summary
    print("\n" + "=" * 60)
    print("Direction R: External NLI Verifier Results")
    print("=" * 60)
    print(f"Model: {args.model}")
    print(f"Problems: {total}, Time: {elapsed:.1f}s")
    print()
    print(f"{'Strategy':<25} {'Acc':>8} {'Correct':>8} {'Delta':>8}")
    print("-" * 50)
    print(f"{'SC baseline':<25} {sc_acc:>7.2%} {sc_correct:>8}")
    print(f"{'NLI standalone':<25} {nli_acc:>7.2%} {nli_correct:>8} {nli_acc-sc_acc:>+7.2%}")
    print(f"{'NLI-as-verifier':<25} {verifier_acc:>7.2%} {verifier_correct:>8} {verifier_acc-sc_acc:>+7.2%}")
    print(f"{'NLI-SICA-combo':<25} {combo_acc:>7.2%} {combo_correct:>8} {combo_acc-sc_acc:>+7.2%}")
    print()
    print("Per-label NLI accuracy:")
    for label in ("True", "False", "Unknown"):
        s = label_stats[label]
        if s["total"] > 0:
            nacc = s["nli_correct"] / s["total"]
            sacc = s["sc_correct"] / s["total"]
            print(f"  {label:<10} NLI={nacc:.2%} ({s['nli_correct']}/{s['total']})  SC={sacc:.2%} ({s['sc_correct']}/{s['total']})")
    print()
    print(f"Agreement: {agree_count}/{total} ({agree_count/total:.1%})")
    print(f"Disagreement: {disagree_count}/{total}")
    print(f"  NLI right: {disagree_nli_right}, SC right: {disagree_sc_right}, Both wrong: {disagree_both_wrong}")

    # Save
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    output = {"summary": summary, "results": results}
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
