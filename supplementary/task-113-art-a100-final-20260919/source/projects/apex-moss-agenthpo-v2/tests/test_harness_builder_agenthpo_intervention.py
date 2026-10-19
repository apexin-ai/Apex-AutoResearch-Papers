from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

import pytest

from optimization_lab.harness_builder.agenthpo_intervention import (
    AgentHPOSpaceSourceReceipt,
    AgentHPOInterventionError,
    DecisionOperationReceipt,
    DiscreteInterventionSpace,
    InterventionSpaceBinding,
    ProviderRequestReceipt,
    StrictIntervention,
    derive_pinned_discrete_intervention_space,
    parse_strict_intervention,
    verify_decision_operation,
)


TASK_SHA = "a" * 64
REQUEST_SHA = "b" * 64
USAGE_SHA = "c" * 64
SOURCE_MANIFEST_SHA = "d" * 64
SPACE_PROJECTION_SHA = "e" * 64
PINNED_SOURCE = Path("/tmp/moss-bench-qual.rYRM8Q/agenthpobench")


def _space() -> DiscreteInterventionSpace:
    return DiscreteInterventionSpace(
        task_id="agenthpo-task-1",
        task_source_sha256=TASK_SHA,
        current_config={
            "batch_size": 32,
            "enabled": False,
            "learning_rate": 0.001,
            "optimizer": "adam",
        },
        allowed_values={
            "batch_size": (16, 32, 64),
            "enabled": (False, True),
            "learning_rate": (0.0005, 0.001, 0.002),
            "optimizer": ("adam", "sgd"),
        },
    )


def _require_pinned_source() -> Path:
    if not PINNED_SOURCE.is_dir():
        pytest.skip("pinned AgentHPO qualification checkout is unavailable")
    return PINNED_SOURCE


def test_pinned_space_derivation_hashes_manifest_runner_and_projection() -> None:
    source = _require_pinned_source()
    space, binding, receipt = derive_pinned_discrete_intervention_space(
        source,
        task_id="hyperboliccv_cifar100_accuracy",
        space_variant="original",
        current_config=None,
        previous_outcome_sha256="0" * 64,
    )
    assert space.current_config == {
        "batch_size": 128,
        "embedding_dim": 512,
        "lr": 0.1,
        "model_type": "E",
        "use_lr_scheduler": False,
        "weight_decay": 0.0005,
    }
    assert space.allowed_values["lr"] == (0.03, 0.1, 0.2)
    assert binding.task_space_projection_sha256 == (
        receipt.task_space_projection_sha256
    )
    assert binding.intervention_space_sha256 == space.sha256
    assert receipt.source_manifest_sha256 == (
        "68d466bc0069908ad178f9a5921e618077545b7aa44d5f64f65cb77cbb88f7de"
    )
    assert receipt.execution_authority == "NOT_GRANTED"
    assert receipt.derivation_status == "MECHANICALLY_DERIVED_ZERO_CALL"
    assert receipt.task_runner_sha256 == hashlib.sha256(
        (
            source
            / "tasks/main/hyperboliccv_cifar100_accuracy/"
            "run_formal_hyperboliccv_cifar100_agent.py"
        ).read_bytes()
    ).hexdigest()
    assert AgentHPOSpaceSourceReceipt.from_canonical_bytes(
        receipt.canonical_bytes
    ) == receipt


def test_pinned_space_derivation_uses_manifest_variant_not_caller_allowlist() -> None:
    source = _require_pinned_source()
    original, _, _ = derive_pinned_discrete_intervention_space(
        source,
        task_id="llm_c_fineweb10b",
        space_variant="original",
        current_config=None,
        previous_outcome_sha256="0" * 64,
    )
    wide, _, _ = derive_pinned_discrete_intervention_space(
        source,
        task_id="llm_c_fineweb10b",
        space_variant="wide",
        current_config=None,
        previous_outcome_sha256="0" * 64,
    )
    assert original.allowed_values["learning_rate"] == (
        0.0004,
        0.0006,
        0.0008,
        0.0009,
        0.001,
    )
    assert wide.allowed_values["learning_rate"] == (
        0.0004,
        0.0006,
        0.0008,
        0.0009,
        0.001,
        0.0005,
        0.0007,
        0.00085,
        0.00095,
        0.0002,
        0.002,
    )
    assert wide.sha256 != original.sha256

    nullable, _, _ = derive_pinned_discrete_intervention_space(
        source,
        task_id="binary_diffusion_adult_rf",
        space_variant="original",
        current_config=None,
        previous_outcome_sha256="0" * 64,
    )
    assert nullable.current_config["max_depth"] is None
    assert nullable.allowed_values["max_depth"] == (3, 4, 5, 8, None)
    nullable_change = parse_strict_intervention(b'{"max_depth":5}', space=nullable)
    assert nullable_change.resulting_config["max_depth"] == 5


