from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.gdpevo_qualification import (
    DEFAULT_GDPEVO_QUALIFICATION_MANIFEST,
    GDPevoQualificationError,
    adapt_gdpevo_evaluator_output,
    canonical_gdpevo_qualification_bytes,
    verify_candidate_artifact,
    verify_future_canary_results,
    verify_gdpevo_qualification,
)


def _payload() -> dict[str, object]:
    return json.loads(
        DEFAULT_GDPEVO_QUALIFICATION_MANIFEST.read_text(encoding="utf-8")
    )


def _write(tmp_path: Path, payload: object, *, canonical: bool = True) -> Path:
    path = tmp_path / "gdpevo-contract.json"
    if canonical:
        path.write_bytes(canonical_gdpevo_qualification_bytes(payload))
    else:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def test_checked_in_gdpevo_contract_is_source_locked_and_zero_authority() -> None:
    payload = verify_gdpevo_qualification()
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert payload["execution_entitlement"] == {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "max_parallel": 0,
        "model_calls": 0,
    }
    assert payload["source_lock"] == {
        "git_commit": "0999c0d1e6f59b1cb8464cac4e5ed856b5dcb9e4",
        "repository": "https://github.com/Prism-Shadow/GDPevo",
        "root_tree": "983742f806f4bf6c4043d5ebea62dc4095be4c0d",
        "task_groups_tree": "2949144b022e5028ee8b48f4bb27355496df19de",
    }
    assert [item["group_id"] for item in payload["qualification_groups"]] == [
        "task_group_006",
        "task_group_024",
        "task_group_015",
        "task_group_007",
        "task_group_001",
        "task_group_014",
    ]
    assert {item["test_task_count"] for item in payload["qualification_groups"]} == {5}
    assert payload["file_manifests"]["task_group_yaml"] == {
        "byte_count": 81_089,
        "file_count": 6,
        "sha256": "91ec78a1b46a1081512b717462cdd0ccd0ab7cd89186cdf7a32e02829ba79fd8",
    }
    assert payload["file_manifests"]["evaluator_template_gold"] == {
        "byte_count": 544_234,
        "file_count": 120,
        "sha256": "41cd3e50fe83ead610908bbea20ca9b21a86f3e38a0303cb873bfaba328f77b0",
    }
    assert payload["file_manifests"]["environment"] == {
        "byte_count": 1_739_394,
        "file_count": 108,
        "sha256": "0befc37814b414ca7ebf8675a17f90add1ecc7446c44e5fa1b3033df29fa209a",
    }
    assert payload["file_manifests"]["control_plane"] == {
        "byte_count": 2_364_717,
        "file_count": 234,
        "sha256": "f119fc1e3f09affa94f22c14c310eb238b6c7add047440949e9c8996b7bcd86a",
    }


def test_all_group_trees_and_score_modes_are_frozen() -> None:
    payload = verify_gdpevo_qualification()
    groups = {
        item["group_id"]: item for item in payload["qualification_groups"]
    }
    assert groups["task_group_001"]["trees"] == {
        "env_tree": "4f102c7ba5b9949a83e05b07575616ec4f89974d",
        "group_tree": "c29a7931b8dc4d7ee7b1b56f01beb1f016b52b0c",
        "test_tasks_tree": "85efbc731dfaad7c8bd1ac26dd235e51420d54d7",
    }
    assert groups["task_group_006"]["trees"] == {
        "env_tree": "1055712612a837101278a4755d75a0023751bd50",
        "group_tree": "14ae5eff6d9d9a356b5d49673f1d742c10731fb4",
        "test_tasks_tree": "db73b876f27e42c62c914f26ebfbe32814675c13",
    }
    assert groups["task_group_007"]["trees"] == {
        "env_tree": "ca8a41152c19b6d47e1fb2c7cc81070bbecec66c",
        "group_tree": "a100b1ede8b6c0839549b5f9816b0d84d4c703f9",
        "test_tasks_tree": "a3b7c5f93c4142ecd1fc98d3a8a7d5381e128f1a",
    }
    assert groups["task_group_014"]["trees"] == {
        "env_tree": "439812c36a1632099999b19981d47dc8ae05a903",
        "group_tree": "940f35104ca37b407846553e691e1a97514a3a58",
        "test_tasks_tree": "a47e3794d5bfb84147ecd2d6d6c747b9c42f2b63",
    }
    assert groups["task_group_015"]["trees"] == {
        "env_tree": "6b98a0ad8da2a395b66c239f18493f478b1a4c97",
        "group_tree": "541e130c30f79b521aadae4c2899acd50b83ac5d",
        "test_tasks_tree": "c822793843928fde0d0c682416509b0e060e4d90",
    }
    assert groups["task_group_024"]["trees"] == {
        "env_tree": "2a9adc4f84f7a7d73593220eeee3c93a72b09153",
        "group_tree": "9403255853f26b9b50c89035312d2d30cf6f9728",
        "test_tasks_tree": "6e79b4da5420ec4ce50195e9414b1eee51fe25ad",
    }
    assert groups["task_group_001"]["score_contract"]["metric_field"] == "total_score"
    for group_id in ("task_group_006", "task_group_007", "task_group_014", "task_group_015"):
        assert groups[group_id]["score_contract"]["metric_field"] == "score"
    assert groups["task_group_024"]["score_contract"] == {
        "metric_field": "score",
        "mode": "normalized_numeric_field_direct_no_renormalization",
        "points_max_score_use": "optional_consistency_check_only",
        "range": [0.0, 1.0],
    }


