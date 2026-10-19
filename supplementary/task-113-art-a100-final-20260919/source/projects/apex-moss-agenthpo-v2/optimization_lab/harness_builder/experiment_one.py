from __future__ import annotations

import hashlib
import json
import math
import os
import re
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Any, Callable, Mapping, Sequence

from .dual_harness import HarnessWorkspace, TaskHarnessArtifact


_SHA256 = re.compile(r"[0-9a-f]{64}")
_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_POSITIONS = ("A", "B", "C")
_SEEDS = ("S1", "S2", "S3")


def _canonical_json(value: Any) -> str:
    return json.dumps(
        _json_compatible(value),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _json_compatible(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_compatible(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_compatible(item) for item in value]
    return value


def _json_copy(value: Any, label: str) -> Any:
    try:
        return json.loads(_canonical_json(value))
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be JSON serializable") from exc


def _sha256_json(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _require_sha256(value: Any, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{label} must be a sha256")
    return value


def _require_safe_id(value: Any, label: str) -> str:
    if (
        not isinstance(value, str)
        or _SAFE_ID.fullmatch(value) is None
        or ".." in value
    ):
        raise ValueError(f"{label} is unsafe")
    return value


def _require_nonempty(value: Any, label: str, *, maximum: int = 32_000) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ValueError(f"{label} must be non-empty bounded text")
    return value


def _public_failure_reason(exc: Exception) -> str:
    """Expose bounded, non-secret details only for explicitly public failures."""

    error_type = type(exc).__name__
    if error_type not in {"SolutionContractError", "OpenAIResponsesError"}:
        return error_type
    message = " ".join(str(exc).split())
    if not message:
        return error_type
    return f"{error_type}: {message[:1000]}"


def _numeric_score(value: Any, label: str, *, allow_none: bool = False) -> float | None:
    if value is None and allow_none:
        return None
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not math.isfinite(float(value))
    ):
        raise ValueError(f"{label} must be a finite numeric official score")
    return float(value)


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, suffix=".experiment-one.tmp"
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary_name).replace(path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def _write_once(path: Path, payload: Mapping[str, Any]) -> str:
    copied = _json_copy(payload, "immutable receipt")
    payload_sha256 = _sha256_json(copied)
    envelope = {
        "schema_version": 1,
        "payload": copied,
        "payload_sha256": payload_sha256,
    }
    encoded = (_canonical_json(envelope) + "\n").encode("utf-8")
    if path.exists():
        if path.read_bytes() != encoded:
            raise ValueError(f"refusing to overwrite different receipt: {path.name}")
        return payload_sha256
    _atomic_write(path, encoded)
    return payload_sha256


def _load_once(path: Path, *, label: str) -> tuple[dict[str, Any], str]:
    try:
        envelope = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} failed integrity verification") from exc
    if not isinstance(envelope, dict) or set(envelope) != {
        "schema_version",
        "payload",
        "payload_sha256",
    }:
        raise ValueError(f"{label} failed integrity verification")
    if envelope["schema_version"] != 1 or not isinstance(envelope["payload"], dict):
        raise ValueError(f"{label} failed integrity verification")
    expected = _require_sha256(envelope["payload_sha256"], f"{label} payload hash")
    if _sha256_json(envelope["payload"]) != expected:
        raise ValueError(f"{label} failed integrity verification")
    return envelope["payload"], expected


def _exact_mapping(payload: Mapping[str, Any], fields: set[str], label: str) -> None:
    if not isinstance(payload, Mapping) or set(payload) != fields:
        raise ValueError(f"{label} fields differ from the contract")


@dataclass(frozen=True)
class ModelConfiguration:
    provider: str
    api_family: str
    transport: str
    model: str
    reasoning_effort: str
    max_output_tokens: int
    sampling_parameters: Mapping[str, Any] = field(default_factory=dict)
    tool_permission_policy: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for label in ("provider", "api_family", "transport", "model", "reasoning_effort"):
            _require_nonempty(getattr(self, label), f"model configuration {label}", maximum=256)
        if (
            not isinstance(self.max_output_tokens, int)
            or isinstance(self.max_output_tokens, bool)
            or self.max_output_tokens < 1
        ):
            raise ValueError("model configuration max output tokens is invalid")
        sampling = _json_copy(self.sampling_parameters, "sampling parameters")
        policy = _json_copy(self.tool_permission_policy, "tool permission policy")
        if not isinstance(sampling, dict) or not isinstance(policy, dict):
            raise ValueError("model configuration policies must be objects")
        object.__setattr__(self, "sampling_parameters", MappingProxyType(sampling))
        object.__setattr__(self, "tool_permission_policy", MappingProxyType(policy))

    def to_dict(self) -> dict[str, Any]:
        return {
            "provider": self.provider,
            "api_family": self.api_family,
            "transport": self.transport,
            "model": self.model,
            "reasoning_effort": self.reasoning_effort,
            "max_output_tokens": self.max_output_tokens,
            "sampling_parameters": _json_copy(self.sampling_parameters, "sampling parameters"),
            "tool_permission_policy": _json_copy(
                self.tool_permission_policy, "tool permission policy"
            ),
        }

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "ModelConfiguration":
        fields = {
            "provider",
            "api_family",
            "transport",
            "model",
            "reasoning_effort",
            "max_output_tokens",
            "sampling_parameters",
            "tool_permission_policy",
        }
        _exact_mapping(payload, fields, "model configuration")
        return cls(**dict(payload))

    @property
    def sha256(self) -> str:
        return _sha256_json(self.to_dict())


@dataclass(frozen=True)
class TargetBinding:
    position: str
    task_id: str
    task: str
    submission_path: str
    evaluator_contract_sha256: str
    score_direction: str = "maximize"

    def __post_init__(self) -> None:
        if self.position not in _POSITIONS:
            raise ValueError("target position must be A, B, or C")
        _require_safe_id(self.task_id, "target task id")
        _require_nonempty(self.task, "target task", maximum=2_000_000)
        _require_nonempty(self.submission_path, "target submission path", maximum=4_000)
        path = self.submission_path.replace("\\", "/")
        if path.startswith("/") or ".." in path.split("/"):
            raise ValueError("target submission path is unsafe")
        _require_sha256(self.evaluator_contract_sha256, "evaluator contract hash")
        if self.score_direction not in {"maximize", "minimize"}:
            raise ValueError("target score direction is invalid")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def sha256(self) -> str:
        return _sha256_json(self.to_dict())


@dataclass(frozen=True)
class ExperimentOneManifest:
    schema_version: int
    experiment_id: str
    benchmark: str
    seed_id: str
    rounds: int
    h0: TaskHarnessArtifact
    targets: tuple[TargetBinding, ...]
    builder_model_configuration: ModelConfiguration
    solver_model_configuration: ModelConfiguration
    moss_revision_sha256: str
    tracked_tree_sha256: str
    source_revision_sha256: str
    task_data_revision_sha256: str
    image_digest_sha256: str
    api_base_host_sha256: str

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported experiment-one manifest schema")
        _require_safe_id(self.experiment_id, "experiment id")
        _require_safe_id(self.benchmark, "benchmark id")
        if self.seed_id not in _SEEDS:
            raise ValueError("experiment seed must be S1, S2, or S3")
        if self.rounds != 8:
            raise ValueError("experiment one requires exactly eight rounds")
        if tuple(target.position for target in self.targets) != _POSITIONS:
            raise ValueError("experiment one requires exactly A, B, and C targets")
        if len({target.task_id for target in self.targets}) != 3:
            raise ValueError("experiment one target ids must be distinct")
        if self.h0.version != 1 or self.h0.parent_sha256 is not None:
            raise ValueError("H0 must be a parentless version-one Harness")
        for config in (
            self.builder_model_configuration,
            self.solver_model_configuration,
        ):
            if config.model != "gpt-5.6-sol":
                raise ValueError("experiment one requires gpt-5.6-sol")
            if config.reasoning_effort != "high":
                raise ValueError("experiment one requires high reasoning effort")
            if config.api_family != "responses":
                raise ValueError("experiment one requires the Responses API")
        if (
            self.builder_model_configuration.sha256
            != self.solver_model_configuration.sha256
        ):
            raise ValueError("upper and lower model configurations must be identical")
        for label in (
            "moss_revision_sha256",
            "tracked_tree_sha256",
            "source_revision_sha256",
            "task_data_revision_sha256",
            "image_digest_sha256",
            "api_base_host_sha256",
        ):
            _require_sha256(getattr(self, label), label.replace("_", " "))

    def target(self, position: str) -> TargetBinding:
        if position not in _POSITIONS:
            raise ValueError("target position must be A, B, or C")
        return self.targets[_POSITIONS.index(position)]

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "experiment_id": self.experiment_id,
            "benchmark": self.benchmark,
            "seed_id": self.seed_id,
            "rounds": self.rounds,
            "h0": self.h0.to_dict(),
            "targets": [target.to_dict() for target in self.targets],
            "builder_model_configuration": self.builder_model_configuration.to_dict(),
            "solver_model_configuration": self.solver_model_configuration.to_dict(),
            "moss_revision_sha256": self.moss_revision_sha256,
            "tracked_tree_sha256": self.tracked_tree_sha256,
            "source_revision_sha256": self.source_revision_sha256,
            "task_data_revision_sha256": self.task_data_revision_sha256,
            "image_digest_sha256": self.image_digest_sha256,
            "api_base_host_sha256": self.api_base_host_sha256,
        }

    @property
    def sha256(self) -> str:
        return _sha256_json(self.to_dict())


@dataclass(frozen=True)
class LineageRoundRequest:
    manifest_sha256: str
    benchmark: str
    seed_id: str
    position: str
    round_index: int
    operation_id: str
    lineage_root: Path
    workspace: HarnessWorkspace
    target: TargetBinding
    builder_model_configuration: ModelConfiguration
    solver_model_configuration: ModelConfiguration


@dataclass(frozen=True)
class LineageRoundResult:
    evaluated_harness_sha256: str
    next_harness_sha256: str
    candidate_sha256: str
    official_score: float | None
    official_score_valid: bool
    public_feedback: str
    evaluator_receipt_sha256: str
    private_evidence_sha256: str
    audit_ledger_sha256: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.evaluated_harness_sha256, "evaluated Harness hash"),
            (self.next_harness_sha256, "next Harness hash"),
            (self.candidate_sha256, "candidate hash"),
            (self.evaluator_receipt_sha256, "evaluator receipt hash"),
            (self.private_evidence_sha256, "private evidence hash"),
            (self.audit_ledger_sha256, "audit ledger hash"),
        ):
            _require_sha256(value, label)
        if type(self.official_score_valid) is not bool:
            raise ValueError("official score validity must be boolean")
        _numeric_score(self.official_score, "official score", allow_none=True)
        if self.official_score_valid:
            _numeric_score(self.official_score, "valid official score")
        if not isinstance(self.public_feedback, str) or len(self.public_feedback) > 32_000:
            raise ValueError("public feedback is invalid")


