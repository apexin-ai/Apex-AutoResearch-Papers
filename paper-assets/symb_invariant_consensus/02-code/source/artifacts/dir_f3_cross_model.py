"""
Dir-F3: Cross-Model Constraint Verification
Qwen2.5-14B verifies constraints extracted by Mistral-7B.
"""
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import requests

QWEN_URL = "http://localhost:8011/v1/chat/completions"
QWEN_MODEL = None  # will be auto-detected
CONSTRAINT_CACHE_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/constraint_cache"
INTERMEDIATES_DIR = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates"
FOLIO_DATA = "/root/symb_invariant_consensus/data/folio_full.json"
SC_MATRIX = "/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/sc_answer_matrix.json"
OUTPUT_DIR = "/root/symb_invariant_consensus/results/dir_f3_cross_model_verification"
N_QUESTIONS = 30


def detect_model():
    """Auto-detect the model name from vLLM."""
    resp = requests.get("http://localhost:8011/v1/models", timeout=10)
    resp.raise_for_status()
    models = resp.json()["data"]
    assert len(models) > 0, "No models found on vLLM server"
    model_id = models[0]["id"]
    print(f"Detected model: {model_id}")
    return model_id


def query_qwen(model, premises_text, constraint_expr, constraint_type):
    """Ask Qwen whether a constraint logically follows from the premises."""
    if constraint_type == "fact":
        question = f"Constraint (fact): {constraint_expr}"
    else:
        question = f"Constraint (logical rule in FOL-like notation): {constraint_expr}"

    prompt = f"""Given the following premises:
{premises_text}

Does the following logical constraint logically follow from the premises alone?
{question}

Answer only: Yes / No"""

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 16,
        "temperature": 0.0,
    }
    resp = requests.post(QWEN_URL, json=payload, timeout=60)
    resp.raise_for_status()
    text = resp.json()["choices"][0]["message"]["content"].strip()
    return text


def parse_yes_no(text):
    """Parse Qwen response to boolean."""
    t = text.lower().strip().rstrip(".")
    if t.startswith("yes"):
        return True
    if t.startswith("no"):
        return False
    if "yes" in t and "no" not in t:
        return True
    if "no" in t and "yes" not in t:
        return False
    return None


def extract_premises_text(problem_text):
    """Extract just the premises from the problem text (before 'Determine whether')."""
    marker = "Determine whether"
    idx = problem_text.find(marker)
    if idx > 0:
        text = problem_text[:idx].strip()
    else:
        text = problem_text
    if text.startswith("Given the following premises:\n"):
        text = text[len("Given the following premises:\n"):]
    return text.strip()


def sc_majority_vote(answers):
    """Self-consistency majority vote from trace answers."""
    valid = [a for a in answers if a in ("True", "False", "Unknown")]
    if not valid:
        return "Unknown"
    counter = Counter(valid)
    return counter.most_common(1)[0][0]


