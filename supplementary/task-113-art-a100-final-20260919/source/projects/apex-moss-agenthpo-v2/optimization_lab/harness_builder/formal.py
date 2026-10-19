from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol

from optimization_lab.registry import ExperimentRegistry

from ._safe_artifacts import (
    ensure_safe_directory,
    lexical_absolute,
    read_safe_regular_file,
    safe_regular_file_exists,
    write_once_safe_regular_file,
)
from .events import ResourceCaps
from .experience import ExperienceRecord
from .learning import (
    BuilderCheckpoint,
    BuilderCheckpointArchive,
    ContinualUpdater,
    ExperienceBankArchive,
    ExperienceBankSnapshot,
    SealedInstanceTrajectory,
)
from .model_gateway import GatewayGenerator, IsolatedModelGateway
from .operators import CrossInstanceMemoryGrant, TrustedOperatorRegistry
from .runner import CellRunResult, HarnessBuilderCellRunner, SolutionCodec
from .schema import BuilderVariant
from .stream import ARMS, PrequentialState, StreamItem
from .evaluation import EvaluationBackend


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9*._:/+-]{0,255}")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -]evaluator|private[_ -]log)", re.IGNORECASE
)
_STAGING_REQUIRED = {
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
    "stream",
    "no_next_phase",
    "no_paid_provider_fallback",
}


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _write_once(path: Path, content: bytes) -> None:
    write_once_safe_regular_file(
        path,
        content,
        label=f"sealed formal artifact {path.name}",
        temporary_suffix=".hb-formal.tmp",
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise ValueError(f"unsafe {label}")
    return value


def _sha256(value: Any, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"invalid {label}")
    return value


def _resource_caps(payload: Any, label: str) -> ResourceCaps:
    if not isinstance(payload, dict) or set(payload) != {
        "model_calls",
        "evaluator_transactions",
        "gpu_exclusive_seconds",
        "cpu_evaluator_seconds",
    }:
        raise ValueError(f"{label} resource fields differ")
    try:
        return ResourceCaps(**payload)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid {label} resources") from exc


def _stream_item(payload: Any, *, expected_index: int) -> StreamItem:
    expected = {
        "stream_index",
        "block_index",
        "suite",
        "task_id",
        "instance_id",
        "arm_order",
    }
    if not isinstance(payload, dict) or set(payload) != expected:
        raise ValueError("formal stream item fields differ")
    if payload["stream_index"] != expected_index:
        raise ValueError("formal stream index is not contiguous")
    block_index = payload["block_index"]
    if isinstance(block_index, bool) or not isinstance(block_index, int) or block_index < 0:
        raise ValueError("formal block index is invalid")
    suite = _safe_id(payload["suite"], "formal suite")
    task_id = _safe_id(payload["task_id"], "formal task id")
    instance_id = f"{suite}:{task_id}"
    if payload["instance_id"] != instance_id:
        raise ValueError("formal instance id binding differs")
    raw_order = payload["arm_order"]
    if not isinstance(raw_order, list) or set(raw_order) != set(ARMS) or len(raw_order) != 4:
        raise ValueError("formal arm order must contain each arm exactly once")
    return StreamItem(
        stream_index=expected_index,
        block_index=block_index,
        suite=suite,
        task_id=task_id,
        arm_order=tuple(raw_order),
    )


@dataclass(frozen=True)
class FormalCampaignContract:
    staging_plan_sha256: str
    phase_id: str
    model: str
    execution_ready: bool
    blockers: tuple[str, ...]
    no_next_phase: bool
    stream: tuple[StreamItem, ...]
    global_caps: ResourceCaps
    cell_entitlements: dict[str, ResourceCaps]

    @classmethod
    def from_staging_bytes(
        cls,
        encoded: bytes,
        *,
        require_full_stream: bool = True,
    ) -> "FormalCampaignContract":
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("formal staging plan is invalid JSON") from exc
        if not isinstance(payload, dict) or set(payload) != _STAGING_REQUIRED:
            raise ValueError("formal staging plan fields differ")
        if payload["schema_version"] != 1:
            raise ValueError("unsupported formal staging schema")
        execution_ready = payload["execution_ready"]
        if not isinstance(execution_ready, bool):
            raise ValueError("staging execution_ready must be boolean")
        raw_blockers = payload["blockers"]
        if not isinstance(raw_blockers, list) or not all(
            isinstance(value, str) and value for value in raw_blockers
        ):
            raise ValueError("formal blockers must be text")
        if execution_ready and raw_blockers:
            raise ValueError("an execution-ready staging plan cannot retain blockers")
        if payload["no_next_phase"] is not True:
            raise ValueError("formal staging must prohibit automatic next-phase entry")
        if payload["no_paid_provider_fallback"] is not True:
            raise ValueError("formal staging must prohibit provider fallback")
        if payload["variant_ids"] != list(ARMS):
            raise ValueError("formal staging variant order differs")
        signature = payload["model_signature"]
        if not isinstance(signature, dict) or not isinstance(
            signature.get("executor_model"), str
        ):
            raise ValueError("formal model signature is invalid")
        raw_stream = payload["stream"]
        if not isinstance(raw_stream, list) or not raw_stream:
            raise ValueError("formal stream cannot be empty")
        stream = tuple(
            _stream_item(item, expected_index=index)
            for index, item in enumerate(raw_stream)
        )
        if len({item.instance_id for item in stream}) != len(stream):
            raise ValueError("a formal instance may appear only once")
        if require_full_stream:
            if len(stream) != 24:
                raise ValueError("formal HB-GEN-1 requires 24 first encounters")
            suites = {item.suite for item in stream}
            if len(suites) != 3 or any(
                sum(item.suite == suite for item in stream) != 8 for suite in suites
            ):
                raise ValueError("formal stream must contain eight instances per suite")

        global_caps = _resource_caps(payload["budgets"], "global")
        raw_cells = payload["cell_entitlements"]
        if not isinstance(raw_cells, dict):
            raise ValueError("formal cell entitlements must be an object")
        cells = {
            _safe_id(cell_id, "cell entitlement id"): _resource_caps(
                value, f"cell {cell_id}"
            )
            for cell_id, value in raw_cells.items()
        }
        declared_totals = _resource_caps(
            payload["resource_entitlement_totals"], "entitlement total"
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
            raise ValueError("formal entitlement total does not match its cells")
        for field in (
            "model_calls",
            "evaluator_transactions",
            "gpu_exclusive_seconds",
            "cpu_evaluator_seconds",
        ):
            if getattr(declared_totals, field) > getattr(global_caps, field):
                raise ValueError("formal entitlement total exceeds a global hard cap")
        for item in stream:
            for arm in ARMS:
                cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
                cap = cells.get(cell_id)
                if cap is None or cap.model_calls != 16 or cap.evaluator_transactions != 11:
                    raise ValueError("formal cell entitlement differs from v001-v008 contract")
            distill_id = f"distill:{item.stream_index:03d}:{item.instance_id}"
            if cells.get(distill_id) != ResourceCaps(model_calls=1):
                raise ValueError("formal distillation entitlement differs")
        return cls(
            staging_plan_sha256=_sha256_bytes(encoded),
            phase_id=_safe_id(payload["phase_id"], "formal phase id"),
            model=signature["executor_model"],
            execution_ready=execution_ready,
            blockers=tuple(raw_blockers),
            no_next_phase=True,
            stream=stream,
            global_caps=global_caps,
            cell_entitlements=cells,
        )

    @classmethod
    def from_staging_path(
        cls, path: Path, *, require_full_stream: bool = True
    ) -> "FormalCampaignContract":
        return cls.from_staging_bytes(
            Path(path).read_bytes(), require_full_stream=require_full_stream
        )

    def require_executable(self) -> None:
        if not self.execution_ready:
            suffix = ", ".join(self.blockers) or "execution_ready=false"
            raise RuntimeError(f"formal campaign staging is blocked: {suffix}")


@dataclass(frozen=True)
class FormalTaskBinding:
    suite: str
    task_id: str
    instance_id: str
    task_binding_sha256: str
    task_card: str
    reference_artifact: str
    instance_descriptors: tuple[str, ...]
    solution_codec: SolutionCodec
    evaluator: EvaluationBackend

    def validate_for(self, item: StreamItem) -> None:
        if (
            self.suite != item.suite
            or self.task_id != item.task_id
            or self.instance_id != item.instance_id
        ):
            raise ValueError("formal task provider rebound the stream item")
        _sha256(self.task_binding_sha256, "formal task binding sha256")
        if not self.task_card.strip() or not self.reference_artifact.strip():
            raise ValueError("formal task card and reference artifact are required")
        if not self.instance_descriptors or not all(
            isinstance(value, str) and value.strip()
            for value in self.instance_descriptors
        ):
            raise ValueError("formal task descriptors are required")


class FormalSuiteProvider(Protocol):
    suite: str

    def bind(self, item: StreamItem) -> FormalTaskBinding: ...


class FormalProviderFactory(Protocol):
    staging_plan_sha256: str

    def create(self, suite: str) -> FormalSuiteProvider: ...


@dataclass(frozen=True)
class FormalCampaignResult:
    sealed: bool
    completed_instance_ids: tuple[str, ...]
    newly_executed_instances: int
    replayed_instances: int
    online_checkpoint_sha256: str
    online_bank_sha256: str
    first_encounter_summary_sha256: str


@dataclass(frozen=True)
class _ArmReceipt:
    sha256: str
    payload: dict[str, Any]


class FormalCampaignRunner:
    """Execute/replay the frozen 24-instance prequential formal campaign.

    The runner owns sequencing only.  Suite code and evaluators arrive through a
    staging-bound provider factory; no evaluator authority is exposed to a Builder.
    """

    def __init__(
        self,
        *,
        artifact_root: Path,
        contract: FormalCampaignContract,
        variants: tuple[BuilderVariant, ...],
        operator_registry: TrustedOperatorRegistry,
        model_gateway: IsolatedModelGateway,
        provider_factory: FormalProviderFactory,
        initial_trained_bank: ExperienceBankSnapshot,
        initial_trained_checkpoint: BuilderCheckpoint,
        untrained_checkpoint_sha256: str,
    ) -> None:
        contract.require_executable()
        self.artifact_root = ensure_safe_directory(
            lexical_absolute(artifact_root), label="formal campaign artifact root"
        )
        self.formal_root = ensure_safe_directory(
            self.artifact_root / "formal", label="formal campaign state root"
        )
        self.contract = contract
        self.operator_registry = operator_registry
        self.model_gateway = model_gateway
        self.provider_factory = provider_factory
        self.initial_bank = initial_trained_bank
        self.initial_checkpoint = initial_trained_checkpoint
        self.untrained_checkpoint_sha256 = _sha256(
            untrained_checkpoint_sha256, "untrained Builder checkpoint"
        )
        self.registry = ExperimentRegistry(
            self.formal_root,
            integrity_mode=(
                "hash_chain_v1"
                if any(
                    variant.adaptation_policy
                    in {"targeted_any_change_v1", "wide_all_fields_recompile_v1"}
                    for variant in variants
                )
                else "legacy"
            ),
        )
        self.bank_archive = ExperienceBankArchive(
            self.formal_root / "experience_banks"
        )
        self.checkpoint_archive = BuilderCheckpointArchive(
            self.formal_root / "builder_checkpoints"
        )
        self.variants = {variant.variant_id: variant for variant in variants}
        self._providers: dict[str, FormalSuiteProvider] = {}
        self._validate_bindings()
        self.bank_archive.store(self.initial_bank)
        self.checkpoint_archive.store(self.initial_checkpoint)

    def _validate_bindings(self) -> None:
        if set(self.variants) != set(ARMS) or len(self.variants) != 4:
            raise ValueError("formal runner requires exactly A/B0/B*/B-online")
        a = self.variants["A"]
        b0 = self.variants["B0"]
        trained = self.variants["B*"]
        online = self.variants["B-online"]
        if (
            not a.freeze_after_initial
            or a.continual_update
            or b0.freeze_after_initial
            or b0.continual_update
            or trained.freeze_after_initial
            or trained.continual_update
            or online.freeze_after_initial
            or not online.continual_update
        ):
            raise ValueError("formal Builder variant semantics differ")
        if a.experience_sources or b0.experience_sources:
            raise ValueError("A/B0 cannot receive cross-instance experience")
        if (
            trained.rule_registry_sha256 != online.rule_registry_sha256
            or trained.allowed_rule_ids != online.allowed_rule_ids
            or trained.experience_sources != online.experience_sources
            or trained.excluded_task_ids != online.excluded_task_ids
        ):
            raise ValueError("B* and B-online do not share one byte-identical start")
        if trained.rule_registry_sha256 != self.operator_registry.rule_registry_sha256:
            raise ValueError("formal Rule Registry binding differs")
        heldout = {item.instance_id for item in self.contract.stream}
        if set(trained.excluded_task_ids) != heldout:
            raise ValueError("formal held-out exclusion set differs from the stream")
        if any(record.source_instance_id in heldout for record in self.initial_bank.records):
            raise ValueError("trained Experience Bank contains a formal held-out instance")
        if (
            self.initial_checkpoint.experience_bank_sha256 != self.initial_bank.sha256
            or self.initial_checkpoint.rule_registry_sha256
            != self.operator_registry.rule_registry_sha256
        ):
            raise ValueError("initial trained checkpoint does not bind its bank and rules")
        if self.provider_factory.staging_plan_sha256 != self.contract.staging_plan_sha256:
            raise ValueError("formal provider factory is bound to another staging plan")
        governor = self.model_gateway.governor
        if governor.global_caps != self.contract.global_caps:
            raise ValueError("formal ResourceGovernor global caps differ from staging")
        if governor.cell_caps != self.contract.cell_entitlements:
            raise ValueError("formal ResourceGovernor cell caps differ from staging")

    def run(self) -> FormalCampaignResult:
        state = PrequentialState(
            self.contract.stream,
            initial_checkpoint_sha256=self.initial_checkpoint.sha256,
        )
        online_bank = self.initial_bank
        completed: list[str] = []
        newly_executed = 0
        replayed = 0
        receipt_hashes: list[str] = []

        for item in self.contract.stream:
            if state.current != item:
                raise ValueError("formal prequential reducer diverged from staging order")
            receipt_path = self._instance_receipt_path(item)
            if safe_regular_file_exists(
                receipt_path, label="formal instance receipt"
            ):
                replay_binding = (
                    self._binding_for(item)
                    if any(
                        self._requires_trusted_cell_replay(arm) for arm in ARMS
                    )
                    else None
                )
                payload, receipt_sha, online_bank = self._replay_instance_receipt(
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
            binding = self._binding_for(item)
            arm_receipts: dict[str, _ArmReceipt] = {}
            for arm in item.arm_order:
                checkpoint_sha, bank = self._arm_experience_binding(
                    arm=arm,
                    state=state,
                    online_bank=online_bank,
                )
                receipt = self._run_or_replay_arm(
                    item=item,
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha,
                    bank=bank,
                )
                arm_receipts[arm] = receipt
                state.seal_arm(arm)
            state.seal_instance()

            trajectory = SealedInstanceTrajectory(
                instance_id=item.instance_id,
                suite=item.suite,
                builder_checkpoint_sha256=input_checkpoint_sha,
                arm_event_ids={
                    arm: tuple(arm_receipts[arm].payload["round_event_ids"])
                    for arm in ARMS
                },
                public_summary={
                    arm: arm_receipts[arm].payload["curve"] for arm in ARMS
                },
                sealed=True,
            )
            trajectory_sha = self._store_trajectory(item, trajectory)
            update = self._distill(
                item=item,
                state=state,
                trajectory=trajectory,
                bank=online_bank,
            )
            online_bank = update.bank
            receipt = {
                "schema_version": 1,
                "phase_id": self.contract.phase_id,
                "staging_plan_sha256": self.contract.staging_plan_sha256,
                "stream_item": item.to_dict(),
                "first_encounter": True,
                "same_instance_rerun_policy": "replay_only_no_formal_update",
                "task_binding_sha256": binding.task_binding_sha256,
                "input_online_checkpoint_sha256": input_checkpoint_sha,
                "input_online_bank_sha256": input_bank_sha,
                "arm_order": list(item.arm_order),
                "arm_receipt_sha256s": {
                    arm: arm_receipts[arm].sha256 for arm in ARMS
                },
                "trajectory_sha256": trajectory_sha,
                "distillation_operation_id": self._distillation_operation_id(item),
                "output_online_bank_sha256": update.bank.sha256,
                "output_online_checkpoint_sha256": update.checkpoint.sha256,
                "sealed": True,
                "no_next_phase": True,
            }
            encoded = _canonical_bytes(receipt)
            _write_once(receipt_path, encoded)
            receipt_sha = _sha256_bytes(encoded)
            self._append_instance_fact(item, receipt, receipt_sha)
            receipt_hashes.append(receipt_sha)
            completed.append(item.instance_id)
            newly_executed += 1

        summary = {
            "schema_version": 1,
            "phase_id": self.contract.phase_id,
            "staging_plan_sha256": self.contract.staging_plan_sha256,
            "first_encounter_only": True,
            "stream_instance_ids": [item.instance_id for item in self.contract.stream],
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
        campaign_receipt = {
            "schema_version": 1,
            "staging_plan_sha256": self.contract.staging_plan_sha256,
            "summary_sha256": summary_sha,
            "sealed": True,
            "no_next_phase": True,
        }
        _write_once(
            self.formal_root / "campaign_receipt.json",
            _canonical_bytes(campaign_receipt),
        )
        event_payload = {
            "summary_sha256": summary_sha,
            "instance_count": len(completed),
            "final_online_checkpoint_sha256": state.online_checkpoint_sha256,
            "final_online_bank_sha256": online_bank.sha256,
        }
        event = self.registry.append(
            "hb_gen1_formal_campaign_sealed",
            event_payload,
            event_id=f"hb-gen1-formal-campaign:{summary_sha}",
        )
        if event.get("payload") != event_payload:
            raise ValueError("formal campaign fact is rebound")
        return FormalCampaignResult(
            sealed=True,
            completed_instance_ids=tuple(completed),
            newly_executed_instances=newly_executed,
            replayed_instances=replayed,
            online_checkpoint_sha256=state.online_checkpoint_sha256,
            online_bank_sha256=online_bank.sha256,
            first_encounter_summary_sha256=summary_sha,
        )

    def _provider(self, suite: str) -> FormalSuiteProvider:
        provider = self._providers.get(suite)
        if provider is None:
            provider = self.provider_factory.create(suite)
            if provider.suite != suite:
                raise ValueError("formal suite provider identity differs")
            self._providers[suite] = provider
        return provider

    def _binding_for(self, item: StreamItem) -> FormalTaskBinding:
        binding = self._provider(item.suite).bind(item)
        binding.validate_for(item)
        return binding

    def _arm_experience_binding(
        self,
        *,
        arm: str,
        state: PrequentialState,
        online_bank: ExperienceBankSnapshot,
    ) -> tuple[str, ExperienceBankSnapshot | None]:
        if arm in {"A", "B0"}:
            return self.untrained_checkpoint_sha256, None
        if arm == "B*":
            return self.initial_checkpoint.sha256, self.initial_bank
        if arm == "B-online":
            return state.online_checkpoint_sha256, online_bank
        raise ValueError("unknown formal arm")

    def _cross_instance_memory_grant(
        self,
        *,
        item: StreamItem,
        arm: str,
        checkpoint_sha256: str,
        bank: ExperienceBankSnapshot | None,
        records: tuple[dict[str, str], ...],
    ) -> CrossInstanceMemoryGrant | None:
        """Return controller authority for a bounded prior-task memory view.

        Historical four-arm campaigns keep their legacy static source binding.
        New prequential contracts override this hook with stream-order authority.
        """

        return None

    def _run_or_replay_arm(
        self,
        *,
        item: StreamItem,
        arm: str,
        binding: FormalTaskBinding,
        checkpoint_sha256: str,
        bank: ExperienceBankSnapshot | None,
    ) -> _ArmReceipt:
        path = self._arm_receipt_path(item, arm)
        bank_sha = bank.sha256 if bank is not None else None
        if safe_regular_file_exists(path, label="formal arm receipt"):
            receipt = self._load_arm_receipt(
                path=path,
                item=item,
                arm=arm,
                task_binding_sha256=binding.task_binding_sha256,
                checkpoint_sha256=checkpoint_sha256,
                bank_sha256=bank_sha,
            )
            if self._requires_trusted_cell_replay(arm):
                records, memory_grant = self._arm_runtime_inputs(
                    item=item,
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha256,
                    bank=bank,
                )
                self._trusted_replay_wide_arm(
                    item=item,
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=checkpoint_sha256,
                    bank_sha256=bank_sha,
                    records=records,
                    memory_grant=memory_grant,
                    receipt=receipt,
                )
            return receipt
        records, memory_grant = self._arm_runtime_inputs(
            item=item,
            arm=arm,
            binding=binding,
            checkpoint_sha256=checkpoint_sha256,
            bank=bank,
        )
        cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
        cell_root = self._cell_root(cell_id)
        result = self._cell_runner(
            item=item,
            arm=arm,
            binding=binding,
            records=records,
            memory_grant=memory_grant,
        ).run()
        if not result.sealed or len(result.attempts) != 8:
            raise ValueError("formal arm did not seal v001-v008")
        round_events = self._round_events(cell_root=cell_root, cell_id=cell_id)
        curve = self._curve(result, checkpoint_sha256, bank_sha, records)
        round_hashes = {
            version: _sha256_bytes(
                read_safe_regular_file(
                    cell_root / "rounds" / f"{version}.json",
                    label="formal sealed round",
                )
            )
            for version in (f"v{index:03d}" for index in range(1, 9))
        }
        payload = {
            "schema_version": 1,
            "staging_plan_sha256": self.contract.staging_plan_sha256,
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "arm": arm,
            "cell_id": cell_id,
            "task_binding_sha256": binding.task_binding_sha256,
            "builder_checkpoint_sha256": checkpoint_sha256,
            "experience_bank_sha256": bank_sha,
            "cross_instance_record_ids": [record["record_id"] for record in records],
            "round_event_ids": [event["event_id"] for event in round_events],
            "round_sha256s": round_hashes,
            "curve": curve,
            "sealed": True,
        }
        encoded = _canonical_bytes(payload)
        _write_once(path, encoded)
        receipt = _ArmReceipt(sha256=_sha256_bytes(encoded), payload=payload)
        event_payload = {
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "arm": arm,
            "cell_id": cell_id,
            "arm_receipt_sha256": receipt.sha256,
        }
        event = self.registry.append(
            "hb_gen1_formal_arm_sealed",
            event_payload,
            event_id="hb-gen1-formal-arm:"
            + hashlib.sha256(f"{item.stream_index}:{arm}".encode()).hexdigest(),
        )
        if event.get("payload") != event_payload:
            raise ValueError("formal arm fact is rebound")
        return receipt

    def _requires_trusted_cell_replay(self, arm: str) -> bool:
        return (
            self.variants[arm].adaptation_policy
            in {"targeted_any_change_v1", "wide_all_fields_recompile_v1"}
        )

    def _arm_runtime_inputs(
        self,
        *,
        item: StreamItem,
        arm: str,
        binding: FormalTaskBinding,
        checkpoint_sha256: str,
        bank: ExperienceBankSnapshot | None,
    ) -> tuple[tuple[dict[str, str], ...], CrossInstanceMemoryGrant | None]:
        records: tuple[dict[str, str], ...] = ()
        if bank is not None:
            records = bank.retrieve(
                instance_id=item.instance_id,
                instance_descriptors=binding.instance_descriptors,
            )
        memory_grant = self._cross_instance_memory_grant(
            item=item,
            arm=arm,
            checkpoint_sha256=checkpoint_sha256,
            bank=bank,
            records=records,
        )
        return records, memory_grant

    def _cell_runner(
        self,
        *,
        item: StreamItem,
        arm: str,
        binding: FormalTaskBinding,
        records: tuple[dict[str, str], ...],
        memory_grant: CrossInstanceMemoryGrant | None,
    ) -> HarnessBuilderCellRunner:
        cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
        cell_root = self._cell_root(cell_id)
        return HarnessBuilderCellRunner(
            artifact_root=cell_root,
            cell_id=cell_id,
            instance_id=item.instance_id,
            suite=item.suite,
            task_card=binding.task_card,
            reference_artifact=binding.reference_artifact,
            variant=self.variants[arm],
            operator_registry=self.operator_registry,
            model_gateway=self.model_gateway,
            model=self.contract.model,
            solution_codec=binding.solution_codec,
            evaluator=binding.evaluator,
            cross_instance_records=records,
            cross_instance_memory_grant=memory_grant,
            stream_index=(
                item.stream_index
                if self._requires_trusted_cell_replay(arm)
                else None
            ),
            rounds=8,
            operation_prefix="formal-op:"
            + hashlib.sha256(cell_id.encode()).hexdigest(),
        )

    def _trusted_replay_wide_arm(
        self,
        *,
        item: StreamItem,
        arm: str,
        binding: FormalTaskBinding,
        checkpoint_sha256: str,
        bank_sha256: str | None,
        records: tuple[dict[str, str], ...],
        memory_grant: CrossInstanceMemoryGrant | None,
        receipt: _ArmReceipt,
    ) -> None:
        """Recompile every sealed wide Harness version without new side effects."""

        result = self._cell_runner(
            item=item,
            arm=arm,
            binding=binding,
            records=records,
            memory_grant=memory_grant,
        ).run()
        if not result.sealed or len(result.attempts) != 8:
            raise ValueError("trusted wide Harness replay did not restore eight rounds")
        expected_curve = self._curve(
            result, checkpoint_sha256, bank_sha256, records
        )
        if receipt.payload.get("curve") != expected_curve:
            raise ValueError("trusted wide Harness replay curve differs from its receipt")

    @staticmethod
    def _curve(
        result: CellRunResult,
        checkpoint_sha256: str,
        bank_sha256: str | None,
        records: tuple[dict[str, str], ...],
    ) -> dict[str, Any]:
        running_best: float | None = None
        rounds = []
        for index, (decision, attempt) in enumerate(
            zip(result.decisions, result.attempts, strict=True), start=1
        ):
            if attempt.correct:
                running_best = max(running_best or 0.0, float(attempt.score))
            rounds.append(
                {
                    "version": f"v{index:03d}",
                    "correct": attempt.correct,
                    "score": attempt.score,
                    "running_best": running_best,
                    "outcome": attempt.outcome,
                    "public_feedback": attempt.public_summary,
                    "structural_signature": attempt.structural_signature,
                    "rule_id": None if decision is None else decision.rule_id,
                    "operational_fingerprint": (
                        None if decision is None else decision.operational_fingerprint
                    ),
                }
            )
        initial = rounds[0]["score"] if rounds[0]["correct"] else None
        gain = None
        if initial is not None and running_best is not None:
            gain = running_best / initial - 1.0
        return {
            "builder_checkpoint_sha256": checkpoint_sha256,
            "experience_bank_sha256": bank_sha256,
            "cross_instance_record_ids": [record["record_id"] for record in records],
            "initial_score": initial,
            "final_best": running_best,
            "evolution_gain": gain,
            "rounds": rounds,
        }

    def _round_events(self, *, cell_root: Path, cell_id: str) -> tuple[dict[str, Any], ...]:
        selected = [
            event
            for event in ExperimentRegistry(cell_root).read_events()
            if event.get("event_type") == "hb_gen1_round_sealed"
            and event.get("payload", {}).get("cell_id") == cell_id
        ]
        by_version = {event["payload"]["version"]: event for event in selected}
        versions = tuple(f"v{index:03d}" for index in range(1, 9))
        if len(selected) != 8 or set(by_version) != set(versions):
            raise ValueError("formal arm round facts are incomplete")
        return tuple(by_version[version] for version in versions)

    def _load_arm_receipt(
        self,
        *,
        path: Path,
        item: StreamItem,
        arm: str,
        task_binding_sha256: str,
        checkpoint_sha256: str,
        bank_sha256: str | None,
    ) -> _ArmReceipt:
        encoded = read_safe_regular_file(path, label="formal arm receipt")
        payload = self._canonical_object(encoded, "formal arm receipt")
        expected = {
            "schema_version",
            "staging_plan_sha256",
            "stream_index",
            "instance_id",
            "arm",
            "cell_id",
            "task_binding_sha256",
            "builder_checkpoint_sha256",
            "experience_bank_sha256",
            "cross_instance_record_ids",
            "round_event_ids",
            "round_sha256s",
            "curve",
            "sealed",
        }
        cell_id = f"formal:{item.suite}:{item.task_id}:{arm}"
        if set(payload) != expected or (
            payload["schema_version"] != 1
            or payload["staging_plan_sha256"] != self.contract.staging_plan_sha256
            or payload["stream_index"] != item.stream_index
            or payload["instance_id"] != item.instance_id
            or payload["arm"] != arm
            or payload["cell_id"] != cell_id
            or payload["task_binding_sha256"] != task_binding_sha256
            or payload["builder_checkpoint_sha256"] != checkpoint_sha256
            or payload["experience_bank_sha256"] != bank_sha256
            or payload["sealed"] is not True
        ):
            raise ValueError("formal arm receipt binding differs")
        cell_root = self._cell_root(cell_id)
        events = self._round_events(cell_root=cell_root, cell_id=cell_id)
        if payload["round_event_ids"] != [event["event_id"] for event in events]:
            raise ValueError("formal arm receipt event chain differs")
        versions = tuple(f"v{index:03d}" for index in range(1, 9))
        if set(payload["round_sha256s"]) != set(versions):
            raise ValueError("formal arm receipt round hashes differ")
        for version in versions:
            round_path = cell_root / "rounds" / f"{version}.json"
            if (
                not safe_regular_file_exists(
                    round_path, label="formal sealed round"
                )
                or _sha256_bytes(
                    read_safe_regular_file(round_path, label="formal sealed round")
                )
                != payload["round_sha256s"][version]
            ):
                raise ValueError("formal sealed round artifact differs")
        return _ArmReceipt(sha256=_sha256_bytes(encoded), payload=payload)

    def _distill(
        self,
        *,
        item: StreamItem,
        state: PrequentialState,
        trajectory: SealedInstanceTrajectory,
        bank: ExperienceBankSnapshot,
    ):
        cell_id = self._distillation_cell_id(item)
        updater = ContinualUpdater(
            bank_archive=self.bank_archive,
            checkpoint_archive=self.checkpoint_archive,
            distiller=GatewayGenerator(
                gateway=self.model_gateway,
                operation_id=self._distillation_operation_id(item),
                cell_id=cell_id,
                operation_kind="distillation_call",
                output_mode="plain_text",
            ),
            model=self.contract.model,
            rule_registry_sha256=self.operator_registry.rule_registry_sha256,
        )
        update = updater.update(state=state, trajectory=trajectory, bank=bank)
        if (
            update.bank.parent_sha256 != bank.sha256
            or update.checkpoint.parent_checkpoint_sha256
            != trajectory.builder_checkpoint_sha256
            or update.checkpoint.experience_bank_sha256 != update.bank.sha256
            or update.checkpoint.learned_through_instance != item.instance_id
        ):
            raise ValueError("formal online checkpoint/bank parent chain differs")
        event_payload = {
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "input_checkpoint_sha256": trajectory.builder_checkpoint_sha256,
            "input_bank_sha256": bank.sha256,
            "output_checkpoint_sha256": update.checkpoint.sha256,
            "output_bank_sha256": update.bank.sha256,
            "distillation_operation_id": self._distillation_operation_id(item),
        }
        event = self.registry.append(
            "hb_gen1_formal_online_updated",
            event_payload,
            event_id="hb-gen1-formal-online:"
            + hashlib.sha256(item.instance_id.encode()).hexdigest(),
        )
        if event.get("payload") != event_payload:
            raise ValueError("formal online update fact is rebound")
        return update

    def _store_trajectory(
        self, item: StreamItem, trajectory: SealedInstanceTrajectory
    ) -> str:
        payload = {"schema_version": 1, **trajectory.public_payload()}
        encoded = _canonical_bytes(payload)
        sha = _sha256_bytes(encoded)
        _write_once(
            self.formal_root / "trajectories" / "objects" / f"{sha}.json", encoded
        )
        binding = {
            "schema_version": 1,
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "trajectory_sha256": sha,
        }
        _write_once(
            self.formal_root
            / "trajectories"
            / "bindings"
            / f"{item.stream_index:03d}.json",
            _canonical_bytes(binding),
        )
        return sha

    def _replay_instance_receipt(
        self,
        *,
        item: StreamItem,
        state: PrequentialState,
        online_bank: ExperienceBankSnapshot,
        path: Path,
        binding: FormalTaskBinding | None = None,
    ) -> tuple[dict[str, Any], str, ExperienceBankSnapshot]:
        encoded = read_safe_regular_file(path, label="formal instance receipt")
        payload = self._canonical_object(encoded, "formal instance receipt")
        expected = {
            "schema_version",
            "phase_id",
            "staging_plan_sha256",
            "stream_item",
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
            payload["schema_version"] != 1
            or payload["phase_id"] != self.contract.phase_id
            or payload["staging_plan_sha256"] != self.contract.staging_plan_sha256
            or payload["stream_item"] != item.to_dict()
            or payload["first_encounter"] is not True
            or payload["same_instance_rerun_policy"]
            != "replay_only_no_formal_update"
            or payload["input_online_checkpoint_sha256"]
            != state.online_checkpoint_sha256
            or payload["input_online_bank_sha256"] != online_bank.sha256
            or payload["arm_order"] != list(item.arm_order)
            or set(payload["arm_receipt_sha256s"]) != set(ARMS)
            or payload["distillation_operation_id"]
            != self._distillation_operation_id(item)
            or payload["sealed"] is not True
            or payload["no_next_phase"] is not True
        ):
            raise ValueError("formal instance receipt binding differs")
        if binding is not None and (
            binding.task_binding_sha256 != payload["task_binding_sha256"]
        ):
            raise ValueError("formal replay task binding differs")
        for arm in ARMS:
            arm_encoded = read_safe_regular_file(
                self._arm_receipt_path(item, arm), label="formal arm receipt"
            )
            if _sha256_bytes(arm_encoded) != payload["arm_receipt_sha256s"][arm]:
                raise ValueError("formal instance arm receipt hash differs")
            if arm in {"A", "B0"}:
                expected_checkpoint = self.untrained_checkpoint_sha256
                expected_bank = None
            elif arm == "B*":
                expected_checkpoint = self.initial_checkpoint.sha256
                expected_bank = self.initial_bank.sha256
            else:
                expected_checkpoint = state.online_checkpoint_sha256
                expected_bank = online_bank.sha256
            self._load_arm_receipt(
                path=self._arm_receipt_path(item, arm),
                item=item,
                arm=arm,
                task_binding_sha256=payload["task_binding_sha256"],
                checkpoint_sha256=expected_checkpoint,
                bank_sha256=expected_bank,
            )
            if self._requires_trusted_cell_replay(arm):
                if binding is None:
                    raise ValueError(
                        "wide Harness instance replay requires a trusted task binding"
                    )
                bank = (
                    None
                    if arm in {"A", "B0"}
                    else self.initial_bank if arm == "B*" else online_bank
                )
                records, memory_grant = self._arm_runtime_inputs(
                    item=item,
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=expected_checkpoint,
                    bank=bank,
                )
                receipt = self._load_arm_receipt(
                    path=self._arm_receipt_path(item, arm),
                    item=item,
                    arm=arm,
                    task_binding_sha256=payload["task_binding_sha256"],
                    checkpoint_sha256=expected_checkpoint,
                    bank_sha256=expected_bank,
                )
                self._trusted_replay_wide_arm(
                    item=item,
                    arm=arm,
                    binding=binding,
                    checkpoint_sha256=expected_checkpoint,
                    bank_sha256=expected_bank,
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
            not safe_regular_file_exists(
                trajectory_path, label="formal trajectory object"
            )
            or _sha256_bytes(
                read_safe_regular_file(
                    trajectory_path, label="formal trajectory object"
                )
            )
            != payload["trajectory_sha256"]
        ):
            raise ValueError("formal sealed trajectory hash differs")
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
            raise ValueError("replayed formal parent chain differs")
        operation = self.model_gateway.governor.journal.replay().operations.get(
            payload["distillation_operation_id"]
        )
        if (
            operation is None
            or operation.state != "completed"
            or operation.cell_id != self._distillation_cell_id(item)
            or operation.operation_kind != "distillation_call"
        ):
            raise ValueError("formal distillation operation is not completed and bound")
        for arm in item.arm_order:
            state.seal_arm(arm)
        state.seal_instance()
        state.apply_distillation(updated_checkpoint.sha256)
        return payload, _sha256_bytes(encoded), updated_bank

    def _load_bank(self, sha: str) -> ExperienceBankSnapshot:
        _sha256(sha, "formal Experience Bank sha256")
        path = self.formal_root / "experience_banks" / f"{sha}.json"
        encoded = read_safe_regular_file(path, label="formal Experience Bank")
        payload = self._canonical_object(encoded, "formal Experience Bank")
        if set(payload) != {"schema_version", "bank_id", "parent_sha256", "records"}:
            raise ValueError("formal Experience Bank fields differ")
        bank = ExperienceBankSnapshot.create(
            bank_id=payload["bank_id"],
            parent_sha256=payload["parent_sha256"],
            records=tuple(ExperienceRecord.from_dict(value) for value in payload["records"]),
        )
        if bank.sha256 != sha or bank.canonical_bytes != encoded:
            raise ValueError("formal Experience Bank content hash differs")
        return bank

    def _load_checkpoint(self, sha: str) -> BuilderCheckpoint:
        _sha256(sha, "formal Builder checkpoint sha256")
        path = self.formal_root / "builder_checkpoints" / f"{sha}.json"
        encoded = read_safe_regular_file(path, label="formal checkpoint")
        payload = self._canonical_object(encoded, "formal Builder checkpoint")
        if set(payload) != {
            "schema_version",
            "parent_checkpoint_sha256",
            "experience_bank_sha256",
            "rule_registry_sha256",
            "learned_through_instance",
            "stream_index",
        } or payload.pop("schema_version") != 1:
            raise ValueError("formal Builder checkpoint fields differ")
        checkpoint = BuilderCheckpoint(**payload)
        if checkpoint.sha256 != sha or checkpoint.canonical_bytes != encoded:
            raise ValueError("formal Builder checkpoint content hash differs")
        return checkpoint

    @staticmethod
    def _canonical_object(encoded: bytes, label: str) -> dict[str, Any]:
        try:
            payload = json.loads(encoded)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"{label} is invalid JSON") from exc
        if not isinstance(payload, dict) or _canonical_bytes(payload) != encoded:
            raise ValueError(f"{label} is not canonical")
        if _PRIVATE_TEXT.search(json.dumps(payload, ensure_ascii=False)):
            raise ValueError(f"{label} contains private evaluator text")
        return payload

    def _append_instance_fact(
        self, item: StreamItem, receipt: dict[str, Any], receipt_sha: str
    ) -> None:
        event_payload = {
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "instance_receipt_sha256": receipt_sha,
            "trajectory_sha256": receipt["trajectory_sha256"],
            "output_online_checkpoint_sha256": receipt[
                "output_online_checkpoint_sha256"
            ],
            "output_online_bank_sha256": receipt["output_online_bank_sha256"],
        }
        event = self.registry.append(
            "hb_gen1_formal_instance_sealed",
            event_payload,
            event_id="hb-gen1-formal-instance:"
            + hashlib.sha256(item.instance_id.encode()).hexdigest(),
        )
        if event.get("payload") != event_payload:
            raise ValueError("formal instance fact is rebound")

    def _instance_root(self, item: StreamItem) -> Path:
        digest = hashlib.sha256(item.instance_id.encode()).hexdigest()
        return self.formal_root / "instances" / f"{item.stream_index:03d}-{digest}"

    def _instance_receipt_path(self, item: StreamItem) -> Path:
        return self._instance_root(item) / "instance_receipt.json"

    def _arm_receipt_path(self, item: StreamItem, arm: str) -> Path:
        return self._instance_root(item) / "arms" / f"{arm}.json"

    def _cell_root(self, cell_id: str) -> Path:
        return self.formal_root / "cells" / hashlib.sha256(cell_id.encode()).hexdigest()

    @staticmethod
    def _distillation_cell_id(item: StreamItem) -> str:
        return f"distill:{item.stream_index:03d}:{item.instance_id}"

    def _distillation_operation_id(self, item: StreamItem) -> str:
        return f"{self._distillation_cell_id(item)}:distillation_call"
