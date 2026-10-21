"""
Dir-F PRM Step-Level Verifier — FOLIO 30-question Pilot
Uses DeBERTa-large-mnli as NLI-based proxy for process reward scoring.
"""
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ── Config ──────────────────────────────────────────────────────────────
DEVICE = "cuda:2"
MODEL_NAME = "microsoft/deberta-large-mnli"
INTERMEDIATES_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/dir_f_prm_verifier_pilot")
NUM_QUESTIONS = 30
MAX_PREMISE_TOKENS = 400
MAX_STEP_TOKENS = 100

# ── Step splitting ──────────────────────────────────────────────────────
def split_into_steps(trace_text: str) -> list[str]:
    """Split a reasoning trace into individual steps."""
    trace_text = trace_text.strip()
    # Try numbered steps first (1. 2. 3. or Step 1: etc.)
    numbered = re.split(r'\n\s*(?:\d+[\.\)]\s|Step\s+\d+)', trace_text)
    if len(numbered) > 2:
        steps = [s.strip() for s in numbered if s.strip()]
        return steps

    # Fall back to paragraph splitting
    paragraphs = re.split(r'\n\s*\n', trace_text)
    if len(paragraphs) > 1:
        steps = [p.strip() for p in paragraphs if p.strip()]
        return steps

    # Fall back to sentence-level splitting for single-block traces
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', trace_text)
    if len(sentences) > 2:
        # Group into chunks of 2-3 sentences
        steps = []
        for i in range(0, len(sentences), 2):
            chunk = ' '.join(sentences[i:i+2])
            if chunk.strip():
                steps.append(chunk.strip())
        return steps

    return [trace_text]


# ── NLI scoring ─────────────────────────────────────────────────────────
def load_nli_model(model_name: str, device: str):
    print(f"Loading {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model = model.to(device).eval()
    print(f"Model loaded on {device}")
    return tokenizer, model


def score_step_nli(tokenizer, model, premise: str, hypothesis: str, device: str) -> dict:
    """Score a single reasoning step via NLI. Returns entailment/neutral/contradiction probs."""
    inputs = tokenizer(
        premise, hypothesis,
        truncation=True,
        max_length=512,
        return_tensors="pt",
        padding=True
    ).to(device)

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]

    # DeBERTa-large-mnli labels: 0=contradiction, 1=neutral, 2=entailment
    return {
        "contradiction": float(probs[0]),
        "neutral": float(probs[1]),
        "entailment": float(probs[2]),
    }


def score_trace(tokenizer, model, premise_text: str, trace_text: str, device: str) -> dict:
    """Score all steps in a trace, return aggregate scores."""
    steps = split_into_steps(trace_text)
    if not steps:
        return {"step_scores": [], "mean_entailment": 0.0, "min_entailment": 0.0, "mean_contradiction": 1.0, "num_steps": 0}

    step_scores = []
    for step in steps:
        if len(step.split()) < 3:
            continue
        scores = score_step_nli(tokenizer, model, premise_text, step, device)
        step_scores.append(scores)

    if not step_scores:
        return {"step_scores": [], "mean_entailment": 0.0, "min_entailment": 0.0, "mean_contradiction": 1.0, "num_steps": 0}

    entailments = [s["entailment"] for s in step_scores]
    contradictions = [s["contradiction"] for s in step_scores]

    return {
        "step_scores": step_scores,
        "mean_entailment": float(np.mean(entailments)),
        "min_entailment": float(np.min(entailments)),
        "mean_contradiction": float(np.mean(contradictions)),
        "num_steps": len(step_scores),
        "composite": float(np.mean(entailments)) - float(np.mean(contradictions)),
    }


# ── SC methods ──────────────────────────────────────────────────────────
def standard_sc(traces: list[dict]) -> str:
    """Standard majority vote."""
    answers = [t["answer"] for t in traces if t["answer"]]
    if not answers:
        return "Unknown"
    counts = Counter(answers)
    return counts.most_common(1)[0][0]


def filtered_sc(traces: list[dict], trace_scores: list[dict], score_key: str = "composite") -> str:
    """Remove traces below median score, then majority vote."""
    scored = [(t, s) for t, s in zip(traces, trace_scores) if t["answer"] and s["num_steps"] > 0]
    if not scored:
        return "Unknown"

    scores_vals = [s[score_key] for _, s in scored]
    median_score = float(np.median(scores_vals))

    filtered = [(t, s) for t, s in scored if s[score_key] >= median_score]
    if not filtered:
        return "Unknown"

    answers = [t["answer"] for t, _ in filtered]
    counts = Counter(answers)
    return counts.most_common(1)[0][0]


