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
from optimization_lab.harness_builder.formal import (
    FormalCampaignContract,
    FormalCampaignResult,
    FormalCampaignRunner,
    FormalTaskBinding,
    _write_once,
)
from optimization_lab.harness_builder.learning import (
    BuilderCheckpoint,
    ExperienceBankSnapshot,
)
from optimization_lab.harness_builder.model_gateway import IsolatedModelGateway
from optimization_lab.harness_builder.operators import TrustedOperatorRegistry
from optimization_lab.harness_builder.schema import BuilderVariant
from optimization_lab.harness_builder.solutions import SolutionArtifact
from optimization_lab.harness_builder.stream import ARMS, StreamItem
from scripts.run_harness_builder_formal import main as formal_cli_main


RULE_SHA = "a" * 64
UNTRAINED_SHA = "b" * 64


def test_formal_write_once_rejects_symlink_target_and_parent(tmp_path: Path) -> None:
    outside_file = tmp_path / "outside.json"
    outside_file.write_bytes(b"original\n")
    receipts = tmp_path / "receipts"
    receipts.mkdir()
    target = receipts / "sealed.json"
    target.symlink_to(outside_file)
    with pytest.raises(ValueError, match="unsafe sealed formal artifact"):
        _write_once(target, b"sealed\n")
    assert outside_file.read_bytes() == b"original\n"

    outside_dir = tmp_path / "outside-receipts"
    outside_dir.mkdir()
    linked_parent = tmp_path / "linked-receipts"
    linked_parent.symlink_to(outside_dir, target_is_directory=True)
    with pytest.raises(ValueError, match="unsafe sealed formal artifact"):
        _write_once(linked_parent / "sealed.json", b"sealed\n")
    assert list(outside_dir.iterdir()) == []


class TextCodec:
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


class FakeEvaluator:
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


class PromptAwareGenerator:
    def __init__(self, calls: list[str]) -> None:
        self.calls = calls

    def estimated_api_cost_usd(self) -> float:
        return 0.0

    def generate(self, prompt: str, *, model: str) -> GenerationResult:
        self.calls.append(prompt)
        if prompt.startswith("Distill the fully sealed first-encounter"):
            marker = "Sealed public trajectory:\n"
            public = json.loads(prompt.split(marker, 1)[1])
            instance_id = public["instance_id"]
            event_id = public["arm_event_ids"]["A"][0]
            raw = json.dumps(
                {
                    "records": [
                        _record(
                            record_id="online-"
                            + hashlib.sha256(instance_id.encode()).hexdigest()[:16],
                            source=instance_id,
                            event_id=event_id,
                        )
                    ]
                }
            )
        elif prompt.startswith("Choose one bounded system-level Harness") or prompt.startswith(
            "Sham planner control call"
        ):
            match = re.search(r'"round_index":\s*(\d+)', prompt)
            round_index = int(match.group(1)) if match else 1
            raw = _decision(round_index)
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
class FakeSuiteProvider:
    suite: str
    bind_calls: list[str]
    evaluators: dict[str, FakeEvaluator]

    def bind(self, item: StreamItem) -> FormalTaskBinding:
        self.bind_calls.append(item.instance_id)
        evaluator = self.evaluators.setdefault(
            item.instance_id, FakeEvaluator(item.instance_id)
        )
        return FormalTaskBinding(
            suite=item.suite,
            task_id=item.task_id,
            instance_id=item.instance_id,
            task_binding_sha256=hashlib.sha256(item.instance_id.encode()).hexdigest(),
            task_card=f"Optimize public fixture {item.instance_id}.",
            reference_artifact=f"reference for {item.instance_id}",
            instance_descriptors=(item.suite, "fixture", item.task_id),
            solution_codec=TextCodec(),
            evaluator=evaluator,
        )


class FakeProviderFactory:
    def __init__(self, staging_sha: str, *, fail_if_created: bool = False) -> None:
        self.staging_plan_sha256 = staging_sha
        self.fail_if_created = fail_if_created
        self.bind_calls: list[str] = []
        self.evaluators: dict[str, FakeEvaluator] = {}

    def create(self, suite: str) -> FakeSuiteProvider:
        if self.fail_if_created:
            pytest.fail("completed formal replay requested a suite provider")
        return FakeSuiteProvider(suite, self.bind_calls, self.evaluators)


