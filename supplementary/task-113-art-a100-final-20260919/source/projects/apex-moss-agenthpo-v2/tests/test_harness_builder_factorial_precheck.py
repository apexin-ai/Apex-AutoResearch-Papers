from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from types import MappingProxyType

import pytest

from optimization_lab.harness_builder.factorial_policies import (
    ARM_IDS,
    ARM_POLICY_SPECS,
)
from optimization_lab.harness_builder.factorial_precheck import (
    FIXTURE_ONLY_PLAN_SCOPE,
    FORMAL_ARM_ORDER_ALGORITHM,
    PRECHECK_PHASES,
    FactorialFormalZeroCallBarrierController,
    FactorialFormalZeroCallPlan,
    FactorialPrecheckController,
    FactorialTaskSeedSchedule,
    FactorialZeroCallPlan,
    task_seed_arm_order,
    verify_formal_v001_fork_bindings,
)
from optimization_lab.harness_builder.factorial_contract import (
    DEFAULT_FACTORIAL_MANIFEST,
    factorial_main_matrix_projection,
    verify_factorial_contract,
)
from optimization_lab.harness_builder.factorial_trunk import TaskSeedKey
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)


_AGENT_ROOT = Path("/tmp/moss-bench-qual.rYRM8Q/agenthpobench")
_GDPEVO_ROOT = Path("/tmp/moss-bench-qual.rYRM8Q/gdpevo")


def _sha(label: str) -> str:
    return hashlib.sha256(label.encode()).hexdigest()


def _key(suite: str, instance: str, seed: int) -> TaskSeedKey:
    return TaskSeedKey(
        suite=suite,
        instance_id=instance,
        seed=seed,
        task_binding_sha256=_sha(f"task:{suite}:{instance}"),
        factorial_contract_sha256=_sha("factorial-contract"),
        context_binding_sha256=_sha(f"context:{suite}:{instance}:{seed}"),
    )


def _plan(*, final_version: int = 3) -> FactorialZeroCallPlan:
    keys = (
        _key("agenthpobench", "task-a", 11),
        _key("gdpevo", "task-group-003:test-1", 11),
    )
    return FactorialZeroCallPlan(
        schedules=tuple(
            FactorialTaskSeedSchedule(
                key=key,
                final_version=final_version,
                arm_order=task_seed_arm_order(key),
            )
            for key in keys
        )
    )


def _formal_keys() -> tuple[TaskSeedKey, ...]:
    payload = verify_factorial_contract()
    return tuple(
        TaskSeedKey(
            suite=item["benchmark_id"],
            instance_id=item["instance_id"],
            seed=item["seed"],
            task_binding_sha256=_sha(
                f"formal-task:{item['benchmark_id']}:{item['instance_id']}"
            ),
            factorial_contract_sha256=payload["contract_digest"],
            context_binding_sha256=_sha(
                f"formal-context:{item['benchmark_id']}:"
                f"{item['instance_id']}:{item['seed']}"
            ),
        )
        for item in factorial_main_matrix_projection(payload)
    )


def _formal_source_authority():
    if not _AGENT_ROOT.is_dir() or not _GDPEVO_ROOT.is_dir():
        pytest.skip("pinned benchmark qualification checkouts are unavailable")
    authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT_ROOT,
        gdpevo_checkout=_GDPEVO_ROOT,
    )
    bundle = authority.rederive_exact_bundle()
    plan = FactorialFormalZeroCallPlan.from_authority_bundle(
        bundle, task_authority=authority
    )
    return authority, bundle, plan


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()


@dataclass(frozen=True)
class _Object:
    sha256: str


@dataclass(frozen=True)
class _Intent(_Object):
    task_seed_key: TaskSeedKey


@dataclass(frozen=True)
class _Canonical(_Object):
    task_seed_key_sha256: str
    context_binding_sha256: str
    compiled_harness_semantic_sha256: str


@dataclass(frozen=True)
class _Equivalence(_Object):
    task_seed_key_sha256: str
    canonical_compile_contract_sha256: str
    canonical_compiled_harness_semantic_sha256: str
    arm_compile_receipt_sha256s: MappingProxyType


