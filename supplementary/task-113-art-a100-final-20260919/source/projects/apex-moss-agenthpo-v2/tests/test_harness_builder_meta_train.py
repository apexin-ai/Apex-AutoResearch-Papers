from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from optimization_lab.generation import GenerationResult
from optimization_lab.harness_builder.evaluation import NormalizedEvaluation
from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.meta_train import (
    MetaTrainCampaignRunner,
    MetaTrainContract,
    MetaTrainFreezer,
    MetaTrainTask,
    MetaTrainTrajectory,
)
from optimization_lab.harness_builder.model_gateway import IsolatedModelGateway
from optimization_lab.harness_builder.operators import HarnessContext, TrustedOperatorRegistry
from optimization_lab.harness_builder.schema import BuilderVariant
from optimization_lab.harness_builder.solutions import KernelBenchSolutionCodec


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "optimization_lab/harness_builder/data"


def _variant(
    variant_id: str,
    *,
    experience_sources: tuple[str, ...] = (),
    excluded_task_ids: tuple[str, ...] = (),
) -> BuilderVariant:
    return BuilderVariant(
        variant_id=variant_id,
        description="fixture",
        freeze_after_initial=False,
        continual_update=variant_id == "B-online",
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=experience_sources,
        excluded_task_ids=excluded_task_ids,
    )


def _decision(round_index: int) -> str:
    payload = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["task_analyst", "performance_analyst", "generator", "verifier"],
        "memory_views": ["current", "best", "failures"],
        "tools": ["task_semantics", "score_history", "static_structure"],
        "parent_strategy": "incumbent" if round_index % 2 else "stable_best",
        "workflow": ["analyze", "select_parent", "inspect", "generate", "verify_contract"],
        "scheduler_mode": "single_candidate" if round_index % 2 else "explore_then_exploit",
        "recovery_mode": "preserve_failure",
        "kernel_directive": f"Generate candidate {round_index}.",
    }
    return json.dumps(payload)


class ScriptedTransport:
    def __init__(self, output_mode: str) -> None:
        self.output_mode = output_mode

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        del model
        if prompt.startswith("Distill the fully sealed KernelBench meta-train trajectory"):
            marker = '"source_instance_id": "'
            source = prompt.split(marker, 1)[1].split('"', 1)[0]
            event_marker = '"provenance_event_ids": ['
            event_tail = prompt.split(event_marker, 1)[1]
            event_id = event_tail.split('"', 2)[1]
            digest = hashlib.sha256(source.encode()).hexdigest()[:16]
            response = {
                "records": [
                    {
                        "record_id": f"meta-{digest}",
                        "source_instance_id": source,
                        "builder_version": "hb-gen1-h0",
                        "instance_descriptor": ["kernelbench", "tensor-program"],
                        "initial_harness_structure": [
                            "task_analyst",
                            "performance_analyst",
                            "generator",
                            "verifier",
                        ],
                        "evolution_rule": "discipline",
                        "trigger_evidence": ["sealed public score trajectory"],
                        "outcome_delta": 0.03,
                        "correctness": True,
                        "resource_cost": {"model_calls": 16.0, "evaluator_seconds": 8.0},
                        "counterexamples": ["single-instance evidence only"],
                        "scope": "single_instance_observation",
                        "provenance_event_ids": [event_id],
                        "sealed": True,
                    }
                ]
            }
            return GenerationResult(raw_response=json.dumps(response), provider="fake")
        if self.output_mode == "python_candidate":
            return GenerationResult(
                raw_response="""```python
import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
```
""",
                provider="fake",
            )
        marker = '"round_index": '
        round_index = int(prompt.split(marker, 1)[1].split(",", 1)[0])
        return GenerationResult(raw_response=_decision(round_index), provider="fake")


class FakeKernelBenchBackend:
    reservation = ResourceVector(
        evaluator_transactions=1,
        gpu_exclusive_seconds=600.0,
    )

    def __init__(self) -> None:
        self.calls = 0

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        assert artifact_path.read_text(encoding="utf-8").startswith("import torch")
        private_dir.mkdir(parents=True, exist_ok=True)
        self.calls += 1
        return NormalizedEvaluation(
            status="valid",
            correct=True,
            score=1.0 + self.calls / 100.0,
            public_feedback={"status": "valid", "round": self.calls},
            actual_usage=ResourceVector(
                evaluator_transactions=1,
                gpu_exclusive_seconds=1.0,
            ),
            evidence_sha256=hashlib.sha256(str(self.calls).encode()).hexdigest(),
        )


