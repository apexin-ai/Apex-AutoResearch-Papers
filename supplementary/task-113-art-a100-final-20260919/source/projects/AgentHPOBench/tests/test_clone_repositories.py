from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "clone_repositories", ROOT / "scripts" / "clone_repositories.py"
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def git(repository: Path, *arguments: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repository), *arguments], text=True
    ).strip()


class CloneRepositoriesTests(unittest.TestCase):
    def create_upstream(self, root: Path) -> tuple[Path, str, Path]:
        upstream = root / "upstream"
        upstream.mkdir()
        subprocess.run(["git", "init", "--quiet"], cwd=upstream, check=True)
        subprocess.run(
            ["git", "config", "user.email", "tests@example.com"],
            cwd=upstream,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "AgentHPOBench Tests"],
            cwd=upstream,
            check=True,
        )
        source = upstream / "config.py"
        source.write_text("WINDOWS = [2]\n")
        subprocess.run(["git", "add", "config.py"], cwd=upstream, check=True)
        subprocess.run(
            ["git", "commit", "--quiet", "-m", "initial"],
            cwd=upstream,
            check=True,
        )
        revision = git(upstream, "rev-parse", "HEAD")
        source.write_text("WINDOWS = [2, 3]\n")
        patch_path = root / "compatibility.patch"
        patch_path.write_text(git(upstream, "diff", "--unified=0") + "\n")
        subprocess.run(
            ["git", "checkout", "--quiet", "--", "config.py"],
            cwd=upstream,
            check=True,
        )
        return upstream, revision, patch_path

    def test_prepares_and_reverifies_exact_patched_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            upstream, revision, patch_path = self.create_upstream(root)
            item = {
                "task": "example",
                "url": str(upstream),
                "path": "repositories/example",
                "revision": revision,
                "patch": patch_path.name,
            }
            MODULE.prepare_repository(item, root=root, depth=1)
            destination = root / item["path"]
            self.assertEqual(git(destination, "rev-parse", "HEAD"), revision)
            self.assertEqual(
                (destination / "config.py").read_text(), "WINDOWS = [2, 3]\n"
            )

            # A second invocation verifies instead of silently skipping or
            # attempting to apply the same patch twice.
            MODULE.prepare_repository(item, root=root, depth=1)

    def test_rejects_revision_mismatch_and_unexpected_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            upstream, revision, _ = self.create_upstream(root)
            destination = root / "repositories" / "example"
            MODULE.clone_repository(str(upstream), destination, revision, depth=1)

            with self.assertRaisesRegex(RuntimeError, "origin mismatch"):
                MODULE.verify_checkout(
                    destination, revision, None, "https://example.com/wrong.git"
                )

            with self.assertRaisesRegex(RuntimeError, "revision mismatch"):
                MODULE.verify_checkout(destination, "0" * 40, None)

            (destination / "config.py").write_text("WINDOWS = [99]\n")
            with self.assertRaisesRegex(RuntimeError, "tracked worktree changes"):
                MODULE.verify_checkout(destination, revision, None)

            subprocess.run(
                ["git", "checkout", "--quiet", "--", "config.py"],
                cwd=destination,
                check=True,
            )
            (destination / "unexpected.txt").write_text("unexpected\n")
            with self.assertRaisesRegex(RuntimeError, "unexpected untracked files"):
                MODULE.verify_checkout(destination, revision, None)


if __name__ == "__main__":
    unittest.main()