@dataclass(frozen=True)
class _Trunk(_Object):
    task_seed_key_sha256: str
    intent_sha256: str
    canonical_compile_contract_sha256: str
    compile_equivalence_receipt_sha256: str
    version: str
    trunk_status: str
    decision_sha256: str
    operational_fingerprint: str
    compiled_harness_semantic_sha256: str
    solution_prompt_sha256: str
    solution_artifact_sha256: str
    attempt_artifact_sha256: str
    evaluation_artifact_sha256: str


@dataclass(frozen=True)
class _Fork(_Object):
    task_seed_key_sha256: str
    trunk_receipt_sha256: str
    arm_id: str
    arm_cell_id: str
    arm_variant_sha256: str
    arm_contract_sha256: str
    arm_compile_receipt_sha256: str
    trunk_status: str
    version: str
    shared_decision_sha256: str
    shared_operational_fingerprint: str
    shared_compiled_harness_semantic_sha256: str
    shared_solution_prompt_sha256: str
    shared_solution_artifact_sha256: str
    shared_attempt_artifact_sha256: str
    shared_evaluation_artifact_sha256: str


class _FakeTrunkArchive:
    def __init__(
        self,
        keys: tuple[TaskSeedKey, ...],
        *,
        arm_variant_sha256s: dict[str, str] | None = None,
        arm_contract_sha256: str | None = None,
    ) -> None:
        self.items: dict[str, dict[str, object]] = {}
        variants = arm_variant_sha256s or {
            arm: _sha(f"fixture-variant:{arm}") for arm in ARM_IDS
        }
        for key in keys:
            intent = _Intent(_sha(f"intent:{key.sha256}"), key)
            canonical = _Canonical(
                _sha(f"canonical:{key.sha256}"),
                key.sha256,
                key.context_binding_sha256,
                _sha(f"semantic:{key.sha256}"),
            )
            arm_compiles = MappingProxyType(
                {arm: _sha(f"compile:{key.sha256}:{arm}") for arm in ARM_IDS}
            )
            equivalence = _Equivalence(
                _sha(f"equivalence:{key.sha256}"),
                key.sha256,
                canonical.sha256,
                canonical.compiled_harness_semantic_sha256,
                arm_compiles,
            )
            trunk = _Trunk(
                _sha(f"trunk:{key.sha256}"),
                key.sha256,
                intent.sha256,
                canonical.sha256,
                equivalence.sha256,
                "v001",
                "SUCCESS",
                _sha(f"decision:{key.sha256}"),
                _sha(f"fingerprint:{key.sha256}"),
                canonical.compiled_harness_semantic_sha256,
                _sha(f"prompt:{key.sha256}"),
                _sha(f"solution:{key.sha256}"),
                _sha(f"attempt:{key.sha256}"),
                _sha(f"evaluation:{key.sha256}"),
            )
            forks = {
                arm: _Fork(
                    _sha(f"fork:{key.sha256}:{arm}"),
                    key.sha256,
                    trunk.sha256,
                    arm,
                    key.arm_cell_id(arm),
                    variants[arm],
                    arm_contract_sha256 or key.factorial_contract_sha256,
                    arm_compiles[arm],
                    trunk.trunk_status,
                    "v001",
                    trunk.decision_sha256,
                    trunk.operational_fingerprint,
                    trunk.compiled_harness_semantic_sha256,
                    trunk.solution_prompt_sha256,
                    trunk.solution_artifact_sha256,
                    trunk.attempt_artifact_sha256,
                    trunk.evaluation_artifact_sha256,
                )
                for arm in ARM_IDS
            }
            self.items[key.sha256] = {
                "intent": intent,
                "canonical": canonical,
                "equivalence": equivalence,
                "trunk": trunk,
                "forks": forks,
            }

    def load_intent(self, key_sha256: str) -> _Intent:
        return self.items[key_sha256]["intent"]  # type: ignore[return-value]

    def load_canonical_compile(self, key_sha256: str) -> _Canonical:
        return self.items[key_sha256]["canonical"]  # type: ignore[return-value]

    def load_equivalence(self, key_sha256: str) -> _Equivalence:
        return self.items[key_sha256]["equivalence"]  # type: ignore[return-value]

    def load_trunk(self, key_sha256: str) -> _Trunk:
        return self.items[key_sha256]["trunk"]  # type: ignore[return-value]

    def load_fork(self, key_sha256: str, arm_id: str) -> _Fork:
        return self.items[key_sha256]["forks"][arm_id]  # type: ignore[index,return-value]


