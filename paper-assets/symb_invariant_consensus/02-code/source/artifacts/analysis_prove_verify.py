#!/usr/bin/env python3
"""Direction A: PROVE-style code-as-verifier on FOLIO-204.
LLM generates Python verification functions; execution replaces FOL MAX-SAT.
"""

import json
import os
import re
import signal
import time
import traceback
from collections import Counter
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
VLLM_BASE = os.environ.get("VLLM_BASE", "http://localhost:8021")
MODEL_NAME = os.environ.get("MODEL_NAME", "Qwen2.5-7B-Instruct")
DATA_PATH = Path("/root/symb_invariant_consensus/data/folio_full.json")
OUTPUT_DIR = Path("/root/symb_invariant_consensus/results/direction_a_prove")
K_TRACES = 12  # match baseline
TEMPERATURE = 0.7
MAX_TOKENS = 2048
EXEC_TIMEOUT = 5
CANDIDATES = ["True", "False", "Unknown"]

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# FOLIO parsing
# ---------------------------------------------------------------------------
SPLIT_PATTERN = re.compile(
    r"Determine whether the following conclusion is true, false, or uncertain:\n",
    re.IGNORECASE,
)


def parse_problem(problem_text: str) -> tuple[str, str]:
    """Extract premises and conclusion from FOLIO problem text."""
    parts = SPLIT_PATTERN.split(problem_text, maxsplit=1)
    if len(parts) == 2:
        premises = parts[0].strip()
        if premises.lower().startswith("given the following premises:"):
            premises = premises[len("given the following premises:"):].strip()
        conclusion = parts[1].strip()
        return premises, conclusion
    return problem_text.strip(), ""


# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------
def call_llm(prompt: str, temperature: float = 0.0, max_tokens: int = MAX_TOKENS, n: int = 1) -> list[str]:
    """Call vLLM OpenAI-compatible endpoint. Returns list of n completions."""
    resp = requests.post(
        f"{VLLM_BASE}/v1/chat/completions",
        json={
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "n": n,
        },
        timeout=300,
    )
    resp.raise_for_status()
    choices = resp.json()["choices"]
    return [c["message"]["content"] for c in choices]


# ---------------------------------------------------------------------------
# Verification function generation
# ---------------------------------------------------------------------------
VERIFY_PROMPT_TEMPLATE = """You are given a logical reasoning problem. Your task is to write a Python function that verifies whether a given answer is correct.

Premises:
{premises}

Conclusion:
{conclusion}

Write a Python function `verify(answer: str) -> bool` that:
- Takes a candidate answer: "True" (conclusion follows), "False" (conclusion is contradicted), or "Unknown" (cannot be determined)
- Returns True if the answer is logically consistent with the premises, False otherwise
- Encodes the logical relationships from the premises as Python logic
- Evaluates whether the conclusion follows, is contradicted, or is undetermined

Think step by step about the logical relationships, then write the function.

IMPORTANT: Return ONLY the Python function, no explanations. The function must be self-contained (no imports needed). Start with `def verify(answer: str) -> bool:`.

```python
def verify(answer: str) -> bool:
"""


