from pathlib import Path

import pytest

from optimization_lab.harness_evolution import (
    HarnessArchive,
    HarnessVersion,
    InvalidHarness,
)


VALID_HARNESS = """# Task-specialist Harness

1. Read the task card and this lineage's feedback.
2. Preserve correctness before testing one focused performance change.
3. Keep the evaluator, model, GPU, and budget frozen.
"""


def test_harness_archive_is_immutable_and_parented(tmp_path: Path) -> None:
    archive = HarnessArchive(tmp_path / "lineage")
    seed = HarnessVersion.from_text("v001", VALID_HARNESS, parent_version_id=None)
    archive.store_seed(VALID_HARNESS, expected_sha256=seed.sha256)
    revised = HarnessVersion.from_text(
        "v002",
        VALID_HARNESS + "4. Compare against the historical best.\n",
        parent_version_id="v001",
    )

    archive.store_generated(revised, raw_response=revised.text, prompt_sha256="a" * 64)

    assert archive.load("v001") == seed
    assert archive.load("v002") == revised
    (tmp_path / "lineage/harnesses/v002.md").write_text(
        VALID_HARNESS, encoding="utf-8"
    )
    with pytest.raises(ValueError, match="changed"):
        archive.load("v002")


def test_harness_rejects_absolute_private_paths() -> None:
    with pytest.raises(InvalidHarness, match="absolute paths"):
        HarnessVersion.from_text(
            "v002",
            VALID_HARNESS + "Read /private/evaluator/raw.log before deciding.\n",
            parent_version_id="v001",
        )
