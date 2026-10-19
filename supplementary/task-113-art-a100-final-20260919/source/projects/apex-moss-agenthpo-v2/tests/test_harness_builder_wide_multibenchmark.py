from __future__ import annotations

import hashlib
import json
from collections import deque
from dataclasses import asdict
from pathlib import Path

import pytest

from optimization_lab.generation import FakeGenerator
from optimization_lab.harness_builder.evaluation import NormalizedEvaluation
from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.model_gateway import IsolatedModelGateway
from optimization_lab.harness_builder.compile_receipts import (
    CompileReceiptArchive,
    HarnessCompileReceipt,
)
from optimization_lab.harness_builder.operators import (
    HarnessContext,
    PublicAttempt,
    TrustedOperatorRegistry,
)
from optimization_lab.harness_builder.runtime import HarnessRuntime
from optimization_lab.harness_builder.runner import HarnessBuilderCellRunner
from optimization_lab.harness_builder.schema import BuilderVariant, HarnessDecision
from optimization_lab.harness_builder.solutions import SolutionArtifact


_AXES = {
    "role_graph",
    "memory_views",
    "tools",
    "parent_strategy",
    "workflow",
    "scheduler_mode",
    "recovery_mode",
}

_BENCHMARK_BINDINGS = (
    ("agenthpobench", "agenthpobench:modernbert_mnli_accuracy"),
    ("gdpevo", "gdpevo:task_group_006"),
)


@pytest.fixture(params=_BENCHMARK_BINDINGS, ids=lambda item: item[0])
def benchmark_binding(request: pytest.FixtureRequest) -> tuple[str, str]:
    return request.param


def _variant() -> BuilderVariant:
    return BuilderVariant(
        variant_id="B-frozen-wide",
        description="mandatory full Harness recompilation fixture",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256="a" * 64,
        allowed_rule_ids=("discipline",),
        experience_sources=(),
        excluded_task_ids=(),
        adaptation_policy="wide_all_fields_recompile_v1",
    )


def _initial_decision() -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": ["task_analyst", "generator", "verifier"],
            "memory_views": ["current", "best"],
            "tools": ["task_semantics", "score_history"],
            "parent_strategy": "reference",
            "workflow": ["analyze", "generate", "verify_contract"],
            "scheduler_mode": "single_candidate",
            "recovery_mode": "preserve_failure",
            "kernel_directive": "Preserve the benchmark contract.",
        }
    )


def _wide_decision() -> HarnessDecision:
    return HarnessDecision.from_dict(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": [
                "performance_analyst",
                "critic",
                "generator",
                "verifier",
            ],
            "memory_views": ["current", "failures"],
            "tools": ["static_structure", "code_diff"],
            "parent_strategy": "incumbent",
            "workflow": [
                "select_parent",
                "inspect",
                "criticize",
                "generate",
                "verify_contract",
            ],
            "scheduler_mode": "repair_first",
            "recovery_mode": "repair_then_reset",
            "kernel_directive": "Rebuild every trusted Harness component axis.",
        }
    )


def _context(
    suite: str, instance_id: str, *, round_index: int
) -> HarnessContext:
    attempts = ()
    if round_index > 1:
        attempts = (
            PublicAttempt(
                attempt_id="v001",
                artifact_sha256="1" * 64,
                artifact_text="sealed public candidate",
                correct=True,
                score=1.0,
                outcome="valid",
                structural_signature="family-a",
                public_summary="valid score 1.0",
            ),
        )
    return HarnessContext(
        instance_id=instance_id,
        suite=suite,
        round_index=round_index,
        task_card=f"Optimize one frozen {suite} fixture.",
        reference_artifact_id="reference",
        reference_artifact="sealed reference artifact",
        attempts=attempts,
    )


def _components_by_axis(compiled: object) -> dict[str, tuple[str, ...]]:
    instances = getattr(compiled, "component_instances")
    return {
        axis: tuple(
            item.component_id for item in instances if item.axis == axis
        )
        for axis in _AXES
    }


