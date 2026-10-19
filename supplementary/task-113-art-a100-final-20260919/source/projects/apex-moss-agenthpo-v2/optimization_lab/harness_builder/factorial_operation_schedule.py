"""Exact zero-call side-effect schedule for the factorial main experiment.

The schedule expands the pinned 1,566 scoring slots into every *potential*
external operation: an optional update, one solution generation, and one
benchmark-native evaluation.  It is a resource-accounting and coverage
artifact only.  CPU/GPU reservations still depend on real canaries, and this
module exposes no journal, governor, provider, evaluator, or execution hook.

Short-circuit failures may later mark a potential stage as skipped by a typed
parent receipt.  They must not manufacture an operation merely to satisfy the
counts recorded here.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from typing import Any, Mapping

from .events import ResourceVector
from .factorial_coverage import (
    ExactFactorialAttemptMatrix,
    FactorialScoringSlot,
    SHARED_V001_ARM_ID,
)
from .factorial_policies import (
    ARM_IDS,
    A_FIXED_FEEDBACK,
    B_FROZEN_WIDE,
    B_TARGETED,
    S_REFLECTION_SKILL,
)
from .factorial_precheck import FactorialFormalZeroCallPlan
from .factorial_task_authority import (
    ExactTaskSeedAuthorityBundle,
    FactorialTaskArtifactAuthority,
)


EXECUTION_AUTHORITY = "NOT_GRANTED"
ENVIRONMENT_RESOURCE_STATUS = "CPU_GPU_CAPS_PENDING_REAL_CANARY"
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_VERSION = re.compile(r"v([0-9]{3})")
_STAGES = ("update", "solution", "evaluator")
_SEMANTIC_ROLES = {
    "shared_v001": "shared_v001_builder",
    S_REFLECTION_SKILL: "task_local_reflection_skill_update",
    B_TARGETED: "targeted_harness_builder_update",
    B_FROZEN_WIDE: "wide_harness_builder_update",
    "solution": "solution_generation",
    "evaluator": "benchmark_native_evaluation",
}
_JOURNAL_KINDS = {
    "update": "planner_call",
    "solution": "solution_call",
    "evaluator": "evaluator_transaction",
}


class FactorialOperationScheduleError(ValueError):
    """The exact potential-operation schedule is malformed or untrusted."""


def _canonical_bytes(payload: object) -> bytes:
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
        raise FactorialOperationScheduleError(
            "operation schedule is not canonical JSON"
        ) from exc


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise FactorialOperationScheduleError(f"invalid {label}")
    return value


def _safe(value: object, label: str) -> str:
    if (
        not isinstance(value, str)
        or _SAFE_ID.fullmatch(value) is None
        or ".." in value
        or "//" in value
        or value.endswith("/")
    ):
        raise FactorialOperationScheduleError(f"unsafe {label}")
    return value


def _resource_for(stage: str) -> ResourceVector:
    if stage in {"update", "solution"}:
        return ResourceVector(model_calls=1)
    if stage == "evaluator":
        return ResourceVector(evaluator_transactions=1)
    raise FactorialOperationScheduleError("unknown potential stage")


def _semantic_role_for_fields(*, arm_id: str, shared_v001: bool, stage: str) -> str:
    if stage != "update":
        return _SEMANTIC_ROLES[stage]
    if shared_v001:
        return _SEMANTIC_ROLES["shared_v001"]
    try:
        return _SEMANTIC_ROLES[arm_id]
    except KeyError as exc:
        raise FactorialOperationScheduleError(
            "fixed-feedback arm cannot own an update stage"
        ) from exc


def _semantic_role(slot: FactorialScoringSlot, stage: str) -> str:
    return _semantic_role_for_fields(
        arm_id=slot.arm_id,
        shared_v001=slot.shared_v001,
        stage=stage,
    )


@dataclass(frozen=True)
class FactorialPotentialOperation:
    """One exact potential side-effect stage, not a reservation or execution."""

    matrix_sha256: str
    slot_sha256: str
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    factorial_contract_sha256: str
    task_seed_key_sha256: str
    benchmark_id: str
    instance_id: str
    seed: int
    arm_id: str
    version: str
    shared_v001: bool
    cell_id: str
    attempt_id: str
    stage: str
    stage_ordinal: int
    logical_operation_id: str
    semantic_role: str
    journal_operation_kind: str
    full_path_reservation: ResourceVector
    schema_version: int = 1
    operation_kind: str = "factorial_potential_side_effect_operation_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.operation_kind != (
            "factorial_potential_side_effect_operation_v1"
        ):
            raise FactorialOperationScheduleError(
                "unsupported potential-operation schema"
            )
        for value, label in (
            (self.matrix_sha256, "matrix sha256"),
            (self.slot_sha256, "slot sha256"),
            (self.factorial_plan_sha256, "plan sha256"),
            (self.task_authority_bundle_sha256, "authority bundle sha256"),
            (self.factorial_contract_sha256, "factorial contract sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
        ):
            _sha(value, label)
        for value, label in (
            (self.benchmark_id, "benchmark id"),
            (self.instance_id, "instance id"),
            (self.cell_id, "cell id"),
            (self.attempt_id, "attempt id"),
            (self.logical_operation_id, "logical operation id"),
            (self.semantic_role, "semantic role"),
            (self.journal_operation_kind, "journal operation kind"),
        ):
            _safe(value, label)
        if type(self.seed) is not int or self.seed < 0:
            raise FactorialOperationScheduleError("operation seed differs")
        if type(self.shared_v001) is not bool:
            raise FactorialOperationScheduleError("operation shared-v001 flag differs")
        version_match = _VERSION.fullmatch(self.version)
        if version_match is None:
            raise FactorialOperationScheduleError("operation version differs")
        if self.stage not in _STAGES or self.stage_ordinal != _STAGES.index(self.stage):
            raise FactorialOperationScheduleError("operation stage order differs")
        if type(self.full_path_reservation) is not ResourceVector:
            raise FactorialOperationScheduleError(
                "operation reservation is not an exact ResourceVector"
            )
        if (
            self.full_path_reservation != _resource_for(self.stage)
            or self.journal_operation_kind != _JOURNAL_KINDS[self.stage]
            or self.semantic_role
            != (
                _semantic_role_for_fields(
                    arm_id=self.arm_id,
                    shared_v001=self.shared_v001,
                    stage=self.stage,
                )
            )
        ):
            raise FactorialOperationScheduleError(
                "potential operation kind or discrete reservation differs"
            )
        if self.shared_v001:
            expected_operation = {
                "update": f"factorial-v001:{self.task_seed_key_sha256}:builder",
                "solution": f"factorial-v001:{self.task_seed_key_sha256}:solution",
                "evaluator": f"factorial-v001:{self.task_seed_key_sha256}:evaluator",
            }[self.stage]
            if (
                self.arm_id != SHARED_V001_ARM_ID
                or self.version != "v001"
                or self.cell_id
                != f"factorial-v001-cell:{self.task_seed_key_sha256}"
                or self.attempt_id
                != f"factorial-attempt:{self.task_seed_key_sha256}:shared-v001"
                or self.logical_operation_id != expected_operation
            ):
                raise FactorialOperationScheduleError(
                    "shared-v001 potential operation identity differs"
                )
        else:
            if self.arm_id not in ARM_IDS or int(version_match.group(1)) < 2:
                raise FactorialOperationScheduleError(
                    "post-v001 potential operation arm/version differs"
                )
            if self.stage == "update" and self.arm_id == A_FIXED_FEEDBACK:
                raise FactorialOperationScheduleError(
                    "fixed-feedback update is policy-inapplicable"
                )
            prefix = (
                f"factorial-round:{self.task_seed_key_sha256}:"
                f"{self.arm_id}:{self.version}"
            )
            if (
                self.cell_id
                != f"factorial-cell:{self.task_seed_key_sha256}:{self.arm_id}"
                or self.attempt_id != prefix + ":attempt"
                or self.logical_operation_id != prefix + f":{self.stage}"
            ):
                raise FactorialOperationScheduleError(
                    "post-v001 potential operation identity differs"
                )

    @classmethod
    def from_slot(
        cls,
        *,
        matrix_sha256: str,
        slot: FactorialScoringSlot,
        stage: str,
    ) -> "FactorialPotentialOperation":
        if type(slot) is not FactorialScoringSlot:
            raise FactorialOperationScheduleError("exact scoring slot is required")
        if stage == "update":
            if not slot.update_operation_expected:
                raise FactorialOperationScheduleError(
                    "policy-inapplicable update cannot become a potential operation"
                )
            operation_id = slot.update_operation_id
        elif stage == "solution":
            operation_id = slot.solution_operation_id
        elif stage == "evaluator":
            operation_id = slot.evaluator_operation_id
        else:
            raise FactorialOperationScheduleError("unknown potential stage")
        return cls(
            matrix_sha256=matrix_sha256,
            slot_sha256=slot.sha256,
            factorial_plan_sha256=slot.factorial_plan_sha256,
            task_authority_bundle_sha256=slot.task_authority_bundle_sha256,
            factorial_contract_sha256=slot.factorial_contract_sha256,
            task_seed_key_sha256=slot.task_seed_key_sha256,
            benchmark_id=slot.benchmark_id,
            instance_id=slot.instance_id,
            seed=slot.seed,
            arm_id=slot.arm_id,
            version=slot.version,
            shared_v001=slot.shared_v001,
            cell_id=slot.cell_id,
            attempt_id=slot.attempt_id,
            stage=stage,
            stage_ordinal=_STAGES.index(stage),
            logical_operation_id=operation_id,
            semantic_role=_semantic_role(slot, stage),
            journal_operation_kind=_JOURNAL_KINDS[stage],
            full_path_reservation=_resource_for(stage),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "attempt_id": self.attempt_id,
            "benchmark_id": self.benchmark_id,
            "cell_id": self.cell_id,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "full_path_reservation": self.full_path_reservation.to_dict(),
            "instance_id": self.instance_id,
            "journal_operation_kind": self.journal_operation_kind,
            "logical_operation_id": self.logical_operation_id,
            "matrix_sha256": self.matrix_sha256,
            "operation_kind": self.operation_kind,
            "schema_version": self.schema_version,
            "seed": self.seed,
            "semantic_role": self.semantic_role,
            "shared_v001": self.shared_v001,
            "slot_sha256": self.slot_sha256,
            "stage": self.stage,
            "stage_ordinal": self.stage_ordinal,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def _sum_resources(operations: tuple[FactorialPotentialOperation, ...]) -> ResourceVector:
    total = ResourceVector()
    for operation in operations:
        total = total + operation.full_path_reservation
    return total


@dataclass(frozen=True)
class ExactFactorialOperationSchedule:
    """Exact full-path upper-bound schedule with permanently zero authority."""

    operations: tuple[FactorialPotentialOperation, ...]
    matrix_sha256: str
    factorial_plan_sha256: str
    task_authority_bundle_sha256: str
    factorial_contract_sha256: str
    execution_authority: str = EXECUTION_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    gpu_exclusive_second_entitlement: int = 0
    cpu_evaluator_second_entitlement: int = 0
    environment_resource_status: str = ENVIRONMENT_RESOURCE_STATUS
    schema_version: int = 1
    schedule_kind: str = "factorial_exact_potential_operation_schedule_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.schedule_kind != (
            "factorial_exact_potential_operation_schedule_v1"
        ):
            raise FactorialOperationScheduleError(
                "unsupported exact operation schedule schema"
            )
        if (
            self.execution_authority != EXECUTION_AUTHORITY
            or self.environment_resource_status != ENVIRONMENT_RESOURCE_STATUS
            or any(
                type(value) is not int or value != 0
                for value in (
                    self.model_call_entitlement,
                    self.evaluator_transaction_entitlement,
                    self.gpu_exclusive_second_entitlement,
                    self.cpu_evaluator_second_entitlement,
                )
            )
        ):
            raise FactorialOperationScheduleError(
                "operation schedule cannot grant execution or resources"
            )
        for value, label in (
            (self.matrix_sha256, "matrix sha256"),
            (self.factorial_plan_sha256, "plan sha256"),
            (self.task_authority_bundle_sha256, "authority bundle sha256"),
            (self.factorial_contract_sha256, "factorial contract sha256"),
        ):
            _sha(value, label)
        if (
            not isinstance(self.operations, tuple)
            or any(type(item) is not FactorialPotentialOperation for item in self.operations)
            or len(self.operations) != 4338
        ):
            raise FactorialOperationScheduleError(
                "operation schedule must contain exactly 4,338 potential stages"
            )
        if any(
            item.matrix_sha256 != self.matrix_sha256
            or item.factorial_plan_sha256 != self.factorial_plan_sha256
            or item.task_authority_bundle_sha256
            != self.task_authority_bundle_sha256
            or item.factorial_contract_sha256 != self.factorial_contract_sha256
            for item in self.operations
        ):
            raise FactorialOperationScheduleError(
                "operation schedule member binding differs"
            )
        identities = tuple(item.logical_operation_id for item in self.operations)
        hashes = tuple(item.sha256 for item in self.operations)
        if len(set(identities)) != len(identities) or len(set(hashes)) != len(hashes):
            raise FactorialOperationScheduleError(
                "operation schedule repeats a potential stage"
            )
        if self.counts != {
            "evaluator": 1566,
            "potential_side_effect_stages": 4338,
            "solution": 1566,
            "update": 1206,
        }:
            raise FactorialOperationScheduleError("operation schedule counts differ")
        if self.full_path_resource_upper_bound != ResourceVector(
            model_calls=2772, evaluator_transactions=1566
        ):
            raise FactorialOperationScheduleError(
                "operation schedule full-path resource count differs"
            )

    @classmethod
    def from_verified_sources(
        cls,
        *,
        matrix: ExactFactorialAttemptMatrix,
        plan: FactorialFormalZeroCallPlan,
        bundle: ExactTaskSeedAuthorityBundle,
        task_authority: FactorialTaskArtifactAuthority,
    ) -> "ExactFactorialOperationSchedule":
        if type(matrix) is not ExactFactorialAttemptMatrix:
            raise FactorialOperationScheduleError("exact attempt matrix is required")
        expected_matrix = ExactFactorialAttemptMatrix.from_verified_sources(
            plan=plan, bundle=bundle, task_authority=task_authority
        )
        # ``ExactFactorialAttemptMatrix.sha256`` serializes all 1,566 slots.  It
        # is a trust-root digest, not a per-stage computation; derive it once to
        # keep this expansion linear rather than accidentally O(slots²).
        expected_matrix_bytes = expected_matrix.canonical_bytes
        expected_matrix_sha256 = hashlib.sha256(expected_matrix_bytes).hexdigest()
        matrix_bytes = matrix.canonical_bytes
        matrix_sha256 = hashlib.sha256(matrix_bytes).hexdigest()
        if (
            matrix != expected_matrix
            or matrix_bytes != expected_matrix_bytes
            or matrix_sha256 != expected_matrix_sha256
        ):
            raise FactorialOperationScheduleError(
                "attempt matrix differs from pinned source replay"
            )
        operations: list[FactorialPotentialOperation] = []
        for slot in expected_matrix.slots:
            if slot.update_operation_expected:
                operations.append(
                    FactorialPotentialOperation.from_slot(
                        matrix_sha256=expected_matrix_sha256,
                        slot=slot,
                        stage="update",
                    )
                )
            operations.extend(
                FactorialPotentialOperation.from_slot(
                    matrix_sha256=expected_matrix_sha256,
                    slot=slot,
                    stage=stage,
                )
                for stage in ("solution", "evaluator")
            )
        return cls(
            operations=tuple(operations),
            matrix_sha256=expected_matrix_sha256,
            factorial_plan_sha256=expected_matrix.factorial_plan_sha256,
            task_authority_bundle_sha256=(
                expected_matrix.task_authority_bundle_sha256
            ),
            factorial_contract_sha256=expected_matrix.factorial_contract_sha256,
        )

    @classmethod
    def verify_from_sources(
        cls,
        schedule: "ExactFactorialOperationSchedule",
        *,
        matrix: ExactFactorialAttemptMatrix,
        plan: FactorialFormalZeroCallPlan,
        bundle: ExactTaskSeedAuthorityBundle,
        task_authority: FactorialTaskArtifactAuthority,
    ) -> "ExactFactorialOperationSchedule":
        if type(schedule) is not ExactFactorialOperationSchedule:
            raise FactorialOperationScheduleError(
                "exact typed operation schedule is required"
            )
        expected = cls.from_verified_sources(
            matrix=matrix,
            plan=plan,
            bundle=bundle,
            task_authority=task_authority,
        )
        if (
            schedule != expected
            or schedule.canonical_bytes != expected.canonical_bytes
            or schedule.sha256 != expected.sha256
        ):
            raise FactorialOperationScheduleError(
                "operation schedule differs from pinned source replay"
            )
        return expected

    @property
    def counts(self) -> dict[str, int]:
        counts = {stage: 0 for stage in _STAGES}
        for operation in self.operations:
            counts[operation.stage] += 1
        return {
            "evaluator": counts["evaluator"],
            "potential_side_effect_stages": len(self.operations),
            "solution": counts["solution"],
            "update": counts["update"],
        }

    @property
    def full_path_resource_upper_bound(self) -> ResourceVector:
        return _sum_resources(self.operations)

    @property
    def per_cell_full_path_caps(self) -> Mapping[str, ResourceVector]:
        by_cell: dict[str, ResourceVector] = {}
        for operation in self.operations:
            by_cell[operation.cell_id] = by_cell.get(
                operation.cell_id, ResourceVector()
            ) + operation.full_path_reservation
        return dict(sorted(by_cell.items()))

    def to_dict(self) -> dict[str, Any]:
        return {
            "counts": self.counts,
            "environment_resource_status": self.environment_resource_status,
            "execution_authority": self.execution_authority,
            "execution_entitlement": {
                "cpu_evaluator_seconds": self.cpu_evaluator_second_entitlement,
                "evaluator_transactions": self.evaluator_transaction_entitlement,
                "gpu_exclusive_seconds": self.gpu_exclusive_second_entitlement,
                "model_calls": self.model_call_entitlement,
            },
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "factorial_plan_sha256": self.factorial_plan_sha256,
            "full_path_resource_upper_bound": (
                self.full_path_resource_upper_bound.to_dict()
            ),
            "matrix_sha256": self.matrix_sha256,
            "operations": [item.to_dict() for item in self.operations],
            "per_cell_full_path_caps": {
                cell_id: value.to_dict()
                for cell_id, value in self.per_cell_full_path_caps.items()
            },
            "schedule_kind": self.schedule_kind,
            "schema_version": self.schema_version,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


__all__ = [
    "ENVIRONMENT_RESOURCE_STATUS",
    "ExactFactorialOperationSchedule",
    "FactorialOperationScheduleError",
    "FactorialPotentialOperation",
]
