from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
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
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.formal import FormalTaskBinding
from optimization_lab.harness_builder.learning import (
    BuilderCheckpoint,
    ExperienceBankSnapshot,
)
from optimization_lab.harness_builder.model_gateway import IsolatedModelGateway
from optimization_lab.harness_builder.operators import TrustedOperatorRegistry
from optimization_lab.harness_builder.schema import BuilderVariant
from optimization_lab.harness_builder.solutions import SolutionArtifact
from optimization_lab.harness_builder.three_arm import (
    THREE_ARMS,
    ThreeArmCampaignContract,
    ThreeArmCampaignRunner,
)


RULE_SHA = "a" * 64
EMPTY_PARENT_SHA = "b" * 64


class _TextCodec:
    output_mode = "plain_text"

    def parse(self, raw_response: str) -> SolutionArtifact:
        text = raw_response.strip() + "\n"
        return SolutionArtifact(
            raw_response=raw_response,
            text=text,
            sha256=hashlib.sha256(text.encode()).hexdigest(),
            structural_signature=hashlib.sha256(
                ("structure:" + text).encode()
            ).hexdigest(),
            extension=".txt",
            artifact_kind="fixture",
        )


class _Evaluator:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=10.0
    )

    def __init__(self, instance_id: str) -> None:
        self.instance_id = instance_id
        self.calls = 0

    def evaluate(self, artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        self.calls += 1
        private_dir.mkdir(parents=True, exist_ok=True)
        score = 1.0 + self.calls / 100.0
        return NormalizedEvaluation(
            status="valid",
            correct=True,
            score=score,
            public_feedback={"status": "valid", "score": score},
            actual_usage=ResourceVector(
                evaluator_transactions=1, cpu_evaluator_seconds=2.0
            ),
            evidence_sha256=hashlib.sha256(
                f"{self.instance_id}:{self.calls}".encode()
            ).hexdigest(),
        )


class _Generator:
    def __init__(self, calls: list[str], *, wide: bool = False) -> None:
        self.calls = calls
        self.wide = wide

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append(prompt)
        if prompt.startswith("Distill the fully sealed first-encounter"):
            marker = "Sealed public trajectory:\n"
            public = json.loads(prompt.split(marker, 1)[1])
            instance_id = public["instance_id"]
            # Continual learning may use only B-online's sealed public trajectory;
            # control-arm evidence must not leak into the learner.
            event_id = public["arm_event_ids"]["B-online"][0]
            raw = json.dumps(
                {
                    "records": [
                        {
                            "record_id": "online-"
                            + hashlib.sha256(instance_id.encode()).hexdigest()[:16],
                            "source_instance_id": instance_id,
                            "builder_version": "builder-v001",
                            "instance_descriptor": ["fixture", "optimization"],
                            "initial_harness_structure": [
                                "task_analyst",
                                "generator",
                                "verifier",
                            ],
                            "evolution_rule": "discipline",
                            "trigger_evidence": ["public score trajectory"],
                            "outcome_delta": 0.03,
                            "correctness": True,
                            "resource_cost": {
                                "model_calls": 16.0,
                                "evaluator_seconds": 16.0,
                            },
                            "counterexamples": ["single-instance evidence only"],
                            "scope": "single_instance_observation",
                            "provenance_event_ids": [event_id],
                            "sealed": True,
                        }
                    ]
                }
            )
        elif prompt.startswith("Choose one bounded system-level Harness") or prompt.startswith(
            "Sham planner control call"
        ):
            match = re.search(r'"round_index":\s*(\d+)', prompt)
            round_index = int(match.group(1)) if match else 1
            if self.wide:
                raw = json.dumps(_wide_decision(round_index))
            else:
                raw = json.dumps({
                    "schema_version": 1,
                    "rule_id": "discipline",
                    "role_graph": [
                        "task_analyst",
                        *(["critic"] if round_index % 2 == 0 else []),
                        "generator",
                        "verifier",
                    ],
                    "memory_views": ["current", "best", "failures"],
                    "tools": ["task_semantics", "score_history", "static_structure"],
                    "parent_strategy": "reference" if round_index % 2 else "incumbent",
                    "workflow": ["analyze", "generate", "verify_contract"],
                    "scheduler_mode": "single_candidate",
                    "recovery_mode": "preserve_failure",
                    "kernel_directive": f"Generate fixture {round_index}.",
                })
        else:
            raw = "solution-" + hashlib.sha256(prompt.encode()).hexdigest()[:16]
        return GenerationResult(
            raw_response=raw,
            api_cost_usd=0.0,
            provider="fake",
            usage={},
            audit_log_path="",
        )


@dataclass
class _Provider:
    suite: str
    bind_calls: list[str]
    evaluators: dict[str, _Evaluator]

    def bind(self, item) -> FormalTaskBinding:
        self.bind_calls.append(item.instance_id)
        evaluator = self.evaluators.setdefault(
            item.instance_id, _Evaluator(item.instance_id)
        )
        return FormalTaskBinding(
            suite=item.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=hashlib.sha256(item.instance_id.encode()).hexdigest(),
            task_card=f"Optimize public fixture {item.instance_id}.",
            reference_artifact=f"reference for {item.instance_id}",
            instance_descriptors=(item.suite, "fixture", item.task_id),
            solution_codec=_TextCodec(),
            evaluator=evaluator,
        )


class _Factory:
    def __init__(self, staging_sha: str, *, fail_if_created: bool = False) -> None:
        self.staging_plan_sha256 = staging_sha
        self.fail_if_created = fail_if_created
        self.bind_calls: list[str] = []
        self.evaluators: dict[str, _Evaluator] = {}

    def create(self, suite: str) -> _Provider:
        if self.fail_if_created:
            pytest.fail("completed replay requested a suite provider")
        return _Provider(suite, self.bind_calls, self.evaluators)


def _wide_decision(round_index: int) -> dict[str, object]:
    role_graphs = (
        ["task_analyst", "generator", "verifier"],
        ["performance_analyst", "critic", "generator", "verifier"],
        ["compiler_analyst", "generator", "verifier"],
        ["task_analyst", "critic", "generator", "verifier"],
        ["performance_analyst", "generator", "verifier"],
        ["compiler_analyst", "critic", "generator", "verifier"],
        ["task_analyst", "performance_analyst", "generator", "verifier"],
        ["task_analyst", "compiler_analyst", "generator", "verifier"],
    )
    memories = (
        ["current"],
        ["best", "failures"],
        ["current", "structural_diverse"],
        ["failures"],
        ["best"],
        ["current", "failures"],
        ["best", "structural_diverse"],
        ["current", "best", "failures"],
    )
    tools = (
        ["task_semantics"],
        ["score_history", "static_structure"],
        ["public_profile"],
        ["compiler_observation", "code_diff"],
        ["task_semantics", "static_structure"],
        ["score_history"],
        ["public_profile", "code_diff"],
        ["compiler_observation"],
    )
    workflows = (
        ["generate", "verify_contract"],
        ["analyze", "generate", "verify_contract"],
        ["inspect", "generate", "verify_contract"],
        ["hypothesize", "criticize", "generate", "verify_contract"],
        ["select_parent", "generate", "verify_contract"],
        ["analyze", "criticize", "generate", "verify_contract"],
        ["inspect", "hypothesize", "generate", "verify_contract"],
        ["select_parent", "criticize", "generate", "verify_contract"],
    )
    index = round_index - 1
    return {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": role_graphs[index],
        "memory_views": memories[index],
        "tools": tools[index],
        "parent_strategy": (
            "reference",
            "incumbent",
            "restart",
            "stable_best",
            "reference",
            "incumbent",
            "restart",
            "stable_best",
        )[index],
        "workflow": workflows[index],
        "scheduler_mode": (
            "single_candidate",
            "repair_first",
            "explore_then_exploit",
            "single_candidate",
            "repair_first",
            "explore_then_exploit",
            "single_candidate",
            "repair_first",
        )[index],
        "recovery_mode": (
            "preserve_failure",
            "repair_then_reset",
            "reset_immediately",
            "preserve_failure",
            "repair_then_reset",
            "reset_immediately",
            "preserve_failure",
            "repair_then_reset",
        )[index],
        "kernel_directive": f"Recompile all seven Harness axes for round {round_index}.",
    }


def _variants(
    instance_ids: tuple[str, ...], *, wide_frozen: bool = False
) -> tuple[BuilderVariant, ...]:
    shared = {
        "description": "fixture Builder",
        "rule_registry_sha256": RULE_SHA,
        "allowed_rule_ids": ("discipline",),
        "experience_sources": (),
        "excluded_task_ids": instance_ids,
    }
    return (
        BuilderVariant(
            variant_id="A",
            description="fixture task-conditioned arm",
            freeze_after_initial=True,
            continual_update=False,
            rule_registry_sha256=RULE_SHA,
            allowed_rule_ids=("discipline",),
            experience_sources=(),
            excluded_task_ids=(),
        ),
        BuilderVariant(
            variant_id="B-frozen",
            freeze_after_initial=False,
            continual_update=False,
            adaptation_policy=(
                "wide_all_fields_recompile_v1"
                if wide_frozen
                else "conditional_any_v1"
            ),
            **shared,
        ),
        BuilderVariant(
            variant_id="B-online",
            freeze_after_initial=False,
            continual_update=True,
            **shared,
        ),
    )


def _staging(instance_ids: tuple[str, ...]) -> bytes:
    stream = []
    cells: dict[str, dict[str, int | float]] = {}
    for index, instance_id in enumerate(instance_ids):
        suite, task_id = instance_id.split(":", 1)
        order = THREE_ARMS[index % 3 :] + THREE_ARMS[: index % 3]
        learning_mode = "online" if index == 0 else "sealed"
        stream.append(
            {
                "stream_index": index,
                "block_index": index,
                "suite": suite,
                "task_id": task_id,
                "instance_id": instance_id,
                "arm_order": list(order),
                "learning_mode": learning_mode,
            }
        )
        for arm in THREE_ARMS:
            cells[f"formal:{suite}:{task_id}:{arm}"] = ResourceCaps(
                model_calls=16,
                evaluator_transactions=8,
                cpu_evaluator_seconds=80.0,
            ).to_dict()
        if learning_mode == "online":
            cells[f"distill:{index:03d}:{instance_id}"] = ResourceCaps(
                model_calls=1
            ).to_dict()
    totals = ResourceCaps(
        model_calls=97,
        evaluator_transactions=48,
        cpu_evaluator_seconds=480.0,
    )
    payload = {
        "schema_version": 5,
        "phase_id": "hb-three-arm-fixture",
        "code_revision": "c" * 40,
        "model_signature": {
            "executor_model": "fixture-model",
            "reasoning_effort": "high",
            "transport": "fake",
            "client_version": "fake-1",
        },
        "execution_ready": True,
        "blockers": [],
        "source_hashes": {"fixture": "d" * 64},
        "budgets": totals.to_dict(),
        "resource_entitlement_totals": totals.to_dict(),
        "cell_entitlements": cells,
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "validity_policy": {
            "rounds_per_arm": 8,
            "minimum_valid_rounds_per_arm": 4,
            "learning_tasks_per_suite": 6,
            "minimum_paired_learning_tasks": 5,
            "insufficient_status": "insufficient_validity",
            "score_aggregation": "valid_only_mean_and_best",
        },
        "stream": stream,
        "experience_initialization": "empty",
        "online_instances_per_suite": 1,
        "sealed_instances_per_suite": 1,
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    return json.dumps(payload, sort_keys=True).encode()


def _runner(
    tmp_path: Path,
    *,
    fail_provider: bool = False,
    calls=None,
    wide_frozen: bool = False,
):
    instance_ids = ("suite-a:task-online", "suite-a:task-sealed")
    contract = ThreeArmCampaignContract.from_staging_bytes(
        _staging(instance_ids), require_full_stream=False
    )
    journal = OperationJournal(
        tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=contract.global_caps,
        cell_caps=contract.cell_entitlements,
    )
    transport_calls = calls if calls is not None else []
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=lambda _root, _mode: _Generator(
            transport_calls, wide=wide_frozen
        ),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    bank = ExperienceBankSnapshot.create(
        bank_id="hb-three-arm-empty-v1", parent_sha256=None, records=()
    )
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=EMPTY_PARENT_SHA,
        experience_bank_sha256=bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance="initial-empty",
        stream_index=0,
    )
    provider = _Factory(contract.staging_plan_sha256, fail_if_created=fail_provider)
    runner = ThreeArmCampaignRunner(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        variants=_variants(instance_ids, wide_frozen=wide_frozen),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256=RULE_SHA),
        model_gateway=gateway,
        provider_factory=provider,
        initial_empty_bank=bank,
        initial_empty_checkpoint=checkpoint,
        task_conditioned_checkpoint_sha256=EMPTY_PARENT_SHA,
    )
    return runner, provider, governor, bank, checkpoint, transport_calls