def _controller(tmp_path: Path, *, final_version: int = 3):
    plan = _plan(final_version=final_version)
    archive = _FakeTrunkArchive(tuple(item.key for item in plan.schedules))
    return (
        FactorialPrecheckController(
            root=tmp_path / "precheck", plan=plan, trunk_archive=archive
        ),
        plan,
        archive,
    )


def _formal_controller(tmp_path: Path, *, schedule_index: int = 0):
    authority, bundle, plan = _formal_source_authority()
    schedule = plan.schedules[schedule_index]
    archive = _FakeTrunkArchive(
        (schedule.key,),
        arm_variant_sha256s=dict(plan.arm_variant_sha256s),
        arm_contract_sha256=plan.factorial_contract_sha256,
    )
    return (
        FactorialFormalZeroCallBarrierController(
            root=tmp_path / "formal-precheck",
            plan=plan,
            trunk_archive=archive,
            task_authority=authority,
            task_authority_bundle=bundle,
        ),
        plan,
        schedule,
        archive,
    )


def _run_phase(
    controller: FactorialPrecheckController,
    schedule: FactorialTaskSeedSchedule,
    version: int,
    phase: str,
) -> str:
    result = None
    for arm_id in schedule.arm_order:
        result = controller.acknowledge_phase(
            key=schedule.key,
            version=version,
            phase=phase,
            arm_id=arm_id,
            arm_update_policy=ARM_POLICY_SPECS[arm_id].update_policy,
            fixture_evidence_sha256=_sha(
                f"fixture:{schedule.key.sha256}:{version}:{phase}:{arm_id}"
            ),
        )
    assert result is not None and result.phase_barrier_sha256 is not None
    return result.phase_barrier_sha256


def _run_version(
    controller: FactorialPrecheckController,
    schedule: FactorialTaskSeedSchedule,
    version: int,
) -> None:
    for phase in PRECHECK_PHASES:
        _run_phase(controller, schedule, version, phase)


def test_plan_requires_two_benchmarks_frozen_hash_order_and_zero_authority() -> None:
    plan = _plan()
    assert plan.plan_scope == FIXTURE_ONLY_PLAN_SCOPE
    assert plan.execution_authority == "NOT_GRANTED"
    assert set(plan.execution_entitlement.values()) == {0}
    assert len({item.key.suite for item in plan.schedules}) == 2
    assert all(item.arm_order == task_seed_arm_order(item.key) for item in plan.schedules)
    assert plan.canonical_bytes.endswith(b"\n")
    assert FactorialZeroCallPlan.from_bytes(
        plan.canonical_bytes, expected_sha256=plan.sha256
    ) == plan

    single = (plan.schedules[0],)
    with pytest.raises(ValueError, match="at least two Benchmarks"):
        FactorialZeroCallPlan(single)
    with pytest.raises(ValueError, match="nonzero execution authority"):
        replace(plan, execution_authority="GRANTED")
    with pytest.raises(ValueError, match="nonzero execution entitlement"):
        replace(plan, model_call_entitlement=1)
    wrong_rotation = task_seed_arm_order(plan.schedules[0].key)[1:] + task_seed_arm_order(
        plan.schedules[0].key
    )[:1]
    with pytest.raises(ValueError, match="task/seed hash"):
        replace(plan.schedules[0], arm_order=wrong_rotation)
    with pytest.raises(ValueError, match="not canonical"):
        FactorialZeroCallPlan.from_bytes(plan.canonical_bytes.rstrip())