def _decision(round_index: int) -> str:
    payload = {
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
    }
    return json.dumps(payload)


def _record(*, record_id: str, source: str, event_id: str) -> dict[str, object]:
    return {
        "record_id": record_id,
        "source_instance_id": source,
        "builder_version": "builder-v001",
        "instance_descriptor": ["fixture", "optimization"],
        "initial_harness_structure": ["task_analyst", "generator", "verifier"],
        "evolution_rule": "discipline",
        "trigger_evidence": ["public score trajectory"],
        "outcome_delta": 0.03,
        "correctness": True,
        "resource_cost": {"model_calls": 16.0, "evaluator_seconds": 16.0},
        "counterexamples": ["single-instance evidence only"],
        "scope": "single_instance_observation",
        "provenance_event_ids": [event_id],
        "sealed": True,
    }


def _variants(instance_ids: tuple[str, ...]) -> tuple[BuilderVariant, ...]:
    return (
        BuilderVariant(
            variant_id="A",
            description="fixture A",
            freeze_after_initial=True,
            continual_update=False,
            rule_registry_sha256=RULE_SHA,
            allowed_rule_ids=("discipline",),
            experience_sources=(),
            excluded_task_ids=(),
        ),
        BuilderVariant(
            variant_id="B0",
            description="fixture B0",
            freeze_after_initial=False,
            continual_update=False,
            rule_registry_sha256=RULE_SHA,
            allowed_rule_ids=("discipline",),
            experience_sources=(),
            excluded_task_ids=(),
        ),
        *(
            BuilderVariant(
                variant_id=variant_id,
                description=f"fixture {variant_id}",
                freeze_after_initial=False,
                continual_update=variant_id == "B-online",
                rule_registry_sha256=RULE_SHA,
                allowed_rule_ids=("discipline",),
                experience_sources=("fixture-meta-bank",),
                excluded_task_ids=instance_ids,
            )
            for variant_id in ("B*", "B-online")
        ),
    )


def _ready_staging(instance_ids: tuple[str, ...]) -> bytes:
    stream = []
    cells: dict[str, dict[str, int | float]] = {}
    for index, instance_id in enumerate(instance_ids):
        suite, task_id = instance_id.split(":", 1)
        order = ARMS[index % 4 :] + ARMS[: index % 4]
        stream.append(
            {
                "stream_index": index,
                "block_index": index,
                "suite": suite,
                "task_id": task_id,
                "instance_id": instance_id,
                "arm_order": list(order),
            }
        )
        for arm in ARMS:
            cells[f"formal:{suite}:{task_id}:{arm}"] = ResourceCaps(
                model_calls=16,
                evaluator_transactions=11,
                cpu_evaluator_seconds=110.0,
            ).to_dict()
        cells[f"distill:{index:03d}:{instance_id}"] = ResourceCaps(
            model_calls=1
        ).to_dict()
    global_caps = ResourceCaps(
        model_calls=65 * len(instance_ids),
        evaluator_transactions=44 * len(instance_ids),
        cpu_evaluator_seconds=440.0 * len(instance_ids),
    )
    payload = {
        "schema_version": 1,
        "phase_id": "hb-gen1-formal-fixture",
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
        "budgets": global_caps.to_dict(),
        "resource_entitlement_totals": global_caps.to_dict(),
        "cell_entitlements": cells,
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(ARMS),
        "stream": stream,
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    return json.dumps(payload, sort_keys=True).encode()


def _initial_bank_and_checkpoint() -> tuple[ExperienceBankSnapshot, BuilderCheckpoint]:
    bank = ExperienceBankSnapshot.create(
        bank_id="fixture-meta-bank",
        parent_sha256=None,
        records=(
            ExperienceRecord.from_dict(
                _record(
                    record_id="meta-record",
                    source="kernelbench:meta-task",
                    event_id="meta-event",
                )
            ),
        ),
    )
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=UNTRAINED_SHA,
        experience_bank_sha256=bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance="kernelbench:meta-train-complete",
        stream_index=8,
    )
    return bank, checkpoint


