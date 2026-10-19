"""Initialize and evolve two independent tdd hidden-Harness lineages."""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import config  # noqa: E402
from eval import evaluate  # noqa: E402
from harness_source import validate_harness, validate_sandbox_contract  # noqa: E402
from proposer import propose, repair_candidate  # noqa: E402
from scripts.formal_runner import QueuePaused, _isolate, _valid, smoke  # noqa: E402

LINEAGES = ("tddgen_hidden_r01", "tddgen_hidden_r02")
TRAIN = ROOT / "benchmarks" / "tddgen_hidden" / "train"
START = ROOT / "harnesses" / "tddgen_hidden" / "v001" / "harness.py"
FAMILY_DESC = (
    "Hidden-verification implementation: solution.py is a documented stub; "
    "one visible behavior test is incomplete feedback and the unseen final "
    "suite requires specification-driven boundary reasoning."
)
MAX_IMPROVEMENT_ROUNDS = 6
MAX_CONTRACT_REPAIR_ROUNDS = 3
QUICK_BUDGET_TOKENS = 10_000_000
CELL_RESERVE_TOKENS = 1_500_000
STATE = ROOT / "results" / "official" / "_q1_lineage_state.json"


class FakeBlock(SimpleNamespace):
    def model_dump(self) -> dict:
        return {
            key: value for key, value in vars(self).items()
            if value is not None
        }


class FakeMessages:
    def __init__(self, forbidden_write_path: str | None = None):
        self.forbidden_write_path = forbidden_write_path
        self.calls = 0

    def create(self, **kwargs):
        self.calls += 1
        if self.calls == 1 and self.forbidden_write_path:
            return SimpleNamespace(
                content=[FakeBlock(
                    type="tool_use",
                    id="offline-tool-1",
                    name="write_file",
                    input={
                        "path": self.forbidden_write_path,
                        "content": "# forbidden smoke write\n",
                    },
                )],
                # Deliberately inconsistent: content is authoritative.
                stop_reason="end_turn",
                usage=SimpleNamespace(input_tokens=1, output_tokens=1),
            )
        return SimpleNamespace(
            content=[FakeBlock(type="text", text="offline smoke complete")],
            stop_reason="end_turn",
            usage=SimpleNamespace(input_tokens=1, output_tokens=1),
        )