def test_formal_plan_factory_binds_exact_matrix_rounds_variants_and_balance() -> None:
    _authority, bundle, plan = _formal_source_authority()
    assert len(plan.schedules) == 126
    assert len({item.key.sha256 for item in plan.schedules}) == 126
    assert plan.execution_authority == "NOT_GRANTED"
    assert set(plan.execution_entitlement.values()) == {0}
    assert plan.to_dict()["formal_execution_ready"] is False
    assert plan.to_dict()["arm_order_algorithm"] == FORMAL_ARM_ORDER_ALGORITHM
    assert tuple(dict(plan.arm_variant_sha256s)) == ARM_IDS
    assert plan.task_authority_bundle_sha256 == bundle.sha256

    by_suite = {
        suite: [item for item in plan.schedules if item.key.suite == suite]
        for suite in {item.key.suite for item in plan.schedules}
    }
    assert len(by_suite["agenthpobench"]) == 36
    assert {item.final_version for item in by_suite["agenthpobench"]} == {6}
    assert len(by_suite["gdpevo"]) == 90
    assert {item.final_version for item in by_suite["gdpevo"]} == {3}
    assert plan.arm_order_balance["maximum_cell_imbalance"] == 1
    agent_groups = [
        group
        for group in plan.arm_order_balance["groups"]
        if group["benchmark_id"] == "agenthpobench"
    ]
    assert len(agent_groups) == 3
    assert all(group["maximum_cell_imbalance"] == 0 for group in agent_groups)

    assert FactorialFormalZeroCallPlan.from_bytes(
        plan.canonical_bytes,
        task_authority=_authority,
        task_authority_bundle=bundle,
        expected_sha256=plan.sha256,
    ) == plan


def test_formal_plan_rejects_missing_extra_or_contract_drifted_task_keys() -> None:
    keys = _formal_keys()
    with pytest.raises(ValueError, match="task key matrix differs"):
        FactorialFormalZeroCallPlan._from_task_seed_keys_for_fixture(
            keys[:-1], task_authority_bundle_sha256=_sha("fixture-bundle")
        )

    unexpected = replace(keys[-1], instance_id="unexpected_task")
    with pytest.raises(ValueError, match="task key matrix differs"):
        FactorialFormalZeroCallPlan._from_task_seed_keys_for_fixture(
            (*keys[:-1], unexpected),
            task_authority_bundle_sha256=_sha("fixture-bundle"),
        )

    drifted = replace(keys[0], factorial_contract_sha256=_sha("wrong-contract"))
    with pytest.raises(ValueError, match="contract binding differs"):
        FactorialFormalZeroCallPlan._from_task_seed_keys_for_fixture(
            (drifted, *keys[1:]),
            task_authority_bundle_sha256=_sha("fixture-bundle"),
        )


def test_public_formal_plan_factory_rejects_raw_self_consistent_keys() -> None:
    keys = tuple(
        replace(
            key,
            task_binding_sha256="a" * 64,
            context_binding_sha256="b" * 64,
        )
        for key in _formal_keys()
    )
    with pytest.raises(ValueError, match="task authority bundle"):
        FactorialFormalZeroCallPlan.from_authority_bundle(
            keys, task_authority=None
        )


def test_public_formal_plan_parser_requires_and_replays_source_authority() -> None:
    authority, bundle, plan = _formal_source_authority()
    with pytest.raises(TypeError, match="task_authority"):
        FactorialFormalZeroCallPlan.from_bytes(plan.canonical_bytes)

    forged_bundle_sha = _sha("forged-authority-bundle")
    forged_plan = replace(plan, task_authority_bundle_sha256=forged_bundle_sha)
    with pytest.raises(ValueError, match="source authority replay differs"):
        FactorialFormalZeroCallPlan.from_bytes(
            forged_plan.canonical_bytes,
            task_authority=authority,
            task_authority_bundle=bundle,
        )


def test_formal_plan_parser_rejects_arm_order_balance_policy_and_variant_tamper() -> None:
    _authority, _bundle, plan = _formal_source_authority()

    payload = json.loads(plan.canonical_bytes)
    payload["schedules"][0]["arm_order"], payload["schedules"][1]["arm_order"] = (
        payload["schedules"][1]["arm_order"],
        payload["schedules"][0]["arm_order"],
    )
    with pytest.raises(ValueError, match="arm order differs from frozen design"):
        FactorialFormalZeroCallPlan._from_bytes_unverified_source(
            _canonical(payload)
        )

    payload = json.loads(plan.canonical_bytes)
    payload["arm_order_balance"]["maximum_cell_imbalance"] = 0
    payload["arm_order_balance_sha256"] = _sha("forged-balance")
    with pytest.raises(ValueError, match="arm balance audit differs"):
        FactorialFormalZeroCallPlan._from_bytes_unverified_source(
            _canonical(payload)
        )

    payload = json.loads(plan.canonical_bytes)
    payload["arm_policies"][0]["update_policy"] = "forged-policy"
    with pytest.raises(ValueError, match="manifest/policy/variant binding differs"):
        FactorialFormalZeroCallPlan._from_bytes_unverified_source(
            _canonical(payload)
        )

    payload = json.loads(plan.canonical_bytes)
    payload["arm_variant_sha256s"][ARM_IDS[-1]] = _sha("forged-variant")
    with pytest.raises(ValueError, match="manifest/policy/variant binding differs"):
        FactorialFormalZeroCallPlan._from_bytes_unverified_source(
            _canonical(payload)
        )