def _build_two_version_lineage(
    root: Path, *, suite: str, instance_id: str
) -> dict[str, object]:
    variant = _variant()
    registry = TrustedOperatorRegistry(rule_registry_sha256="a" * 64)
    archive = CompileReceiptArchive(root)
    initial = _initial_decision()
    wide = _wide_decision()

    initial_context = _context(suite, instance_id, round_index=1)
    initial_compiled = registry.compile(
        initial,
        variant=variant,
        context=initial_context,
    )
    initial_receipt = HarnessCompileReceipt.create(
        cell_id=f"formal:{instance_id}:B-frozen-wide",
        suite=suite,
        instance_id=instance_id,
        variant_id=variant.variant_id,
        version="v001",
        adaptation_policy=variant.adaptation_policy,
        previous_receipt_sha256="0" * 64,
        previous_decision_sha256="0" * 64,
        compiled=initial_compiled,
        decision=initial,
    )
    archive.store_version(
        receipt=initial_receipt, decision=initial, fixture_only=True
    )

    wide_context = _context(suite, instance_id, round_index=2)
    wide_compiled = registry.compile(
        wide,
        variant=variant,
        context=wide_context,
        previous_decision=initial,
        prior_operational_fingerprints=(initial.operational_fingerprint,),
    )
    wide_receipt = HarnessCompileReceipt.create(
        cell_id=f"formal:{instance_id}:B-frozen-wide",
        suite=suite,
        instance_id=instance_id,
        variant_id=variant.variant_id,
        version="v002",
        adaptation_policy=variant.adaptation_policy,
        previous_receipt_sha256=initial_receipt.sha256,
        previous_decision_sha256=initial.sha256,
        compiled=wide_compiled,
        decision=wide,
        previous_decision=initial,
        prior_operational_fingerprints=(initial.operational_fingerprint,),
    )
    archive.store_version(receipt=wide_receipt, decision=wide, fixture_only=True)

    return {
        "archive": archive,
        "registry": registry,
        "variant": variant,
        "initial": initial,
        "wide": wide,
        "initial_compiled": initial_compiled,
        "wide_compiled": wide_compiled,
        "initial_receipt": initial_receipt,
        "wide_receipt": wide_receipt,
    }


def test_b_frozen_wide_contract_holds_in_each_benchmark(
    tmp_path: Path, benchmark_binding: tuple[str, str]
) -> None:
    suite, instance_id = benchmark_binding
    lineage = _build_two_version_lineage(
        tmp_path / suite, suite=suite, instance_id=instance_id
    )
    archive = lineage["archive"]
    registry = lineage["registry"]
    variant = lineage["variant"]
    initial = lineage["initial"]
    wide = lineage["wide"]
    initial_compiled = lineage["initial_compiled"]
    wide_compiled = lineage["wide_compiled"]
    initial_receipt = lineage["initial_receipt"]
    wide_receipt = lineage["wide_receipt"]
    assert isinstance(archive, CompileReceiptArchive)
    assert isinstance(registry, TrustedOperatorRegistry)
    assert isinstance(variant, BuilderVariant)
    assert isinstance(initial, HarnessDecision)
    assert isinstance(wide, HarnessDecision)
    assert isinstance(initial_receipt, HarnessCompileReceipt)
    assert isinstance(wide_receipt, HarnessCompileReceipt)

    assert set(wide_compiled.change_map) == _AXES
    assert all(wide_compiled.change_map.values())
    assert set(_components_by_axis(initial_compiled)) == _AXES
    assert all(
        _components_by_axis(initial_compiled)[axis]
        != _components_by_axis(wide_compiled)[axis]
        for axis in _AXES
    )

    replayed_compile = registry.compile(
        wide,
        variant=variant,
        context=_context(suite, instance_id, round_index=2),
        previous_decision=initial,
        prior_operational_fingerprints=(initial.operational_fingerprint,),
    )
    assert replayed_compile.component_instances == wide_compiled.component_instances
    assert all(
        replayed is not sealed
        for replayed, sealed in zip(
            replayed_compile.component_instances,
            wide_compiled.component_instances,
            strict=True,
        )
    )

    loaded_v1, loaded_initial = archive.load_version(
        "v001",
        cell_id=initial_receipt.cell_id,
        suite=suite,
        instance_id=instance_id,
        variant_id=variant.variant_id,
    )
    loaded_v2, loaded_wide = archive.load_version(
        "v002",
        cell_id=wide_receipt.cell_id,
        suite=suite,
        instance_id=instance_id,
        variant_id=variant.variant_id,
    )
    assert loaded_initial == initial
    assert loaded_wide == wide
    assert loaded_v1.previous_receipt_sha256 == "0" * 64
    assert loaded_v1.previous_decision_sha256 == "0" * 64
    assert loaded_v2.previous_receipt_sha256 == loaded_v1.sha256
    assert loaded_v2.previous_decision_sha256 == loaded_initial.sha256
    assert (loaded_v2.suite, loaded_v2.instance_id) == (suite, instance_id)

    runtime = HarnessRuntime(
        operator_registry=registry,
        planner=FakeGenerator(json.dumps(asdict(initial))),
        solution_generator=FakeGenerator("candidate must not be generated"),
        model="fixture-model",
    )
    reused = runtime.plan_and_compile(
        variant=variant,
        context=_context(suite, instance_id, round_index=3),
        previous_decision=wide,
        previous_compile_receipt_sha256=wide_receipt.sha256,
        prior_operational_fingerprints=(
            initial.operational_fingerprint,
            wide.operational_fingerprint,
        ),
    )
    assert reused.planner_rejection_reason == "wide_harness_fingerprint_reused"
    assert reused.compiled_harness is None

    other_suite = "gdpevo" if suite == "agenthpobench" else "agenthpobench"
    with pytest.raises(ValueError, match="binding differs"):
        archive.load_version(
            "v002",
            cell_id=wide_receipt.cell_id,
            suite=other_suite,
            instance_id=instance_id,
            variant_id=variant.variant_id,
        )
    with pytest.raises(ValueError, match="binding differs"):
        archive.load_version(
            "v002",
            cell_id=wide_receipt.cell_id,
            suite=suite,
            instance_id=f"{suite}:cross-used-instance",
            variant_id=variant.variant_id,
        )


