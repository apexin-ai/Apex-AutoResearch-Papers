from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.builder_memory import (
    BuilderMemoryConfig,
    CrossTaskMemoryRecord,
    CrossTaskMemoryStore,
)


def _general_rule(
    *,
    record_id: str = "rule-001",
    source_order: int = 1,
    rule: str = "When public feedback reports a contract error, repair the emit path first.",
) -> CrossTaskMemoryRecord:
    return CrossTaskMemoryRecord.create(
        record_id=record_id,
        rule=rule,
        source_benchmark="edgebench",
        source_instance_hash="a" * 64,
        source_lineage_hash="b" * 64,
        source_round=7,
        source_order=source_order,
        distiller_version="moss-memory-distiller-v1",
        sanitizer_version="moss-memory-sanitizer-v1",
    )


def test_instance_only_rejects_cross_task_records() -> None:
    with pytest.raises(ValueError, match="instance-only"):
        BuilderMemoryConfig(mode="instance_only", cross_task_records=(_general_rule(),))


def test_cross_task_online_accepts_only_sanitized_rules() -> None:
    record = _general_rule()
    config = BuilderMemoryConfig(
        mode="cross_task_online",
        cross_task_records=(record,),
    )

    payload = config.public_payload()

    assert payload["mode"] == "cross_task_online"
    assert payload["cross_task_records"] == [record.to_dict()]


@pytest.mark.parametrize(
    "rule",
    (
        "```json\n{\"schema_version\": 2}\n```",
        "Read C:\\private\\answer.txt before solving.",
        "Inspect ../other-instance/trace.json.",
        '{"schema_version":2,"nodes":[],"interface":{},"memory":{}}',
        "Reuse candidate answer: SECRET_OUTPUT",
        "Copy raw_trace and hidden_test output into the next prompt.",
        "Use private_evaluator feedback from task_id=ahc024.",
        "Reuse identifier " + "c" * 64 + " in a later instance.",
    ),
)
def test_record_sanitizer_rejects_cross_task_leakage(rule: str) -> None:
    with pytest.raises(ValueError, match="sanitized"):
        _general_rule(rule=rule)


def test_record_hash_binds_all_public_provenance() -> None:
    record = _general_rule()
    payload = record.to_dict()
    payload["source_round"] = 6

    with pytest.raises(ValueError, match="hash"):
        CrossTaskMemoryRecord.from_dict(payload)


def test_store_is_append_only_and_idempotent_for_the_same_record(tmp_path: Path) -> None:
    store = CrossTaskMemoryStore(tmp_path)
    record = _general_rule()

    first = store.append(record)
    second = store.append(record)

    assert first == second
    assert store.snapshot(before_order=2).records == (record,)

    conflicting = _general_rule(rule="Prefer a different generic workflow rule.")
    with pytest.raises(ValueError, match="append-only"):
        store.append(conflicting)


def test_open_existing_requires_an_existing_directory_without_creating_it(
    tmp_path: Path,
) -> None:
    missing = tmp_path / "missing-memory"

    with pytest.raises(ValueError, match="existing directory"):
        CrossTaskMemoryStore.open_existing(missing)

    assert not missing.exists()


def test_open_existing_rejects_a_file_root(tmp_path: Path) -> None:
    root = tmp_path / "memory-file"
    root.write_text("not a directory", encoding="utf-8")

    with pytest.raises(ValueError, match="directory"):
        CrossTaskMemoryStore.open_existing(root)


def test_open_existing_rejects_a_symlink_root(tmp_path: Path) -> None:
    real_root = tmp_path / "real-memory"
    real_root.mkdir()
    root = tmp_path / "memory-link"
    try:
        root.symlink_to(real_root, target_is_directory=True)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"directory symlinks unavailable: {exc}")

    with pytest.raises(ValueError, match="symlink"):
        CrossTaskMemoryStore.open_existing(root)


