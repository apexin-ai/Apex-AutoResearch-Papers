"""BugsInPy dataset preparation for DTD experiments.

Provides checkout of buggy/fixed versions, test command extraction,
and a curated list of 45 candidate bug instances.

Dependencies: git (system), standard library.
"""
from __future__ import annotations

import logging
import os
import subprocess
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

BUGSINPY_REPO = "https://github.com/soarsmu/BugsInPy.git"


class BugsInPySetup:

    CANDIDATE_BUGS: List[Tuple[str, int, str]] = [
        # (project, bug_id, bug_characteristic)
        ("thefuck", 1, "multi-function call chain, rule matching logic"),
        ("thefuck", 2, "exception handling in shell command execution"),
        ("thefuck", 4, "string processing across helper functions"),
        ("black", 1, "AST traversal with recursive formatting"),
        ("black", 2, "multi-function string normalization"),
        ("cookiecutter", 1, "template rendering call chain"),
        ("cookiecutter", 2, "file I/O with exception handling"),
        ("cookiecutter", 3, "config parsing multi-step pipeline"),
        ("fastapi", 1, "request routing with dependency injection"),
        ("fastapi", 2, "response model validation chain"),
        ("fastapi", 3, "middleware exception propagation"),
        ("httpie", 1, "request building multi-function pipeline"),
        ("httpie", 2, "header parsing with edge cases"),
        ("luigi", 1, "task dependency resolution chain"),
        ("luigi", 2, "scheduler loop iteration bug"),
        ("pandas", 1, "DataFrame operation call chain"),
        ("pandas", 2, "indexing with type coercion across functions"),
        ("pandas", 3, "groupby aggregation pipeline"),
        ("rich", 1, "console rendering with style inheritance"),
        ("rich", 3, "table formatting recursive layout"),
        ("sanic", 1, "request handling middleware chain"),
        ("sanic", 2, "routing with exception fallback"),
        ("scrapy", 1, "spider callback chain processing"),
        ("scrapy", 2, "middleware pipeline with error handling"),
        ("tornado", 1, "async handler call chain"),
        ("tornado", 2, "IOLoop callback exception handling"),
        ("tqdm", 1, "progress bar update loop logic"),
        ("tqdm", 2, "format_meter multi-branch computation"),
        ("youtube-dl", 1, "extractor call chain with fallback"),
        ("youtube-dl", 2, "format selection multi-step pipeline"),
        # --- batch 2: 15 new candidates (deep call chain + loop logic) ---
        ("scrapy", 3, "redirect middleware URL scheme rewriting chain"),
        ("scrapy", 4, "contract errback callback chain exc_info ordering"),
        ("scrapy", 7, "form request URL extraction pipeline"),
        ("tornado", 4, "StaticFileHandler range request multi-branch processing"),
        ("tornado", 5, "PeriodicCallback timer update loop logic"),
        ("tornado", 7, "IOLoop run_in_executor future chaining"),
        ("luigi", 5, "task decorator inheritance chain (inherits/requires)"),
        ("luigi", 10, "worker pending task filtering in scheduler loop"),
        ("luigi", 14, "scheduler failure detection state machine"),
        ("youtube-dl", 5, "unified_timestamp multi-format date parsing pipeline"),
        ("youtube-dl", 10, "js_to_json regex substitution pipeline"),
        ("youtube-dl", 20, "HTML element attribute extraction iteration"),
        ("black", 5, "bracket split trailing comma detection loop"),
        ("black", 14, "future imports recursive AST child traversal"),
        ("fastapi", 5, "recursive model field cloning chain"),
    ]

    def __init__(self, workspace_dir: str = "./bugsinpy_workspace"):
        self.workspace_dir = os.path.abspath(workspace_dir)
        self.repo_dir = os.path.join(self.workspace_dir, "BugsInPy")

    def _ensure_repo(self):
        if os.path.isdir(os.path.join(self.repo_dir, ".git")):
            logger.info("BugsInPy repo already cloned at %s", self.repo_dir)
            return
        os.makedirs(self.workspace_dir, exist_ok=True)
        logger.info("Cloning BugsInPy repo...")
        subprocess.run(
            ["git", "clone", "--depth", "1", BUGSINPY_REPO, self.repo_dir],
            check=True,
            capture_output=True,
        )

    def setup_instance(self, project: str, bug_id: int) -> dict:
        self._ensure_repo()

        bug_dir = os.path.join(self.repo_dir, "projects", project, "bugs", str(bug_id))
        if not os.path.isdir(bug_dir):
            raise FileNotFoundError(f"Bug directory not found: {bug_dir}")

        bug_info = self._read_bug_info(bug_dir)
        test_command = bug_info.get("test_command", f"python -m pytest")
        issue_description = bug_info.get("issue_description", f"{project} bug #{bug_id}")

        work_dir = os.path.join(self.workspace_dir, "instances", f"{project}_{bug_id}")
        os.makedirs(work_dir, exist_ok=True)

        buggy_dir = os.path.join(work_dir, "buggy")
        if not os.path.isdir(buggy_dir):
            self._checkout_version(project, bug_id, "buggy", buggy_dir)

        return {
            "project": project,
            "bug_id": bug_id,
            "buggy_dir": buggy_dir,
            "test_command": test_command,
            "issue_description": issue_description,
            "bug_info": bug_info,
        }

    def setup_batch(self, instances: Optional[List[Tuple[str, int]]] = None) -> List[dict]:
        if instances is None:
            instances = [(p, bid) for p, bid, _ in self.CANDIDATE_BUGS]

        results = []
        for project, bug_id in instances:
            try:
                result = self.setup_instance(project, bug_id)
                results.append(result)
                logger.info("Prepared %s#%d", project, bug_id)
            except Exception as e:
                logger.error("Failed to prepare %s#%d: %s", project, bug_id, e)
        return results

    def get_buggy_code(self, instance: dict) -> str:
        bug_info = instance.get("bug_info", {})
        buggy_file = bug_info.get("buggy_file", "")
        if buggy_file:
            path = os.path.join(instance["buggy_dir"], buggy_file)
            if os.path.isfile(path):
                with open(path, "r") as f:
                    return f.read()
        return self._find_main_python_file(instance["buggy_dir"])

    def get_fixed_code(self, instance: dict) -> str:
        work_dir = os.path.dirname(instance["buggy_dir"])
        fixed_dir = os.path.join(work_dir, "fixed")
        if not os.path.isdir(fixed_dir):
            self._checkout_version(instance["project"], instance["bug_id"], "fixed", fixed_dir)

        bug_info = instance.get("bug_info", {})
        buggy_file = bug_info.get("buggy_file", "")
        if buggy_file:
            path = os.path.join(fixed_dir, buggy_file)
            if os.path.isfile(path):
                with open(path, "r") as f:
                    return f.read()
        return self._find_main_python_file(fixed_dir)

    def _read_bug_info(self, bug_dir: str) -> dict:
        info = {}
        info_file = os.path.join(bug_dir, "bug.info")
        if not os.path.isfile(info_file):
            return info

        with open(info_file, "r") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    info[key.strip().lower().replace(" ", "_")] = value.strip().strip('"')

        bug_patch = os.path.join(bug_dir, "bug_patch.txt")
        if os.path.isfile(bug_patch):
            with open(bug_patch, "r") as f:
                info["patch"] = f.read()

        return info

    def _checkout_version(self, project: str, bug_id: int, version: str, target_dir: str):
        project_dir = os.path.join(self.repo_dir, "projects", project)
        bug_dir = os.path.join(project_dir, "bugs", str(bug_id))

        bug_info = self._read_bug_info(bug_dir)
        repo_url = bug_info.get("github_url", "")
        if not repo_url:
            project_info_file = os.path.join(project_dir, "project.info")
            if os.path.isfile(project_info_file):
                with open(project_info_file, "r") as f:
                    for line in f:
                        if "github_url" in line.lower():
                            _, _, url = line.partition("=")
                            repo_url = url.strip().strip('"')
                            break

        if not repo_url:
            raise ValueError(f"Cannot find GitHub URL for {project}")

        commit_key = f"{version}_commit_id" if version == "buggy" else "fixed_commit_id"
        commit_id = bug_info.get(commit_key, "")
        if not commit_id:
            raise ValueError(f"No {version} commit ID found for {project}#{bug_id}")

        logger.info("Checking out %s version of %s#%d (commit %s)", version, project, bug_id, commit_id[:8])
        subprocess.run(["git", "clone", repo_url, target_dir], check=True, capture_output=True)
        subprocess.run(["git", "checkout", commit_id], check=True, capture_output=True, cwd=target_dir)

    def _find_main_python_file(self, directory: str) -> str:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".tox", "venv")]
            for f in sorted(files):
                if f.endswith(".py") and not f.startswith("test_") and f != "setup.py":
                    path = os.path.join(root, f)
                    with open(path, "r") as fh:
                        return fh.read()
        return ""


if __name__ == "__main__":
    print(f"BugsInPy candidate bugs: {len(BugsInPySetup.CANDIDATE_BUGS)}")
    for project, bug_id, desc in BugsInPySetup.CANDIDATE_BUGS:
        print(f"  {project}#{bug_id}: {desc}")

    print("\nTo prepare an instance:")
    print("  setup = BugsInPySetup('./workspace')")
    print("  instance = setup.setup_instance('thefuck', 1)")