@dataclass(frozen=True)
class LineageRoundReceipt:
    schema_version: int
    manifest_sha256: str
    benchmark: str
    seed_id: str
    position: str
    task_id: str
    target_binding_sha256: str
    round_index: int
    operation_id: str
    status: str
    consumed_budget: bool
    harness_sha256: str
    next_harness_sha256: str
    parent_harness_sha256: str | None
    candidate_sha256: str | None
    official_score: float | None
    official_score_valid: bool
    public_feedback: str
    evaluator_receipt_sha256: str | None
    private_evidence_sha256: str | None
    audit_ledger_sha256: str | None
    builder_model_configuration_sha256: str
    solver_model_configuration_sha256: str
    evaluator_contract_sha256: str
    moss_revision_sha256: str
    tracked_tree_sha256: str
    source_revision_sha256: str
    task_data_revision_sha256: str
    image_digest_sha256: str
    api_base_host_sha256: str
    task_sha256: str
    operation_journal_head_sha256: str

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported lineage receipt schema")
        if self.position not in _POSITIONS or self.seed_id not in _SEEDS:
            raise ValueError("lineage receipt identity is invalid")
        if not 1 <= self.round_index <= 8:
            raise ValueError("lineage receipt round is invalid")
        _require_safe_id(self.operation_id, "lineage operation id")
        if self.status not in {"completed", "abandoned"}:
            raise ValueError("lineage receipt status is invalid")
        if self.consumed_budget is not True:
            raise ValueError("every terminal lineage receipt must consume budget")
        if type(self.official_score_valid) is not bool:
            raise ValueError("official score validity must be boolean")
        _numeric_score(self.official_score, "official score", allow_none=True)
        if self.official_score_valid:
            _numeric_score(self.official_score, "valid official score")
        _require_sha256(self.harness_sha256, "lineage Harness hash")
        _require_sha256(self.next_harness_sha256, "lineage next Harness hash")
        if self.parent_harness_sha256 is not None:
            _require_sha256(self.parent_harness_sha256, "lineage parent Harness hash")
        for value, label in (
            (self.manifest_sha256, "manifest hash"),
            (self.target_binding_sha256, "target binding hash"),
            (self.builder_model_configuration_sha256, "Builder model configuration hash"),
            (self.solver_model_configuration_sha256, "Solver model configuration hash"),
            (self.evaluator_contract_sha256, "evaluator contract hash"),
            (self.moss_revision_sha256, "Moss revision hash"),
            (self.tracked_tree_sha256, "tracked tree hash"),
            (self.source_revision_sha256, "official source hash"),
            (self.task_data_revision_sha256, "task data hash"),
            (self.image_digest_sha256, "image digest hash"),
            (self.api_base_host_sha256, "API base host hash"),
            (self.task_sha256, "task hash"),
            (self.operation_journal_head_sha256, "operation journal head hash"),
        ):
            _require_sha256(value, label)
        for value, label in (
            (self.candidate_sha256, "candidate hash"),
            (self.evaluator_receipt_sha256, "evaluator receipt hash"),
            (self.private_evidence_sha256, "private evidence hash"),
            (self.audit_ledger_sha256, "audit ledger hash"),
        ):
            if value is not None:
                _require_sha256(value, label)
        if self.status == "completed" and None in (
            self.candidate_sha256,
            self.evaluator_receipt_sha256,
            self.private_evidence_sha256,
            self.audit_ledger_sha256,
        ):
            raise ValueError("completed lineage receipt is missing evidence")
        if self.status == "abandoned" and self.official_score_valid:
            raise ValueError("abandoned lineage receipt cannot authorize a score")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "LineageRoundReceipt":
        fields = set(cls.__dataclass_fields__)
        _exact_mapping(payload, fields, "lineage round receipt")
        return cls(**dict(payload))


def select_best_round(
    receipts: Sequence[LineageRoundReceipt],
    *,
    score_direction: str = "maximize",
) -> LineageRoundReceipt:
    if score_direction not in {"maximize", "minimize"}:
        raise ValueError("score direction is invalid")
    eligible = [
        receipt
        for receipt in receipts
        if receipt.status == "completed"
        and receipt.official_score_valid
        and receipt.official_score is not None
        and math.isfinite(float(receipt.official_score))
    ]
    if not eligible:
        raise ValueError("cannot freeze without a valid numeric official score")
    direction = -1.0 if score_direction == "maximize" else 1.0
    return min(
        eligible,
        key=lambda item: (
            direction * float(item.official_score),
            item.round_index,
            item.harness_sha256,
        ),
    )


@dataclass(frozen=True)
class FreezeReceipt:
    schema_version: int
    manifest_sha256: str
    benchmark: str
    seed_id: str
    position: str
    task_id: str
    target_binding_sha256: str
    selected_round: int
    harness_sha256: str
    ancestry_sha256s: tuple[str, ...]
    candidate_sha256: str
    official_score: float
    evaluator_receipt_sha256: str
    private_evidence_sha256: str
    audit_ledger_sha256: str
    operation_journal_head_sha256: str
    builder_model_configuration_sha256: str
    solver_model_configuration_sha256: str
    evaluator_contract_sha256: str
    moss_revision_sha256: str
    tracked_tree_sha256: str
    source_revision_sha256: str
    task_data_revision_sha256: str
    image_digest_sha256: str
    api_base_host_sha256: str
    valid: bool

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.valid is not True:
            raise ValueError("valid FreezeReceipt contract is required")
        if self.position not in _POSITIONS or self.seed_id not in _SEEDS:
            raise ValueError("FreezeReceipt identity is invalid")
        if not 1 <= self.selected_round <= 8:
            raise ValueError("FreezeReceipt selected round is invalid")
        _numeric_score(self.official_score, "FreezeReceipt official score")
        if not self.ancestry_sha256s or self.ancestry_sha256s[-1] != self.harness_sha256:
            raise ValueError("FreezeReceipt ancestry is incomplete")
        for value in self.ancestry_sha256s:
            _require_sha256(value, "FreezeReceipt ancestry hash")
        for field_name in (
            "manifest_sha256",
            "target_binding_sha256",
            "harness_sha256",
            "candidate_sha256",
            "evaluator_receipt_sha256",
            "private_evidence_sha256",
            "audit_ledger_sha256",
            "operation_journal_head_sha256",
            "builder_model_configuration_sha256",
            "solver_model_configuration_sha256",
            "evaluator_contract_sha256",
            "moss_revision_sha256",
            "tracked_tree_sha256",
            "source_revision_sha256",
            "task_data_revision_sha256",
            "image_digest_sha256",
            "api_base_host_sha256",
        ):
            _require_sha256(getattr(self, field_name), field_name.replace("_", " "))

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["ancestry_sha256s"] = list(self.ancestry_sha256s)
        return payload

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "FreezeReceipt":
        fields = set(cls.__dataclass_fields__)
        _exact_mapping(payload, fields, "FreezeReceipt")
        copied = dict(payload)
        ancestry = copied.get("ancestry_sha256s")
        if not isinstance(ancestry, list):
            raise ValueError("FreezeReceipt ancestry is invalid")
        copied["ancestry_sha256s"] = tuple(ancestry)
        return cls(**copied)

    @property
    def sha256(self) -> str:
        return _sha256_json(self.to_dict())