def test_contract_requires_three_arms_and_distillation_only_for_online() -> None:
    encoded = _staging(("suite-a:task-online", "suite-a:task-sealed"))
    contract = ThreeArmCampaignContract.from_staging_bytes(
        encoded, require_full_stream=False
    )
    assert contract.arms == THREE_ARMS
    assert [item.learning_mode for item in contract.stream] == ["online", "sealed"]

    payload = json.loads(encoded)
    payload["variant_ids"] = ["A", "B0", "B-online"]
    with pytest.raises(ValueError, match="variant order"):
        ThreeArmCampaignContract.from_staging_bytes(
            json.dumps(payload).encode(), require_full_stream=False
        )

    payload = json.loads(encoded)
    payload["cell_entitlements"][
        "distill:001:suite-a:task-sealed"
    ] = ResourceCaps(model_calls=1).to_dict()
    payload["resource_entitlement_totals"]["model_calls"] += 1
    payload["budgets"]["model_calls"] += 1
    with pytest.raises(ValueError, match="sealed instance cannot distill"):
        ThreeArmCampaignContract.from_staging_bytes(
            json.dumps(payload).encode(), require_full_stream=False
        )


def test_runner_learns_after_online_but_never_after_sealed(tmp_path: Path) -> None:
    runner, provider, governor, empty_bank, checkpoint, calls = _runner(tmp_path)

    result = runner.run()

    assert result.sealed is True
    assert result.completed_instance_ids == (
        "suite-a:task-online",
        "suite-a:task-sealed",
    )
    assert result.newly_executed_arm_cells == 6
    assert len(calls) == 97  # 6 cells * 16 calls + one online distillation
    assert sum(value.calls for value in provider.evaluators.values()) == 48
    assert governor.snapshot().global_committed == ResourceVector(
        model_calls=97,
        evaluator_transactions=48,
        cpu_evaluator_seconds=96.0,
    )

    formal = tmp_path / "campaign/formal"
    first = next(path for path in (formal / "instances").iterdir() if path.name.startswith("000-"))
    second = next(path for path in (formal / "instances").iterdir() if path.name.startswith("001-"))
    first_frozen = json.loads((first / "arms/B-frozen.json").read_text())
    first_online = json.loads((first / "arms/B-online.json").read_text())
    second_frozen = json.loads((second / "arms/B-frozen.json").read_text())
    second_online = json.loads((second / "arms/B-online.json").read_text())
    assert first_frozen["builder_checkpoint_sha256"] == checkpoint.sha256
    assert first_online["builder_checkpoint_sha256"] == checkpoint.sha256
    assert first_frozen["experience_bank_sha256"] == empty_bank.sha256
    assert first_online["experience_bank_sha256"] == empty_bank.sha256
    assert second_frozen["builder_checkpoint_sha256"] == checkpoint.sha256
    assert second_frozen["experience_bank_sha256"] == empty_bank.sha256
    assert second_online["builder_checkpoint_sha256"] != checkpoint.sha256
    assert second_frozen["cross_instance_record_ids"] == []
    assert second_online["cross_instance_record_ids"][0].startswith("online-")
    assert second_online["curve"]["validity_status"] == "sufficient_validity"
    assert second_online["curve"]["valid_rounds"] == 8
    second_online_planners = [
        prompt
        for prompt in calls
        if prompt.startswith("Choose one bounded system-level Harness")
        and '"instance_id": "suite-a:task-sealed"' in prompt
    ]
    assert second_online_planners
    assert any('"cross_instance_memory_available": true' in prompt for prompt in second_online_planners)
    assert any('"record_id": "online-' in prompt for prompt in second_online_planners)

    first_receipt = json.loads((first / "instance_receipt.json").read_text())
    second_receipt = json.loads((second / "instance_receipt.json").read_text())
    assert first_receipt["learning_mode"] == "online"
    assert first_receipt["distillation_operation_id"] is not None
    assert second_receipt["learning_mode"] == "sealed"
    assert second_receipt["distillation_operation_id"] is None
    assert (
        second_receipt["output_online_checkpoint_sha256"]
        == second_receipt["input_online_checkpoint_sha256"]
    )


