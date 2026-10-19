"""Cross-instance Harness Builder experiment contracts and trusted runtime.

Heavy benchmark adapters are loaded lazily so portable Harness contracts can be
imported without initializing Linux-only evaluator dependencies.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any


_EXPORTS = {
    "AgentAction": (".agent_runtime", "AgentAction"),
    "AgentProtocolError": (".agent_runtime", "AgentProtocolError"),
    "AgentRun": (".agent_runtime", "AgentRun"),
    "AgentRuntime": (".agent_runtime", "AgentRuntime"),
    "AgentTurn": (".agent_runtime", "AgentTurn"),
    "BuilderHarness": (".builder_harness", "BuilderHarness"),
    "BuilderHarnessSpec": (".builder_harness", "BuilderHarnessSpec"),
    "BuilderArchive": (".builder_evolution", "BuilderArchive"),
    "BuilderArtifact": (".builder_evolution", "BuilderArtifact"),
    "BuilderBoundaryError": (".builder_evolution", "BuilderBoundaryError"),
    "BuilderPublicState": (".builder_evolution", "BuilderPublicState"),
    "BuilderScaffoldCompiler": (".builder_evolution", "BuilderScaffoldCompiler"),
    "CompiledBuilderScaffold": (".builder_evolution", "CompiledBuilderScaffold"),
    "BuilderImpK": (".builder_evolution", "BuilderImpK"),
    "BuilderEvolutionResult": (".builder_evolution", "BuilderEvolutionResult"),
    "BuilderSelfModificationProposal": (
        ".builder_evolution",
        "BuilderSelfModificationProposal",
    ),
    "ImmutableBuilderController": (
        ".builder_evolution",
        "ImmutableBuilderController",
    ),
    "MetaPolicy": (".builder_evolution", "MetaPolicy"),
    "SelfEvolvingBuilder": (".builder_evolution", "SelfEvolvingBuilder"),
    "TaskHarnessPolicy": (".builder_evolution", "TaskHarnessPolicy"),
    "ChampionArchivePolicy": (".champion_archive", "ChampionArchivePolicy"),
    "GateDecision": (".champion_archive", "GateDecision"),
    "PortfolioEvolutionPolicy": (".champion_archive", "PortfolioEvolutionPolicy"),
    "BuilderVariant": (".schema", "BuilderVariant"),
    "HarnessContext": (".operators", "HarnessContext"),
    "HarnessDecision": (".schema", "HarnessDecision"),
    "HarnessRuntime": (".runtime", "HarnessRuntime"),
    "DualHarnessRuntime": (".dual_runtime", "DualHarnessRuntime"),
    "EvaluationResult": (".dual_runtime", "EvaluationResult"),
    "IncompleteRoundError": (".dual_runtime", "IncompleteRoundError"),
    "CallbackEvaluatorRunner": (".evolution", "CallbackEvaluatorRunner"),
    "HarnessRoundAssessment": (".evolution", "HarnessRoundAssessment"),
    "summarize_harness_change": (".evolution", "summarize_harness_change"),
    "TaskHarnessEvolutionCampaign": (".evolution", "TaskHarnessEvolutionCampaign"),
    "TaskHarnessEvolutionResult": (".evolution", "TaskHarnessEvolutionResult"),
    "PublicEvaluation": (".dual_runtime", "PublicEvaluation"),
    "DualHarnessModelConfig": (".dual_config", "DualHarnessModelConfig"),
    "create_dual_harness_generators": (".dual_config", "create_dual_harness_generators"),
    "create_dual_harness_runtime": (".dual_config", "create_dual_harness_runtime"),
    "HarnessWorkspace": (".dual_harness", "HarnessWorkspace"),
    "TaskHarnessArtifact": (".dual_harness", "TaskHarnessArtifact"),
    "TaskHarnessRuntime": (".dual_harness", "TaskHarnessRuntime"),
    "AgentHPOOutcome": (".adapters.agenthpo_v2", "AgentHPOOutcome"),
    "AgentHPOV2Trace": (".adapters.agenthpo_v2", "AgentHPOV2Trace"),
    "run_agenthpo_v2_task": (".adapters.agenthpo_v2", "run_agenthpo_v2_task"),
    "HistoricalImportContract": (".historical_import", "HistoricalImportContract"),
    "HistoricalTrajectoryImporter": (".historical_import", "HistoricalTrajectoryImporter"),
    "prepare_historical_trajectories": (".historical_import", "prepare_historical_trajectories"),
    "ExperienceBankSnapshot": (".learning", "ExperienceBankSnapshot"),
    "FormalCampaignContract": (".formal", "FormalCampaignContract"),
    "FormalCampaignResult": (".formal", "FormalCampaignResult"),
    "FormalCampaignRunner": (".formal", "FormalCampaignRunner"),
    "FormalProviderFactory": (".formal", "FormalProviderFactory"),
    "FormalSuiteProvider": (".formal", "FormalSuiteProvider"),
    "FormalTaskBinding": (".formal", "FormalTaskBinding"),
    "FormalProviderCompositionBlocked": (".formal_providers", "FormalProviderCompositionBlocked"),
    "FormalProviderCompositionConfig": (".formal_providers", "FormalProviderCompositionConfig"),
    "FormalProviderPreflight": (".formal_providers", "FormalProviderPreflight"),
    "StagingBoundFormalProviderFactory": (".formal_providers", "StagingBoundFormalProviderFactory"),
    "compose_formal_provider_factory": (".formal_providers", "compose_formal_provider_factory"),
    "compose_verified_suite_provider": (".formal_providers", "compose_verified_suite_provider"),
    "preflight_formal_providers": (".formal_providers", "preflight_formal_providers"),
    "IsolatedModelGateway": (".model_gateway", "IsolatedModelGateway"),
    "MetaTrainCampaignRunner": (".meta_train", "MetaTrainCampaignRunner"),
    "MetaTrainContract": (".meta_train", "MetaTrainContract"),
    "MetaTrainFreezer": (".meta_train", "MetaTrainFreezer"),
    "MetaTrainTask": (".meta_train", "MetaTrainTask"),
    "bind_kernelbench_meta_tasks": (".meta_train", "bind_kernelbench_meta_tasks"),
    "PilotManifest": (".schema", "PilotManifest"),
    "PublicAttempt": (".operators", "PublicAttempt"),
    "RuleRegistry": (".schema", "RuleRegistry"),
    "TrustedOperatorRegistry": (".operators", "TrustedOperatorRegistry"),
    "BoundTool": (".tool_registry", "BoundTool"),
    "ToolBudgetError": (".tool_registry", "ToolBudgetError"),
    "ToolCallReceipt": (".tool_registry", "ToolCallReceipt"),
    "ToolCallResult": (".tool_registry", "ToolCallResult"),
    "ToolContext": (".tool_registry", "ToolContext"),
    "ToolOutputLimitError": (".tool_registry", "ToolOutputLimitError"),
    "ToolPolicy": (".tool_registry", "ToolPolicy"),
    "ToolRegistry": (".tool_registry", "ToolRegistry"),
    "ToolReplayError": (".tool_registry", "ToolReplayError"),
    "ToolSession": (".tool_registry", "ToolSession"),
    "ToolTimeoutError": (".tool_registry", "ToolTimeoutError"),
    "ALE_CPP_SYNTAX_CHECK_TOOL_ID": (
        ".experiment_one_tools",
        "ALE_CPP_SYNTAX_CHECK_TOOL_ID",
    ),
    "ALE_PUBLIC_TOOL_IDS": (".experiment_one_tools", "ALE_PUBLIC_TOOL_IDS"),
    "CONTRACT_CHECK_TOOL_ID": (".experiment_one_tools", "CONTRACT_CHECK_TOOL_ID"),
    "EDGE_PUBLIC_TOOL_IDS": (".experiment_one_tools", "EDGE_PUBLIC_TOOL_IDS"),
    "EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID": (
        ".experiment_one_tools",
        "EDGE_PYTHON_SYNTAX_CHECK_TOOL_ID",
    ),
    "ExperimentOneToolPack": (".experiment_one_tools", "ExperimentOneToolPack"),
    "FORBIDDEN_EVALUATOR_TOOL_IDS": (
        ".experiment_one_tools",
        "FORBIDDEN_EVALUATOR_TOOL_IDS",
    ),
    "allowed_experiment_one_tool_ids": (
        ".experiment_one_tools",
        "allowed_experiment_one_tool_ids",
    ),
    "build_experiment_one_tool_pack": (
        ".experiment_one_tools",
        "build_experiment_one_tool_pack",
    ),
    "WorkflowDefinition": (".workflows", "WorkflowDefinition"),
    "WorkflowRegistry": (".workflows", "WorkflowRegistry"),
    "THREE_ARMS": (".three_arm", "THREE_ARMS"),
    "ThreeArmCampaignContract": (".three_arm", "ThreeArmCampaignContract"),
    "ThreeArmCampaignResult": (".three_arm", "ThreeArmCampaignResult"),
    "ThreeArmCampaignRunner": (".three_arm", "ThreeArmCampaignRunner"),
    "SimpleTESScalingContract": (".simpletes_scaling", "SimpleTESScalingContract"),
    "SimpleTESTaskLineageContract": (
        ".simpletes_scaling",
        "SimpleTESTaskLineageContract",
    ),
    "SimpleTESHarnessEvolutionCampaign": (
        ".simpletes_scaling",
        "SimpleTESHarnessEvolutionCampaign",
    ),
    "SimpleTESLineageAdapter": (".simpletes_scaling", "SimpleTESLineageAdapter"),
    "rich_simpletes_harness": (".simpletes_scaling", "rich_simpletes_harness"),
    "SimpleTESHarnessEvolutionResult": (
        ".simpletes_scaling",
        "SimpleTESHarnessEvolutionResult",
    ),
}

__all__ = sorted(_EXPORTS)


def __getattr__(name: str) -> Any:
    target = _EXPORTS.get(name)
    if target is None:
        raise AttributeError(name)
    module_name, attribute = target
    value = getattr(import_module(module_name, __name__), attribute)
    globals()[name] = value
    return value
