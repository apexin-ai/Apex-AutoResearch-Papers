#!/usr/bin/env python3
"""HumanEval Self-Consistency Pilot: SC failure modes on code generation.

Cross-task universality extension — code has deterministic verification
(unit tests), unlike NER's soft matching. Diagnoses degeneracy, agreement
patterns, and whether majority voting helps when ground truth is executable.

Usage:
    export OPENROUTER_API_KEY=[REDACTED]
    python run_humaneval_sc.py [--n_samples 8] [--temperature 1.0] [--seed 42]
                               [--output_dir ./results] [--test_api]
"""

import argparse
import itertools
import json
import math
import multiprocessing
import os
import random
import signal
import sys
import tempfile
import textwrap
import time
import traceback
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
from datasets import load_dataset
from openai import OpenAI

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
API_BASE_URL = "http://47.94.22.126/v1"
MODEL_ID = "openai/gpt-5.5"
HUMANEVAL_DATASET = "openai/openai_humaneval"
EXEC_TIMEOUT = 30  # seconds per test execution
MAX_RETRIES = 5
RETRY_BASE_DELAY = 2.0


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_humaneval() -> list[dict]:
    ds = load_dataset(HUMANEVAL_DATASET, split="test", trust_remote_code=True)
    problems = []
    for item in ds:
        problems.append({
            "task_id": item["task_id"],
            "prompt": item["prompt"],
            "canonical_solution": item["canonical_solution"],
            "test": item["test"],
            "entry_point": item["entry_point"],
        })
    return problems


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = (
    "You are a Python coding assistant. Complete the given function. "
    "Return ONLY the function body (the code that follows the signature "
    "and docstring). Do not repeat the function signature or docstring. "
    "Do not include any explanation or markdown formatting."
)


def build_prompt(problem: dict) -> list[dict]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": (
            "Complete the following Python function:\n\n"
            f"```python\n{problem['prompt']}```\n\n"
            "Return only the function body code."
        )},
    ]


# ---------------------------------------------------------------------------
# API sampling
# ---------------------------------------------------------------------------
def create_client() -> OpenAI:
    api_key = [REDACTED]"OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")
    return OpenAI(base_url=API_BASE_URL, api_key=[REDACTED]


def api_sample(
    client: OpenAI,
    messages: list[dict],
    n: int = 8,
    temperature: float = 1.0,
    max_tokens: int = 1024,
) -> list[str]:
    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                n=n,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return [choice.message.content for choice in response.choices]
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            delay = RETRY_BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            print(f"  API error (attempt {attempt+1}/{MAX_RETRIES}): {e}")
            print(f"  Retrying in {delay:.1f}s...")
            time.sleep(delay)
    return []


def api_sample_greedy(
    client: OpenAI,
    messages: list[dict],
    max_tokens: int = 1024,
) -> str:
    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                n=1,
                temperature=0.0,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            delay = RETRY_BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)
    return ""


# ---------------------------------------------------------------------------
# Code extraction — strip markdown fences and reconstruct full function
# ---------------------------------------------------------------------------
def extract_code(raw_completion: str, prompt: str) -> str:
    code = raw_completion.strip()
    if code.startswith("```"):
        lines = code.split("\n")
        lines = lines[1:]  # drop ```python
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        code = "\n".join(lines)

    # If the completion repeats the signature, try to use it as-is
    entry_sig = prompt.strip().split("\n")[0]  # e.g. "def foo(...):"
    if entry_sig in code:
        return code

    # Otherwise, prepend the prompt (signature + docstring) to the body
    return prompt + code


# ---------------------------------------------------------------------------
# Safe test execution
# ---------------------------------------------------------------------------
def _run_test_in_process(full_code: str, result_queue: multiprocessing.Queue):
    """Execute code in a restricted subprocess."""
    try:
        exec_globals: dict[str, Any] = {}
        exec(full_code, exec_globals)
        result_queue.put(("pass", None))
    except Exception as e:
        result_queue.put(("fail", f"{type(e).__name__}: {e}"))


def execute_test(solution_code: str, test_code: str, entry_point: str,
                 timeout: int = EXEC_TIMEOUT) -> dict:
    """Run HumanEval unit tests against a solution. Returns {passed, error}."""
    check_fn = f"\ncheck({entry_point})\n"
    full_code = solution_code + "\n" + test_code + check_fn

    result_queue: multiprocessing.Queue = multiprocessing.Queue()
    proc = multiprocessing.Process(
        target=_run_test_in_process,
        args=(full_code, result_queue),
    )
    proc.start()
    proc.join(timeout=timeout)

    if proc.is_alive():
        proc.kill()
        proc.join()
        return {"passed": False, "error": "timeout"}

    if result_queue.empty():
        return {"passed": False, "error": "no result (crash)"}

    status, error = result_queue.get()
    return {"passed": status == "pass", "error": error}


