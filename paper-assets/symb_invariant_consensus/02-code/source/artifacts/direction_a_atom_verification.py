"""
Direction A: Multi-Stage Atom-Level Verification Pipeline (Pilot 20)
- Read exp-033 Mistral-7B traces (12 traces per problem)
- Split each trace into atomic claims (sentence-level)
- Use DeBERTa-large-MNLI to verify each atom against premises
- Keep only entailed atoms -> derive final answer
- Compare atom-verified SC vs raw SC vs SICA
"""

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


TRACE_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
MODEL_PATH = "/root/models/deberta-large-mnli"
NUM_PROBLEMS = 20
LABEL_MAP = {0: "contradiction", 1: "neutral", 2: "entailment"}
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_problem(idx):
    path = os.path.join(TRACE_DIR, f"folio_{idx}.json")
    with open(path) as f:
        return json.load(f)


def extract_premises_and_conclusion(problem_text):
    parts = problem_text.split("Determine whether the following conclusion is true, false, or uncertain:")
    premise_block = parts[0].replace("Given the following premises:\n", "").strip()
    conclusion = parts[1].strip() if len(parts) > 1 else ""
    return premise_block, conclusion


def split_into_atoms(trace_text):
    trace_text = trace_text.strip()
    trace_text = re.sub(r"\\boxed\{[^}]*\}", "", trace_text)
    trace_text = re.sub(r"\\\\boxed\{[^}]*\}", "", trace_text)
    trace_text = re.sub(r"Final answer:.*$", "", trace_text, flags=re.MULTILINE)

    lines = trace_text.split("\n")
    atoms = []
    for line in lines:
        line = line.strip()
        line = re.sub(r"^\d+[\.\)]\s*", "", line)
        if len(line) < 15:
            continue
        sentences = re.split(r'(?<=[.!?])\s+', line)
        for s in sentences:
            s = s.strip()
            if len(s) >= 15 and not s.lower().startswith(("to determine", "we need to", "let's", "let us", "now,")):
                atoms.append(s)
    return atoms


def classify_nli_batch(model, tokenizer, premises, hypotheses, batch_size=32):
    results = []
    for i in range(0, len(hypotheses), batch_size):
        batch_hyps = hypotheses[i:i+batch_size]
        batch_prems = [premises] * len(batch_hyps)
        encodings = tokenizer(
            batch_prems, batch_hyps,
            padding=True, truncation=True, max_length=512,
            return_tensors="pt"
        ).to(DEVICE)
        with torch.no_grad():
            logits = model(**encodings).logits
            preds = logits.argmax(dim=-1).cpu().tolist()
            probs = torch.softmax(logits, dim=-1).cpu().tolist()
        for j, (pred, prob) in enumerate(zip(preds, probs)):
            results.append({
                "label": LABEL_MAP[pred],
                "prob": {LABEL_MAP[k]: round(prob[k], 4) for k in range(3)},
            })
    return results


def derive_answer_from_atoms(verified_atoms, conclusion, nli_results_for_conclusion):
    support_count = 0
    contradict_count = 0

    for res in nli_results_for_conclusion:
        if res["label"] == "entailment":
            support_count += 1
        elif res["label"] == "contradiction":
            contradict_count += 1

    if support_count > contradict_count and support_count > 0:
        return "True"
    elif contradict_count > support_count and contradict_count > 0:
        return "False"
    else:
        return "Unknown"


