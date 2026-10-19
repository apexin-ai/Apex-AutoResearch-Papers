from __future__ import annotations

from pathlib import Path

import pytest

from optimization_lab.harness_builder.experience import (
    ExperienceRecord,
    promotion_level,
)
from optimization_lab.harness_builder.schema import PilotManifest
from optimization_lab.harness_builder.stream import ARMS, PrequentialState, build_stream


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"


def test_stream_interleaves_three_suites_and_rotates_all_four_arms() -> None:
    manifest = PilotManifest.from_json(MANIFEST)
    stream = build_stream(manifest)

    assert len(stream) == 24
    assert len({item.instance_id for item in stream}) == 24
    for block in range(8):
        items = [item for item in stream if item.block_index == block]
        assert len(items) == 3
        assert {item.suite for item in items} == {
            "kernelbenchx",
            "compilergym-cbench",
            "swe-perf",
        }
    assert all(set(item.arm_order) == set(ARMS) for item in stream)
    assert len({item.arm_order for item in stream[:4]}) == 4


def test_online_builder_cannot_learn_until_current_instance_is_fully_sealed() -> None:
    stream = build_stream(PilotManifest.from_json(MANIFEST))
    state = PrequentialState(stream, initial_checkpoint_sha256="1" * 64)

    assert state.current == stream[0]
    for arm in ARMS[:-1]:
        state.seal_arm(arm)
    with pytest.raises(ValueError, match="all arms"):
        state.seal_instance()
    with pytest.raises(ValueError, match="sealed"):
        state.apply_distillation("2" * 64)

    state.seal_arm(ARMS[-1])
    state.seal_instance()
    with pytest.raises(ValueError, match="distillation"):
        state.seal_arm(ARMS[0])
    state.apply_distillation("2" * 64)
    assert state.current == stream[1]
    assert state.online_checkpoint_sha256 == "2" * 64


def test_experience_record_requires_sealed_public_provenance() -> None:
    record = ExperienceRecord.from_dict(
        {
            "record_id": "record-001",
            "source_instance_id": "kernelbenchx:example",
            "builder_version": "builder-v001",
            "instance_descriptor": ["quantized", "reduction"],
            "initial_harness_structure": ["analyst", "generator"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["correct incumbent", "flat score"],
            "outcome_delta": 0.03,
            "correctness": True,
            "resource_cost": {"model_calls": 2.0, "evaluator_seconds": 12.5},
            "counterexamples": ["No gain on a memory-bound shape."],
            "scope": "single_instance_observation",
            "provenance_event_ids": ["event-001", "event-002"],
            "sealed": True,
        }
    )
    assert record.sealed is True

    payload = record.to_dict()
    payload["sealed"] = False
    with pytest.raises(ValueError, match="sealed"):
        ExperienceRecord.from_dict(payload)

    payload = record.to_dict()
    payload["counterexamples"] = ["private evaluator log at /data3/secret"]
    with pytest.raises(ValueError, match="private path"):
        ExperienceRecord.from_dict(payload)


def test_promotion_levels_require_cross_benchmark_replication() -> None:
    assert promotion_level(instance_count=1, benchmark_count=1) == "single_instance_observation"
    assert promotion_level(instance_count=3, benchmark_count=1) == "within_benchmark_replicated"
    assert promotion_level(instance_count=4, benchmark_count=2) == "cross_benchmark_replicated"
    assert promotion_level(instance_count=6, benchmark_count=3) == "trusted_default_prior"
