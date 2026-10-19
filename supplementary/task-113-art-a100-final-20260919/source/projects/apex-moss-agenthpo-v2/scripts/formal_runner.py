"""Serial, restart-safe runner for the frozen hidden-final formal queue.

It deliberately delegates all scoring to :func:`eval.evaluate`; this module only
orders cells, enforces the pre-registered budget guard, and isolates invalid grids.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import threading
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import anthropic  # noqa: E402

import config  # noqa: E402
from eval import evaluate  # noqa: E402

FORMAL_BUDGET_TOKENS = 16_500_000  # user-approved basis (a): new valid formal cells
SMOKE_TIMEOUT_SECONDS = 60.0


@dataclass(frozen=True)
class Cell:
    key: str
    harness: str
    family: str
    split: str
    tag: str
    upper_tokens: int
    canary: bool = False


class QueuePaused(RuntimeError):
    """The queue stopped without interpreting an invalid grid as capability."""


Q1_CELLS = (
    Cell("q1-v007-spec-train", "harnesses/specgen_hidden/v007/harness.py",
         "specgen_hidden", "train", "hidden-v007-specgen_hidden-train", 900_000, True),
    Cell("q1-v005-tdd-train", "harnesses/tddgen_hidden/v005/harness.py",
         "tddgen_hidden", "train", "hidden-v005-tddgen_hidden-train", 2_400_000),
    Cell("q1-v005-tdd-val", "harnesses/tddgen_hidden/v005/harness.py",
         "tddgen_hidden", "val", "hidden-v005-tddgen_hidden-val", 1_900_000),
    Cell("q1-v007-spec-val", "harnesses/specgen_hidden/v007/harness.py",
         "specgen_hidden", "val", "hidden-v007-specgen_hidden-val", 1_100_000),
)
Q2_CELLS = (
    Cell("q2-v007-tdd-val", "harnesses/specgen_hidden/v007/harness.py",
         "tddgen_hidden", "val", "hidden-v007-tddgen_hidden-val", 1_200_000, True),
    Cell("q2-v005-spec-val", "harnesses/tddgen_hidden/v005/harness.py",
         "specgen_hidden", "val", "hidden-v005-specgen_hidden-val", 2_200_000, True),
)
Q3_CELLS = (
    Cell("q3-builder0-tdd-train", "harnesses/tddgen_hidden/builder0/harness.py",
         "tddgen_hidden", "train", "hidden-builder0-tddgen_hidden-train", 2_500_000, True),
    Cell("q3-builder0-tdd-val", "harnesses/tddgen_hidden/builder0/harness.py",
         "tddgen_hidden", "val", "hidden-builder0-tddgen_hidden-val", 2_500_000),
    Cell("q3-builder0-spec-train", "harnesses/specgen_hidden/builder0/harness.py",
         "specgen_hidden", "train", "hidden-builder0-specgen_hidden-train", 2_500_000, True),
    Cell("q3-builder0-spec-val", "harnesses/specgen_hidden/builder0/harness.py",
         "specgen_hidden", "val", "hidden-builder0-specgen_hidden-val", 2_500_000),
)


def _paths(root: Path, cell: Cell) -> tuple[Path, Path, Path]:
    harness = root / cell.harness
    benchmark = root / "benchmarks" / cell.family / cell.split
    out = root / "results" / "official" / cell.tag
    return harness, benchmark, out


def _valid(summary: dict) -> bool:
    return (
        summary.get("tampered_runs", 0) == 0
        and summary.get("contract_violations", 0) == 0
        and summary.get("n_infra_invalid", 0) == 0
    )


def _load_ledger(root: Path, filename: str = "_ledger.jsonl") -> list[dict]:
    path = root / "results" / "official" / filename
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def _append_ledger(
        root: Path, entry: dict, filename: str = "_ledger.jsonl"
) -> None:
    path = root / "results" / "official" / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _write_state(
        root: Path, filename: str = "_formal_runner_state.json", **state: object
) -> None:
    path = root / "results" / "official" / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def _quota_errors(out_dir: Path) -> int:
    count = 0
    markers = ("quota", "额度", "token remain", "rate limit", " 5xx", "error code: 5")
    for result_file in out_dir.glob("*.rep*.json"):
        result = json.loads(result_file.read_text())
        error = (result.get("error") or "").lower()
        if any(marker in error for marker in markers):
            count += 1
    return count


def _isolate(root: Path, cell: Cell, out_dir: Path, summary: dict) -> Path:
    base = root / "results" / "invalid" / f"formal-{cell.key}"
    invalid_root = base
    attempt = 1
    while invalid_root.exists():
        attempt += 1
        invalid_root = root / "results" / "invalid" / f"formal-{cell.key}-attempt{attempt}"
    invalid_root.mkdir(parents=True)
    moved = invalid_root / "results"
    shutil.move(str(out_dir), str(moved))
    quota_errors = _quota_errors(moved)
    classification = "quota_fuse" if quota_errors >= 3 else "infra_invalid"
    review = {
        "cell": asdict(cell),
        "attempt": attempt,
        "classification": classification,
        "quota_error_runs": quota_errors,
        "summary": summary,
        "disposition": "Excluded from conclusions; rerun this full 3-repeat cell after recovery.",
    }
    (invalid_root / "review.json").write_text(json.dumps(review, indent=2, ensure_ascii=False))
    return invalid_root


def run_canary(cell: Cell, *, root: Path = ROOT,
               evaluate_fn: Callable = evaluate) -> None:
    """Run one non-formal task from the target family's train split."""
    out = root / "results" / "canary" / f"formal-{cell.key}"
    summary_file = out / "summary.json"
    if summary_file.exists() and _valid(json.loads(summary_file.read_text())):
        return

    source = root / "benchmarks" / cell.family / "train"
    task = next(d for d in sorted(source.iterdir()) if d.is_dir() and not d.name.startswith("_"))
    with tempfile.TemporaryDirectory(prefix="formal-canary-") as temp:
        temp_path = Path(temp)
        (temp_path / task.name).symlink_to(task, target_is_directory=True)
        summary = evaluate_fn(
            str(root / cell.harness), str(temp_path), repeats=1, concurrency=1,
            out_dir=str(out),
        )
    if not _valid(summary):
        _isolate(root, cell, out, summary)
        raise QueuePaused(f"{cell.key}: canary was infra-invalid")


