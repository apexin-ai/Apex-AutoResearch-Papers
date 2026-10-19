from __future__ import annotations

import pytest

from optimization_lab.codex_generator import CodexExecGenerator
from optimization_lab.harness_builder.dual_config import (
    DualHarnessModelConfig,
    create_dual_harness_generators,
    create_dual_harness_runtime,
)
from optimization_lab.harness_builder.dual_harness import HarnessWorkspace
from optimization_lab.harness_builder.experiment_one_audit import (
    assemble_experiment_one,
)
from optimization_lab.openai_generator import OpenAIResponsesGenerator
from test_dual_harness import artifact


def test_default_uses_same_frozen_model_for_both_layers() -> None:
    config = DualHarnessModelConfig.from_env({})
    assert config.builder_model == config.solver_model
    assert config.builder_model == "gpt-5.6-sol"
    assert config.reasoning_effort == "high"


def test_builder_and_solver_models_can_be_separated() -> None:
    config = DualHarnessModelConfig.from_env(
        {
            "MOSS_BUILDER_MODEL": "builder-x",
            "MOSS_SOLVER_MODEL": "solver-y",
            "MOSS_BUILDER_TRANSPORT": "openai_responses",
            "MOSS_SOLVER_TRANSPORT": "codex_cli",
        }
    )
    assert config.builder_model == "builder-x"
    assert config.solver_model == "solver-y"
    assert config.builder_transport == "openai_responses"
    assert config.solver_transport == "codex_cli"


def test_blank_model_names_are_rejected() -> None:
    with pytest.raises(ValueError, match="model"):
        DualHarnessModelConfig.from_env({"MOSS_BUILDER_MODEL": " "})


def test_unknown_transport_and_unimplemented_native_tools_are_rejected() -> None:
    with pytest.raises(ValueError, match="transport"):
        DualHarnessModelConfig.from_env({"MOSS_BUILDER_TRANSPORT": "unknown"})
    with pytest.raises(ValueError, match="tool protocol"):
        DualHarnessModelConfig.from_env({"MOSS_TOOL_PROTOCOL": "native_tool_calling"})


def test_dual_harness_exports_are_available_from_package() -> None:
    import optimization_lab.harness_builder as harness_builder

    assert harness_builder.BuilderHarness.__name__ == "BuilderHarness"
    assert harness_builder.DualHarnessRuntime.__name__ == "DualHarnessRuntime"
    assert harness_builder.TaskHarnessArtifact.__name__ == "TaskHarnessArtifact"
    assert harness_builder.EvaluationResult.__name__ == "EvaluationResult"
    assert harness_builder.IncompleteRoundError.__name__ == "IncompleteRoundError"
    assert harness_builder.PublicEvaluation.__name__ == "PublicEvaluation"
    assert callable(harness_builder.create_dual_harness_runtime)


def test_transport_config_constructs_separate_builder_and_solver_generators(tmp_path) -> None:
    config = DualHarnessModelConfig.from_env(
        {
            "MOSS_BUILDER_TRANSPORT": "openai_responses",
            "MOSS_SOLVER_TRANSPORT": "codex_cli",
        }
    )
    client = object()

    generators = create_dual_harness_generators(
        config,
        operation_root=tmp_path,
        openai_client=client,
    )

    assert isinstance(generators.builder, OpenAIResponsesGenerator)
    assert generators.builder.client is client
    assert generators.builder.reasoning_effort == "high"
    assert isinstance(generators.solver, CodexExecGenerator)
    assert generators.solver.work_root == (tmp_path / "solver").resolve()
    assert generators.solver.output_mode == "plain_text"
    assert generators.solver.reasoning_effort == "high"

    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())
    runtime = create_dual_harness_runtime(
        config,
        workspace=workspace,
        operation_root=tmp_path / "runtime-operations",
        openai_client=client,
    )
    assert isinstance(runtime.builder.generator, OpenAIResponsesGenerator)
    assert isinstance(runtime.task_runtime.generator, CodexExecGenerator)


def test_experiment_one_assembly_accepts_frozen_openai_transports(tmp_path) -> None:
    config = DualHarnessModelConfig.from_env(
        {
            "MOSS_BUILDER_TRANSPORT": "openai_responses",
            "MOSS_SOLVER_TRANSPORT": "openai_responses",
        }
    )
    generators = create_dual_harness_generators(
        config,
        operation_root=tmp_path,
        openai_client=object(),
    )
    workspace = HarnessWorkspace(tmp_path / "workspace")
    workspace.commit(artifact())

    assembly = assemble_experiment_one(
        workspace=workspace,
        builder_generator=generators.builder,
        solver_generator=generators.solver,
        builder_model=config.builder_model,
        audit_directory=tmp_path / "audit",
        builder_operation_id_factory=lambda: "experiment-one.builder.v001",
        solver_operation_id_factory=lambda: "experiment-one.solver.v001",
        builder_reasoning_effort="high",
        solver_reasoning_effort="high",
    )

    assert assembly.builder.generator.generator is generators.builder
    assert assembly.solver_generator.generator is generators.solver
    assert (
        assembly.builder.generator._transport_config
        is generators.builder.request_config
    )
    assert (
        assembly.solver_generator._transport_config
        is generators.solver.request_config
    )


def test_openai_transports_use_frozen_streaming_limits(tmp_path) -> None:
    config = DualHarnessModelConfig.from_env(
        {
            "MOSS_BUILDER_TRANSPORT": "openai_responses",
            "MOSS_SOLVER_TRANSPORT": "openai_responses",
        }
    )
    generators = create_dual_harness_generators(
        config,
        operation_root=tmp_path,
        openai_client=object(),
    )

    assert generators.builder.request_config.stream is True
    assert generators.builder.request_config.max_attempts == 3
    assert generators.builder.request_config.max_output_tokens == 16_384
    assert generators.solver.request_config.stream is True
    assert generators.solver.request_config.max_attempts == 3
    assert generators.solver.request_config.max_output_tokens == 32_768


def test_openai_transports_have_separate_builder_solver_audit_roots(tmp_path) -> None:
    config = DualHarnessModelConfig.from_env(
        {
            "MOSS_BUILDER_TRANSPORT": "openai_responses",
            "MOSS_SOLVER_TRANSPORT": "openai_responses",
        }
    )
    generators = create_dual_harness_generators(
        config,
        operation_root=tmp_path / "operations",
        openai_client=object(),
    )

    assert generators.builder.audit_root == (tmp_path / "operations" / "builder").resolve()
    assert generators.solver.audit_root == (tmp_path / "operations" / "solver").resolve()