def _historical(contract: MetaTrainContract) -> tuple[MetaTrainTrajectory, ...]:
    values = []
    for index, source in enumerate(contract.historical_sources):
        values.append(
            MetaTrainTrajectory.create(
                source_instance_id=source.instance_id,
                source_sha256=source.source_sha256,
                instance_descriptor=("kernelbench", f"level-{source.level}"),
                initial_harness_structure=("task_analyst", "generator", "verifier"),
                provenance_event_ids=(f"historical-sealed-{index}",),
                round_summaries=(
                    {
                        "version": "historical",
                        "rule_id": "discipline",
                        "correct": True,
                        "score": 1.1,
                        "outcome": "valid",
                    },
                ),
                sealed=True,
            )
        )
    return tuple(values)


def _fixture_contract() -> MetaTrainContract:
    contract = MetaTrainContract.from_json(DATA / "experience_bank_v1.json")
    sources = tuple(
        source
        if source in contract.historical_sources
        else replace(
            source,
            source_sha256=hashlib.sha256(f"# {source.task_id}\n".encode()).hexdigest(),
        )
        for source in contract.sources
    )
    return replace(contract, sources=sources)


def _formal_heldout_ids() -> tuple[str, ...]:
    return tuple(f"kernelbenchx:heldout-{index:02d}" for index in range(24))


def test_meta_train_contract_freezes_six_new_and_two_historical_sources() -> None:
    contract = MetaTrainContract.from_json(DATA / "experience_bank_v1.json")

    assert len(contract.sources) == 8
    assert len(contract.historical_sources) == 2
    assert len(contract.new_sources) == 6
    assert contract.new_sources[0].task_id == "level1/21_Sigmoid.py"
    assert contract.new_sources[-1].problem_id == 67
    assert all(source.instance_id.startswith("kernelbench:") for source in contract.sources)


def test_kernelbench_codec_requires_one_modelnew_candidate() -> None:
    artifact = KernelBenchSolutionCodec().parse(
        """```python
import torch
import torch.nn as nn

class ModelNew(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.sigmoid(x)
```
"""
    )
    assert artifact.artifact_kind == "kernelbench_modelnew_python"
    assert artifact.text.startswith("import torch\n")

    with pytest.raises(ValueError, match="ModelNew"):
        KernelBenchSolutionCodec().parse("```python\nclass Other: pass\n```\n")


def test_excluded_formal_task_cannot_enter_builder_cross_instance_memory() -> None:
    heldout = "kernelbenchx:Quantization/matmul_w8a8.py"
    context = HarnessContext(
        instance_id="kernelbenchx:Quantization/conv2d_w8a8.py",
        suite="kernelbenchx",
        round_index=1,
        task_card="Optimize the public task.",
        reference_artifact_id="reference",
        reference_artifact="reference candidate",
        cross_instance_records=(
            {
                "record_id": "record-1",
                "source_instance_id": heldout,
                "scope": "single_instance_observation",
                "summary": "sealed public trajectory",
            },
        ),
    )
    decision = json.loads(_decision(1))
    decision["memory_views"].append("cross_instance_records")
    from optimization_lab.harness_builder.schema import HarnessDecision

    with pytest.raises(ValueError, match="excluded task"):
        TrustedOperatorRegistry(rule_registry_sha256="a" * 64).compile(
            HarnessDecision.from_dict(decision),
            variant=_variant(
                "B*",
                experience_sources=("moss-kernelbench-meta-train-v1",),
                excluded_task_ids=(heldout,),
            ),
            context=context,
        )


