"""Offline contracts for the frozen three-tier qualification protocol."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import pytest

from scripts import three_tier_runner as runner


def _task(root: Path, split: str, name: str) -> Path:
    task = root / split / name
    (task / "_hidden").mkdir(parents=True)
    (task / "solution.py").write_text("def shared():\n    pass\n")
    (task / "test_solution.py").write_text("from solution import shared\n")
    (task / "_hidden" / "test_hidden.py").write_text("from solution import shared\n")
    return task


def test_selector_uses_integer_strict_gain_and_fixed_validation_tolerance():
    assert runner.accept_selector(
        candidate_train=9, parent_train=8, candidate_validation=11,
        seed_validation=12, parent_validation=12,
    )
    assert not runner.accept_selector(
        candidate_train=8, parent_train=8, candidate_validation=20,
        seed_validation=12, parent_validation=12,
    )
    assert not runner.accept_selector(
        candidate_train=9, parent_train=8, candidate_validation=10,
        seed_validation=12, parent_validation=12,
    )


def test_formal_gates_use_exact_fraction_and_repeat_variance():
    decision = runner.pretest_gate(
        seed_train=(8, 8, 8), final_train=(11, 11, 11),
        seed_validation=(10, 10, 10), final_validation=(9, 9, 9),
    )
    assert decision.train_gain == Fraction(3, 16)
    assert decision.validation_gain == Fraction(-1, 20)
    assert decision.passed

    noisy = runner.pretest_gate(
        seed_train=(8, 8, 8), final_train=(16, 8, 8),
        seed_validation=(10, 10, 10), final_validation=(10, 10, 10),
    )
    assert not noisy.passed
    assert noisy.reason == "training_repeat_variation"


def test_instance_linter_normalizes_and_rejects_tagged_id_or_unique_symbol():
    linter = runner.InstanceLinter(
        task_ids=("BigCodeBench/341",),
        basenames=("bigcodebench_341",), unique_symbols=("only_here",),
    )
    assert linter.match("# BIGCODEBENCH／341\n")
    assert linter.match("# task #341\n")
    assert linter.match("def only_here():\n    pass\n")
    assert not linter.match("def shared_helper():\n    pass\n")


def test_protocol_builder_copies_only_allowed_files_and_has_disjoint_pools(tmp_path):
    source = tmp_path / "source"
    for split, names in (("train", ("train_a",)), ("validation", ("val_a",)), ("test", ("test_a",))):
        for name in names:
            _task(source, split, name)
    artifact = tmp_path / "persistent-artifacts"
    manifest = runner.build_protocol_snapshot(
        source_root=source,
        pools={"training": ("train_a",), "validation": ("val_a",), "test": ("test_a",)},
        artifact_root=artifact,
        experiment_id="offline-contract",
        seed_bytes=b"seed",
    )
    assert manifest["pools"]["test"]["task_ids"] == ["test_a"]
    assert manifest["pools"]["test"]["entries"][0]["basename"] == "test_a"
    assert manifest["pools"]["test"]["report_block_a"] == ["test_a"]
    assert (artifact / "offline-contract" / "snapshot" / "test" / "test_a" / "_hidden" / "test_hidden.py").exists()
    verified = runner.verify_protocol_snapshot(
        artifact / "offline-contract" / "protocol_manifest.json"
    )
    assert verified["manifest_digest"] == manifest["manifest_digest"]

    with pytest.raises(runner.ProtocolError, match="disjoint"):
        runner.build_protocol_snapshot(
            source_root=source,
            pools={"training": ("train_a",), "validation": ("train_a",), "test": ("test_a",)},
            artifact_root=tmp_path / "other-artifacts",
            experiment_id="overlap",
            seed_bytes=b"seed",
        )


def test_real_pool_builder_uses_all_q1_and_q2_roles_without_mutating_sources(
    monkeypatch, tmp_path
):
    root = tmp_path / "repo"
    q1 = root / "benchmarks" / "q1_external"
    q2 = root / "benchmarks" / "q2_paired"
    for split, name in (("canary", "q1a"), ("val", "q1b")):
        _task(q1, split, name)
    _task(q2, "tdd_val_v1", "q2a")
    _task(q2, "spec_val_v1", "q2b")
    (q1 / "_manifest.json").write_text(json.dumps({
        "canary": ["Q1/A"], "val": ["Q1/B"], "reserve": ["Q1/C"],
        "tasks": [
            {"task_id": "Q1/A", "name": "q1a", "split": "canary"},
            {"task_id": "Q1/B", "name": "q1b", "split": "val"},
        ],
    }))
    (q2 / "_manifest.json").write_text(json.dumps({"tasks": [
        {"task_id": "Q2/A", "name": "q2a", "block": "tdd"},
        {"task_id": "Q2/B", "name": "q2b", "block": "spec"},
    ]}))
    reserve = {
        "Q1/C": {
            "solution": "def shared():\n    return 1\n",
            "visible": "from solution import shared\n",
            "hidden": "from solution import shared\n",
        },
    }
    monkeypatch.setattr(runner, "TRAIN_SIZE", 2)
    monkeypatch.setattr(runner, "VALIDATION_SIZE", 2)
    monkeypatch.setattr(runner, "TEST_SIZE", 1)
    result = runner.build_real_pool_snapshot(
        repo_root=root, artifact_root=tmp_path / "artifacts",
        experiment_id="real-build", seed_bytes=b"seed", reserve_artifacts=reserve,
    )
    assert result["pools"]["training"]["task_ids"] == ["Q1/A", "Q1/B"]
    assert result["pools"]["validation"]["task_ids"] == ["Q2/A", "Q2/B"]
    assert result["pools"]["test"]["task_ids"] == ["Q1/C"]
    assert (q1 / "canary" / "q1a" / "solution.py").read_text() == "def shared():\n    pass\n"


def test_proposer_payload_cannot_contain_private_selector_or_test_data(tmp_path):
    visible = tmp_path / "visible"
    visible.mkdir()
    (visible / "round-1.json").write_text(json.dumps({"train": 8, "trace": "safe"}))
    payload = runner.build_proposer_payload(
        parent_source="MODEL = 'claude-haiku-4-5'",
        visible_artifacts=(visible / "round-1.json",),
        family_description="family",
    )
    text = json.dumps(payload)
    assert "safe" in text
    assert "validation" not in text.lower()
    with pytest.raises(runner.ProtocolError, match="private"):
        runner.build_proposer_payload(
            parent_source="x", visible_artifacts=(tmp_path / "private" / "x.json",),
            family_description="family",
        )


def test_test_matrix_cannot_unseal_until_registry_and_never_retries_started(tmp_path):
    scheduler = runner.TestMatrix(
        root=tmp_path, matrix_id="m", jobs=("b", "a"), max_in_flight=3,
    )
    with pytest.raises(runner.ProtocolError, match="registry"):
        scheduler.unseal(registry_digest=None)
    scheduler.unseal(registry_digest="frozen")
    assert scheduler.claim() == "a"
    scheduler.mark_lost("a")
    assert scheduler.state()["status"] == "aborted_incomplete"
    assert scheduler.claim() is None