class LineageRunner:
    """Run one isolated eight-round A/B/C Harness lineage with durable recovery."""

    def __init__(
        self,
        *,
        manifest: ExperimentOneManifest,
        position: str,
        root: Path,
        round_executor_factory: Callable[
            [str, Path], Callable[[LineageRoundRequest], LineageRoundResult]
        ],
    ) -> None:
        if position not in _POSITIONS:
            raise ValueError("lineage position must be A, B, or C")
        if not callable(round_executor_factory):
            raise TypeError("round executor factory must be callable")
        self.manifest = manifest
        self.position = position
        self.target = manifest.target(position)
        self.root = Path(root).resolve()
        self.round_executor_factory = round_executor_factory
        self.operations_root = self.root / "operations"
        manifest_path = self.root / "manifest.json"
        lineage_path = self.root / "lineage_binding.json"

        if self.root.exists() and any(self.root.iterdir()) and not manifest_path.is_file():
            raise ValueError("lineage root is not an owned experiment-one root")
        self.root.mkdir(parents=True, exist_ok=True)
        if manifest_path.is_file():
            saved_manifest, _ = _load_once(manifest_path, label="lineage manifest")
            if saved_manifest != manifest.to_dict():
                raise ValueError("lineage root belongs to a different manifest")
        else:
            _write_once(manifest_path, manifest.to_dict())
        binding = {
            "schema_version": 1,
            "manifest_sha256": manifest.sha256,
            "position": position,
            "target_binding_sha256": self.target.sha256,
            "h0_sha256": manifest.h0.sha256,
        }
        _write_once(lineage_path, binding)

        self.workspace = HarnessWorkspace(self.root / "workspace")
        if self.workspace.current_path.is_file():
            current = self.workspace.current()
            self._verify_descends_from_h0(current)
        else:
            if any(self.workspace.artifacts_root.iterdir()):
                raise ValueError("lineage workspace has artifacts but no current Harness")
            self.workspace.commit(manifest.h0)
        self.round_executor = round_executor_factory(self.position, self.root)
        if not callable(self.round_executor):
            raise TypeError("round executor factory must return a callable")

    @classmethod
    def initialize_all(
        cls,
        *,
        manifest: ExperimentOneManifest,
        experiment_root: Path,
        round_executor_factory: Callable[
            [str, Path], Callable[[LineageRoundRequest], LineageRoundResult]
        ],
    ) -> dict[str, "LineageRunner"]:
        base = (
            Path(experiment_root).resolve()
            / manifest.benchmark
            / manifest.seed_id
            / "lineages"
        )
        runners = {
            position: cls(
                manifest=manifest,
                position=position,
                root=base / position,
                round_executor_factory=round_executor_factory,
            )
            for position in _POSITIONS
        }
        roots = {runner.workspace.root for runner in runners.values()}
        if len(roots) != 3:
            raise ValueError("A/B/C lineages must use separate workspaces")
        h0_bytes = {
            runner.workspace.artifact_path(manifest.h0.sha256).read_bytes()
            for runner in runners.values()
        }
        if len(h0_bytes) != 1:
            raise ValueError("A/B/C H0 artifacts are not byte-identical")
        return runners

    def run(self) -> tuple[LineageRoundReceipt, ...]:
        receipts: list[LineageRoundReceipt] = []
        for round_index in range(1, self.manifest.rounds + 1):
            saved = self._load_terminal_round(round_index)
            if saved is not None:
                receipts.append(saved)
                continue
            operation_id = self._operation_id(round_index)
            start_path, result_path, abandoned_path = self._operation_paths(round_index)
            if start_path.is_file():
                start, head = _load_once(start_path, label="lineage operation start")
                receipt = self._abandon_started_round(
                    round_index=round_index,
                    operation_id=operation_id,
                    start=start,
                    operation_head_sha256=head,
                    path=abandoned_path,
                )
                receipts.append(receipt)
                continue

            current = self.workspace.current()
            start = self._start_payload(
                round_index=round_index,
                operation_id=operation_id,
                harness_sha256=current.sha256,
            )
            operation_head_sha256 = _write_once(start_path, start)
            request = LineageRoundRequest(
                manifest_sha256=self.manifest.sha256,
                benchmark=self.manifest.benchmark,
                seed_id=self.manifest.seed_id,
                position=self.position,
                round_index=round_index,
                operation_id=operation_id,
                lineage_root=self.root,
                workspace=self.workspace,
                target=self.target,
                builder_model_configuration=self.manifest.builder_model_configuration,
                solver_model_configuration=self.manifest.solver_model_configuration,
            )
            try:
                result = self.round_executor(request)
                receipt = self._completed_receipt(
                    round_index=round_index,
                    operation_id=operation_id,
                    starting_harness=current,
                    result=result,
                    operation_head_sha256=operation_head_sha256,
                )
                _write_once(result_path, receipt.to_dict())
            except Exception as exc:
                receipt = self._abandon_started_round(
                    round_index=round_index,
                    operation_id=operation_id,
                    start=start,
                    operation_head_sha256=operation_head_sha256,
                    path=abandoned_path,
                    reason=_public_failure_reason(exc),
                )
            receipts.append(receipt)
        return tuple(receipts)

    def freeze(self) -> FreezeReceipt:
        receipts = self._all_terminal_receipts()
        if len(receipts) != self.manifest.rounds:
            raise ValueError("all eight lineage rounds must be terminal before freeze")
        selected = select_best_round(
            receipts, score_direction=self.target.score_direction
        )
        artifact = self.workspace.load_artifact(selected.harness_sha256)
        ancestry = self._ancestry(artifact)
        assert selected.candidate_sha256 is not None
        assert selected.evaluator_receipt_sha256 is not None
        assert selected.private_evidence_sha256 is not None
        assert selected.audit_ledger_sha256 is not None
        assert selected.official_score is not None
        receipt = FreezeReceipt(
            schema_version=1,
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            position=self.position,
            task_id=self.target.task_id,
            target_binding_sha256=self.target.sha256,
            selected_round=selected.round_index,
            harness_sha256=selected.harness_sha256,
            ancestry_sha256s=ancestry,
            candidate_sha256=selected.candidate_sha256,
            official_score=float(selected.official_score),
            evaluator_receipt_sha256=selected.evaluator_receipt_sha256,
            private_evidence_sha256=selected.private_evidence_sha256,
            audit_ledger_sha256=selected.audit_ledger_sha256,
            operation_journal_head_sha256=selected.operation_journal_head_sha256,
            builder_model_configuration_sha256=(
                self.manifest.builder_model_configuration.sha256
            ),
            solver_model_configuration_sha256=(
                self.manifest.solver_model_configuration.sha256
            ),
            evaluator_contract_sha256=self.target.evaluator_contract_sha256,
            moss_revision_sha256=self.manifest.moss_revision_sha256,
            tracked_tree_sha256=self.manifest.tracked_tree_sha256,
            source_revision_sha256=self.manifest.source_revision_sha256,
            task_data_revision_sha256=self.manifest.task_data_revision_sha256,
            image_digest_sha256=self.manifest.image_digest_sha256,
            api_base_host_sha256=self.manifest.api_base_host_sha256,
            valid=True,
        )
        path = self.root / "freeze_receipt.json"
        _write_once(path, receipt.to_dict())
        saved, _ = _load_once(path, label="FreezeReceipt")
        loaded = FreezeReceipt.from_dict(saved)
        if loaded != receipt:
            raise ValueError("FreezeReceipt does not match the current lineage")
        return loaded

    def _completed_receipt(
        self,
        *,
        round_index: int,
        operation_id: str,
        starting_harness: TaskHarnessArtifact,
        result: LineageRoundResult,
        operation_head_sha256: str,
    ) -> LineageRoundReceipt:
        if not isinstance(result, LineageRoundResult):
            raise TypeError("round executor must return LineageRoundResult")
        if result.evaluated_harness_sha256 != starting_harness.sha256:
            raise ValueError("round result evaluated a different Harness")
        current = self.workspace.current()
        if result.next_harness_sha256 != current.sha256:
            raise ValueError("round result next Harness does not match the workspace")
        self.workspace.load_artifact(result.next_harness_sha256)
        return LineageRoundReceipt(
            schema_version=1,
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            position=self.position,
            task_id=self.target.task_id,
            target_binding_sha256=self.target.sha256,
            round_index=round_index,
            operation_id=operation_id,
            status="completed",
            consumed_budget=True,
            harness_sha256=result.evaluated_harness_sha256,
            next_harness_sha256=result.next_harness_sha256,
            parent_harness_sha256=starting_harness.parent_sha256,
            candidate_sha256=result.candidate_sha256,
            official_score=result.official_score,
            official_score_valid=result.official_score_valid,
            public_feedback=result.public_feedback,
            evaluator_receipt_sha256=result.evaluator_receipt_sha256,
            private_evidence_sha256=result.private_evidence_sha256,
            audit_ledger_sha256=result.audit_ledger_sha256,
            **self._common_evidence(operation_head_sha256),
        )

    def _abandon_started_round(
        self,
        *,
        round_index: int,
        operation_id: str,
        start: Mapping[str, Any],
        operation_head_sha256: str,
        path: Path,
        reason: str = "started_without_durable_result",
    ) -> LineageRoundReceipt:
        expected = self._start_payload(
            round_index=round_index,
            operation_id=operation_id,
            harness_sha256=start.get("harness_sha256"),
        )
        if dict(start) != expected:
            raise ValueError("lineage operation start belongs to a different request")
        harness = self._rollback_to_started_harness(start)
        receipt = LineageRoundReceipt(
            schema_version=1,
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            position=self.position,
            task_id=self.target.task_id,
            target_binding_sha256=self.target.sha256,
            round_index=round_index,
            operation_id=operation_id,
            status="abandoned",
            consumed_budget=True,
            harness_sha256=harness.sha256,
            next_harness_sha256=harness.sha256,
            parent_harness_sha256=harness.parent_sha256,
            candidate_sha256=None,
            official_score=None,
            official_score_valid=False,
            public_feedback=f"terminal abandonment: {reason}",
            evaluator_receipt_sha256=None,
            private_evidence_sha256=None,
            audit_ledger_sha256=None,
            **self._common_evidence(operation_head_sha256),
        )
        _write_once(path, receipt.to_dict())
        return receipt

    def _common_evidence(self, operation_head_sha256: str) -> dict[str, Any]:
        return {
            "builder_model_configuration_sha256": (
                self.manifest.builder_model_configuration.sha256
            ),
            "solver_model_configuration_sha256": (
                self.manifest.solver_model_configuration.sha256
            ),
            "evaluator_contract_sha256": self.target.evaluator_contract_sha256,
            "moss_revision_sha256": self.manifest.moss_revision_sha256,
            "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
            "source_revision_sha256": self.manifest.source_revision_sha256,
            "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
            "image_digest_sha256": self.manifest.image_digest_sha256,
            "api_base_host_sha256": self.manifest.api_base_host_sha256,
            "task_sha256": hashlib.sha256(self.target.task.encode("utf-8")).hexdigest(),
            "operation_journal_head_sha256": operation_head_sha256,
        }

    def _start_payload(
        self, *, round_index: int, operation_id: str, harness_sha256: Any
    ) -> dict[str, Any]:
        _require_sha256(harness_sha256, "started Harness hash")
        harness = self.workspace.load_artifact(harness_sha256)
        artifact_payload = harness.to_dict()
        request = {
            "manifest_sha256": self.manifest.sha256,
            "position": self.position,
            "round_index": round_index,
            "operation_id": operation_id,
            "harness_sha256": harness_sha256,
            "harness_artifact": artifact_payload,
            "harness_artifact_sha256": _sha256_json(artifact_payload),
            "current_binding_sha256": _sha256_json({"sha256": harness_sha256}),
            "target_binding_sha256": self.target.sha256,
        }
        return {
            "schema_version": 1,
            **request,
            "request_sha256": _sha256_json(request),
        }

    def _rollback_to_started_harness(
        self, start: Mapping[str, Any]
    ) -> TaskHarnessArtifact:
        artifact_payload = start.get("harness_artifact")
        if not isinstance(artifact_payload, Mapping):
            raise ValueError("lineage operation start lacks recovery evidence")
        artifact = TaskHarnessArtifact.from_dict(artifact_payload)
        if (
            artifact.sha256 != start.get("harness_sha256")
            or _sha256_json(artifact.to_dict())
            != start.get("harness_artifact_sha256")
            or _sha256_json({"sha256": artifact.sha256})
            != start.get("current_binding_sha256")
        ):
            raise ValueError("lineage operation recovery evidence is invalid")
        stored = self.workspace.load_artifact(artifact.sha256)
        if stored != artifact:
            raise ValueError("lineage pre-round Harness evidence does not match storage")
        current = self.workspace.current()
        if current.sha256 == artifact.sha256:
            return artifact
        cursor = current
        seen: set[str] = set()
        while cursor.sha256 != artifact.sha256:
            if cursor.sha256 in seen or cursor.parent_sha256 is None:
                raise RuntimeError("cannot rollback an unrelated Harness lineage")
            seen.add(cursor.sha256)
            cursor = self.workspace.load_artifact(cursor.parent_sha256)
        _atomic_write(
            self.workspace.current_path,
            (_canonical_json({"sha256": artifact.sha256}) + "\n").encode("utf-8"),
        )
        if self.workspace.current().sha256 != artifact.sha256:
            raise RuntimeError("lineage rollback did not restore the pre-round Harness")
        return artifact

    def _operation_id(self, round_index: int) -> str:
        return f"{self.manifest.seed_id}-{self.position}-round-{round_index:02d}"

    def _operation_paths(self, round_index: int) -> tuple[Path, Path, Path]:
        stem = f"round-{round_index:02d}"
        return (
            self.operations_root / f"{stem}.started.json",
            self.operations_root / f"{stem}.result.json",
            self.operations_root / f"{stem}.abandoned.json",
        )

    def _load_terminal_round(self, round_index: int) -> LineageRoundReceipt | None:
        start_path, result_path, abandoned_path = self._operation_paths(round_index)
        terminal = [path for path in (result_path, abandoned_path) if path.is_file()]
        if len(terminal) > 1:
            raise ValueError("lineage operation has multiple terminal receipts")
        if not terminal:
            return None
        if not start_path.is_file():
            raise ValueError("lineage terminal receipt has no operation start")
        payload, _ = _load_once(terminal[0], label="lineage terminal receipt")
        receipt = LineageRoundReceipt.from_dict(payload)
        if (
            receipt.manifest_sha256 != self.manifest.sha256
            or receipt.position != self.position
            or receipt.round_index != round_index
            or receipt.operation_id != self._operation_id(round_index)
        ):
            raise ValueError("lineage terminal receipt belongs to another request")
        return receipt

    def _all_terminal_receipts(self) -> tuple[LineageRoundReceipt, ...]:
        return tuple(
            receipt
            for index in range(1, self.manifest.rounds + 1)
            if (receipt := self._load_terminal_round(index)) is not None
        )

    def _ancestry(self, artifact: TaskHarnessArtifact) -> tuple[str, ...]:
        ancestry: list[str] = []
        seen: set[str] = set()
        current = artifact
        while True:
            if current.sha256 in seen:
                raise ValueError("Harness ancestry contains a cycle")
            seen.add(current.sha256)
            ancestry.append(current.sha256)
            if current.parent_sha256 is None:
                break
            current = self.workspace.load_artifact(current.parent_sha256)
        ancestry.reverse()
        if ancestry[0] != self.manifest.h0.sha256:
            raise ValueError("Harness ancestry does not start at H0")
        return tuple(ancestry)

    def _verify_descends_from_h0(self, artifact: TaskHarnessArtifact) -> None:
        self._ancestry(artifact)


