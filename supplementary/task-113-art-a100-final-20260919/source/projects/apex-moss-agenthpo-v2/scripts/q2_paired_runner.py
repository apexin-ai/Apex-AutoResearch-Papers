"""Restart-safe runner for the frozen Q2 paired-feedback confirmation."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from eval import evaluate
import config
from scripts.analyze_q2_paired import analyze
from scripts.formal_runner import (
    Cell,
    QueuePaused,
    _isolate,
    _valid,
    run_parallel,
    smoke,
)

BUDGET_TOKENS = 7_000_000

G_CELLS = (
    Cell(
        "q2paired-v001-tdd-v0",
        "harnesses/tddgen_hidden/v001/harness.py",
        "q2_paired",
        "tdd_val_v0",
        "q2paired-v001-tdd-v0",
        800_000,
        True,
    ),
    Cell(
        "q2paired-v001-spec-v1",
        "harnesses/tddgen_hidden/v001/harness.py",
        "q2_paired",
        "spec_val_v1",
        "q2paired-v001-spec-v1",
        800_000,
        True,
    ),
)

S_CELLS = (
    Cell(
        "q2paired-v005-tdd-v0",
        "harnesses/tddgen_hidden/v005/harness.py",
        "q2_paired",
        "tdd_val_v0",
        "q2paired-v005-tdd-v0",
        2_200_000,
        True,
    ),
    Cell(
        "q2paired-v005-spec-v1",
        "harnesses/tddgen_hidden/v005/harness.py",
        "q2_paired",
        "spec_val_v1",
        "q2paired-v005-spec-v1",
        2_200_000,
        True,
    ),
)


def _canary_task(cell: Cell, root: Path) -> Path:
    manifest = json.loads(
        (root / "benchmarks" / "q2_paired" / "_manifest.json").read_text()
    )
    block = "tdd" if cell.split.startswith("tdd_") else "spec"
    entries = [task for task in manifest["tasks"] if task["block"] == block]
    selected = min(
        entries,
        key=lambda task: hashlib.sha256(task["task_id"].encode()).hexdigest(),
    )
    return root / "benchmarks" / cell.family / cell.split / selected["name"]


def run_paired_canary(cell: Cell, *, root: Path = ROOT) -> None:
    out = root / "results" / "canary" / cell.key
    summary_file = out / "summary.json"
    if summary_file.exists() and _valid(json.loads(summary_file.read_text())):
        return
    task = _canary_task(cell, root)
    with tempfile.TemporaryDirectory(prefix="q2-paired-canary-") as temp:
        temp_path = Path(temp)
        (temp_path / task.name).symlink_to(task, target_is_directory=True)
        summary = evaluate(
            str(root / cell.harness),
            str(temp_path),
            repeats=1,
            concurrency=1,
            out_dir=str(out),
        )
    if not _valid(summary):
        _isolate(root, cell, out, summary)
        raise QueuePaused(f"{cell.key}: paired canary was infra-invalid")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stagger-seconds", type=float, default=30)
    args = parser.parse_args()
    smoke((config.EXECUTOR_MODEL,))
    run_parallel(
        {"generic": G_CELLS, "specialized": S_CELLS},
        root=ROOT,
        budget_tokens=BUDGET_TOKENS,
        run_canary_fn=lambda cell: run_paired_canary(cell, root=ROOT),
        stagger_seconds=args.stagger_seconds,
        ledger_filename="_q2_paired_ledger.jsonl",
        state_filename="_q2_paired_state.json",
    )
    report = analyze(ROOT)
    print(
        "Q2 paired:",
        report["decision"],
        f"interaction={report['interaction_all']:.1%}",
        f"CI={report['interaction_all_ci95']}",
    )


if __name__ == "__main__":
    main()