def run_pilot():
    print("Loading DeBERTa NLI model...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH).to(DEVICE)
    model.eval()
    print(f"Model loaded on {DEVICE}")

    all_results = []
    total_atoms = 0
    total_entailed = 0
    total_contradicted = 0
    total_neutral = 0

    for idx in range(NUM_PROBLEMS):
        data = load_problem(idx)
        problem = data["problem"]
        sica = data["sica_result"]
        gt_answer = problem["answer"]

        premise_text, conclusion_text = extract_premises_and_conclusion(problem["problem"])
        traces = sica["traces"]

        raw_answers = []
        verified_answers = []
        problem_atom_counts = []

        for trace_obj in traces:
            trace_text = trace_obj["trace"]
            raw_answer = trace_obj.get("answer", "")
            if raw_answer:
                raw_answers.append(raw_answer)

            atoms = split_into_atoms(trace_text)
            problem_atom_counts.append(len(atoms))

            if not atoms:
                verified_answers.append("Unknown")
                continue

            nli_results = classify_nli_batch(model, tokenizer, premise_text, atoms)

            entailed_atoms = []
            for atom, nli_res in zip(atoms, nli_results):
                if nli_res["label"] == "entailment":
                    entailed_atoms.append(atom)
                    total_entailed += 1
                elif nli_res["label"] == "contradiction":
                    total_contradicted += 1
                else:
                    total_neutral += 1
            total_atoms += len(atoms)

            if not entailed_atoms:
                verified_answers.append("Unknown")
                continue

            conclusion_nli = classify_nli_batch(
                model, tokenizer,
                " ".join(entailed_atoms),
                [conclusion_text]
            )
            v_answer = derive_answer_from_atoms(entailed_atoms, conclusion_text, conclusion_nli)
            verified_answers.append(v_answer)

        raw_sc = Counter(raw_answers).most_common(1)[0][0] if raw_answers else "Unknown"
        verified_sc = Counter(verified_answers).most_common(1)[0][0] if verified_answers else "Unknown"
        sica_answer = sica["answer"]

        all_results.append({
            "id": problem["id"],
            "gt": gt_answer,
            "raw_sc": raw_sc,
            "verified_sc": verified_sc,
            "sica": sica_answer,
            "raw_answers": dict(Counter(raw_answers)),
            "verified_answers": dict(Counter(verified_answers)),
            "atom_stats": {
                "mean": round(sum(problem_atom_counts) / max(len(problem_atom_counts), 1), 1),
                "min": min(problem_atom_counts) if problem_atom_counts else 0,
                "max": max(problem_atom_counts) if problem_atom_counts else 0,
            },
        })

        status = "✓" if verified_sc == gt_answer else "✗"
        print(f"  [{idx:2d}] GT={gt_answer:7s} | RawSC={raw_sc:7s} | AtomSC={verified_sc:7s} | SICA={sica_answer:7s} {status}")

    # Summary
    raw_correct = sum(1 for r in all_results if r["raw_sc"] == r["gt"])
    verified_correct = sum(1 for r in all_results if r["verified_sc"] == r["gt"])
    sica_correct = sum(1 for r in all_results if r["sica"] == r["gt"])
    n = len(all_results)

    print("\n" + "=" * 60)
    print(f"Results on {n} problems:")
    print(f"  Raw SC accuracy:          {raw_correct}/{n} = {raw_correct/n:.1%}")
    print(f"  Atom-verified SC accuracy: {verified_correct}/{n} = {verified_correct/n:.1%}")
    print(f"  SICA accuracy:            {sica_correct}/{n} = {sica_correct/n:.1%}")
    print(f"  Δ(AtomSC - RawSC):        {(verified_correct - raw_correct)/n:+.1%}")
    print(f"  Δ(AtomSC - SICA):         {(verified_correct - sica_correct)/n:+.1%}")

    all_atom_counts = []
    for r in all_results:
        all_atom_counts.append(r["atom_stats"]["mean"])
    print(f"\nAtom statistics (per trace):")
    print(f"  Mean atoms: {sum(all_atom_counts)/len(all_atom_counts):.1f}")
    print(f"  Min mean:   {min(all_atom_counts):.1f}")
    print(f"  Max mean:   {max(all_atom_counts):.1f}")

    print(f"\nNLI label distribution (total {total_atoms} atoms):")
    if total_atoms > 0:
        print(f"  Entailed:     {total_entailed} ({total_entailed/total_atoms:.1%})")
        print(f"  Contradicted: {total_contradicted} ({total_contradicted/total_atoms:.1%})")
        print(f"  Neutral:      {total_neutral} ({total_neutral/total_atoms:.1%})")

    # Per-problem detail
    print("\n" + "=" * 60)
    print("Per-problem breakdown:")
    for r in all_results:
        match_raw = "✓" if r["raw_sc"] == r["gt"] else "✗"
        match_ver = "✓" if r["verified_sc"] == r["gt"] else "✗"
        match_sica = "✓" if r["sica"] == r["gt"] else "✗"
        print(f"  {r['id']:10s} GT={r['gt']:7s} RawSC={r['raw_sc']:7s}{match_raw} "
              f"AtomSC={r['verified_sc']:7s}{match_ver} SICA={r['sica']:7s}{match_sica} "
              f"atoms={r['atom_stats']['mean']:.0f}")

    # Save detailed results
    out_path = "/root/symb_invariant_consensus/results/direction_a_atom_pilot20.json"
    with open(out_path, "w") as f:
        json.dump({
            "method": "direction_a_atom_verification",
            "num_problems": n,
            "accuracy": {
                "raw_sc": raw_correct / n,
                "atom_verified_sc": verified_correct / n,
                "sica": sica_correct / n,
            },
            "nli_distribution": {
                "total_atoms": total_atoms,
                "entailed": total_entailed,
                "contradicted": total_contradicted,
                "neutral": total_neutral,
            },
            "per_problem": all_results,
        }, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    run_pilot()
