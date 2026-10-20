"""Labeling functions for agent progress probe.

Each LF takes a sliding window of steps and returns:
  1 = progress, 0 = stagnation, -1 = abstain
"""

from __future__ import annotations

import re
from difflib import SequenceMatcher
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from data_loader import Step, Trajectory

PROGRESS = 1
STAGNATION = 0
ABSTAIN = -1

EDIT_PATTERN = re.compile(r"^edit\s+\d+", re.MULTILINE)
SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep"}


def _extract_edited_files(steps: list[Step]) -> tuple[int, set[str]]:
    """Count edit commands and unique files edited in a window."""
    edit_count = 0
    files = set()
    for step in steps:
        if not step.is_action:
            continue
        cmd = step.command
        if not cmd:
            continue
        if cmd.strip().startswith("edit"):
            edit_count += 1
            # Try to get the filename from the next observation
            idx = step.index
            for s in steps:
                if s.index == idx + 1 and s.is_observation:
                    match = re.search(r"\[File:\s*([^\]]+?)(?:\s*\(\d+\s*lines)", s.text)
                    if match:
                        files.add(match.group(1).strip())
                    break
    return edit_count, files


def _count_search_only(steps: list[Step]) -> int:
    """Count consecutive search/find commands without any edit."""
    count = 0
    for step in steps:
        if not step.is_action:
            continue
        cmd = step.command
        if not cmd:
            continue
        first_word = cmd.strip().split()[0] if cmd.strip() else ""
        if first_word in SEARCH_CMDS:
            count += 1
    return count


def lf_file_diff_delta(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
    """LF1: Whether the agent is meaningfully modifying code in this window."""
    edit_count, files = _extract_edited_files(window)

    if edit_count >= 2 and len(files) >= 1:
        return PROGRESS
    if edit_count == 0:
        search_count = _count_search_only(window)
        if search_count >= 3:
            return STAGNATION
        return ABSTAIN
    return ABSTAIN


def _cmd_similarity(a: str, b: str) -> float:
    """Character-level similarity between two commands using SequenceMatcher."""
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def _has_consecutive_similar(commands: list[str], min_run: int = 3, threshold: float = 0.9) -> bool:
    """Check if there are ≥min_run consecutive commands with similarity > threshold."""
    if len(commands) < min_run:
        return False
    run = 1
    for i in range(1, len(commands)):
        if _cmd_similarity(commands[i - 1], commands[i]) >= threshold:
            run += 1
            if run >= min_run:
                return True
        else:
            run = 1
    return False


def lf_command_repetition(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
    """LF2: Detect command repetition patterns as stagnation signal."""
    commands = [s.command for s in window if s.is_action and s.command is not None]

    if len(commands) < 2:
        return ABSTAIN

    if _has_consecutive_similar(commands, min_run=3, threshold=1.0):
        return STAGNATION

    if _has_consecutive_similar(commands, min_run=3, threshold=0.9):
        return STAGNATION

    if len(set(commands)) == len(commands):
        return PROGRESS

    return ABSTAIN


# --- Deprecated ---
def _parse_test_pass_rate(text: str) -> float | None:
    passed = 0
    failed = 0
    passed_lines = re.findall(r"PASSED\s+\S+", text)
    failed_lines = re.findall(r"FAILED\s+\S+", text)
    passed += len(passed_lines)
    failed += len(failed_lines)
    summary_passed = re.search(r"(\d+)\s+passed", text)
    summary_failed = re.search(r"(\d+)\s+failed", text)
    if summary_passed and passed == 0:
        passed = int(summary_passed.group(1))
    if summary_failed and failed == 0:
        failed = int(summary_failed.group(1))
    total = passed + failed
    if total == 0:
        return None
    return passed / total


def lf_test_pass_rate_transition_deprecated(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
    """LF2 (deprecated): Whether test pass rate is improving within the window."""
    test_runs = []
    for step in window:
        if not step.is_observation:
            continue
        if not step.has_test_output:
            continue
        rate = _parse_test_pass_rate(step.text)
        if rate is not None:
            test_runs.append(rate)
    if len(test_runs) < 2:
        return ABSTAIN
    last = test_runs[-1]
    second_last = test_runs[-2]
    if last > second_last:
        return PROGRESS
    return STAGNATION


def lf_outcome_backpropagation(window: list[Step], trajectory: Trajectory, window_position: dict) -> int:
    """LF3: Label last windows based on final trajectory outcome."""
    total_windows = window_position["total_windows"]
    window_idx = window_position["window_idx"]

    is_last_two = window_idx >= total_windows - 2

    if trajectory.exit_status in ("exit_context",):
        return STAGNATION

    if not is_last_two:
        return ABSTAIN

    if trajectory.target:
        return PROGRESS
    else:
        return STAGNATION


ALL_LFS = [
    ("file_diff_delta", lf_file_diff_delta),
    ("command_repetition", lf_command_repetition),
    ("outcome_backpropagation", lf_outcome_backpropagation),
]