@dataclass(frozen=True)
class TaskExecutionRequest:
    manifest_sha256: str
    operation_id: str
    source_position: str
    target: TargetBinding
    harness: TaskHarnessArtifact
    task: str
    model_configuration: ModelConfiguration
    cell_root: Path
    history: tuple[Any, ...] = ()
    memory: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        _require_sha256(self.manifest_sha256, "task execution manifest hash")
        _require_safe_id(self.operation_id, "task execution operation id")
        if self.source_position not in _POSITIONS:
            raise ValueError("task execution source position is invalid")
        root = Path(self.cell_root).resolve()
        if root != self.cell_root:
            object.__setattr__(self, "cell_root", root)
        if self.task != self.target.task:
            raise ValueError("task execution target binding is inconsistent")
        if self.history != () or dict(self.memory) != {}:
            raise ValueError("frozen Task Harness execution must start without history or Memory")
        object.__setattr__(self, "memory", MappingProxyType({}))


@dataclass(frozen=True)
class CallLedgerEvidence:
    operation_id: str
    builder_constructed_count: int
    builder_call_count: int
    solver_call_count: int
    memory_read_count: int
    audit_ledger_sha256: str

    def __post_init__(self) -> None:
        _require_safe_id(self.operation_id, "call ledger operation id")
        for field_name in (
            "builder_constructed_count",
            "builder_call_count",
            "solver_call_count",
            "memory_read_count",
        ):
            value = getattr(self, field_name)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValueError("call ledger counts must be non-negative integers")
        _require_sha256(self.audit_ledger_sha256, "call ledger hash")

    def require_frozen_solver_only(self) -> None:
        if (
            self.builder_constructed_count,
            self.builder_call_count,
            self.solver_call_count,
            self.memory_read_count,
        ) != (0, 0, 1, 0):
            raise ValueError(
                "frozen execution ledger must prove no Builder/Memory and one Solver call"
            )


@dataclass(frozen=True)
class TaskExecutionResult:
    candidate: Any = field(repr=False, compare=False)
    candidate_sha256: str
    candidate_archive_sha256: str
    call_ledger: CallLedgerEvidence

    def __post_init__(self) -> None:
        for value, label in (
            (self.candidate_sha256, "candidate hash"),
            (self.candidate_archive_sha256, "candidate archive hash"),
        ):
            _require_sha256(value, label)
        if not isinstance(self.call_ledger, CallLedgerEvidence):
            raise TypeError("task execution result requires call ledger evidence")

    @property
    def audit_ledger_sha256(self) -> str:
        return self.call_ledger.audit_ledger_sha256


@dataclass(frozen=True)
class HarnessTransferProvenance:
    source_position: str
    harness_sha256: str
    neutral_artifact_sha256: str
    cleared_private_state_sha256: str
    source_private_material_sha256s: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.source_position not in _POSITIONS:
            raise ValueError("transfer provenance source position is invalid")
        for value, label in (
            (self.harness_sha256, "transfer Harness hash"),
            (self.neutral_artifact_sha256, "neutral artifact hash"),
            (self.cleared_private_state_sha256, "cleared private state hash"),
        ):
            _require_sha256(value, label)
        for value in self.source_private_material_sha256s:
            _require_sha256(value, "source private material hash")
        if self.source_private_material_sha256s:
            raise ValueError("transfer provenance must clear all source-private material")

    @classmethod
    def cleared(
        cls, *, source_position: str, harness: TaskHarnessArtifact
    ) -> "HarnessTransferProvenance":
        return cls(
            source_position=source_position,
            harness_sha256=harness.sha256,
            neutral_artifact_sha256=_sha256_json(
                {"schema_version": 1, "spec": harness.spec.to_dict()}
            ),
            cleared_private_state_sha256=_sha256_json(
                {
                    "candidate": None,
                    "score": None,
                    "feedback": None,
                    "history": [],
                    "memory": {},
                    "trace": None,
                }
            ),
            source_private_material_sha256s=(),
        )

    @property
    def sha256(self) -> str:
        return _sha256_json(asdict(self))


@dataclass(frozen=True)
class EvaluationRequest:
    manifest_sha256: str
    operation_id: str
    target: TargetBinding
    candidate: TaskExecutionResult
    cell_root: Path
    frozen_harness_sha256: str
    private_eval_allowed: bool
    freeze_receipt_path: Path | None = None
    freeze_receipt_sha256: str | None = None
    freeze_lineage_position: str | None = None
    freeze_candidate_sha256: str | None = None
    freeze_public_score: float | None = None

    def __post_init__(self) -> None:
        _require_sha256(self.manifest_sha256, "evaluation manifest hash")
        _require_safe_id(self.operation_id, "evaluation operation id")
        object.__setattr__(self, "cell_root", Path(self.cell_root).resolve())
        _require_sha256(self.frozen_harness_sha256, "frozen Harness hash")
        if type(self.private_eval_allowed) is not bool:
            raise ValueError("private evaluation permission must be boolean")
        if self.private_eval_allowed:
            if self.freeze_receipt_path is None or not Path(
                self.freeze_receipt_path
            ).resolve().is_file():
                raise ValueError("private evaluation requires a real FreezeReceipt path")
            object.__setattr__(
                self, "freeze_receipt_path", Path(self.freeze_receipt_path).resolve()
            )
            _require_sha256(self.freeze_receipt_sha256, "FreezeReceipt hash")
            _require_sha256(self.freeze_candidate_sha256, "freeze candidate hash")
            if self.freeze_lineage_position not in _POSITIONS:
                raise ValueError("freeze lineage position is invalid")
            _numeric_score(self.freeze_public_score, "freeze public score")
        elif any(
            value is not None
            for value in (
                self.freeze_receipt_path,
                self.freeze_receipt_sha256,
                self.freeze_lineage_position,
                self.freeze_candidate_sha256,
                self.freeze_public_score,
            )
        ):
            raise ValueError("H0 evaluation cannot carry private freeze authorization")


@dataclass(frozen=True)
class OfficialEvaluationResult:
    score: float | None
    valid: bool
    public_feedback: str
    evaluator_receipt_sha256: str
    private_evidence_sha256: str
    evaluator_call_count: int = 1

    def __post_init__(self) -> None:
        if type(self.valid) is not bool:
            raise ValueError("official evaluation validity must be boolean")
        _numeric_score(self.score, "official evaluation score", allow_none=True)
        if self.valid:
            _numeric_score(self.score, "valid official evaluation score")
        if not isinstance(self.public_feedback, str) or len(self.public_feedback) > 32_000:
            raise ValueError("official public feedback is invalid")
        _require_sha256(self.evaluator_receipt_sha256, "evaluator receipt hash")
        _require_sha256(self.private_evidence_sha256, "private evaluator evidence hash")
        if self.evaluator_call_count != 1:
            raise ValueError("official evaluator ledger must prove exactly one call")