def run_queue(cells: tuple[Cell, ...] | list[Cell], *, root: Path = ROOT,
              budget_tokens: int = FORMAL_BUDGET_TOKENS,
              evaluate_fn: Callable = evaluate,
              run_canary_fn: Callable[[Cell], None] | None = None) -> None:
    """Run frozen cells serially and stop at the first invalid or over-budget cell."""
    canary = run_canary_fn or (lambda cell: run_canary(cell, root=root, evaluate_fn=evaluate_fn))
    ledger = _load_ledger(root)
    completed = {entry["cell"] for entry in ledger if entry.get("status") == "valid"}
    spent = sum(entry.get("tokens", 0) for entry in ledger if entry.get("status") == "valid")

    for cell in cells:
        if cell.key in completed:
            continue
        invalid_attempts = sum(
            1 for entry in ledger
            if entry.get("cell") == cell.key and entry.get("status") == "invalid"
        )
        if invalid_attempts >= 3:
            _write_state(root, status="third_infra_pause", cell=cell.key, spent=spent,
                         budget_tokens=budget_tokens)
            raise QueuePaused(
                f"{cell.key}: already has three infra-invalid attempts; plan review required"
            )
        if budget_tokens - spent < cell.upper_tokens * 1.5:
            _write_state(root, status="budget_pause", cell=cell.key, spent=spent,
                         budget_tokens=budget_tokens)
            raise QueuePaused(f"{cell.key}: budget guard would be violated")
        if cell.canary:
            canary(cell)

        harness, benchmark, out = _paths(root, cell)
        if not harness.exists():
            raise QueuePaused(f"{cell.key}: missing frozen harness {harness}")
        _write_state(root, status="running", cell=cell.key, spent=spent,
                     budget_tokens=budget_tokens)
        summary = evaluate_fn(
            str(harness), str(benchmark), repeats=3, concurrency=4, out_dir=str(out)
        )
        if not _valid(summary):
            invalid = _isolate(root, cell, out, summary)
            _append_ledger(root, {
                "cell": cell.key, "status": "invalid", "tokens": summary.get("total_tokens", 0),
                "attempt": invalid_attempts + 1,
                "invalid_dir": str(invalid.relative_to(root)),
            })
            _write_state(root, status="infra_pause", cell=cell.key, spent=spent,
                         budget_tokens=budget_tokens)
            raise QueuePaused(f"{cell.key}: infra-invalid; queue paused")

        tokens = summary.get("total_tokens", 0)
        _append_ledger(root, {
            "cell": cell.key, "status": "valid", "tokens": tokens,
            "tag": cell.tag, "summary": str((out / "summary.json").relative_to(root)),
        })
        spent += tokens
        _write_state(root, status="completed", cell=cell.key, spent=spent,
                     budget_tokens=budget_tokens)