def test_formal_plan_parser_rejects_checked_in_manifest_byte_drift(tmp_path: Path) -> None:
    _authority, _bundle, plan = _formal_source_authority()
    payload = json.loads(DEFAULT_FACTORIAL_MANIFEST.read_bytes())
    # Reordering an array produces a different valid contract projection and
    # must fail before persisted plan bytes can be trusted.
    payload["main_experiment"]["benchmarks"][0]["task_units"][0:2] = reversed(
        payload["main_experiment"]["benchmarks"][0]["task_units"][0:2]
    )
    manifest = tmp_path / "drifted-factorial.json"
    manifest.write_bytes(_canonical(payload))
    with pytest.raises(ValueError, match="requires checked-in manifest path"):
        FactorialFormalZeroCallPlan._from_bytes_unverified_source(
            plan.canonical_bytes, manifest_path=manifest
        )


@pytest.mark.parametrize("field", ("arm_variant_sha256", "arm_contract_sha256"))
def test_formal_v001_precheck_rejects_arbitrary_nonzero_fork_digest(
    field: str,
) -> None:
    _authority, _bundle, plan = _formal_source_authority()
    schedule = plan.schedules[0]
    variants = dict(plan.arm_variant_sha256s)
    archive = _FakeTrunkArchive(
        (schedule.key,),
        arm_variant_sha256s=variants,
        arm_contract_sha256=plan.factorial_contract_sha256,
    )
    receipt = verify_formal_v001_fork_bindings(
        plan=plan,
        trunk_archive=archive,
        key=schedule.key,
    )
    assert receipt.factorial_contract_sha256 == plan.factorial_contract_sha256
    assert dict(receipt.arm_variant_sha256s) == variants

    forks = archive.items[schedule.key.sha256]["forks"]
    arm_id = ARM_IDS[-1]
    fork = forks[arm_id]  # type: ignore[index]
    forks[arm_id] = replace(  # type: ignore[index]
        fork,
        **{field: _sha(f"arbitrary-nonzero:{field}")},
    )
    with pytest.raises(ValueError, match="formal v001 fork variant/contract differs"):
        verify_formal_v001_fork_bindings(
            plan=plan,
            trunk_archive=archive,
            key=schedule.key,
        )


def test_exact_formal_barrier_binds_v001_and_recovers_with_zero_entitlement(
    tmp_path: Path,
) -> None:
    controller, plan, schedule, archive = _formal_controller(tmp_path)
    receipt = controller.bind_shared_v001(schedule.key)
    assert receipt.plan_sha256 == plan.sha256
    assert receipt.arm_policy_sha256 == plan.bound_arm_policy_sha256
    assert receipt.model_calls == 0
    assert receipt.evaluator_transactions == 0

    _run_version(controller, schedule, 2)
    assert controller.task_seed_complete(schedule.key) is False
    status = controller.status()
    assert status["plan_scope"] == "FORMAL_EXACT_MATRIX_ZERO_CALL_ONLY"
    assert status["execution_authority"] == "NOT_GRANTED"
    assert set(status["execution_entitlement"].values()) == {0}
    assert status["formal_execution_ready"] is False

    resumed = FactorialFormalZeroCallBarrierController(
        root=tmp_path / "formal-precheck",
        plan=plan,
        trunk_archive=archive,
        task_authority=controller.task_authority,
        task_authority_bundle=controller.task_authority_bundle,
    )
    assert resumed.bind_shared_v001(schedule.key) == receipt
    assert resumed._verified_barrier(  # noqa: SLF001 - explicit recovery audit
        schedule.key, version=2, phase="evaluation"
    ).model_calls == 0