@dataclass(frozen=True)
class CrossTestReceipt:
    schema_version: int
    manifest_sha256: str
    benchmark: str
    seed_id: str
    status: str
    source_position: str
    target_position: str
    task_id: str
    target_binding_sha256: str
    freeze_receipt_sha256: str
    transfer_provenance_sha256: str
    harness_sha256: str
    candidate_sha256: str | None
    candidate_archive_sha256: str | None
    official_score: float | None
    official_score_valid: bool
    public_feedback: str
    evaluator_receipt_sha256: str | None
    private_evidence_sha256: str | None
    audit_ledger_sha256: str | None
    solver_model_configuration_sha256: str
    evaluator_contract_sha256: str
    moss_revision_sha256: str
    tracked_tree_sha256: str
    source_revision_sha256: str
    task_data_revision_sha256: str
    image_digest_sha256: str
    api_base_host_sha256: str
    task_sha256: str
    fresh_root_proof_sha256: str
    operation_journal_head_sha256: str
    builder_constructed_count: int
    builder_call_count: int
    solver_call_count: int
    memory_read_count: int
    official_evaluator_call_count: int

    def __post_init__(self) -> None:
        if self.schema_version != 1:
            raise ValueError("unsupported cross-test receipt schema")
        if self.source_position not in _POSITIONS or self.target_position not in _POSITIONS:
            raise ValueError("cross-test positions are invalid")
        if self.seed_id not in _SEEDS:
            raise ValueError("cross-test seed is invalid")
        if self.status not in {"completed", "invalid", "abandoned"}:
            raise ValueError("cross-test status is invalid")
        if type(self.official_score_valid) is not bool:
            raise ValueError("cross-test score validity is invalid")
        _numeric_score(self.official_score, "cross-test score", allow_none=True)
        if self.official_score_valid:
            _numeric_score(self.official_score, "valid cross-test score")
        counts = (
            self.builder_constructed_count,
            self.builder_call_count,
            self.solver_call_count,
            self.memory_read_count,
            self.official_evaluator_call_count,
        )
        if any(not isinstance(value, int) or isinstance(value, bool) or value < 0 for value in counts):
            raise ValueError("cross-test call ledger counts are invalid")
        if self.status == "completed" and counts != (0, 0, 1, 0, 1):
            raise ValueError("cross-test completed ledger must be 0/0/1/0/1")
        if self.status != "completed" and self.official_score_valid:
            raise ValueError("non-completed cross-test receipt cannot authorize a score")
        for field_name in (
            "manifest_sha256",
            "target_binding_sha256",
            "freeze_receipt_sha256",
            "transfer_provenance_sha256",
            "harness_sha256",
            "solver_model_configuration_sha256",
            "evaluator_contract_sha256",
            "moss_revision_sha256",
            "tracked_tree_sha256",
            "source_revision_sha256",
            "task_data_revision_sha256",
            "image_digest_sha256",
            "api_base_host_sha256",
            "task_sha256",
            "fresh_root_proof_sha256",
            "operation_journal_head_sha256",
        ):
            _require_sha256(getattr(self, field_name), field_name.replace("_", " "))
        optional_evidence = (
            self.candidate_sha256,
            self.candidate_archive_sha256,
            self.evaluator_receipt_sha256,
            self.private_evidence_sha256,
            self.audit_ledger_sha256,
        )
        if self.status == "completed" and any(value is None for value in optional_evidence):
            raise ValueError("completed cross-test receipt is missing evidence")
        for value in optional_evidence:
            if value is not None:
                _require_sha256(value, "cross-test optional evidence hash")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "CrossTestReceipt":
        _exact_mapping(payload, set(cls.__dataclass_fields__), "cross-test receipt")
        return cls(**dict(payload))


@dataclass(frozen=True)
class H0BaselineReceipt:
    schema_version: int
    manifest_sha256: str
    benchmark: str
    seed_id: str
    status: str
    target_position: str
    task_id: str
    target_binding_sha256: str
    h0_sha256: str
    candidate_sha256: str | None
    candidate_archive_sha256: str | None
    official_score: float | None
    official_score_valid: bool
    public_feedback: str
    evaluator_receipt_sha256: str | None
    private_evidence_sha256: str | None
    audit_ledger_sha256: str | None
    upper_model_configuration: Mapping[str, Any]
    lower_model_configuration: Mapping[str, Any]
    upper_model_configuration_sha256: str
    lower_model_configuration_sha256: str
    evaluator_contract_sha256: str
    moss_revision_sha256: str
    tracked_tree_sha256: str
    source_revision_sha256: str
    task_data_revision_sha256: str
    image_digest_sha256: str
    api_base_host_sha256: str
    task_sha256: str
    fresh_root_proof_sha256: str
    operation_journal_head_sha256: str
    builder_constructed_count: int
    builder_call_count: int
    solver_call_count: int
    memory_read_count: int
    official_evaluator_call_count: int

    def __post_init__(self) -> None:
        if self.schema_version != 1 or self.target_position not in _POSITIONS:
            raise ValueError("H0 baseline receipt identity is invalid")
        if self.seed_id not in _SEEDS:
            raise ValueError("H0 baseline seed is invalid")
        if self.status not in {"completed", "invalid", "abandoned"}:
            raise ValueError("H0 baseline status is invalid")
        upper = _json_copy(self.upper_model_configuration, "upper model configuration")
        lower = _json_copy(self.lower_model_configuration, "lower model configuration")
        if not isinstance(upper, dict) or not isinstance(lower, dict):
            raise ValueError("H0 model configurations must be objects")
        allowed = {
            "provider",
            "api_family",
            "transport",
            "model",
            "reasoning_effort",
            "max_output_tokens",
            "sampling_parameters",
            "tool_permission_policy",
        }
        if set(upper) != allowed or set(lower) != allowed:
            raise ValueError("H0 model configuration contains non-configuration state")
        if upper != lower:
            raise ValueError("H0 upper and lower model configurations must be identical")
        if upper["model"] != "gpt-5.6-sol" or upper["reasoning_effort"] != "high":
            raise ValueError("H0 model configuration must be gpt-5.6-sol/high")
        object.__setattr__(self, "upper_model_configuration", MappingProxyType(upper))
        object.__setattr__(self, "lower_model_configuration", MappingProxyType(lower))
        if (
            self.upper_model_configuration_sha256
            != self.lower_model_configuration_sha256
            or self.upper_model_configuration_sha256 != _sha256_json(upper)
        ):
            raise ValueError("H0 upper/lower model configuration hashes must be equal")
        counts = (
            self.builder_constructed_count,
            self.builder_call_count,
            self.solver_call_count,
            self.memory_read_count,
            self.official_evaluator_call_count,
        )
        if any(not isinstance(value, int) or isinstance(value, bool) or value < 0 for value in counts):
            raise ValueError("H0 baseline call ledger counts are invalid")
        if self.status == "completed" and counts != (0, 0, 1, 0, 1):
            raise ValueError("H0 completed ledger must be 0/0/1/0/1")
        if self.status != "completed" and self.official_score_valid:
            raise ValueError("non-completed H0 receipt cannot authorize a score")
        if type(self.official_score_valid) is not bool:
            raise ValueError("H0 score validity is invalid")
        _numeric_score(self.official_score, "H0 official score", allow_none=True)
        if self.official_score_valid:
            _numeric_score(self.official_score, "valid H0 official score")
        for field_name in (
            "manifest_sha256",
            "target_binding_sha256",
            "h0_sha256",
            "upper_model_configuration_sha256",
            "lower_model_configuration_sha256",
            "evaluator_contract_sha256",
            "moss_revision_sha256",
            "tracked_tree_sha256",
            "source_revision_sha256",
            "task_data_revision_sha256",
            "image_digest_sha256",
            "api_base_host_sha256",
            "task_sha256",
            "fresh_root_proof_sha256",
            "operation_journal_head_sha256",
        ):
            _require_sha256(getattr(self, field_name), field_name.replace("_", " "))
        optional_evidence = (
            self.candidate_sha256,
            self.candidate_archive_sha256,
            self.evaluator_receipt_sha256,
            self.private_evidence_sha256,
            self.audit_ledger_sha256,
        )
        if self.status == "completed" and any(value is None for value in optional_evidence):
            raise ValueError("completed H0 receipt is missing evidence")
        for value in optional_evidence:
            if value is not None:
                _require_sha256(value, "H0 optional evidence hash")

    def to_dict(self) -> dict[str, Any]:
        payload = {
            field_name: getattr(self, field_name)
            for field_name in self.__dataclass_fields__
            if field_name not in {
                "upper_model_configuration",
                "lower_model_configuration",
            }
        }
        payload["upper_model_configuration"] = _json_copy(
            self.upper_model_configuration, "upper model configuration"
        )
        payload["lower_model_configuration"] = _json_copy(
            self.lower_model_configuration, "lower model configuration"
        )
        return payload

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "H0BaselineReceipt":
        _exact_mapping(payload, set(cls.__dataclass_fields__), "H0 baseline receipt")
        return cls(**dict(payload))


