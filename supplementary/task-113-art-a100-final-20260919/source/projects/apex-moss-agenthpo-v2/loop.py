"""Evolution loop for one task family: evaluate on train benchmark → propose → repeat.

Quick feedback inside the loop uses 1 repeat (direction only); official scoring
elsewhere uses 3 repeats. The loop NEVER touches the validation benchmark.

Usage: python loop.py <family> [--iterations 6]
"""

import argparse
import datetime
import json
from pathlib import Path

from eval import evaluate
from proposer import propose

HERE = Path(__file__).resolve().parent
FAMILY_DESCS = {
    "bugfix": "Bug fixing: solution.py contains working-but-buggy code; make the existing tests pass with a minimal fix.",
    "tddgen": "Test-driven implementation: solution.py contains only a stub (signature/docstring); implement it from scratch so the tests pass.",
    "tddgen_hidden": (
        "Hidden-verification implementation: solution.py is a documented stub; "
        "one visible behavior test is incomplete feedback and the unseen final "
        "suite requires specification-driven boundary reasoning."
    ),
    "specgen_hidden": (
        "Pure-specification hidden verification: solution.py is a documented "
        "stub and the visible suite is import/callability smoke only; implement "
        "the complete specification without behavioral test feedback."
    ),
}


def log_archive(entry: dict) -> None:
    with open(HERE / "archive.jsonl", "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def run_loop(family: str, iterations: int = 6) -> None:
    family_dir = HERE / "harnesses" / family
    train_dir = HERE / "benchmarks" / family / "train"

    versions = sorted([d.name for d in family_dir.iterdir() if d.is_dir() and d.name.startswith("v")])
    current = versions[-1]
    max_version = iterations + 1  # v001 + N improvement rounds; resume-safe cap

    while True:
        v_dir = family_dir / current
        num = int(current[1:])
        next_version = f"v{num + 1:03d}"
        next_dir = family_dir / next_version

        # Resume support: skip work that already finished before an interruption.
        summary_file = v_dir / "train_summary.json"
        if summary_file.exists() and next_dir.exists():
            current = next_version
            continue

        print(f"\n=== [{family}] evaluating {current} on train (round {num}/{max_version}) ===")
        if summary_file.exists():
            summary = json.loads(summary_file.read_text())
        else:
            summary = evaluate(
                str(v_dir / "harness.py"), str(train_dir),
                repeats=1, concurrency=4, out_dir=str(v_dir / "train_results"),
            )
            summary_file.write_text(json.dumps(summary, indent=2))

        if summary["pass_rate_mean"] >= 1.0:
            print(f"[{family}] perfect training score; stopping early.")
            break
        if num >= max_version:
            break

        print(f"[{family}] proposing next version...")
        code, mechanism = propose(str(family_dir), FAMILY_DESCS[family])

        next_dir.mkdir(parents=True)
        (next_dir / "harness.py").write_text(code)

        log_archive({
            "family": family, "version": next_version, "parent": current,
            "mechanism": mechanism,
            "parent_train_pass_rate": summary["pass_rate_mean"],
            "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        })
        print(f"[{family}] {next_version}: {mechanism}")
        current = next_version

    print(f"\n[{family}] final version: {current}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("family", choices=list(FAMILY_DESCS))
    ap.add_argument("--iterations", type=int, default=6)
    a = ap.parse_args()
    run_loop(a.family, a.iterations)
