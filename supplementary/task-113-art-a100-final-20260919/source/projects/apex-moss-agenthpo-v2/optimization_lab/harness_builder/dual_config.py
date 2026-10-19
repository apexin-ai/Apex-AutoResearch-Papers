from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from optimization_lab.codex_generator import CodexExecGenerator
from optimization_lab.generation import CandidateGenerator
from optimization_lab.openai_generator import OpenAIResponsesGenerator

from .builder_harness import BuilderHarness
from .dual_harness import HarnessWorkspace, TaskHarnessRuntime
from .dual_runtime import DualHarnessRuntime


@dataclass(frozen=True)
class DualHarnessModelConfig:
    builder_model: str
    solver_model: str
    builder_transport: str = "codex_cli"
    solver_transport: str = "codex_cli"
    tool_protocol: str = "controller_json"
    reasoning_effort: str = "high"

    def __post_init__(self) -> None:
        if not self.builder_model.strip() or not self.solver_model.strip():
            raise ValueError("Builder and Solver model names are required")
        if self.builder_transport not in {"codex_cli", "openai_responses"}:
            raise ValueError("unsupported Builder model transport")
        if self.solver_transport not in {"codex_cli", "openai_responses"}:
            raise ValueError("unsupported Solver model transport")
        if self.tool_protocol != "controller_json":
            raise ValueError("unsupported model tool protocol")
        if self.reasoning_effort not in {
            "none",
            "minimal",
            "low",
            "medium",
            "high",
            "xhigh",
            "max",
            "ultra",
        }:
            raise ValueError("unsupported reasoning effort")

    @classmethod
    def from_env(cls, environment: Mapping[str, str]) -> "DualHarnessModelConfig":
        default = "gpt-5.6-sol"
        return cls(
            builder_model=environment.get("MOSS_BUILDER_MODEL", default),
            solver_model=environment.get("MOSS_SOLVER_MODEL", default),
            builder_transport=environment.get("MOSS_BUILDER_TRANSPORT", "codex_cli"),
            solver_transport=environment.get("MOSS_SOLVER_TRANSPORT", "codex_cli"),
            tool_protocol=environment.get("MOSS_TOOL_PROTOCOL", "controller_json"),
            reasoning_effort=environment.get("MOSS_REASONING_EFFORT", "high"),
        )


@dataclass(frozen=True)
class DualHarnessGenerators:
    builder: CandidateGenerator
    solver: CandidateGenerator


def create_dual_harness_generators(
    config: DualHarnessModelConfig,
    *,
    operation_root: Path,
    openai_client: object | None = None,
) -> DualHarnessGenerators:
    operation_root = operation_root.resolve()

    def create(transport: str, layer: str) -> CandidateGenerator:
        if transport == "codex_cli":
            return CodexExecGenerator(
                work_root=operation_root / layer,
                reasoning_effort=config.reasoning_effort,
                output_mode="plain_text",
            )
        return OpenAIResponsesGenerator(
            client=openai_client,
            max_output_tokens=16_384 if layer == "builder" else 32_768,
            reasoning_effort=config.reasoning_effort,
            max_attempts=3,
            stream=True,
            audit_root=operation_root / layer,
        )

    return DualHarnessGenerators(
        builder=create(config.builder_transport, "builder"),
        solver=create(config.solver_transport, "solver"),
    )


def create_dual_harness_runtime(
    config: DualHarnessModelConfig,
    *,
    workspace: HarnessWorkspace,
    operation_root: Path,
    openai_client: object | None = None,
) -> DualHarnessRuntime:
    generators = create_dual_harness_generators(
        config,
        operation_root=operation_root,
        openai_client=openai_client,
    )
    return DualHarnessRuntime(
        workspace=workspace,
        task_runtime=TaskHarnessRuntime(generator=generators.solver),
        builder=BuilderHarness(
            workspace=workspace,
            generator=generators.builder,
            model=config.builder_model,
        ),
        solver_model=config.solver_model,
    )
