"""
Dir-F PRM Step-Level Verifier — FOLIO 30-question Pilot (v2)
Uses Mistral-7B vLLM API with logprobs for step-level reasoning quality scoring.
"""
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import requests

# ── Config ──────────────────────────────────────────────────────────────
VLLM_URL = "http://localhost:8012/v1/completions"
MODEL_ID = "/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3"
INTERMEDIATES_DIR = Path("/root/symb_invariant_consensus/results/exp033_mistral_7b_folio204/intermediates")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/dir_f_prm_verifier_pilot")
NUM_QUESTIONS = 30


# ── Step splitting ──────────────────────────────────────────────────────
def split_into_steps(trace_text: str) -> list[str]:
    trace_text = trace_text.strip()
    numbered = re.split(r'\n\s*(?:\d+[\.\)]\s|Step\s+\d+)', trace_text)
    if len(numbered) > 2:
        return [s.strip() for s in numbered if s.strip()]

    paragraphs = re.split(r'\n\s*\n', trace_text)
    if len(paragraphs) > 1:
        return [p.strip() for p in paragraphs if p.strip()]

    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', trace_text)
    if len(sentences) > 2:
        steps = []
        for i in range(0, len(sentences), 3):
            chunk = ' '.join(sentences[i:i+3])
            if chunk.strip():
                steps.append(chunk.strip())
        return steps

    return [trace_text]


