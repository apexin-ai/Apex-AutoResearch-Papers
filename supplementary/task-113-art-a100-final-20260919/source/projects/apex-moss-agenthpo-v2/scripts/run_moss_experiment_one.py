#!/usr/bin/env python3
"""Production entry point for Moss Experiment One.

Every command emits one JSON object.  Commands that can call a model, invoke an
official evaluator, or write formal evidence are planning-only unless ``--execute``
is supplied.  The controller and evaluator modules are imported only after that
gate, so a dry run cannot accidentally spend API or evaluator budget.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field, is_dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from optimization_lab.harness_builder.builder_memory import (
    BuilderMemoryConfig,
    CrossTaskMemoryStore,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
# Allow invocation by absolute path from any working directory.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
MANIFEST_ROOT = PROJECT_ROOT / "optimization_lab" / "harness_builder" / "manifests"
DEFAULT_MANIFESTS = {
    "edgebench": MANIFEST_ROOT / "experiment_one_edgebench.json",
    "alebench": MANIFEST_ROOT / "experiment_one_alebench.json",
}
V2_MANIFESTS = {
    "edgebench": MANIFEST_ROOT / "experiment_one_edgebench_v2.json",
    "alebench": MANIFEST_ROOT / "experiment_one_alebench_v2.json",
}
POSITIONS = ("A", "B", "C")
SEEDS = ("S1", "S2", "S3")
ROUNDS = 8
MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "high"
API_FAMILY = "responses"
FROZEN_TARGETS = {
    "edgebench": {
        "A": "apple_incremental_game",
        "B": "molecular_self_assembly",
        "C": "treant_forest",
    },
    "alebench": {"A": "ahc024", "B": "ahc026", "C": "ahc011"},
}
FROZEN_REVISIONS = {
    "edgebench": (
        "a87350ab80eeb320b13cb71d1b0c3ffcc20a670f",
        "6cc5a7f1b3288ce52484ad828177b8cc86b05b75",
    ),
    "alebench": (
        "f7d927906dc1dcd860ee086e4560d576438b1354",
        "0f426173b4e4e73b09b2b3631ae0490f66b75f99",
    ),
}
FROZEN_MANIFEST_SHA256 = {
    "edgebench": "dd98d418c70d4aca2be7abc87db2b55b2662e7caecde9a9140242310e646c410",
    "alebench": "27bfe5a1eb0ca40d289bb16c04911b0543514fa1c24fe3364f3fd672d633735c",
}
# V2 manifests are additive.  Their hashes are filled after the checked-in
# files are created and are intentionally kept separate from the historical
# V1 replay hashes above.
V2_MANIFEST_SHA256 = {
    "edgebench": "c65ab5c74b90ae2b6f3e17ab8e1ac0a20a1af7eca0c41a3b23524aad015d49ea",
    "alebench": "051ffa04bfdea481fa820d856aafdf5c0af9ca9f3264931a7caa365c718d1bf8",
}


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _json_copy(value: object, label: str) -> Any:
    try:
        return json.loads(_canonical_json(value))
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be JSON serializable") from exc


def _exact_keys(value: object, expected: set[str], label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or set(value) != expected:
        raise ValueError(f"{label} fields differ from the frozen contract")
    return value


@dataclass(frozen=True)
class FrozenModel:
    provider: str
    api_family: str
    transport: str
    model: str
    reasoning_effort: str
    max_output_tokens: int
    sampling_parameters: Mapping[str, Any]
    tool_permission_policy: Mapping[str, Any]

    @classmethod
    def from_dict(cls, payload: object) -> "FrozenModel":
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
        raw = _exact_keys(payload, fields, "model")
        model = cls(**dict(raw))
        if (
            model.model != MODEL
            or model.reasoning_effort != REASONING_EFFORT
            or model.api_family != API_FAMILY
            or model.transport != "https"
            or model.provider != "openai-compatible"
        ):
            raise ValueError("formal models must use gpt-5.6-sol/high Responses API")
        if not isinstance(model.max_output_tokens, int) or model.max_output_tokens < 1:
            raise ValueError("model max_output_tokens is invalid")
        if not isinstance(model.sampling_parameters, Mapping) or not isinstance(
            model.tool_permission_policy, Mapping
        ):
            raise ValueError("model policies must be objects")
        return model


@dataclass(frozen=True)
class FrozenTarget:
    position: str
    task_id: str
    submission_path: str
    evaluator_timeout_seconds: int

    @classmethod
    def from_dict(cls, payload: object) -> "FrozenTarget":
        raw = _exact_keys(
            payload,
            {"position", "task_id", "submission_path", "evaluator_timeout_seconds"},
            "target",
        )
        target = cls(**dict(raw))
        if target.position not in POSITIONS:
            raise ValueError("formal target position must be A/B/C")
        if (
            not isinstance(target.evaluator_timeout_seconds, int)
            or target.evaluator_timeout_seconds < 1
        ):
            raise ValueError("target evaluator timeout is invalid")
        if not target.submission_path or ".." in Path(target.submission_path).parts:
            raise ValueError("target submission path is unsafe")
        return target


@dataclass(frozen=True)
class ResourceEnvelope:
    operating_system: str
    minimum_cpu_count: int
    minimum_memory_gib: int
    minimum_disk_gib: int
    gpu_count: int

    @classmethod
    def from_dict(cls, payload: object) -> "ResourceEnvelope":
        fields = {
            "operating_system",
            "minimum_cpu_count",
            "minimum_memory_gib",
            "minimum_disk_gib",
            "gpu_count",
        }
        resource = cls(**dict(_exact_keys(payload, fields, "resources")))
        if resource.operating_system != "linux" or resource.gpu_count != 0:
            raise ValueError("experiment one requires Linux and no GPU")
        if min(
            resource.minimum_cpu_count,
            resource.minimum_memory_gib,
            resource.minimum_disk_gib,
        ) < 1:
            raise ValueError("resource minimums must be positive")
        return resource


@dataclass(frozen=True)
class OfficialContract:
    source_repository: str
    source_revision: str
    task_data_revision: str
    adapter: str
    evolution_evaluator: str
    cross_test_evaluator: str
    score_direction: str
    require_image_digest: bool

    @classmethod
    def from_dict(cls, payload: object) -> "OfficialContract":
        fields = {
            "source_repository",
            "source_revision",
            "task_data_revision",
            "adapter",
            "evolution_evaluator",
            "cross_test_evaluator",
            "score_direction",
            "require_image_digest",
        }
        contract = cls(**dict(_exact_keys(payload, fields, "official contract")))
        if contract.score_direction != "maximize" or contract.require_image_digest is not True:
            raise ValueError("official score direction/image policy differs")
        return contract


@dataclass(frozen=True)
class FrozenManifest:
    schema_version: int
    experiment_id: str
    suite: str
    benchmark: str
    rounds: int
    seeds: tuple[str, ...]
    h0: Mapping[str, Any]
    builder_model: FrozenModel
    solver_model: FrozenModel
    official: OfficialContract
    resources: ResourceEnvelope
    targets: tuple[FrozenTarget, ...]
    source_path: Path
    sha256: str
    task_harness_schema_version: int = 1

    def target(self, position: str) -> FrozenTarget:
        for target in self.targets:
            if target.position == position:
                return target
        raise ValueError(f"unknown target position: {position}")


def load_frozen_manifest(path: Path, *, expected_harness_version: int | None = None) -> FrozenManifest:
    path = path.resolve()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("formal manifest is unreadable") from exc
    fields = {
        "schema_version",
        "experiment_id",
        "suite",
        "benchmark",
        "rounds",
        "seeds",
        "h0",
        "models",
        "official",
        "resources",
        "targets",
    }
    optional_fields = {"task_harness_schema_version"}
    if not isinstance(payload, Mapping) or not fields.issubset(set(payload)):
        raise ValueError("formal manifest fields differ from the frozen contract")
    if set(payload) - fields - optional_fields:
        raise ValueError("formal manifest fields differ from the frozen contract")
    raw = payload
    if raw["schema_version"] != 1 or raw["experiment_id"] != "moss-experiment-one":
        raise ValueError("unsupported formal manifest identity")
    harness_version = raw.get("task_harness_schema_version", 1)
    if harness_version not in {1, 2}:
        raise ValueError("unsupported Task Harness manifest version")
    if expected_harness_version is not None and harness_version != expected_harness_version:
        raise ValueError("manifest Task Harness version differs from the requested version")
    suite = raw["suite"]
    if suite not in DEFAULT_MANIFESTS:
        raise ValueError("formal manifest suite is unsupported")
    if raw["rounds"] != ROUNDS:
        raise ValueError("formal evolution budget must be exactly eight rounds")
    if raw["seeds"] != list(SEEDS):
        raise ValueError("formal seed IDs must be exactly S1/S2/S3")
    models = _exact_keys(raw["models"], {"builder", "solver"}, "models")
    builder = FrozenModel.from_dict(models["builder"])
    solver = FrozenModel.from_dict(models["solver"])
    if builder != solver:
        raise ValueError("Builder and Solver model configurations must be identical")
    targets_raw = raw["targets"]
    if not isinstance(targets_raw, list):
        raise ValueError("formal targets must be a list")
    targets = tuple(FrozenTarget.from_dict(item) for item in targets_raw)
    mapping = {target.position: target.task_id for target in targets}
    if (
        len(targets) != 3
        or len(mapping) != 3
        or len({target.task_id for target in targets}) != 3
        or mapping != FROZEN_TARGETS[suite]
    ):
        raise ValueError("formal manifest changed the frozen A/B/C mapping")
    official = OfficialContract.from_dict(raw["official"])
    if (
        official.source_revision,
        official.task_data_revision,
    ) != FROZEN_REVISIONS[suite]:
        raise ValueError("official source/data revisions differ from the frozen contract")
    h0 = _json_copy(raw["h0"], "H0")
    if not isinstance(h0, dict):
        raise ValueError("H0 must be an object")
    h0_spec = h0.get("spec")
    if not isinstance(h0_spec, Mapping) or h0_spec.get("schema_version") != harness_version:
        raise ValueError("H0 Task Harness schema differs from the manifest declaration")
    encoded = _canonical_json(payload).encode("utf-8")
    manifest_sha256 = hashlib.sha256(encoded).hexdigest()
    expected_hash = (
        FROZEN_MANIFEST_SHA256[suite]
        if harness_version == 1
        else V2_MANIFEST_SHA256.get(suite)
    )
    if expected_hash is None or manifest_sha256 != expected_hash:
        raise ValueError("formal manifest differs from the checked-in frozen manifest")
    return FrozenManifest(
        schema_version=1,
        experiment_id="moss-experiment-one",
        suite=suite,
        benchmark=str(raw["benchmark"]),
        rounds=ROUNDS,
        seeds=SEEDS,
        h0=h0,
        builder_model=builder,
        solver_model=solver,
        official=official,
        resources=ResourceEnvelope.from_dict(raw["resources"]),
        targets=targets,
        source_path=path,
        sha256=manifest_sha256,
        task_harness_schema_version=harness_version,
    )


@dataclass(frozen=True)
class ExecutionContext:
    manifest: FrozenManifest
    artifact_root: Path
    seed_id: str
    builder_memory_config: BuilderMemoryConfig = field(default_factory=BuilderMemoryConfig)
    memory_arm: str = "B-Frozen"

    @property
    def formal_seed_root(self) -> Path:
        return (
            self.artifact_root / "formal" / self.manifest.suite / self.seed_id
        ).resolve()

    @property
    def canary_suite_root(self) -> Path:
        return (self.artifact_root / "canary" / self.manifest.suite).resolve()

    def lineage_root(self, position: str) -> Path:
        return (self.formal_seed_root / "lineages" / position).resolve()

    def frozen_root(self, position: str) -> Path:
        return (self.formal_seed_root / "frozen" / position).resolve()

    def cross_root(self, source: str, target: str) -> Path:
        return (self.formal_seed_root / "cross" / f"{source}-to-{target}").resolve()

    def baseline_root(self, target: str) -> Path:
        return (self.formal_seed_root / "h0-baselines" / target).resolve()


class ProductionController(Protocol):
    def run_canary(self, position: str) -> object: ...

    def evolve(self, position: str) -> object: ...

    def freeze(self, position: str) -> object: ...

    def cross_test(self) -> object: ...

    def resume(self, position: str | None) -> object: ...


def create_production_controller(context: ExecutionContext) -> ProductionController:
    """Load the Task-4 production factory only after the explicit execute gate."""

    module = importlib.import_module("optimization_lab.harness_builder.experiment_one_production")
    factory = getattr(module, "build_production_controller", None)
    if factory is None or not callable(factory):
        raise RuntimeError(
            "Task-4 integration is unavailable: experiment_one.build_production_controller "
            "must bind real Builder/Solver transports and official evaluator adapters"
        )
    return factory(context)


def _memory_gib() -> float | None:
    if hasattr(os, "sysconf"):
        try:
            pages = int(os.sysconf("SC_PHYS_PAGES"))
            page_size = int(os.sysconf("SC_PAGE_SIZE"))
            return pages * page_size / (1024**3)
        except (OSError, ValueError, TypeError):
            return None
    return None


def _existing_ancestor(path: Path) -> Path:
    current = path.resolve()
    while not current.exists() and current != current.parent:
        current = current.parent
    return current


def _git_head(repository: Path) -> str | None:
    if not repository.is_dir():
        return None
    completed = subprocess.run(
        ["git", "-C", str(repository), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
        shell=False,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip()


def inspect_host(root: Path, manifest: FrozenManifest) -> dict[str, object]:
    resources = manifest.resources
    cpu = os.cpu_count() or 0
    memory = _memory_gib()
    disk = shutil.disk_usage(_existing_ancestor(root)).free / (1024**3)
    repository = Path(manifest.official.source_repository)
    head = _git_head(repository)
    checks = {
        "operating_system": platform.system().lower() == resources.operating_system,
        "cpu": cpu >= resources.minimum_cpu_count,
        "memory": memory is not None and memory >= resources.minimum_memory_gib,
        "disk": disk >= resources.minimum_disk_gib,
        "source_repository": head == manifest.official.source_revision,
        "api_key_present": bool(os.environ.get("LLM_API_KEY")),
        "base_url_present": bool(os.environ.get("LLM_BASE_URL")),
        "model": os.environ.get("LLM_MODEL") == MODEL,
        "reasoning_effort": os.environ.get("LLM_REASONING_EFFORT") == REASONING_EFFORT,
        "image_digest_present": bool(
            os.environ.get(f"MOSS_{manifest.suite.upper()}_IMAGE_DIGEST")
        ),
    }
    return {
        "ready": all(checks.values()),
        "checks": checks,
        "observed": {
            "cpu_count": cpu,
            "memory_gib": round(memory, 3) if memory is not None else None,
            "free_disk_gib": round(disk, 3),
            "source_head": head,
        },
    }


def require_execution_environment(manifest: FrozenManifest) -> None:
    required = ("LLM_API_KEY", "LLM_BASE_URL", "LLM_MODEL", "LLM_REASONING_EFFORT")
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise ValueError(f"execution environment is missing: {', '.join(missing)}")
    if os.environ["LLM_MODEL"] != MODEL:
        raise ValueError(f"LLM_MODEL must be {MODEL}")
    if os.environ["LLM_REASONING_EFFORT"] != REASONING_EFFORT:
        raise ValueError(f"LLM_REASONING_EFFORT must be {REASONING_EFFORT}")
    base_url = os.environ["LLM_BASE_URL"]
    if not base_url.startswith("https://"):
        raise ValueError("LLM_BASE_URL must use HTTPS")
    family = os.environ.get("LLM_API_FAMILY", API_FAMILY)
    if family != API_FAMILY:
        raise ValueError("LLM_API_FAMILY must be responses")
    image_name = f"MOSS_{manifest.suite.upper()}_IMAGE_DIGEST"
    image_digest = os.environ.get(image_name)
    if not image_digest:
        raise ValueError(f"execution environment is missing: {image_name}")
    if not image_digest.startswith("sha256:") or len(image_digest) != 71:
        raise ValueError(f"{image_name} must be an immutable sha256 digest")


def _layout(context: ExecutionContext, position: str = "A") -> dict[str, str]:
    return {
        "artifact_root": str(context.artifact_root),
        "canary_root": str(context.canary_suite_root / position),
        "formal_seed_root": str(context.formal_seed_root),
        "lineage_root": str(context.lineage_root(position)),
        "frozen_root": str(context.frozen_root(position)),
        "cross_root_example": str(context.cross_root("A", "B")),
        "h0_baseline_root": str(context.baseline_root(position)),
    }


def _jsonable(value: object) -> Any:
    if hasattr(value, "to_dict") and callable(value.to_dict):
        return _jsonable(value.to_dict())
    if is_dataclass(value) and not isinstance(value, type):
        return _jsonable(asdict(value))
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError(f"controller returned non-JSON result: {type(value).__name__}")


def _status_path(context: ExecutionContext, command: str, position: str | None) -> Path:
    if command == "canary":
        base = context.canary_suite_root / "status"
    else:
        base = context.formal_seed_root / "status"
    suffix = position or "all"
    return base / f"{command}-{suffix}.json"


def _write_status(path: Path, payload: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = (_canonical_json(payload) + "\n").encode("utf-8")
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    with temporary.open("xb") as handle:
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
    temporary.replace(path)


def _base_report(
    *, command: str, context: ExecutionContext, position: str | None, executed: bool
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "experiment_id": context.manifest.experiment_id,
        "command": command,
        "suite": context.manifest.suite,
        "seed_id": context.seed_id,
        "position": position,
        "manifest_sha256": context.manifest.sha256,
        "executed": executed,
        "model": {
            "builder": MODEL,
            "solver": MODEL,
            "reasoning_effort": REASONING_EFFORT,
            "api_family": API_FAMILY,
        },
        "rounds": ROUNDS,
        "builder_memory": {
            "arm": context.memory_arm,
            **context.builder_memory_config.receipt_payload(),
        },
        "layout": _layout(context, position or "A"),
    }


def _emit(payload: Mapping[str, object]) -> None:
    print(_canonical_json(payload))


def _read_report(context: ExecutionContext) -> dict[str, object]:
    status_root = context.formal_seed_root / "status"
    records: list[object] = []
    if status_root.is_dir():
        for path in sorted(status_root.glob("*.json")):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                raise ValueError(f"status record failed integrity parsing: {path.name}") from exc
            records.append(_jsonable(value))
    report = _base_report(
        command="report", context=context, position=None, executed=False
    )
    report.update(status="reported", records=records)
    return report


def _dispatch_execute(
    command: str,
    context: ExecutionContext,
    position: str | None,
) -> dict[str, object]:
    require_execution_environment(context.manifest)
    controller = create_production_controller(context)
    if command == "canary":
        assert position is not None
        result = controller.run_canary(position)
    elif command == "evolve":
        assert position is not None
        result = controller.evolve(position)
    elif command == "freeze":
        assert position is not None
        result = controller.freeze(position)
    elif command == "cross-test":
        result = controller.cross_test()
    elif command == "resume":
        result = controller.resume(position)
    else:  # pragma: no cover - parser owns the command set
        raise ValueError(f"unsupported execute command: {command}")
    report = _base_report(
        command=command, context=context, position=position, executed=True
    )
    result_payload = _jsonable(result)
    if not isinstance(result_payload, Mapping):
        raise TypeError("controller result must be a JSON object")
    report.update(status="completed", result=dict(result_payload))
    # Promote compact progress keys without interpreting or inventing any score.
    for key in (
        "rounds_completed",
        "valid_cells",
        "receipt_sha256",
        "freeze_receipt_sha256",
        "resumed",
    ):
        if key in result_payload:
            report[key] = result_payload[key]
    _write_status(_status_path(context, command, position), report)
    return report


def _add_common_arguments(
    parser: argparse.ArgumentParser,
    *, position: bool = False,
    position_optional: bool = False,
    execute: bool = False,
) -> None:
    parser.add_argument("--suite", choices=tuple(DEFAULT_MANIFESTS), required=True)
    parser.add_argument(
        "--harness-version",
        choices=("v1", "v2"),
        default="v1",
        help="Task Harness artifact schema; v1 is the replay-compatible default",
    )
    parser.add_argument("--root", type=Path, required=True, help="Experiment artifact root")
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Frozen manifest override; its suite and immutable contract are revalidated",
    )
    parser.add_argument("--seed", choices=SEEDS, default="S1")
    if position:
        parser.add_argument(
            "--position", choices=POSITIONS, required=not position_optional
        )
    if execute:
        parser.add_argument(
            "--execute",
            action="store_true",
            help="Authorize model/evaluator calls and artifact writes",
        )
    parser.add_argument(
        "--builder-memory-mode",
        choices=("instance_only", "cross_task_online"),
        default="instance_only",
    )
    parser.add_argument(
        "--memory-arm",
        choices=("B-Frozen", "B-online"),
        default="B-Frozen",
        help="Experiment identity; cross-task memory is restricted to B-online position B",
    )
    parser.add_argument("--cross-task-memory-root", type=Path)
    parser.add_argument("--source-order", type=int)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the frozen EdgeBench/ALE-Bench Moss specialization experiment"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    preflight = subparsers.add_parser("preflight", help="Read-only contract/host check")
    _add_common_arguments(preflight)

    canary = subparsers.add_parser("canary", help="Plan or run an official evaluator canary")
    _add_common_arguments(canary, position=True, execute=True)

    evolve = subparsers.add_parser("evolve", help="Plan or run one isolated 8-round lineage")
    _add_common_arguments(evolve, position=True, execute=True)

    freeze = subparsers.add_parser("freeze", help="Plan or freeze the best scored Harness")
    _add_common_arguments(freeze, position=True, execute=True)

    cross = subparsers.add_parser(
        "cross-test", help="Plan or run the frozen no-Builder 3x3 matrix"
    )
    _add_common_arguments(cross, execute=True)

    report = subparsers.add_parser("report", help="Read-only status aggregation")
    _add_common_arguments(report)

    resume = subparsers.add_parser(
        "resume", help="Plan or resume append-only formal execution"
    )
    _add_common_arguments(resume, position=True, position_optional=True, execute=True)
    return parser


def _load_context(args: argparse.Namespace) -> ExecutionContext:
    requested_harness_version = 1 if args.harness_version == "v1" else 2
    manifest_path = (
        args.manifest.resolve()
        if args.manifest is not None
        else (DEFAULT_MANIFESTS if requested_harness_version == 1 else V2_MANIFESTS)[args.suite]
    )
    manifest = load_frozen_manifest(
        manifest_path,
        expected_harness_version=requested_harness_version,
    )
    if manifest.suite != args.suite:
        raise ValueError("--suite does not match the frozen manifest")
    if args.seed not in manifest.seeds:
        raise ValueError("seed is outside the frozen S1/S2/S3 contract")
    mode = getattr(args, "builder_memory_mode", "instance_only")
    memory_arm = getattr(args, "memory_arm", "B-Frozen")
    position = getattr(args, "position", None)
    memory_root = getattr(args, "cross_task_memory_root", None)
    source_order = getattr(args, "source_order", None)
    if mode == "instance_only":
        if memory_root is not None or source_order is not None:
            raise ValueError("instance_only Builder memory cannot use cross-task-memory-root or source-order")
        if memory_arm != "B-Frozen":
            raise ValueError("B-online memory arm requires cross_task_online Builder memory")
        builder_memory_config = BuilderMemoryConfig()
    else:
        if memory_root is None:
            raise ValueError("cross-task-memory-root is required for cross_task_online")
        if source_order is None:
            raise ValueError("source-order is required for cross_task_online")
        if source_order < 0:
            raise ValueError("source-order must be non-negative")
        if memory_arm != "B-online":
            raise ValueError("cross_task_online Builder memory requires explicit B-online arm")
        if position != "B":
            raise ValueError("cross_task_online Builder memory is restricted to position B")
        snapshot = CrossTaskMemoryStore.open_existing(memory_root).snapshot(
            before_order=source_order
        )
        builder_memory_config = BuilderMemoryConfig.from_snapshot(snapshot)
    return ExecutionContext(
        manifest=manifest,
        artifact_root=args.root.resolve(),
        seed_id=args.seed,
        builder_memory_config=builder_memory_config,
        memory_arm=memory_arm,
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    context = _load_context(args)
    command = str(args.command)
    position = getattr(args, "position", None)

    if command == "preflight":
        host = inspect_host(context.artifact_root, context.manifest)
        report = _base_report(
            command=command, context=context, position=None, executed=False
        )
        report.update(
            status="ready" if bool(host.get("ready")) else "blocked",
            host=host,
        )
        _emit(report)
        return 0

    if command == "report":
        _emit(_read_report(context))
        return 0

    if not bool(args.execute):
        report = _base_report(
            command=command, context=context, position=position, executed=False
        )
        report.update(status="planned", requires_execute=True)
        _emit(report)
        return 0

    _emit(_dispatch_execute(command, context, position))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