def test_canary_plan_is_declared_but_has_no_entitlement() -> None:
    payload = verify_gdpevo_qualification()
    plan = payload["canary_plan"]
    assert plan["candidate_count_by_kind"] == {
        "blank": 30,
        "gold": 30,
        "template": 30,
    }
    assert plan["deterministic_repeat_count"] == 2
    assert plan["expected_normalized_score_by_kind"] == {
        "blank": 0.0,
        "gold": 1.0,
        "template": 0.0,
    }
    assert plan["planned_evaluator_transactions"] == 180
    assert plan["future_gate_only"] is True
    assert payload["capability"] == {
        "blockers": [
            "docker_or_podman_runtime_unavailable",
            "minimum_2_cpu_capacity_unverified",
            "minimum_8_gib_memory_capacity_unverified",
            "disk_capacity_insufficient",
            "evaluator_runtime_isolation_canary_pending",
        ],
        "execution_ready": False,
        "status": "BLOCKED_CAPABILITY",
    }


def test_manifest_schema_source_and_observed_hash_drift_fail_closed(
    tmp_path: Path,
) -> None:
    payload = _payload()
    payload["unexpected"] = True
    with pytest.raises(GDPevoQualificationError, match="fields or source bindings"):
        verify_gdpevo_qualification(_write(tmp_path, payload))

    payload = _payload()
    payload["source_lock"]["root_tree"] = "0" * 40
    with pytest.raises(GDPevoQualificationError, match="fields or source bindings"):
        verify_gdpevo_qualification(_write(tmp_path, payload))

    expected = verify_gdpevo_qualification()
    observed = copy.deepcopy(expected["source_lock"])
    observed["git_commit"] = "0" * 40
    with pytest.raises(GDPevoQualificationError, match="source lock drifted"):
        verify_gdpevo_qualification(observed_source_lock=observed)

    observed_files = copy.deepcopy(expected["file_manifests"])
    observed_files["environment"]["sha256"] = "0" * 64
    with pytest.raises(GDPevoQualificationError, match="file manifests drifted"):
        verify_gdpevo_qualification(observed_file_manifests=observed_files)


def test_noncanonical_duplicate_and_execution_request_fail(tmp_path: Path) -> None:
    with pytest.raises(GDPevoQualificationError, match="not canonically encoded"):
        verify_gdpevo_qualification(_write(tmp_path, _payload(), canonical=False))

    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"schema_version":1,"schema_version":1}\n', encoding="utf-8")
    with pytest.raises(GDPevoQualificationError, match="repeats"):
        verify_gdpevo_qualification(duplicate)

    with pytest.raises(GDPevoQualificationError, match="no execution authority"):
        verify_gdpevo_qualification(request_execution=True)


def test_candidate_binding_accepts_only_explicit_external_real_file(
    tmp_path: Path,
) -> None:
    evaluator_root = tmp_path / "task" / "eval"
    gold_root = tmp_path / "task" / "output"
    candidate_root = tmp_path / "attempt"
    evaluator_root.mkdir(parents=True)
    gold_root.mkdir(parents=True)
    candidate_root.mkdir()
    candidate = candidate_root / "candidate.json"
    candidate.write_text('{"answer":1}\n', encoding="utf-8")
    digest = hashlib.sha256(candidate.read_bytes()).hexdigest()

    result = verify_candidate_artifact(
        candidate.resolve(),
        expected_sha256=digest,
        forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
    )
    assert result == {
        "candidate_realpath": str(candidate.resolve()),
        "candidate_sha256": digest,
        "size_bytes": candidate.stat().st_size,
    }

    with pytest.raises(GDPevoQualificationError, match="must be explicit"):
        verify_candidate_artifact(
            None,
            expected_sha256=digest,
            forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
        )
    with pytest.raises(GDPevoQualificationError, match="must be absolute"):
        verify_candidate_artifact(
            Path("candidate.json"),
            expected_sha256=digest,
            forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
        )


