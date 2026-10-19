"""Run the external difficulty gate and formal Q1 confirmation matrix."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("MPLBACKEND", "Agg")

import config  # noqa: E402
from eval import evaluate  # noqa: E402
from scripts.analyze_q1_confirmation import analyze  # noqa: E402
from scripts.formal_runner import (  # noqa: E402
    Cell,
    QueuePaused,
    _isolate,
    _load_ledger,
    _valid,
    run_parallel,
    smoke,
)

TOTAL_EXPERIMENT_BUDGET_TOKENS = 24_000_000
LEDGER = "_q1_confirmation_ledger.jsonl"
STATE = "_q1_confirmation_state.json"
LINEAGE_STATE = ROOT / "results" / "official" / "_q1_lineage_state.json"


def external_difficulty_gate() -> dict:
    out = ROOT / "results" / "canary" / "q1-external-v001"
    summary_file = out / "summary.json"
    if summary_file.exists() and _valid(json.loads(summary_file.read_text())):
        summary = json.loads(summary_file.read_text())
    else:
        summary = evaluate(
            str(ROOT / "harnesses/tddgen_hidden/v001/harness.py"),
            str(ROOT / "benchmarks/q1_external/canary"),
            repeats=1,
            concurrency=4,
            out_dir=str(out),
        )
    if not _valid(summary):
        cell = Cell(
            "q1-external-difficulty-gate",
            "harnesses/tddgen_hidden/v001/harness.py",
            "q1_external",
            "canary",
            "q1-external-difficulty-gate",
            500_000,
        )
        _isolate(ROOT, cell, out, summary)
        raise QueuePaused("Q1 external difficulty gate infra-invalid")
    passed = summary["pass_rate_mean"]
    if passed in (0.0, 1.0):
        raise QueuePaused(
            f"Q1 external difficulty gate stopped at {passed:.0%}"
        )
    gate = {
        "status": "passed",
        "pass_rate": passed,
        "target": "1-3 of 4",
        "tokens": summary.get("total_tokens", 0),
    }
    path = ROOT / "results" / "official" / "_q1_external_gate.json"
    path.write_text(json.dumps(gate, indent=2) + "\n")
    return gate


def external_canary(cell: Cell) -> int:
    if cell.split != "val":
        return 0
    out = ROOT / "results" / "canary" / cell.key
    summary_file = out / "summary.json"
    if summary_file.exists() and _valid(json.loads(summary_file.read_text())):
        return 0
    manifest = json.loads(
        (ROOT / "benchmarks/q1_external/_manifest.json").read_text()
    )
    task_id = manifest["val"][0]
    task = (
        ROOT / "benchmarks/q1_external/val"
        / task_id.replace("/", "_").lower()
    )
    with tempfile.TemporaryDirectory(prefix="q1-external-canary-") as temp:
        temp_path = Path(temp)
        (temp_path / task.name).symlink_to(task, target_is_directory=True)
        summary = evaluate(
            str(ROOT / cell.harness),
            str(temp_path),
            repeats=1,
            concurrency=1,
            out_dir=str(out),
        )
    if not _valid(summary):
        _isolate(ROOT, cell, out, summary)
        raise QueuePaused(f"{cell.key}: external canary infra-invalid")
    return int(summary.get("total_tokens", 0))


def priority_cells() -> tuple[Cell, ...]:
    """Return the frozen revision-A order from the resumption protocol."""
    if not LINEAGE_STATE.exists():
        raise QueuePaused("Q1 independent lineage state is missing")
    state = json.loads(LINEAGE_STATE.read_text())
    if state.get("status") != "complete":
        raise QueuePaused("Q1 independent lineages are incomplete")
    r01 = state["lineages"]["tddgen_hidden_r01"]["harness"]
    r02 = state["lineages"]["tddgen_hidden_r02"]["harness"]
    return (
        Cell(
            "q1confirm-r02-train", r02, "tddgen_hidden", "train",
            "q1confirm-r02-train", 2_500_000,
        ),
        Cell(
            "q1confirm-v001-external",
            "harnesses/tddgen_hidden/v001/harness.py",
            "q1_external", "val", "q1confirm-v001-external",
            1_200_000, True,
        ),
        Cell(
            "q1confirm-r00-external",
            "harnesses/tddgen_hidden/v005/harness.py",
            "q1_external", "val", "q1confirm-r00-external",
            2_500_000, True,
        ),
        Cell(
            "q1confirm-r02-external", r02, "q1_external", "val",
            "q1confirm-r02-external", 2_500_000, True,
        ),
        Cell(
            "q1confirm-r01-train", r01, "tddgen_hidden", "train",
            "q1confirm-r01-train", 2_500_000,
        ),
        Cell(
            "q1confirm-r01-external", r01, "q1_external", "val",
            "q1confirm-r01-external", 2_500_000, True,
        ),
    )


def _summary_tokens(path: Path) -> int:
    if not path.exists():
        return 0
    return int(json.loads(path.read_text()).get("total_tokens", 0))


def preformal_executor_spent(root: Path = ROOT) -> int:
    """Reconstruct all Q1-confirmation executor use before formal cells."""
    total = 0
    for lineage in ("tddgen_hidden_r01", "tddgen_hidden_r02"):
        for path in (root / "harnesses" / lineage).glob(
            "v*/train_summary.json"
        ):
            total += _summary_tokens(path)
    for path in (root / "results" / "canary").glob("q1-*/summary.json"):
        total += _summary_tokens(path)
    invalid = root / "results" / "invalid"
    if invalid.exists():
        for path in invalid.glob("*q1-tddgen_hidden_r0*/**/summary.json"):
            total += _summary_tokens(path)
    return total


def remaining_formal_budget(root: Path = ROOT) -> int:
    """Apply revision B1's 24M total cap, including invalid formal attempts."""
    invalid_formal = sum(
        int(entry.get("tokens", 0))
        for entry in _load_ledger(root, LEDGER)
        if entry.get("status") == "invalid"
    )
    return max(
        0,
        TOTAL_EXPERIMENT_BUDGET_TOKENS
        - preformal_executor_spent(root)
        - invalid_formal,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate-only", action="store_true")
    parser.add_argument("--stagger-seconds", type=float, default=30)
    args = parser.parse_args()
    smoke((config.EXECUTOR_MODEL,))
    gate = external_difficulty_gate()
    print("external gate", gate)
    if args.gate_only:
        return
    ordered = priority_cells()
    budget = remaining_formal_budget(ROOT)
    print(
        "Q1 total budget:",
        TOTAL_EXPERIMENT_BUDGET_TOKENS,
        "preformal spent:",
        preformal_executor_spent(ROOT),
        "formal allowance:",
        budget,
    )
    try:
        run_parallel(
            {"priority": ordered},
            root=ROOT,
            budget_tokens=budget,
            run_canary_fn=external_canary,
            stagger_seconds=0,
            ledger_filename=LEDGER,
            state_filename=STATE,
        )
    except QueuePaused:
        analyze(ROOT)
        raise
    report = analyze(ROOT)
    print(
        "Q1 confirmation:",
        report["decision"],
        report["external_effect_qualified"],
        report["external_effect_ci95"],
    )


if __name__ == "__main__":
    main()
