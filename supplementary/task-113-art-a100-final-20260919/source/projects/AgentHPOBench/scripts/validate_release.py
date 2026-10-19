#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_CONFIG = ROOT / "configs" / "tasks.json"
REPOSITORY_CONFIG = ROOT / "configs" / "repositories.json"
TEXT_SUFFIXES = {
    ".cfg", ".csv", ".env", ".ini", ".json", ".md", ".patch", ".py", ".sh", ".tex", ".toml", ".txt", ".yaml", ".yml"
}
BLOCKED_PATTERNS = {
    "private Qizhi path": re.compile(r"/inspire/(?:ssd|hdd)/project/"),
    "private user path": re.compile(r"/Users/[^/]+/"),
    "legacy secret directory": re.compile(r"\.secrets/"),
    "private project account": re.compile(r"huaitianyu-\d+"),
}
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[opsu]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def release_files() -> list[Path]:
    """Return exactly the files Git would consider for the release."""
    try:
        output = subprocess.check_output(
            [
                "git",
                "-C",
                str(ROOT),
                "ls-files",
                "-z",
                "--cached",
                "--others",
                "--exclude-standard",
            ]
        )
    except (OSError, subprocess.CalledProcessError):
        return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]

    paths = []
    for relative in output.decode("utf-8", errors="surrogateescape").split("\0"):
        if relative:
            paths.append(ROOT / relative)
    return paths


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    task_payload = load_json(TASK_CONFIG)
    tasks = task_payload["tasks"]
    task_ids = [item["id"] for item in tasks]
    if len(tasks) != 30 or len(set(task_ids)) != 30:
        errors.append(f"configs/tasks.json must contain 30 unique tasks, found {len(tasks)}")
    if [item["index"] for item in tasks] != list(range(1, 31)):
        errors.append("task indexes must be contiguous from 1 to 30")
    if sum(bool(item["ray"]) for item in tasks) != 4:
        errors.append("exactly four tasks must be marked as Ray tasks")

    for task_id in task_ids:
        for overlay in (ROOT / "tasks" / "main", ROOT / "tasks" / "ablations" / "no_feedback"):
            task_dir = overlay / task_id
            if not task_dir.is_dir():
                errors.append(f"missing task directory: {task_dir.relative_to(ROOT)}")
                continue
            baseline = task_dir / "baseline.json"
            if not baseline.is_file():
                errors.append(f"missing baseline.json: {baseline.relative_to(ROOT)}")
            else:
                try:
                    load_json(baseline)
                except Exception as exc:
                    errors.append(f"invalid JSON {baseline.relative_to(ROOT)}: {exc}")

    repository_payload = load_json(REPOSITORY_CONFIG)
    repositories = repository_payload["repositories"]
    repository_tasks = [item["task"] for item in repositories]
    if set(repository_tasks) != set(task_ids) or len(repository_tasks) != 30:
        errors.append("configs/repositories.json must map each task exactly once")
    unpinned = [item["task"] for item in repositories if not item.get("revision")]
    if unpinned:
        warnings.append(f"{len(unpinned)} upstream repositories are not commit-pinned")
    for item in repositories:
        revision = item.get("revision")
        if revision and not re.fullmatch(r"[0-9a-f]{40}", revision):
            errors.append(f"invalid repository revision for {item['task']}: {revision}")
        patch = item.get("patch")
        if not patch:
            continue
        patch_path = (ROOT / patch).resolve()
        try:
            patch_path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"repository patch escapes release root for {item['task']}: {patch}")
            continue
        if not patch_path.is_file():
            errors.append(f"missing repository patch for {item['task']}: {patch}")
        elif patch_path.suffix != ".patch":
            errors.append(f"repository patch must use .patch suffix for {item['task']}: {patch}")

    for path in release_files():
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if path.stat().st_size > 100 * 1024 * 1024:
            errors.append(f"file exceeds 100 MiB: {relative}")
        if relative == Path("scripts/validate_release.py") or path.name == ".gitignore":
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(errors="replace")
        except OSError as exc:
            errors.append(f"cannot read {relative}: {exc}")
            continue
        for label, pattern in BLOCKED_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label} in {relative}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label} in {relative}")

    print(f"tasks: {len(tasks)}")
    print(f"repositories: {len(repositories)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("release validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
