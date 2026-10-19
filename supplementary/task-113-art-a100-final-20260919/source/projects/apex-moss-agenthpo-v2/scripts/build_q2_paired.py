"""Build paired V0/V1 views of the frozen hidden-final validation tasks."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.import_bigcodebench_hard_canary import build_solution
from scripts.import_bigcodebench_hidden import (
    DATASET,
    DATASET_COMMIT,
    PARQUET_SHA256,
    SPLIT,
    build_hidden_test,
    build_visible_test,
    fetch_official_rows,
    run_pytest,
)

OUT = ROOT / "benchmarks" / "q2_paired"
BLOCKS = (
    ("tdd", "tddgen_hidden", "V1"),
    ("spec", "specgen_hidden", "V0"),
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def build_pair(
    row: dict, source_task: Path, source_level: str
) -> dict[str, object]:
    """Return paired files after proving the source matches the frozen dataset."""
    solution = (source_task / "solution.py").read_text()
    hidden = (source_task / "_hidden" / "test_hidden.py").read_text()
    source_visible = (source_task / "test_solution.py").read_text()

    expected_solution = build_solution(row)
    expected_hidden, hidden_names = build_hidden_test(row)
    if solution != expected_solution:
        raise ValueError(f"{row['task_id']}: frozen solution does not match dataset")
    if hidden != expected_hidden:
        raise ValueError(f"{row['task_id']}: frozen hidden test does not match dataset")

    views = {}
    for level in ("V0", "V1"):
        visible, visible_names = build_visible_test(row, level)
        views[level] = {
            "test_solution.py": visible,
            "visible_tests": visible_names,
        }
    if source_visible != views[source_level]["test_solution.py"]:
        raise ValueError(
            f"{row['task_id']}: source visible test does not match {source_level}"
        )
    return {
        "solution.py": solution,
        "_hidden/test_hidden.py": hidden,
        "hidden_tests": hidden_names,
        "views": views,
    }


def validate_pair(row: dict, pair: dict[str, object]) -> None:
    """Re-run the frozen offline quality gate without exposing tests to a model."""
    solution = pair["solution.py"]
    hidden = pair["_hidden/test_hidden.py"]
    views = pair["views"]
    assert isinstance(solution, str)
    assert isinstance(hidden, str)
    assert isinstance(views, dict)

    if run_pytest(solution, hidden).returncode == 0:
        raise ValueError(f"{row['task_id']}: stub unexpectedly passes hidden tests")
    oracle = build_solution(row, oracle=True)
    if run_pytest(oracle, hidden).returncode != 0:
        raise ValueError(f"{row['task_id']}: oracle fails hidden tests")
    for level in ("V0", "V1"):
        visible = views[level]["test_solution.py"]
        if run_pytest(oracle, visible).returncode != 0:
            raise ValueError(f"{row['task_id']}: oracle fails {level} visible test")


def _write_exact(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text() != content:
            raise ValueError(f"refusing to overwrite mismatched frozen file: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def build_benchmarks(
    *, root: Path = ROOT, rows: list[dict] | None = None, validate: bool = True
) -> dict:
    out = root / "benchmarks" / "q2_paired"
    row_map = {
        row["task_id"]: row for row in (rows if rows is not None else fetch_official_rows())
    }
    task_entries = []
    block_entries = []

    for block, family, source_level in BLOCKS:
        source_root = root / "benchmarks" / family
        source_manifest = json.loads((source_root / "_manifest.json").read_text())
        task_manifest = {
            item["task_id"]: item for item in source_manifest["tasks"]
            if item["split"] == "val"
        }
        task_ids = list(source_manifest["val"])
        block_entries.append({
            "block": block,
            "source_family": family,
            "source_level": source_level,
            "task_ids": task_ids,
        })
        for task_id in task_ids:
            if task_id not in row_map:
                raise ValueError(f"missing frozen dataset row: {task_id}")
            source_entry = task_manifest[task_id]
            source_task = source_root / "val" / source_entry["name"]
            pair = build_pair(row_map[task_id], source_task, source_level)
            if validate:
                validate_pair(row_map[task_id], pair)

            views = pair["views"]
            for level in ("V0", "V1"):
                target = out / f"{block}_val_{level.lower()}" / source_entry["name"]
                _write_exact(target / "solution.py", pair["solution.py"])
                _write_exact(
                    target / "test_solution.py",
                    views[level]["test_solution.py"],
                )
                _write_exact(
                    target / "_hidden" / "test_hidden.py",
                    pair["_hidden/test_hidden.py"],
                )

            task_entries.append({
                "pair_id": f"{block}:{task_id}",
                "block": block,
                "task_id": task_id,
                "name": source_entry["name"],
                "entry_point": source_entry["entry_point"],
                "source_family": family,
                "source_level": source_level,
                "visible_tests": {
                    level: views[level]["visible_tests"] for level in ("V0", "V1")
                },
                "hidden_tests": pair["hidden_tests"],
                "sha256": {
                    "solution.py": sha256_text(pair["solution.py"]),
                    "_hidden/test_hidden.py": sha256_text(
                        pair["_hidden/test_hidden.py"]
                    ),
                    "V0/test_solution.py": sha256_text(
                        views["V0"]["test_solution.py"]
                    ),
                    "V1/test_solution.py": sha256_text(
                        views["V1"]["test_solution.py"]
                    ),
                },
            })

    manifest = {
        "protocol": "q2-paired-feedback-confirmation",
        "dataset": DATASET,
        "split": SPLIT,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": PARQUET_SHA256,
        "selection": "all 20 frozen hidden-final validation tasks; no score filtering",
        "treatment": "V0 callable smoke versus V1 first behavior test only",
        "hidden_suite": "identical complete official suite within every pair",
        "blocks": block_entries,
        "tasks": task_entries,
    }
    manifest_text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    _write_exact(out / "_manifest.json", manifest_text)
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--no-validate", action="store_true",
        help="skip local oracle/stub pytest gates (tests only)",
    )
    args = parser.parse_args()
    manifest = build_benchmarks(validate=not args.no_validate)
    print(f"wrote {len(manifest['tasks'])} paired tasks to {OUT}")


if __name__ == "__main__":
    main()