def test_pinned_space_derivation_chains_current_config_to_previous_outcome() -> None:
    source = _require_pinned_source()
    initial, _, _ = derive_pinned_discrete_intervention_space(
        source,
        task_id="hyperboliccv_cifar100_accuracy",
        space_variant="original",
        current_config=None,
        previous_outcome_sha256="0" * 64,
    )
    raw = b'{"lr":0.2}'
    prior = parse_strict_intervention(raw, space=initial)
    current, binding, receipt = derive_pinned_discrete_intervention_space(
        source,
        task_id=initial.task_id,
        space_variant="original",
        current_config=prior.resulting_config,
        previous_outcome_sha256=prior.sha256,
    )
    assert current.current_config["lr"] == 0.2
    assert binding.previous_outcome_sha256 == prior.sha256
    assert receipt.previous_outcome_sha256 == prior.sha256
    with pytest.raises(AgentHPOInterventionError, match="previous outcome"):
        derive_pinned_discrete_intervention_space(
            source,
            task_id=initial.task_id,
            space_variant="original",
            current_config=prior.resulting_config,
            previous_outcome_sha256="0" * 64,
        )


def test_free_form_agent_lightning_space_fails_closed_before_codec() -> None:
    source = _require_pinned_source()
    with pytest.raises(AgentHPOInterventionError, match="free-form prompt"):
        derive_pinned_discrete_intervention_space(
            source,
            task_id="agent_lightning_room_selector",
            space_variant="original",
            current_config=None,
            previous_outcome_sha256="0" * 64,
        )