def _runner_fixture(
    tmp_path: Path,
    *,
    instance_ids: tuple[str, ...] = ("suite-a:task-1", "suite-b:task-2"),
    fail_provider: bool = False,
    transport_calls: list[str] | None = None,
):
    encoded = _ready_staging(instance_ids)
    contract = FormalCampaignContract.from_staging_bytes(
        encoded, require_full_stream=False
    )
    journal = OperationJournal(
        tmp_path / "journal", anchor_path=tmp_path / "trusted-head.json"
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=contract.global_caps,
        cell_caps=contract.cell_entitlements,
    )
    calls = transport_calls if transport_calls is not None else []
    gateway = IsolatedModelGateway(
        artifact_root=tmp_path / "models",
        governor=governor,
        transport_factory=lambda _root, _mode: PromptAwareGenerator(calls),
        signing_key=b"fixture-signing-key-with-enough-entropy",
    )
    bank, checkpoint = _initial_bank_and_checkpoint()
    provider = FakeProviderFactory(
        contract.staging_plan_sha256, fail_if_created=fail_provider
    )
    runner = FormalCampaignRunner(
        artifact_root=tmp_path / "campaign",
        contract=contract,
        variants=_variants(instance_ids),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256=RULE_SHA),
        model_gateway=gateway,
        provider_factory=provider,
        initial_trained_bank=bank,
        initial_trained_checkpoint=checkpoint,
        untrained_checkpoint_sha256=UNTRAINED_SHA,
    )
    return runner, provider, governor, bank, checkpoint, calls


def test_formal_prequential_runner_seals_in_order_and_learns_only_forward(
    tmp_path: Path,
) -> None:
    runner, provider, governor, initial_bank, checkpoint, calls = _runner_fixture(
        tmp_path
    )

    result = runner.run()

    assert result.sealed is True
    assert result.completed_instance_ids == ("suite-a:task-1", "suite-b:task-2")
    assert result.newly_executed_instances == 2
    assert result.replayed_instances == 0
    assert len(calls) == 130  # 2 instances * (4 arms * 16 calls + 1 distill)
    assert sum(evaluator.calls for evaluator in provider.evaluators.values()) == 64
    assert governor.snapshot().global_committed == ResourceVector(
        model_calls=130,
        evaluator_transactions=64,
        cpu_evaluator_seconds=128.0,
    )

    formal = tmp_path / "campaign/formal"
    first = next(path for path in (formal / "instances").iterdir() if path.name.startswith("000-"))
    second = next(path for path in (formal / "instances").iterdir() if path.name.startswith("001-"))
    first_star = json.loads((first / "arms/B*.json").read_text())
    first_online = json.loads((first / "arms/B-online.json").read_text())
    second_star = json.loads((second / "arms/B*.json").read_text())
    second_online = json.loads((second / "arms/B-online.json").read_text())
    assert first_star["builder_checkpoint_sha256"] == checkpoint.sha256
    assert first_online["builder_checkpoint_sha256"] == checkpoint.sha256
    assert first_star["experience_bank_sha256"] == initial_bank.sha256
    assert first_online["experience_bank_sha256"] == initial_bank.sha256
    assert second_star["builder_checkpoint_sha256"] == checkpoint.sha256
    assert second_star["experience_bank_sha256"] == initial_bank.sha256
    assert second_online["builder_checkpoint_sha256"] != checkpoint.sha256
    assert first_online["cross_instance_record_ids"] == ["meta-record"]
    assert "online-" in " ".join(second_online["cross_instance_record_ids"])

    arm_facts = [
        event["payload"]
        for event in runner.registry.read_events()
        if event["event_type"] == "hb_gen1_formal_arm_sealed"
    ]
    assert [value["arm"] for value in arm_facts[:4]] == list(ARMS)
    assert [value["arm"] for value in arm_facts[4:8]] == list(ARMS[1:] + ARMS[:1])
    assert (formal / "campaign_receipt.json").is_file()


def test_completed_formal_rerun_is_replay_only_and_never_relearns(
    tmp_path: Path,
) -> None:
    first, _provider, governor, _bank, _checkpoint, calls = _runner_fixture(tmp_path)
    original = first.run()
    event_count = len(first.registry.read_events())
    ledger_bytes = governor.journal.ledger_path.read_bytes()

    restored, restored_provider, _restored_governor, _bank, _checkpoint, restored_calls = (
        _runner_fixture(tmp_path, fail_provider=True, transport_calls=[])
    )
    replayed = restored.run()

    assert replayed.first_encounter_summary_sha256 == original.first_encounter_summary_sha256
    assert replayed.newly_executed_instances == 0
    assert replayed.replayed_instances == 2
    assert restored_calls == []
    assert restored_provider.bind_calls == []
    assert len(restored.registry.read_events()) == event_count
    assert restored.model_gateway.governor.journal.ledger_path.read_bytes() == ledger_bytes
    assert len(calls) == 130