def run_parallel(
    lanes: dict[str, tuple[Cell, ...] | list[Cell]], *,
    root: Path = ROOT,
    budget_tokens: int = FORMAL_BUDGET_TOKENS,
    evaluate_fn: Callable = evaluate,
    run_canary_fn: Callable[[Cell], None] | None = None,
    stagger_seconds: float = 30,
    ledger_filename: str = "_ledger.jsonl",
    state_filename: str = "_formal_runner_state.json",
) -> None:
    """Run one cell per lane concurrently while preserving lane order."""
    canary = run_canary_fn or (
        lambda cell: run_canary(cell, root=root, evaluate_fn=evaluate_fn)
    )
    lock = threading.Lock()
    global_stop = threading.Event()
    ledger = _load_ledger(root, ledger_filename)
    completed = {
        entry["cell"] for entry in ledger if entry.get("status") == "valid"
    }
    spent = sum(
        entry.get("tokens", 0)
        for entry in ledger if entry.get("status") == "valid"
        or entry.get("status") == "canary"
    )
    reserved = 0
    lane_state = {name: {"status": "pending", "cell": None} for name in lanes}
    lane_errors: dict[str, str] = {}

    def persist() -> None:
        _write_state(
            root, state_filename, mode="controlled_parallel", status=(
                "global_pause" if global_stop.is_set() else "running"
            ), lanes=lane_state, spent=spent, reserved=reserved,
            budget_tokens=budget_tokens,
        )

    def fail_lane(name: str, message: str, *, global_failure: bool = False) -> None:
        with lock:
            lane_errors[name] = message
            lane_state[name] = {"status": "paused", "cell": lane_state[name]["cell"]}
            if global_failure:
                global_stop.set()
            persist()

    def worker(name: str, cells: tuple[Cell, ...] | list[Cell]) -> None:
        nonlocal spent, reserved
        try:
            for cell in cells:
                if cell.key in completed:
                    with lock:
                        lane_state[name] = {"status": "skipped_valid", "cell": cell.key}
                        persist()
                    continue
                if global_stop.is_set():
                    with lock:
                        lane_state[name] = {"status": "global_paused", "cell": cell.key}
                        persist()
                    return

                invalid_attempts = sum(
                    1 for entry in ledger
                    if entry.get("cell") == cell.key
                    and entry.get("status") == "invalid"
                )
                if invalid_attempts >= 3:
                    fail_lane(
                        name,
                        f"{cell.key}: already has three infra-invalid attempts",
                    )
                    return

                requirement = int(cell.upper_tokens * 1.5)
                with lock:
                    if budget_tokens - spent - reserved < requirement:
                        fail_message = f"{cell.key}: budget guard would be violated"
                    else:
                        fail_message = ""
                        reserved += requirement
                        lane_state[name] = {"status": "running", "cell": cell.key}
                        persist()
                if fail_message:
                    with lock:
                        lane_state[name] = {
                            "status": "budget_pause",
                            "cell": cell.key,
                        }
                        persist()
                    fail_lane(name, fail_message, global_failure=True)
                    return

                try:
                    canary_tokens = 0
                    if cell.canary:
                        canary_tokens = int(canary(cell) or 0)
                        if canary_tokens:
                            canary_entry = {
                                "cell": f"{cell.key}::canary",
                                "parent_cell": cell.key,
                                "lane": name,
                                "status": "canary",
                                "tokens": canary_tokens,
                            }
                            with lock:
                                ledger.append(canary_entry)
                                _append_ledger(
                                    root, canary_entry, ledger_filename
                                )
                                spent += canary_tokens
                                persist()
                                can_continue = (
                                    budget_tokens - spent - reserved >= 0
                                )
                            if not can_continue:
                                raise QueuePaused(
                                    f"{cell.key}: canary consumed the "
                                    "remaining budget reserve"
                                )
                    harness, benchmark, out = _paths(root, cell)
                    if not harness.exists():
                        raise QueuePaused(
                            f"{cell.key}: missing frozen harness {harness}"
                        )
                    if out.exists():
                        summary_file = out / "summary.json"
                        if summary_file.exists():
                            cached = json.loads(summary_file.read_text())
                            if _valid(cached):
                                summary = cached
                            else:
                                raise QueuePaused(
                                    f"{cell.key}: existing output is infra-invalid"
                                )
                        else:
                            raise QueuePaused(
                                f"{cell.key}: existing output is incomplete"
                            )
                    else:
                        summary = evaluate_fn(
                            str(harness), str(benchmark), repeats=3,
                            concurrency=4, out_dir=str(out),
                        )
                except Exception as exc:
                    with lock:
                        reserved -= requirement
                    fail_lane(name, str(exc))
                    return

                with lock:
                    reserved -= requirement
                if not _valid(summary):
                    invalid = _isolate(root, cell, out, summary)
                    quota_fuse = _quota_errors(invalid / "results") >= 3
                    entry = {
                        "cell": cell.key,
                        "lane": name,
                        "status": "invalid",
                        "tokens": summary.get("total_tokens", 0),
                        "attempt": invalid_attempts + 1,
                        "invalid_dir": str(invalid.relative_to(root)),
                    }
                    with lock:
                        ledger.append(entry)
                        _append_ledger(root, entry, ledger_filename)
                    fail_lane(
                        name,
                        f"{cell.key}: infra-invalid",
                        global_failure=quota_fuse,
                    )
                    return

                tokens = summary.get("total_tokens", 0)
                entry = {
                    "cell": cell.key,
                    "lane": name,
                    "status": "valid",
                    "tokens": tokens,
                    "tag": cell.tag,
                    "summary": str((out / "summary.json").relative_to(root)),
                }
                with lock:
                    ledger.append(entry)
                    completed.add(cell.key)
                    _append_ledger(root, entry, ledger_filename)
                    spent += tokens
                    lane_state[name] = {"status": "completed_cell", "cell": cell.key}
                    persist()

            with lock:
                lane_state[name] = {"status": "complete", "cell": None}
                persist()
        except BaseException as exc:  # keep sibling lanes auditable
            fail_lane(name, f"{type(exc).__name__}: {exc}")

    threads = []
    for index, (name, cells) in enumerate(lanes.items()):
        thread = threading.Thread(
            target=worker, args=(name, cells), name=f"formal-{name}"
        )
        thread.start()
        threads.append(thread)
        if stagger_seconds and index < len(lanes) - 1:
            time.sleep(stagger_seconds)
    for thread in threads:
        thread.join()

    if lane_errors:
        with lock:
            _write_state(
                root,
                state_filename,
                mode="controlled_parallel",
                status="paused",
                lanes=lane_state,
                spent=spent,
                reserved=reserved,
                budget_tokens=budget_tokens,
            )
        details = "; ".join(
            f"{name}: {message}" for name, message in sorted(lane_errors.items())
        )
        raise QueuePaused(details)
    with lock:
        _write_state(
            root,
            state_filename,
            mode="controlled_parallel",
            status="complete",
            lanes=lane_state,
            spent=spent,
            reserved=reserved,
            budget_tokens=budget_tokens,
        )


