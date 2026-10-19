"""Three-arm prequential campaign with per-task test-then-learn updates.

This module deliberately does not mutate the historical HB-GEN-1 four-arm
contract.  It adds the user-approved A/B-frozen/B-online experiment as a new
schema so old ledgers remain replayable byte-for-byte.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .events import ResourceCaps
from .formal import (
    FormalCampaignRunner,
    FormalProviderFactory,
    FormalTaskBinding,
    _ArmReceipt,
    _canonical_bytes,
    _resource_caps,
    _safe_id,
    _sha256_bytes,
    _write_once,
)
from .learning import (
    BuilderCheckpoint,
    ExperienceBankSnapshot,
    SealedInstanceTrajectory,
)
from .model_gateway import IsolatedModelGateway
from .operators import CrossInstanceMemoryGrant, TrustedOperatorRegistry
from .schema import BuilderVariant


THREE_ARMS = ("A", "B-frozen", "B-online")
THREE_ARM_VALIDITY_POLICY = {
    "rounds_per_arm": 8,
    "minimum_valid_rounds_per_arm": 4,
    "learning_tasks_per_suite": 6,
    "minimum_paired_learning_tasks": 5,
    "insufficient_status": "insufficient_validity",
    "score_aggregation": "valid_only_mean_and_best",
}
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_LEARNING_MODES = {"online", "sealed"}
_STAGING_FIELDS = {
    "schema_version",
    "phase_id",
    "code_revision",
    "model_signature",
    "execution_ready",
    "blockers",
    "source_hashes",
    "budgets",
    "resource_entitlement_totals",
    "cell_entitlements",
    "rule_ids",
    "variant_ids",
    "stream_policy",
    "stream",
    "experience_initialization",
    "online_instances_per_suite",
    "sealed_instances_per_suite",
    "validity_policy",
    "no_next_phase",
    "no_paid_provider_fallback",
}
_STREAM_FIELDS = {
    "stream_index",
    "block_index",
    "suite",
    "task_id",
    "instance_id",
    "arm_order",
    "learning_mode",
}


@dataclass(frozen=True)
class ThreeArmStreamItem:
    stream_index: int
    block_index: int
    suite: str
    task_id: str
    arm_order: tuple[str, ...]
    learning_mode: str

    @property
    def instance_id(self) -> str:
        return f"{self.suite}:{self.task_id}"

    def to_dict(self) -> dict[str, object]:
        return {
            "stream_index": self.stream_index,
            "block_index": self.block_index,
            "suite": self.suite,
            "task_id": self.task_id,
            "instance_id": self.instance_id,
            "arm_order": list(self.arm_order),
            "learning_mode": self.learning_mode,
        }


def _stream_item(payload: Any, *, expected_index: int) -> ThreeArmStreamItem:
    if not isinstance(payload, dict) or set(payload) != _STREAM_FIELDS:
        raise ValueError("three-arm stream item fields differ")
    if payload["stream_index"] != expected_index:
        raise ValueError("three-arm stream index is not contiguous")
    block_index = payload["block_index"]
    if isinstance(block_index, bool) or not isinstance(block_index, int) or block_index < 0:
        raise ValueError("three-arm block index is invalid")
    suite = _safe_id(payload["suite"], "three-arm suite")
    task_id = _safe_id(payload["task_id"], "three-arm task id")
    if payload["instance_id"] != f"{suite}:{task_id}":
        raise ValueError("three-arm instance id binding differs")
    raw_order = payload["arm_order"]
    expected_order = THREE_ARMS[expected_index % 3 :] + THREE_ARMS[: expected_index % 3]
    if raw_order != list(expected_order):
        raise ValueError("three-arm order must use the frozen rotation")
    learning_mode = payload["learning_mode"]
    if learning_mode not in _LEARNING_MODES:
        raise ValueError("three-arm learning mode is invalid")
    return ThreeArmStreamItem(
        stream_index=expected_index,
        block_index=block_index,
        suite=suite,
        task_id=task_id,
        arm_order=expected_order,
        learning_mode=learning_mode,
    )


@dataclass(frozen=True)
class ThreeArmCampaignContract:
    staging_plan_sha256: str
    phase_id: str
    model: str
    execution_ready: bool
    blockers: tuple[str, ...]
    no_next_phase: bool
    stream_policy: str
    stream: tuple[ThreeArmStreamItem, ...]
    global_caps: ResourceCaps
    cell_entitlements: dict[str, ResourceCaps]
    online_instances_per_suite: int
    sealed_instances_per_suite: int
    minimum_valid_rounds_per_arm: int
    minimum_paired_learning_tasks: int
    arms: tuple[str, ...] = THREE_ARMS

    @classmethod
    def from_staging_bytes(
        cls, encoded: bytes, *, require_full_stream: bool = True
    ) -> "ThreeArmCampaignContract":
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("three-arm staging plan is invalid JSON") from exc
        if not isinstance(payload, dict) or set(payload) != _STAGING_FIELDS:
            raise ValueError("three-arm staging plan fields differ")
        if payload["schema_version"] != 5:
            raise ValueError("unsupported three-arm staging schema")
        if payload["validity_policy"] != THREE_ARM_VALIDITY_POLICY:
            raise ValueError("three-arm validity policy differs")
        if not isinstance(payload["code_revision"], str) or not _COMMIT.fullmatch(
            payload["code_revision"]
        ):
            raise ValueError("three-arm staging requires a full code revision")
        execution_ready = payload["execution_ready"]
        blockers = payload["blockers"]
        if not isinstance(execution_ready, bool):
            raise ValueError("three-arm execution_ready must be boolean")
        if not isinstance(blockers, list) or not all(
            isinstance(value, str) and value for value in blockers
        ):
            raise ValueError("three-arm blockers must be text")
        if execution_ready and blockers:
            raise ValueError("execution-ready three-arm staging cannot retain blockers")
        if payload["no_next_phase"] is not True:
            raise ValueError("three-arm staging must prohibit automatic next-phase entry")
        if payload["no_paid_provider_fallback"] is not True:
            raise ValueError("three-arm staging must prohibit paid provider fallback")
        if payload["experience_initialization"] != "empty":
            raise ValueError("three-arm experiment must start from empty experience")
        if payload["variant_ids"] != list(THREE_ARMS):
            raise ValueError("three-arm variant order differs")
        if payload["stream_policy"] != "balanced_interleaved":
            raise ValueError("three-arm stream policy must be balanced_interleaved")

        signature = payload["model_signature"]
        if not isinstance(signature, dict) or set(signature) != {
            "executor_model",
            "reasoning_effort",
            "transport",
            "client_version",
        } or not all(isinstance(value, str) and value for value in signature.values()):
            raise ValueError("three-arm model signature is invalid")
        source_hashes = payload["source_hashes"]
        if not isinstance(source_hashes, dict) or not source_hashes or any(
            not isinstance(name, str)
            or not name
            or not isinstance(value, str)
            or not _SHA256.fullmatch(value)
            for name, value in source_hashes.items()
        ):
            raise ValueError("three-arm source hashes are invalid")
        rule_ids = payload["rule_ids"]
        if (
            not isinstance(rule_ids, list)
            or len(rule_ids) != len(set(rule_ids))
            or "cross_instance_distillation" not in rule_ids
        ):
            raise ValueError("three-arm rule ids are incomplete")
        for rule_id in rule_ids:
            _safe_id(rule_id, "three-arm rule id")

        online_count = payload["online_instances_per_suite"]
        sealed_count = payload["sealed_instances_per_suite"]
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value <= 0
            for value in (online_count, sealed_count)
        ):
            raise ValueError("three-arm per-suite counts are invalid")
        if require_full_stream and (online_count, sealed_count) != (6, 2):
            raise ValueError("formal three-arm experiment requires six online and two sealed")

        raw_stream = payload["stream"]
        if not isinstance(raw_stream, list) or not raw_stream:
            raise ValueError("three-arm stream cannot be empty")
        stream = tuple(
            _stream_item(value, expected_index=index)
            for index, value in enumerate(raw_stream)
        )
        if len({item.instance_id for item in stream}) != len(stream):
            raise ValueError("a three-arm instance may appear only once")
        suites = tuple(dict.fromkeys(item.suite for item in stream))
        for suite in suites:
            selected = tuple(item for item in stream if item.suite == suite)
            if tuple(item.block_index for item in selected) != tuple(
                range(len(selected))
            ):
                raise ValueError("each suite must use contiguous task positions")
            modes = tuple(item.learning_mode for item in selected)
            if modes != ("online",) * online_count + ("sealed",) * sealed_count:
                raise ValueError("each suite must test online tasks before sealed tasks")
        if require_full_stream:
            if len(stream) != 24 or len(suites) != 3:
                raise ValueError("formal three-arm stream requires three suites and 24 tasks")
            if any(
                len(tuple(item for item in stream if item.suite == suite)) != 8
                for suite in suites
            ):
                raise ValueError("each formal suite must contain eight tasks")
            for block_index in range(8):
                block = stream[block_index * 3 : (block_index + 1) * 3]
                offset = block_index % len(suites)
                expected_suites = suites[offset:] + suites[:offset]
                if tuple(item.suite for item in block) != expected_suites:
                    raise ValueError("formal stream differs from balanced interleaving")
                if any(item.block_index != block_index for item in block):
                    raise ValueError("formal balanced block index differs")
                expected_mode = "online" if block_index < 6 else "sealed"
                if any(item.learning_mode != expected_mode for item in block):
                    raise ValueError("formal balanced block learning mode differs")

        global_caps = _resource_caps(payload["budgets"], "three-arm global")
        raw_cells = payload["cell_entitlements"]
        if not isinstance(raw_cells, dict):
            raise ValueError("three-arm cell entitlements must be an object")
        cells = {
            _safe_id(cell_id, "three-arm cell id"): _resource_caps(
                value, f"three-arm cell {cell_id}"
            )
            for cell_id, value in raw_cells.items()
        }
        expected_cells: set[str] = set()
        for item in stream:
            for arm in THREE_ARMS:
                cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
                expected_cells.add(cell_id)
                cap = cells.get(cell_id)
                if cap is None or cap.model_calls != 16 or cap.evaluator_transactions != 8:
                    raise ValueError("three-arm cell entitlement differs from eight rounds")
            distill_id = f"distill:{item.stream_index:03d}:{item.instance_id}"
            if item.learning_mode == "online":
                expected_cells.add(distill_id)
                if cells.get(distill_id) != ResourceCaps(model_calls=1):
                    raise ValueError("online instance requires one distillation entitlement")
            elif distill_id in cells:
                raise ValueError("sealed instance cannot distill")
        if set(cells) != expected_cells:
            raise ValueError("three-arm cell entitlement set differs")

        declared_totals = _resource_caps(
            payload["resource_entitlement_totals"], "three-arm entitlement total"
        )
        computed_totals = ResourceCaps(
            model_calls=sum(value.model_calls for value in cells.values()),
            evaluator_transactions=sum(
                value.evaluator_transactions for value in cells.values()
            ),
            gpu_exclusive_seconds=sum(
                value.gpu_exclusive_seconds for value in cells.values()
            ),
            cpu_evaluator_seconds=sum(
                value.cpu_evaluator_seconds for value in cells.values()
            ),
        )
        if declared_totals != computed_totals:
            raise ValueError("three-arm entitlement total does not match its cells")
        for field in (
            "model_calls",
            "evaluator_transactions",
            "gpu_exclusive_seconds",
            "cpu_evaluator_seconds",
        ):
            if getattr(declared_totals, field) > getattr(global_caps, field):
                raise ValueError("three-arm entitlement total exceeds global hard cap")

        return cls(
            staging_plan_sha256=hashlib.sha256(encoded).hexdigest(),
            phase_id=_safe_id(payload["phase_id"], "three-arm phase id"),
            model=signature["executor_model"],
            execution_ready=execution_ready,
            blockers=tuple(blockers),
            no_next_phase=True,
            stream_policy="balanced_interleaved",
            stream=stream,
            global_caps=global_caps,
            cell_entitlements=cells,
            online_instances_per_suite=online_count,
            sealed_instances_per_suite=sealed_count,
            minimum_valid_rounds_per_arm=THREE_ARM_VALIDITY_POLICY[
                "minimum_valid_rounds_per_arm"
            ],
            minimum_paired_learning_tasks=THREE_ARM_VALIDITY_POLICY[
                "minimum_paired_learning_tasks"
            ],
        )

    @classmethod
    def from_staging_path(
        cls, path: Path, *, require_full_stream: bool = True
    ) -> "ThreeArmCampaignContract":
        return cls.from_staging_bytes(
            Path(path).read_bytes(), require_full_stream=require_full_stream
        )

    def require_executable(self) -> None:
        if not self.execution_ready:
            suffix = ", ".join(self.blockers) or "execution_ready=false"
            raise RuntimeError(f"three-arm campaign staging is blocked: {suffix}")


class _ThreeArmState:
    def __init__(
        self,
        stream: tuple[ThreeArmStreamItem, ...],
        *,
        initial_checkpoint_sha256: str,
        start_cursor: int = 0,
    ) -> None:
        if not stream or not _SHA256.fullmatch(initial_checkpoint_sha256):
            raise ValueError("three-arm state requires a stream and checkpoint")
        if (
            isinstance(start_cursor, bool)
            or not isinstance(start_cursor, int)
            or not 0 <= start_cursor < len(stream)
        ):
            raise ValueError("three-arm state start cursor is invalid")
        self._stream = stream
        self._cursor = start_cursor
        self._sealed_arms: set[str] = set()
        self._instance_sealed = False
        self.online_checkpoint_sha256 = initial_checkpoint_sha256

    @property
    def current(self) -> ThreeArmStreamItem:
        if self._cursor >= len(self._stream):
            raise StopIteration("three-arm stream is complete")
        return self._stream[self._cursor]

    @property
    def ready_for_distillation(self) -> bool:
        return self._instance_sealed and self.current.learning_mode == "online"

    def seal_arm(self, arm: str) -> None:
        if self._instance_sealed or arm not in THREE_ARMS or arm in self._sealed_arms:
            raise ValueError("invalid three-arm seal transition")
        self._sealed_arms.add(arm)

    def seal_instance(self) -> None:
        if self._instance_sealed or self._sealed_arms != set(THREE_ARMS):
            raise ValueError("all three arms must seal before the instance")
        self._instance_sealed = True

    def apply_distillation(self, checkpoint_sha256: str) -> None:
        if not self.ready_for_distillation or not _SHA256.fullmatch(checkpoint_sha256):
            raise ValueError("online instance must seal before distillation")
        self.online_checkpoint_sha256 = checkpoint_sha256
        self._advance()

    def advance_without_learning(self) -> None:
        if not self._instance_sealed or self.current.learning_mode != "sealed":
            raise ValueError("only a sealed holdout may advance without learning")
        self._advance()

    def _advance(self) -> None:
        self._cursor += 1
        self._sealed_arms.clear()
        self._instance_sealed = False


@dataclass(frozen=True)
class ThreeArmCampaignResult:
    sealed: bool
    completed_instance_ids: tuple[str, ...]
    newly_executed_instances: int
    newly_executed_arm_cells: int
    replayed_instances: int
    online_checkpoint_sha256: str
    online_bank_sha256: str
    first_encounter_summary_sha256: str | None


class ThreeArmCampaignRunner(FormalCampaignRunner):
    """Run/recover the three-arm stream at an arm-cell transaction boundary."""

    def __init__(
        self,
        *,
        artifact_root: Path,
        contract: ThreeArmCampaignContract,
        variants: tuple[BuilderVariant, ...],
        operator_registry: TrustedOperatorRegistry,
        model_gateway: IsolatedModelGateway,
        provider_factory: FormalProviderFactory,
        initial_empty_bank: ExperienceBankSnapshot,
        initial_empty_checkpoint: BuilderCheckpoint,
        task_conditioned_checkpoint_sha256: str,
        execution_start_index: int = 0,
        initial_online_bank: ExperienceBankSnapshot | None = None,
        initial_online_checkpoint: BuilderCheckpoint | None = None,
    ) -> None:
        self.execution_start_index = execution_start_index
        self.initial_online_bank = initial_online_bank or initial_empty_bank
        self.initial_online_checkpoint = (
            initial_online_checkpoint or initial_empty_checkpoint
        )
        super().__init__(
            artifact_root=artifact_root,
            contract=contract,  # type: ignore[arg-type]
            variants=variants,
            operator_registry=operator_registry,
            model_gateway=model_gateway,
            provider_factory=provider_factory,
            initial_trained_bank=initial_empty_bank,
            initial_trained_checkpoint=initial_empty_checkpoint,
            untrained_checkpoint_sha256=task_conditioned_checkpoint_sha256,
        )

    def _validate_bindings(self) -> None:
        if set(self.variants) != set(THREE_ARMS) or len(self.variants) != 3:
            raise ValueError("three-arm runner requires A/B-frozen/B-online")
        a = self.variants["A"]
        frozen = self.variants["B-frozen"]
        online = self.variants["B-online"]
        if (
            not a.freeze_after_initial
            or a.continual_update
            or frozen.freeze_after_initial
            or frozen.continual_update
            or online.freeze_after_initial
            or not online.continual_update
        ):
            raise ValueError("three-arm Builder variant semantics differ")
        if a.experience_sources or frozen.experience_sources or online.experience_sources:
            raise ValueError("three-arm experiment must start without history")
        if (
            frozen.rule_registry_sha256 != online.rule_registry_sha256
            or frozen.allowed_rule_ids != online.allowed_rule_ids
            or frozen.excluded_task_ids != online.excluded_task_ids
        ):
            raise ValueError("B-frozen and B-online must share one byte-identical start")
        if frozen.rule_registry_sha256 != self.operator_registry.rule_registry_sha256:
            raise ValueError("three-arm Rule Registry binding differs")
        heldout = {item.instance_id for item in self.contract.stream}
        if set(frozen.excluded_task_ids) != heldout:
            raise ValueError("three-arm held-out exclusion set differs from the stream")
        if self.initial_bank.records:
            raise ValueError("three-arm initial Experience Bank must be empty")
        if (
            self.initial_checkpoint.experience_bank_sha256 != self.initial_bank.sha256
            or self.initial_checkpoint.rule_registry_sha256
            != self.operator_registry.rule_registry_sha256
        ):
            raise ValueError("initial empty checkpoint does not bind its bank and rules")
        if (
            isinstance(self.execution_start_index, bool)
            or not isinstance(self.execution_start_index, int)
            or not 0 <= self.execution_start_index < len(self.contract.stream)
        ):
            raise ValueError("three-arm execution start index is invalid")
        if (
            self.initial_online_checkpoint.experience_bank_sha256
            != self.initial_online_bank.sha256
            or self.initial_online_checkpoint.rule_registry_sha256
            != self.operator_registry.rule_registry_sha256
        ):
            raise ValueError("initial online checkpoint does not bind its bank and rules")
        if self.execution_start_index == 0:
            if (
                self.initial_online_bank.sha256 != self.initial_bank.sha256
                or self.initial_online_checkpoint.sha256
                != self.initial_checkpoint.sha256
            ):
                raise ValueError("fresh three-arm campaign cannot import online experience")
        else:
            prefix = self.contract.stream[: self.execution_start_index]
            if (
                self.initial_online_checkpoint.stream_index
                != self.execution_start_index - 1
                or self.initial_online_checkpoint.learned_through_instance
                != prefix[-1].instance_id
            ):
                raise ValueError("successor online checkpoint boundary differs")
            source_ids = tuple(
                record.source_instance_id for record in self.initial_online_bank.records
            )
            if source_ids != tuple(item.instance_id for item in prefix):
                raise ValueError("successor online Bank sources differ from prefix")
        if self.provider_factory.staging_plan_sha256 != self.contract.staging_plan_sha256:
            raise ValueError("three-arm provider factory is bound to another staging plan")
        governor = self.model_gateway.governor
        if governor.global_caps != self.contract.global_caps:
            raise ValueError("three-arm ResourceGovernor global caps differ from staging")
        if governor.cell_caps != self.contract.cell_entitlements:
            raise ValueError("three-arm ResourceGovernor cell caps differ from staging")

    def _arm_experience_binding(
        self,
        *,
        arm: str,
        state: _ThreeArmState,
        online_bank: ExperienceBankSnapshot,
    ) -> tuple[str, ExperienceBankSnapshot | None]:
        if arm == "A":
            return self.untrained_checkpoint_sha256, None
        if arm == "B-frozen":
            return self.initial_checkpoint.sha256, self.initial_bank
        if arm == "B-online":
            return state.online_checkpoint_sha256, online_bank
        raise ValueError("unknown three-arm experiment arm")

    def _cross_instance_memory_grant(
        self,
        *,
        item: ThreeArmStreamItem,
        arm: str,
        checkpoint_sha256: str,
        bank: ExperienceBankSnapshot | None,
        records: tuple[dict[str, str], ...],
    ) -> CrossInstanceMemoryGrant | None:
        if arm != "B-online" or bank is None or not records:
            return None
        eligible_sources = tuple(
            prior.instance_id
            for prior in self.contract.stream
            if prior.stream_index < item.stream_index
        )
        return CrossInstanceMemoryGrant.issue(
            stream_index=item.stream_index,
            checkpoint_sha256=checkpoint_sha256,
            experience_bank_sha256=bank.sha256,
            records=records,
            eligible_source_instance_ids=eligible_sources,
        )

    @staticmethod
    def _curve(
        result,
        checkpoint_sha256: str,
        bank_sha256: str | None,
        records: tuple[dict[str, str], ...],
    ) -> dict[str, Any]:
        curve = FormalCampaignRunner._curve(
            result, checkpoint_sha256, bank_sha256, records
        )
        valid_scores = [
            float(attempt.score)
            for attempt in result.attempts
            if attempt.correct and attempt.score is not None
        ]
        sufficient = len(valid_scores) >= THREE_ARM_VALIDITY_POLICY[
            "minimum_valid_rounds_per_arm"
        ]
        curve.update(
            {
                "attempted_rounds": len(result.attempts),
                "valid_rounds": len(valid_scores),
                "invalid_rounds": len(result.attempts) - len(valid_scores),
                "validity_status": (
                    "sufficient_validity"
                    if sufficient
                    else THREE_ARM_VALIDITY_POLICY["insufficient_status"]
                ),
                "valid_only_mean": (
                    sum(valid_scores) / len(valid_scores) if sufficient else None
                ),
                "best_score": max(valid_scores) if sufficient else None,
            }
        )
        return curve

    def run(self, *, max_new_arm_cells: int | None = None) -> ThreeArmCampaignResult:
        if max_new_arm_cells is not None and (
            isinstance(max_new_arm_cells, bool) or max_new_arm_cells <= 0
        ):
            raise ValueError("max_new_arm_cells must be positive")
        state = _ThreeArmState(
            self.contract.stream,
            initial_checkpoint_sha256=self.initial_online_checkpoint.sha256,
            start_cursor=self.execution_start_index,
        )
        online_bank = self.initial_online_bank
        completed: list[str] = []
        newly_executed_instances = 0
        newly_executed_arm_cells = 0
        replayed = 0
        receipt_hashes: list[str] = []

        execution_stream = self.contract.stream[self.execution_start_index :]
        for item in execution_stream:
            if state.current != item:
                raise ValueError("three-arm reducer diverged from staging order")
            receipt_path = self._instance_receipt_path(item)
            if receipt_path.is_file():
                replay_binding = (
                    self._binding_for(item)  # type: ignore[arg-type]
                    if any(
                        self._requires_trusted_cell_replay(arm)
                        for arm in THREE_ARMS
                    )
                    else None
                )
                payload, receipt_sha, online_bank = self._replay_instance_receipt_v2(
                    item=item,
                    state=state,
                    online_bank=online_bank,
                    path=receipt_path,
                    binding=replay_binding,
                )
                self._append_instance_fact(item, payload, receipt_sha)
                receipt_hashes.append(receipt_sha)
                completed.append(item.instance_id)
                replayed += 1
                continue

            input_checkpoint_sha = state.online_checkpoint_sha256
            input_bank_sha = online_bank.sha256
            binding = self._binding_for(item)  # type: ignore[arg-type]
            arm_receipts: dict[str, _ArmReceipt] = {}
            for arm_index, arm in enumerate(item.arm_order):
                arm_path = self._arm_receipt_path(item, arm)
                existed = arm_path.is_file()
                checkpoint_sha, bank = self._arm_experience_binding(
                    arm=arm, state=state, online_bank=online_bank
                )
                arm_receipts[arm] = self._run_or_replay_arm(
                    item=item,  # type: ignore[arg-type]
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha,
                    bank=bank,
                )
                state.seal_arm(arm)
                if not existed:
                    newly_executed_arm_cells += 1
                if (
                    max_new_arm_cells is not None
                    and newly_executed_arm_cells >= max_new_arm_cells
                    and arm_index < len(item.arm_order) - 1
                ):
                    return self._partial_result(
                        completed=completed,
                        newly_executed_instances=newly_executed_instances,
                        newly_executed_arm_cells=newly_executed_arm_cells,
                        replayed=replayed,
                        state=state,
                        online_bank=online_bank,
                    )
            state.seal_instance()

            # Only B-online's own public trajectory may teach B-online.  Control
            # arm outputs remain evaluation evidence and never leak into memory.
            online_receipt = arm_receipts["B-online"]
            trajectory = SealedInstanceTrajectory(
                instance_id=item.instance_id,
                suite=item.suite,
                builder_checkpoint_sha256=input_checkpoint_sha,
                arm_event_ids={
                    "B-online": tuple(online_receipt.payload["round_event_ids"])
                },
                public_summary={"B-online": online_receipt.payload["curve"]},
                sealed=True,
            )
            trajectory_sha = self._store_trajectory(item, trajectory)  # type: ignore[arg-type]
            distillation_operation_id: str | None
            if item.learning_mode == "online":
                update = self._distill(
                    item=item,  # type: ignore[arg-type]
                    state=state,  # type: ignore[arg-type]
                    trajectory=trajectory,
                    bank=online_bank,
                )
                online_bank = update.bank
                output_checkpoint_sha = update.checkpoint.sha256
                distillation_operation_id = self._distillation_operation_id(item)  # type: ignore[arg-type]
            else:
                state.advance_without_learning()
                output_checkpoint_sha = input_checkpoint_sha
                distillation_operation_id = None

            receipt = {
                "schema_version": 2,
                "phase_id": self.contract.phase_id,
                "staging_plan_sha256": self.contract.staging_plan_sha256,
                "stream_item": item.to_dict(),
                "learning_mode": item.learning_mode,
                "first_encounter": True,
                "same_instance_rerun_policy": "replay_only_no_formal_update",
                "task_binding_sha256": binding.task_binding_sha256,
                "input_online_checkpoint_sha256": input_checkpoint_sha,
                "input_online_bank_sha256": input_bank_sha,
                "arm_order": list(item.arm_order),
                "arm_receipt_sha256s": {
                    arm: arm_receipts[arm].sha256 for arm in THREE_ARMS
                },
                "trajectory_sha256": trajectory_sha,
                "distillation_operation_id": distillation_operation_id,
                "output_online_bank_sha256": online_bank.sha256,
                "output_online_checkpoint_sha256": output_checkpoint_sha,
                "sealed": True,
                "no_next_phase": True,
            }
            encoded = _canonical_bytes(receipt)
            _write_once(receipt_path, encoded)
            receipt_sha = _sha256_bytes(encoded)
            self._append_instance_fact(item, receipt, receipt_sha)  # type: ignore[arg-type]
            receipt_hashes.append(receipt_sha)
            completed.append(item.instance_id)
            newly_executed_instances += 1
            if (
                max_new_arm_cells is not None
                and newly_executed_arm_cells >= max_new_arm_cells
                and len(completed) < len(execution_stream)
            ):
                return self._partial_result(
                    completed=completed,
                    newly_executed_instances=newly_executed_instances,
                    newly_executed_arm_cells=newly_executed_arm_cells,
                    replayed=replayed,
                    state=state,
                    online_bank=online_bank,
                )

        summary = {
            "schema_version": 2,
            "phase_id": self.contract.phase_id,
            "staging_plan_sha256": self.contract.staging_plan_sha256,
            "learning_policy": "score_then_distill_B-online_before_next_unseen_task",
            "stream_instance_ids": [item.instance_id for item in execution_stream],
            "instance_receipt_sha256s": receipt_hashes,
            "final_online_checkpoint_sha256": state.online_checkpoint_sha256,
            "final_online_bank_sha256": online_bank.sha256,
            "sealed": True,
            "no_next_phase": True,
        }
        summary_bytes = _canonical_bytes(summary)
        summary_sha = _sha256_bytes(summary_bytes)
        _write_once(
            self.formal_root / "first_encounter_summaries" / f"{summary_sha}.json",
            summary_bytes,
        )
        _write_once(
            self.formal_root / "campaign_receipt.json",
            _canonical_bytes(
                {
                    "schema_version": 2,
                    "staging_plan_sha256": self.contract.staging_plan_sha256,
                    "summary_sha256": summary_sha,
                    "sealed": True,
                    "no_next_phase": True,
                }
            ),
        )
        event_payload = {
            "summary_sha256": summary_sha,
            "instance_count": len(completed),
            "final_online_checkpoint_sha256": state.online_checkpoint_sha256,
            "final_online_bank_sha256": online_bank.sha256,
        }
        event = self.registry.append(
            "hb_three_arm_campaign_sealed",
            event_payload,
            event_id=f"hb-three-arm-campaign:{summary_sha}",
        )
        if event.get("payload") != event_payload:
            raise ValueError("three-arm campaign fact is rebound")
        return ThreeArmCampaignResult(
            sealed=True,
            completed_instance_ids=tuple(completed),
            newly_executed_instances=newly_executed_instances,
            newly_executed_arm_cells=newly_executed_arm_cells,
            replayed_instances=replayed,
            online_checkpoint_sha256=state.online_checkpoint_sha256,
            online_bank_sha256=online_bank.sha256,
            first_encounter_summary_sha256=summary_sha,
        )

    def _partial_result(
        self,
        *,
        completed: list[str],
        newly_executed_instances: int,
        newly_executed_arm_cells: int,
        replayed: int,
        state: _ThreeArmState,
        online_bank: ExperienceBankSnapshot,
    ) -> ThreeArmCampaignResult:
        return ThreeArmCampaignResult(
            sealed=False,
            completed_instance_ids=tuple(completed),
            newly_executed_instances=newly_executed_instances,
            newly_executed_arm_cells=newly_executed_arm_cells,
            replayed_instances=replayed,
            online_checkpoint_sha256=state.online_checkpoint_sha256,
            online_bank_sha256=online_bank.sha256,
            first_encounter_summary_sha256=None,
        )

    def _replay_instance_receipt_v2(
        self,
        *,
        item: ThreeArmStreamItem,
        state: _ThreeArmState,
        online_bank: ExperienceBankSnapshot,
        path: Path,
        binding: FormalTaskBinding | None = None,
    ) -> tuple[dict[str, Any], str, ExperienceBankSnapshot]:
        encoded = path.read_bytes()
        payload = self._canonical_object(encoded, "three-arm instance receipt")
        expected = {
            "schema_version",
            "phase_id",
            "staging_plan_sha256",
            "stream_item",
            "learning_mode",
            "first_encounter",
            "same_instance_rerun_policy",
            "task_binding_sha256",
            "input_online_checkpoint_sha256",
            "input_online_bank_sha256",
            "arm_order",
            "arm_receipt_sha256s",
            "trajectory_sha256",
            "distillation_operation_id",
            "output_online_bank_sha256",
            "output_online_checkpoint_sha256",
            "sealed",
            "no_next_phase",
        }
        if set(payload) != expected or (
            payload["schema_version"] != 2
            or payload["phase_id"] != self.contract.phase_id
            or payload["staging_plan_sha256"] != self.contract.staging_plan_sha256
            or payload["stream_item"] != item.to_dict()
            or payload["learning_mode"] != item.learning_mode
            or payload["first_encounter"] is not True
            or payload["same_instance_rerun_policy"]
            != "replay_only_no_formal_update"
            or payload["input_online_checkpoint_sha256"]
            != state.online_checkpoint_sha256
            or payload["input_online_bank_sha256"] != online_bank.sha256
            or payload["arm_order"] != list(item.arm_order)
            or set(payload["arm_receipt_sha256s"]) != set(THREE_ARMS)
            or payload["sealed"] is not True
            or payload["no_next_phase"] is not True
        ):
            raise ValueError("three-arm instance receipt binding differs")
        if binding is not None and (
            binding.task_binding_sha256 != payload["task_binding_sha256"]
        ):
            raise ValueError("three-arm replay task binding differs")
        for arm in THREE_ARMS:
            arm_path = self._arm_receipt_path(item, arm)
            arm_encoded = arm_path.read_bytes()
            if _sha256_bytes(arm_encoded) != payload["arm_receipt_sha256s"][arm]:
                raise ValueError("three-arm instance arm receipt hash differs")
            checkpoint_sha, bank = self._arm_experience_binding(
                arm=arm, state=state, online_bank=online_bank
            )
            receipt = self._load_arm_receipt(
                path=arm_path,
                item=item,  # type: ignore[arg-type]
                arm=arm,
                task_binding_sha256=payload["task_binding_sha256"],
                checkpoint_sha256=checkpoint_sha,
                bank_sha256=bank.sha256 if bank is not None else None,
            )
            if self._requires_trusted_cell_replay(arm):
                if binding is None:
                    raise ValueError(
                        "wide Harness instance replay requires a trusted task binding"
                    )
                records, memory_grant = self._arm_runtime_inputs(
                    item=item,  # type: ignore[arg-type]
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha,
                    bank=bank,
                )
                self._trusted_replay_wide_arm(
                    item=item,  # type: ignore[arg-type]
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha,
                    bank_sha256=bank.sha256 if bank is not None else None,
                    records=records,
                    memory_grant=memory_grant,
                    receipt=receipt,
                )
        trajectory_path = (
            self.formal_root
            / "trajectories"
            / "objects"
            / f"{payload['trajectory_sha256']}.json"
        )
        if (
            not trajectory_path.is_file()
            or _sha256_bytes(trajectory_path.read_bytes()) != payload["trajectory_sha256"]
        ):
            raise ValueError("three-arm sealed trajectory hash differs")
        for arm in item.arm_order:
            state.seal_arm(arm)
        state.seal_instance()

        if item.learning_mode == "online":
            expected_operation = self._distillation_operation_id(item)  # type: ignore[arg-type]
            if payload["distillation_operation_id"] != expected_operation:
                raise ValueError("three-arm distillation operation binding differs")
            updated_bank = self._load_bank(payload["output_online_bank_sha256"])
            updated_checkpoint = self._load_checkpoint(
                payload["output_online_checkpoint_sha256"]
            )
            if (
                updated_bank.parent_sha256 != online_bank.sha256
                or updated_checkpoint.parent_checkpoint_sha256
                != state.online_checkpoint_sha256
                or updated_checkpoint.experience_bank_sha256 != updated_bank.sha256
                or updated_checkpoint.learned_through_instance != item.instance_id
                or updated_checkpoint.stream_index != item.stream_index
            ):
                raise ValueError("replayed three-arm parent chain differs")
            operation = self.model_gateway.governor.journal.replay().operations.get(
                expected_operation
            )
            if (
                operation is None
                or operation.state != "completed"
                or operation.cell_id != self._distillation_cell_id(item)  # type: ignore[arg-type]
                or operation.operation_kind != "distillation_call"
            ):
                raise ValueError("three-arm distillation operation is incomplete")
            state.apply_distillation(updated_checkpoint.sha256)
            return payload, _sha256_bytes(encoded), updated_bank

        if (
            payload["distillation_operation_id"] is not None
            or payload["output_online_bank_sha256"] != online_bank.sha256
            or payload["output_online_checkpoint_sha256"]
            != state.online_checkpoint_sha256
        ):
            raise ValueError("sealed holdout changed online experience")
        state.advance_without_learning()
        return payload, _sha256_bytes(encoded), online_bank


__all__ = [
    "THREE_ARMS",
    "ThreeArmCampaignContract",
    "ThreeArmCampaignResult",
    "ThreeArmCampaignRunner",
    "ThreeArmStreamItem",
]