@pytest.mark.parametrize("storage_name", ("objects", "bindings"))
def test_open_existing_rejects_dangling_storage_symlink(
    tmp_path: Path, storage_name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "memory"
    root.mkdir()
    dangling = root / storage_name

    # Windows may disallow creating directory symlinks in an ordinary test
    # process, so explicitly exercise the same path predicate used by the
    # production check.
    def fake_is_symlink(path: Path) -> bool:
        return path == dangling

    monkeypatch.setattr(Path, "is_symlink", fake_is_symlink)

    with pytest.raises(ValueError, match="real directories"):
        CrossTaskMemoryStore.open_existing(root)


@pytest.mark.parametrize(
    "rule",
    (
        r"Read(C:\private\answer.txt)",
        "Read(/private/answer.txt)",
        "candidate-answer SECRET",
        "candidate：answer SECRET",
        "candidate(answer)",
        '{"candidate-answer":"SECRET"}',
        "task_id: ahc024",
        "instance_id: other-instance",
        "hidden-test output",
        "private(evaluator) feedback",
        '"trace": "raw output"',
        "ＥＶＡＬＵＡＴＯＲ\u3000feedback",
    ),
)
def test_record_sanitizer_rejects_sensitive_rule_variants(rule: str) -> None:
    with pytest.raises(ValueError, match="sanitized"):
        _general_rule(rule=rule)


@pytest.mark.parametrize(
    "rule",
    (
        "candіdate feedback",  # Cyrillic small i
        "candidatе feedback",  # Cyrillic small e
        "candıdate feedback",  # dotless i
    ),
)
def test_record_sanitizer_rejects_unicode_confusable_variants(rule: str) -> None:
    with pytest.raises(ValueError, match="sanitized"):
        _general_rule(rule=rule)


def test_open_existing_snapshot_is_read_only_and_does_not_create_storage(
    tmp_path: Path,
) -> None:
    root = tmp_path / "empty-memory"
    root.mkdir()

    store = CrossTaskMemoryStore.open_existing(root)

    assert store.snapshot(before_order=3).records == ()
    assert sorted(path.name for path in root.iterdir()) == []


def test_open_existing_cannot_be_used_to_append(tmp_path: Path) -> None:
    root = tmp_path / "memory"
    root.mkdir()
    store = CrossTaskMemoryStore.open_existing(root)

    with pytest.raises(ValueError, match="read-only"):
        store.append(_general_rule())


def test_append_publishes_only_a_complete_record_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    store = CrossTaskMemoryStore(tmp_path / "memory")
    record = _general_rule()
    published: list[dict[str, object]] = []
    real_link = os.link

    def observe_publish(source: str | bytes, destination: str | bytes, *args: object, **kwargs: object) -> None:
        destination_path = Path(destination)
        assert not destination_path.exists()
        published.append(json.loads(Path(source).read_text(encoding="utf-8")))
        real_link(source, destination, *args, **kwargs)

    monkeypatch.setattr(os, "link", observe_publish)
    store.append(record)

    assert published == [
        record.to_dict(),
        {"record_id": record.record_id, "record_sha256": record.record_sha256},
    ]
    object_files = list((tmp_path / "memory" / "objects").glob("*.json"))
    assert len(object_files) == 1
    assert json.loads(object_files[0].read_text(encoding="utf-8")) == record.to_dict()


def test_online_snapshot_cannot_read_current_or_future_instance_records(
    tmp_path: Path,
) -> None:
    store = CrossTaskMemoryStore(tmp_path)
    earlier = _general_rule(record_id="rule-001", source_order=1)
    current = _general_rule(record_id="rule-003", source_order=3)
    future = _general_rule(record_id="rule-004", source_order=4)
    for record in (future, current, earlier):
        store.append(record)

    snapshot = store.snapshot(before_order=3)

    assert snapshot.records == (earlier,)
    assert all(record.source_order < 3 for record in snapshot.records)
    payload = snapshot.public_payload()
    assert payload["before_order"] == 3
    assert payload["records"] == [earlier.to_dict()]
    assert payload["snapshot_sha256"] == snapshot.sha256
    assert json.dumps(payload, sort_keys=True)


def test_snapshot_hash_changes_with_cutoff_and_visible_records(tmp_path: Path) -> None:
    store = CrossTaskMemoryStore(tmp_path)
    store.append(_general_rule(record_id="rule-001", source_order=1))
    first = store.snapshot(before_order=2)
    later = store.snapshot(before_order=3)

    assert first.records == later.records
    assert first.sha256 != later.sha256


def test_config_from_snapshot_preserves_snapshot_identity_and_receipt_provenance(
    tmp_path: Path,
) -> None:
    store = CrossTaskMemoryStore(tmp_path)
    record = store.append(_general_rule(record_id="rule-001", source_order=1))
    snapshot = store.snapshot(before_order=3)

    config = BuilderMemoryConfig.from_snapshot(snapshot)

    assert config.public_payload()["snapshot_sha256"] == snapshot.sha256
    assert config.receipt_payload() == {
        "mode": "cross_task_online",
        "snapshot_sha256": snapshot.sha256,
        "record_count": 1,
        "provenance": [
            {
                "record_id": record.record_id,
                "record_sha256": record.record_sha256,
                "source_benchmark": record.source_benchmark,
                "source_instance_hash": record.source_instance_hash,
                "source_lineage_hash": record.source_lineage_hash,
                "source_round": record.source_round,
                "source_order": record.source_order,
                "distiller_version": record.distiller_version,
                "sanitizer_version": record.sanitizer_version,
            }
        ],
    }
    assert record.rule not in json.dumps(config.receipt_payload(), sort_keys=True)


def test_instance_only_receipt_is_explicit_and_empty() -> None:
    config = BuilderMemoryConfig()

    assert config.public_payload() == {
        "mode": "instance_only",
        "cross_task_records": [],
        "snapshot_sha256": None,
    }
    assert config.receipt_payload() == {
        "mode": "instance_only",
        "snapshot_sha256": None,
        "record_count": 0,
        "provenance": [],
    }
