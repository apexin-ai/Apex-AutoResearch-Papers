"""Build a fresh V1 external-validation pool for Q1."""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.metadata
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.import_bigcodebench_hidden import (  # noqa: E402
    DATASET,
    DATASET_COMMIT,
    PARQUET_SHA256,
    SIDE_EFFECT_BLACKLIST,
    SPLIT,
    fetch_official_rows,
    qualify_formal_rows,
)

OUT = ROOT / "benchmarks" / "q1_external"
EXPANDED_IMPORTS = {"matplotlib", "scipy", "sklearn", "seaborn"}
PINNED_PACKAGES = {
    "matplotlib": "3.9.2",
    "scipy": "1.14.1",
    "scikit-learn": "1.5.2",
    "seaborn": "0.13.2",
}
CANARY_SIZE = 4
VAL_SIZE = 12
os.environ.setdefault("MPLBACKEND", "Agg")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _libs(row: dict) -> set[str]:
    value = row["libs"]
    return set(ast.literal_eval(value) if isinstance(value, str) else value)


def select_candidates(
    rows: list[dict],
    *,
    old_allowed: set[str],
    prior_ids: set[str],
) -> tuple[list[dict], list[dict]]:
    """Apply the frozen dependency/side-effect/prior-exposure filter."""
    allowed = old_allowed | EXPANDED_IMPORTS
    eligible = []
    excluded = []
    for row in rows:
        task_id = row["task_id"]
        libs = _libs(row)
        if task_id in prior_ids:
            excluded.append({"task_id": task_id, "reason": "prior_model_pool"})
        elif libs & SIDE_EFFECT_BLACKLIST:
            excluded.append({
                "task_id": task_id,
                "reason": "side_effect_blacklist:"
                + ",".join(sorted(libs & SIDE_EFFECT_BLACKLIST)),
            })
        elif not libs <= allowed:
            excluded.append({
                "task_id": task_id,
                "reason": "outside_frozen_imports:"
                + ",".join(sorted(libs - allowed)),
            })
        else:
            eligible.append(row)
    return eligible, excluded


def frozen_order(rows: list[dict]) -> list[dict]:
    return sorted(
        rows,
        key=lambda row: hashlib.sha256(row["task_id"].encode()).hexdigest(),
    )


def _write_exact(path: Path, text: str) -> None:
    if path.exists():
        if path.read_text() != text:
            raise ValueError(f"refusing to overwrite mismatched frozen file: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def build_external_pool(
    *, root: Path = ROOT, rows: list[dict] | None = None
) -> dict:
    source_manifest = json.loads(
        (root / "benchmarks" / "tddgen_hidden" / "_manifest.json").read_text()
    )
    old_allowed = set(source_manifest["environment"]["allowed_libs"])
    prior_ids = (
        set(source_manifest["qualified_order"])
        | set(source_manifest["canary_excluded"])
    )
    all_rows = rows if rows is not None else fetch_official_rows()
    candidates, filter_excluded = select_candidates(
        all_rows,
        old_allowed=old_allowed,
        prior_ids=prior_ids,
    )
    qualified, artifacts, quality_excluded = qualify_formal_rows(candidates, "V1")
    ordered = frozen_order(qualified)
    needed = CANARY_SIZE + VAL_SIZE
    if len(ordered) < needed:
        raise ValueError(
            f"fresh qualified pool has {len(ordered)} tasks; need {needed}"
        )
    selected = ordered[:needed]

    task_entries = []
    out = root / "benchmarks" / "q1_external"
    for index, row in enumerate(selected):
        split = "canary" if index < CANARY_SIZE else "val"
        task_id = row["task_id"]
        data = artifacts[task_id]
        name = task_id.replace("/", "_").lower()
        task_dir = out / split / name
        _write_exact(task_dir / "solution.py", data["solution"])
        _write_exact(task_dir / "test_solution.py", data["visible"])
        _write_exact(
            task_dir / "_hidden" / "test_hidden.py",
            data["hidden"],
        )
        task_entries.append({
            "task_id": task_id,
            "name": name,
            "split": split,
            "entry_point": row["entry_point"],
            "score": row["score"],
            "libs": sorted(_libs(row)),
            "visible_tests": data["visible_tests"],
            "hidden_tests": data["hidden_tests"],
            "sha256": {
                "solution.py": _sha(data["solution"]),
                "test_solution.py": _sha(data["visible"]),
                "_hidden/test_hidden.py": _sha(data["hidden"]),
            },
        })

    package_versions = {
        package: importlib.metadata.version(package)
        for package in PINNED_PACKAGES
    }
    if package_versions != PINNED_PACKAGES:
        raise ValueError(
            f"expanded dependency mismatch: {package_versions}"
        )
    allowed = sorted(old_allowed | EXPANDED_IMPORTS)
    manifest = {
        "protocol": "q1-independent-lineage-external-validation",
        "dataset": DATASET,
        "split": SPLIT,
        "dataset_commit": DATASET_COMMIT,
        "dataset_parquet_sha256": PARQUET_SHA256,
        "visibility_level": "V1",
        "visible_behavior_tests": 1,
        "hidden_suite": "complete official suite",
        "selection": (
            "exclude every prior model pool; frozen import subset; offline V1 "
            "quality gate; sha256(task_id) ascending; first 4 canary, next 12 val"
        ),
        "prior_ids_sha256": _sha("\n".join(sorted(prior_ids)) + "\n"),
        "expanded_imports": sorted(EXPANDED_IMPORTS),
        "pinned_packages": package_versions,
        "mplbackend": os.environ["MPLBACKEND"],
        "allowed_libs_sha256": _sha("\n".join(allowed) + "\n"),
        "filter_excluded": filter_excluded,
        "quality_excluded": quality_excluded,
        "qualified_order": [row["task_id"] for row in ordered],
        "qualified_order_sha256": _sha(
            "\n".join(row["task_id"] for row in ordered) + "\n"
        ),
        "canary": [row["task_id"] for row in selected[:CANARY_SIZE]],
        "val": [row["task_id"] for row in selected[CANARY_SIZE:needed]],
        "reserve": [row["task_id"] for row in ordered[needed:]],
        "tasks": task_entries,
    }
    _write_exact(
        out / "_manifest.json",
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    manifest = build_external_pool()
    print(
        f"wrote Q1 external pool: {len(manifest['canary'])} canary, "
        f"{len(manifest['val'])} val, {len(manifest['reserve'])} reserve"
    )


if __name__ == "__main__":
    main()
