"""Exact zero-call schedule for the isolated B-online mechanism pilot.

The checked-in factorial contract preregisters four independent lanes:

``O0``
    No learned cross-task state.
``OM``
    Content-addressed meta-memory / Experience Bank state.
``OP``
    A typed, versioned policy over trusted Harness components.
``OA``
    A typed population/archive of previously compiled Harness recipes.

This module expands the contract into every logical source, updater, O1 and
O2 slot.  It deliberately has no model, provider, evaluator, subprocess or
resource-governor interface.  In particular, a schedule is not authority to
run the pilot: source-task artifact authority, provider canaries, a transport
ledger and non-zero entitlements remain separate fail-closed gates.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from types import MappingProxyType
from typing import Any, Mapping

from .factorial_contract import verify_factorial_contract


ONLINE_MECHANISMS = ("O0", "OM", "OP", "OA")
LEARNED_MECHANISMS = ("OM", "OP", "OA")
ONLINE_STAGES = ("source", "O1", "O2")
ONLINE_AUTHORITY = "NOT_GRANTED"
ONLINE_TASK_AUTHORITY_STATUS = (
    "ONLINE_SOURCE_AND_HELDOUT_TASK_AUTHORITY_NOT_BOUND"
)
ONLINE_STATE_LINEAGE_STATUS = (
    "SOURCE_TERMINAL_RECEIPT_PARENT_AND_OUTPUT_CHECKPOINT_NOT_BOUND"
)
ONLINE_MAIN_OVERLAP_POLICY = (
    "PREDECLARED_TASK_IDENTITIES_REUSED_BUT_MAIN_RESULTS_TRACES_AND_STATE_"
    "MUST_NOT_ENTER_ONLINE"
)
_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")


class FactorialOnlinePlanError(ValueError):
    """The logical online schedule differs from the frozen contract."""


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
        raise FactorialOnlinePlanError(
            "online plan payload is not canonical JSON"
        ) from exc


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise FactorialOnlinePlanError(f"invalid {label}")
    return value


def _safe_id(value: object, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise FactorialOnlinePlanError(f"unsafe {label}")
    return value


def _strict_json(raw: bytes, *, label: str) -> dict[str, Any]:
    def reject_constant(value: str) -> None:
        raise FactorialOnlinePlanError(f"{label} contains {value}")

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise FactorialOnlinePlanError(
                    f"{label} repeats field {key!r}"
                )
            result[key] = value
        return result

    if not isinstance(raw, bytes) or not raw:
        raise FactorialOnlinePlanError(f"{label} bytes are empty")
    try:
        payload = json.loads(
            raw.decode("utf-8", errors="strict"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise FactorialOnlinePlanError(f"{label} is not strict JSON") from exc
    if not isinstance(payload, dict) or _canonical_bytes(payload) != raw:
        raise FactorialOnlinePlanError(f"{label} is not canonical")
    return payload


def _exact_fields(payload: Mapping[str, Any], expected: set[str], label: str) -> None:
    if not isinstance(payload, Mapping) or set(payload) != expected:
        raise FactorialOnlinePlanError(f"{label} fields differ")


def _attempt_id(
    *,
    stage: str,
    benchmark_id: str,
    instance_id: str,
    seed: int,
    mechanism_id: str,
    version: int,
) -> str:
    return (
        f"factorial-online:{stage}:{benchmark_id}:{instance_id}:"
        f"seed-{seed}:{mechanism_id}:v{version:03d}"
    )


@dataclass(frozen=True)
class OnlineAttemptSlot:
    """One evaluator-bearing trajectory step in the logical pilot."""

    stage: str
    benchmark_id: str
    instance_id: str
    seed: int
    mechanism_id: str
    version: int
    attempt_id: str
    builder_operation_id: str
    solution_operation_id: str
    evaluator_operation_id: str

    def __post_init__(self) -> None:
        if self.stage not in ONLINE_STAGES:
            raise FactorialOnlinePlanError("online attempt stage differs")
        _safe_id(self.benchmark_id, "online benchmark id")
        _safe_id(self.instance_id, "online instance id")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise FactorialOnlinePlanError("online attempt seed differs")
        if self.stage == "source":
            if self.mechanism_id != "SHARED" or self.version < 1:
                raise FactorialOnlinePlanError("source attempt identity differs")
        else:
            if self.mechanism_id not in ONLINE_MECHANISMS:
                raise FactorialOnlinePlanError("held-out mechanism differs")
            if (self.stage == "O1") != (self.version == 1):
                raise FactorialOnlinePlanError("online stage/version differs")
            if self.stage == "O2" and self.version < 2:
                raise FactorialOnlinePlanError("O2 must start at v002")
        expected = _attempt_id(
            stage=self.stage,
            benchmark_id=self.benchmark_id,
            instance_id=self.instance_id,
            seed=self.seed,
            mechanism_id=self.mechanism_id,
            version=self.version,
        )
        if self.attempt_id != expected:
            raise FactorialOnlinePlanError("online attempt id differs")
        operations = {
            "builder": self.builder_operation_id,
            "solution": self.solution_operation_id,
            "evaluator": self.evaluator_operation_id,
        }
        if operations != {
            kind: f"{expected}:{kind}" for kind in operations
        } or len(set(operations.values())) != 3:
            raise FactorialOnlinePlanError("online attempt operations differ")

    @classmethod
    def create(
        cls,
        *,
        stage: str,
        benchmark_id: str,
        instance_id: str,
        seed: int,
        mechanism_id: str,
        version: int,
    ) -> "OnlineAttemptSlot":
        attempt_id = _attempt_id(
            stage=stage,
            benchmark_id=benchmark_id,
            instance_id=instance_id,
            seed=seed,
            mechanism_id=mechanism_id,
            version=version,
        )
        return cls(
            stage=stage,
            benchmark_id=benchmark_id,
            instance_id=instance_id,
            seed=seed,
            mechanism_id=mechanism_id,
            version=version,
            attempt_id=attempt_id,
            builder_operation_id=f"{attempt_id}:builder",
            solution_operation_id=f"{attempt_id}:solution",
            evaluator_operation_id=f"{attempt_id}:evaluator",
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_id": self.attempt_id,
            "benchmark_id": self.benchmark_id,
            "builder_operation_id": self.builder_operation_id,
            "evaluator_operation_id": self.evaluator_operation_id,
            "instance_id": self.instance_id,
            "mechanism_id": self.mechanism_id,
            "seed": self.seed,
            "solution_operation_id": self.solution_operation_id,
            "stage": self.stage,
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "OnlineAttemptSlot":
        expected = {
            "attempt_id",
            "benchmark_id",
            "builder_operation_id",
            "evaluator_operation_id",
            "instance_id",
            "mechanism_id",
            "seed",
            "solution_operation_id",
            "stage",
            "version",
        }
        _exact_fields(payload, expected, "online attempt slot")
        return cls(**dict(payload))


@dataclass(frozen=True)
class OnlineMechanismUpdateSlot:
    """Exactly one post-source update for one learned mechanism lane."""

    benchmark_id: str
    source_instance_id: str
    seed: int
    mechanism_id: str
    source_final_version: int
    update_id: str
    updater_operation_id: str

    def __post_init__(self) -> None:
        _safe_id(self.benchmark_id, "online update benchmark id")
        _safe_id(self.source_instance_id, "online source instance id")
        if self.mechanism_id not in LEARNED_MECHANISMS:
            raise FactorialOnlinePlanError("online updater mechanism differs")
        if type(self.seed) is not int or not 0 <= self.seed <= 2**31 - 1:
            raise FactorialOnlinePlanError("online updater seed differs")
        if type(self.source_final_version) is not int or self.source_final_version < 1:
            raise FactorialOnlinePlanError("online source final version differs")
        expected = (
            f"factorial-online:update:{self.benchmark_id}:"
            f"{self.source_instance_id}:seed-{self.seed}:{self.mechanism_id}"
        )
        if self.update_id != expected or self.updater_operation_id != (
            f"{expected}:updater"
        ):
            raise FactorialOnlinePlanError("online updater operation differs")

    @classmethod
    def create(
        cls,
        *,
        benchmark_id: str,
        source_instance_id: str,
        seed: int,
        mechanism_id: str,
        source_final_version: int,
    ) -> "OnlineMechanismUpdateSlot":
        update_id = (
            f"factorial-online:update:{benchmark_id}:"
            f"{source_instance_id}:seed-{seed}:{mechanism_id}"
        )
        return cls(
            benchmark_id=benchmark_id,
            source_instance_id=source_instance_id,
            seed=seed,
            mechanism_id=mechanism_id,
            source_final_version=source_final_version,
            update_id=update_id,
            updater_operation_id=f"{update_id}:updater",
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "benchmark_id": self.benchmark_id,
            "mechanism_id": self.mechanism_id,
            "seed": self.seed,
            "source_final_version": self.source_final_version,
            "source_instance_id": self.source_instance_id,
            "update_id": self.update_id,
            "updater_operation_id": self.updater_operation_id,
        }

    @classmethod
    def from_dict(
        cls, payload: Mapping[str, Any]
    ) -> "OnlineMechanismUpdateSlot":
        expected = {
            "benchmark_id",
            "mechanism_id",
            "seed",
            "source_final_version",
            "source_instance_id",
            "update_id",
            "updater_operation_id",
        }
        _exact_fields(payload, expected, "online mechanism update slot")
        return cls(**dict(payload))


@dataclass(frozen=True)
class FactorialOnlineZeroCallPlan:
    """Complete logical pilot expansion with permanently zero authority."""

    factorial_contract_sha256: str
    attempt_slots: tuple[OnlineAttemptSlot, ...]
    update_slots: tuple[OnlineMechanismUpdateSlot, ...]
    mechanism_state_roots: Mapping[str, str]
    stage_budget_projection: tuple[Mapping[str, Any], ...]
    task_artifact_authority_status: str = ONLINE_TASK_AUTHORITY_STATUS
    state_lineage_binding_status: str = ONLINE_STATE_LINEAGE_STATUS
    main_experiment_overlap_policy: str = ONLINE_MAIN_OVERLAP_POLICY
    independent_fresh_confirmation: bool = False
    execution_authority: str = ONLINE_AUTHORITY
    model_call_entitlement: int = 0
    evaluator_transaction_entitlement: int = 0
    schema_version: int = 1
    plan_kind: str = "moss_factorial_online_exact_zero_call_plan_v1"

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.plan_kind != (
            "moss_factorial_online_exact_zero_call_plan_v1"
        ):
            raise FactorialOnlinePlanError("unsupported online plan schema")
        _sha(self.factorial_contract_sha256, "factorial contract sha256")
        if self.execution_authority != ONLINE_AUTHORITY:
            raise FactorialOnlinePlanError("online plan cannot grant execution")
        if (
            type(self.model_call_entitlement) is not int
            or type(self.evaluator_transaction_entitlement) is not int
            or self.model_call_entitlement != 0
            or self.evaluator_transaction_entitlement != 0
        ):
            raise FactorialOnlinePlanError("online plan entitlement must be zero")
        if self.task_artifact_authority_status != ONLINE_TASK_AUTHORITY_STATUS:
            raise FactorialOnlinePlanError("online task authority status differs")
        if self.state_lineage_binding_status != ONLINE_STATE_LINEAGE_STATUS:
            raise FactorialOnlinePlanError("online state lineage status differs")
        if self.main_experiment_overlap_policy != ONLINE_MAIN_OVERLAP_POLICY:
            raise FactorialOnlinePlanError("online main-overlap policy differs")
        if self.independent_fresh_confirmation is not False:
            raise FactorialOnlinePlanError(
                "online pilot is not an independent fresh confirmation"
            )
        if not isinstance(self.attempt_slots, tuple) or any(
            type(item) is not OnlineAttemptSlot for item in self.attempt_slots
        ):
            raise FactorialOnlinePlanError("online attempt slots are not exact typed")
        if not isinstance(self.update_slots, tuple) or any(
            type(item) is not OnlineMechanismUpdateSlot for item in self.update_slots
        ):
            raise FactorialOnlinePlanError("online update slots are not exact typed")
        attempt_ids = tuple(item.attempt_id for item in self.attempt_slots)
        update_ids = tuple(item.update_id for item in self.update_slots)
        operation_ids = tuple(
            operation
            for item in self.attempt_slots
            for operation in (
                item.builder_operation_id,
                item.solution_operation_id,
                item.evaluator_operation_id,
            )
        ) + tuple(item.updater_operation_id for item in self.update_slots)
        if (
            len(attempt_ids) != len(set(attempt_ids))
            or len(update_ids) != len(set(update_ids))
            or len(operation_ids) != len(set(operation_ids))
        ):
            raise FactorialOnlinePlanError("online plan repeats a logical identity")
        if len(self.attempt_slots) != 732 or len(self.update_slots) != 84:
            raise FactorialOnlinePlanError("online plan logical slot count differs")
        roots = dict(self.mechanism_state_roots)
        if set(roots) != set(ONLINE_MECHANISMS) or roots["O0"] != "NONE":
            raise FactorialOnlinePlanError("online mechanism state roots differ")
        if (
            any(roots[item] == "NONE" for item in LEARNED_MECHANISMS)
            or len(set(roots.values())) != len(ONLINE_MECHANISMS)
        ):
            raise FactorialOnlinePlanError("learned state roots are not isolated")
        budgets = tuple(dict(item) for item in self.stage_budget_projection)
        if tuple(item.get("stage_id") for item in budgets) != ONLINE_STAGES:
            raise FactorialOnlinePlanError("online stage budget order differs")
        expected_budget_fields = {
            "evaluator_transactions_cumulative",
            "evaluator_transactions_incremental",
            "execution_condition",
            "logical_model_calls_cumulative",
            "logical_model_calls_incremental",
            "stage_id",
        }
        if any(set(item) != expected_budget_fields for item in budgets):
            raise FactorialOnlinePlanError("online stage budget fields differ")
        stage_attempts = {
            stage: sum(item.stage == stage for item in self.attempt_slots)
            for stage in ONLINE_STAGES
        }
        expected_update_calls = len(self.update_slots)
        expected_incremental = {
            "source": (
                stage_attempts["source"],
                2 * stage_attempts["source"] + expected_update_calls,
            ),
            "O1": (stage_attempts["O1"], 2 * stage_attempts["O1"]),
            "O2": (stage_attempts["O2"], 2 * stage_attempts["O2"]),
        }
        cumulative_evaluator = 0
        cumulative_model = 0
        for item in budgets:
            evaluator_increment, model_increment = expected_incremental[
                item["stage_id"]
            ]
            cumulative_evaluator += evaluator_increment
            cumulative_model += model_increment
            if (
                item["evaluator_transactions_incremental"]
                != evaluator_increment
                or item["logical_model_calls_incremental"] != model_increment
                or item["evaluator_transactions_cumulative"]
                != cumulative_evaluator
                or item["logical_model_calls_cumulative"] != cumulative_model
            ):
                raise FactorialOnlinePlanError(
                    "online stage budget arithmetic differs"
                )
        object.__setattr__(
            self,
            "mechanism_state_roots",
            MappingProxyType({item: roots[item] for item in ONLINE_MECHANISMS}),
        )
        object.__setattr__(
            self,
            "stage_budget_projection",
            tuple(MappingProxyType(item) for item in budgets),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "attempt_slots": [item.to_dict() for item in self.attempt_slots],
            "evaluator_transaction_entitlement": (
                self.evaluator_transaction_entitlement
            ),
            "execution_authority": self.execution_authority,
            "factorial_contract_sha256": self.factorial_contract_sha256,
            "independent_fresh_confirmation": self.independent_fresh_confirmation,
            "main_experiment_overlap_policy": (
                self.main_experiment_overlap_policy
            ),
            "mechanism_state_roots": dict(self.mechanism_state_roots),
            "model_call_entitlement": self.model_call_entitlement,
            "plan_kind": self.plan_kind,
            "schema_version": self.schema_version,
            "stage_budget_projection": [
                dict(item) for item in self.stage_budget_projection
            ],
            "state_lineage_binding_status": self.state_lineage_binding_status,
            "task_artifact_authority_status": self.task_artifact_authority_status,
            "update_slots": [item.to_dict() for item in self.update_slots],
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.to_dict())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()

    @property
    def logical_model_calls(self) -> int:
        return 2 * len(self.attempt_slots) + len(self.update_slots)

    @property
    def logical_evaluator_transactions(self) -> int:
        return len(self.attempt_slots)

    @classmethod
    def from_verified_contract(cls) -> "FactorialOnlineZeroCallPlan":
        contract = verify_factorial_contract()
        online = contract["online_pilot"]
        seeds = tuple(online["seeds"])
        attempts: list[OnlineAttemptSlot] = []
        updates: list[OnlineMechanismUpdateSlot] = []

        def instances(partition: Mapping[str, Any], *, source: bool) -> tuple[str, ...]:
            per_unit = partition["tasks_per_unit"]
            result: list[str] = []
            for task_unit in partition["task_units"]:
                for ordinal in range(1, per_unit + 1):
                    if per_unit == 1:
                        result.append(task_unit)
                    else:
                        suffix = "train" if source else "test"
                        result.append(f"{task_unit}:{suffix}_{ordinal}")
            if len(result) != partition["task_count"]:
                raise FactorialOnlinePlanError(
                    "online task partition expansion differs"
                )
            return tuple(result)

        for design in online["benchmark_designs"]:
            benchmark_id = design["benchmark_id"]
            source = design["source"]
            source_instances = instances(source, source=True)
            for seed in seeds:
                for instance_id in source_instances:
                    for version in range(1, source["rounds"] + 1):
                        attempts.append(
                            OnlineAttemptSlot.create(
                                stage="source",
                                benchmark_id=benchmark_id,
                                instance_id=instance_id,
                                seed=seed,
                                mechanism_id="SHARED",
                                version=version,
                            )
                        )
                    for mechanism_id in LEARNED_MECHANISMS:
                        updates.append(
                            OnlineMechanismUpdateSlot.create(
                                benchmark_id=benchmark_id,
                                source_instance_id=instance_id,
                                seed=seed,
                                mechanism_id=mechanism_id,
                                source_final_version=source["rounds"],
                            )
                        )

            heldout = design["heldout"]
            heldout_instances = instances(heldout, source=False)
            for seed in seeds:
                for instance_id in heldout_instances:
                    for mechanism_id in ONLINE_MECHANISMS:
                        attempts.append(
                            OnlineAttemptSlot.create(
                                stage="O1",
                                benchmark_id=benchmark_id,
                                instance_id=instance_id,
                                seed=seed,
                                mechanism_id=mechanism_id,
                                version=1,
                            )
                        )
                        for version in range(2, heldout["rounds"] + 1):
                            attempts.append(
                                OnlineAttemptSlot.create(
                                    stage="O2",
                                    benchmark_id=benchmark_id,
                                    instance_id=instance_id,
                                    seed=seed,
                                    mechanism_id=mechanism_id,
                                    version=version,
                                )
                            )

        plan = cls(
            factorial_contract_sha256=contract["contract_digest"],
            attempt_slots=tuple(attempts),
            update_slots=tuple(updates),
            mechanism_state_roots={
                item["mechanism_id"]: item["state_root"]
                for item in online["mechanisms"]
            },
            stage_budget_projection=tuple(dict(item) for item in online["stages"]),
        )
        if plan.logical_model_calls != online["stages"][-1][
            "logical_model_calls_cumulative"
        ] or plan.logical_evaluator_transactions != online["stages"][-1][
            "evaluator_transactions_cumulative"
        ]:
            raise FactorialOnlinePlanError("online logical budget expansion differs")
        stage_attempts = {
            stage: sum(item.stage == stage for item in plan.attempt_slots)
            for stage in ONLINE_STAGES
        }
        declared = {
            item["stage_id"]: item["evaluator_transactions_incremental"]
            for item in online["stages"]
        }
        if stage_attempts != declared:
            raise FactorialOnlinePlanError("online stage attempt expansion differs")
        return plan

    @classmethod
    def from_canonical_bytes(
        cls, raw: bytes, *, expected_sha256: str | None = None
    ) -> "FactorialOnlineZeroCallPlan":
        payload = _strict_json(raw, label="factorial online zero-call plan")
        expected = {
            "attempt_slots",
            "evaluator_transaction_entitlement",
            "execution_authority",
            "factorial_contract_sha256",
            "independent_fresh_confirmation",
            "main_experiment_overlap_policy",
            "mechanism_state_roots",
            "model_call_entitlement",
            "plan_kind",
            "schema_version",
            "stage_budget_projection",
            "state_lineage_binding_status",
            "task_artifact_authority_status",
            "update_slots",
        }
        _exact_fields(payload, expected, "factorial online zero-call plan")
        raw_attempts = payload["attempt_slots"]
        raw_updates = payload["update_slots"]
        if not isinstance(raw_attempts, list) or not isinstance(raw_updates, list):
            raise FactorialOnlinePlanError("online plan slot arrays differ")
        item = cls(
            factorial_contract_sha256=payload["factorial_contract_sha256"],
            attempt_slots=tuple(
                OnlineAttemptSlot.from_dict(value) for value in raw_attempts
            ),
            update_slots=tuple(
                OnlineMechanismUpdateSlot.from_dict(value) for value in raw_updates
            ),
            mechanism_state_roots=payload["mechanism_state_roots"],
            stage_budget_projection=tuple(payload["stage_budget_projection"]),
            task_artifact_authority_status=payload[
                "task_artifact_authority_status"
            ],
            state_lineage_binding_status=payload[
                "state_lineage_binding_status"
            ],
            main_experiment_overlap_policy=payload[
                "main_experiment_overlap_policy"
            ],
            independent_fresh_confirmation=payload[
                "independent_fresh_confirmation"
            ],
            execution_authority=payload["execution_authority"],
            model_call_entitlement=payload["model_call_entitlement"],
            evaluator_transaction_entitlement=payload[
                "evaluator_transaction_entitlement"
            ],
            schema_version=payload["schema_version"],
            plan_kind=payload["plan_kind"],
        )
        if item.canonical_bytes != raw:
            raise FactorialOnlinePlanError("online plan replay differs")
        if expected_sha256 is not None:
            _sha(expected_sha256, "expected online plan sha256")
            if item.sha256 != expected_sha256:
                raise FactorialOnlinePlanError("online plan hash differs")
        trusted = cls.from_verified_contract()
        if item != trusted or item.sha256 != trusted.sha256:
            raise FactorialOnlinePlanError(
                "online plan differs from the verified factorial contract"
            )
        return item


__all__ = [
    "FactorialOnlinePlanError",
    "FactorialOnlineZeroCallPlan",
    "LEARNED_MECHANISMS",
    "ONLINE_MECHANISMS",
    "ONLINE_STAGES",
    "ONLINE_STATE_LINEAGE_STATUS",
    "ONLINE_MAIN_OVERLAP_POLICY",
    "ONLINE_TASK_AUTHORITY_STATUS",
    "OnlineAttemptSlot",
    "OnlineMechanismUpdateSlot",
]