def test_exact_formal_barrier_rejects_fixture_plan(tmp_path: Path) -> None:
    fixture = _plan(final_version=2)
    archive = _FakeTrunkArchive(tuple(item.key for item in fixture.schedules))
    with pytest.raises(ValueError, match="exact formal zero-call plan"):
        FactorialFormalZeroCallBarrierController(
            root=tmp_path / "formal-precheck",
            plan=fixture,  # type: ignore[arg-type]
            trunk_archive=archive,
            task_authority=None,
            task_authority_bundle=None,
        )


@pytest.mark.parametrize("field", ("arm_variant_sha256", "arm_contract_sha256"))
def test_exact_formal_barrier_bind_v001_rejects_variant_or_contract_drift(
    tmp_path: Path,
    field: str,
) -> None:
    controller, _plan, schedule, archive = _formal_controller(tmp_path)
    controller.bind_shared_v001(schedule.key)
    forks = archive.items[schedule.key.sha256]["forks"]
    arm_id = ARM_IDS[0]
    fork = forks[arm_id]  # type: ignore[index]
    forks[arm_id] = replace(  # type: ignore[index]
        fork,
        **{field: _sha(f"formal-barrier-drift:{field}")},
    )
    with pytest.raises(ValueError, match="formal v001 fork variant/contract differs"):
        # Recovery/rebind must re-run the formal verifier rather than trust the
        # already persisted generic v001 binding.
        controller.bind_shared_v001(schedule.key)


def test_v002_requires_and_replays_one_shared_v001_trunk(tmp_path: Path) -> None:
    controller, plan, _archive = _controller(tmp_path)
    schedule = plan.schedules[0]
    first_arm = schedule.arm_order[0]
    with pytest.raises(ValueError, match="shared-v001 trunk must be bound"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=first_arm,
            arm_update_policy=ARM_POLICY_SPECS[first_arm].update_policy,
            fixture_evidence_sha256=_sha("fixture"),
        )
    receipt = controller.bind_shared_v001(schedule.key)
    assert receipt.model_calls == 0
    assert receipt.evaluator_transactions == 0
    assert tuple(arm for arm, _ in receipt.arm_fork_receipts) == ARM_IDS

    # Idempotent replay is byte-identical and still records no work.
    assert controller.bind_shared_v001(schedule.key) == receipt


def test_four_arm_order_and_phase_barriers_fail_closed(tmp_path: Path) -> None:
    controller, plan, _archive = _controller(tmp_path)
    schedule = plan.schedules[0]
    controller.bind_shared_v001(schedule.key)
    first, second, *_ = schedule.arm_order

    with pytest.raises(ValueError, match="predecessor is missing"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=second,
            arm_update_policy=ARM_POLICY_SPECS[second].update_policy,
            fixture_evidence_sha256=_sha("out-of-order"),
        )
    with pytest.raises(ValueError, match="arm policy differs"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=first,
            arm_update_policy="wrong-policy",
            fixture_evidence_sha256=_sha("wrong-policy"),
        )
    with pytest.raises(ValueError, match="phase barrier is missing"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="solution",
            arm_id=first,
            arm_update_policy=ARM_POLICY_SPECS[first].update_policy,
            fixture_evidence_sha256=_sha("too-early"),
        )

    update_barrier = _run_phase(controller, schedule, 2, "update")
    assert update_barrier != receipt_hash(controller, schedule.key, 2, "update", first)
    with pytest.raises(ValueError, match="refusing to overwrite"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=first,
            arm_update_policy=ARM_POLICY_SPECS[first].update_policy,
            fixture_evidence_sha256=_sha("different-replay"),
        )

    _run_phase(controller, schedule, 2, "solution")
    _run_phase(controller, schedule, 2, "evaluation")
    assert controller.task_seed_complete(schedule.key) is False


def receipt_hash(
    controller: FactorialPrecheckController,
    key: TaskSeedKey,
    version: int,
    phase: str,
    arm: str,
) -> str:
    schedule = controller.plan.schedule_for(key)
    position = schedule.arm_order.index(arm)
    return controller._load_phase_receipt_path(  # noqa: SLF001 - test replay surface
        controller._phase_path(key, version, phase, position, arm)  # noqa: SLF001
    ).sha256