class CrossMatrixRunner:
    """Execute isolated one-shot transfer and H0 cells with durable receipts."""

    def __init__(
        self,
        *,
        manifest: ExperimentOneManifest,
        root: Path,
        task_executor_factory: Callable[
            [Path, str], Callable[[TaskExecutionRequest], TaskExecutionResult]
        ],
        evaluator_factory: Callable[
            [Path, str], Callable[[EvaluationRequest], OfficialEvaluationResult]
        ],
    ) -> None:
        if not callable(task_executor_factory) or not callable(evaluator_factory):
            raise TypeError("cross cells require executor and evaluator factories")
        self.manifest = manifest
        self.root = Path(root).resolve()
        self.task_executor_factory = task_executor_factory
        self.evaluator_factory = evaluator_factory

    def run(
        self,
        *,
        freeze_receipts: Mapping[str, FreezeReceipt],
        frozen_harnesses: Mapping[str, TaskHarnessArtifact],
        freeze_receipt_paths: Mapping[str, Path],
        transfer_provenance: Mapping[str, HarnessTransferProvenance],
    ) -> tuple[CrossTestReceipt, ...]:
        receipts, harnesses, paths, provenance = self._validate_frozen_inputs(
            freeze_receipts=freeze_receipts,
            frozen_harnesses=frozen_harnesses,
            freeze_receipt_paths=freeze_receipt_paths,
            transfer_provenance=transfer_provenance,
        )
        results: list[CrossTestReceipt] = []
        for source_position in _POSITIONS:
            for target_position in _POSITIONS:
                results.append(
                    self._run_cross_cell(
                        source_position=source_position,
                        target_position=target_position,
                        freeze_receipt=receipts[source_position],
                        freeze_receipt_path=paths[source_position],
                        harness=harnesses[source_position],
                        provenance=provenance[source_position],
                    )
                )
        return tuple(results)

    def run_h0_baselines(self) -> tuple[H0BaselineReceipt, ...]:
        return tuple(self._run_h0_baseline(position) for position in _POSITIONS)

    def _run_cross_cell(
        self,
        *,
        source_position: str,
        target_position: str,
        freeze_receipt: FreezeReceipt,
        freeze_receipt_path: Path,
        harness: TaskHarnessArtifact,
        provenance: HarnessTransferProvenance,
    ) -> CrossTestReceipt:
        target = self.manifest.target(target_position)
        operation_id = f"{self.manifest.seed_id}-cross-{source_position}-to-{target_position}"
        cell_root = (self.root / "cross_matrix" / f"{source_position}-to-{target_position}").resolve()
        fresh_root_proof_sha256 = self._claim_fresh_root(
            cell_root,
            {
                "schema_version": 1,
                "kind": "cross_test",
                "manifest_sha256": self.manifest.sha256,
                "source_position": source_position,
                "target_position": target_position,
            },
        )
        task_sha256 = hashlib.sha256(target.task.encode("utf-8")).hexdigest()
        start_payload = {
            "schema_version": 1,
            "kind": "cross_test",
            "manifest_sha256": self.manifest.sha256,
            "operation_id": operation_id,
            "source_position": source_position,
            "target_position": target_position,
            "target_binding_sha256": target.sha256,
            "freeze_receipt_sha256": freeze_receipt.sha256,
            "transfer_provenance_sha256": provenance.sha256,
            "harness_sha256": harness.sha256,
            "solver_model_configuration_sha256": self.manifest.solver_model_configuration.sha256,
            "evaluator_contract_sha256": target.evaluator_contract_sha256,
            "moss_revision_sha256": self.manifest.moss_revision_sha256,
            "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
            "source_revision_sha256": self.manifest.source_revision_sha256,
            "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
            "image_digest_sha256": self.manifest.image_digest_sha256,
            "api_base_host_sha256": self.manifest.api_base_host_sha256,
            "task_sha256": task_sha256,
        }
        start_path = cell_root / "operation.started.json"
        result_path = cell_root / "receipt.json"
        abandoned_path = cell_root / "operation.abandoned.json"
        replay = self._load_cross_replay(
            result_path=result_path,
            abandoned_path=abandoned_path,
            start_path=start_path,
            expected_start=start_payload,
            source_position=source_position,
            target_position=target_position,
            freeze_receipt=freeze_receipt,
            harness=harness,
            provenance=provenance,
            fresh_root_proof_sha256=fresh_root_proof_sha256,
        )
        if replay is not None:
            return replay
        operation_head = _write_once(start_path, start_payload)
        execution: TaskExecutionResult | None = None
        evaluation: OfficialEvaluationResult | None = None
        failure_stage = "solver"
        try:
            executor = self.task_executor_factory(cell_root, operation_id)
            evaluator = self.evaluator_factory(cell_root, operation_id)
            if not callable(executor) or not callable(evaluator):
                raise TypeError("cell factories must return callables")
            execution = executor(
                TaskExecutionRequest(
                    manifest_sha256=self.manifest.sha256,
                    operation_id=operation_id,
                    source_position=source_position,
                    target=target,
                    harness=harness,
                    task=target.task,
                    model_configuration=self.manifest.solver_model_configuration,
                    cell_root=cell_root,
                    history=(),
                    memory={},
                )
            )
            if not isinstance(execution, TaskExecutionResult):
                raise TypeError("task executor must return TaskExecutionResult")
            if execution.call_ledger.operation_id != operation_id:
                raise ValueError("task execution ledger belongs to another operation")
            _write_once(
                cell_root / "execution.evidence.json",
                self._execution_evidence_payload(execution),
            )
            execution.call_ledger.require_frozen_solver_only()
            failure_stage = "evaluator"
            raw_evaluation = evaluator(
                EvaluationRequest(
                    manifest_sha256=self.manifest.sha256,
                    operation_id=operation_id,
                    target=target,
                    candidate=execution,
                    cell_root=cell_root,
                    frozen_harness_sha256=harness.sha256,
                    private_eval_allowed=True,
                    freeze_receipt_path=freeze_receipt_path,
                    freeze_receipt_sha256=freeze_receipt.sha256,
                    freeze_lineage_position=source_position,
                    freeze_candidate_sha256=freeze_receipt.candidate_sha256,
                    freeze_public_score=freeze_receipt.official_score,
                )
            )
            if not isinstance(raw_evaluation, OfficialEvaluationResult):
                raise TypeError("evaluator must return OfficialEvaluationResult")
            evaluation = raw_evaluation
            _write_once(
                cell_root / "evaluation.evidence.json",
                self._evaluation_evidence_payload(evaluation, operation_id),
            )
            receipt = self._cross_receipt(
                status="completed",
                source_position=source_position,
                target_position=target_position,
                target=target,
                freeze_receipt=freeze_receipt,
                harness=harness,
                provenance=provenance,
                execution=execution,
                evaluation=evaluation,
                feedback=evaluation.public_feedback,
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
        except Exception as exc:
            partial_ledger = (
                None
                if execution is not None
                else self._partial_solver_call_ledger(cell_root, operation_id)
            )
            error_payload = {
                "schema_version": 1,
                "kind": "cross_test_error",
                "operation_id": operation_id,
                "source_position": source_position,
                "target_position": target_position,
                "failure_stage": failure_stage,
                "error_type": type(exc).__name__,
                "error_message": str(exc)[:4000],
                "official_score": None,
                "official_score_valid": False,
                "retry": False,
            }
            if partial_ledger is not None:
                error_payload.update(
                    {
                        "solver_call_count": partial_ledger.solver_call_count,
                        "audit_ledger_sha256": partial_ledger.audit_ledger_sha256,
                    }
                )
            _write_once(cell_root / "error.evidence.json", error_payload)
            receipt = self._cross_receipt(
                status="invalid",
                source_position=source_position,
                target_position=target_position,
                target=target,
                freeze_receipt=freeze_receipt,
                harness=harness,
                provenance=provenance,
                execution=execution,
                evaluation=evaluation,
                partial_ledger=partial_ledger,
                feedback=f"terminal invalid cell: {failure_stage}:{type(exc).__name__}",
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
        _write_once(result_path, receipt.to_dict())
        return receipt

    def _cross_receipt(
        self,
        *,
        status: str,
        source_position: str,
        target_position: str,
        target: TargetBinding,
        freeze_receipt: FreezeReceipt,
        harness: TaskHarnessArtifact,
        provenance: HarnessTransferProvenance,
        execution: TaskExecutionResult | None,
        evaluation: OfficialEvaluationResult | None,
        feedback: str,
        fresh_root_proof_sha256: str,
        operation_head: str,
        partial_ledger: CallLedgerEvidence | None = None,
    ) -> CrossTestReceipt:
        ledger = execution.call_ledger if execution is not None else partial_ledger
        completed = status == "completed"
        return CrossTestReceipt(
            schema_version=1,
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            status=status,
            source_position=source_position,
            target_position=target_position,
            task_id=target.task_id,
            target_binding_sha256=target.sha256,
            freeze_receipt_sha256=freeze_receipt.sha256,
            transfer_provenance_sha256=provenance.sha256,
            harness_sha256=harness.sha256,
            candidate_sha256=execution.candidate_sha256 if execution else None,
            candidate_archive_sha256=execution.candidate_archive_sha256 if execution else None,
            official_score=evaluation.score if completed and evaluation else None,
            official_score_valid=bool(completed and evaluation and evaluation.valid),
            public_feedback=feedback,
            evaluator_receipt_sha256=evaluation.evaluator_receipt_sha256 if evaluation else None,
            private_evidence_sha256=evaluation.private_evidence_sha256 if evaluation else None,
            audit_ledger_sha256=ledger.audit_ledger_sha256 if ledger else None,
            solver_model_configuration_sha256=self.manifest.solver_model_configuration.sha256,
            evaluator_contract_sha256=target.evaluator_contract_sha256,
            moss_revision_sha256=self.manifest.moss_revision_sha256,
            tracked_tree_sha256=self.manifest.tracked_tree_sha256,
            source_revision_sha256=self.manifest.source_revision_sha256,
            task_data_revision_sha256=self.manifest.task_data_revision_sha256,
            image_digest_sha256=self.manifest.image_digest_sha256,
            api_base_host_sha256=self.manifest.api_base_host_sha256,
            task_sha256=hashlib.sha256(target.task.encode("utf-8")).hexdigest(),
            fresh_root_proof_sha256=fresh_root_proof_sha256,
            operation_journal_head_sha256=operation_head,
            builder_constructed_count=ledger.builder_constructed_count if ledger else 0,
            builder_call_count=ledger.builder_call_count if ledger else 0,
            solver_call_count=ledger.solver_call_count if ledger else 0,
            memory_read_count=ledger.memory_read_count if ledger else 0,
            official_evaluator_call_count=evaluation.evaluator_call_count if evaluation else 0,
        )

    @staticmethod
    def _partial_solver_call_ledger(
        cell_root: Path, operation_id: str
    ) -> CallLedgerEvidence | None:
        ledger_path = cell_root / "audit" / "solver_model_calls.jsonl"
        if not ledger_path.is_file():
            return None
        raw = ledger_path.read_bytes()
        solver_call_count = 0
        prefix = f"{operation_id}-"
        for raw_line in raw.splitlines():
            if not raw_line:
                continue
            try:
                record = json.loads(raw_line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
            record_operation_id = (
                record.get("operation_id") if isinstance(record, dict) else None
            )
            if (
                isinstance(record_operation_id, str)
                and (record_operation_id == operation_id or record_operation_id.startswith(prefix))
                and record.get("event") == "start"
            ):
                solver_call_count += 1
        return CallLedgerEvidence(
            operation_id=operation_id,
            builder_constructed_count=0,
            builder_call_count=0,
            solver_call_count=solver_call_count,
            memory_read_count=0,
            audit_ledger_sha256=hashlib.sha256(raw).hexdigest(),
        )

    def _run_h0_baseline(self, target_position: str) -> H0BaselineReceipt:
        target = self.manifest.target(target_position)
        operation_id = f"{self.manifest.seed_id}-h0-{target_position}"
        cell_root = (self.root / "h0_baselines" / target_position).resolve()
        fresh_root_proof_sha256 = self._claim_fresh_root(
            cell_root,
            {
                "schema_version": 1,
                "kind": "h0_baseline",
                "manifest_sha256": self.manifest.sha256,
                "target_position": target_position,
            },
        )
        start_payload = {
            "schema_version": 1,
            "kind": "h0_baseline",
            "manifest_sha256": self.manifest.sha256,
            "operation_id": operation_id,
            "target_position": target_position,
            "target_binding_sha256": target.sha256,
            "h0_sha256": self.manifest.h0.sha256,
            "upper_model_configuration_sha256": self.manifest.builder_model_configuration.sha256,
            "lower_model_configuration_sha256": self.manifest.solver_model_configuration.sha256,
            "evaluator_contract_sha256": target.evaluator_contract_sha256,
            "moss_revision_sha256": self.manifest.moss_revision_sha256,
            "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
            "source_revision_sha256": self.manifest.source_revision_sha256,
            "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
            "image_digest_sha256": self.manifest.image_digest_sha256,
            "api_base_host_sha256": self.manifest.api_base_host_sha256,
            "task_sha256": hashlib.sha256(target.task.encode("utf-8")).hexdigest(),
        }
        start_path = cell_root / "operation.started.json"
        result_path = cell_root / "receipt.json"
        abandoned_path = cell_root / "operation.abandoned.json"
        replay = self._load_h0_replay(
            result_path=result_path,
            abandoned_path=abandoned_path,
            start_path=start_path,
            expected_start=start_payload,
            target_position=target_position,
            fresh_root_proof_sha256=fresh_root_proof_sha256,
        )
        if replay is not None:
            return replay
        operation_head = _write_once(start_path, start_payload)
        execution: TaskExecutionResult | None = None
        evaluation: OfficialEvaluationResult | None = None
        try:
            executor = self.task_executor_factory(cell_root, operation_id)
            evaluator = self.evaluator_factory(cell_root, operation_id)
            if not callable(executor) or not callable(evaluator):
                raise TypeError("cell factories must return callables")
            execution = executor(
                TaskExecutionRequest(
                    manifest_sha256=self.manifest.sha256,
                    operation_id=operation_id,
                    source_position=target_position,
                    target=target,
                    harness=self.manifest.h0,
                    task=target.task,
                    model_configuration=self.manifest.solver_model_configuration,
                    cell_root=cell_root,
                    history=(),
                    memory={},
                )
            )
            if not isinstance(execution, TaskExecutionResult):
                raise TypeError("task executor must return TaskExecutionResult")
            if execution.call_ledger.operation_id != operation_id:
                raise ValueError("task execution ledger belongs to another operation")
            _write_once(
                cell_root / "execution.evidence.json",
                self._execution_evidence_payload(execution),
            )
            execution.call_ledger.require_frozen_solver_only()
            raw_evaluation = evaluator(
                EvaluationRequest(
                    manifest_sha256=self.manifest.sha256,
                    operation_id=operation_id,
                    target=target,
                    candidate=execution,
                    cell_root=cell_root,
                    frozen_harness_sha256=self.manifest.h0.sha256,
                    private_eval_allowed=False,
                )
            )
            if not isinstance(raw_evaluation, OfficialEvaluationResult):
                raise TypeError("evaluator must return OfficialEvaluationResult")
            evaluation = raw_evaluation
            _write_once(
                cell_root / "evaluation.evidence.json",
                self._evaluation_evidence_payload(evaluation, operation_id),
            )
            receipt = self._h0_receipt(
                status="completed",
                target=target,
                execution=execution,
                evaluation=evaluation,
                feedback=evaluation.public_feedback,
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
        except Exception as exc:
            receipt = self._h0_receipt(
                status="invalid",
                target=target,
                execution=execution,
                evaluation=evaluation,
                feedback=f"terminal invalid cell: {type(exc).__name__}",
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
        _write_once(result_path, receipt.to_dict())
        return receipt

    def _h0_receipt(
        self,
        *,
        status: str,
        target: TargetBinding,
        execution: TaskExecutionResult | None,
        evaluation: OfficialEvaluationResult | None,
        feedback: str,
        fresh_root_proof_sha256: str,
        operation_head: str,
    ) -> H0BaselineReceipt:
        ledger = execution.call_ledger if execution is not None else None
        completed = status == "completed"
        model_payload = self.manifest.solver_model_configuration.to_dict()
        return H0BaselineReceipt(
            schema_version=1,
            manifest_sha256=self.manifest.sha256,
            benchmark=self.manifest.benchmark,
            seed_id=self.manifest.seed_id,
            status=status,
            target_position=target.position,
            task_id=target.task_id,
            target_binding_sha256=target.sha256,
            h0_sha256=self.manifest.h0.sha256,
            candidate_sha256=execution.candidate_sha256 if execution else None,
            candidate_archive_sha256=execution.candidate_archive_sha256 if execution else None,
            official_score=evaluation.score if completed and evaluation else None,
            official_score_valid=bool(completed and evaluation and evaluation.valid),
            public_feedback=feedback,
            evaluator_receipt_sha256=evaluation.evaluator_receipt_sha256 if evaluation else None,
            private_evidence_sha256=evaluation.private_evidence_sha256 if evaluation else None,
            audit_ledger_sha256=execution.audit_ledger_sha256 if execution else None,
            upper_model_configuration=model_payload,
            lower_model_configuration=model_payload,
            upper_model_configuration_sha256=self.manifest.builder_model_configuration.sha256,
            lower_model_configuration_sha256=self.manifest.solver_model_configuration.sha256,
            evaluator_contract_sha256=target.evaluator_contract_sha256,
            moss_revision_sha256=self.manifest.moss_revision_sha256,
            tracked_tree_sha256=self.manifest.tracked_tree_sha256,
            source_revision_sha256=self.manifest.source_revision_sha256,
            task_data_revision_sha256=self.manifest.task_data_revision_sha256,
            image_digest_sha256=self.manifest.image_digest_sha256,
            api_base_host_sha256=self.manifest.api_base_host_sha256,
            task_sha256=hashlib.sha256(target.task.encode("utf-8")).hexdigest(),
            fresh_root_proof_sha256=fresh_root_proof_sha256,
            operation_journal_head_sha256=operation_head,
            builder_constructed_count=ledger.builder_constructed_count if ledger else 0,
            builder_call_count=ledger.builder_call_count if ledger else 0,
            solver_call_count=ledger.solver_call_count if ledger else 0,
            memory_read_count=ledger.memory_read_count if ledger else 0,
            official_evaluator_call_count=evaluation.evaluator_call_count if evaluation else 0,
        )

    def _validate_frozen_inputs(
        self,
        *,
        freeze_receipts: Mapping[str, FreezeReceipt],
        frozen_harnesses: Mapping[str, TaskHarnessArtifact],
        freeze_receipt_paths: Mapping[str, Path],
        transfer_provenance: Mapping[str, HarnessTransferProvenance],
    ) -> tuple[
        dict[str, FreezeReceipt],
        dict[str, TaskHarnessArtifact],
        dict[str, Path],
        dict[str, HarnessTransferProvenance],
    ]:
        required = set(_POSITIONS)
        if any(
            set(mapping) != required
            for mapping in (
                freeze_receipts,
                frozen_harnesses,
                freeze_receipt_paths,
                transfer_provenance,
            )
        ):
            raise ValueError("cross matrix requires complete A/B/C freeze authorization")
        receipts = dict(freeze_receipts)
        harnesses = dict(frozen_harnesses)
        paths = {key: Path(value).resolve() for key, value in freeze_receipt_paths.items()}
        provenance = dict(transfer_provenance)
        for position in _POSITIONS:
            receipt = receipts[position]
            harness = harnesses[position]
            path = paths[position]
            proof = provenance[position]
            if not isinstance(receipt, FreezeReceipt) or not isinstance(harness, TaskHarnessArtifact):
                raise TypeError("cross matrix requires FreezeReceipt and Harness artifacts")
            if not isinstance(proof, HarnessTransferProvenance):
                raise TypeError("cross matrix requires transfer provenance")
            saved, saved_sha = _load_once(path, label="FreezeReceipt authorization")
            if saved != receipt.to_dict() or saved_sha != receipt.sha256:
                raise ValueError("FreezeReceipt path/hash authorization is invalid")
            source_target = self.manifest.target(position)
            expected = {
                "manifest_sha256": self.manifest.sha256,
                "benchmark": self.manifest.benchmark,
                "seed_id": self.manifest.seed_id,
                "position": position,
                "task_id": source_target.task_id,
                "target_binding_sha256": source_target.sha256,
                "harness_sha256": harness.sha256,
                "builder_model_configuration_sha256": self.manifest.builder_model_configuration.sha256,
                "solver_model_configuration_sha256": self.manifest.solver_model_configuration.sha256,
                "evaluator_contract_sha256": source_target.evaluator_contract_sha256,
                "moss_revision_sha256": self.manifest.moss_revision_sha256,
                "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
                "source_revision_sha256": self.manifest.source_revision_sha256,
                "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
                "image_digest_sha256": self.manifest.image_digest_sha256,
                "api_base_host_sha256": self.manifest.api_base_host_sha256,
                "valid": True,
            }
            if any(getattr(receipt, key) != value for key, value in expected.items()):
                raise ValueError("FreezeReceipt does not match the experiment manifest")
            if (
                not receipt.ancestry_sha256s
                or receipt.ancestry_sha256s[0] != self.manifest.h0.sha256
                or receipt.ancestry_sha256s[-1] != harness.sha256
            ):
                raise ValueError("FreezeReceipt Harness ancestry is invalid")
            expected_proof = HarnessTransferProvenance.cleared(
                source_position=position, harness=harness
            )
            if proof != expected_proof:
                raise ValueError("transfer provenance does not prove cleared source-private state")
        return receipts, harnesses, paths, provenance

    def _claim_fresh_root(self, path: Path, binding: Mapping[str, Any]) -> str:
        marker = path / "fresh_root_receipt.json"
        if path.exists() and not marker.is_file() and any(path.iterdir()):
            raise ValueError("fresh root requirement failed: root is already occupied")
        path.mkdir(parents=True, exist_ok=True)
        proof_sha256 = _write_once(marker, binding)
        saved, saved_sha256 = _load_once(marker, label="fresh root receipt")
        if saved != dict(binding) or saved_sha256 != proof_sha256:
            raise ValueError("fresh root receipt belongs to another operation")
        return proof_sha256

    @staticmethod
    def _execution_evidence_payload(execution: TaskExecutionResult) -> dict[str, Any]:
        ledger = execution.call_ledger
        return {
            "schema_version": 1,
            "operation_id": ledger.operation_id,
            "candidate_sha256": execution.candidate_sha256,
            "candidate_archive_sha256": execution.candidate_archive_sha256,
            "audit_ledger_sha256": ledger.audit_ledger_sha256,
            "builder_constructed_count": ledger.builder_constructed_count,
            "builder_call_count": ledger.builder_call_count,
            "solver_call_count": ledger.solver_call_count,
            "memory_read_count": ledger.memory_read_count,
        }

    @staticmethod
    def _evaluation_evidence_payload(
        evaluation: OfficialEvaluationResult, operation_id: str
    ) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "operation_id": operation_id,
            "official_score": evaluation.score,
            "official_score_valid": evaluation.valid,
            "public_feedback": evaluation.public_feedback,
            "evaluator_receipt_sha256": evaluation.evaluator_receipt_sha256,
            "private_evidence_sha256": evaluation.private_evidence_sha256,
            "official_evaluator_call_count": evaluation.evaluator_call_count,
        }

    def _verify_terminal_evidence(
        self,
        *,
        cell_root: Path,
        operation_id: str,
        receipt: CrossTestReceipt | H0BaselineReceipt,
    ) -> None:
        execution_path = cell_root / "execution.evidence.json"
        evaluation_path = cell_root / "evaluation.evidence.json"
        execution_expected = {
            "schema_version": 1,
            "operation_id": operation_id,
            "candidate_sha256": receipt.candidate_sha256,
            "candidate_archive_sha256": receipt.candidate_archive_sha256,
            "audit_ledger_sha256": receipt.audit_ledger_sha256,
            "builder_constructed_count": receipt.builder_constructed_count,
            "builder_call_count": receipt.builder_call_count,
            "solver_call_count": receipt.solver_call_count,
            "memory_read_count": receipt.memory_read_count,
        }
        execution_required = receipt.status == "completed" or receipt.candidate_sha256 is not None
        if execution_required:
            if not execution_path.is_file():
                raise ValueError("terminal replay lacks execution evidence")
            saved_execution, _ = _load_once(
                execution_path, label="terminal execution evidence"
            )
            if saved_execution != execution_expected:
                raise ValueError("terminal replay execution evidence differs")

        evaluation_expected = {
            "schema_version": 1,
            "operation_id": operation_id,
            "official_score": receipt.official_score,
            "official_score_valid": receipt.official_score_valid,
            "public_feedback": receipt.public_feedback,
            "evaluator_receipt_sha256": receipt.evaluator_receipt_sha256,
            "private_evidence_sha256": receipt.private_evidence_sha256,
            "official_evaluator_call_count": receipt.official_evaluator_call_count,
        }
        evaluation_required = receipt.status == "completed"
        if evaluation_required:
            if not evaluation_path.is_file():
                raise ValueError("terminal replay lacks evaluation evidence")
            saved_evaluation, _ = _load_once(
                evaluation_path, label="terminal evaluation evidence"
            )
            if saved_evaluation != evaluation_expected:
                raise ValueError("terminal replay evaluation evidence differs")

    def _load_cross_replay(
        self,
        *,
        result_path: Path,
        abandoned_path: Path,
        start_path: Path,
        expected_start: Mapping[str, Any],
        source_position: str,
        target_position: str,
        freeze_receipt: FreezeReceipt,
        harness: TaskHarnessArtifact,
        provenance: HarnessTransferProvenance,
        fresh_root_proof_sha256: str,
    ) -> CrossTestReceipt | None:
        terminal = [path for path in (result_path, abandoned_path) if path.is_file()]
        if len(terminal) > 1:
            raise ValueError("cross-test operation has multiple terminal records")
        if not terminal:
            if not start_path.is_file():
                return None
            operation_head = self._verify_start(start_path, expected_start)
            target = self.manifest.target(target_position)
            receipt = self._cross_receipt(
                status="abandoned",
                source_position=source_position,
                target_position=target_position,
                target=target,
                freeze_receipt=freeze_receipt,
                harness=harness,
                provenance=provenance,
                execution=None,
                evaluation=None,
                feedback="terminal abandonment: started_without_durable_result",
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
            _write_once(abandoned_path, receipt.to_dict())
            return receipt
        operation_head = self._verify_start(start_path, expected_start)
        payload, _ = _load_once(terminal[0], label="cross-test terminal receipt")
        receipt = CrossTestReceipt.from_dict(payload)
        self._verify_cross_receipt(
            receipt=receipt,
            cell_root=result_path.parent,
            source_position=source_position,
            target_position=target_position,
            freeze_receipt=freeze_receipt,
            harness=harness,
            provenance=provenance,
            fresh_root_proof_sha256=fresh_root_proof_sha256,
            operation_head=operation_head,
        )
        return receipt

    def _verify_cross_receipt(
        self,
        *,
        receipt: CrossTestReceipt,
        cell_root: Path,
        source_position: str,
        target_position: str,
        freeze_receipt: FreezeReceipt,
        harness: TaskHarnessArtifact,
        provenance: HarnessTransferProvenance,
        fresh_root_proof_sha256: str,
        operation_head: str,
    ) -> None:
        target = self.manifest.target(target_position)
        expected = {
            "manifest_sha256": self.manifest.sha256,
            "benchmark": self.manifest.benchmark,
            "seed_id": self.manifest.seed_id,
            "source_position": source_position,
            "target_position": target_position,
            "task_id": target.task_id,
            "target_binding_sha256": target.sha256,
            "freeze_receipt_sha256": freeze_receipt.sha256,
            "transfer_provenance_sha256": provenance.sha256,
            "harness_sha256": harness.sha256,
            "solver_model_configuration_sha256": self.manifest.solver_model_configuration.sha256,
            "evaluator_contract_sha256": target.evaluator_contract_sha256,
            "moss_revision_sha256": self.manifest.moss_revision_sha256,
            "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
            "source_revision_sha256": self.manifest.source_revision_sha256,
            "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
            "image_digest_sha256": self.manifest.image_digest_sha256,
            "api_base_host_sha256": self.manifest.api_base_host_sha256,
            "task_sha256": hashlib.sha256(target.task.encode("utf-8")).hexdigest(),
            "fresh_root_proof_sha256": fresh_root_proof_sha256,
            "operation_journal_head_sha256": operation_head,
        }
        if any(getattr(receipt, key) != value for key, value in expected.items()):
            raise ValueError("cross-test replay evidence differs from the manifest")
        self._verify_terminal_evidence(
            cell_root=cell_root,
            operation_id=f"{self.manifest.seed_id}-cross-{source_position}-to-{target_position}",
            receipt=receipt,
        )

    def _load_h0_replay(
        self,
        *,
        result_path: Path,
        abandoned_path: Path,
        start_path: Path,
        expected_start: Mapping[str, Any],
        target_position: str,
        fresh_root_proof_sha256: str,
    ) -> H0BaselineReceipt | None:
        terminal = [path for path in (result_path, abandoned_path) if path.is_file()]
        if len(terminal) > 1:
            raise ValueError("H0 operation has multiple terminal records")
        if not terminal:
            if not start_path.is_file():
                return None
            operation_head = self._verify_start(start_path, expected_start)
            receipt = self._h0_receipt(
                status="abandoned",
                target=self.manifest.target(target_position),
                execution=None,
                evaluation=None,
                feedback="terminal abandonment: started_without_durable_result",
                fresh_root_proof_sha256=fresh_root_proof_sha256,
                operation_head=operation_head,
            )
            _write_once(abandoned_path, receipt.to_dict())
            return receipt
        operation_head = self._verify_start(start_path, expected_start)
        payload, _ = _load_once(terminal[0], label="H0 terminal receipt")
        receipt = H0BaselineReceipt.from_dict(payload)
        target = self.manifest.target(target_position)
        expected = {
            "manifest_sha256": self.manifest.sha256,
            "benchmark": self.manifest.benchmark,
            "seed_id": self.manifest.seed_id,
            "target_position": target_position,
            "task_id": target.task_id,
            "target_binding_sha256": target.sha256,
            "h0_sha256": self.manifest.h0.sha256,
            "upper_model_configuration_sha256": self.manifest.builder_model_configuration.sha256,
            "lower_model_configuration_sha256": self.manifest.solver_model_configuration.sha256,
            "evaluator_contract_sha256": target.evaluator_contract_sha256,
            "moss_revision_sha256": self.manifest.moss_revision_sha256,
            "tracked_tree_sha256": self.manifest.tracked_tree_sha256,
            "source_revision_sha256": self.manifest.source_revision_sha256,
            "task_data_revision_sha256": self.manifest.task_data_revision_sha256,
            "image_digest_sha256": self.manifest.image_digest_sha256,
            "api_base_host_sha256": self.manifest.api_base_host_sha256,
            "task_sha256": hashlib.sha256(target.task.encode("utf-8")).hexdigest(),
            "fresh_root_proof_sha256": fresh_root_proof_sha256,
            "operation_journal_head_sha256": operation_head,
        }
        if any(getattr(receipt, key) != value for key, value in expected.items()):
            raise ValueError("H0 replay evidence differs from the manifest")
        self._verify_terminal_evidence(
            cell_root=result_path.parent,
            operation_id=f"{self.manifest.seed_id}-h0-{target_position}",
            receipt=receipt,
        )
        return receipt

    @staticmethod
    def _verify_start(path: Path, expected: Mapping[str, Any]) -> str:
        payload, payload_sha256 = _load_once(path, label="operation start")
        if payload != dict(expected):
            raise ValueError("operation start belongs to another request")
        return payload_sha256
