"""Zero-call precheck state machine for the four-arm factorial experiment.

This module intentionally has no provider, model, evaluator, subprocess, or
resource-allocation interface.  It verifies either an explicitly fixture-only
schedule or the exact checked-in multi-Benchmark matrix, binds the already
sealed arm-independent v001 trunk, and exercises the v002--v008 arm/phase
barriers with immutable local zero-call receipts.

The precheck is not formal execution authority.  Every persisted record says
that it consumed zero calls and zero evaluator transactions, and construction
fails unless the declared execution authority is ``NOT_GRANTED`` with an
all-zero entitlement.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from ._safe_artifacts import (
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .factorial_contract import (
    DEFAULT_FACTORIAL_MANIFEST,
    factorial_main_arm_variant_projections,
    factorial_main_arm_variant_sha256s,
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from .factorial_policies import ARM_IDS, ARM_POLICY_SPECS
from .factorial_trunk import TaskSeedKey, ZERO_SHA256


PRECHECK_AUTHORITY = "NOT_GRANTED"
PRECHECK_PHASES = ("update", "solution", "evaluation")
PRECHECK_MIN_VERSION = 2
PRECHECK_MAX_VERSION = 8
FIXTURE_ONLY_PLAN_SCOPE = "FIXTURE_ONLY"
FORMAL_EXACT_MATRIX_PLAN_SCOPE = "FORMAL_EXACT_MATRIX_ZERO_CALL_ONLY"
FORMAL_ARM_ORDER_ALGORITHM = "benchmark_seed_latin_rotation_v1"
_RESULT_TRUNK_STATUSES = frozenset({"SUCCESS", "SOLUTION_CONTRACT_REJECTED"})
_ENTITLEMENT_FIELDS = (
    "model_calls",
    "evaluator_transactions",
    "gpu_exclusive_seconds",
    "cpu_evaluator_seconds",
)
_SHA256 = re.compile(r"[0-9a-f]{64}")


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
        raise ValueError("factorial precheck payload is not canonical JSON") from exc


def _reject_constant(value: str) -> None:
    raise ValueError(f"factorial precheck JSON contains forbidden constant {value}")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"factorial precheck JSON repeats field {key!r}")
        result[key] = value
    return result


def _decode_canonical(raw: bytes, *, label: str) -> dict[str, Any]:
    if not isinstance(raw, bytes) or not raw:
        raise ValueError(f"{label} bytes are empty")
    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not strict JSON") from exc
    if not isinstance(payload, dict) or _canonical_bytes(payload) != raw:
        raise ValueError(f"{label} is not canonical")
    return payload


def _sha(value: Any, label: str, *, allow_zero: bool = False) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid factorial precheck {label}")
    if not allow_zero and value == ZERO_SHA256:
        raise ValueError(f"empty factorial precheck {label}")
    return value


def _hash(payload: object) -> str:
    return hashlib.sha256(_canonical_bytes(payload)).hexdigest()


def _version_label(version: int) -> str:
    if (
        type(version) is not int
        or not PRECHECK_MIN_VERSION <= version <= PRECHECK_MAX_VERSION
    ):
        raise ValueError("factorial precheck version must be between v002 and v008")
    return f"v{version:03d}"


def _arm_policy_projection() -> list[dict[str, Any]]:
    return [
        {
            "arm_id": arm_id,
            "architecture_frozen": ARM_POLICY_SPECS[arm_id].architecture_frozen,
            "minimum_material_axis_changes": (
                ARM_POLICY_SPECS[arm_id].minimum_material_axis_changes
            ),
            "require_lineage_unique": ARM_POLICY_SPECS[arm_id].require_lineage_unique,
            "update_kind": ARM_POLICY_SPECS[arm_id].update_kind,
            "update_policy": ARM_POLICY_SPECS[arm_id].update_policy,
        }
        for arm_id in ARM_IDS
    ]


def factorial_arm_policy_sha256() -> str:
    """Return the frozen typed four-arm policy-table hash."""

    return _hash(_arm_policy_projection())


def rotated_arm_order(offset: int) -> tuple[str, ...]:
    """Return one canonical Latin rotation of the four arm identities."""

    if type(offset) is not int:
        raise ValueError("factorial arm rotation offset must be an integer")
    index = offset % len(ARM_IDS)
    return tuple((*ARM_IDS[index:], *ARM_IDS[:index]))


def task_seed_arm_order(key: TaskSeedKey) -> tuple[str, ...]:
    """Derive the frozen Latin rotation from the complete task×seed key."""

    if not isinstance(key, TaskSeedKey):
        raise ValueError("factorial arm ordering requires a TaskSeedKey")
    return rotated_arm_order(int(key.sha256[:16], 16))


def _is_arm_rotation(value: Sequence[str]) -> bool:
    if isinstance(value, (str, bytes)) or len(value) != len(ARM_IDS):
        return False
    candidate = tuple(value)
    return any(candidate == rotated_arm_order(offset) for offset in range(len(ARM_IDS)))


@dataclass(frozen=True)
class FactorialTaskSeedSchedule:
    """One independent task×seed block in the zero-call schedule."""

    key: TaskSeedKey
    final_version: int
    arm_order: tuple[str, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.key, TaskSeedKey):
            raise ValueError("factorial schedule requires a typed TaskSeedKey")
        _version_label(self.final_version)
        if not isinstance(self.arm_order, tuple) or not _is_arm_rotation(
            self.arm_order
        ):
            raise ValueError("factorial schedule arm order must be one Latin rotation")
        if self.arm_order != task_seed_arm_order(self.key):
            raise ValueError(
                "factorial schedule arm order differs from the task/seed hash"
            )

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_order": list(self.arm_order),
            "final_version": self.final_version,
            "task_seed_key": self.key.core_payload(),
            "task_seed_key_sha256": self.key.sha256,
        }


@dataclass(frozen=True)
class FactorialZeroCallPlan:
    """Arbitrary multi-Benchmark fixture plan with no execution entitlement.

    This permissive plan exists only for unit/fixture state-machine exercise.
    It is deliberately not evidence that the checked-in formal matrix, arm
    policies, or arm variants were bound.  Use
    :class:`FactorialFormalZeroCallPlan` for that audit surface.
    """

    schedules: tuple[FactorialTaskSeedSchedule, ...]
    execution_authority: str = PRECHECK_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    gpu_exclusive_second_entitlement: int = 0
    cpu_evaluator_second_entitlement: int = 0
    plan_scope: str = FIXTURE_ONLY_PLAN_SCOPE
    schema_version: int = 1
    plan_kind: str = "moss_four_arm_factorial_zero_call_precheck_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.plan_kind != (
            "moss_four_arm_factorial_zero_call_precheck_v1"
        ):
            raise ValueError("unsupported factorial zero-call plan schema")
        if self.plan_scope != FIXTURE_ONLY_PLAN_SCOPE:
            raise ValueError("arbitrary factorial zero-call plan is fixture-only")
        if self.execution_authority != PRECHECK_AUTHORITY:
            raise ValueError("factorial precheck refuses nonzero execution authority")
        entitlement_values = (
            self.model_call_entitlement,
            self.evaluator_transaction_entitlement,
            self.gpu_exclusive_second_entitlement,
            self.cpu_evaluator_second_entitlement,
        )
        if any(type(value) is not int or value != 0 for value in entitlement_values):
            raise ValueError("factorial precheck refuses nonzero execution entitlement")
        if not isinstance(self.schedules, tuple) or not self.schedules:
            raise ValueError("factorial precheck requires task/seed schedules")
        if any(
            not isinstance(item, FactorialTaskSeedSchedule)
            for item in self.schedules
        ):
            raise ValueError("factorial precheck schedule is not typed")
        keys = tuple(item.key.sha256 for item in self.schedules)
        if len(keys) != len(set(keys)):
            raise ValueError("factorial precheck repeats a task/seed identity")
        if len({item.key.suite for item in self.schedules}) < 2:
            raise ValueError("factorial precheck requires at least two Benchmarks")
        contract_hashes = {
            item.key.factorial_contract_sha256 for item in self.schedules
        }
        if len(contract_hashes) != 1:
            raise ValueError("factorial precheck task/seed contract bindings differ")

    @property
    def arm_policy_sha256(self) -> str:
        return factorial_arm_policy_sha256()

    @property
    def execution_entitlement(self) -> dict[str, int]:
        return {
            "cpu_evaluator_seconds": self.cpu_evaluator_second_entitlement,
            "evaluator_transactions": self.evaluator_transaction_entitlement,
            "gpu_exclusive_seconds": self.gpu_exclusive_second_entitlement,
            "model_calls": self.model_call_entitlement,
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_policies": _arm_policy_projection(),
            "arm_policy_sha256": self.arm_policy_sha256,
            "execution_authority": self.execution_authority,
            "execution_entitlement": self.execution_entitlement,
            "plan_kind": self.plan_kind,
            "plan_scope": self.plan_scope,
            "schedules": [item.to_dict() for item in self.schedules],
            "schema_version": self.schema_version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def from_bytes(
        cls, raw: bytes, *, expected_sha256: str | None = None
    ) -> "FactorialZeroCallPlan":
        """Strictly replay canonical checked-in or persisted plan bytes."""

        payload = _decode_canonical(raw, label="factorial zero-call precheck plan")
        _required_fields(
            payload,
            {
                "arm_policies",
                "arm_policy_sha256",
                "execution_authority",
                "execution_entitlement",
                "plan_kind",
                "plan_scope",
                "schedules",
                "schema_version",
            },
            "factorial zero-call precheck plan",
        )
        if payload["arm_policies"] != _arm_policy_projection() or payload[
            "arm_policy_sha256"
        ] != factorial_arm_policy_sha256():
            raise ValueError("factorial zero-call plan arm policies differ")
        entitlement = payload["execution_entitlement"]
        if not isinstance(entitlement, dict) or set(entitlement) != set(
            _ENTITLEMENT_FIELDS
        ):
            raise ValueError("factorial zero-call plan entitlement fields differ")
        schedules_payload = payload["schedules"]
        if not isinstance(schedules_payload, list):
            raise ValueError("factorial zero-call plan schedules differ")
        schedules: list[FactorialTaskSeedSchedule] = []
        for item in schedules_payload:
            _required_fields(
                item,
                {
                    "arm_order",
                    "final_version",
                    "task_seed_key",
                    "task_seed_key_sha256",
                },
                "factorial task/seed schedule",
            )
            key_payload = item["task_seed_key"]
            if not isinstance(key_payload, dict):
                raise ValueError("factorial schedule TaskSeedKey differs")
            key_bytes = _canonical_bytes(key_payload)
            key = TaskSeedKey.from_bytes(
                key_bytes, expected_sha256=item["task_seed_key_sha256"]
            )
            schedules.append(
                FactorialTaskSeedSchedule(
                    key=key,
                    final_version=item["final_version"],
                    arm_order=tuple(item["arm_order"]),
                )
            )
        plan = cls(
            schedules=tuple(schedules),
            execution_authority=payload["execution_authority"],
            model_call_entitlement=entitlement["model_calls"],
            evaluator_transaction_entitlement=entitlement[
                "evaluator_transactions"
            ],
            gpu_exclusive_second_entitlement=entitlement[
                "gpu_exclusive_seconds"
            ],
            cpu_evaluator_second_entitlement=entitlement[
                "cpu_evaluator_seconds"
            ],
            plan_scope=payload["plan_scope"],
            schema_version=payload["schema_version"],
            plan_kind=payload["plan_kind"],
        )
        if plan.canonical_bytes != raw:
            raise ValueError("factorial zero-call plan replay differs")
        if expected_sha256 is not None:
            _sha(expected_sha256, "expected plan sha256")
            if plan.sha256 != expected_sha256:
                raise ValueError("factorial zero-call plan hash differs")
        return plan

    def schedule_for(self, key: TaskSeedKey) -> FactorialTaskSeedSchedule:
        if not isinstance(key, TaskSeedKey):
            raise ValueError("factorial precheck lookup requires a TaskSeedKey")
        matches = [item for item in self.schedules if item.key.sha256 == key.sha256]
        if len(matches) != 1 or matches[0].key != key:
            raise ValueError("task/seed is outside the frozen factorial plan")
        return matches[0]


def _formal_arm_order(
    *, task_index: int, seed_index: int
) -> tuple[str, ...]:
    if type(task_index) is not int or task_index < 0:
        raise ValueError("formal factorial task index differs")
    if type(seed_index) is not int or seed_index < 0:
        raise ValueError("formal factorial seed index differs")
    return rotated_arm_order(task_index + seed_index)


@dataclass(frozen=True)
class FactorialFormalTaskSeedSchedule:
    """One exact checked-in main-matrix task×seed cell.

    Unlike :class:`FactorialTaskSeedSchedule`, arm order is not chosen by a
    task-binding hash that can accidentally imbalance a small sample.  It is a
    preregistered Latin rotation over manifest task and seed positions.
    """

    key: TaskSeedKey
    task_unit: str
    task_ordinal: int
    task_index: int
    seed_index: int
    final_version: int
    arm_order: tuple[str, ...]

    def __post_init__(self) -> None:
        if type(self.final_version) is not int or not 1 <= self.final_version <= 999:
            raise ValueError("formal factorial final version differs")
        if not isinstance(self.key, TaskSeedKey):
            raise ValueError("formal factorial schedule requires a TaskSeedKey")
        if not isinstance(self.task_unit, str) or not self.task_unit:
            raise ValueError("formal factorial task unit differs")
        if type(self.task_ordinal) is not int or self.task_ordinal < 1:
            raise ValueError("formal factorial task ordinal differs")
        if not isinstance(self.arm_order, tuple) or not _is_arm_rotation(
            self.arm_order
        ):
            raise ValueError("formal factorial arm order must be a Latin rotation")
        if self.arm_order != _formal_arm_order(
            task_index=self.task_index, seed_index=self.seed_index
        ):
            raise ValueError("formal factorial arm order differs from frozen design")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_order": list(self.arm_order),
            "final_version": self.final_version,
            "seed_index": self.seed_index,
            "task_index": self.task_index,
            "task_ordinal": self.task_ordinal,
            "task_seed_key": self.key.core_payload(),
            "task_seed_key_sha256": self.key.sha256,
            "task_unit": self.task_unit,
        }


def _formal_arm_balance_projection(
    schedules: Sequence[FactorialFormalTaskSeedSchedule],
) -> dict[str, Any]:
    groups: dict[tuple[str, int], list[FactorialFormalTaskSeedSchedule]] = {}
    for item in schedules:
        if not isinstance(item, FactorialFormalTaskSeedSchedule):
            raise ValueError("formal factorial balance input is not typed")
        groups.setdefault((item.key.suite, item.key.seed), []).append(item)
    projection: list[dict[str, Any]] = []
    maximum_imbalance = 0
    for (benchmark_id, seed), items in groups.items():
        counts = {
            arm_id: [0 for _ in ARM_IDS]
            for arm_id in ARM_IDS
        }
        for item in items:
            for position, arm_id in enumerate(item.arm_order):
                counts[arm_id][position] += 1
        flattened = [value for arm in ARM_IDS for value in counts[arm]]
        imbalance = max(flattened) - min(flattened)
        maximum_imbalance = max(maximum_imbalance, imbalance)
        projection.append(
            {
                "benchmark_id": benchmark_id,
                "counts_by_arm_and_position": [
                    {
                        "arm_id": arm_id,
                        "position_counts": counts[arm_id],
                    }
                    for arm_id in ARM_IDS
                ],
                "maximum_cell_imbalance": imbalance,
                "seed": seed,
                "task_count": len(items),
            }
        )
    return {
        "algorithm": FORMAL_ARM_ORDER_ALGORITHM,
        "groups": projection,
        "maximum_cell_imbalance": maximum_imbalance,
    }


def _formal_manifest_bindings(
    manifest_path: Path,
) -> tuple[
    dict[str, Any],
    str,
    tuple[dict[str, Any], ...],
    str,
    tuple[tuple[str, str], ...],
]:
    resolved = manifest_path.resolve(strict=True)
    if resolved != DEFAULT_FACTORIAL_MANIFEST.resolve(strict=True):
        raise ValueError("formal factorial plan requires checked-in manifest path")
    payload = verify_factorial_contract(resolved)
    raw = resolved.read_bytes()
    matrix = factorial_main_matrix_projection(payload)
    variant_sha256s = factorial_main_arm_variant_sha256s(payload)
    return (
        payload,
        hashlib.sha256(raw).hexdigest(),
        matrix,
        _hash(matrix),
        tuple((arm_id, variant_sha256s[arm_id]) for arm_id in ARM_IDS),
    )


@dataclass(frozen=True)
class FactorialFormalZeroCallPlan:
    """Exact checked-in factorial matrix binding with zero execution authority.

    Construction and replay both reverify ``wide_meta_factorial_v1.json`` and
    require all 126 main task×seed cells.  This closes the arbitrary fixture
    schedule gap, but it intentionally remains a precheck artifact: provider,
    evaluator, score-boundary, budget, and execution authority gates are still
    outside this class and still closed.
    """

    schedules: tuple[FactorialFormalTaskSeedSchedule, ...]
    factorial_manifest_sha256: str
    factorial_contract_sha256: str
    factorial_matrix_sha256: str
    bound_arm_policy_sha256: str
    arm_variant_sha256s: tuple[tuple[str, str], ...]
    task_authority_bundle_sha256: str
    execution_authority: str = PRECHECK_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    gpu_exclusive_second_entitlement: int = 0
    cpu_evaluator_second_entitlement: int = 0
    plan_scope: str = FORMAL_EXACT_MATRIX_PLAN_SCOPE
    schema_version: int = 1
    plan_kind: str = "moss_four_arm_factorial_formal_zero_call_plan_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.plan_kind != (
            "moss_four_arm_factorial_formal_zero_call_plan_v1"
        ):
            raise ValueError("unsupported formal factorial zero-call plan schema")
        if self.plan_scope != FORMAL_EXACT_MATRIX_PLAN_SCOPE:
            raise ValueError("formal factorial plan scope differs")
        if self.execution_authority != PRECHECK_AUTHORITY:
            raise ValueError("formal factorial plan refuses execution authority")
        entitlements = (
            self.model_call_entitlement,
            self.evaluator_transaction_entitlement,
            self.gpu_exclusive_second_entitlement,
            self.cpu_evaluator_second_entitlement,
        )
        if any(type(value) is not int or value != 0 for value in entitlements):
            raise ValueError("formal factorial plan refuses execution entitlement")
        for value, label in (
            (self.factorial_manifest_sha256, "manifest sha256"),
            (self.factorial_contract_sha256, "contract sha256"),
            (self.factorial_matrix_sha256, "matrix sha256"),
            (self.bound_arm_policy_sha256, "arm policy sha256"),
            (self.task_authority_bundle_sha256, "task authority bundle sha256"),
        ):
            _sha(value, f"formal factorial {label}")
        if tuple(arm_id for arm_id, _ in self.arm_variant_sha256s) != ARM_IDS:
            raise ValueError("formal factorial arm variant coverage or order differs")
        for _arm_id, value in self.arm_variant_sha256s:
            _sha(value, "formal factorial arm variant sha256")
        if not isinstance(self.schedules, tuple) or any(
            not isinstance(item, FactorialFormalTaskSeedSchedule)
            for item in self.schedules
        ):
            raise ValueError("formal factorial schedules are not typed")
        self._verify_internal_bindings()

    @classmethod
    def _from_task_seed_keys_for_fixture(
        cls,
        task_seed_keys: Sequence[TaskSeedKey],
        *,
        task_authority_bundle_sha256: str,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialFormalZeroCallPlan":
        """Internal constructor; public formal code must supply an authority bundle."""

        payload, manifest_sha, matrix, matrix_sha, variant_hashes = (
            _formal_manifest_bindings(manifest_path)
        )
        if isinstance(task_seed_keys, (str, bytes)) or any(
            not isinstance(item, TaskSeedKey) for item in task_seed_keys
        ):
            raise ValueError("formal factorial task keys are not typed")
        by_identity: dict[tuple[str, str, int], TaskSeedKey] = {}
        for key in task_seed_keys:
            identity = (key.suite, key.instance_id, key.seed)
            if identity in by_identity:
                raise ValueError("formal factorial task keys repeat an identity")
            by_identity[identity] = key
        expected_identities = {
            (item["benchmark_id"], item["instance_id"], item["seed"])
            for item in matrix
        }
        if set(by_identity) != expected_identities:
            missing = expected_identities - set(by_identity)
            extra = set(by_identity) - expected_identities
            raise ValueError(
                "formal factorial task key matrix differs: "
                f"missing={len(missing)}, extra={len(extra)}"
            )
        contract_sha = payload["contract_digest"]
        schedules: list[FactorialFormalTaskSeedSchedule] = []
        for item in matrix:
            identity = (item["benchmark_id"], item["instance_id"], item["seed"])
            key = by_identity[identity]
            if key.factorial_contract_sha256 != contract_sha:
                raise ValueError("formal factorial task key contract binding differs")
            schedules.append(
                FactorialFormalTaskSeedSchedule(
                    key=key,
                    task_unit=item["task_unit"],
                    task_ordinal=item["task_ordinal"],
                    task_index=item["task_index"],
                    seed_index=item["seed_index"],
                    final_version=item["final_version"],
                    arm_order=_formal_arm_order(
                        task_index=item["task_index"],
                        seed_index=item["seed_index"],
                    ),
                )
            )
        return cls(
            schedules=tuple(schedules),
            factorial_manifest_sha256=manifest_sha,
            factorial_contract_sha256=contract_sha,
            factorial_matrix_sha256=matrix_sha,
            bound_arm_policy_sha256=factorial_arm_policy_sha256(),
            arm_variant_sha256s=variant_hashes,
            task_authority_bundle_sha256=task_authority_bundle_sha256,
        )

    @classmethod
    def from_authority_bundle(
        cls,
        bundle: Any,
        *,
        task_authority: Any,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
    ) -> "FactorialFormalZeroCallPlan":
        """Build the exact plan only after pinned-source authority replay."""

        from .factorial_task_authority import (
            ExactTaskSeedAuthorityBundle,
            FactorialTaskArtifactAuthority,
        )

        if type(bundle) is not ExactTaskSeedAuthorityBundle:
            raise ValueError("formal factorial plan requires a task authority bundle")
        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise ValueError("formal factorial plan requires a source authority")
        replayed = ExactTaskSeedAuthorityBundle.from_canonical_bytes(
            bundle.canonical_bytes, expected_sha256=bundle.sha256
        )
        if replayed != bundle:
            raise ValueError("formal factorial task authority bundle replay differs")
        replayed = task_authority.verify_exact_bundle(replayed)
        return cls._from_task_seed_keys_for_fixture(
            replayed.task_seed_keys,
            task_authority_bundle_sha256=replayed.sha256,
            manifest_path=manifest_path,
        )

    def _verify_internal_bindings(self) -> None:
        payload, manifest_sha, matrix, matrix_sha, variant_hashes = (
            _formal_manifest_bindings(DEFAULT_FACTORIAL_MANIFEST)
        )
        if (
            self.factorial_manifest_sha256 != manifest_sha
            or self.factorial_contract_sha256 != payload["contract_digest"]
            or self.factorial_matrix_sha256 != matrix_sha
            or self.bound_arm_policy_sha256 != factorial_arm_policy_sha256()
            or self.arm_variant_sha256s != variant_hashes
        ):
            raise ValueError("formal factorial manifest/policy/variant binding differs")
        _sha(
            self.task_authority_bundle_sha256,
            "formal factorial task authority bundle sha256",
        )
        if len(self.schedules) != len(matrix):
            raise ValueError("formal factorial schedule count differs")
        for schedule, expected in zip(self.schedules, matrix, strict=True):
            if (
                schedule.key.suite != expected["benchmark_id"]
                or schedule.key.instance_id != expected["instance_id"]
                or schedule.key.seed != expected["seed"]
                or schedule.key.factorial_contract_sha256
                != payload["contract_digest"]
                or schedule.task_unit != expected["task_unit"]
                or schedule.task_ordinal != expected["task_ordinal"]
                or schedule.task_index != expected["task_index"]
                or schedule.seed_index != expected["seed_index"]
                or schedule.final_version != expected["final_version"]
                or schedule.arm_order
                != _formal_arm_order(
                    task_index=expected["task_index"],
                    seed_index=expected["seed_index"],
                )
            ):
                raise ValueError("formal factorial schedule identity/order differs")
        key_hashes = tuple(item.key.sha256 for item in self.schedules)
        if len(key_hashes) != len(set(key_hashes)):
            raise ValueError("formal factorial schedule repeats a task key")
        balance = _formal_arm_balance_projection(self.schedules)
        if balance["maximum_cell_imbalance"] > 1:
            raise ValueError("formal factorial arm ordering is imbalanced")

    @property
    def execution_entitlement(self) -> dict[str, int]:
        return {
            "cpu_evaluator_seconds": self.cpu_evaluator_second_entitlement,
            "evaluator_transactions": self.evaluator_transaction_entitlement,
            "gpu_exclusive_seconds": self.gpu_exclusive_second_entitlement,
            "model_calls": self.model_call_entitlement,
        }

    @property
    def arm_order_balance(self) -> dict[str, Any]:
        return _formal_arm_balance_projection(self.schedules)

    @property
    def arm_policy_sha256(self) -> str:
        """Expose the exact bound policy through the barrier-plan interface."""

        return self.bound_arm_policy_sha256

    def to_dict(self) -> dict[str, Any]:
        payload = verify_factorial_contract(DEFAULT_FACTORIAL_MANIFEST)
        balance = self.arm_order_balance
        return {
            "arm_order_algorithm": FORMAL_ARM_ORDER_ALGORITHM,
            "arm_order_balance": balance,
            "arm_order_balance_sha256": _hash(balance),
            "arm_policies": _arm_policy_projection(),
            "arm_policy_sha256": self.bound_arm_policy_sha256,
            "arm_variant_projections": list(
                factorial_main_arm_variant_projections(payload)
            ),
            "arm_variant_sha256s": dict(self.arm_variant_sha256s),
            "execution_authority": self.execution_authority,
            "execution_entitlement": self.execution_entitlement,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "factorial_manifest_sha256": self.factorial_manifest_sha256,
            "factorial_matrix_sha256": self.factorial_matrix_sha256,
            "formal_execution_ready": False,
            "plan_kind": self.plan_kind,
            "plan_scope": self.plan_scope,
            "schedules": [item.to_dict() for item in self.schedules],
            "schema_version": self.schema_version,
            "task_authority_bundle_sha256": self.task_authority_bundle_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @classmethod
    def _from_bytes_unverified_source(
        cls,
        raw: bytes,
        *,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
        expected_sha256: str | None = None,
    ) -> "FactorialFormalZeroCallPlan":
        """Replay DTO/manifest integrity without claiming source provenance."""

        payload = _decode_canonical(raw, label="formal factorial zero-call plan")
        _required_fields(
            payload,
            {
                "arm_order_algorithm",
                "arm_order_balance",
                "arm_order_balance_sha256",
                "arm_policies",
                "arm_policy_sha256",
                "arm_variant_projections",
                "arm_variant_sha256s",
                "execution_authority",
                "execution_entitlement",
                "factorial_contract_sha256",
                "factorial_manifest_sha256",
                "factorial_matrix_sha256",
                "formal_execution_ready",
                "plan_kind",
                "plan_scope",
                "schedules",
                "schema_version",
                "task_authority_bundle_sha256",
            },
            "formal factorial zero-call plan",
        )
        verified, manifest_sha, _matrix, matrix_sha, variant_hashes = (
            _formal_manifest_bindings(manifest_path)
        )
        if payload["arm_order_algorithm"] != FORMAL_ARM_ORDER_ALGORITHM:
            raise ValueError("formal factorial arm order algorithm differs")
        if (
            payload["arm_policies"] != _arm_policy_projection()
            or payload["arm_policy_sha256"] != factorial_arm_policy_sha256()
            or payload["arm_variant_projections"]
            != list(factorial_main_arm_variant_projections(verified))
            or payload["arm_variant_sha256s"] != dict(variant_hashes)
            or payload["factorial_manifest_sha256"] != manifest_sha
            or payload["factorial_contract_sha256"]
            != verified["contract_digest"]
            or payload["factorial_matrix_sha256"] != matrix_sha
            or payload["formal_execution_ready"] is not False
        ):
            raise ValueError("formal factorial manifest/policy/variant binding differs")
        entitlement = payload["execution_entitlement"]
        if not isinstance(entitlement, dict) or set(entitlement) != set(
            _ENTITLEMENT_FIELDS
        ):
            raise ValueError("formal factorial entitlement fields differ")
        raw_schedules = payload["schedules"]
        if not isinstance(raw_schedules, list):
            raise ValueError("formal factorial schedules differ")
        schedules: list[FactorialFormalTaskSeedSchedule] = []
        for item in raw_schedules:
            _required_fields(
                item,
                {
                    "arm_order",
                    "final_version",
                    "seed_index",
                    "task_index",
                    "task_ordinal",
                    "task_seed_key",
                    "task_seed_key_sha256",
                    "task_unit",
                },
                "formal factorial task/seed schedule",
            )
            key_payload = item["task_seed_key"]
            if not isinstance(key_payload, dict):
                raise ValueError("formal factorial TaskSeedKey differs")
            key = TaskSeedKey.from_bytes(
                _canonical_bytes(key_payload),
                expected_sha256=item["task_seed_key_sha256"],
            )
            arm_order = item["arm_order"]
            if not isinstance(arm_order, list):
                raise ValueError("formal factorial arm order differs")
            schedules.append(
                FactorialFormalTaskSeedSchedule(
                    key=key,
                    task_unit=item["task_unit"],
                    task_ordinal=item["task_ordinal"],
                    task_index=item["task_index"],
                    seed_index=item["seed_index"],
                    final_version=item["final_version"],
                    arm_order=tuple(arm_order),
                )
            )
        plan = cls(
            schedules=tuple(schedules),
            factorial_manifest_sha256=payload["factorial_manifest_sha256"],
            factorial_contract_sha256=payload["factorial_contract_sha256"],
            factorial_matrix_sha256=payload["factorial_matrix_sha256"],
            bound_arm_policy_sha256=payload["arm_policy_sha256"],
            arm_variant_sha256s=tuple(
                (arm_id, payload["arm_variant_sha256s"].get(arm_id))
                for arm_id in ARM_IDS
            ),
            task_authority_bundle_sha256=payload[
                "task_authority_bundle_sha256"
            ],
            execution_authority=payload["execution_authority"],
            model_call_entitlement=entitlement["model_calls"],
            evaluator_transaction_entitlement=entitlement[
                "evaluator_transactions"
            ],
            gpu_exclusive_second_entitlement=entitlement[
                "gpu_exclusive_seconds"
            ],
            cpu_evaluator_second_entitlement=entitlement[
                "cpu_evaluator_seconds"
            ],
            plan_scope=payload["plan_scope"],
            schema_version=payload["schema_version"],
            plan_kind=payload["plan_kind"],
        )
        if payload["arm_order_balance"] != plan.arm_order_balance or payload[
            "arm_order_balance_sha256"
        ] != _hash(plan.arm_order_balance):
            raise ValueError("formal factorial arm balance audit differs")
        if plan.canonical_bytes != raw:
            raise ValueError("formal factorial zero-call plan replay differs")
        if expected_sha256 is not None:
            _sha(expected_sha256, "expected formal factorial plan sha256")
            if plan.sha256 != expected_sha256:
                raise ValueError("formal factorial zero-call plan hash differs")
        return plan

    @classmethod
    def from_bytes(
        cls,
        raw: bytes,
        *,
        task_authority: Any,
        task_authority_bundle: Any,
        manifest_path: Path = DEFAULT_FACTORIAL_MANIFEST,
        expected_sha256: str | None = None,
    ) -> "FactorialFormalZeroCallPlan":
        """Replay a persisted plan and rederive its pinned-source authority."""

        from .factorial_task_authority import (
            ExactTaskSeedAuthorityBundle,
            FactorialTaskArtifactAuthority,
        )

        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise ValueError("formal factorial plan replay requires source authority")
        if type(task_authority_bundle) is not ExactTaskSeedAuthorityBundle:
            raise ValueError(
                "formal factorial plan replay requires exact authority bundle"
            )
        plan = cls._from_bytes_unverified_source(
            raw,
            manifest_path=manifest_path,
            expected_sha256=expected_sha256,
        )
        verified_bundle = task_authority.verify_exact_bundle(
            task_authority_bundle
        )
        if (
            plan.task_authority_bundle_sha256 != verified_bundle.sha256
            or tuple(item.key for item in plan.schedules)
            != verified_bundle.task_seed_keys
        ):
            raise ValueError("formal factorial plan/source authority replay differs")
        return plan

    def schedule_for(self, key: TaskSeedKey) -> FactorialFormalTaskSeedSchedule:
        if not isinstance(key, TaskSeedKey):
            raise ValueError("formal factorial lookup requires a TaskSeedKey")
        matches = [item for item in self.schedules if item.key.sha256 == key.sha256]
        if len(matches) != 1 or matches[0].key != key:
            raise ValueError("task/seed is outside the exact formal factorial plan")
        return matches[0]

class FactorialTrunkReader(Protocol):
    """Read-only subset of :class:`FactorialTrunkArchive` used by precheck."""

    def load_intent(self, key_sha256: str) -> Any: ...

    def load_canonical_compile(self, key_sha256: str) -> Any: ...

    def load_equivalence(self, key_sha256: str) -> Any: ...

    def load_trunk(self, key_sha256: str) -> Any: ...

    def load_fork(self, key_sha256: str, arm_id: str) -> Any: ...


@dataclass(frozen=True)
class FormalV001ForkBindingReceipt:
    """Exact-plan audit binding for all four already-sealed v001 forks."""

    formal_plan_sha256: str
    task_seed_key_sha256: str
    factorial_contract_sha256: str
    arm_variant_sha256s: tuple[tuple[str, str], ...]
    arm_fork_receipt_sha256s: tuple[tuple[str, str], ...]
    schema_version: int = 1
    receipt_kind: str = "formal_v001_fork_binding_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "formal_v001_fork_binding_receipt_v1"
        ):
            raise ValueError("unsupported formal v001 fork binding receipt")
        for value, label in (
            (self.formal_plan_sha256, "formal plan sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.factorial_contract_sha256, "factorial contract sha256"),
        ):
            _sha(value, label)
        for mapping, label in (
            (self.arm_variant_sha256s, "arm variant sha256"),
            (self.arm_fork_receipt_sha256s, "arm fork receipt sha256"),
        ):
            if tuple(arm_id for arm_id, _ in mapping) != ARM_IDS:
                raise ValueError(f"formal v001 {label} coverage or order differs")
            for _arm_id, value in mapping:
                _sha(value, label)

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_fork_receipt_sha256s": dict(self.arm_fork_receipt_sha256s),
            "arm_variant_sha256s": dict(self.arm_variant_sha256s),
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "formal_plan_sha256": self.formal_plan_sha256,
            "receipt_kind": self.receipt_kind,
            "schema_version": self.schema_version,
            "task_seed_key_sha256": self.task_seed_key_sha256,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


def verify_formal_v001_fork_bindings(
    *,
    plan: FactorialFormalZeroCallPlan,
    trunk_archive: FactorialTrunkReader,
    key: TaskSeedKey,
) -> FormalV001ForkBindingReceipt:
    """Mechanically bind all v001 fork metadata to the exact formal plan.

    This is read-only zero-call audit evidence.  The dedicated exact-plan
    barrier controller invokes it at every v001 bind/replay; the receipt still
    cannot grant execution authority.
    """

    if not isinstance(plan, FactorialFormalZeroCallPlan):
        raise ValueError("formal v001 fork verification requires an exact plan")
    plan.schedule_for(key)
    if key.factorial_contract_sha256 != plan.factorial_contract_sha256:
        raise ValueError("formal v001 fork task contract differs")
    expected_variants = dict(plan.arm_variant_sha256s)
    fork_hashes: list[tuple[str, str]] = []
    for arm_id in ARM_IDS:
        fork = trunk_archive.load_fork(key.sha256, arm_id)
        if (
            getattr(fork, "task_seed_key_sha256", None) != key.sha256
            or getattr(fork, "arm_id", None) != arm_id
            or getattr(fork, "arm_cell_id", None) != key.arm_cell_id(arm_id)
            or getattr(fork, "arm_variant_sha256", None)
            != expected_variants[arm_id]
            or getattr(fork, "arm_contract_sha256", None)
            != plan.factorial_contract_sha256
        ):
            raise ValueError("formal v001 fork variant/contract differs")
        fork_hashes.append(
            (arm_id, _sha(getattr(fork, "sha256", None), "arm fork receipt sha256"))
        )
    return FormalV001ForkBindingReceipt(
        formal_plan_sha256=plan.sha256,
        task_seed_key_sha256=key.sha256,
        factorial_contract_sha256=plan.factorial_contract_sha256,
        arm_variant_sha256s=plan.arm_variant_sha256s,
        arm_fork_receipt_sha256s=tuple(fork_hashes),
    )


@dataclass(frozen=True)
class V001PrecheckReceipt:
    plan_sha256: str
    task_seed_key_sha256: str
    intent_sha256: str
    canonical_compile_contract_sha256: str
    compile_equivalence_receipt_sha256: str
    trunk_receipt_sha256: str
    trunk_status: str
    arm_policy_sha256: str
    arm_fork_receipts: tuple[tuple[str, str], ...]
    model_calls: int = 0
    evaluator_transactions: int = 0
    schema_version: int = 1
    receipt_kind: str = "shared_v001_precheck_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "shared_v001_precheck_receipt_v1"
        ):
            raise ValueError("unsupported shared-v001 precheck receipt")
        for value, label in (
            (self.plan_sha256, "plan sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.intent_sha256, "intent sha256"),
            (
                self.canonical_compile_contract_sha256,
                "canonical compile contract sha256",
            ),
            (
                self.compile_equivalence_receipt_sha256,
                "compile equivalence receipt sha256",
            ),
            (self.trunk_receipt_sha256, "trunk receipt sha256"),
            (self.arm_policy_sha256, "arm policy sha256"),
        ):
            _sha(value, label)
        if self.trunk_status not in _RESULT_TRUNK_STATUSES:
            raise ValueError("shared-v001 precheck trunk is not a result trunk")
        if tuple(arm for arm, _ in self.arm_fork_receipts) != tuple(ARM_IDS):
            raise ValueError("shared-v001 precheck fork coverage or order differs")
        fork_hashes = tuple(value for _, value in self.arm_fork_receipts)
        if len(fork_hashes) != len(set(fork_hashes)):
            raise ValueError("shared-v001 precheck fork receipts are not distinct")
        for value in fork_hashes:
            _sha(value, "arm fork receipt sha256")
        if self.model_calls != 0 or self.evaluator_transactions != 0:
            raise ValueError("shared-v001 precheck receipt cannot record calls")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_fork_receipts": {
                arm_id: sha256 for arm_id, sha256 in self.arm_fork_receipts
            },
            "arm_policy_sha256": self.arm_policy_sha256,
            "canonical_compile_contract_sha256": (
                self.canonical_compile_contract_sha256
            ),
            "compile_equivalence_receipt_sha256": (
                self.compile_equivalence_receipt_sha256
            ),
            "evaluator_transactions": self.evaluator_transactions,
            "intent_sha256": self.intent_sha256,
            "model_calls": self.model_calls,
            "plan_sha256": self.plan_sha256,
            "receipt_kind": self.receipt_kind,
            "schema_version": self.schema_version,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "trunk_receipt_sha256": self.trunk_receipt_sha256,
            "trunk_status": self.trunk_status,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class PrecheckPhaseReceipt:
    plan_sha256: str
    task_seed_key_sha256: str
    version: str
    phase: str
    arm_id: str
    arm_position: int
    arm_update_policy: str
    prerequisite_barrier_sha256: str
    fixture_evidence_sha256: str
    operation_id: str
    model_calls: int = 0
    evaluator_transactions: int = 0
    schema_version: int = 1
    receipt_kind: str = "factorial_phase_precheck_receipt_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_phase_precheck_receipt_v1"
        ):
            raise ValueError("unsupported factorial phase precheck receipt")
        for value, label in (
            (self.plan_sha256, "plan sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.prerequisite_barrier_sha256, "prerequisite barrier sha256"),
            (self.fixture_evidence_sha256, "fixture evidence sha256"),
        ):
            _sha(value, label)
        if self.phase not in PRECHECK_PHASES:
            raise ValueError("factorial precheck phase differs")
        if self.arm_id not in ARM_IDS or type(self.arm_position) is not int:
            raise ValueError("factorial precheck arm identity differs")
        if self.arm_update_policy != ARM_POLICY_SPECS[self.arm_id].update_policy:
            raise ValueError("factorial precheck arm policy differs")
        if not isinstance(self.operation_id, str) or not self.operation_id:
            raise ValueError("factorial precheck operation id is empty")
        if self.model_calls != 0 or self.evaluator_transactions != 0:
            raise ValueError("factorial phase precheck cannot record calls")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_id": self.arm_id,
            "arm_position": self.arm_position,
            "arm_update_policy": self.arm_update_policy,
            "evaluator_transactions": self.evaluator_transactions,
            "fixture_evidence_sha256": self.fixture_evidence_sha256,
            "model_calls": self.model_calls,
            "operation_id": self.operation_id,
            "phase": self.phase,
            "plan_sha256": self.plan_sha256,
            "prerequisite_barrier_sha256": self.prerequisite_barrier_sha256,
            "receipt_kind": self.receipt_kind,
            "schema_version": self.schema_version,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class PrecheckPhaseBarrier:
    plan_sha256: str
    task_seed_key_sha256: str
    version: str
    phase: str
    prerequisite_barrier_sha256: str
    arm_order: tuple[str, ...]
    phase_receipt_sha256s: tuple[str, ...]
    model_calls: int = 0
    evaluator_transactions: int = 0
    schema_version: int = 1
    receipt_kind: str = "factorial_phase_barrier_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.receipt_kind != (
            "factorial_phase_barrier_v1"
        ):
            raise ValueError("unsupported factorial phase barrier")
        for value, label in (
            (self.plan_sha256, "plan sha256"),
            (self.task_seed_key_sha256, "task/seed key sha256"),
            (self.prerequisite_barrier_sha256, "prerequisite barrier sha256"),
        ):
            _sha(value, label)
        if self.phase not in PRECHECK_PHASES or not _is_arm_rotation(self.arm_order):
            raise ValueError("factorial phase barrier identity differs")
        if len(self.phase_receipt_sha256s) != len(ARM_IDS):
            raise ValueError("factorial phase barrier receipt coverage differs")
        for value in self.phase_receipt_sha256s:
            _sha(value, "phase receipt sha256")
        if len(set(self.phase_receipt_sha256s)) != len(ARM_IDS):
            raise ValueError("factorial phase barrier receipt hashes are not distinct")
        if self.model_calls != 0 or self.evaluator_transactions != 0:
            raise ValueError("factorial phase barrier cannot record calls")

    def to_dict(self) -> dict[str, Any]:
        return {
            "arm_order": list(self.arm_order),
            "evaluator_transactions": self.evaluator_transactions,
            "model_calls": self.model_calls,
            "phase": self.phase,
            "phase_receipt_sha256s": list(self.phase_receipt_sha256s),
            "plan_sha256": self.plan_sha256,
            "prerequisite_barrier_sha256": self.prerequisite_barrier_sha256,
            "receipt_kind": self.receipt_kind,
            "schema_version": self.schema_version,
            "task_seed_key_sha256": self.task_seed_key_sha256,
            "version": self.version,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


@dataclass(frozen=True)
class PrecheckAdvance:
    phase_receipt_sha256: str
    phase_barrier_sha256: str | None


def _required_fields(payload: Mapping[str, Any], fields: set[str], label: str) -> None:
    if set(payload) != fields:
        raise ValueError(f"{label} fields differ")


def _load_v001_receipt(raw: bytes) -> V001PrecheckReceipt:
    payload = _decode_canonical(raw, label="shared-v001 precheck receipt")
    _required_fields(
        payload,
        {
            "arm_fork_receipts",
            "arm_policy_sha256",
            "canonical_compile_contract_sha256",
            "compile_equivalence_receipt_sha256",
            "evaluator_transactions",
            "intent_sha256",
            "model_calls",
            "plan_sha256",
            "receipt_kind",
            "schema_version",
            "task_seed_key_sha256",
            "trunk_receipt_sha256",
            "trunk_status",
        },
        "shared-v001 precheck receipt",
    )
    forks = payload["arm_fork_receipts"]
    if not isinstance(forks, dict) or set(forks) != set(ARM_IDS):
        raise ValueError("shared-v001 precheck fork mapping differs")
    return V001PrecheckReceipt(
        plan_sha256=payload["plan_sha256"],
        task_seed_key_sha256=payload["task_seed_key_sha256"],
        intent_sha256=payload["intent_sha256"],
        canonical_compile_contract_sha256=payload[
            "canonical_compile_contract_sha256"
        ],
        compile_equivalence_receipt_sha256=payload[
            "compile_equivalence_receipt_sha256"
        ],
        trunk_receipt_sha256=payload["trunk_receipt_sha256"],
        trunk_status=payload["trunk_status"],
        arm_policy_sha256=payload["arm_policy_sha256"],
        arm_fork_receipts=tuple((arm, forks[arm]) for arm in ARM_IDS),
        model_calls=payload["model_calls"],
        evaluator_transactions=payload["evaluator_transactions"],
        schema_version=payload["schema_version"],
        receipt_kind=payload["receipt_kind"],
    )


def _load_phase_receipt(raw: bytes) -> PrecheckPhaseReceipt:
    payload = _decode_canonical(raw, label="factorial phase precheck receipt")
    expected = {
        "arm_id",
        "arm_position",
        "arm_update_policy",
        "evaluator_transactions",
        "fixture_evidence_sha256",
        "model_calls",
        "operation_id",
        "phase",
        "plan_sha256",
        "prerequisite_barrier_sha256",
        "receipt_kind",
        "schema_version",
        "task_seed_key_sha256",
        "version",
    }
    _required_fields(payload, expected, "factorial phase precheck receipt")
    return PrecheckPhaseReceipt(**payload)


def _load_phase_barrier(raw: bytes) -> PrecheckPhaseBarrier:
    payload = _decode_canonical(raw, label="factorial phase barrier")
    expected = {
        "arm_order",
        "evaluator_transactions",
        "model_calls",
        "phase",
        "phase_receipt_sha256s",
        "plan_sha256",
        "prerequisite_barrier_sha256",
        "receipt_kind",
        "schema_version",
        "task_seed_key_sha256",
        "version",
    }
    _required_fields(payload, expected, "factorial phase barrier")
    payload["arm_order"] = tuple(payload["arm_order"])
    payload["phase_receipt_sha256s"] = tuple(payload["phase_receipt_sha256s"])
    return PrecheckPhaseBarrier(**payload)


class _FactorialZeroCallBarrierController:
    """Shared immutable task×seed barrier implementation.

    Different task×seed blocks may be acknowledged concurrently because each
    has a separate state directory.  Within one block, arm acknowledgements
    follow the frozen Latin rotation and a phase cannot begin until all four
    arms have sealed the prior phase.  Public constructors below decide whether
    the state machine is fixture-only or bound to the exact formal matrix.
    """

    def __init__(
        self,
        *,
        root: Path,
        plan: FactorialZeroCallPlan | FactorialFormalZeroCallPlan,
        trunk_archive: FactorialTrunkReader,
    ) -> None:
        if type(plan) is FactorialZeroCallPlan:
            parser = FactorialZeroCallPlan.from_bytes
            plan_label = "factorial zero-call fixture plan"
        elif type(plan) is FactorialFormalZeroCallPlan:
            parser = FactorialFormalZeroCallPlan._from_bytes_unverified_source
            plan_label = "exact formal factorial zero-call plan"
        else:
            raise ValueError("factorial barrier requires a typed zero-call plan")
        self.root = lexical_absolute(root)
        self.plan = plan
        self.trunk_archive = trunk_archive
        self._assert_zero_authority()
        plan_path = self.root / "plan.json"
        write_once_safe_regular_file(
            plan_path,
            plan.canonical_bytes,
            label=plan_label,
            temporary_suffix=".plan.tmp",
        )
        replayed = parser(
            read_safe_regular_file(plan_path, label=plan_label),
            expected_sha256=plan.sha256,
        )
        if replayed != plan:
            raise ValueError("factorial zero-call barrier plan replay differs")

    def _assert_zero_authority(self) -> None:
        if self.plan.execution_authority != PRECHECK_AUTHORITY or any(
            self.plan.execution_entitlement[field] != 0
            for field in _ENTITLEMENT_FIELDS
        ):
            raise ValueError(
                "factorial precheck refuses execution authority or entitlement"
            )

    def _block_root(self, key: TaskSeedKey) -> Path:
        self.plan.schedule_for(key)
        return self.root / "task-seeds" / key.sha256

    def _v001_path(self, key: TaskSeedKey) -> Path:
        return self._block_root(key) / "v001.json"

    def _phase_path(
        self, key: TaskSeedKey, version: int, phase: str, position: int, arm_id: str
    ) -> Path:
        return (
            self._block_root(key)
            / _version_label(version)
            / phase
            / f"{position:02d}-{arm_id}.json"
        )

    def _barrier_path(self, key: TaskSeedKey, version: int, phase: str) -> Path:
        return self._block_root(key) / _version_label(version) / f"{phase}.barrier.json"

    def _operation_id(
        self, key: TaskSeedKey, version: int, phase: str, arm_id: str
    ) -> str:
        return (
            f"factorial-precheck:{self.plan.sha256}:{key.sha256}:"
            f"{_version_label(version)}:{phase}:{arm_id}"
        )

    def _validate_shared_v001(self, key: TaskSeedKey) -> V001PrecheckReceipt:
        """Replay the public trunk archive and return its zero-call binding."""

        self.plan.schedule_for(key)
        intent = self.trunk_archive.load_intent(key.sha256)
        canonical = self.trunk_archive.load_canonical_compile(key.sha256)
        equivalence = self.trunk_archive.load_equivalence(key.sha256)
        trunk = self.trunk_archive.load_trunk(key.sha256)

        if getattr(intent, "task_seed_key", None) != key:
            raise ValueError("shared-v001 intent task/seed binding differs")
        if (
            getattr(canonical, "task_seed_key_sha256", None) != key.sha256
            or getattr(canonical, "context_binding_sha256", None)
            != key.context_binding_sha256
        ):
            raise ValueError("shared-v001 canonical compile binding differs")
        if (
            getattr(equivalence, "task_seed_key_sha256", None) != key.sha256
            or getattr(equivalence, "canonical_compile_contract_sha256", None)
            != canonical.sha256
            or getattr(equivalence, "canonical_compiled_harness_semantic_sha256", None)
            != getattr(canonical, "compiled_harness_semantic_sha256", None)
        ):
            raise ValueError("shared-v001 compile equivalence binding differs")
        if (
            getattr(trunk, "task_seed_key_sha256", None) != key.sha256
            or getattr(trunk, "intent_sha256", None) != intent.sha256
            or getattr(trunk, "canonical_compile_contract_sha256", None)
            != canonical.sha256
            or getattr(trunk, "compile_equivalence_receipt_sha256", None)
            != equivalence.sha256
            or getattr(trunk, "version", None) != "v001"
            or getattr(trunk, "trunk_status", None) not in _RESULT_TRUNK_STATUSES
        ):
            raise ValueError("shared-v001 result trunk binding differs")

        arm_compile_receipts = getattr(
            equivalence, "arm_compile_receipt_sha256s", None
        )
        if not isinstance(arm_compile_receipts, Mapping) or set(
            arm_compile_receipts
        ) != set(ARM_IDS):
            raise ValueError("shared-v001 arm compile receipt coverage differs")
        fork_pairs: list[tuple[str, str]] = []
        for arm_id in ARM_IDS:
            fork = self.trunk_archive.load_fork(key.sha256, arm_id)
            expected = {
                "task_seed_key_sha256": key.sha256,
                "trunk_receipt_sha256": trunk.sha256,
                "arm_id": arm_id,
                "arm_cell_id": key.arm_cell_id(arm_id),
                "arm_compile_receipt_sha256": arm_compile_receipts[arm_id],
                "trunk_status": trunk.trunk_status,
                "version": "v001",
            }
            if any(
                getattr(fork, field, None) != value
                for field, value in expected.items()
            ):
                raise ValueError(f"shared-v001 {arm_id} fork binding differs")
            shared = {
                "shared_decision_sha256": "decision_sha256",
                "shared_operational_fingerprint": "operational_fingerprint",
                "shared_compiled_harness_semantic_sha256": (
                    "compiled_harness_semantic_sha256"
                ),
                "shared_solution_prompt_sha256": "solution_prompt_sha256",
                "shared_solution_artifact_sha256": "solution_artifact_sha256",
                "shared_attempt_artifact_sha256": "attempt_artifact_sha256",
                "shared_evaluation_artifact_sha256": "evaluation_artifact_sha256",
            }
            if any(
                getattr(fork, fork_field, None) != getattr(trunk, trunk_field, None)
                for fork_field, trunk_field in shared.items()
            ):
                raise ValueError(f"shared-v001 {arm_id} fork outcome differs")
            fork_pairs.append((arm_id, _sha(fork.sha256, "arm fork receipt sha256")))

        return V001PrecheckReceipt(
            plan_sha256=self.plan.sha256,
            task_seed_key_sha256=key.sha256,
            intent_sha256=intent.sha256,
            canonical_compile_contract_sha256=canonical.sha256,
            compile_equivalence_receipt_sha256=equivalence.sha256,
            trunk_receipt_sha256=trunk.sha256,
            trunk_status=trunk.trunk_status,
            arm_policy_sha256=self.plan.arm_policy_sha256,
            arm_fork_receipts=tuple(fork_pairs),
        )

    def bind_shared_v001(self, key: TaskSeedKey) -> V001PrecheckReceipt:
        """Bind an existing common v001 trunk; this performs no task work."""

        self._assert_zero_authority()
        expected = self._validate_shared_v001(key)
        write_once_safe_regular_file(
            self._v001_path(key),
            expected.canonical_bytes,
            label="shared-v001 precheck binding",
            temporary_suffix=".v001.tmp",
        )
        return expected

    def _load_bound_v001(self, key: TaskSeedKey) -> V001PrecheckReceipt:
        path = self._v001_path(key)
        if not safe_regular_file_exists(path, label="shared-v001 precheck binding"):
            raise ValueError("shared-v001 trunk must be bound before v002")
        receipt = _load_v001_receipt(
            read_safe_regular_file(path, label="shared-v001 precheck binding")
        )
        expected = self._validate_shared_v001(key)
        if receipt != expected or receipt.canonical_bytes != expected.canonical_bytes:
            raise ValueError("shared-v001 precheck binding differs on replay")
        return receipt

    def _load_phase_receipt_path(self, path: Path) -> PrecheckPhaseReceipt:
        if not safe_regular_file_exists(path, label="factorial phase precheck receipt"):
            raise ValueError("factorial phase precheck predecessor is missing")
        return _load_phase_receipt(
            read_safe_regular_file(path, label="factorial phase precheck receipt")
        )

    def _validate_phase_member(
        self,
        member: PrecheckPhaseReceipt,
        *,
        key: TaskSeedKey,
        version: int,
        phase: str,
        arm_id: str,
        position: int,
        prerequisite: str,
    ) -> None:
        expected = {
            "plan_sha256": self.plan.sha256,
            "task_seed_key_sha256": key.sha256,
            "version": _version_label(version),
            "phase": phase,
            "arm_id": arm_id,
            "arm_position": position,
            "arm_update_policy": ARM_POLICY_SPECS[arm_id].update_policy,
            "prerequisite_barrier_sha256": prerequisite,
            "operation_id": self._operation_id(key, version, phase, arm_id),
            "model_calls": 0,
            "evaluator_transactions": 0,
        }
        if any(getattr(member, field) != value for field, value in expected.items()):
            raise ValueError("factorial phase barrier member binding differs")

    def _load_barrier_path(self, path: Path) -> PrecheckPhaseBarrier:
        if not safe_regular_file_exists(path, label="factorial phase barrier"):
            raise ValueError("factorial precheck phase barrier is missing")
        return _load_phase_barrier(
            read_safe_regular_file(path, label="factorial phase barrier")
        )

    def _verified_barrier(
        self, key: TaskSeedKey, *, version: int, phase: str
    ) -> PrecheckPhaseBarrier:
        """Replay a sealed barrier and all four immutable member receipts."""

        schedule = self.plan.schedule_for(key)
        label = _version_label(version)
        if version > schedule.final_version or phase not in PRECHECK_PHASES:
            raise ValueError("factorial phase barrier is outside the frozen schedule")
        barrier = self._load_barrier_path(self._barrier_path(key, version, phase))
        prerequisite = self._prerequisite_sha256(key, version=version, phase=phase)
        if (
            barrier.plan_sha256 != self.plan.sha256
            or barrier.task_seed_key_sha256 != key.sha256
            or barrier.version != label
            or barrier.phase != phase
            or barrier.prerequisite_barrier_sha256 != prerequisite
            or barrier.arm_order != schedule.arm_order
        ):
            raise ValueError("factorial phase barrier binding differs")
        members: list[PrecheckPhaseReceipt] = []
        for position, arm_id in enumerate(schedule.arm_order):
            member = self._load_phase_receipt_path(
                self._phase_path(key, version, phase, position, arm_id)
            )
            self._validate_phase_member(
                member,
                key=key,
                version=version,
                phase=phase,
                arm_id=arm_id,
                position=position,
                prerequisite=prerequisite,
            )
            members.append(member)
        if barrier.phase_receipt_sha256s != tuple(item.sha256 for item in members):
            raise ValueError("factorial phase barrier member hashes differ")
        return barrier

    def _prerequisite_sha256(
        self,
        key: TaskSeedKey,
        *,
        version: int,
        phase: str,
    ) -> str:
        if phase == "update":
            if version == PRECHECK_MIN_VERSION:
                return self._load_bound_v001(key).sha256
            return self._verified_barrier(
                key, version=version - 1, phase="evaluation"
            ).sha256
        phase_index = PRECHECK_PHASES.index(phase)
        return self._verified_barrier(
            key, version=version, phase=PRECHECK_PHASES[phase_index - 1]
        ).sha256

    def acknowledge_phase(
        self,
        *,
        key: TaskSeedKey,
        version: int,
        phase: str,
        arm_id: str,
        arm_update_policy: str,
        fixture_evidence_sha256: str,
    ) -> PrecheckAdvance:
        """Acknowledge one fixture phase and seal a barrier after its fourth arm.

        The evidence digest is only a caller-supplied precheck fixture token. It
        is never dereferenced and cannot grant authority to invoke anything.
        """

        self._assert_zero_authority()
        schedule = self.plan.schedule_for(key)
        label = _version_label(version)
        if version > schedule.final_version:
            raise ValueError("factorial phase exceeds the frozen task/seed schedule")
        if phase not in PRECHECK_PHASES:
            raise ValueError("factorial precheck phase differs")
        if arm_id not in ARM_IDS:
            raise ValueError("factorial precheck arm differs")
        expected_policy = ARM_POLICY_SPECS[arm_id].update_policy
        if arm_update_policy != expected_policy:
            raise ValueError("factorial precheck arm policy differs")
        _sha(fixture_evidence_sha256, "fixture evidence sha256")
        prerequisite = self._prerequisite_sha256(
            key, version=version, phase=phase
        )
        position = schedule.arm_order.index(arm_id)
        path = self._phase_path(key, version, phase, position, arm_id)
        receipt = PrecheckPhaseReceipt(
            plan_sha256=self.plan.sha256,
            task_seed_key_sha256=key.sha256,
            version=label,
            phase=phase,
            arm_id=arm_id,
            arm_position=position,
            arm_update_policy=arm_update_policy,
            prerequisite_barrier_sha256=prerequisite,
            fixture_evidence_sha256=fixture_evidence_sha256,
            operation_id=self._operation_id(key, version, phase, arm_id),
        )

        if position:
            prior_arm = schedule.arm_order[position - 1]
            prior = self._load_phase_receipt_path(
                self._phase_path(key, version, phase, position - 1, prior_arm)
            )
            if (
                prior.plan_sha256 != self.plan.sha256
                or prior.task_seed_key_sha256 != key.sha256
                or prior.version != label
                or prior.phase != phase
                or prior.arm_id != prior_arm
                or prior.arm_position != position - 1
                or prior.prerequisite_barrier_sha256 != prerequisite
            ):
                raise ValueError("factorial phase arm order predecessor differs")

        write_once_safe_regular_file(
            path,
            receipt.canonical_bytes,
            label="factorial phase precheck receipt",
            temporary_suffix=".phase.tmp",
        )

        barrier_sha: str | None = None
        if position == len(schedule.arm_order) - 1:
            receipts = tuple(
                self._load_phase_receipt_path(
                    self._phase_path(key, version, phase, index, ordered_arm)
                )
                for index, ordered_arm in enumerate(schedule.arm_order)
            )
            for index, item in enumerate(receipts):
                self._validate_phase_member(
                    item,
                    key=key,
                    version=version,
                    phase=phase,
                    arm_id=schedule.arm_order[index],
                    position=index,
                    prerequisite=prerequisite,
                )
            barrier = PrecheckPhaseBarrier(
                plan_sha256=self.plan.sha256,
                task_seed_key_sha256=key.sha256,
                version=label,
                phase=phase,
                prerequisite_barrier_sha256=prerequisite,
                arm_order=schedule.arm_order,
                phase_receipt_sha256s=tuple(item.sha256 for item in receipts),
            )
            write_once_safe_regular_file(
                self._barrier_path(key, version, phase),
                barrier.canonical_bytes,
                label="factorial phase barrier",
                temporary_suffix=".barrier.tmp",
            )
            barrier_sha = barrier.sha256
        else:
            barrier_path = self._barrier_path(key, version, phase)
            if safe_regular_file_exists(barrier_path, label="factorial phase barrier"):
                barrier_sha = self._verified_barrier(
                    key, version=version, phase=phase
                ).sha256
        return PrecheckAdvance(receipt.sha256, barrier_sha)

    def task_seed_complete(self, key: TaskSeedKey) -> bool:
        """Return whether the final vNNN evaluation barrier is sealed and valid."""

        self._assert_zero_authority()
        schedule = self.plan.schedule_for(key)
        path = self._barrier_path(key, schedule.final_version, "evaluation")
        if not safe_regular_file_exists(path, label="factorial phase barrier"):
            return False
        self._verified_barrier(
            key, version=schedule.final_version, phase="evaluation"
        )
        return True

    def status(self) -> dict[str, Any]:
        """Return a read-only zero-call progress projection."""

        self._assert_zero_authority()
        complete = [
            item.key.sha256
            for item in self.plan.schedules
            if self.task_seed_complete(item.key)
        ]
        return {
            "execution_authority": PRECHECK_AUTHORITY,
            "execution_entitlement": dict(self.plan.execution_entitlement),
            "plan_scope": self.plan.plan_scope,
            "plan_sha256": self.plan.sha256,
            "planned_benchmark_count": len(
                {item.key.suite for item in self.plan.schedules}
            ),
            "planned_task_seed_count": len(self.plan.schedules),
            "complete_task_seed_count": len(complete),
            "complete_task_seed_sha256s": complete,
            "formal_execution_ready": False,
        }


class FactorialPrecheckController(_FactorialZeroCallBarrierController):
    """Fixture-only barrier controller used by local state-machine tests.

    It deliberately rejects :class:`FactorialFormalZeroCallPlan`; formal matrix
    evidence must pass through the dedicated exact-plan controller below.
    """

    def __init__(
        self,
        *,
        root: Path,
        plan: FactorialZeroCallPlan,
        trunk_archive: FactorialTrunkReader,
    ) -> None:
        if type(plan) is not FactorialZeroCallPlan:
            raise ValueError("factorial fixture barrier requires a fixture-only plan")
        super().__init__(root=root, plan=plan, trunk_archive=trunk_archive)


class FactorialFormalZeroCallBarrierController(
    _FactorialZeroCallBarrierController
):
    """Exact-matrix zero-call barrier and recovery controller.

    This controller accepts only :class:`FactorialFormalZeroCallPlan`, replays
    that plan against the checked-in manifest at construction/recovery, and
    mechanically verifies the four v001 fork variant/contract bindings every
    time v001 is bound or replayed.  It exposes no execution callback and its
    plan is required to retain ``NOT_GRANTED`` authority and all-zero
    entitlements.
    """

    def __init__(
        self,
        *,
        root: Path,
        plan: FactorialFormalZeroCallPlan,
        trunk_archive: FactorialTrunkReader,
        task_authority: Any,
        task_authority_bundle: Any,
    ) -> None:
        if type(plan) is not FactorialFormalZeroCallPlan:
            raise ValueError(
                "formal factorial barrier requires an exact formal zero-call plan"
            )
        from .factorial_task_authority import (
            ExactTaskSeedAuthorityBundle,
            FactorialTaskArtifactAuthority,
        )

        if type(task_authority) is not FactorialTaskArtifactAuthority:
            raise ValueError("formal factorial barrier requires a source authority")
        if type(task_authority_bundle) is not ExactTaskSeedAuthorityBundle:
            raise ValueError(
                "formal factorial barrier requires an exact authority bundle"
            )
        verified_bundle = task_authority.verify_exact_bundle(task_authority_bundle)
        if plan.task_authority_bundle_sha256 != verified_bundle.sha256:
            raise ValueError("formal factorial plan/source authority binding differs")
        if tuple(item.key for item in plan.schedules) != verified_bundle.task_seed_keys:
            raise ValueError("formal factorial plan/source task keys differ")
        self.task_authority = task_authority
        self.task_authority_bundle = verified_bundle
        super().__init__(root=root, plan=plan, trunk_archive=trunk_archive)

    def _verify_source_authority(self) -> None:
        replayed = self.task_authority.verify_exact_bundle(
            self.task_authority_bundle
        )
        if (
            replayed.sha256 != self.plan.task_authority_bundle_sha256
            or tuple(item.key for item in self.plan.schedules)
            != replayed.task_seed_keys
        ):
            raise ValueError("formal factorial source authority replay differs")

    def _validate_shared_v001(self, key: TaskSeedKey) -> V001PrecheckReceipt:
        self._verify_source_authority()
        generic = super()._validate_shared_v001(key)
        formal = verify_formal_v001_fork_bindings(
            plan=self.plan,
            trunk_archive=self.trunk_archive,
            key=key,
        )
        if (
            formal.formal_plan_sha256 != self.plan.sha256
            or formal.task_seed_key_sha256 != key.sha256
            or formal.factorial_contract_sha256
            != self.plan.factorial_contract_sha256
            or formal.arm_variant_sha256s != self.plan.arm_variant_sha256s
            or formal.arm_fork_receipt_sha256s != generic.arm_fork_receipts
            or generic.arm_policy_sha256 != self.plan.bound_arm_policy_sha256
        ):
            raise ValueError("formal shared-v001 barrier binding differs")
        return generic