def test_candidate_gold_symlink_and_hash_drift_are_rejected(tmp_path: Path) -> None:
    evaluator_root = tmp_path / "eval"
    gold_root = tmp_path / "output"
    candidate_root = tmp_path / "attempt"
    for root in (evaluator_root, gold_root, candidate_root):
        root.mkdir()
    gold = gold_root / "answer.json"
    gold.write_text("{}\n", encoding="utf-8")
    digest = hashlib.sha256(gold.read_bytes()).hexdigest()

    with pytest.raises(GDPevoQualificationError, match="inside a gold or evaluator"):
        verify_candidate_artifact(
            gold.resolve(),
            expected_sha256=digest,
            forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
        )

    candidate = candidate_root / "candidate.json"
    candidate.write_text("{}\n", encoding="utf-8")
    link = candidate_root / "linked.json"
    link.symlink_to(candidate)
    with pytest.raises(GDPevoQualificationError, match="symlinks"):
        verify_candidate_artifact(
            link.absolute(),
            expected_sha256=digest,
            forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
        )

    with pytest.raises(GDPevoQualificationError, match="content hash drifted"):
        verify_candidate_artifact(
            candidate.resolve(),
            expected_sha256="0" * 64,
            forbidden_roots=(evaluator_root.resolve(), gold_root.resolve()),
        )


def test_scored_adapter_uses_group_specific_metric_and_private_boundary() -> None:
    group_one = adapt_gdpevo_evaluator_output(
        "task_group_001",
        json.dumps({"total_score": 0.75, "details": [{"gold": "private"}]}),
    )
    assert group_one.public_projection == {
        "normalized_score": 0.75,
        "validity": "valid",
        "coarse_reason_codes": [],
    }
    assert set(group_one.public_projection) == {
        "normalized_score",
        "validity",
        "coarse_reason_codes",
    }
    assert "details" not in group_one.public_projection
    assert group_one.private_evidence["raw_evaluator_output"]["details"] == [
        {"gold": "private"}
    ]

    ordinary = adapt_gdpevo_evaluator_output(
        "task_group_006",
        '{"error":"bad candidate","score":0.0}',
    )
    assert ordinary.public_projection == {
        "normalized_score": 0.0,
        "validity": "invalid",
        "coarse_reason_codes": ["evaluator_reported_error"],
    }


@pytest.mark.parametrize(
    ("group_id", "stdout", "message"),
    [
        ("task_group_001", '{"score":0.5}', "requires numeric total_score"),
        ("task_group_006", '{"total_score":0.5}', "requires numeric score"),
        ("task_group_006", '{"score":1.1}', "outside finite"),
        ("task_group_006", '{"score":NaN}', "contains NaN"),
        ("task_group_006", '{"score":0.5} trailing', "contains data after"),
        ("task_group_006", '[{"score":0.5}]', "must be a JSON object"),
    ],
)
def test_scored_adapter_rejects_wrong_ambiguous_or_nonfinite_output(
    group_id: str,
    stdout: str,
    message: str,
) -> None:
    with pytest.raises(GDPevoQualificationError, match=message):
        adapt_gdpevo_evaluator_output(group_id, stdout)


def test_group_024_uses_score_directly_and_only_checks_points_ratio() -> None:
    result = adapt_gdpevo_evaluator_output(
        "task_group_024", '{"score":0.75,"points":3,"max_score":4}'
    )
    assert result.public_projection == {
        "normalized_score": 0.75,
        "validity": "valid",
        "coarse_reason_codes": [],
    }

    without_optional_ratio = adapt_gdpevo_evaluator_output(
        "task_group_024", '{"score":0.25}'
    )
    assert without_optional_ratio.public_projection["normalized_score"] == 0.25

    with pytest.raises(GDPevoQualificationError, match="disagrees"):
        adapt_gdpevo_evaluator_output(
            "task_group_024", '{"score":0.9,"points":3,"max_score":4}'
        )
    with pytest.raises(GDPevoQualificationError, match="appear together"):
        adapt_gdpevo_evaluator_output(
            "task_group_024", '{"score":0.5,"max_score":4}'
        )


def test_future_canary_gate_requires_gold_one_blank_and_template_zero() -> None:
    results = {
        "gold": [[1.0, 1.0] for _ in range(30)],
        "blank": [[0.0, 0.0] for _ in range(30)],
        "template": [[0.0, 0.0] for _ in range(30)],
    }
    assert verify_future_canary_results(results) == {
        "candidate_count": 90,
        "deterministic_repeat_count": 2,
        "evaluator_transaction_count": 180,
        "passed": True,
    }

    results["gold"][0] = [1.0, 0.0]
    with pytest.raises(GDPevoQualificationError, match="nondeterministic"):
        verify_future_canary_results(results)

    results["gold"][0] = [0.0, 0.0]
    with pytest.raises(GDPevoQualificationError, match="expected score"):
        verify_future_canary_results(results)
