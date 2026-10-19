from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec

from .learning import (
    BuilderCheckpoint,
    BuilderCheckpointArchive,
    ExperienceBankArchive,
    ExperienceBankSnapshot,
    parse_distillation_records,
)
from .adapters.kernelbench_meta import KernelBenchMetaAdapter, KernelBenchMetaTask
from .evaluation import KernelBenchMetaEvaluationBackend
from .model_gateway import GatewayGenerator, IsolatedModelGateway
from .operators import TrustedOperatorRegistry
from .runner import EvaluationBackend, HarnessBuilderCellRunner, SolutionCodec
from .schema import BuilderVariant
from .solutions import KernelBenchSolutionCodec


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SOURCE_PATH = re.compile(r"KernelBench/level([12])/(\d+)_([^/]+)\.py")
_PRIVATE_TEXT = re.compile(
    r"(?:/home/|/data\d*/|private[_ -]evaluator|private[_ -]log)", re.IGNORECASE
)
_HISTORICAL_TASK_IDS = (
    "level1/40_LayerNorm.py",
    "level2/56_Matmul_Sigmoid_Sum.py",
)
_NEW_TASK_IDS = (
    "level1/21_Sigmoid.py",
    "level1/92_cumsum_exclusive.py",
    "level1/97_ScaledDotProductAttention.py",
    "level2/45_Gemm_Sigmoid_LogSumExp.py",
    "level2/57_Conv2d_ReLU_HardSwish.py",
    "level2/67_Conv2d_GELU_GlobalAvgPool.py",
)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
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
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError(f"refusing to overwrite different meta-train artifact: {path.name}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".meta-train.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


@dataclass(frozen=True)
class MetaTrainSource:
    task_id: str
    source_path: str
    source_sha256: str
    level: int
    problem_id: int
    display_name: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "MetaTrainSource":
        if set(payload) != {"task_id", "source_path", "source_sha256"}:
            raise ValueError("meta-train source binding fields differ")
        task_id = payload["task_id"]
        source_path = payload["source_path"]
        source_sha = payload["source_sha256"]
        if not isinstance(task_id, str) or not isinstance(source_path, str):
            raise ValueError("meta-train source identity must be text")
        if source_path != f"KernelBench/{task_id}":
            raise ValueError("meta-train source path does not match its task id")
        if not isinstance(source_sha, str) or not _SHA256.fullmatch(source_sha):
            raise ValueError("meta-train source hash is invalid")
        match = _SOURCE_PATH.fullmatch(source_path)
        if match is None:
            raise ValueError("meta-train source is not a frozen KernelBench task")
        level = int(match.group(1))
        problem_id = int(match.group(2))
        display_name = match.group(3).replace("_", " ")
        return cls(
            task_id=task_id,
            source_path=source_path,
            source_sha256=source_sha,
            level=level,
            problem_id=problem_id,
            display_name=display_name,
        )

    @property
    def instance_id(self) -> str:
        return f"kernelbench:{self.task_id}"

    @property
    def cell_id(self) -> str:
        return f"meta:kernelbench:{self.task_id}"

    def task_spec(self, repository_commit: str) -> TaskSpec:
        return TaskSpec(
            task_id=self.instance_id,
            display_name=f"KernelBench meta-train {self.display_name}",
            level=self.level,
            problem_id=self.problem_id,
            task_path=self.source_path,
            task_sha256=self.source_sha256,
            repository_commit=repository_commit,
            target_gpu="A100",
            gpu_arch="Ampere",
            backend="triton",
            precision="fp32",
            correctness_trials=5,
            performance_trials=100,
            timeout_seconds=300,
        )


@dataclass(frozen=True)
class MetaTrainContract:
    bank_id: str
    repository_commit: str
    sources: tuple[MetaTrainSource, ...]
    historical_policy_id: str
    historical_source_manifest: str
    historical_source_manifest_sha256: str

    @classmethod
    def from_json(cls, path: Path) -> "MetaTrainContract":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        expected = {
            "schema_version",
            "bank_id",
            "status",
            "source_suite",
            "repository_commit",
            "source_instances",
            "source_bindings",
            "existing_sources",
            "record_schema",
            "promotion_levels",
        }
        if not isinstance(payload, dict) or set(payload) != expected:
            raise ValueError("meta-train Experience Bank manifest fields differ")
        if payload["schema_version"] != 1 or payload["source_suite"] != "kernelbench":
            raise ValueError("unsupported meta-train manifest")
        if payload["status"] != "pending-six-new-meta-train-trajectories":
            raise ValueError("meta-train manifest is not in its frozen pending state")
        repository_commit = payload["repository_commit"]
        if not isinstance(repository_commit, str) or not re.fullmatch(
            r"[0-9a-f]{40}", repository_commit
        ):
            raise ValueError("meta-train repository commit is not pinned")
        sources = tuple(
            MetaTrainSource.from_dict(item) for item in payload["source_bindings"]
        )
        expected_ids = _HISTORICAL_TASK_IDS + _NEW_TASK_IDS
        if tuple(payload["source_instances"]) != expected_ids:
            raise ValueError("meta-train source instance order changed")
        if tuple(source.task_id for source in sources) != expected_ids:
            raise ValueError("meta-train source bindings changed")
        existing = payload["existing_sources"]
        historical_policy_id = "hb-gen1-kernelbench-historical-all-lanes-v1"
        historical_source_manifest = (
            "optimization_lab/harness_builder/data/"
            "historical_trajectory_sources_v1.json"
        )
        if (
            not isinstance(existing, list)
            or len(existing) != 2
            or any(
                not isinstance(item, dict)
                or set(item)
                != {
                    "aggregation",
                    "evidence",
                    "policy_id",
                    "source_id",
                    "source_manifest",
                    "source_manifest_sha256",
                    "status",
                    "task_id",
                }
                or item.get("status") != "frozen"
                or item.get("aggregation")
                != "all_terminal_public_attempts_in_source_ledger_order"
                or item.get("policy_id") != historical_policy_id
                or item.get("source_manifest") != historical_source_manifest
                or item.get("task_id") != _HISTORICAL_TASK_IDS[index]
                or not isinstance(item.get("source_manifest_sha256"), str)
                or not _SHA256.fullmatch(item["source_manifest_sha256"])
                for index, item in enumerate(existing)
            )
        ):
            raise ValueError("historical meta-train sources are not frozen")
        historical_manifest_hashes = {
            item["source_manifest_sha256"] for item in existing
        }
        if len(historical_manifest_hashes) != 1:
            raise ValueError("historical meta-train source manifests differ")
        bank_id = payload["bank_id"]
        if bank_id != "moss-kernelbench-meta-train-v1":
            raise ValueError("meta-train bank id changed")
        return cls(
            bank_id=bank_id,
            repository_commit=repository_commit,
            sources=sources,
            historical_policy_id=historical_policy_id,
            historical_source_manifest=historical_source_manifest,
            historical_source_manifest_sha256=historical_manifest_hashes.pop(),
        )

    @property
    def historical_sources(self) -> tuple[MetaTrainSource, ...]:
        return self.sources[:2]

    @property
    def new_sources(self) -> tuple[MetaTrainSource, ...]:
        return self.sources[2:]

    @property
    def expected_instance_ids(self) -> tuple[str, ...]:
        return tuple(source.instance_id for source in self.sources)


@dataclass(frozen=True)
class MetaTrainTask:
    source: MetaTrainSource
    task_card: str
    reference_artifact: str
    solution_codec: SolutionCodec
    evaluator: EvaluationBackend

    def __post_init__(self) -> None:
        if not self.task_card.strip() or not self.reference_artifact.strip():
            raise ValueError("meta-train task card and reference are required")
        if _PRIVATE_TEXT.search(self.task_card) or _PRIVATE_TEXT.search(
            self.reference_artifact
        ):
            raise ValueError("meta-train public task context contains a private path")
        actual_sha = hashlib.sha256(self.reference_artifact.encode("utf-8")).hexdigest()
        if actual_sha != self.source.source_sha256:
            raise ValueError("meta-train reference does not match the frozen source hash")


def bind_kernelbench_meta_tasks(
    *,
    contract: MetaTrainContract,
    repository: Path,
    adapter: KernelBenchMetaAdapter,
) -> tuple[MetaTrainTask, ...]:
    """Bind the six public sources to the strict per-attempt backend.

    Reading task source is intentionally separate from evaluation.  The latter
    re-verifies the checkout and task digest before every attempt, so replacing
    a file after task construction cannot change the scored instance.
    """

    repository = Path(repository).resolve()
    tasks: list[MetaTrainTask] = []
    for source in contract.new_sources:
        evaluator_task = KernelBenchMetaTask.from_task_id(source.task_id)
        if (
            evaluator_task.source_path != source.source_path
            or evaluator_task.task_sha256 != source.source_sha256
            or evaluator_task.repository_commit != contract.repository_commit
        ):
            raise ValueError("meta-train evaluator binding differs from the contract")
        path = repository / source.source_path
        try:
            metadata = path.lstat()
        except OSError as exc:
            raise ValueError("frozen meta-train source is missing") from exc
        if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
            raise ValueError("frozen meta-train source must be a regular file")
        try:
            reference = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            raise ValueError("frozen meta-train source is unreadable") from exc
        if hashlib.sha256(reference.encode("utf-8")).hexdigest() != source.source_sha256:
            raise ValueError("frozen meta-train source sha256 differs")
        tasks.append(
            MetaTrainTask(
                source=source,
                task_card=(
                    "Optimize this frozen public KernelBench instance for A100 using the "
                    "declared Harness workflow. The formal evaluator remains private."
                ),
                reference_artifact=reference,
                solution_codec=KernelBenchSolutionCodec(task_id=source.task_id),
                evaluator=KernelBenchMetaEvaluationBackend(
                    adapter=adapter,
                    task=evaluator_task,
                ),
            )
        )
    return tuple(tasks)


@dataclass(frozen=True)
class MetaTrainTrajectory:
    source_instance_id: str
    source_sha256: str
    instance_descriptor: tuple[str, ...]
    initial_harness_structure: tuple[str, ...]
    provenance_event_ids: tuple[str, ...]
    round_summaries: tuple[dict[str, Any], ...]
    sealed: bool

    @classmethod
    def create(
        cls,
        *,
        source_instance_id: str,
        source_sha256: str,
        instance_descriptor: tuple[str, ...],
        initial_harness_structure: tuple[str, ...],
        provenance_event_ids: tuple[str, ...],
        round_summaries: tuple[dict[str, Any], ...],
        sealed: bool,
    ) -> "MetaTrainTrajectory":
        item = cls(
            source_instance_id=source_instance_id,
            source_sha256=source_sha256,
            instance_descriptor=instance_descriptor,
            initial_harness_structure=initial_harness_structure,
            provenance_event_ids=provenance_event_ids,
            round_summaries=round_summaries,
            sealed=sealed,
        )
        item._validate()
        return item

    @classmethod
    def from_json(cls, path: Path) -> "MetaTrainTrajectory":
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(payload, dict) or set(payload) != {
            "schema_version",
            "source_instance_id",
            "source_sha256",
            "instance_descriptor",
            "initial_harness_structure",
            "provenance_event_ids",
            "round_summaries",
            "sealed",
        }:
            raise ValueError("meta-train trajectory fields differ")
        if payload.pop("schema_version") != 1:
            raise ValueError("unsupported meta-train trajectory schema")
        return cls.create(
            source_instance_id=payload["source_instance_id"],
            source_sha256=payload["source_sha256"],
            instance_descriptor=tuple(payload["instance_descriptor"]),
            initial_harness_structure=tuple(payload["initial_harness_structure"]),
            provenance_event_ids=tuple(payload["provenance_event_ids"]),
            round_summaries=tuple(payload["round_summaries"]),
            sealed=payload["sealed"],
        )

    def _validate(self) -> None:
        if not self.source_instance_id.startswith("kernelbench:"):
            raise ValueError("meta-train trajectory is not from KernelBench")
        if not _SHA256.fullmatch(self.source_sha256):
            raise ValueError("invalid meta-train trajectory source hash")
        for values, label in (
            (self.instance_descriptor, "instance descriptor"),
            (self.initial_harness_structure, "initial Harness structure"),
            (self.provenance_event_ids, "provenance events"),
        ):
            if not values or not all(isinstance(value, str) and value for value in values):
                raise ValueError(f"meta-train {label} is empty or invalid")
        if not self.round_summaries or not all(
            isinstance(value, dict) and value for value in self.round_summaries
        ):
            raise ValueError("meta-train round summaries are empty or invalid")
        if len(set(self.provenance_event_ids)) != len(self.provenance_event_ids):
            raise ValueError("meta-train provenance events contain duplicates")
        if self.sealed is not True:
            raise ValueError("meta-train trajectory must be sealed")
        if _PRIVATE_TEXT.search(json.dumps(self.public_payload(), ensure_ascii=False)):
            raise ValueError("meta-train trajectory contains private evaluator data")

    def public_payload(self) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "source_instance_id": self.source_instance_id,
            "source_sha256": self.source_sha256,
            "instance_descriptor": list(self.instance_descriptor),
            "initial_harness_structure": list(self.initial_harness_structure),
            "provenance_event_ids": list(self.provenance_event_ids),
            "round_summaries": list(self.round_summaries),
            "sealed": True,
        }

    @property
    def canonical_bytes(self) -> bytes:
        return _canonical_bytes(self.public_payload())

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.canonical_bytes).hexdigest()