def test_max_new_arm_cells_stops_at_recoverable_arm_boundary(tmp_path: Path) -> None:
    runner, _provider, _governor, _bank, _checkpoint, calls = _runner(tmp_path)

    partial = runner.run(max_new_arm_cells=1)

    assert partial.sealed is False
    assert partial.newly_executed_arm_cells == 1
    assert partial.completed_instance_ids == ()
    assert len(calls) == 16

    restored, _provider, _governor, _bank, _checkpoint, restored_calls = _runner(
        tmp_path, calls=[]
    )
    complete = restored.run()
    assert complete.sealed is True
    assert len(restored_calls) == 81


def test_completed_rerun_is_replay_only(tmp_path: Path) -> None:
    first, _provider, governor, _bank, _checkpoint, calls = _runner(tmp_path)
    original = first.run()
    ledger = governor.journal.ledger_path.read_bytes()

    restored, provider, _governor, _bank, _checkpoint, restored_calls = _runner(
        tmp_path, fail_provider=True, calls=[]
    )
    replayed = restored.run()

    assert replayed.first_encounter_summary_sha256 == original.first_encounter_summary_sha256
    assert replayed.newly_executed_arm_cells == 0
    assert replayed.replayed_instances == 2
    assert restored_calls == []
    assert provider.bind_calls == []
    assert restored.model_gateway.governor.journal.ledger_path.read_bytes() == ledger
    assert len(calls) == 97


