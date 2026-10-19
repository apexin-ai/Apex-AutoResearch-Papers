from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.learning import (
    BuilderCheckpointArchive,
    ContinualUpdater,
    ExperienceBankArchive,
    ExperienceBankSnapshot,
    SealedInstanceTrajectory,
    parse_distillation_records,
)
from optimization_lab.harness_builder.schema import PilotManifest
from optimization_lab.harness_builder.stream import ARMS, PrequentialState, build_stream


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"


def _record(
    *,
    record_id: str = "record-001",
    source: str = "kernelbenchx:task-001",
    event_id: str = "event-001",
) -> dict[str, object]:
    return {
        "record_id": record_id,
        "source_instance_id": source,
        "builder_version": "builder-v001",
        "instance_descriptor": ["quantized", "reduction"],
        "initial_harness_structure": ["task_analyst", "generator", "verifier"],
        "evolution_rule": "discipline",
        "trigger_evidence": ["correct incumbent", "flat score"],
        "outcome_delta": 0.03,
        "correctness": True,
        "resource_cost": {"model_calls": 2.0, "evaluator_seconds": 12.5},
        "counterexamples": ["The gain did not transfer to a memory-bound shape."],
        "scope": "single_instance_observation",
        "provenance_event_ids": [event_id],
        "sealed": True,
    }


def _sealed_trajectory(instance_id: str) -> SealedInstanceTrajectory:
    return SealedInstanceTrajectory(
        instance_id=instance_id,
        suite=instance_id.split(":", 1)[0],
        builder_checkpoint_sha256="1" * 64,
        arm_event_ids={arm: (f"{arm}-sealed",) for arm in ARMS},
        public_summary={
            arm: {
                "initial_score": 1.0,
                "final_best": 1.1,
                "rules": ["discipline"],
            }
            for arm in ARMS
        },
        sealed=True,
    )


def test_experience_bank_is_content_addressed_and_append_only(tmp_path: Path) -> None:
    archive = ExperienceBankArchive(tmp_path / "banks")
    initial = ExperienceBankSnapshot.create(
        bank_id="bank-v1", parent_sha256=None, records=()
    )
    assert archive.store(initial) == archive.store(initial)
    assert (tmp_path / "banks" / f"{initial.sha256}.json").is_file()

    record = ExperienceRecord.from_dict(_record())
    updated = initial.extend((record,), bank_id="bank-v2")
    archive.store(updated)
    assert updated.parent_sha256 == initial.sha256
    assert updated.sha256 != initial.sha256

    with pytest.raises(ValueError, match="record id"):
        updated.extend(
            (ExperienceRecord.from_dict(_record(source="another-suite:task")),),
            bank_id="bank-v3",
        )


def test_distillation_parser_is_strict_and_sealed() -> None:
    payload = {"records": [_record()]}
    records = parse_distillation_records(json.dumps(payload))
    assert records[0].sealed is True

    with pytest.raises(ValueError, match="whole response"):
        parse_distillation_records("result: " + json.dumps(payload))
    duplicate = json.dumps(payload)[:-1] + ',"records":[]}'
    with pytest.raises(ValueError, match="duplicate"):
        parse_distillation_records(duplicate)