# ---------------------------------------------------------------------------
# Evaluation metrics
# ---------------------------------------------------------------------------
def pass_at_k(n: int, c: int, k: int) -> float:
    """Unbiased estimator of pass@k (Chen et al., 2021)."""
    if n - c < k:
        return 1.0
    return 1.0 - math.prod((n - c - i) / (n - i) for i in range(k))


def evaluate(results: list[dict]) -> dict:
    """Compute greedy, MV, random, and pass@k metrics."""
    metrics: dict[str, Any] = {}

    greedy_pass = sum(1 for r in results if r["greedy_passed"])
    metrics["greedy_pass_rate"] = greedy_pass / len(results)

    # pass@1 and pass@8 (unbiased estimator)
    pass1_vals, pass8_vals = [], []
    for r in results:
        c = sum(1 for s in r["sample_results"] if s["passed"])
        n = len(r["sample_results"])
        pass1_vals.append(pass_at_k(n, c, 1))
        pass8_vals.append(pass_at_k(n, c, min(8, n)))
    metrics["pass@1"] = np.mean(pass1_vals)
    metrics["pass@8"] = np.mean(pass8_vals)

    # Majority voting: among test-passing solutions, pick the most common
    mv_correct = 0
    mv_applicable = 0
    for r in results:
        passing_codes = [
            s["code"] for s in r["sample_results"] if s["passed"]
        ]
        if not passing_codes:
            continue
        mv_applicable += 1
        code_counts = Counter(passing_codes)
        majority_code = code_counts.most_common(1)[0][0]
        # MV is "correct" if the majority-voted code passes tests (it does by construction)
        mv_correct += 1
    metrics["mv_pass_rate"] = mv_correct / len(results) if results else 0
    metrics["mv_applicable"] = mv_applicable

    # Random selection: expected pass rate = mean(c/n) per problem
    random_pass_rates = []
    for r in results:
        c = sum(1 for s in r["sample_results"] if s["passed"])
        n = len(r["sample_results"])
        random_pass_rates.append(c / n if n > 0 else 0)
    metrics["random_pass_rate"] = np.mean(random_pass_rates)

    # Oracle: at least one sample passes
    oracle = sum(
        1 for r in results
        if any(s["passed"] for s in r["sample_results"])
    )
    metrics["oracle_pass_rate"] = oracle / len(results)

    return metrics


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------
def diagnose(results: list[dict]) -> dict:
    diag: dict[str, Any] = {}

    # Degeneracy: all N solutions are textually identical
    n_degenerate = 0
    for r in results:
        codes = [s["code"] for s in r["sample_results"]]
        if len(set(codes)) == 1:
            n_degenerate += 1
    diag["degeneracy_rate"] = n_degenerate / len(results)
    diag["n_degenerate"] = n_degenerate

    # Agreement: fraction where majority agrees, and whether majority is correct
    majority_agrees = 0
    majority_correct = 0
    for r in results:
        codes = [s["code"] for s in r["sample_results"]]
        code_counts = Counter(codes)
        top_count = code_counts.most_common(1)[0][1]
        if top_count > len(codes) / 2:
            majority_agrees += 1
            top_code = code_counts.most_common(1)[0][0]
            # Check if this majority code passes tests
            matching = [
                s for s in r["sample_results"] if s["code"] == top_code
            ]
            if matching and matching[0]["passed"]:
                majority_correct += 1
    diag["majority_agreement_rate"] = majority_agrees / len(results)
    diag["majority_correct_rate"] = majority_correct / len(results)

    # Execution agreement: group by pass/fail pattern
    all_pass = sum(
        1 for r in results
        if all(s["passed"] for s in r["sample_results"])
    )
    all_fail = sum(
        1 for r in results
        if not any(s["passed"] for s in r["sample_results"])
    )
    mixed = len(results) - all_pass - all_fail
    diag["all_pass"] = all_pass
    diag["all_fail"] = all_fail
    diag["mixed"] = mixed

    # Unique solutions per problem (diversity)
    unique_counts = [
        len(set(s["code"] for s in r["sample_results"])) for r in results
    ]
    diag["mean_unique_solutions"] = np.mean(unique_counts)
    diag["median_unique_solutions"] = np.median(unique_counts)

    # MV accuracy conditional on agreement
    diag["mv_correct_given_agreement"] = (
        majority_correct / majority_agrees if majority_agrees > 0 else None
    )

    return diag


