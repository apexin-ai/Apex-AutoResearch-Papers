from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.learning import (
    BuilderCheckpoint,
    ExperienceBankArchive,
    ExperienceBankSnapshot,
)
from optimization_lab.harness_builder.three_arm import THREE_ARMS
from optimization_lab.harness_builder.three_arm_continuation import (
    ContinuationSourceSpec,
    ExcludedTailExpectation,
    ThreeArmContinuationContract,
    ThreeArmContinuationSourceGuard,
    prepare_three_arm_continuation_source,
    verify_three_arm_continuation_source,
)


RULE_SHA = "a" * 64
SOURCE_REVISION = "b" * 40
PREFIX = (
    "suite-a:a0",
    "suite-b:b0",
    "suite-c:c0",
    "suite-b:b1",
    "suite-c:c1",
    "suite-a:a1",
)
TAIL_INSTANCE = "suite-c:discarded-tail"


def _canonical(payload: dict) -> bytes:
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode()


def _full_stream() -> list[dict]:
    suites = ("suite-a", "suite-b", "suite-c")
    per_suite = {suite: 0 for suite in suites}
    result: list[dict] = []
    for block in range(8):
        order = suites[block % 3 :] + suites[: block % 3]
        for suite in order:
            task_position = per_suite[suite]
            per_suite[suite] += 1
            task_id = f"{suite[-1]}{task_position}"
            index = len(result)
            arm_order = THREE_ARMS[index % 3 :] + THREE_ARMS[: index % 3]
            result.append(
                {
                    "stream_index": index,
                    "block_index": block,
                    "suite": suite,
                    "task_id": task_id,
                    "instance_id": f"{suite}:{task_id}",
                    "arm_order": list(arm_order),
                    "learning_mode": "online" if block < 6 else "sealed",
                }
            )
    assert tuple(item["instance_id"] for item in result[:6]) == PREFIX
    return result


def _cells(stream: list[dict], *, start: int) -> dict[str, dict]:
    cells: dict[str, dict] = {}
    for item in stream[start:]:
        for arm in THREE_ARMS:
            cells[f"formal:{item['instance_id']}:{arm}"] = ResourceCaps(
                model_calls=16,
                evaluator_transactions=8,
                cpu_evaluator_seconds=11200.0,
            ).to_dict()
        if item["learning_mode"] == "online":
            cells[
                f"distill:{item['stream_index']:03d}:{item['instance_id']}"
            ] = ResourceCaps(model_calls=1).to_dict()
    return cells


def _totals(cells: dict[str, dict]) -> ResourceCaps:
    vectors = [ResourceVector.from_dict(value) for value in cells.values()]
    return ResourceCaps(
        model_calls=sum(item.model_calls for item in vectors),
        evaluator_transactions=sum(item.evaluator_transactions for item in vectors),
        gpu_exclusive_seconds=sum(item.gpu_exclusive_seconds for item in vectors),
        cpu_evaluator_seconds=sum(item.cpu_evaluator_seconds for item in vectors),
    )