def extract_code(response: str) -> str | None:
    """Extract Python function from LLM response."""
    # Try ```python ... ``` block first
    match = re.search(r"```python\s*\n(.*?)```", response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        if "def verify" in code:
            return code

    # Try ``` ... ``` block
    match = re.search(r"```\s*\n(.*?)```", response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        if "def verify" in code:
            return code

    # Try to find def verify directly
    match = re.search(r"(def verify\(.*?\).*?)(?:\n\n|\Z)", response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        return code

    return None


# ---------------------------------------------------------------------------
# Safe execution sandbox
# ---------------------------------------------------------------------------
SAFE_BUILTINS = {
    "True": True,
    "False": False,
    "None": None,
    "abs": abs,
    "all": all,
    "any": any,
    "bool": bool,
    "dict": dict,
    "enumerate": enumerate,
    "float": float,
    "frozenset": frozenset,
    "int": int,
    "isinstance": isinstance,
    "len": len,
    "list": list,
    "map": map,
    "max": max,
    "min": min,
    "not": None,  # placeholder
    "print": print,
    "range": range,
    "set": set,
    "sorted": sorted,
    "str": str,
    "sum": sum,
    "tuple": tuple,
    "zip": zip,
}


def _timeout_handler(signum, frame):
    raise TimeoutError("Execution timed out")


def safe_exec_verify(code: str, answer: str, timeout: int = EXEC_TIMEOUT) -> bool | None:
    """Execute verification function in sandbox with timeout."""
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    try:
        namespace = {"__builtins__": SAFE_BUILTINS}
        exec(code, namespace)
        if "verify" not in namespace:
            signal.alarm(0)
            return None
        result = namespace["verify"](answer)
        signal.alarm(0)
        if isinstance(result, bool):
            return result
        return None
    except Exception:
        signal.alarm(0)
        return None


# ---------------------------------------------------------------------------
# SC baseline (majority vote from K traces)
# ---------------------------------------------------------------------------
ANSWER_MAP = {
    "true": "True", "yes": "True",
    "false": "False", "no": "False",
    "unknown": "Unknown", "uncertain": "Unknown", "undetermined": "Unknown",
}


def normalize_answer(ans: str) -> str:
    a = ans.strip().lower()
    return ANSWER_MAP.get(a, ans.strip().capitalize())


def extract_answer_from_trace(trace_text: str) -> str | None:
    """Extract final answer from a reasoning trace."""
    # Look for explicit answer patterns
    patterns = [
        r"(?:the\s+)?(?:final\s+)?answer\s*(?:is|:)\s*(true|false|unknown|uncertain)",
        r"(?:conclusion\s+is\s+)(true|false|unknown|uncertain)",
        r"\b(true|false|unknown)\b\s*\.?\s*$",
    ]
    text = trace_text.strip()
    for pat in patterns:
        match = re.search(pat, text, re.IGNORECASE | re.MULTILINE)
        if match:
            return normalize_answer(match.group(1))

    # Last line heuristic
    last_line = text.strip().split("\n")[-1].strip().lower()
    for key in ANSWER_MAP:
        if key in last_line:
            return ANSWER_MAP[key]
    return None


SC_PROMPT_TEMPLATE = """Given the following premises:
{premises}

Determine whether the following conclusion is true, false, or uncertain:
{conclusion}

Think step by step and give your final answer as exactly one of: True, False, or Unknown."""


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def run_problem(item: dict, problem_idx: int) -> dict:
    """Process a single FOLIO problem."""
    pid = item["id"]
    problem_text = item["problem"]
    gt = item["answer"]
    premises, conclusion = parse_problem(problem_text)

    result = {
        "problem_idx": problem_idx,
        "problem_id": pid,
        "ground_truth": gt,
    }

    # --- Step 1: Generate K reasoning traces in one batched call ---
    sc_prompt = SC_PROMPT_TEMPLATE.format(premises=premises, conclusion=conclusion)
    traces = []
    trace_answers = []
    try:
        traces = call_llm(sc_prompt, temperature=TEMPERATURE, n=K_TRACES)
        trace_answers = [extract_answer_from_trace(t) for t in traces]
    except Exception:
        traces = [""] * K_TRACES
        trace_answers = [None] * K_TRACES

    # SC vote
    valid_sc = [a for a in trace_answers if a in CANDIDATES]
    if valid_sc:
        sc_counts = Counter(valid_sc)
        sc_answer = sc_counts.most_common(1)[0][0]
    else:
        sc_answer = "Unknown"
    result["sc_answer"] = sc_answer
    result["sc_correct"] = sc_answer == gt
    result["sc_vote_distribution"] = dict(Counter(valid_sc))

    # --- Step 2: Generate verification function ---
    verify_prompt = VERIFY_PROMPT_TEMPLATE.format(premises=premises, conclusion=conclusion)
    code_gen_success = False
    verify_code = None
    code_response = ""
    try:
        code_response = call_llm(verify_prompt, temperature=0.0)[0]
        verify_code = extract_code(code_response)
        if verify_code is not None:
            # Quick syntax check
            compile(verify_code, "<verify>", "exec")
            code_gen_success = True
    except SyntaxError:
        code_gen_success = False
        verify_code = None
    except Exception:
        code_gen_success = False
        verify_code = None

    result["code_gen_success"] = code_gen_success
    result["verify_code"] = verify_code

    # --- Step 3: Execute verification for each candidate ---
    verify_results = {}
    if code_gen_success and verify_code:
        for cand in CANDIDATES:
            verify_results[cand] = safe_exec_verify(verify_code, cand)
    result["verify_results"] = {k: v for k, v in verify_results.items()}

    # --- Step 4: Determine code-verified answer ---
    if code_gen_success:
        passing = [c for c in CANDIDATES if verify_results.get(c) is True]
        if len(passing) == 1:
            result["prove_answer"] = passing[0]
            result["prove_conclusive"] = True
        else:
            result["prove_answer"] = sc_answer  # fallback to SC
            result["prove_conclusive"] = False
            result["prove_passing_count"] = len(passing)
    else:
        result["prove_answer"] = sc_answer
        result["prove_conclusive"] = False

    result["prove_correct"] = result["prove_answer"] == gt
    result["prove_conclusive_correct"] = (
        result["prove_answer"] == gt if result.get("prove_conclusive") else None
    )

    return result


def main():
    print(f"Loading FOLIO data from {DATA_PATH}")
    data = json.load(open(DATA_PATH))
    print(f"Loaded {len(data)} problems")

    # Check vLLM connectivity
    try:
        resp = requests.get(f"{VLLM_BASE}/v1/models", timeout=10)
        models = resp.json()
        print(f"vLLM models: {[m['id'] for m in models['data']]}")
    except Exception as e:
        print(f"ERROR: Cannot connect to vLLM at {VLLM_BASE}: {e}")
        return

    results = []
    t0 = time.time()

    for idx, item in enumerate(data):
        t_start = time.time()
        r = run_problem(item, idx)
        elapsed = time.time() - t_start
        status = "✓" if r["prove_correct"] else "✗"
        conc = "C" if r.get("prove_conclusive") else "F"
        print(f"[{idx+1:3d}/{len(data)}] {r['problem_id']:12s} gt={r['ground_truth']:8s} "
              f"prove={r['prove_answer']:8s}({conc}) sc={r['sc_answer']:8s} "
              f"code={'OK' if r['code_gen_success'] else 'FAIL':4s} {status} ({elapsed:.1f}s)")
        results.append(r)

    total_time = time.time() - t0

    # --- Compute summary statistics ---
    n = len(results)
    code_gen_ok = sum(1 for r in results if r["code_gen_success"])
    conclusive = [r for r in results if r.get("prove_conclusive")]
    n_conclusive = len(conclusive)
    conclusive_correct = sum(1 for r in conclusive if r["prove_conclusive_correct"])
    prove_correct = sum(1 for r in results if r["prove_correct"])
    sc_correct = sum(1 for r in results if r["sc_correct"])

    summary = {
        "n_problems": n,
        "model": MODEL_NAME,
        "k_traces": K_TRACES,
        "temperature": TEMPERATURE,
        "code_gen_success_rate": code_gen_ok / n,
        "code_gen_success_count": code_gen_ok,
        "verification_conclusive_rate": n_conclusive / n if n else 0,
        "verification_conclusive_count": n_conclusive,
        "accuracy_conclusive_only": conclusive_correct / n_conclusive if n_conclusive else 0,
        "accuracy_prove_with_fallback": prove_correct / n,
        "accuracy_sc_baseline": sc_correct / n,
        "prove_correct_count": prove_correct,
        "sc_correct_count": sc_correct,
        "sica_baseline_ref": 0.7647,  # from exp035
        "sc_baseline_ref": 0.7696,    # from exp035
        "total_wall_time_s": round(total_time, 1),
    }

    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print(f"| {'Metric':<35s} | {'Value':>10s} |")
    print(f"|{'-'*37}|{'-'*12}|")
    print(f"| {'Code gen success rate':<35s} | {summary['code_gen_success_rate']:>9.1%} |")
    print(f"| {'Verification conclusive rate':<35s} | {summary['verification_conclusive_rate']:>9.1%} |")
    print(f"| {'Accuracy (conclusive only)':<35s} | {summary['accuracy_conclusive_only']:>9.1%} |")
    print(f"| {'Accuracy (PROVE + SC fallback)':<35s} | {summary['accuracy_prove_with_fallback']:>9.1%} |")
    print(f"| {'SC baseline (this run)':<35s} | {summary['accuracy_sc_baseline']:>9.1%} |")
    print(f"| {'SC baseline (exp035 ref)':<35s} | {summary['sc_baseline_ref']:>9.1%} |")
    print(f"| {'SICA baseline (exp035 ref)':<35s} | {summary['sica_baseline_ref']:>9.1%} |")
    print(f"| {'Total time':<35s} | {summary['total_wall_time_s']:>8.0f}s |")

    # Save results
    output = {"summary": summary, "results": results}
    out_path = OUTPUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