def main():
    global QWEN_MODEL
    QWEN_MODEL = detect_model()
    assert "qwen" in QWEN_MODEL.lower() or "Qwen" in QWEN_MODEL, \
        f"Expected Qwen model, got: {QWEN_MODEL}. Refusing to use non-Qwen verifier."

    # Load FOLIO data
    with open(FOLIO_DATA) as f:
        folio_data = json.load(f)
    folio_by_id = {item["id"]: item for item in folio_data}

    # Load SC answer matrix
    with open(SC_MATRIX) as f:
        sc_matrix = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    results = []
    total_constraints = 0
    total_kept = 0
    original_correct = 0
    filtered_correct = 0
    sc_correct = 0

    for q_idx in range(N_QUESTIONS):
        pid = f"folio_{q_idx}"
        print(f"\n=== [{q_idx+1}/{N_QUESTIONS}] {pid} ===")

        # Load constraint cache
        cache_path = os.path.join(CONSTRAINT_CACHE_DIR, f"{pid}.json")
        with open(cache_path) as f:
            cache = json.load(f)

        # Load intermediate for original SICA answer
        inter_path = os.path.join(INTERMEDIATES_DIR, f"{pid}.json")
        with open(inter_path) as f:
            inter = json.load(f)

        gold = cache["gt"]
        original_sica_answer = inter["sica_result"]["answer"]

        # Get premises text
        folio_item = folio_by_id[pid]
        premises_text = extract_premises_text(folio_item["problem"])

        # SC answer
        sc_answers = sc_matrix[pid]["answers"]
        sc_answer = sc_majority_vote(sc_answers)

        # Collect unique constraints with answer associations
        # constraint_expr -> set of answers from traces containing it
        expr_to_answers = defaultdict(list)
        expr_to_type = {}
        for trace_data in cache["per_trace"]:
            trace_answer = trace_data["answer"]
            if trace_answer not in ("True", "False", "Unknown"):
                continue
            for c in trace_data["constraints"]:
                expr = c["expression"]
                expr_to_answers[expr].append(trace_answer)
                expr_to_type[expr] = c["type"]

        unique_exprs = list(expr_to_answers.keys())
        print(f"  Gold: {gold}, Original SICA: {original_sica_answer}, SC: {sc_answer}")
        print(f"  Unique constraints: {len(unique_exprs)}")

        # Verify each constraint with Qwen
        verified = {}
        for expr in unique_exprs:
            ctype = expr_to_type[expr]
            raw = query_qwen(QWEN_MODEL, premises_text, expr, ctype)
            is_yes = parse_yes_no(raw)
            verified[expr] = is_yes
            if is_yes is None:
                print(f"  WARNING: unparseable response for '{expr[:60]}...': '{raw}'")

        kept = sum(1 for v in verified.values() if v is True)
        total_constraints += len(unique_exprs)
        total_kept += kept
        print(f"  Kept: {kept}/{len(unique_exprs)} ({kept/max(len(unique_exprs),1)*100:.0f}%)")

        # Re-score with filtered constraints
        answer_scores = defaultdict(float)
        for expr, is_verified in verified.items():
            if is_verified is not True:
                continue
            # Each occurrence in a trace adds weight for that trace's answer
            for ans in expr_to_answers[expr]:
                answer_scores[ans] += 1.0

        if answer_scores:
            filtered_answer = max(answer_scores, key=answer_scores.get)
        else:
            filtered_answer = "Unknown"

        print(f"  Filtered scores: {dict(answer_scores)}")
        print(f"  Filtered answer: {filtered_answer}")

        is_orig_correct = (original_sica_answer == gold)
        is_filt_correct = (filtered_answer == gold)
        is_sc_correct = (sc_answer == gold)
        original_correct += is_orig_correct
        filtered_correct += is_filt_correct
        sc_correct += is_sc_correct

        results.append({
            "pid": pid,
            "gold": gold,
            "original_sica": original_sica_answer,
            "original_sica_correct": is_orig_correct,
            "filtered_sica": filtered_answer,
            "filtered_sica_correct": is_filt_correct,
            "filtered_scores": dict(answer_scores),
            "sc_answer": sc_answer,
            "sc_correct": is_sc_correct,
            "num_constraints": len(unique_exprs),
            "num_kept": kept,
            "keep_rate": kept / max(len(unique_exprs), 1),
            "verification_details": {
                expr: {"verified": verified[expr], "type": expr_to_type[expr]}
                for expr in unique_exprs
            },
        })

    # Compute McNemar's test: filtered SICA vs SC
    # Discordant pairs
    a = 0  # filtered correct, SC wrong
    b = 0  # filtered wrong, SC correct
    for r in results:
        fc = r["filtered_sica_correct"]
        sc = r["sc_correct"]
        if fc and not sc:
            a += 1
        elif not fc and sc:
            b += 1

    from scipy.stats import binomtest
    n_disc = a + b
    if n_disc > 0:
        mcnemar_p = binomtest(min(a, b), n_disc, 0.5).pvalue
    else:
        mcnemar_p = 1.0

    summary = {
        "verifier_model": QWEN_MODEL,
        "generator_model": "Mistral-7B-Instruct-v0.3",
        "n_questions": N_QUESTIONS,
        "original_sica_acc": original_correct / N_QUESTIONS,
        "cross_model_filtered_sica_acc": filtered_correct / N_QUESTIONS,
        "sc_acc": sc_correct / N_QUESTIONS,
        "constraint_keep_rate": total_kept / max(total_constraints, 1),
        "total_constraints": total_constraints,
        "total_kept": total_kept,
        "mcnemar_discordant": {"filtered_right_sc_wrong": a, "filtered_wrong_sc_right": b},
        "mcnemar_p": mcnemar_p,
        "per_question_details": results,
    }

    out_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n{'='*60}")
    print(f"SUMMARY ({N_QUESTIONS} questions)")
    print(f"  Original SICA acc:       {summary['original_sica_acc']:.3f}")
    print(f"  Cross-model filtered acc: {summary['cross_model_filtered_sica_acc']:.3f}")
    print(f"  SC acc:                  {summary['sc_acc']:.3f}")
    print(f"  Constraint keep rate:    {summary['constraint_keep_rate']:.3f}")
    print(f"  McNemar p-value:         {summary['mcnemar_p']:.4f}")
    print(f"  Discordant: filtered>SC={a}, SC>filtered={b}")
    print(f"Results saved to: {out_path}")


if __name__ == "__main__":
    main()