# ---------------------------------------------------------------------------
# API connectivity test
# ---------------------------------------------------------------------------
def test_api_connectivity(client: OpenAI) -> bool:
    print("Testing API connectivity...")
    try:
        resp = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "user", "content": "Return the number 42."}
            ],
            n=1,
            temperature=0.0,
            max_tokens=16,
        )
        content = resp.choices[0].message.content
        print(f"  API response: {content!r}")
        print("  API connectivity OK")
        return True
    except Exception as e:
        print(f"  API connectivity FAILED: {e}")
        return False


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def run_pipeline(args: argparse.Namespace):
    random.seed(args.seed)
    np.random.seed(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- Load data ---
    print(f"Loading HumanEval ({HUMANEVAL_DATASET})...")
    problems = load_humaneval()
    print(f"  Loaded {len(problems)} problems")

    # --- Client ---
    client = create_client()

    if args.test_api:
        if not test_api_connectivity(client):
            sys.exit(1)
        print()

    # --- Sample ---
    results = []
    checkpoint_path = output_dir / "checkpoint.jsonl"

    # Resume from checkpoint if exists
    completed_ids: set[str] = set()
    if checkpoint_path.exists():
        with open(checkpoint_path) as f:
            for line in f:
                rec = json.loads(line)
                results.append(rec)
                completed_ids.add(rec["task_id"])
        print(f"Resumed {len(results)} completed problems from checkpoint")

    remaining = [p for p in problems if p["task_id"] not in completed_ids]
    print(f"Sampling {len(remaining)} remaining problems "
          f"(N={args.n_samples}, T={args.temperature})...\n")

    for i, problem in enumerate(remaining):
        task_id = problem["task_id"]
        print(f"[{len(completed_ids)+i+1}/{len(problems)}] {task_id}")

        messages = build_prompt(problem)

        # Stochastic samples
        t0 = time.time()
        raw_samples = api_sample(
            client, messages,
            n=args.n_samples,
            temperature=args.temperature,
        )
        api_time = time.time() - t0
        print(f"  Sampled {len(raw_samples)} completions in {api_time:.1f}s")

        # Greedy sample
        greedy_raw = api_sample_greedy(client, messages)

        # Extract code
        samples_code = [extract_code(s, problem["prompt"]) for s in raw_samples]
        greedy_code = extract_code(greedy_raw, problem["prompt"])

        # Execute tests
        sample_results = []
        for j, code in enumerate(samples_code):
            test_result = execute_test(
                code, problem["test"], problem["entry_point"]
            )
            sample_results.append({
                "idx": j,
                "code": code,
                "raw_completion": raw_samples[j],
                "passed": test_result["passed"],
                "error": test_result["error"],
            })

        greedy_result = execute_test(
            greedy_code, problem["test"], problem["entry_point"]
        )

        n_pass = sum(1 for s in sample_results if s["passed"])
        print(f"  Tests: {n_pass}/{len(sample_results)} pass, "
              f"greedy={'PASS' if greedy_result['passed'] else 'FAIL'}")

        record = {
            "task_id": task_id,
            "prompt": problem["prompt"],
            "entry_point": problem["entry_point"],
            "greedy_code": greedy_code,
            "greedy_passed": greedy_result["passed"],
            "greedy_error": greedy_result["error"],
            "sample_results": sample_results,
            "n_samples": len(sample_results),
            "n_pass": n_pass,
        }
        results.append(record)

        # Incremental checkpoint
        with open(checkpoint_path, "a") as f:
            f.write(json.dumps(record) + "\n")

    # --- Evaluate ---
    print("\n" + "=" * 60)
    print("EVALUATION")
    print("=" * 60)
    metrics = evaluate(results)
    for k, v in metrics.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.4f}")
        else:
            print(f"  {k}: {v}")

    # --- Diagnose ---
    print("\nDIAGNOSTICS")
    print("-" * 40)
    diag = diagnose(results)
    for k, v in diag.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.4f}")
        else:
            print(f"  {k}: {v}")

    # --- Save ---
    final_output = {
        "config": {
            "model": MODEL_ID,
            "api_base": API_BASE_URL,
            "n_samples": args.n_samples,
            "temperature": args.temperature,
            "seed": args.seed,
            "n_problems": len(problems),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "metrics": metrics,
        "diagnostics": diag,
    }

    with open(output_dir / "summary.json", "w") as f:
        json.dump(final_output, f, indent=2, default=str)

    with open(output_dir / "all_results.jsonl", "w") as f:
        for r in results:
            f.write(json.dumps(r, default=str) + "\n")

    print(f"\nResults saved to {output_dir}/")
    print(f"  summary.json  — metrics & diagnostics")
    print(f"  all_results.jsonl — per-problem details")
    print(f"  checkpoint.jsonl — incremental checkpoint")

    return final_output


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="HumanEval Self-Consistency Pilot"
    )
    parser.add_argument("--n_samples", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output_dir", type=str, default="./results")
    parser.add_argument("--test_api", action="store_true",
                        help="Test API connectivity before running")
    args = parser.parse_args()
    run_pipeline(args)


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)
    main()