def test_pinned_source_drift_fails_before_space_receipt(tmp_path: Path) -> None:
    source = _require_pinned_source()
    forged = tmp_path / "agenthpo"
    subprocess.run(
        ("git", "clone", "--local", "--no-hardlinks", str(source), str(forged)),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    runner = (
        forged
        / "tasks/main/hyperboliccv_cifar100_accuracy/"
        "run_formal_hyperboliccv_cifar100_agent.py"
    )
    runner.write_bytes(runner.read_bytes() + b"\n# drift\n")
    with pytest.raises(AgentHPOInterventionError, match="tracked worktree is dirty"):
        derive_pinned_discrete_intervention_space(
            forged.resolve(),
            task_id="hyperboliccv_cifar100_accuracy",
            space_variant="original",
            current_config=None,
            previous_outcome_sha256="0" * 64,
        )


def test_pinned_runner_must_match_head_tracked_blob_even_if_status_hides_it(
    tmp_path: Path,
) -> None:
    source = _require_pinned_source()
    forged = tmp_path / "agenthpo"
    subprocess.run(
        ("git", "clone", "--local", "--no-hardlinks", str(source), str(forged)),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    runner = (
        forged
        / "tasks/main/hyperboliccv_cifar100_accuracy/"
        "run_formal_hyperboliccv_cifar100_agent.py"
    )
    relative_runner = runner.relative_to(forged)
    subprocess.run(
        (
            "git",
            "-C",
            str(forged),
            "update-index",
            "--assume-unchanged",
            relative_runner,
        ),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    runner.write_bytes(runner.read_bytes() + b"\n# hidden source drift\n")
    assert subprocess.run(
        (
            "git",
            "-C",
            str(forged),
            "status",
            "--porcelain=v1",
            "--untracked-files=no",
        ),
        check=True,
        stdout=subprocess.PIPE,
    ).stdout == b""
    with pytest.raises(AgentHPOInterventionError, match="task runner hash drifted"):
        derive_pinned_discrete_intervention_space(
            forged.resolve(),
            task_id="hyperboliccv_cifar100_accuracy",
            space_variant="original",
            current_config=None,
            previous_outcome_sha256="0" * 64,
        )


def test_space_and_strict_intervention_round_trip() -> None:
    space = _space()
    assert DiscreteInterventionSpace.from_canonical_bytes(space.canonical_bytes) == space
    raw = b'{"batch_size":64,"optimizer":"sgd"}'
    intervention = parse_strict_intervention(raw, space=space)
    assert intervention.proposed_changes == {
        "batch_size": 64,
        "optimizer": "sgd",
    }
    assert intervention.resulting_config == {
        "batch_size": 64,
        "enabled": False,
        "learning_rate": 0.001,
        "optimizer": "sgd",
    }
    assert intervention.raw_response_sha256 == hashlib.sha256(raw).hexdigest()
    assert StrictIntervention.from_canonical_bytes(
        intervention.canonical_bytes
    ) == intervention


@pytest.mark.parametrize(
    ("raw", "reason"),
    [
        (b'{"unknown":1}', "unknown keys"),
        (b'{"batch_size":48}', "outside the allowlist"),
        (b'{"batch_size":32}', "no operational"),
        (b'{"batch_size":64.0}', "scalar type"),
        (b'{"enabled":1}', "scalar type"),
        (b'{}', "empty"),
        (b'{"optimizer":"sgd"} trailing', "contains data after"),
        (b'{"optimizer":"sgd","optimizer":"adam"}', "repeats field"),
        (b'{"learning_rate":NaN}', "contains NaN"),
        (b"{'optimizer':'sgd'}", "not one strict JSON"),
    ],
)
def test_strict_codec_rejects_clamp_alias_fallback_and_permissive_json(
    raw: bytes, reason: str
) -> None:
    with pytest.raises(AgentHPOInterventionError, match=reason):
        parse_strict_intervention(raw, space=_space())


def test_intervention_space_rejects_mixed_types_duplicates_and_missing_current() -> None:
    with pytest.raises(AgentHPOInterventionError, match="scalar type"):
        DiscreteInterventionSpace(
            task_id="task",
            task_source_sha256=TASK_SHA,
            current_config={"batch_size": 32},
            allowed_values={"batch_size": (32, 64.0)},
        )


def test_space_binding_rejects_source_allowlist_and_current_config_rehash() -> None:
    space = _space()
    binding = InterventionSpaceBinding.create(
        space=space,
        expected_task_id=space.task_id,
        expected_task_source_sha256=space.task_source_sha256,
        expected_source_manifest_sha256=SOURCE_MANIFEST_SHA,
        expected_task_space_projection_sha256=SPACE_PROJECTION_SHA,
        previous_outcome_sha256="0" * 64,
    )
    binding.verify_space(
        space,
        expected_task_id=space.task_id,
        expected_task_source_sha256=space.task_source_sha256,
        expected_source_manifest_sha256=SOURCE_MANIFEST_SHA,
        expected_task_space_projection_sha256=SPACE_PROJECTION_SHA,
        expected_previous_outcome_sha256="0" * 64,
    )
    expanded = DiscreteInterventionSpace(
        task_id=space.task_id,
        task_source_sha256=space.task_source_sha256,
        current_config=space.current_config,
        allowed_values={
            **space.allowed_values,
            "batch_size": (*space.allowed_values["batch_size"], 128),
        },
    )
    changed_current = DiscreteInterventionSpace(
        task_id=space.task_id,
        task_source_sha256=space.task_source_sha256,
        current_config={**space.current_config, "batch_size": 64},
        allowed_values=space.allowed_values,
    )
    for forged in (expanded, changed_current):
        with pytest.raises(AgentHPOInterventionError, match="trusted derivation"):
            binding.verify_space(
                forged,
                expected_task_id=space.task_id,
                expected_task_source_sha256=space.task_source_sha256,
                expected_source_manifest_sha256=SOURCE_MANIFEST_SHA,
                expected_task_space_projection_sha256=SPACE_PROJECTION_SHA,
                expected_previous_outcome_sha256="0" * 64,
            )
    with pytest.raises(AgentHPOInterventionError, match="task source differs"):
        InterventionSpaceBinding.create(
            space=space,
            expected_task_id=space.task_id,
            expected_task_source_sha256="f" * 64,
            expected_source_manifest_sha256=SOURCE_MANIFEST_SHA,
            expected_task_space_projection_sha256=SPACE_PROJECTION_SHA,
            previous_outcome_sha256="0" * 64,
        )
    with pytest.raises(AgentHPOInterventionError, match="duplicates"):
        DiscreteInterventionSpace(
            task_id="task",
            task_source_sha256=TASK_SHA,
            current_config={"batch_size": 32},
            allowed_values={"batch_size": (32, 32)},
        )
    with pytest.raises(AgentHPOInterventionError, match="outside"):
        DiscreteInterventionSpace(
            task_id="task",
            task_source_sha256=TASK_SHA,
            current_config={"batch_size": 32},
            allowed_values={"batch_size": (16, 64)},
        )


def _completed_request(intervention: StrictIntervention) -> ProviderRequestReceipt:
    return ProviderRequestReceipt(
        decision_operation_id="agenthpo:task:seed:v002:solution",
        request_index=1,
        provider="codex-cli",
        model="gpt-test",
        request_payload_sha256=REQUEST_SHA,
        response_artifact_sha256=intervention.raw_response_sha256,
        usage_artifact_sha256=USAGE_SHA,
        terminal_status="COMPLETED",
    )


def test_one_logical_decision_binds_exactly_one_underlying_request() -> None:
    space = _space()
    raw = b'{"optimizer":"sgd"}'
    intervention = parse_strict_intervention(raw, space=space)
    request = _completed_request(intervention)
    operation = DecisionOperationReceipt.seal(
        request=request,
        space=space,
        raw_response=raw,
        intervention=intervention,
    )
    assert operation.logical_model_call_debit == 1
    assert operation.provider_request_debit == 1
    assert ProviderRequestReceipt.from_canonical_bytes(
        request.canonical_bytes
    ) == request
    assert DecisionOperationReceipt.from_canonical_bytes(
        operation.canonical_bytes
    ) == operation
    verify_decision_operation(
        operation=operation,
        request_receipts=(request,),
        space=space,
        raw_response=raw,
        intervention=intervention,
    )

    retry = ProviderRequestReceipt(
        **{
            **request.to_dict(),
            "request_index": 1,
            "request_payload_sha256": "d" * 64,
        }
    )
    with pytest.raises(AgentHPOInterventionError, match="exactly one"):
        verify_decision_operation(
            operation=operation,
            request_receipts=(request, retry),
            space=space,
            raw_response=raw,
            intervention=intervention,
        )
    concealed_second = ProviderRequestReceipt(
        **{**request.to_dict(), "request_index": 2}
    )
    with pytest.raises(AgentHPOInterventionError, match="exactly one"):
        verify_decision_operation(
            operation=operation,
            request_receipts=(request, concealed_second),
            space=space,
            raw_response=raw,
            intervention=intervention,
        )


def test_failed_request_is_charged_once_and_has_no_intervention() -> None:
    space = _space()
    request = ProviderRequestReceipt(
        decision_operation_id="agenthpo:task:seed:v003:solution",
        request_index=1,
        provider="codex-cli",
        model="gpt-test",
        request_payload_sha256=REQUEST_SHA,
        response_artifact_sha256="0" * 64,
        usage_artifact_sha256="0" * 64,
        terminal_status="FAILED",
    )
    operation = DecisionOperationReceipt.seal(
        request=request,
        space=space,
        raw_response=None,
        intervention=None,
    )
    assert operation.intervention_sha256 == "0" * 64
    assert operation.logical_model_call_debit == 1
    assert operation.provider_request_debit == 1
    verify_decision_operation(
        operation=operation,
        request_receipts=(request,),
        space=space,
        raw_response=None,
        intervention=None,
    )


def test_response_space_and_operation_rebinding_fail_closed() -> None:
    space = _space()
    raw = b'{"optimizer":"sgd"}'
    intervention = parse_strict_intervention(raw, space=space)
    request = _completed_request(intervention)
    with pytest.raises(AgentHPOInterventionError, match="response differs"):
        DecisionOperationReceipt.seal(
            request=ProviderRequestReceipt(
                **{**request.to_dict(), "response_artifact_sha256": "e" * 64}
            ),
            space=space,
            raw_response=raw,
            intervention=intervention,
        )
    other_space = DiscreteInterventionSpace(
        task_id="agenthpo-task-1",
        task_source_sha256="f" * 64,
        current_config=space.current_config,
        allowed_values=space.allowed_values,
    )
    with pytest.raises(AgentHPOInterventionError, match="codec replay"):
        DecisionOperationReceipt.seal(
            request=request,
            space=other_space,
            raw_response=raw,
            intervention=intervention,
        )


@pytest.mark.parametrize(
    "changes",
    [
        {"task_id": "another-task"},
        {"proposed_changes": {"batch_size": 999}},
        {"resulting_config": {
            "batch_size": 16,
            "enabled": False,
            "learning_rate": 0.001,
            "optimizer": "adam",
        }},
    ],
)
def test_operation_replays_codec_and_rejects_fully_rehashed_intervention_forge(
    changes: dict[str, object],
) -> None:
    space = _space()
    raw = b'{"batch_size":64}'
    valid = parse_strict_intervention(raw, space=space)
    request = _completed_request(valid)
    forged = StrictIntervention(
        task_id=changes.get("task_id", valid.task_id),
        intervention_space_sha256=valid.intervention_space_sha256,
        raw_response_sha256=valid.raw_response_sha256,
        proposed_changes=changes.get("proposed_changes", valid.proposed_changes),
        resulting_config=changes.get("resulting_config", valid.resulting_config),
    )
    with pytest.raises(AgentHPOInterventionError, match="codec replay"):
        DecisionOperationReceipt.seal(
            request=request,
            space=space,
            raw_response=raw,
            intervention=forged,
        )