def offline_smoke(harness_path: Path, *, strict: bool = False) -> dict:
    """Import and execute a generated Harness against fake API/tools."""
    code = harness_path.read_text()
    validate_harness(code)
    validate_sandbox_contract(code)
    name = f"q1_smoke_{harness_path.parent.parent.name}_{harness_path.parent.name}"
    spec = importlib.util.spec_from_file_location(name, harness_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    original_client = module.anthropic.Anthropic
    dispatched_writes = []
    try:
        with tempfile.TemporaryDirectory(prefix="q1-lineage-smoke-") as temp:
            work = Path(temp)
            (work / "solution.py").write_text("def task_func():\n    pass\n")
            (work / "test_solution.py").write_text(
                "from solution import task_func\n"
                "def test_callable(): assert callable(task_func)\n"
            )
            fake_messages = FakeMessages(
                str(work / "test_solution.py") if strict else None
            )
            module.anthropic.Anthropic = lambda **kwargs: SimpleNamespace(
                messages=fake_messages
            )

            def read_file(data):
                return Path(data["path"]).read_text()

            def write_file(data):
                dispatched_writes.append(data["path"])
                Path(data["path"]).write_text(data["content"])
                return "written"

            dispatch = {
                "read_file": read_file,
                "write_file": write_file,
                "run_tests": lambda data: {
                    "returncode": 1,
                    "stdout": "1 failed",
                    "stderr": "",
                    "passed": False,
                },
            }
            result = module.run(str(work), [], dispatch)
    finally:
        module.anthropic.Anthropic = original_client

    if (
        not isinstance(result, dict)
        or not isinstance(result.get("steps"), int)
        or not isinstance(result.get("tokens"), int)
        or not isinstance(result.get("messages"), list)
    ):
        raise ValueError(f"offline smoke returned invalid result: {harness_path}")
    if strict:
        forbidden = {
            path for path in dispatched_writes
            if Path(path).name != "solution.py"
        }
        if forbidden:
            raise ValueError(
                f"strict smoke dispatched forbidden write(s): {sorted(forbidden)}"
            )
        messages = result["messages"]
        for index, message in enumerate(messages):
            content = message.get("content")
            if message.get("role") != "assistant" or not isinstance(content, list):
                continue
            tool_ids = {
                item.get("id") for item in content
                if isinstance(item, dict) and item.get("type") == "tool_use"
            }
            if not tool_ids:
                continue
            if index + 1 >= len(messages):
                raise ValueError("strict smoke found dangling tool_use message")
            following = messages[index + 1]
            results = following.get("content")
            result_ids = {
                item.get("tool_use_id") for item in results
                if isinstance(item, dict) and item.get("type") == "tool_result"
            } if following.get("role") == "user" and isinstance(results, list) else set()
            if not tool_ids <= result_ids:
                raise ValueError(
                    "strict smoke found tool_use without immediate tool_result"
                )
    return result


def initialize_lineage(name: str) -> Path:
    if name not in LINEAGES:
        raise ValueError(f"unknown lineage: {name}")
    target = ROOT / "harnesses" / name / "v001" / "harness.py"
    if target.exists():
        if target.read_bytes() != START.read_bytes():
            raise ValueError(f"{name} v001 differs from frozen generic start")
    else:
        target.parent.mkdir(parents=True)
        shutil.copy2(START, target)
    offline_smoke(target)
    return target.parent.parent


def _quick_spent() -> int:
    total = 0
    for name in LINEAGES:
        for path in (ROOT / "harnesses" / name).glob("v*/train_summary.json"):
            summary = json.loads(path.read_text())
            if _valid(summary):
                total += summary.get("total_tokens", 0)
    return total


def run_lineage_canary(name: str, version: str, harness: Path) -> None:
    out = ROOT / "results" / "canary" / f"q1-{name}-{version}"
    summary_file = out / "summary.json"
    if summary_file.exists() and _valid(json.loads(summary_file.read_text())):
        return
    task = next(path for path in sorted(TRAIN.iterdir()) if path.is_dir())
    with tempfile.TemporaryDirectory(prefix="q1-lineage-canary-") as temp:
        temp_path = Path(temp)
        (temp_path / task.name).symlink_to(task, target_is_directory=True)
        summary = evaluate(
            str(harness),
            str(temp_path),
            repeats=1,
            concurrency=1,
            out_dir=str(out),
        )
    if not _valid(summary):
        from scripts.formal_runner import Cell

        cell = Cell(
            f"q1-{name}-{version}-canary",
            str(harness.relative_to(ROOT)),
            "tddgen_hidden",
            "train",
            f"q1-{name}-{version}-canary",
            CELL_RESERVE_TOKENS,
        )
        _isolate(ROOT, cell, out, summary)
        raise QueuePaused(f"{name}/{version}: canary infra-invalid")


def _archive(entry: dict) -> None:
    with (ROOT / "archive.jsonl").open("a") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


def record_final(name: str, version: str) -> None:
    state = json.loads(STATE.read_text()) if STATE.exists() else {
        "status": "running",
        "lineages": {},
    }
    state["lineages"][name] = {
        "status": "complete",
        "final_version": version,
        "harness": f"harnesses/{name}/{version}/harness.py",
    }
    if all(lineage in state["lineages"] for lineage in LINEAGES):
        state["status"] = "complete"
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def repair_contract(name: str, version: str) -> None:
    """Repair a frozen candidate using only task-independent contract errors."""
    harness = ROOT / "harnesses" / name / version / "harness.py"
    candidate = (
        "MECHANISM: original generated candidate\n"
        f"```python\n{harness.read_text()}```\n"
    )
    contract_error = (
        "Two task-independent Harness contract violations must be repaired. "
        "(1) Treat response.content as authoritative: whenever it contains any "
        "tool_use block, append an immediate user tool_result for every actual "
        "tool_use id even if response.stop_reason is inconsistent. "
        "(2) Before dispatching write_file, allow only the exact solution_path; "
        "for every other path (including test_solution.py), return a blocked "
        "tool_result and do not call the dispatch function. Preserve the intended "
        "workflow mechanism and all frozen signatures/models."
    )
    code, mechanism, _ = repair_candidate(
        str(harness.parent.parent),
        candidate,
        contract_error,
    )
    validate_harness(code)
    validate_sandbox_contract(code)
    canary = ROOT / "results" / "canary" / f"q1-{name}-{version}"
    if canary.exists():
        invalid = (
            ROOT / "results" / "invalid"
            / f"q1-{name}-{version}-pre-contract-repair-canary"
        )
        if invalid.exists():
            raise ValueError(f"canary invalidation target already exists: {invalid}")
        invalid.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(canary), str(invalid))
    harness.write_text(code)
    offline_smoke(harness, strict=True)
    _archive({
        "family": name,
        "version": version,
        "event": "contract_repair",
        "mechanism": mechanism,
        "reason": contract_error,
        "independent_lineage": True,
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
    })


def _generic_smoke_error(exc: ValueError) -> str:
    """Remove run-specific paths while retaining the rejected contract."""
    message = str(exc)
    if "forbidden write" in message:
        return (
            "The strict offline contract smoke observed write_file being "
            "dispatched for a path other than the exact solution_path. Hard-block "
            "that call and return a tool_result without invoking the dispatcher."
        )
    if "tool_use" in message:
        return (
            "The strict offline contract smoke observed a response.content "
            "tool_use without an immediate matching user tool_result. Treat the "
            "actual content blocks as authoritative even when stop_reason is "
            "inconsistent, and pair every tool_use id before the next API call."
        )
    return "The candidate failed the task-independent strict offline Harness smoke."