def test_wide_arm_receipt_replay_recompiles_without_new_operations(
    tmp_path: Path,
) -> None:
    runner, provider, governor, _bank, _checkpoint, calls = _runner(
        tmp_path, wide_frozen=True
    )

    partial = runner.run(max_new_arm_cells=2)
    assert partial.sealed is False
    assert partial.newly_executed_arm_cells == 2
    ledger = governor.journal.ledger_path.read_bytes()
    cell_id = "formal:suite-a:task-online:B-frozen"
    cell_ledger_path = (
        tmp_path
        / "campaign/formal/cells"
        / hashlib.sha256(cell_id.encode()).hexdigest()
        / "ledger.jsonl"
    )
    cell_ledger = cell_ledger_path.read_bytes()
    call_count = len(calls)
    evaluation_count = sum(
        evaluator.calls for evaluator in provider.evaluators.values()
    )

    restored, restored_provider, _governor, _bank, _checkpoint, restored_calls = _runner(
        tmp_path, calls=[], wide_frozen=True
    )
    item = restored.contract.stream[0]
    binding = restored._binding_for(item)  # type: ignore[arg-type]
    restored._run_or_replay_arm(
        item=item,  # type: ignore[arg-type]
        arm="B-frozen",
        binding=binding,
        checkpoint_sha256=restored.initial_checkpoint.sha256,
        bank=restored.initial_bank,
    )

    assert restored_calls == []
    assert restored_provider.bind_calls == ["suite-a:task-online"]
    assert sum(
        evaluator.calls for evaluator in restored_provider.evaluators.values()
    ) == 0
    assert restored.model_gateway.governor.journal.ledger_path.read_bytes() == ledger
    assert cell_ledger_path.read_bytes() == cell_ledger
    assert len(calls) == call_count
    assert evaluation_count == 16


