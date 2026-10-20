# SWE-agent trajectories data loader for agent_progress_probe project.
# Loads and parses nebius/SWE-agent-trajectories JSONL data into structured objects.

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Step:
    """A single step in an agent trajectory."""
    index: int
    role: str  # "system", "user", or "ai"
    text: str
    mask: bool
    cutoff_date: Optional[str] = None
    system_prompt: Optional[str] = None

    @property
    def is_action(self) -> bool:
        return self.role == "ai"

    @property
    def is_observation(self) -> bool:
        return self.role == "user" and self.index > 0

    @property
    def is_system(self) -> bool:
        return self.role == "system"

    @property
    def command(self) -> Optional[str]:
        """Extract the command from an AI step's code block. Returns None for non-AI steps."""
        if self.role != "ai":
            return None
        match = re.search(r"```\n?(.*?)```", self.text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    @property
    def has_file_display(self) -> bool:
        return "[File:" in self.text

    @property
    def has_error(self) -> bool:
        return "Traceback" in self.text or "Error" in self.text

    @property
    def has_test_output(self) -> bool:
        text = self.text
        return ("PASSED" in text or "FAILED" in text) and "test" in text.lower()


@dataclass
class TestResult:
    """Parsed test results from eval_logs."""
    passed: list[str] = field(default_factory=list)
    failed: list[str] = field(default_factory=list)
    errored: list[str] = field(default_factory=list)

    @property
    def total(self) -> int:
        return len(self.passed) + len(self.failed) + len(self.errored)

    @property
    def pass_rate(self) -> float:
        if self.total == 0:
            return 0.0
        return len(self.passed) / self.total


@dataclass
class Trajectory:
    """A complete agent trajectory for one SWE-bench instance attempt."""
    instance_id: str
    model_name: str
    target: bool  # True = resolved, False = unresolved
    steps: list[Step]
    exit_status: str
    generated_patch: Optional[str]
    eval_logs: Optional[str]
    row_index: int = 0  # source file line number, ensures unique trajectory_id

    @property
    def num_steps(self) -> int:
        return len(self.steps)

    @property
    def actions(self) -> list[Step]:
        return [s for s in self.steps if s.is_action]

    @property
    def observations(self) -> list[Step]:
        return [s for s in self.steps if s.is_observation]

    @property
    def issue_text(self) -> Optional[str]:
        """The issue description from step 1 (first user message)."""
        if len(self.steps) > 1 and self.steps[1].role == "user":
            return self.steps[1].text
        return None

    @property
    def has_patch(self) -> bool:
        return bool(self.generated_patch and self.generated_patch.strip())

    def parse_eval_test_results(self) -> Optional[TestResult]:
        """Parse test results from eval_logs.

        Returns:
            TestResult with lists of passed/failed/errored test names,
            or None if eval_logs is empty or has no test section.
        """
        if not self.eval_logs:
            return None
        start_marker = "___TESTS_SECTION___"
        end_marker = "___TESTS_SECTION_END"
        if start_marker not in self.eval_logs:
            return None
        start = self.eval_logs.index(start_marker)
        end = self.eval_logs.index(end_marker) if end_marker in self.eval_logs else len(self.eval_logs)
        section = self.eval_logs[start:end]

        result = TestResult()
        for line in section.splitlines():
            line = line.strip()
            if line.startswith("PASSED "):
                result.passed.append(line[7:])
            elif line.startswith("FAILED "):
                name = line[7:].split(" - ")[0]
                result.failed.append(name)
            elif line.startswith("ERROR "):
                result.errored.append(line[6:])
        return result

    def extract_mid_trajectory_test_results(self) -> list[tuple[int, TestResult]]:
        """Find pytest runs within the trajectory observations.

        Returns:
            List of (step_index, TestResult) for steps containing pytest output.
        """
        results = []
        for step in self.observations:
            if not step.has_test_output:
                continue
            tr = TestResult()
            for line in step.text.splitlines():
                line = line.strip()
                if line.startswith("PASSED "):
                    tr.passed.append(line[7:])
                elif line.startswith("FAILED "):
                    name = line[7:].split(" - ")[0]
                    tr.failed.append(name)
                elif line.startswith("ERROR "):
                    tr.errored.append(line[6:])
            summary = re.search(r"(\d+) passed", step.text)
            if summary and not tr.passed:
                tr.passed = [f"unnamed_{i}" for i in range(int(summary.group(1)))]
            summary = re.search(r"(\d+) failed", step.text)
            if summary and not tr.failed:
                tr.failed = [f"unnamed_{i}" for i in range(int(summary.group(1)))]
            if tr.total > 0:
                results.append((step.index, tr))
        return results

    def get_edit_commands(self) -> list[tuple[int, str]]:
        """Extract all edit commands from the trajectory.

        Returns:
            List of (step_index, command_text) for steps containing edit commands.
        """
        edits = []
        for step in self.actions:
            cmd = step.command
            if cmd and cmd.strip().startswith("edit"):
                edits.append((step.index, cmd))
        return edits


def parse_trajectory(raw: dict, row_index: int = 0) -> Trajectory:
    """Parse a single raw record dict into a Trajectory object.

    Args:
        raw: A dict with keys: instance_id, model_name, target, trajectory,
             exit_status, generated_patch, eval_logs.
        row_index: Source file line number for unique identification.

    Returns:
        A Trajectory object with parsed Steps.
    """
    steps = []
    for i, step_raw in enumerate(raw.get("trajectory") or []):
        steps.append(Step(
            index=i,
            role=step_raw.get("role", "unknown"),
            text=step_raw.get("text") or "",
            mask=step_raw.get("mask", False),
            cutoff_date=step_raw.get("cutoff_date"),
            system_prompt=step_raw.get("system_prompt"),
        ))

    return Trajectory(
        instance_id=raw.get("instance_id", ""),
        model_name=raw.get("model_name", ""),
        target=raw.get("target", False),
        steps=steps,
        exit_status=raw.get("exit_status", ""),
        generated_patch=raw.get("generated_patch"),
        eval_logs=raw.get("eval_logs"),
        row_index=row_index,
    )


def extract_steps(trajectory: Trajectory) -> list[Step]:
    """Extract the step sequence from a trajectory, excluding the system step.

    Args:
        trajectory: A parsed Trajectory object.

    Returns:
        List of Steps starting from step 1 (the issue description),
        excluding the system prompt step.
    """
    return [s for s in trajectory.steps if not s.is_system]


def load_trajectories(path: str | Path) -> list[Trajectory]:
    """Load trajectories from a JSONL file.

    Args:
        path: Path to a .jsonl file where each line is a JSON record.

    Returns:
        List of Trajectory objects.
    """
    path = Path(path)
    trajectories = []
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            trajectories.append(parse_trajectory(raw, row_index=i))
    return trajectories


def load_trajectories_streaming(path: str | Path, limit: int | None = None):
    """Lazily yield trajectories from a JSONL file.

    Args:
        path: Path to a .jsonl file.
        limit: Maximum number of trajectories to yield. None for all.

    Yields:
        Trajectory objects one at a time.
    """
    path = Path(path)
    count = 0
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            yield parse_trajectory(raw, row_index=i)
            count += 1
            if limit and count >= limit:
                break


if __name__ == "__main__":
    import sys
    data_path = sys.argv[1] if len(sys.argv) > 1 else (
        "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/"
        "agent_progress_probe/artifacts/data/swe_agent_trajectories_1000.jsonl"
    )

    print(f"Loading from {data_path}...")
    trajs = load_trajectories(data_path)
    print(f"Loaded {len(trajs)} trajectories")

    resolved = [t for t in trajs if t.target]
    unresolved = [t for t in trajs if not t.target]
    print(f"Resolved: {len(resolved)}, Unresolved: {len(unresolved)}")

    t = trajs[0]
    print(f"\nSample trajectory: {t.instance_id}")
    print(f"  Steps: {t.num_steps}, Actions: {len(t.actions)}, Observations: {len(t.observations)}")
    print(f"  Has patch: {t.has_patch}, Target: {t.target}")

    test_result = t.parse_eval_test_results()
    if test_result:
        print(f"  Eval tests: {len(test_result.passed)} passed, {len(test_result.failed)} failed, pass_rate={test_result.pass_rate:.2f}")

    edits = t.get_edit_commands()
    print(f"  Edit commands: {len(edits)}")

    mid_tests = t.extract_mid_trajectory_test_results()
    print(f"  Mid-trajectory test runs: {len(mid_tests)}")