# ── LLM-based step scoring ─────────────────────────────────────────────
def score_step_llm(premise_text: str, step: str, max_retries: int = 2) -> float:
    prompt = f"""[INST] You are a logic validator. Given premises from a logical reasoning problem, evaluate whether a reasoning step is logically valid.

Premises:
{premise_text[:1500]}

Reasoning step to evaluate:
{step[:500]}

Rate this step's logical validity on a scale of 1-5:
1 = Completely wrong or irrelevant
2 = Contains logical errors
3 = Partially correct but with gaps
4 = Mostly correct with minor issues
5 = Perfectly valid logical reasoning

Output ONLY a single digit (1-5): [/INST]"""

    for attempt in range(max_retries):
        try:
            resp = requests.post(VLLM_URL, json={
                "model": MODEL_ID,
                "prompt": prompt,
                "max_tokens": 3,
                "temperature": 0.0,
                "logprobs": 5,
            }, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            text = data["choices"][0]["text"].strip()
            for ch in text:
                if ch in "12345":
                    return float(ch) / 5.0
            return 0.5
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                print(f"  [WARN] scoring failed: {e}")
                return 0.5
    return 0.5


def score_trace(premise_text: str, trace_text: str) -> dict:
    steps = split_into_steps(trace_text)
    if not steps:
        return {"step_scores": [], "mean_score": 0.5, "min_score": 0.0, "num_steps": 0}

    step_scores = []
    for step in steps:
        if len(step.split()) < 5:
            continue
        score = score_step_llm(premise_text, step)
        step_scores.append(score)

    if not step_scores:
        return {"step_scores": [], "mean_score": 0.5, "min_score": 0.0, "num_steps": 0}

    return {
        "step_scores": step_scores,
        "mean_score": float(np.mean(step_scores)),
        "min_score": float(np.min(step_scores)),
        "num_steps": len(step_scores),
    }


# ── SC methods ──────────────────────────────────────────────────────────
def standard_sc(traces: list[dict]) -> str:
    answers = [t["answer"] for t in traces if t["answer"]]
    if not answers:
        return "Unknown"
    return Counter(answers).most_common(1)[0][0]


def filtered_sc(traces: list[dict], trace_scores: list[dict]) -> str:
    scored = [(t, s) for t, s in zip(traces, trace_scores) if t["answer"] and s["num_steps"] > 0]
    if not scored:
        return "Unknown"

    scores_vals = [s["mean_score"] for _, s in scored]
    median_score = float(np.median(scores_vals))

    filtered = [(t, s) for t, s in scored if s["mean_score"] >= median_score]
    if not filtered:
        return "Unknown"

    return Counter([t["answer"] for t, _ in filtered]).most_common(1)[0][0]


def weighted_sc(traces: list[dict], trace_scores: list[dict]) -> str:
    scored = [(t, s) for t, s in zip(traces, trace_scores) if t["answer"] and s["num_steps"] > 0]
    if not scored:
        return "Unknown"

    weight_by_answer = Counter()
    for t, s in scored:
        weight_by_answer[t["answer"]] += s["mean_score"]

    if not weight_by_answer:
        return "Unknown"
    return weight_by_answer.most_common(1)[0][0]


def min_filtered_sc(traces: list[dict], trace_scores: list[dict]) -> str:
    scored = [(t, s) for t, s in zip(traces, trace_scores) if t["answer"] and s["num_steps"] > 0]
    if not scored:
        return "Unknown"

    scores_vals = [s["min_score"] for _, s in scored]
    median_score = float(np.median(scores_vals))

    filtered = [(t, s) for t, s in scored if s["min_score"] >= median_score]
    if not filtered:
        return "Unknown"

    return Counter([t["answer"] for t, _ in filtered]).most_common(1)[0][0]


# ── Main ────────────────────────────────────────────────────────────────
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    try:
        r = requests.get("http://localhost:8012/v1/models", timeout=5)
        r.raise_for_status()
        print(f"vLLM API OK: {r.json()['data'][0]['id']}")
    except Exception as e:
        print(f"ERROR: vLLM API not available: {e}")
        sys.exit(1)

    results_per_question = []
    sc_correct = 0
    filtered_correct = 0
    weighted_correct = 0
    min_filtered_correct = 0
    total = 0

    t_start = time.time()

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

        q_start = time.time()
        trace_scores = []
        for tidx, trace_obj in enumerate(traces):
            ts = score_trace(premise_text, trace_obj["trace"])
            trace_scores.append(ts)

        sc_ans = standard_sc(traces)
        filt_ans = filtered_sc(traces, trace_scores)
        wt_ans = weighted_sc(traces, trace_scores)
        mf_ans = min_filtered_sc(traces, trace_scores)

        sc_ok = (sc_ans == gold)
        filt_ok = (filt_ans == gold)
        wt_ok = (wt_ans == gold)
        mf_ok = (mf_ans == gold)

        sc_correct += int(sc_ok)
        filtered_correct += int(filt_ok)
        weighted_correct += int(wt_ok)
        min_filtered_correct += int(mf_ok)
        total += 1

        q_time = time.time() - q_start

        q_result = {
            "id": f"folio_{qidx}",
            "gold": gold,
            "sc_answer": sc_ans,
            "filtered_sc_answer": filt_ans,
            "weighted_sc_answer": wt_ans,
            "min_filtered_sc_answer": mf_ans,
            "sc_correct": sc_ok,
            "filtered_correct": filt_ok,
            "weighted_correct": wt_ok,
            "min_filtered_correct": mf_ok,
            "num_traces": len(traces),
            "trace_scores_summary": [
                {
                    "trace_idx": traces[i].get("trace_idx", i),
                    "answer": traces[i]["answer"],
                    "mean_score": trace_scores[i]["mean_score"],
                    "min_score": trace_scores[i]["min_score"],
                    "num_steps": trace_scores[i]["num_steps"],
                }
                for i in range(len(traces))
            ],
        }
        results_per_question.append(q_result)

        print(f"[{qidx+1}/{NUM_QUESTIONS}] folio_{qidx}: gold={gold} sc={sc_ans} filt={filt_ans} wt={wt_ans} mf={mf_ans} | "
              f"SC={'OK' if sc_ok else 'X'} Filt={'OK' if filt_ok else 'X'} Wt={'OK' if wt_ok else 'X'} MF={'OK' if mf_ok else 'X'} | {q_time:.1f}s")

    total_time = time.time() - t_start

    final = {
        "model_used": "Mistral-7B-Instruct-v0.3 (self-eval via vLLM)",
        "scoring_method": "LLM step-level validity rating (1-5 scale, normalized to 0-1)",
        "num_questions": total,
        "sc_accuracy_30": round(sc_correct / total, 4) if total > 0 else 0,
        "filtered_sc_accuracy_30": round(filtered_correct / total, 4) if total > 0 else 0,
        "weighted_sc_accuracy_30": round(weighted_correct / total, 4) if total > 0 else 0,
        "min_filtered_sc_accuracy_30": round(min_filtered_correct / total, 4) if total > 0 else 0,
        "sc_correct": sc_correct,
        "filtered_correct": filtered_correct,
        "weighted_correct": weighted_correct,
        "min_filtered_correct": min_filtered_correct,
        "total_time_s": round(total_time, 1),
        "per_question_scores": results_per_question,
    }

    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(final, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"Results saved to {out_path}")
    print(f"Standard SC accuracy:      {final['sc_accuracy_30']:.4f} ({sc_correct}/{total})")
    print(f"Filtered SC accuracy:      {final['filtered_sc_accuracy_30']:.4f} ({filtered_correct}/{total})")
    print(f"Weighted SC accuracy:      {final['weighted_sc_accuracy_30']:.4f} ({weighted_correct}/{total})")
    print(f"Min-Filtered SC accuracy:  {final['min_filtered_sc_accuracy_30']:.4f} ({min_filtered_correct}/{total})")
    print(f"Total time: {total_time:.1f}s")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
