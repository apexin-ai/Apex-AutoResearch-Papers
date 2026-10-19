"""Structural regression for the frozen Q2 paired benchmark."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmarks" / "q2_paired"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_q2_pairs_change_only_the_visible_test():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    assert len(manifest["tasks"]) == 20
    assert {task["block"] for task in manifest["tasks"]} == {"tdd", "spec"}

    for task in manifest["tasks"]:
        name = task["name"]
        block = task["block"]
        v0 = BENCH / f"{block}_val_v0" / name
        v1 = BENCH / f"{block}_val_v1" / name
        assert (v0 / "solution.py").read_bytes() == (v1 / "solution.py").read_bytes()
        assert (
            (v0 / "_hidden" / "test_hidden.py").read_bytes()
            == (v1 / "_hidden" / "test_hidden.py").read_bytes()
        )
        assert (v0 / "test_solution.py").read_bytes() != (
            v1 / "test_solution.py"
        ).read_bytes()
        assert _sha(v0 / "solution.py") == task["sha256"]["solution.py"]
        assert (
            _sha(v0 / "_hidden" / "test_hidden.py")
            == task["sha256"]["_hidden/test_hidden.py"]
        )
        assert (
            _sha(v0 / "test_solution.py")
            == task["sha256"]["V0/test_solution.py"]
        )
        assert (
            _sha(v1 / "test_solution.py")
            == task["sha256"]["V1/test_solution.py"]
        )


def test_q2_reused_views_are_byte_identical_to_old_formal_tasks():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    for task in manifest["tasks"]:
        old_family = ROOT / "benchmarks" / task["source_family"] / "val" / task["name"]
        old_level = task["source_level"].lower()
        paired = BENCH / f"{task['block']}_val_{old_level}" / task["name"]
        for relative in (
            Path("solution.py"),
            Path("test_solution.py"),
            Path("_hidden/test_hidden.py"),
        ):
            assert (old_family / relative).read_bytes() == (paired / relative).read_bytes()


def test_q2_pair_directories_have_only_frozen_task_files():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    expected_by_block = {
        block: {task["name"] for task in manifest["tasks"] if task["block"] == block}
        for block in ("tdd", "spec")
    }
    for block in ("tdd", "spec"):
        for level in ("v0", "v1"):
            split = BENCH / f"{block}_val_{level}"
            assert {path.name for path in split.iterdir()} == expected_by_block[block]
            for task in split.iterdir():
                files = {
                    path.relative_to(task).as_posix()
                    for path in task.rglob("*")
                    if path.is_file()
                }
                assert files == {
                    "solution.py",
                    "test_solution.py",
                    "_hidden/test_hidden.py",
                }
