#!/usr/bin/env python3
"""Dir-J1: DeBERTa-MNLI Verifier on LogiQA — Cross-dataset NLI escape test

For each LogiQA problem:
  - NLI(premise=context, hypothesis=choice_text) for each of 4 choices
  - Combined score = SC_votes[choice] + w * NLI_entailment_prob[choice]
  - Test w=1, w=3, w=5
"""

import json
import time
import re
import numpy as np
from pathlib import Path
from collections import Counter
from scipy.stats import binomtest

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "/root/autodl-tmp/models/deberta-base-mnli"
TRACE_DIR = Path("/root/symb_invariant_consensus/results/exp049b_mistral_logiqa200/intermediates")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/dir_j1_nli_logiqa")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DEVICE = "cpu"
WEIGHTS = [1, 3, 5]
CANONICAL = ["A", "B", "C", "D"]
# label ordering: 0=contradiction, 1=entailment, 2=neutral
ENTAILMENT_IDX = 1


def normalize_answer(raw, choices):
    if not raw:
        return None
    raw = raw.strip()
    if raw in CANONICAL:
        return raw
    m = re.match(r'^([A-D])\b', raw)
    if m:
        return m.group(1)
    for i, ch in enumerate(choices):
        ch_text = re.sub(r'^[A-D]\.\s*', '', ch).strip()
        if raw.lower() == ch_text.lower() or raw.lower() == ch.lower():
            return CANONICAL[i]
    return None


def get_sc_votes(traces, choices):
    votes = Counter()
    for tr in traces:
        ans = normalize_answer(tr["answer"], choices)
        if ans:
            votes[ans] += 1
    return votes


def sc_answer_from_votes(votes):
    if not votes:
        return None
    return max(CANONICAL, key=lambda x: votes.get(x, 0))


def run_nli_batch(model, tokenizer, premise, hypotheses, device):
    inputs = tokenizer(
        [premise] * len(hypotheses), hypotheses,
        return_tensors="pt", truncation=True, max_length=512, padding=True
    ).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    return probs[:, ENTAILMENT_IDX].cpu().numpy().tolist()


def mcnemar(sc_correct, combo_correct):
    b = sum(1 for s, c in zip(sc_correct, combo_correct) if not s and c)
    c = sum(1 for s, c in zip(sc_correct, combo_correct) if s and not c)
    n = b + c
    if n == 0:
        return 1.0, b, c
    result = binomtest(min(b, c), n, 0.5)
    return result.pvalue, b, c


def main():
    print("Loading model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
    model.to(DEVICE)
    print(f"Model on {DEVICE}")

    trace_files = sorted(TRACE_DIR.glob("logiqa_*.json"))
    print(f"Found {len(trace_files)} trace files")

    per_problem = []
    sc_answers_list = []
    gt_list = []
    nli_best_list = []

    t0 = time.time()
    for i, tf in enumerate(trace_files):
        with open(tf) as f:
            data = json.load(f)

        ctx = data["problem"]["context"]
        choices = data["problem"]["choices"]
        gt = data["problem"]["answer"]
        traces = data["sica_result"]["traces"]

        choice_texts = [re.sub(r'^[A-D]\.\s*', '', ch).strip() for ch in choices]

        sc_vote = get_sc_votes(traces, choices)
        sc_ans = sc_answer_from_votes(sc_vote)

        ent_probs = run_nli_batch(model, tokenizer, ctx, choice_texts, DEVICE)
        nli_best = CANONICAL[int(np.argmax(ent_probs))]

        rec = {
            "problem_id": data["problem"]["id"],
            "ground_truth": gt,
            "sc_votes": dict(sc_vote),
            "sc_answer": sc_ans,
            "nli_entailment_probs": {CANONICAL[j]: round(ent_probs[j], 6) for j in range(4)},
            "nli_best": nli_best,
        }
        per_problem.append(rec)
        sc_answers_list.append(sc_ans)
        gt_list.append(gt)
        nli_best_list.append(nli_best)

        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(trace_files)} ({time.time()-t0:.1f}s)")

    elapsed = time.time() - t0
    print(f"NLI done in {elapsed:.1f}s")

    sc_correct = [s == g for s, g in zip(sc_answers_list, gt_list)]
    sc_acc = sum(sc_correct) / len(sc_correct)
    nli_correct = [n == g for n, g in zip(nli_best_list, gt_list)]
    nli_acc = sum(nli_correct) / len(nli_correct)

    weight_results = {}
    for w in WEIGHTS:
        combo_answers = []
        for idx, rec in enumerate(per_problem):
            sv = rec["sc_votes"]
            np_ = rec["nli_entailment_probs"]
            combined = {ch: sv.get(ch, 0) + w * np_.get(ch, 0) for ch in CANONICAL}
            best = max(CANONICAL, key=lambda x: combined[x])
            combo_answers.append(best)
            rec[f"combo_w{w}"] = best
            rec[f"combined_w{w}"] = {k: round(v, 4) for k, v in combined.items()}

        combo_correct = [ca == g for ca, g in zip(combo_answers, gt_list)]
        combo_acc = sum(combo_correct) / len(combo_correct)
        delta = combo_acc - sc_acc
        p, b, c = mcnemar(sc_correct, combo_correct)

        weight_results[f"w={w}"] = {
            "combo_accuracy": round(combo_acc, 4),
            "sc_accuracy": round(sc_acc, 4),
            "delta_pp": round(delta * 100, 2),
            "mcnemar_p": round(p, 6),
            "discordant_b": b,
            "discordant_c": c,
        }

    output = {
        "experiment": "Dir-J1: DeBERTa-MNLI Verifier on LogiQA",
        "model": "cross-encoder/nli-deberta-base",
        "dataset": "LogiQA-200 (Mistral-7B traces, exp049b)",
        "n_problems": len(trace_files),
        "device": DEVICE,
        "elapsed_s": round(elapsed, 1),
        "sc_accuracy": round(sc_acc, 4),
        "nli_only_accuracy": round(nli_acc, 4),
        "weight_results": weight_results,
        "per_problem": per_problem,
    }

    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults -> {out_path}")
    print(f"SC accuracy:       {sc_acc:.4f} ({sum(sc_correct)}/{len(sc_correct)})")
    print(f"NLI-only accuracy: {nli_acc:.4f} ({sum(nli_correct)}/{len(nli_correct)})")
    for wk, wv in weight_results.items():
        print(f"  {wk}: combo={wv['combo_accuracy']:.4f}, d={wv['delta_pp']:+.2f}pp, p={wv['mcnemar_p']:.4f}, disc=({wv['discordant_b']},{wv['discordant_c']})")


if __name__ == "__main__":
    main()