def _v5_staging(stream: list[dict]) -> bytes:
    cells = _cells(stream, start=0)
    totals = _totals(cells)
    payload = {
        "schema_version": 5,
        "phase_id": "source-v1r8",
        "code_revision": SOURCE_REVISION,
        "model_signature": {
            "executor_model": "fixture-model",
            "reasoning_effort": "high",
            "transport": "fake",
            "client_version": "fixture-1",
        },
        "execution_ready": True,
        "blockers": [],
        "source_hashes": {"fixture": "c" * 64},
        "budgets": totals.to_dict(),
        "resource_entitlement_totals": totals.to_dict(),
        "cell_entitlements": cells,
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "stream": stream,
        "experience_initialization": "empty",
        "online_instances_per_suite": 6,
        "sealed_instances_per_suite": 2,
        "validity_policy": {
            "rounds_per_arm": 8,
            "minimum_valid_rounds_per_arm": 4,
            "learning_tasks_per_suite": 6,
            "minimum_paired_learning_tasks": 5,
            "insufficient_status": "insufficient_validity",
            "score_aggregation": "valid_only_mean_and_best",
        },
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    return _canonical(payload)


def _record(index: int, instance_id: str) -> ExperienceRecord:
    return ExperienceRecord.from_dict(
        {
            "record_id": f"exp-{index:03d}",
            "source_instance_id": instance_id,
            "builder_version": "builder-v001",
            "instance_descriptor": ["fixture"],
            "initial_harness_structure": ["analyze", "generate", "verify"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["sealed public trajectory"],
            "outcome_delta": 0.1,
            "correctness": True,
            "resource_cost": {"model_calls": 16.0},
            "counterexamples": ["fixture only"],
            "scope": "single_instance_observation",
            "provenance_event_ids": [f"event-{index:03d}"],
            "sealed": True,
        }
    )


def _source_fixture(
    tmp_path: Path, *, production_receipts: bool = False
) -> tuple[Path, ContinuationSourceSpec]:
    root = tmp_path / "source"
    stream = _full_stream()
    staging = _v5_staging(stream)
    (root / "staging_plan.json").parent.mkdir(parents=True)
    (root / "staging_plan.json").write_bytes(staging)

    bank = ExperienceBankSnapshot.create(
        bank_id="online-through-005",
        parent_sha256="d" * 64,
        records=tuple(_record(index, instance) for index, instance in enumerate(PREFIX)),
    )
    ExperienceBankArchive(root / "formal/experience_banks").store(bank)
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256="e" * 64,
        experience_bank_sha256=bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance=PREFIX[-1],
        stream_index=5,
    )
    checkpoint_path = root / f"formal/builder_checkpoints/{checkpoint.sha256}.json"
    checkpoint_path.parent.mkdir(parents=True)
    checkpoint_path.write_bytes(checkpoint.canonical_bytes)

    receipt_hashes: list[str] = []
    formal_events: list[dict] = []
    for index, instance_id in enumerate(PREFIX):
        if production_receipts:
            item = stream[index]
            receipt = {
                "schema_version": 2,
                "phase_id": "source-v1r8",
                "staging_plan_sha256": hashlib.sha256(staging).hexdigest(),
                "stream_item": item,
                "arm_order": item["arm_order"],
                "task_binding_sha256": hashlib.sha256(instance_id.encode()).hexdigest(),
                "first_encounter": True,
                "same_instance_rerun_policy": "replay_only_no_formal_update",
                "learning_mode": item["learning_mode"],
                "input_online_checkpoint_sha256": checkpoint.sha256,
                "input_online_bank_sha256": bank.sha256,
                "arm_receipt_sha256s": {arm: str(index + 1) * 64 for arm in THREE_ARMS},
                "trajectory_sha256": str(index + 1) * 64,
                "distillation_operation_id": f"distill:{index:03d}:{instance_id}:distillation_call",
                "output_online_checkpoint_sha256": checkpoint.sha256,
                "output_online_bank_sha256": bank.sha256,
                "sealed": True,
                "no_next_phase": True,
            }
        else:
            receipt = {
                "schema_version": 1,
                "sealed": True,
                "stream_index": index,
                "instance_id": instance_id,
                "staging_plan_sha256": hashlib.sha256(staging).hexdigest(),
                "output_online_checkpoint_sha256": checkpoint.sha256,
                "output_online_bank_sha256": bank.sha256,
            }
        raw = _canonical(receipt)
        digest = hashlib.sha256(raw).hexdigest()
        receipt_hashes.append(digest)
        receipt_path = root / f"formal/instances/{index:03d}-{digest}/instance_receipt.json"
        receipt_path.parent.mkdir(parents=True)
        receipt_path.write_bytes(raw)
        formal_events.append(
            {
                "event_id": f"instance-{index}",
                "event_type": "hb_gen1_formal_instance_sealed",
                "payload": {
                    "stream_index": index,
                    "instance_id": instance_id,
                    "instance_receipt_sha256": digest,
                    "output_online_checkpoint_sha256": checkpoint.sha256,
                    "output_online_bank_sha256": bank.sha256,
                },
                "recorded_at": "2026-08-04T00:00:00+00:00",
            }
        )
    formal_raw = b"".join(_canonical(event) for event in formal_events)
    formal_path = root / "formal/ledger.jsonl"
    formal_path.write_bytes(formal_raw)
    formal_state = {
        "schema_version": 1,
        "event_count": len(formal_events),
        "last_event": formal_events[-1],
        "updated_at": "2026-08-04T00:00:00+00:00",
    }
    formal_state_path = root / "formal/state.json"
    formal_state_path.write_bytes(_canonical(formal_state))

    journal = OperationJournal(
        root / "control/operations",
        anchor_path=root / "control/trusted-operation-head.json",
    )
    cells = {
        f"formal:{PREFIX[0]}:A": ResourceCaps(model_calls=1),
        f"formal:{TAIL_INSTANCE}:A": ResourceCaps(model_calls=3),
    }
    governor = ResourceGovernor(
        journal=journal,
        global_caps=ResourceCaps(model_calls=4),
        cell_caps=cells,
    )
    prefix_op = "formal-op:prefix:planner_call:v001"
    governor.reserve(
        operation_id=prefix_op,
        cell_id=f"formal:{PREFIX[0]}:A",
        operation_kind="planner_call",
        reservation=ResourceVector(model_calls=1),
    )
    governor.start(prefix_op)
    governor.complete(
        prefix_op,
        actual_usage=ResourceVector(model_calls=1),
        artifact_sha256="f" * 64,
    )

    tail: list[ExcludedTailExpectation] = []
    for version, (kind, terminal) in enumerate(
        (("planner_call", True), ("solution_call", True), ("sham_planner_call", False)),
        start=1,
    ):
        operation_id = f"formal-op:discarded:{kind}:v{version:03d}"
        governor.reserve(
            operation_id=operation_id,
            cell_id=f"formal:{TAIL_INSTANCE}:A",
            operation_kind=kind,
            reservation=ResourceVector(model_calls=1),
        )
        started = governor.start(operation_id)
        operation_root = (
            root
            / "model-gateway/operations"
            / ("op-" + hashlib.sha256(operation_id.encode()).hexdigest())
        )
        operation_root.mkdir(parents=True)
        (operation_root / "prompt.txt").write_text(operation_id)
        if terminal:
            result = _canonical({"operation_id": operation_id, "result": "fixture"})
            (operation_root / "result.json").write_bytes(result)
            governor.complete(
                operation_id,
                actual_usage=ResourceVector(model_calls=1),
                artifact_sha256=hashlib.sha256(result).hexdigest(),
            )
            state = "completed"
        else:
            state = "started"
        tail.append(
            ExcludedTailExpectation(
                operation_id=operation_id,
                state=state,
                start_event_sha256=started.event_sha256,
            )
        )

    replay = journal.replay()
    ledger_path = root / "control/operations/operation_ledger.jsonl"
    anchor_path = root / "control/trusted-operation-head.json"
    spec = ContinuationSourceSpec(
        source_staging_plan_sha256=hashlib.sha256(staging).hexdigest(),
        source_code_revision=SOURCE_REVISION,
        prefix_instance_ids=PREFIX,
        prefix_receipt_sha256s=tuple(receipt_hashes),
        online_checkpoint_sha256=checkpoint.sha256,
        online_bank_sha256=bank.sha256,
        rule_registry_sha256=RULE_SHA,
        operation_event_count=replay.event_count,
        operation_head_sha256=replay.head_sha256,
        operation_journal_sha256=hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
        operation_anchor_sha256=hashlib.sha256(anchor_path.read_bytes()).hexdigest(),
        formal_ledger_sha256=hashlib.sha256(formal_raw).hexdigest(),
        formal_state_sha256=hashlib.sha256(formal_state_path.read_bytes()).hexdigest(),
        source_committed_usage=ResourceVector(model_calls=4),
        excluded_instance_id=TAIL_INSTANCE,
        excluded_tail_operations=tuple(tail),
    )
    return root, spec


def _v6_staging(snapshot, stream: list[dict]) -> bytes:
    cells = _cells(stream, start=6)
    suffix_totals = _totals(cells)
    composite = ResourceCaps(
        model_calls=1170,
        evaluator_transactions=576,
        cpu_evaluator_seconds=806400.0,
    )
    payload = {
        "schema_version": 6,
        "phase_id": "successor-v1r9",
        "code_revision": "1" * 40,
        "model_signature": {
            "executor_model": "fixture-model",
            "reasoning_effort": "high",
            "transport": "fake",
            "client_version": "fixture-2",
        },
        "execution_ready": True,
        "blockers": [],
        "source_hashes": {"fixture": "2" * 64},
        "budgets": suffix_totals.to_dict(),
        "resource_entitlement_totals": suffix_totals.to_dict(),
        "cell_entitlements": cells,
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "stream": stream,
        "experience_initialization": "successor_continuation",
        "online_instances_per_suite": 6,
        "sealed_instances_per_suite": 2,
        "validity_policy": {
            "rounds_per_arm": 8,
            "minimum_valid_rounds_per_arm": 4,
            "learning_tasks_per_suite": 6,
            "minimum_paired_learning_tasks": 5,
            "insufficient_status": "insufficient_validity",
            "score_aggregation": "valid_only_mean_and_best",
        },
        "continuation": {
            "source_manifest_sha256": snapshot.source_manifest_sha256,
            "source_snapshot_sha256": snapshot.sha256,
            "source_staging_plan_sha256": snapshot.source_staging_plan_sha256,
            "prefix_length": 6,
            "execution_window": {"start_index": 6, "stop_index": 24},
            "input_online_checkpoint_sha256": snapshot.online_checkpoint.sha256,
            "input_online_bank_sha256": snapshot.online_bank.sha256,
            "source_committed_usage": snapshot.source_committed_usage.to_dict(),
            "composite_hard_caps": composite.to_dict(),
            "excluded_consumed_tail_operation_ids": [
                item.operation_id for item in snapshot.excluded_consumed_tail
            ],
        },
        "qualification_transfer": {
            "receipt_sha256": "f" * 64,
            "passed": True,
            "model_calls_started": 0,
            "evaluator_transactions_started": 0,
            "formal_score_reuse": False,
        },
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    return _canonical(payload)


def test_prepare_is_double_read_content_addressed_and_verifiable(tmp_path: Path) -> None:
    source_root, spec = _source_fixture(tmp_path)
    output_root = tmp_path / "continuation"

    first = prepare_three_arm_continuation_source(
        source_root=source_root,
        output_root=output_root,
        spec=spec,
    )
    second = prepare_three_arm_continuation_source(
        source_root=source_root,
        output_root=output_root,
        spec=spec,
    )

    assert second == first
    assert first.snapshot.prefix_length == 6
    assert first.snapshot.next_stream_index == 6
    assert first.snapshot.online_checkpoint.sha256 == spec.online_checkpoint_sha256
    assert first.snapshot.online_bank.sha256 == spec.online_bank_sha256
    assert first.snapshot.record_source_instance_ids == PREFIX
    assert [item.state for item in first.snapshot.excluded_consumed_tail] == [
        "completed",
        "completed",
        "started",
    ]
    assert all(not item.learning_import for item in first.snapshot.excluded_consumed_tail)
    assert all(not item.performance_import for item in first.snapshot.excluded_consumed_tail)

    verified = verify_three_arm_continuation_source(
        source_root=source_root,
        manifest_path=first.manifest_path,
        snapshot_path=first.snapshot_path,
    )
    assert verified == first.snapshot
    guard = ThreeArmContinuationSourceGuard(
        source_root=source_root,
        manifest_path=first.manifest_path,
        snapshot_path=first.snapshot_path,
        expected_snapshot_sha256=first.snapshot.sha256,
    )
    assert guard() is None

    started = first.snapshot.excluded_consumed_tail[-1]
    result_path = source_root / started.result_relative_path
    result_path.write_bytes(b"late provider result\n")
    with pytest.raises(ValueError, match="started tail result must remain absent"):
        verify_three_arm_continuation_source(
            source_root=source_root,
            manifest_path=first.manifest_path,
            snapshot_path=first.snapshot_path,
        )


def test_prepare_accepts_production_v2_receipts_and_binds_nested_stream_item(
    tmp_path: Path,
) -> None:
    source_root, spec = _source_fixture(tmp_path, production_receipts=True)
    prepared = prepare_three_arm_continuation_source(
        source_root=source_root,
        output_root=tmp_path / "continuation",
        spec=spec,
    )
    assert tuple(
        item.instance_id for item in prepared.snapshot.prefix_instance_receipts
    ) == PREFIX

    receipt_path = next(
        (source_root / "formal/instances").glob("000-*/instance_receipt.json")
    )
    payload = json.loads(receipt_path.read_text())
    payload["stream_item"]["task_id"] = "rebound"
    receipt_path.write_bytes(_canonical(payload))
    rebound_spec = ContinuationSourceSpec(
        **{
            **spec.__dict__,
            "prefix_receipt_sha256s": (
                hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
                *spec.prefix_receipt_sha256s[1:],
            ),
        }
    )
    with pytest.raises(ValueError, match="stream item"):
        prepare_three_arm_continuation_source(
            source_root=source_root,
            output_root=tmp_path / "rebound",
            spec=rebound_spec,
        )


def test_source_prepare_rejects_prefix_bank_or_budget_drift(tmp_path: Path) -> None:
    source_root, spec = _source_fixture(tmp_path)
    bad = ContinuationSourceSpec(
        **{
            **spec.__dict__,
            "source_committed_usage": ResourceVector(model_calls=3),
        }
    )
    with pytest.raises(ValueError, match="committed usage"):
        prepare_three_arm_continuation_source(
            source_root=source_root,
            output_root=tmp_path / "bad-budget",
            spec=bad,
        )

    bank_path = source_root / f"formal/experience_banks/{spec.online_bank_sha256}.json"
    payload = json.loads(bank_path.read_text())
    payload["records"][0]["source_instance_id"] = TAIL_INSTANCE
    bank_path.write_bytes(_canonical(payload))
    with pytest.raises(ValueError, match="online Bank content hash"):
        prepare_three_arm_continuation_source(
            source_root=source_root,
            output_root=tmp_path / "bad-bank",
            spec=spec,
        )


def test_v6_contract_executes_only_suffix_and_debits_source_budget(tmp_path: Path) -> None:
    source_root, spec = _source_fixture(tmp_path)
    prepared = prepare_three_arm_continuation_source(
        source_root=source_root,
        output_root=tmp_path / "continuation",
        spec=spec,
    )
    stream = _full_stream()
    encoded = _v6_staging(prepared.snapshot, stream)

    contract = ThreeArmContinuationContract.from_staging_bytes(
        encoded,
        source_snapshot=prepared.snapshot,
    )

    assert contract.execution_start_index == 6
    assert contract.execution_stop_index == 24
    assert contract.active_stream == contract.stream[6:]
    assert len(contract.active_stream) == 18
    assert len(contract.cell_entitlements) == 66  # 54 arms + 12 distillations
    assert contract.source_committed_usage == ResourceVector(model_calls=4)
    assert contract.composite_hard_caps.model_calls == 1170
    assert contract.suffix_entitlement_totals.model_calls == 876

    payload = json.loads(encoded)
    payload["cell_entitlements"][f"formal:{PREFIX[0]}:A"] = ResourceCaps(
        model_calls=16, evaluator_transactions=8, cpu_evaluator_seconds=11200.0
    ).to_dict()
    payload["resource_entitlement_totals"]["model_calls"] += 16
    payload["resource_entitlement_totals"]["evaluator_transactions"] += 8
    payload["resource_entitlement_totals"]["cpu_evaluator_seconds"] += 11200.0
    payload["budgets"] = payload["resource_entitlement_totals"]
    with pytest.raises(ValueError, match="active suffix"):
        ThreeArmContinuationContract.from_staging_bytes(
            _canonical(payload), source_snapshot=prepared.snapshot
        )

    payload = json.loads(encoded)
    payload["continuation"]["input_online_bank_sha256"] = "9" * 64
    with pytest.raises(ValueError, match="online Bank"):
        ThreeArmContinuationContract.from_staging_bytes(
            _canonical(payload), source_snapshot=prepared.snapshot
        )


def test_v6_contract_rejects_prefix_or_composite_cap_rebinding(tmp_path: Path) -> None:
    source_root, spec = _source_fixture(tmp_path)
    prepared = prepare_three_arm_continuation_source(
        source_root=source_root,
        output_root=tmp_path / "continuation",
        spec=spec,
    )
    encoded = _v6_staging(prepared.snapshot, _full_stream())

    payload = json.loads(encoded)
    payload["stream"][0]["task_id"] = "changed"
    payload["stream"][0]["instance_id"] = "suite-a:changed"
    with pytest.raises(ValueError, match="source prefix"):
        ThreeArmContinuationContract.from_staging_bytes(
            _canonical(payload), source_snapshot=prepared.snapshot
        )

    payload = json.loads(encoded)
    payload["continuation"]["composite_hard_caps"]["model_calls"] = 879
    with pytest.raises(ValueError, match="composite model_calls"):
        ThreeArmContinuationContract.from_staging_bytes(
            _canonical(payload), source_snapshot=prepared.snapshot
        )