def test_crash_after_all_arms_replays_cells_and_runs_one_distillation(
    tmp_path: Path,
) -> None:
    instance_ids = ("suite-a:task-1",)
    runner, provider, _governor, _bank, _checkpoint, calls = _runner_fixture(
        tmp_path, instance_ids=instance_ids
    )
    def crash_before_distill(**_kwargs):
        raise KeyboardInterrupt("fixture crash before distillation")

    runner._distill = crash_before_distill  # type: ignore[method-assign]
    with pytest.raises(KeyboardInterrupt, match="before distillation"):
        runner.run()
    assert len(calls) == 64
    assert sum(evaluator.calls for evaluator in provider.evaluators.values()) == 32

    restored, restored_provider, _governor, _bank, _checkpoint, restored_calls = (
        _runner_fixture(tmp_path, instance_ids=instance_ids, transport_calls=[])
    )
    result = restored.run()

    assert result.sealed is True
    assert restored_calls and len(restored_calls) == 1
    assert sum(evaluator.calls for evaluator in restored_provider.evaluators.values()) == 0


def test_contract_rejects_duplicate_first_encounter_and_blocked_execution() -> None:
    encoded = _ready_staging(("suite-a:task-1", "suite-b:task-2"))
    payload = json.loads(encoded)
    payload["stream"][1]["suite"] = "suite-a"
    payload["stream"][1]["task_id"] = "task-1"
    payload["stream"][1]["instance_id"] = "suite-a:task-1"
    with pytest.raises(ValueError, match="only once"):
        FormalCampaignContract.from_staging_bytes(
            json.dumps(payload).encode(), require_full_stream=False
        )

    payload = json.loads(encoded)
    payload["execution_ready"] = False
    payload["blockers"] = ["evaluator_canary_pending"]
    contract = FormalCampaignContract.from_staging_bytes(
        json.dumps(payload).encode(), require_full_stream=False
    )
    with pytest.raises(RuntimeError, match="evaluator_canary_pending"):
        contract.require_executable()

    payload = json.loads(encoded)
    payload["resource_entitlement_totals"]["model_calls"] -= 1
    with pytest.raises(ValueError, match="does not match"):
        FormalCampaignContract.from_staging_bytes(
            json.dumps(payload).encode(), require_full_stream=False
        )


def test_formal_cli_is_preflight_by_default_and_requires_ready_execute(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    artifact_root = tmp_path / "artifacts"
    artifact_root.mkdir()
    blocked = json.loads(_ready_staging(("suite-a:task-1",)))
    blocked["execution_ready"] = False
    blocked["blockers"] = ["trusted_evaluator_canary_pending"]
    (artifact_root / "staging_plan.json").write_text(json.dumps(blocked))

    assert formal_cli_main(
        ["--artifact-root", str(artifact_root)], require_full_stream=False
    ) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["execution_ready"] is False
    assert report["model_calls_started"] == 0
    with pytest.raises(RuntimeError, match="trusted_evaluator_canary_pending"):
        formal_cli_main(
            ["--artifact-root", str(artifact_root), "--execute"],
            require_full_stream=False,
            runner_factory=lambda _contract: pytest.fail("blocked CLI entered runner"),
        )

    ready = _ready_staging(("suite-a:task-1",))
    (artifact_root / "staging_plan.json").write_bytes(ready)
    entered: list[str] = []

    class StubRunner:
        def run(self) -> FormalCampaignResult:
            entered.append("runner")
            return FormalCampaignResult(
                sealed=True,
                completed_instance_ids=("suite-a:task-1",),
                newly_executed_instances=1,
                replayed_instances=0,
                online_checkpoint_sha256="1" * 64,
                online_bank_sha256="2" * 64,
                first_encounter_summary_sha256="3" * 64,
            )

    assert formal_cli_main(
        ["--artifact-root", str(artifact_root), "--execute"],
        require_full_stream=False,
        runner_factory=lambda _contract: StubRunner(),  # type: ignore[return-value]
    ) == 0
    assert entered == ["runner"]
    result = json.loads(capsys.readouterr().out)
    assert result["result"]["sealed"] is True
