"""
Frontier model SC-Baseline on FOLIO-204 via OpenAI-compatible API.
Async concurrent generation with semaphore-based rate limiting.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from collections import Counter

import aiohttp

API_KEY = [REDACTED]"OPENROUTER_API_KEY"]
BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "http://47.94.22.126/v1")

REASONING_MODELS = {"o1", "o3", "o3-mini", "o4-mini", "gpt-5", "gpt-5.5", "gpt-5.4-pro", "gpt-5.2-pro"}

def is_reasoning_model(model: str) -> bool:
    base = model.split("-202")[0]  # strip date suffix
    return base in REASONING_MODELS

FOLIO_PROMPT = """Read the following premises carefully and determine whether the conclusion is true, false, or uncertain based solely on the given information.

{problem}

Think step by step through the logical reasoning. At the end, state your final answer as exactly one of: True, False, or Unknown.
Put your final answer in \\boxed{{}} format, e.g. \\boxed{{True}}, \\boxed{{False}}, or \\boxed{{Unknown}}."""


def extract_boxed_answer(text: str) -> str:
    matches = re.findall(r'\\boxed\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', text)
    return matches[-1].strip() if matches else ""


def normalize_answer(ans: str) -> str:
    if not ans:
        return ""
    a = ans.strip().lower()
    mapping = {"true": "True", "false": "False", "unknown": "Unknown",
               "uncertain": "Unknown", "proved": "True", "disproved": "False"}
    return mapping.get(a, ans.strip())


def extract_answer_from_trace(text: str) -> str:
    boxed = extract_boxed_answer(text)
    if boxed:
        norm = normalize_answer(boxed)
        if norm in ("True", "False", "Unknown"):
            return norm

    text_lower = text.lower()
    patterns = [
        r'(?:the |my )?(?:final )?answer is[:\s]*\*?\*?(true|false|unknown|uncertain)',
        r'(?:conclusion is|verdict is|therefore)[:\s]*\*?\*?(true|false|unknown|uncertain)',
    ]
    for pat in patterns:
        m = re.search(pat, text_lower)
        if m:
            return normalize_answer(m.group(1))

    last_lines = text.strip().split('\n')[-5:]
    for line in reversed(last_lines):
        ll = line.lower().strip()
        for label in ["true", "false", "unknown"]:
            if label in ll:
                candidates = [w for w in ["true", "false", "unknown"] if w in ll]
                if len(candidates) == 1:
                    return normalize_answer(candidates[0])
    return ""


async def generate_trace(session: aiohttp.ClientSession, model: str,
                         problem_text: str, trace_idx: int,
                         semaphore: asyncio.Semaphore) -> dict | None:
    async with semaphore:
        prompt = FOLIO_PROMPT.format(problem=problem_text)
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2048,
        }
        if not is_reasoning_model(model):
            payload["temperature"] = 0.7
        headers = {
            "Authorization": [REDACTED]"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        for retry in range(3):
            try:
                async with session.post(f"{BASE_URL}/chat/completions",
                                        json=payload, headers=headers,
                                        timeout=aiohttp.ClientTimeout(total=300)) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        text = data["choices"][0]["message"]["content"]
                        answer = extract_answer_from_trace(text)
                        return {"trace": text, "answer": answer, "trace_idx": trace_idx}
                    elif resp.status == 429:
                        wait = 3 * (retry + 1)
                        print(f"    429 rate limit, waiting {wait}s...", flush=True)
                        await asyncio.sleep(wait)
                    elif resp.status == 502:
                        wait = 5 * (retry + 1)
                        print(f"    502 upstream error, waiting {wait}s...", flush=True)
                        await asyncio.sleep(wait)
                    else:
                        body = await resp.text()
                        print(f"    HTTP {resp.status}: {body[:200]}", flush=True)
                        await asyncio.sleep(3 * (retry + 1))
            except asyncio.TimeoutError:
                print(f"    Timeout trace {trace_idx} retry {retry}", flush=True)
                await asyncio.sleep(5)
            except Exception as e:
                print(f"    Error trace {trace_idx}: {e}", flush=True)
                await asyncio.sleep(3)
        return None


async def process_question(session: aiohttp.ClientSession, model: str,
                           question: dict, k: int,
                           semaphore: asyncio.Semaphore) -> dict | None:
    tasks = [generate_trace(session, model, question["problem"], i, semaphore)
             for i in range(k)]
    results = await asyncio.gather(*tasks)
    traces = [r for r in results if r is not None]

    answers = [t["answer"] for t in traces if t["answer"] in ("True", "False", "Unknown")]

    gold = normalize_answer(question["answer"])

    if not answers:
        return {
            "question_id": question["id"],
            "gold": gold,
            "n_traces": len(traces),
            "n_valid_answers": 0,
            "traces": traces,
            "answers": [],
            "sc_answer": "",
            "sc_correct": False,
            "answer_distribution": {},
        }

    counts = Counter(answers)
    max_count = max(counts.values())
    tied = sorted([a for a, c in counts.items() if c == max_count])
    sc_answer = tied[0]

    return {
        "question_id": question["id"],
        "gold": gold,
        "n_traces": len(traces),
        "n_valid_answers": len(answers),
        "traces": traces,
        "answers": answers,
        "sc_answer": sc_answer,
        "sc_correct": sc_answer == gold,
        "answer_distribution": dict(counts),
    }


async def run_model(model_name: str, questions: list[dict], output_dir: str,
                    k: int = 12, concurrency: int = 5):
    os.makedirs(output_dir, exist_ok=True)
    semaphore = asyncio.Semaphore(concurrency)
    results = []
    start_time = time.time()

    checkpoint_path = os.path.join(output_dir, "checkpoint.json")
    done_ids = set()
    if os.path.exists(checkpoint_path):
        with open(checkpoint_path) as f:
            results = json.load(f)
        done_ids = {r["question_id"] for r in results}
        print(f"[{model_name}] Resuming: {len(done_ids)} done", flush=True)

    remaining = [q for q in questions if q["id"] not in done_ids]
    print(f"[{model_name}] {len(remaining)} questions (K={k}, conc={concurrency})", flush=True)

    async with aiohttp.ClientSession() as session:
        for i, q in enumerate(remaining):
            t0 = time.time()
            result = await process_question(session, model_name, q, k, semaphore)
            dt = time.time() - t0
            if result:
                results.append(result)
                status = "OK" if result["sc_correct"] else "WRONG"
                print(f"  [{i+1}/{len(remaining)}] {q['id']} gold={result['gold']} "
                      f"sc={result['sc_answer']} {status} "
                      f"dist={result['answer_distribution']} {dt:.1f}s", flush=True)
            else:
                print(f"  [{i+1}/{len(remaining)}] {q['id']} FAILED {dt:.1f}s", flush=True)

            if (i + 1) % 10 == 0:
                elapsed = time.time() - start_time
                sc_so_far = sum(1 for r in results if r["sc_correct"])
                acc = sc_so_far / len(results) if results else 0
                rate = (i + 1) / elapsed * 60
                eta = (len(remaining) - i - 1) / rate if rate > 0 else 0
                print(f"  === [{model_name}] {i+1}/{len(remaining)} acc={acc:.3f} "
                      f"({sc_so_far}/{len(results)}) {rate:.1f}q/min ETA={eta:.0f}min ===",
                      flush=True)
                with open(checkpoint_path, "w") as f:
                    json.dump(results, f)

    # Final checkpoint
    with open(checkpoint_path, "w") as f:
        json.dump(results, f)

    sc_correct = sum(1 for r in results if r["sc_correct"])
    n_valid = sum(1 for r in results if r["n_valid_answers"] > 0)
    sc_acc = sc_correct / n_valid if n_valid else 0

    per_label_acc = {}
    for label in ("True", "False", "Unknown"):
        subset = [r for r in results if r["gold"] == label]
        if subset:
            correct = sum(1 for r in subset if r["sc_correct"])
            per_label_acc[label] = {"correct": correct, "total": len(subset),
                                     "accuracy": round(correct / len(subset), 4)}

    label_counts = Counter(r["gold"] for r in results)

    summary = {
        "model": model_name,
        "dataset": "FOLIO-204",
        "n_questions": len(results),
        "n_valid": n_valid,
        "k": k,
        "temperature": 0.7,
        "concurrency": concurrency,
        "sc_accuracy": round(sc_acc, 4),
        "sc_correct": sc_correct,
        "per_label_accuracy": per_label_acc,
        "label_distribution": dict(label_counts),
        "elapsed_seconds": round(time.time() - start_time, 1),
        "per_question": results,
    }

    results_path = os.path.join(output_dir, "results.json")
    with open(results_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}", flush=True)
    print(f"[{model_name}] DONE", flush=True)
    print(f"  SC accuracy: {sc_acc:.4f} ({sc_correct}/{n_valid})", flush=True)
    for label, stats in per_label_acc.items():
        print(f"  {label:8s}: {stats['accuracy']:.4f} ({stats['correct']}/{stats['total']})", flush=True)
    print(f"  Time: {summary['elapsed_seconds']:.0f}s", flush=True)
    print(f"  Saved: {results_path}", flush=True)
    print(f"{'='*60}\n", flush=True)

    return summary


async def main_async(args):
    with open(args.data) as f:
        questions = json.load(f)
    print(f"Loaded {len(questions)} FOLIO questions", flush=True)
    print(f"API: {BASE_URL}", flush=True)

    models = [m.strip() for m in args.models.split(",")]
    print(f"Models: {models}", flush=True)

    all_summaries = []
    for model in models:
        safe_name = model.replace("/", "_").replace(":", "_")
        output_dir = os.path.join(args.output_dir, safe_name)
        summary = await run_model(model, questions, output_dir,
                                  k=args.k, concurrency=args.concurrency)
        all_summaries.append(summary)

    print(f"\n{'='*60}", flush=True)
    print("COMPARISON", flush=True)
    print(f"{'='*60}", flush=True)
    print(f"{'Model':30s} {'SC Acc':>8s} {'Correct':>8s} {'N':>5s}", flush=True)
    print("-" * 55, flush=True)
    for s in all_summaries:
        print(f"{s['model']:30s} {s['sc_accuracy']:8.4f} {s['sc_correct']:8d} {s['n_valid']:5d}", flush=True)

    comp_path = os.path.join(args.output_dir, "comparison.json")
    with open(comp_path, "w") as f:
        json.dump([{k: v for k, v in s.items() if k != "per_question"} for s in all_summaries],
                  f, indent=2, ensure_ascii=False)
    print(f"\nComparison saved: {comp_path}", flush=True)


def main():
    parser = argparse.ArgumentParser(description="Frontier SC-Baseline on FOLIO-204")
    parser.add_argument("--models", required=True)
    parser.add_argument("--data", default="/root/symb_invariant_consensus/data/folio_full.json")
    parser.add_argument("--output-dir", default="/root/symb_invariant_consensus/results/exp_d135_frontier_scb/")
    parser.add_argument("--k", type=int, default=12)
    parser.add_argument("--concurrency", type=int, default=5)
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
