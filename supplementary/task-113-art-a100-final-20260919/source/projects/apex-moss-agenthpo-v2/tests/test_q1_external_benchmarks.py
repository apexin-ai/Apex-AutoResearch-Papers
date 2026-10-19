"""Structural regression for the frozen Q1 external pool."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BENCH = ROOT / "benchmarks" / "q1_external"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_q1_external_pool_is_fresh_and_has_frozen_sizes():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    old = json.loads(
        (ROOT / "benchmarks" / "tddgen_hidden" / "_manifest.json").read_text()
    )
    prior = set(old["qualified_order"]) | set(old["canary_excluded"])

    assert len(manifest["canary"]) == 4
    assert len(manifest["val"]) == 12
    assert not (set(manifest["canary"]) | set(manifest["val"])) & prior
    assert manifest["pinned_packages"] == {
        "matplotlib": "3.9.2",
        "scipy": "1.14.1",
        "scikit-learn": "1.5.2",
        "seaborn": "0.13.2",
    }
    assert manifest["mplbackend"] == "Agg"


def test_q1_external_files_match_manifest_and_have_no_extras():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    for task in manifest["tasks"]:
        root = BENCH / task["split"] / task["name"]
        files = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file()
        }
        assert files == {
            "solution.py",
            "test_solution.py",
            "_hidden/test_hidden.py",
        }
        for relative, digest in task["sha256"].items():
            assert _sha(root / relative) == digest


def test_q1_external_selection_is_sha256_ordered():
    manifest = json.loads((BENCH / "_manifest.json").read_text())
    chosen = manifest["canary"] + manifest["val"]
    expected = sorted(
        manifest["qualified_order"],
        key=lambda task_id: hashlib.sha256(task_id.encode()).hexdigest(),
    )
    assert manifest["qualified_order"] == expected
    assert chosen == expected[:16]
