"""Canonical evaluator — the only component allowed to assign scores.

Anti-cheating: after the harness runs, every file except solution.py is restored
from the pristine benchmark copy; any tampering is recorded and the task scores 0.
Each task run executes in a subprocess with a hard wall-clock timeout.

Usage:
  python eval.py <harness.py> <benchmark_dir> [--repeats 3] [--concurrency 4] [--out DIR]
"""

import argparse
import json
import statistics
import subprocess
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from harness_source import InvalidHarness, validate_sandbox_contract

HERE = Path(__file__).resolve().parent
TASK_TIMEOUT = 300  # hard wall-clock cap per task run (seconds)


def check_model_lock(harness_path: Path) -> None:
    """The executor model is part of the protocol; refuse to score anything else."""
    src = harness_path.read_text()
    if 'MODEL = "claude-haiku-4-5"' not in src:
        raise SystemExit(
            f"REFUSED: {harness_path} must declare MODEL = \"claude-haiku-4-5\" "
            "(executor model is frozen by the evaluation protocol)"
        )


def check_sandbox_contract(harness_path: Path) -> None:
    try:
        validate_sandbox_contract(harness_path.read_text())
    except InvalidHarness as exc:
        raise SystemExit(
            f"REFUSED: {harness_path} violates the sandbox contract: {exc}"
        ) from exc


def run_one(harness_path: Path, task_dir: Path, out_file: Path) -> dict:
    cmd = [sys.executable, str(HERE / "_eval_one.py"), str(harness_path), str(task_dir), str(out_file)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TASK_TIMEOUT)
        if out_file.exists():
            return json.loads(out_file.read_text())
        return {
            "task": task_dir.name,
            "passed": False,
            "tampered": False,
            "error": f"no result file; stderr: {proc.stderr[-500:]}",
            "category": "harness_error",
            "contract_violations": 0,
        }
    except subprocess.TimeoutExpired:
        return {
            "task": task_dir.name,
            "passed": False,
            "tampered": False,
            "error": f"hard timeout {TASK_TIMEOUT}s",
            "category": "timeout",
            "contract_violations": 0,
        }


def evaluate(harness_path: str, benchmark_dir: str, repeats: int = 3,
             concurrency: int = 4, out_dir: str | None = None) -> dict:
    harness_path = Path(harness_path).resolve()
    benchmark_dir = Path(benchmark_dir).resolve()
    check_model_lock(harness_path)
    check_sandbox_contract(harness_path)

    task_dirs = sorted([d for d in benchmark_dir.iterdir() if d.is_dir() and not d.name.startswith("_")])
    if not task_dirs:
        raise SystemExit(f"no tasks in {benchmark_dir}")

    if out_dir is None:
        out_dir = HERE / "results" / harness_path.parent.name / benchmark_dir.parent.name / benchmark_dir.name
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    jobs = [(t, r) for r in range(repeats) for t in task_dirs]
    results = {}
    start = time.time()
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {
            pool.submit(run_one, harness_path, t, out_dir / f"{t.name}.rep{r}.json"): (t, r)
            for t, r in jobs
        }
        for fut, (t, r) in futures.items():
            res = fut.result()
            results[(t.name, r)] = res
            flag = (
                "PASS" if res.get("passed")
                else ("TAMPERED" if res.get("tampered") else res.get("category", "fail"))
            )
            print(f"  [{r}] {t.name}: {flag}", flush=True)

    per_repeat = []
    for r in range(repeats):
        n_pass = sum(1 for t in task_dirs if results[(t.name, r)].get("passed"))
        per_repeat.append(n_pass / len(task_dirs))

    category_counts = Counter(
        result.get("category", "harness_error")
        for result in results.values()
    )
    summary = {
        "harness": str(harness_path),
        "benchmark": str(benchmark_dir),
        "repeats": repeats,
        "n_tasks": len(task_dirs),
        "pass_rate_mean": round(statistics.mean(per_repeat), 4),
        "pass_rate_std": round(statistics.pstdev(per_repeat), 4) if repeats > 1 else 0.0,
        "per_repeat": [round(x, 4) for x in per_repeat],
        "per_task_passes": {t.name: sum(1 for r in range(repeats) if results[(t.name, r)].get("passed"))
                            for t in task_dirs},
        "tampered_runs": sum(1 for v in results.values() if v.get("tampered")),
        "contract_violations": sum(
            v.get("contract_violations", 0) for v in results.values()
        ),
        "n_infra_invalid": sum(
            category_counts.get(category, 0)
            for category in ("harness_error", "env_error")
        ),
        "category_counts": dict(sorted(category_counts.items())),
        "total_tokens": sum(v.get("tokens", 0) for v in results.values()),
        "elapsed_sec": round(time.time() - start, 1),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"\n  {harness_path.parent.name} on {benchmark_dir.parent.name}/{benchmark_dir.name}: "
          f"mean={summary['pass_rate_mean']:.1%} std={summary['pass_rate_std']:.3f} "
          f"({summary['elapsed_sec']}s, {summary['total_tokens']} tok)")
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("harness")
    ap.add_argument("benchmark")
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    evaluate(a.harness, a.benchmark, repeats=a.repeats, concurrency=a.concurrency, out_dir=a.out)