class MetaTrainTrajectoryArchive:
    def __init__(self, root: Path) -> None:
        self.root = Path(root).resolve()

    def store(self, trajectory: MetaTrainTrajectory) -> Path:
        object_path = self.root / "objects" / f"{trajectory.sha256}.json"
        _write_once(object_path, trajectory.canonical_bytes)
        source_digest = hashlib.sha256(
            trajectory.source_instance_id.encode("utf-8")
        ).hexdigest()
        binding = {
            "schema_version": 1,
            "source_instance_id": trajectory.source_instance_id,
            "source_sha256": trajectory.source_sha256,
            "trajectory_sha256": trajectory.sha256,
        }
        _write_once(
            self.root / "bindings" / f"{source_digest}.json",
            _canonical_bytes(binding),
        )
        return object_path


class MetaTrainCampaignRunner:
    """Run exactly six independent, frozen-H0 KernelBench training trajectories."""

    def __init__(
        self,
        *,
        artifact_root: Path,
        contract: MetaTrainContract,
        variant: BuilderVariant,
        operator_registry: TrustedOperatorRegistry,
        model_gateway: IsolatedModelGateway,
        model: str,
    ) -> None:
        if (
            variant.variant_id != "B0"
            or variant.freeze_after_initial
            or variant.continual_update
            or variant.experience_sources
        ):
            raise ValueError(
                "meta-train must use the frozen universal adaptive Builder without experience"
            )
        self.artifact_root = Path(artifact_root).resolve()
        self.contract = contract
        self.variant = variant
        self.operator_registry = operator_registry
        self.model_gateway = model_gateway
        self.model = model
        self.registry = ExperimentRegistry(self.artifact_root)
        self.trajectories = MetaTrainTrajectoryArchive(
            self.artifact_root / "meta_train/trajectories"
        )

    def run(self, tasks: tuple[MetaTrainTask, ...]) -> tuple[MetaTrainTrajectory, ...]:
        by_id = {task.source.task_id: task for task in tasks}
        expected = tuple(source.task_id for source in self.contract.new_sources)
        if len(by_id) != len(tasks) or set(by_id) != set(expected):
            raise ValueError("meta-train runner requires exactly the six frozen new tasks")
        results: list[MetaTrainTrajectory] = []
        for source in self.contract.new_sources:
            task = by_id[source.task_id]
            if task.source != source:
                raise ValueError("meta-train task binding differs from the frozen contract")
            cell_digest = hashlib.sha256(source.cell_id.encode("utf-8")).hexdigest()
            cell_root = self.artifact_root / "meta_train/cells" / cell_digest
            result = HarnessBuilderCellRunner(
                artifact_root=cell_root,
                cell_id=source.cell_id,
                instance_id=source.instance_id,
                suite="kernelbench",
                task_card=task.task_card,
                reference_artifact=task.reference_artifact,
                variant=self.variant,
                operator_registry=self.operator_registry,
                model_gateway=self.model_gateway,
                model=self.model,
                solution_codec=task.solution_codec,
                evaluator=task.evaluator,
                cross_instance_records=(),
                rounds=8,
            ).run()
            if not result.sealed or len(result.attempts) != 8:
                raise ValueError("meta-train cell did not seal all eight rounds")
            cell_events = [
                event
                for event in ExperimentRegistry(cell_root).read_events()
                if event.get("event_type") == "hb_gen1_round_sealed"
                and event.get("payload", {}).get("cell_id") == source.cell_id
            ]
            if len(cell_events) != 8:
                raise ValueError("meta-train rounds are not fully bound to public facts")
            by_version = {event["payload"]["version"]: event for event in cell_events}
            versions = tuple(f"v{index:03d}" for index in range(1, 9))
            if set(by_version) != set(versions):
                raise ValueError("meta-train round fact versions differ")
            provenance = tuple(by_version[version]["event_id"] for version in versions)
            summaries = tuple(
                {
                    "version": version,
                    "rule_id": None if decision is None else decision.rule_id,
                    "operational_fingerprint": (
                        None if decision is None else decision.operational_fingerprint
                    ),
                    "parent_strategy": (
                        None if decision is None else decision.parent_strategy
                    ),
                    "correct": attempt.correct,
                    "score": attempt.score,
                    "outcome": attempt.outcome,
                    "public_summary": attempt.public_summary,
                }
                for version, decision, attempt in zip(
                    versions, result.decisions, result.attempts, strict=True
                )
            )
            descriptor = (
                "kernelbench",
                f"level-{source.level}",
                *tuple(part.casefold() for part in source.display_name.split()),
            )
            initial = next(
                (decision for decision in result.decisions if decision is not None),
                None,
            )
            initial_structure = (
                ("planner:all_rejected",)
                if initial is None
                else (
                    *(f"role:{value}" for value in initial.role_graph),
                    *(f"memory:{value}" for value in initial.memory_views),
                    *(f"tool:{value}" for value in initial.tools),
                    *(f"workflow:{value}" for value in initial.workflow),
                    f"parent:{initial.parent_strategy}",
                    f"scheduler:{initial.scheduler_mode}",
                    f"recovery:{initial.recovery_mode}",
                )
            )
            trajectory = MetaTrainTrajectory.create(
                source_instance_id=source.instance_id,
                source_sha256=source.source_sha256,
                instance_descriptor=descriptor,
                initial_harness_structure=initial_structure,
                provenance_event_ids=provenance,
                round_summaries=summaries,
                sealed=True,
            )
            self.trajectories.store(trajectory)
            event_payload = {
                "source_instance_id": source.instance_id,
                "source_sha256": source.source_sha256,
                "trajectory_sha256": trajectory.sha256,
                "round_event_ids": list(provenance),
            }
            event_id = "hb-gen1-meta-trajectory:" + hashlib.sha256(
                source.instance_id.encode("utf-8")
            ).hexdigest()
            event = self.registry.append(
                "hb_gen1_meta_train_trajectory_sealed",
                event_payload,
                event_id=event_id,
            )
            if event.get("payload") != event_payload:
                raise ValueError("meta-train trajectory event is rebound")
            results.append(trajectory)
        return tuple(results)