def weighted_sc(traces: list[dict], trace_scores: list[dict], score_key: str = "composite") -> str:
    """Weighted majority vote using trace scores as weights."""
    scored = [(t, s) for t, s in zip(traces, trace_scores) if t["answer"] and s["num_steps"] > 0]
    if not scored:
        return "Unknown"

    # Shift scores to be non-negative
    scores_vals = [s[score_key] for _, s in scored]
    min_score = min(scores_vals)
    shift = abs(min_score) + 0.01 if min_score < 0 else 0.0

    weight_by_answer = Counter()
    for t, s in scored:
        weight = s[score_key] + shift
        weight_by_answer[t["answer"]] += weight

    if not weight_by_answer:
        return "Unknown"
    return weight_by_answer.most_common(1)[0][0]


# ── Main ────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    tokenizer, model = load_nli_model(MODEL_NAME, DEVICE)

    results_per_question = []
    sc_correct = 0
    filtered_correct = 0
    weighted_correct = 0
    total = 0

    for qidx in range(NUM_QUESTIONS):
        fpath = INTERMEDIATES_DIR / f"folio_{qidx}.json"
        if not fpath.exists():
            print(f"[WARN] {fpath} not found, skipping")
            continue

        with open(fpath) as f:
            data = json.load(f)

        gold = data["problem"]["answer"]
        premise_text = data["problem"]["problem"]
        traces = data["sica_result"]["traces"]

        # Score each trace
        trace_scores = []
        for tidx, trace_obj in enumerate(traces):
            trace_text = trace_obj["trace"]
            ts = score_trace(tokenizer, model, premise_text, trace_text, DEVICE)
            trace_scores.append(ts)

        # Compute SC variants
        sc_ans = standard_sc(traces)
        filt_ans = filtered_sc(traces, trace_scores)
        wt_ans = weighted_sc(traces, trace_scores)

        sc_ok = (sc_ans == gold)
        filt_ok = (filt_ans == gold)
        wt_ok = (wt_ans == gold)

        sc_correct += int(sc_ok)
        filtered_correct += int(filt_ok)
        weighted_correct += int(wt_ok)
        total += 1

        q_result = {
            "id": f"folio_{qidx}",
            "gold": gold,
            "sc_answer": sc_ans,
            "filtered_sc_answer": filt_ans,
            "weighted_sc_answer": wt_ans,
            "sc_correct": sc_ok,
            "filtered_correct": filt_ok,
            "weighted_correct": wt_ok,
            "num_traces": len(traces),
            "trace_scores_summary": [
                {
                    "trace_idx": traces[i].get("trace_idx", i),
                    "answer": traces[i]["answer"],
                    "mean_entailment": trace_scores[i]["mean_entailment"],
                    "composite": trace_scores[i].get("composite", 0),
                    "num_steps": trace_scores[i]["num_steps"],
                }
                for i in range(len(traces))
            ],
        }
        results_per_question.append(q_result)

        status = f"SC={'✓' if sc_ok else '✗'} Filt={'✓' if filt_ok else '✗'} Wt={'✓' if wt_ok else '✗'}"
        print(f"[{qidx+1}/{NUM_QUESTIONS}] folio_{qidx}: gold={gold} sc={sc_ans} filt={filt_ans} wt={wt_ans} | {status}")

    # Final results
    final = {
        "model_used": MODEL_NAME,
        "num_questions": total,
        "sc_accuracy_30": round(sc_correct / total, 4) if total > 0 else 0,
        "filtered_sc_accuracy_30": round(filtered_correct / total, 4) if total > 0 else 0,
        "weighted_sc_accuracy_30": round(weighted_correct / total, 4) if total > 0 else 0,
        "sc_correct": sc_correct,
        "filtered_correct": filtered_correct,
        "weighted_correct": weighted_correct,
        "score_key": "composite (mean_entailment - mean_contradiction)",
        "per_question_scores": results_per_question,
    }

    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(final, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Results saved to {out_path}")
    print(f"Standard SC accuracy:  {final['sc_accuracy_30']:.4f} ({sc_correct}/{total})")
    print(f"Filtered SC accuracy:  {final['filtered_sc_accuracy_30']:.4f} ({filtered_correct}/{total})")
    print(f"Weighted SC accuracy:  {final['weighted_sc_accuracy_30']:.4f} ({weighted_correct}/{total})")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
