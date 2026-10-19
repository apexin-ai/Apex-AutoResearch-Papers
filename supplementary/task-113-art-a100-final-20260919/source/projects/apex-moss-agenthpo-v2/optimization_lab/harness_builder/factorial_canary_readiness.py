"""Zero-call readiness and schedule artifact for factorial benchmark canaries.

The artifact in this module describes future canary work.  It cannot call a
provider, evaluator, benchmark runtime, container engine, or resource
allocator, and it never opens either benchmark checkout.  In particular, a
GDPevo ``gold`` schedule row is only an opaque controller role; no private
answer path, bytes, or content hash is materialized here.

Qualification slices and formal tasks are intentionally represented
separately.  The current AgentHPOBench Q7 and GDPevo six-group qualification
slices do not overlap the formal T12/T6 matrix, so successful qualification
evidence cannot silently authorize formal execution.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
from typing import Any

from .agenthpo_qualification import (
    canonical_agenthpo_qualification_bytes,
    verify_agenthpo_qualification,
)
from .factorial_contract import verify_factorial_contract
from .gdpevo_qualification import (
    canonical_gdpevo_qualification_bytes,
    verify_gdpevo_qualification,
)


_AUTHORITY = "NOT_GRANTED"
_ZERO_ENTITLEMENT = {
    "cpu_evaluator_seconds": 0,
    "evaluator_transactions": 0,
    "gpu_exclusive_seconds": 0,
    "max_parallel": 0,
    "model_calls": 0,
}
_AGENTHPO_NEGATIVE_KINDS = (
    "unknown_key",
    "out_of_range_value",
    "no_operational_change",
)
_GDPEVO_CANDIDATE_KINDS = ("gold", "template", "blank")
_GDPEVO_EXPECTED_SCORES = {"gold": 1.0, "template": 0.0, "blank": 0.0}

_AGENTHPO_SMOKE_BLOCKERS = (
    "agenthpobench_formal_task_reference_smoke_canary_pending",
    "agenthpobench_formal_task_negative_isolation_smoke_canary_pending",
)
_AGENTHPO_ASSET_BLOCKERS = (
    "agenthpobench_pinned_upstream_repository_asset_receipt_pending",
    "agenthpobench_dataset_checkpoint_model_asset_receipt_pending",
    "agenthpobench_python_conda_runtime_receipt_pending",
    "agenthpobench_target_gpu_capability_receipt_pending",
)
_AGENTHPO_GLOBAL_BLOCKERS = (
    "agenthpobench_q7_qualification_does_not_cover_formal_t12",
    *_AGENTHPO_SMOKE_BLOCKERS,
    *_AGENTHPO_ASSET_BLOCKERS,
    "agenthpobench_formal_dispatch_and_trusted_transport_ledger_pending",
    "agenthpobench_free_form_prompt_codec_or_fresh_split_required",
)

_GDPEVO_ISOLATION_BLOCKERS = (
    "gdpevo_container_runtime_capability_receipt_pending",
    "gdpevo_per_attempt_network_and_container_isolation_receipt_pending",
    "gdpevo_controller_private_evaluator_gold_boundary_receipt_pending",
    "gdpevo_test_solver_judge_api_disablement_receipt_pending",
    "gdpevo_health_reset_and_quiescence_receipt_pending",
)
_GDPEVO_IMAGE_BLOCKERS = (
    "gdpevo_base_image_tag_to_digest_resolution_pending",
    "gdpevo_final_environment_image_digest_and_build_receipt_pending",
    "gdpevo_mutable_pull_prohibition_runtime_enforcement_pending",
)
_GDPEVO_MANIFEST_BLOCKERS = (
    "gdpevo_pinned_checkout_file_manifest_independent_replay_pending",
    "gdpevo_candidate_materialization_content_binding_pending",
    "gdpevo_formal_group_tree_evaluator_manifest_smoke_pending",
)
_GDPEVO_GLOBAL_BLOCKERS = (
    "gdpevo_q6_qualification_does_not_cover_formal_t6",
    *_GDPEVO_ISOLATION_BLOCKERS,
    *_GDPEVO_IMAGE_BLOCKERS,
    *_GDPEVO_MANIFEST_BLOCKERS,
)


class FactorialCanaryReadinessError(ValueError):
    """The zero-call canary artifact is malformed, drifted, or asked to run."""


def _reject_constant(value: str) -> None:
    raise FactorialCanaryReadinessError(
        f"canary readiness JSON contains non-finite constant {value}"
    )


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise FactorialCanaryReadinessError(
                f"canary readiness JSON repeats field {key!r}"
            )
        result[key] = value
    return result


def canonical_factorial_canary_readiness_bytes(payload: object) -> bytes:
    """Return the sole accepted serialization for this static artifact."""

    try:
        return (
            json.dumps(
                payload,
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise FactorialCanaryReadinessError(
            "canary readiness payload is not canonical JSON"
        ) from exc


def _load_canonical(raw: bytes) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw:
        raise FactorialCanaryReadinessError(
            "canary readiness artifact must be non-empty bytes"
        )
    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            parse_constant=_reject_constant,
            object_pairs_hook=_reject_duplicates,
        )
    except FactorialCanaryReadinessError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialCanaryReadinessError(
            "canary readiness artifact is not strict JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise FactorialCanaryReadinessError(
            "canary readiness artifact must be a JSON object"
        )
    if canonical_factorial_canary_readiness_bytes(payload) != raw:
        raise FactorialCanaryReadinessError(
            "canary readiness artifact is not canonically encoded"
        )
    return payload


@dataclass(frozen=True)
class FactorialCanaryReadinessArtifact:
    """Immutable canonical bytes for a future-work schedule, not authority."""

    canonical_bytes: bytes

    def __post_init__(self) -> None:
        payload = _load_canonical(self.canonical_bytes)
        if payload.get("execution_authority") != _AUTHORITY:
            raise FactorialCanaryReadinessError(
                "canary readiness artifact cannot grant execution authority"
            )
        if payload.get("execution_entitlement") != _ZERO_ENTITLEMENT:
            raise FactorialCanaryReadinessError(
                "canary readiness artifact entitlement must remain zero"
            )
        suites = payload.get("suites")
        if not isinstance(suites, dict) or set(suites) != {
            "agenthpobench",
            "gdpevo",
        }:
            raise FactorialCanaryReadinessError(
                "canary readiness suite boundary differs"
            )
        for suite_id, suite in suites.items():
            if not isinstance(suite, dict):
                raise FactorialCanaryReadinessError(
                    f"canary readiness suite {suite_id} is malformed"
                )
            if suite.get("execution_authority") != _AUTHORITY:
                raise FactorialCanaryReadinessError(
                    f"canary readiness suite {suite_id} cannot grant authority"
                )
            if suite.get("execution_entitlement") != _ZERO_ENTITLEMENT:
                raise FactorialCanaryReadinessError(
                    f"canary readiness suite {suite_id} entitlement must be zero"
                )
        privacy = payload.get("privacy_boundary")
        if not isinstance(privacy, dict) or any(
            privacy.get(field) is not False
            for field in (
                "benchmark_runtime_connected",
                "evaluator_connected",
                "private_gold_content_read",
                "provider_connected",
            )
        ):
            raise FactorialCanaryReadinessError(
                "canary readiness privacy boundary cannot connect execution"
            )

    @classmethod
    def from_payload(
        cls, payload: Mapping[str, Any]
    ) -> "FactorialCanaryReadinessArtifact":
        if not isinstance(payload, Mapping):
            raise FactorialCanaryReadinessError(
                "canary readiness payload must be a mapping"
            )
        return cls(canonical_factorial_canary_readiness_bytes(dict(payload)))

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        return deepcopy(_load_canonical(self.canonical_bytes))


def _formal_units(
    factorial: Mapping[str, Any], benchmark_id: str
) -> tuple[str, ...]:
    try:
        benchmarks = factorial["main_experiment"]["benchmarks"]
        match = next(
            item for item in benchmarks if item["benchmark_id"] == benchmark_id
        )
        task_units = tuple(match["task_units"])
    except (KeyError, StopIteration, TypeError) as exc:
        raise FactorialCanaryReadinessError(
            f"factorial formal task declaration missing for {benchmark_id}"
        ) from exc
    if not task_units or any(not isinstance(item, str) or not item for item in task_units):
        raise FactorialCanaryReadinessError(
            f"factorial formal task declaration malformed for {benchmark_id}"
        )
    return task_units


def _agenthpo_payload(
    qualification: Mapping[str, Any], formal_tasks: tuple[str, ...]
) -> dict[str, Any]:
    q_tasks = tuple(qualification["qualification_tasks"])
    q_task_ids = tuple(str(item["task_id"]) for item in q_tasks)
    baselines = {str(item["task_id"]): item["baseline"] for item in q_tasks}
    overlap = sorted(set(q_task_ids) & set(formal_tasks))
    if len(q_task_ids) != 7 or overlap:
        raise FactorialCanaryReadinessError(
            "AgentHPO Q7/formal T12 scope differs from the frozen design"
        )

    baseline_schedule = [
        {
            "candidate_kind": "frozen_baseline",
            "expected_native_score": baselines[task_id],
            "planned_evaluator_transactions": 1,
            "repeat_index": repeat_index,
            "schedule_id": (
                f"agenthpobench:q7:baseline:{task_id}:repeat_{repeat_index:02d}"
            ),
            "status": "PLANNED_NOT_AUTHORIZED",
            "task_id": task_id,
        }
        for task_id in q_task_ids
        for repeat_index in (1, 2)
    ]
    negative_assertions = [
        {
            "assertion_id": (
                f"agenthpobench:q7:negative:{kind}:{task_id}"
            ),
            "expected_disposition": "strict_codec_reject_before_evaluator",
            "negative_kind": kind,
            "planned_evaluator_transactions": 0,
            "planned_model_calls": 0,
            "stage": "STRICT_CODEC_BEFORE_EVALUATOR",
            "status": "ZERO_CALL_ASSERTION_ONLY",
            "task_id": task_id,
        }
        for kind in _AGENTHPO_NEGATIVE_KINDS
        for task_id in q_task_ids
    ]
    formal_readiness = []
    for task_id in formal_tasks:
        action_blockers = []
        if task_id == "agent_lightning_room_selector":
            action_blockers.append(
                "agenthpobench_free_form_prompt_codec_or_fresh_split_required"
            )
        formal_readiness.append(
            {
                "action_contract_blockers": action_blockers,
                "environment_asset_blockers": list(_AGENTHPO_ASSET_BLOCKERS),
                "smoke_blockers": list(_AGENTHPO_SMOKE_BLOCKERS),
                "status": "BLOCKED",
                "task_id": task_id,
            }
        )

    return {
        "blockers": list(_AGENTHPO_GLOBAL_BLOCKERS),
        "codec_pre_evaluator_assertions": negative_assertions,
        "execution_authority": _AUTHORITY,
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "formal_task_readiness": formal_readiness,
        "planned_work": {
            "baseline_evaluator_transactions": 14,
            "baseline_repeat_count": 2,
            "baseline_task_count": 7,
            "negative_assertion_count": 21,
            "negative_evaluator_transactions": 0,
            "negative_model_calls": 0,
        },
        "q7_baseline_schedule": baseline_schedule,
        "scope_boundary": {
            "formal_task_ids": list(formal_tasks),
            "formal_task_smoke_required": True,
            "overlap": overlap,
            "qualification_task_ids": list(q_task_ids),
            "qualification_transfer_to_formal": "FORBIDDEN_WITHOUT_FORMAL_SMOKE",
        },
        "status": "BLOCKED_READINESS",
    }


def _gdpevo_payload(
    qualification: Mapping[str, Any], formal_groups: tuple[str, ...]
) -> dict[str, Any]:
    q_groups = tuple(qualification["qualification_groups"])
    q_group_ids = tuple(str(item["group_id"]) for item in q_groups)
    overlap = sorted(set(q_group_ids) & set(formal_groups))
    if len(q_group_ids) != 6 or overlap:
        raise FactorialCanaryReadinessError(
            "GDPevo qualification/formal T6 scope differs from the frozen design"
        )

    evaluator_schedule = []
    for group_id in q_group_ids:
        for task_ordinal in range(1, 6):
            task_id = f"{group_id}:test_{task_ordinal}"
            for kind in _GDPEVO_CANDIDATE_KINDS:
                for repeat_index in (1, 2):
                    if kind == "gold":
                        materialization = (
                            "OPAQUE_CONTROLLER_PRIVATE_REFERENCE_AFTER_AUTHORITY"
                        )
                    elif kind == "template":
                        materialization = (
                            "PUBLIC_ANSWER_TEMPLATE_COPY_AFTER_AUTHORITY"
                        )
                    else:
                        materialization = "SYNTHETIC_BLANK_JSON_AFTER_AUTHORITY"
                    evaluator_schedule.append(
                        {
                            "candidate_kind": kind,
                            "candidate_materialization": materialization,
                            "expected_normalized_score": _GDPEVO_EXPECTED_SCORES[
                                kind
                            ],
                            "group_id": group_id,
                            "planned_evaluator_transactions": 1,
                            "private_gold_content_embedded": False,
                            "repeat_index": repeat_index,
                            "schedule_id": (
                                "gdpevo:qualification:"
                                f"{task_id}:{kind}:repeat_{repeat_index:02d}"
                            ),
                            "status": "PLANNED_NOT_AUTHORIZED",
                            "task_id": task_id,
                        }
                    )

    formal_readiness = [
        {
            "environment_asset_blockers": [
                *_GDPEVO_IMAGE_BLOCKERS,
                *_GDPEVO_MANIFEST_BLOCKERS,
            ],
            "group_id": group_id,
            "isolation_blockers": list(_GDPEVO_ISOLATION_BLOCKERS),
            "status": "BLOCKED",
            "task_ids": [
                f"{group_id}:test_{task_ordinal}"
                for task_ordinal in range(1, 6)
            ],
        }
        for group_id in formal_groups
    ]
    qualification_blockers = tuple(qualification["capability"]["blockers"])

    return {
        "blockers": list(
            dict.fromkeys((*qualification_blockers, *_GDPEVO_GLOBAL_BLOCKERS))
        ),
        "evaluator_schedule": evaluator_schedule,
        "execution_authority": _AUTHORITY,
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "formal_group_readiness": formal_readiness,
        "planned_work": {
            "candidate_count_by_kind": {
                "blank": 30,
                "gold": 30,
                "template": 30,
            },
            "deterministic_repeat_count": 2,
            "evaluator_transactions": 180,
            "model_calls": 0,
        },
        "readiness_gates": {
            "image": {
                "blockers": list(_GDPEVO_IMAGE_BLOCKERS),
                "status": "BLOCKED",
            },
            "isolation": {
                "blockers": list(_GDPEVO_ISOLATION_BLOCKERS),
                "status": "BLOCKED",
            },
            "manifest": {
                "blockers": list(_GDPEVO_MANIFEST_BLOCKERS),
                "status": "BLOCKED",
            },
        },
        "scope_boundary": {
            "formal_group_ids": list(formal_groups),
            "formal_group_smoke_required": True,
            "overlap": overlap,
            "qualification_group_ids": list(q_group_ids),
            "qualification_transfer_to_formal": "FORBIDDEN_WITHOUT_FORMAL_SMOKE",
        },
        "status": "BLOCKED_READINESS",
    }


def _expected_payload() -> dict[str, Any]:
    agenthpo = verify_agenthpo_qualification()
    gdpevo = verify_gdpevo_qualification()
    factorial = verify_factorial_contract()
    formal_agenthpo = _formal_units(factorial, "agenthpobench")
    formal_gdpevo = _formal_units(factorial, "gdpevo")
    return {
        "artifact_id": "moss-factorial-canary-readiness-v1",
        "artifact_kind": "ZERO_CALL_READINESS_AND_SCHEDULE",
        "execution_authority": _AUTHORITY,
        "execution_entitlement": dict(_ZERO_ENTITLEMENT),
        "privacy_boundary": {
            "benchmark_runtime_connected": False,
            "evaluator_connected": False,
            "gdpevo_gold_representation": (
                "OPAQUE_CONTROLLER_ROLE_ONLY_NO_PATH_BYTES_OR_CONTENT_HASH"
            ),
            "private_gold_content_read": False,
            "provider_connected": False,
        },
        "schema_version": 1,
        "source_bindings": {
            "agenthpo_qualification_sha256": hashlib.sha256(
                canonical_agenthpo_qualification_bytes(agenthpo)
            ).hexdigest(),
            "factorial_contract_sha256": factorial["contract_digest"],
            "gdpevo_qualification_sha256": hashlib.sha256(
                canonical_gdpevo_qualification_bytes(gdpevo)
            ).hexdigest(),
        },
        "suites": {
            "agenthpobench": _agenthpo_payload(agenthpo, formal_agenthpo),
            "gdpevo": _gdpevo_payload(gdpevo, formal_gdpevo),
        },
        "status": "BLOCKED_ZERO_ENTITLEMENT",
    }


def build_factorial_canary_readiness() -> FactorialCanaryReadinessArtifact:
    """Build the exact schedule using only checked-in public contracts."""

    return FactorialCanaryReadinessArtifact.from_payload(_expected_payload())


def verify_factorial_canary_readiness(
    artifact: FactorialCanaryReadinessArtifact | Mapping[str, Any] | bytes | None = None,
    *,
    request_execution: bool = False,
) -> FactorialCanaryReadinessArtifact:
    """Rebuild and compare the artifact without granting or consuming work."""

    if request_execution:
        raise FactorialCanaryReadinessError(
            "canary readiness artifact has no execution authority or entitlement"
        )
    expected = build_factorial_canary_readiness()
    if artifact is None:
        return expected
    if isinstance(artifact, FactorialCanaryReadinessArtifact):
        observed = artifact
    elif isinstance(artifact, bytes):
        observed = FactorialCanaryReadinessArtifact(artifact)
    elif isinstance(artifact, Mapping):
        observed = FactorialCanaryReadinessArtifact.from_payload(artifact)
    else:
        raise FactorialCanaryReadinessError(
            "unsupported canary readiness artifact type"
        )
    if observed.canonical_bytes != expected.canonical_bytes:
        raise FactorialCanaryReadinessError(
            "canary readiness artifact differs from frozen contracts"
        )
    return expected


__all__ = [
    "FactorialCanaryReadinessArtifact",
    "FactorialCanaryReadinessError",
    "build_factorial_canary_readiness",
    "canonical_factorial_canary_readiness_bytes",
    "verify_factorial_canary_readiness",
]