@dataclass(frozen=True)
class FrozenMetaTrainResult:
    bank: ExperienceBankSnapshot
    checkpoint: BuilderCheckpoint
    builder_bindings: dict[str, str]
    trajectory_sha256s: dict[str, str]
    freeze_manifest_sha256: str


class MetaTrainFreezer:
    """Distill only after all eight source trajectories are immutable and public."""

    def __init__(
        self,
        *,
        artifact_root: Path,
        contract: MetaTrainContract,
        model_gateway: IsolatedModelGateway,
        model: str,
        rule_registry_sha256: str,
        untrained_checkpoint_sha256: str,
        trained_variant: BuilderVariant,
        online_variant: BuilderVariant,
        formal_heldout_ids: tuple[str, ...],
    ) -> None:
        if not _SHA256.fullmatch(rule_registry_sha256) or not _SHA256.fullmatch(
            untrained_checkpoint_sha256
        ):
            raise ValueError("meta-train checkpoint and Rule Registry hashes are required")
        if (
            trained_variant.variant_id != "B*"
            or trained_variant.continual_update
            or online_variant.variant_id != "B-online"
            or not online_variant.continual_update
            or trained_variant.freeze_after_initial
            or online_variant.freeze_after_initial
        ):
            raise ValueError("meta-train freeze requires the B* and B-online variants")
        if len(formal_heldout_ids) != 24 or len(set(formal_heldout_ids)) != 24:
            raise ValueError("meta-train freeze requires the exact 24 formal held-out ids")
        if (
            trained_variant.rule_registry_sha256 != rule_registry_sha256
            or online_variant.rule_registry_sha256 != rule_registry_sha256
            or trained_variant.allowed_rule_ids != online_variant.allowed_rule_ids
            or trained_variant.experience_sources != (contract.bank_id,)
            or online_variant.experience_sources != (contract.bank_id,)
            or set(trained_variant.excluded_task_ids) != set(formal_heldout_ids)
            or set(online_variant.excluded_task_ids) != set(formal_heldout_ids)
        ):
            raise ValueError("B* and B-online do not share one frozen prequential start")
        self.artifact_root = Path(artifact_root).resolve()
        self.contract = contract
        self.model_gateway = model_gateway
        self.model = model
        self.rule_registry_sha256 = rule_registry_sha256
        self.untrained_checkpoint_sha256 = untrained_checkpoint_sha256
        self.trained_variant = trained_variant
        self.online_variant = online_variant
        self.formal_heldout_ids = formal_heldout_ids
        self.bank_archive = ExperienceBankArchive(
            self.artifact_root / "meta_train/experience_banks"
        )
        self.checkpoint_archive = BuilderCheckpointArchive(
            self.artifact_root / "meta_train/builder_checkpoints"
        )
        self.registry = ExperimentRegistry(self.artifact_root)

    def freeze(
        self, trajectories: tuple[MetaTrainTrajectory, ...]
    ) -> FrozenMetaTrainResult:
        if len(trajectories) != 8:
            raise ValueError("meta-train freeze requires exactly eight sealed trajectories")
        by_source = {item.source_instance_id: item for item in trajectories}
        if len(by_source) != 8 or set(by_source) != set(
            self.contract.expected_instance_ids
        ):
            raise ValueError("meta-train trajectories do not match all eight sources")
        ordered = tuple(by_source[source_id] for source_id in self.contract.expected_instance_ids)
        for source, trajectory in zip(self.contract.sources, ordered, strict=True):
            if (
                trajectory.sealed is not True
                or trajectory.source_sha256 != source.source_sha256
            ):
                raise ValueError("meta-train trajectory source binding differs")
            if source in self.contract.new_sources and (
                len(trajectory.round_summaries) != 8
                or len(trajectory.provenance_event_ids) != 8
            ):
                raise ValueError("new meta-train trajectory must contain eight sealed rounds")

        records = []
        excluded = set(self.trained_variant.excluded_task_ids)
        for index, trajectory in enumerate(ordered):
            distiller = GatewayGenerator(
                gateway=self.model_gateway,
                operation_id=f"meta:distillation:{index:03d}",
                cell_id="meta:distillation",
                operation_kind="distillation_call",
                output_mode="plain_text",
            )
            prompt = (
                "Distill the fully sealed KernelBench meta-train trajectory into one or more "
                "strict Experience Records. Use only the supplied public summaries and event "
                "IDs. Do not copy candidate code, private evaluator evidence, or infer held-out "
                "test behavior. Every record scope must be single_instance_observation. Return "
                "one bare JSON object containing only a records array.\n\n"
                + json.dumps(
                    trajectory.public_payload(),
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
            )
            generation = distiller.generate(prompt, model=self.model)
            proposed = parse_distillation_records(generation.raw_response)
            for record in proposed:
                serialized_record = json.dumps(
                    record.to_dict(), ensure_ascii=False, sort_keys=True
                )
                if record.source_instance_id != trajectory.source_instance_id:
                    raise ValueError("distilled record cites the wrong meta-train source")
                if any(task_id in serialized_record for task_id in excluded):
                    raise ValueError("distilled record cites a Builder-excluded task")
                if record.scope != "single_instance_observation":
                    raise ValueError("one meta-train trajectory cannot self-promote")
                if not set(record.provenance_event_ids).issubset(
                    trajectory.provenance_event_ids
                ):
                    raise ValueError("distilled record cites unbound public evidence")
                records.append(record)

        bank = ExperienceBankSnapshot.create(
            bank_id=self.contract.bank_id,
            parent_sha256=None,
            records=tuple(records),
        )
        self.bank_archive.store(bank)
        checkpoint = BuilderCheckpoint(
            parent_checkpoint_sha256=self.untrained_checkpoint_sha256,
            experience_bank_sha256=bank.sha256,
            rule_registry_sha256=self.rule_registry_sha256,
            learned_through_instance="kernelbench:meta-train-complete",
            stream_index=8,
        )
        self.checkpoint_archive.store(checkpoint)
        bindings = {"B*": checkpoint.sha256, "B-online": checkpoint.sha256}
        trajectory_hashes = {
            item.source_instance_id: item.sha256 for item in ordered
        }
        manifest = {
            "schema_version": 1,
            "bank_id": self.contract.bank_id,
            "repository_commit": self.contract.repository_commit,
            "trajectory_sha256s": trajectory_hashes,
            "experience_bank_sha256": bank.sha256,
            "builder_checkpoint_sha256": checkpoint.sha256,
            "builder_bindings": bindings,
            "B_star_B_online_byte_identical": True,
            "formal_excluded_task_ids": list(self.trained_variant.excluded_task_ids),
            "sealed": True,
        }
        encoded = _canonical_bytes(manifest)
        freeze_sha = hashlib.sha256(encoded).hexdigest()
        _write_once(self.artifact_root / "meta_train/meta_train_frozen.json", encoded)
        event_payload = {
            "freeze_manifest_sha256": freeze_sha,
            "experience_bank_sha256": bank.sha256,
            "builder_checkpoint_sha256": checkpoint.sha256,
            "trajectory_sha256s": trajectory_hashes,
        }
        event = self.registry.append(
            "hb_gen1_meta_train_frozen",
            event_payload,
            event_id=f"hb-gen1-meta-train-frozen:{freeze_sha}",
        )
        if event.get("payload") != event_payload:
            raise ValueError("meta-train freeze event is rebound")
        return FrozenMetaTrainResult(
            bank=bank,
            checkpoint=checkpoint,
            builder_bindings=bindings,
            trajectory_sha256s=trajectory_hashes,
            freeze_manifest_sha256=freeze_sha,
        )