def test_compile_receipt_cannot_be_cross_used_between_benchmark_cells(
    tmp_path: Path,
) -> None:
    agent = _build_two_version_lineage(
        tmp_path / "agenthpobench",
        suite="agenthpobench",
        instance_id="agenthpobench:modernbert_mnli_accuracy",
    )
    gdpevo = _build_two_version_lineage(
        tmp_path / "gdpevo",
        suite="gdpevo",
        instance_id="gdpevo:task_group_006",
    )
    agent_receipt = agent["wide_receipt"]
    agent_decision = agent["wide"]
    gdpevo_receipt = gdpevo["wide_receipt"]
    assert isinstance(agent_receipt, HarnessCompileReceipt)
    assert isinstance(agent_decision, HarnessDecision)
    assert isinstance(gdpevo_receipt, HarnessCompileReceipt)
    assert agent_receipt.sha256 != gdpevo_receipt.sha256

    cross_archive = CompileReceiptArchive(tmp_path / "cross-use")
    agent_initial_receipt = agent["initial_receipt"]
    agent_initial_decision = agent["initial"]
    assert isinstance(agent_initial_receipt, HarnessCompileReceipt)
    assert isinstance(agent_initial_decision, HarnessDecision)
    cross_archive.store_version(
        receipt=agent_initial_receipt,
        decision=agent_initial_decision,
        fixture_only=True,
    )
    cross_archive.store_version(
        receipt=agent_receipt,
        decision=agent_decision,
        fixture_only=True,
    )
    with pytest.raises(ValueError, match="binding differs"):
        cross_archive.load_version(
            "v002",
            cell_id=gdpevo_receipt.cell_id,
            suite=gdpevo_receipt.suite,
            instance_id=gdpevo_receipt.instance_id,
            variant_id=gdpevo_receipt.variant_id,
        )


_EIGHT_WORKFLOWS = (
    ("analyze", "generate", "verify_contract"),
    ("inspect", "generate", "verify_contract"),
    ("hypothesize", "generate", "verify_contract"),
    ("criticize", "generate", "verify_contract"),
    ("select_parent", "generate", "verify_contract"),
    ("analyze", "inspect", "generate", "verify_contract"),
    ("hypothesize", "criticize", "generate", "verify_contract"),
    ("select_parent", "inspect", "generate", "verify_contract"),
)


def _eight_round_decision(round_index: int) -> str:
    odd = round_index % 2 == 1
    return json.dumps(
        {
            "schema_version": 1,
            "rule_id": "discipline",
            "role_graph": (
                ["task_analyst", "critic", "generator", "verifier"]
                if odd
                else [
                    "performance_analyst",
                    "compiler_analyst",
                    "generator",
                    "verifier",
                ]
            ),
            "memory_views": ["current", "best"] if odd else ["current", "failures"],
            "tools": (
                ["task_semantics", "score_history"]
                if odd
                else ["static_structure", "code_diff"]
            ),
            "parent_strategy": "reference" if odd else "incumbent",
            "workflow": list(_EIGHT_WORKFLOWS[round_index - 1]),
            "scheduler_mode": "single_candidate" if odd else "repair_first",
            "recovery_mode": "preserve_failure" if odd else "repair_then_reset",
            "kernel_directive": f"Compile a fresh seven-axis Harness v{round_index:03d}.",
        }
    )


