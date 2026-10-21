"""HumanEval evaluation utilities: dataset loading, code extraction, and sandboxed execution."""

import re
import subprocess
import tempfile
import time


def load_humaneval(num_tasks: int = 50, seed: int = 42) -> list[dict]:
    """Load and sample HumanEval tasks from HuggingFace."""
    from datasets import load_dataset

    ds = load_dataset("openai_humaneval", split="test")
    ds = ds.shuffle(seed=seed).select(range(min(num_tasks, len(ds))))

    tasks = []
    for item in ds:
        tasks.append({
            "task_id": item["task_id"],
            "prompt": item["prompt"],
            "canonical_solution": item["canonical_solution"],
            "test": item["test"],
            "entry_point": item["entry_point"],
        })
    return tasks


def extract_code_from_response(text: str) -> str:
    """Extract Python code from LLM response text.

    Tries fenced code blocks first, then falls back to finding function definitions.
    """
    blocks = re.findall(r"```(?:python)?\s*\n(.*?)```", text, re.DOTALL)
    if blocks:
        return blocks[-1].strip()

    match = re.search(r"(def \w+\(.*?\):.*?)(?=\n(?:[^ \t\n]|\Z))", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    return text.strip()


def execute_code_safely(code: str, test: str, entry_point: str, timeout: int = 10) -> dict:
    """Execute generated code with test cases in a subprocess sandbox.

    Returns dict with is_correct, error, and execution_time.
    """
    full_code = code + "\n\n" + test + "\n\n" + f"check({entry_point})\n"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=True) as f:
        f.write(full_code)
        f.flush()

        t0 = time.time()
        try:
            result = subprocess.run(
                ["python3", f.name],
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            elapsed = time.time() - t0
            return {
                "is_correct": result.returncode == 0,
                "error": result.stderr.strip() if result.returncode != 0 else None,
                "execution_time": round(elapsed, 3),
            }
        except subprocess.TimeoutExpired:
            return {
                "is_correct": False,
                "error": "timeout",
                "execution_time": float(timeout),
            }
