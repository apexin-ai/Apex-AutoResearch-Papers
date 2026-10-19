#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "configs" / "repositories.json"


def run(
    command: list[str],
    *,
    cwd: Path = ROOT,
    env: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, env=env, check=check, text=True)


def command_succeeds(
    command: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None
) -> bool:
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def git_output(repository: Path, *arguments: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repository), *arguments], text=True
    ).strip()


def clone_repository(
    url: str, destination: Path, revision: str | None, depth: int
) -> None:
    """Clone a repository, fetching only the pinned object when possible."""
    if revision is None:
        run(
            [
                "git",
                "clone",
                "--depth",
                str(depth),
                "--no-tags",
                url,
                str(destination),
            ]
        )
        return

    run(["git", "init", "--quiet", str(destination)])
    run(["git", "-C", str(destination), "remote", "add", "origin", url])
    fetched = command_succeeds(
        [
            "git",
            "-C",
            str(destination),
            "fetch",
            "--depth",
            str(depth),
            "--no-tags",
            "origin",
            revision,
        ]
    )
    if fetched:
        run(["git", "-C", str(destination), "checkout", "--quiet", "--detach", "FETCH_HEAD"])
        return

    # Some servers reject fetching an unadvertised SHA. The destination was
    # created by this function, so replacing only this incomplete clone is safe.
    print(f"exact shallow fetch unavailable; falling back to full clone: {url}")
    shutil.rmtree(destination)
    run(["git", "clone", "--no-checkout", url, str(destination)])
    run(["git", "-C", str(destination), "checkout", "--quiet", "--detach", revision])


def apply_patch_if_needed(repository: Path, patch_path: Path) -> None:
    forward = [
        "git",
        "-C",
        str(repository),
        "apply",
        "--unidiff-zero",
        "--check",
        str(patch_path),
    ]
    reverse = [
        "git",
        "-C",
        str(repository),
        "apply",
        "--unidiff-zero",
        "--reverse",
        "--check",
        str(patch_path),
    ]
    if command_succeeds(forward):
        run(forward[:-2] + [str(patch_path)])
        return
    if command_succeeds(reverse):
        return
    raise RuntimeError(
        f"patch is neither cleanly applicable nor already applied: {patch_path}"
    )


def verify_checkout(
    repository: Path,
    revision: str | None,
    patch_path: Path | None,
    expected_url: str | None = None,
) -> None:
    if not (repository / ".git").exists():
        raise RuntimeError(f"existing destination is not a Git repository: {repository}")

    if expected_url is not None:
        actual_url = git_output(repository, "remote", "get-url", "origin")
        if actual_url.rstrip("/") != expected_url.rstrip("/"):
            raise RuntimeError(
                f"origin mismatch for {repository}: expected {expected_url}, got {actual_url}"
            )

    if revision is not None:
        actual_revision = git_output(repository, "rev-parse", "HEAD")
        if actual_revision != revision:
            raise RuntimeError(
                f"revision mismatch for {repository}: expected {revision}, got {actual_revision}"
            )

    untracked = git_output(repository, "ls-files", "--others", "--exclude-standard")
    if untracked:
        raise RuntimeError(
            f"unexpected untracked files in {repository}: {untracked.splitlines()[0]}"
        )

    with tempfile.TemporaryDirectory(prefix="agenthpobench-index-") as directory:
        index_path = Path(directory) / "index"
        env = {**os.environ, "GIT_INDEX_FILE": str(index_path)}
        run(["git", "-C", str(repository), "read-tree", "HEAD"], env=env)
        if patch_path is not None:
            run(
                [
                    "git",
                    "-C",
                    str(repository),
                    "apply",
                    "--cached",
                    "--unidiff-zero",
                    str(patch_path),
                ],
                env=env,
            )
        matches_expected_tree = command_succeeds(
            ["git", "-C", str(repository), "diff", "--quiet"], env=env
        )
    if not matches_expected_tree:
        expected = "the pinned revision plus its compatibility patch" if patch_path else "the pinned revision"
        raise RuntimeError(
            f"tracked worktree changes in {repository} do not match {expected}"
        )


def prepare_repository(item: dict[str, Any], *, root: Path, depth: int) -> None:
    destination = root / item["path"]
    revision = item.get("revision")
    patch = item.get("patch")
    patch_path = root / patch if patch else None

    if destination.exists():
        print(f"verify existing: {destination.relative_to(root)}")
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        print(f"clone {item['task']}: {item['url']}")
        clone_repository(item["url"], destination, revision, depth)

    if patch_path is not None:
        print(f"verify patch: {patch_path.relative_to(root)}")
        apply_patch_if_needed(destination, patch_path)
    verify_checkout(destination, revision, patch_path, item["url"])
    print(f"verified: {destination.relative_to(root)}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Clone and verify AgentHPOBench upstream repositories."
    )
    parser.add_argument(
        "--task", action="append", default=[], help="Clone only this task id; repeat as needed."
    )
    parser.add_argument(
        "--depth", type=int, default=1, help="Initial fetch depth for every repository."
    )
    args = parser.parse_args()
    if args.depth < 1:
        parser.error("--depth must be at least 1")

    payload = json.loads(MANIFEST.read_text())
    selected = set(args.task)
    known_tasks = {item["task"] for item in payload["repositories"]}
    unknown_tasks = sorted(selected - known_tasks)
    if unknown_tasks:
        parser.error(f"unknown task id(s): {', '.join(unknown_tasks)}")

    for item in payload["repositories"]:
        if selected and item["task"] not in selected:
            continue
        prepare_repository(item, root=ROOT, depth=args.depth)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