def smoke(models: tuple[str, ...] | None = None) -> None:
    config.load_env()
    client = anthropic.Anthropic(
        timeout=SMOKE_TIMEOUT_SECONDS,
        max_retries=0,
    )
    for model in models or (config.EXECUTOR_MODEL, config.PROPOSER_MODEL):
        response = client.messages.create(
            model=model, max_tokens=16,
            messages=[{"role": "user", "content": "reply with exactly: ok"}],
        )
        print(f"smoke {model}: {response.content[0].text.strip()}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", choices=("q1", "q2", "q3", "full"), default="q1")
    parser.add_argument("--budget-tokens", type=int, default=FORMAL_BUDGET_TOKENS)
    parser.add_argument("--skip-smoke", action="store_true")
    parser.add_argument("--parallel", action="store_true")
    parser.add_argument("--stagger-seconds", type=float, default=30)
    args = parser.parse_args()
    queues = {"q1": Q1_CELLS, "q2": Q2_CELLS, "q3": Q3_CELLS,
              "full": Q1_CELLS + Q2_CELLS + Q3_CELLS}
    if not args.skip_smoke:
        smoke()
    if args.parallel:
        run_parallel(
            {"q1": Q1_CELLS, "q2": Q2_CELLS, "q3": Q3_CELLS},
            budget_tokens=args.budget_tokens,
            stagger_seconds=args.stagger_seconds,
        )
    else:
        run_queue(queues[args.queue], budget_tokens=args.budget_tokens)


if __name__ == "__main__":
    main()
