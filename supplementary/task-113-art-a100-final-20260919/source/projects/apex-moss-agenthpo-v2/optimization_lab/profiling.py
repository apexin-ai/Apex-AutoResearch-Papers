from __future__ import annotations

import ast
import hashlib
import re
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any, Protocol

from optimization_lab.feedback import FeedbackCard
from optimization_lab.task_spec import TaskSpec


HARDWARE_COUNTER_METRICS = {
    "achieved_occupancy_pct",
    "dram_throughput_pct",
    "l2_hit_rate_pct",
    "warp_stall_summary",
}
OPTIONAL_METRICS = HARDWARE_COUNTER_METRICS | {
    "registers_per_thread",
    "register_spills",
    "shared_memory_bytes",
    "kernel_count",
    "launch_count",
    "num_warps",
    "num_stages",
    "theoretical_occupancy_pct",
}


class InvalidProfileSummary(ValueError):
    pass


@dataclass(frozen=True)
class ProfilerCapabilities:
    nsys: bool
    ncu: bool
    hardware_counters: bool
    ptxas: bool
    cuobjdump: bool
    detail: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ProfileSummary:
    task_id: str
    candidate_id: str
    candidate_sha256: str
    level: str
    status: str
    candidate_runtime_ms: float
    reference_runtime_ms: float
    speedup: float
    structural_signature: str
    structure: dict[str, Any] | None = None
    kernel_count: int | None = None
    launch_count: int | None = None
    registers_per_thread: int | None = None
    register_spills: int | None = None
    shared_memory_bytes: int | None = None
    num_warps: int | None = None
    num_stages: int | None = None
    theoretical_occupancy_pct: float | None = None
    achieved_occupancy_pct: float | None = None
    dram_throughput_pct: float | None = None
    l2_hit_rate_pct: float | None = None
    warp_stall_summary: str | None = None
    timeline_summary: tuple[str, ...] = ()
    compiler_summary: tuple[str, ...] = ()
    missing_metrics: tuple[str, ...] = ()
    gpu_seconds: float = 0.0

    def __post_init__(self) -> None:
        if self.level not in {"light", "full"}:
            raise InvalidProfileSummary("profile level must be light or full")
        if self.status not in {"complete", "partial", "unavailable"}:
            raise InvalidProfileSummary("profile status is invalid")
        if not re.fullmatch(r"[0-9a-f]{64}", self.candidate_sha256):
            raise InvalidProfileSummary("profile candidate hash is invalid")
        if min(
            self.candidate_runtime_ms,
            self.reference_runtime_ms,
            self.speedup,
        ) <= 0:
            raise InvalidProfileSummary("profile runtimes and score must be positive")
        if self.gpu_seconds < 0:
            raise InvalidProfileSummary("profile GPU accounting cannot be negative")
        unknown = set(self.missing_metrics) - OPTIONAL_METRICS
        if unknown:
            raise InvalidProfileSummary(f"unknown missing profile metrics: {sorted(unknown)}")
        for metric in self.missing_metrics:
            if getattr(self, metric) is not None:
                raise InvalidProfileSummary(
                    f"metric {metric} is unavailable but also has an observed value"
                )
        for text in (*self.timeline_summary, *self.compiler_summary):
            if _contains_absolute_path(text):
                raise InvalidProfileSummary("public profile summary contains an absolute path")

    def to_public_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["missing_metrics"] = list(self.missing_metrics)
        data["timeline_summary"] = list(self.timeline_summary)
        data["compiler_summary"] = list(self.compiler_summary)
        return data


class Profiler(Protocol):
    def capabilities(self) -> ProfilerCapabilities:
        """Return read-only profiler capability facts."""

    def estimated_gpu_seconds(self, task: TaskSpec, level: str) -> float:
        """Return a conservative reservation before a profile run."""

    def profile(
        self,
        *,
        task: TaskSpec,
        candidate_path: Path,
        candidate_id: str,
        feedback: FeedbackCard,
        level: str,
        private_log_dir: Path,
    ) -> ProfileSummary:
        """Profile one already-correct candidate and return only public evidence."""


class FakeProfiler:
    def __init__(self, template: ProfileSummary):
        self.template = template
        self.calls: list[dict[str, Any]] = []

    def capabilities(self) -> ProfilerCapabilities:
        return ProfilerCapabilities(
            nsys=True,
            ncu=False,
            hardware_counters=False,
            ptxas=True,
            cuobjdump=True,
            detail="fake",
        )

    def estimated_gpu_seconds(self, task: TaskSpec, level: str) -> float:
        return self.template.gpu_seconds

    def profile(
        self,
        *,
        task: TaskSpec,
        candidate_path: Path,
        candidate_id: str,
        feedback: FeedbackCard,
        level: str,
        private_log_dir: Path,
    ) -> ProfileSummary:
        if not feedback.correct or feedback.speedup_vs_eager is None:
            raise ValueError("profiler can run only after a correct scored candidate")
        private_log_dir.mkdir(parents=True, exist_ok=True)
        source = candidate_path.read_text(encoding="utf-8")
        structure = static_structure_signature(source)
        sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
        self.calls.append(
            {
                "task_id": task.task_id,
                "candidate_id": candidate_id,
                "level": level,
            }
        )
        return replace(
            self.template,
            task_id=task.task_id,
            candidate_id=candidate_id,
            candidate_sha256=sha,
            level=level,
            candidate_runtime_ms=float(feedback.candidate_runtime_ms),
            reference_runtime_ms=float(feedback.reference_runtime_ms),
            speedup=float(feedback.speedup_vs_eager),
            structural_signature=_signature_digest(structure),
            structure=structure,
        )


def static_structure_signature(source: str) -> dict[str, Any]:
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        raise InvalidProfileSummary("cannot profile a syntactically invalid candidate") from exc
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = _call_name(node.func)
            if name:
                calls.append(name)
    decorators = [
        _call_name(decorator.func) if isinstance(decorator, ast.Call) else _call_name(decorator)
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        for decorator in node.decorator_list
    ]
    integer_parameters: dict[str, list[int]] = {"num_warps": [], "num_stages": []}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        for keyword in node.keywords:
            if (
                keyword.arg in integer_parameters
                and isinstance(keyword.value, ast.Constant)
                and isinstance(keyword.value.value, int)
            ):
                integer_parameters[keyword.arg].append(keyword.value.value)
    triton_kernels = sum(
        decorator in {"triton.jit", "triton.autotune"} for decorator in decorators
    )
    return {
        "triton_kernel_count": triton_kernels,
        "triton_kernel_names": sorted(
            {
                node.name
                for node in ast.walk(tree)
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and any(
                    decorator in {"triton.jit", "triton.autotune"}
                    for decorator in (
                        _call_name(item.func)
                        if isinstance(item, ast.Call)
                        else _call_name(item)
                        for item in node.decorator_list
                    )
                )
            }
        ),
        "uses_autotune": "triton.autotune" in decorators,
        "num_warps_values": sorted(set(integer_parameters["num_warps"])),
        "num_stages_values": sorted(set(integer_parameters["num_stages"])),
        "torch_calls": sorted({name for name in calls if name.startswith("torch.")}),
        "tl_calls": sorted({name for name in calls if name.startswith("tl.")}),
        "function_count": sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree)),
    }


def _call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = _call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def _signature_digest(structure: dict[str, Any]) -> str:
    import json

    encoded = json.dumps(structure, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode()).hexdigest()[:20]


def _contains_absolute_path(text: str) -> bool:
    return bool(re.search(r"(?<![A-Za-z0-9])/(?:[^\s:|]+/)+[^\s:|]+", text))