def test_wide_completed_instance_replay_uses_provider_and_is_zero_call(
    tmp_path: Path,
) -> None:
    first, _provider, governor, _bank, _checkpoint, _calls = _runner(
        tmp_path, wide_frozen=True
    )
    original = first.run()
    operation_ledger = governor.journal.ledger_path.read_bytes()
    formal_ledger = first.registry.ledger_path.read_bytes()

    restored, provider, _governor, _bank, _checkpoint, restored_calls = _runner(
        tmp_path, calls=[], wide_frozen=True
    )
    replayed = restored.run()

    assert replayed.first_encounter_summary_sha256 == original.first_encounter_summary_sha256
    assert replayed.replayed_instances == 2
    assert restored_calls == []
    assert provider.bind_calls == [
        "suite-a:task-online",
        "suite-a:task-sealed",
    ]
    assert sum(evaluator.calls for evaluator in provider.evaluators.values()) == 0
    assert restored.model_gateway.governor.journal.ledger_path.read_bytes() == operation_ledger
    assert restored.registry.ledger_path.read_bytes() == formal_ledger


def test_successor_starts_at_global_cursor_and_isolates_control_arms(
    tmp_path: Path,
) -> None:
    instance_ids = ("suite-a:task-online", "suite-a:task-sealed")
    contract = ThreeArmCampaignContract.from_staging_bytes(
        _staging(instance_ids), require_full_stream=False
    )
    journal = OperationJournal(
        tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=contract.global_caps,
        cell_caps=contract.cell_entitlements,
    )
    calls: list[str] = []
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=lambda _root, _mode: _Generator(calls),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    empty_bank = ExperienceBankSnapshot.create(
        bank_id="hb-three-arm-empty-v1", parent_sha256=None, records=()
    )
    empty_checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=EMPTY_PARENT_SHA,
        experience_bank_sha256=empty_bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance="initial-empty",
        stream_index=0,
    )
    imported_record = ExperienceRecord.from_dict(
        {
            "record_id": "imported-record",
            "source_instance_id": "suite-a:task-online",
            "builder_version": "builder-v001",
            "instance_descriptor": ["suite-a", "fixture", "task-online"],
            "initial_harness_structure": ["generator", "verifier"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["sealed prefix evidence"],
            "outcome_delta": 0.1,
            "correctness": True,
            "resource_cost": {"model_calls": 1.0},
            "counterexamples": ["single prefix only"],
            "scope": "single_instance_observation",
            "provenance_event_ids": ["prefix-event"],
            "sealed": True,
        }
    )
    imported_bank = ExperienceBankSnapshot.create(
        bank_id="hb-three-arm-imported-v1",
        parent_sha256=empty_bank.sha256,
        records=(imported_record,),
    )
    imported_checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=empty_checkpoint.sha256,
        experience_bank_sha256=imported_bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance="suite-a:task-online",
        stream_index=0,
    )
    provider = _Factory(contract.staging_plan_sha256)
    runner = ThreeArmCampaignRunner(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        variants=_variants(instance_ids),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256=RULE_SHA),
        model_gateway=gateway,
        provider_factory=provider,
        initial_empty_bank=empty_bank,
        initial_empty_checkpoint=empty_checkpoint,
        task_conditioned_checkpoint_sha256=EMPTY_PARENT_SHA,
        execution_start_index=1,
        initial_online_bank=imported_bank,
        initial_online_checkpoint=imported_checkpoint,
    )

    # A bounded successor must still seal when its final active cell completes;
    # the historical prefix is outside this runner's execution window.
    result = runner.run(max_new_arm_cells=3)

    assert result.sealed is True
    assert result.completed_instance_ids == ("suite-a:task-sealed",)
    assert provider.bind_calls == ["suite-a:task-sealed"]
    assert len(calls) == 48
    instance_root = next(
        (tmp_path / "campaign/formal/instances").glob("001-*")
    )
    a = json.loads((instance_root / "arms/A.json").read_text())
    frozen = json.loads((instance_root / "arms/B-frozen.json").read_text())
    online = json.loads((instance_root / "arms/B-online.json").read_text())
    assert a["experience_bank_sha256"] is None
    assert a["cross_instance_record_ids"] == []
    assert frozen["builder_checkpoint_sha256"] == empty_checkpoint.sha256
    assert frozen["experience_bank_sha256"] == empty_bank.sha256
    assert frozen["cross_instance_record_ids"] == []
    assert online["builder_checkpoint_sha256"] == imported_checkpoint.sha256
    assert online["experience_bank_sha256"] == imported_bank.sha256
    assert online["cross_instance_record_ids"] == ["imported-record"]
    assert not (
        tmp_path
        / "campaign/formal/experience_banks"
        / f"{imported_bank.sha256}.json"
    ).exists()
    assert not (
        tmp_path
        / "campaign/formal/builder_checkpoints"
        / f"{imported_checkpoint.sha256}.json"
    ).exists()