def test_six_task_fake_meta_train_then_eight_source_distillation_is_recoverable(
    tmp_path: Path,
) -> None:
    contract = _fixture_contract()
    cell_caps = {
        source.cell_id: ResourceCaps(
            model_calls=16,
            evaluator_transactions=8,
            gpu_exclusive_seconds=4800.0,
        )
        for source in contract.new_sources
    }
    cell_caps["meta:distillation"] = ResourceCaps(model_calls=8)
    global_caps = ResourceCaps(
        model_calls=104,
        evaluator_transactions=48,
        gpu_exclusive_seconds=28800.0,
    )
    journal = OperationJournal(
        tmp_path / "operations",
        anchor_path=tmp_path / "independent-head.json",
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=global_caps,
        cell_caps=cell_caps,
    )
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model-artifacts",
        governor=governor,
        transport_factory=lambda _root, mode: ScriptedTransport(mode),
        signing_key=b"meta-train-fixture-signing-key-32-bytes",
    )
    evaluators = {source.task_id: FakeKernelBenchBackend() for source in contract.new_sources}
    tasks = tuple(
        MetaTrainTask(
            source=source,
            task_card="Optimize the frozen public KernelBench reference.",
            reference_artifact=f"# {source.task_id}\n",
            solution_codec=KernelBenchSolutionCodec(),
            evaluator=evaluators[source.task_id],
        )
        for source in contract.new_sources
    )
    runner = MetaTrainCampaignRunner(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        variant=_variant("B0"),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=gateway,
        model="fixture-model",
    )

    new_trajectories = runner.run(tasks)
    assert len(new_trajectories) == 6
    assert all(item.sealed and len(item.round_summaries) == 8 for item in new_trajectories)
    assert sum(evaluator.calls for evaluator in evaluators.values()) == 48

    freezer = MetaTrainFreezer(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        model_gateway=gateway,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
        untrained_checkpoint_sha256="b" * 64,
        trained_variant=_variant(
            "B*",
            experience_sources=(contract.bank_id,),
            excluded_task_ids=_formal_heldout_ids(),
        ),
        online_variant=_variant(
            "B-online",
            experience_sources=(contract.bank_id,),
            excluded_task_ids=_formal_heldout_ids(),
        ),
        formal_heldout_ids=_formal_heldout_ids(),
    )
    frozen = freezer.freeze(_historical(contract) + new_trajectories)

    assert len(frozen.bank.records) == 8
    assert frozen.checkpoint.experience_bank_sha256 == frozen.bank.sha256
    assert frozen.builder_bindings == {
        "B*": frozen.checkpoint.sha256,
        "B-online": frozen.checkpoint.sha256,
    }
    assert governor.snapshot().global_committed == ResourceVector(
        model_calls=104,
        evaluator_transactions=48,
        gpu_exclusive_seconds=48.0,
    )

    # Recovery replays sealed rounds and completed distillation artifacts. It must
    # not call a model or evaluator again and must reproduce the same freeze.
    restored_gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "model-artifacts",
        governor=ResourceGovernor(
            journal=OperationJournal(
                tmp_path / "operations",
                anchor_path=tmp_path / "independent-head.json",
            ),
            global_caps=global_caps,
            cell_caps=cell_caps,
        ),
        transport_factory=lambda _root, _mode: pytest.fail("recovery called transport"),
        signing_key=b"different-recovery-signing-key-32b",
    )
    restored_evaluators = {
        source.task_id: FakeKernelBenchBackend() for source in contract.new_sources
    }
    restored_tasks = tuple(
        MetaTrainTask(
            source=source,
            task_card="Optimize the frozen public KernelBench reference.",
            reference_artifact=f"# {source.task_id}\n",
            solution_codec=KernelBenchSolutionCodec(),
            evaluator=restored_evaluators[source.task_id],
        )
        for source in contract.new_sources
    )
    restored_runner = MetaTrainCampaignRunner(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        variant=_variant("B0"),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=restored_gateway,
        model="fixture-model",
    )
    restored_new = restored_runner.run(restored_tasks)
    restored = MetaTrainFreezer(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        model_gateway=restored_gateway,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
        untrained_checkpoint_sha256="b" * 64,
        trained_variant=freezer.trained_variant,
        online_variant=freezer.online_variant,
        formal_heldout_ids=_formal_heldout_ids(),
    ).freeze(_historical(contract) + restored_new)

    assert restored == frozen
    assert all(evaluator.calls == 0 for evaluator in restored_evaluators.values())


def test_distillation_is_blocked_until_all_eight_sources_are_sealed(tmp_path: Path) -> None:
    contract = MetaTrainContract.from_json(DATA / "experience_bank_v1.json")
    caps = {"meta:distillation": ResourceCaps(model_calls=8)}
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=ResourceGovernor(
            journal=OperationJournal(tmp_path / "journal"),
            global_caps=ResourceCaps(model_calls=8),
            cell_caps=caps,
        ),
        transport_factory=lambda _root, mode: ScriptedTransport(mode),
        signing_key=b"meta-train-gate-signing-key-32bytes",
    )
    freezer = MetaTrainFreezer(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        model_gateway=gateway,
        model="fixture-model",
        rule_registry_sha256="a" * 64,
        untrained_checkpoint_sha256="b" * 64,
        trained_variant=_variant(
            "B*",
            experience_sources=(contract.bank_id,),
            excluded_task_ids=_formal_heldout_ids(),
        ),
        online_variant=_variant(
            "B-online",
            experience_sources=(contract.bank_id,),
            excluded_task_ids=_formal_heldout_ids(),
        ),
        formal_heldout_ids=_formal_heldout_ids(),
    )

    with pytest.raises(ValueError, match="exactly eight"):
        freezer.freeze(_historical(contract))
    assert gateway.governor.snapshot().global_committed.model_calls == 0