class _TextCodec:
    output_mode = "plain_text"

    def parse(self, raw_response: str) -> SolutionArtifact:
        text = raw_response.strip() + "\n"
        return SolutionArtifact(
            raw_response=raw_response,
            text=text,
            sha256=hashlib.sha256(text.encode()).hexdigest(),
            structural_signature=hashlib.sha256(
                ("wide-structure:" + text).encode()
            ).hexdigest(),
            extension=".txt",
            artifact_kind="wide-fixture",
        )


class _Evaluator:
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=5.0
    )

    def __init__(self) -> None:
        self.calls = 0

    def evaluate(self, _artifact_path: Path, private_dir: Path) -> NormalizedEvaluation:
        self.calls += 1
        private_dir.mkdir(parents=True, exist_ok=True)
        score = 1.0 + self.calls / 100.0
        return NormalizedEvaluation(
            status="valid",
            correct=True,
            score=score,
            public_feedback={"status": "valid", "score": score},
            actual_usage=ResourceVector(
                evaluator_transactions=1, cpu_evaluator_seconds=1.0
            ),
        )


def test_eight_round_wide_reinstallation_runs_on_each_benchmark(
    tmp_path: Path, benchmark_binding: tuple[str, str]
) -> None:
    """Exercise the real cell runner, not merely the decision helper.

    Mandatory components such as generator/verifier may retain their trusted
    implementation IDs.  Their round-bound instance/config nonces must still be
    fresh, while every one of the seven architectural selections changes.
    """

    suite, instance_id = benchmark_binding
    cell_id = f"formal:{instance_id}:B-frozen-wide"
    responses = deque(
        item
        for round_index in range(1, 9)
        for item in (
            _eight_round_decision(round_index),
            f"{suite}-solution-{round_index}",
        )
    )
    caps = ResourceCaps(
        model_calls=16,
        evaluator_transactions=8,
        gpu_exclusive_seconds=0,
        cpu_evaluator_seconds=40,
    )
    governor = ResourceGovernor(
        journal=OperationJournal(
            tmp_path / suite / "journal",
            anchor_path=tmp_path / suite / "trusted-head.json",
        ),
        global_caps=caps,
        cell_caps={cell_id: caps},
    )
    evaluator = _Evaluator()
    artifact_root = tmp_path / suite / "campaign"
    result = HarnessBuilderCellRunner(
        artifact_root=artifact_root,
        cell_id=cell_id,
        instance_id=instance_id,
        suite=suite,
        task_card=f"Optimize one frozen {suite} fixture.",
        reference_artifact="sealed reference artifact",
        variant=_variant(),
        operator_registry=TrustedOperatorRegistry(rule_registry_sha256="a" * 64),
        model_gateway=IsolatedModelGateway(
            artifact_root=tmp_path / suite / "models",
            governor=governor,
            transport_factory=lambda _root, _mode: FakeGenerator(responses.popleft()),
            signing_key=b"wide-fixture-signing-key-with-enough-entropy",
        ),
        model="fixture-model",
        solution_codec=_TextCodec(),
        evaluator=evaluator,
    ).run()

    assert result.sealed
    assert evaluator.calls == 8
    assert not responses
    assert len({decision.operational_fingerprint for decision in result.decisions if decision}) == 8

    archive = CompileReceiptArchive(artifact_root / "compiled")
    previous_receipt: HarnessCompileReceipt | None = None
    previous_nonces: set[str] = set()
    previous_configs: set[str] = set()
    for round_index in range(1, 9):
        version = f"v{round_index:03d}"
        receipt, decision = archive.load_version(
            version,
            cell_id=cell_id,
            suite=suite,
            instance_id=instance_id,
            variant_id="B-frozen-wide",
            adaptation_policy="wide_all_fields_recompile_v1",
        )
        assert decision == result.decisions[round_index - 1]
        assert set(receipt.change_map) == _AXES
        assert all(receipt.change_map.values())
        assert {item["axis"] for item in receipt.component_instances} == _AXES
        current_nonces = {
            str(item["instance_nonce_sha256"])
            for item in receipt.component_instances
        }
        current_configs = {
            str(item["config_sha256"]) for item in receipt.component_instances
        }
        assert not current_nonces & previous_nonces
        assert not current_configs & previous_configs
        assert receipt.previous_receipt_sha256 == (
            "0" * 64 if previous_receipt is None else previous_receipt.sha256
        )
        previous_receipt = receipt
        previous_nonces = current_nonces
        previous_configs = current_configs