def test_v002_through_v008_resume_is_idempotent_and_complete(tmp_path: Path) -> None:
    controller, plan, archive = _controller(tmp_path, final_version=8)
    schedule = plan.schedules[0]
    controller.bind_shared_v001(schedule.key)
    for version in range(2, 9):
        _run_version(controller, schedule, version)
    assert controller.task_seed_complete(schedule.key) is True

    status = controller.status()
    assert status["formal_execution_ready"] is False
    assert status["complete_task_seed_count"] == 1
    assert status["planned_benchmark_count"] == 2
    assert set(status["execution_entitlement"].values()) == {0}

    # Reconstructing the controller proves write-once plan replay and full-chain
    # recovery without executing any callback or allocating authority.
    resumed = FactorialPrecheckController(
        root=tmp_path / "precheck", plan=plan, trunk_archive=archive
    )
    assert resumed.task_seed_complete(schedule.key) is True
    first = schedule.arm_order[0]
    evidence = _sha(f"fixture:{schedule.key.sha256}:8:evaluation:{first}")
    replay = resumed.acknowledge_phase(
        key=schedule.key,
        version=8,
        phase="evaluation",
        arm_id=first,
        arm_update_policy=ARM_POLICY_SPECS[first].update_policy,
        fixture_evidence_sha256=evidence,
    )
    assert replay.phase_barrier_sha256 is not None


def test_two_benchmarks_have_independent_progress_and_tamper_fails(tmp_path: Path) -> None:
    controller, plan, _archive = _controller(tmp_path, final_version=2)
    left, right = plan.schedules
    controller.bind_shared_v001(left.key)
    controller.bind_shared_v001(right.key)
    _run_version(controller, left, 2)
    assert controller.task_seed_complete(left.key) is True
    assert controller.task_seed_complete(right.key) is False

    # The final barrier alone is insufficient: altering one immutable member
    # makes complete replay fail closed.
    member = controller._phase_path(  # noqa: SLF001 - deliberate corruption test
        left.key, 2, "evaluation", 0, left.arm_order[0]
    )
    member.write_bytes(member.read_bytes().replace(b'"model_calls":0', b'"model_calls":1'))
    with pytest.raises(ValueError, match="cannot record calls"):
        controller.task_seed_complete(left.key)


def test_barrier_sealing_revalidates_complete_rehashed_members(tmp_path: Path) -> None:
    controller, plan, _archive = _controller(tmp_path, final_version=2)
    schedule = plan.schedules[0]
    controller.bind_shared_v001(schedule.key)
    for arm_id in schedule.arm_order[:-1]:
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=arm_id,
            arm_update_policy=ARM_POLICY_SPECS[arm_id].update_policy,
            fixture_evidence_sha256=_sha(f"fixture:{arm_id}"),
        )
    first = schedule.arm_order[0]
    member = controller._phase_path(  # noqa: SLF001 - deliberate corruption test
        schedule.key, 2, "update", 0, first
    )
    payload = __import__("json").loads(member.read_bytes())
    payload["operation_id"] = "fully-rehashed-wrong-operation"
    member.write_bytes(
        (__import__("json").dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    )
    last = schedule.arm_order[-1]
    with pytest.raises(ValueError, match="member binding differs"):
        controller.acknowledge_phase(
            key=schedule.key,
            version=2,
            phase="update",
            arm_id=last,
            arm_update_policy=ARM_POLICY_SPECS[last].update_policy,
            fixture_evidence_sha256=_sha(f"fixture:{last}"),
        )
    assert not controller._barrier_path(  # noqa: SLF001
        schedule.key, 2, "update"
    ).exists()


def test_symlink_state_root_is_rejected(tmp_path: Path) -> None:
    plan = _plan()
    archive = _FakeTrunkArchive(tuple(item.key for item in plan.schedules))
    real = tmp_path / "real"
    real.mkdir()
    linked = tmp_path / "linked"
    linked.symlink_to(real, target_is_directory=True)
    with pytest.raises(ValueError, match="unsafe"):
        FactorialPrecheckController(root=linked, plan=plan, trunk_archive=archive)