def enforce_generated_contract(
    name: str,
    version: str,
    mechanism: str,
) -> str:
    """Repair one generated candidate without exposing benchmark information."""
    harness = ROOT / "harnesses" / name / version / "harness.py"
    try:
        offline_smoke(harness, strict=True)
        return mechanism
    except ValueError as exc:
        contract_error = _generic_smoke_error(exc)

    reasons = []
    for attempt in range(1, MAX_CONTRACT_REPAIR_ROUNDS + 1):
        reasons.append(contract_error)
        candidate = (
            f"MECHANISM: {mechanism}\n"
            f"```python\n{harness.read_text()}```\n"
        )
        code, repaired_mechanism, _ = repair_candidate(
            str(harness.parent.parent),
            candidate,
            contract_error,
        )
        validate_harness(code)
        validate_sandbox_contract(code)
        harness.write_text(code)
        try:
            offline_smoke(harness, strict=True)
        except ValueError as exc:
            contract_error = _generic_smoke_error(exc)
            mechanism = repaired_mechanism
            continue
        _archive({
            "family": name,
            "version": version,
            "event": "contract_repair",
            "mechanism": repaired_mechanism,
            "reason": reasons,
            "repair_attempts": attempt,
            "independent_lineage": True,
            "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        })
        return repaired_mechanism
    raise QueuePaused(
        f"{name}/{version}: contract repair failed "
        f"{MAX_CONTRACT_REPAIR_ROUNDS} strict smoke attempts: {contract_error}"
    )


def evolve(name: str) -> str:
    lineage = initialize_lineage(name)
    while True:
        versions = sorted(
            path.name for path in lineage.iterdir()
            if path.is_dir() and path.name.startswith("v")
        )
        current = versions[-1]
        current_number = int(current[1:])
        version_dir = lineage / current
        harness = version_dir / "harness.py"
        if current == "v001":
            offline_smoke(harness)
        else:
            enforce_generated_contract(
                name,
                current,
                "existing generated candidate",
            )
        run_lineage_canary(name, current, harness)

        summary_file = version_dir / "train_summary.json"
        if summary_file.exists():
            summary = json.loads(summary_file.read_text())
        else:
            if _quick_spent() + CELL_RESERVE_TOKENS > QUICK_BUDGET_TOKENS:
                raise QueuePaused("Q1 lineage quick-evaluation budget guard")
            summary = evaluate(
                str(harness),
                str(TRAIN),
                repeats=1,
                concurrency=4,
                out_dir=str(version_dir / "train_results"),
            )
            if not _valid(summary):
                from scripts.formal_runner import Cell

                cell = Cell(
                    f"q1-{name}-{current}-quick",
                    str(harness.relative_to(ROOT)),
                    "tddgen_hidden",
                    "train",
                    f"q1-{name}-{current}-quick",
                    CELL_RESERVE_TOKENS,
                )
                _isolate(
                    ROOT,
                    cell,
                    version_dir / "train_results",
                    summary,
                )
                raise QueuePaused(f"{name}/{current}: quick train infra-invalid")
            summary_file.write_text(json.dumps(summary, indent=2) + "\n")

        if (
            summary["pass_rate_mean"] >= 1.0
            or current_number >= MAX_IMPROVEMENT_ROUNDS + 1
        ):
            return current

        next_version = f"v{current_number + 1:03d}"
        next_dir = lineage / next_version
        if next_dir.exists():
            continue
        code, mechanism = propose(str(lineage), FAMILY_DESC)
        next_dir.mkdir()
        (next_dir / "harness.py").write_text(code)
        mechanism = enforce_generated_contract(name, next_version, mechanism)
        _archive({
            "family": name,
            "version": next_version,
            "parent": current,
            "mechanism": mechanism,
            "parent_train_pass_rate": summary["pass_rate_mean"],
            "independent_lineage": True,
            "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lineage", choices=(*LINEAGES, "all"), default="all"
    )
    parser.add_argument("--init-only", action="store_true")
    parser.add_argument("--repair-contract-version")
    args = parser.parse_args()
    selected = LINEAGES if args.lineage == "all" else (args.lineage,)
    for name in selected:
        initialize_lineage(name)
    if args.repair_contract_version:
        if len(selected) != 1:
            raise ValueError("contract repair requires exactly one lineage")
        repair_contract(selected[0], args.repair_contract_version)
        print(f"repaired {selected[0]}/{args.repair_contract_version}")
        return
    if args.init_only:
        print("initialized", ", ".join(selected))
        return
    smoke((config.EXECUTOR_MODEL, config.PROPOSER_MODEL))
    for name in selected:
        final = evolve(name)
        record_final(name, final)
        print(f"{name} final: {final}")


if __name__ == "__main__":
    main()