def test_online_update_happens_only_after_all_arms_are_sealed(tmp_path: Path) -> None:
    stream = build_stream(PilotManifest.from_json(MANIFEST))
    state = PrequentialState(stream, initial_checkpoint_sha256="1" * 64)
    current = state.current.instance_id
    trajectory = _sealed_trajectory(current)
    event_id = trajectory.arm_event_ids["A"][0]
    proposal = _record(source=current, event_id=event_id)
    distiller = FakeGenerator(json.dumps({"records": [proposal]}))
    bank = ExperienceBankSnapshot.create(
        bank_id="online-bank-v000", parent_sha256=None, records=()
    )
    updater = ContinualUpdater(
        bank_archive=ExperienceBankArchive(tmp_path / "banks"),
        checkpoint_archive=BuilderCheckpointArchive(tmp_path / "checkpoints"),
        distiller=distiller,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
    )

    with pytest.raises(ValueError, match="sealed"):
        updater.update(state=state, trajectory=trajectory, bank=bank)
    assert distiller.calls == []

    for arm in ARMS:
        state.seal_arm(arm)
    state.seal_instance()
    result = updater.update(state=state, trajectory=trajectory, bank=bank)

    assert len(distiller.calls) == 1
    prompt = distiller.calls[0]["prompt"]
    for field in _record(source=current, event_id=event_id):
        assert f'"{field}"' in prompt
    assert '"records": [' in prompt
    assert "exactly these 14 keys" in prompt
    assert "Do not substitute suite, instance_id, builder_checkpoint_sha256" in prompt
    assert result.bank.records[0].source_instance_id == current
    assert result.bank.parent_sha256 == bank.sha256
    assert result.checkpoint.experience_bank_sha256 == result.bank.sha256
    assert state.current.instance_id != current
    assert state.online_checkpoint_sha256 == result.checkpoint.sha256


def test_distillation_cannot_claim_unbound_or_wrong_instance_evidence(tmp_path: Path) -> None:
    stream = build_stream(PilotManifest.from_json(MANIFEST))
    state = PrequentialState(stream, initial_checkpoint_sha256="1" * 64)
    current = state.current.instance_id
    for arm in ARMS:
        state.seal_arm(arm)
    state.seal_instance()
    trajectory = _sealed_trajectory(current)
    bank = ExperienceBankSnapshot.create(
        bank_id="online-bank-v000", parent_sha256=None, records=()
    )

    wrong_source = FakeGenerator(
        json.dumps({"records": [_record(source="other-suite:other-task", event_id="A-sealed")]})
    )
    updater = ContinualUpdater(
        bank_archive=ExperienceBankArchive(tmp_path / "banks"),
        checkpoint_archive=BuilderCheckpointArchive(tmp_path / "checkpoints"),
        distiller=wrong_source,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
    )
    with pytest.raises(ValueError, match="current sealed instance"):
        updater.update(state=state, trajectory=trajectory, bank=bank)

    unbound = FakeGenerator(
        json.dumps({"records": [_record(source=current, event_id="invented-event")]})
    )
    updater = ContinualUpdater(
        bank_archive=ExperienceBankArchive(tmp_path / "banks-2"),
        checkpoint_archive=BuilderCheckpointArchive(tmp_path / "checkpoints-2"),
        distiller=unbound,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
    )
    with pytest.raises(ValueError, match="provenance"):
        updater.update(state=state, trajectory=trajectory, bank=bank)


def test_experience_retrieval_matches_new_instance_and_derives_rule_support() -> None:
    records = (
        ExperienceRecord.from_dict(
            _record(
                record_id="record-match-a",
                source="kernelbench:train-a",
                event_id="event-a",
            )
        ),
        ExperienceRecord.from_dict(
            _record(
                record_id="record-match-b",
                source="kernelbench:train-b",
                event_id="event-b",
            )
        ),
        ExperienceRecord.from_dict(
            {
                **_record(
                    record_id="record-unrelated",
                    source="swe-perf:train-c",
                    event_id="event-c",
                ),
                "instance_descriptor": ["repository-patch", "io-bound"],
                "evolution_rule": "dream",
            }
        ),
        ExperienceRecord.from_dict(
            _record(
                record_id="record-self",
                source="kernelbenchx:new-task",
                event_id="event-self",
            )
        ),
    )
    bank = ExperienceBankSnapshot.create(
        bank_id="retrieval-bank", parent_sha256=None, records=records
    )

    retrieved = bank.retrieve(
        instance_id="kernelbenchx:new-task",
        instance_descriptors=("quantized", "reduction"),
        limit=3,
    )

    assert [item["record_id"] for item in retrieved[:2]] == [
        "record-match-a",
        "record-match-b",
    ]
    assert all(item["source_instance_id"] != "kernelbenchx:new-task" for item in retrieved)
    assert retrieved[0]["scope"] == "within_benchmark_replicated"
    assert "initial_harness=" in retrieved[0]["summary"]
    assert "evolution_rule=discipline" in retrieved[0]["summary"]
