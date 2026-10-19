from __future__ import annotations

import hashlib
import json
import os
import shutil
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import ResourceCaps, ResourceVector
from optimization_lab.harness_builder.three_arm import THREE_ARMS, ThreeArmStreamItem
from optimization_lab.harness_builder.three_arm_composition import (
    SOURCE_PREFIX_SEGMENT_ID,
    SUCCESSOR_SUFFIX_SEGMENT_ID,
    build_three_arm_composition_payload,
    prepare_verified_three_arm_composition_manifest,
)
from optimization_lab.harness_builder.three_arm_continuation import (
    ArtifactBinding,
    ExcludedTailBinding,
    OperationJournalBinding,
    PrefixReceiptBinding,
    ThreeArmContinuationContract,
    ThreeArmContinuationSourceSnapshot,
)
from optimization_lab.harness_builder.three_arm_report import (
    generate_three_arm_composite_report,
)


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _write(path: Path, payload: object) -> str:
    raw = _canonical(payload)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def _stream() -> tuple[ThreeArmStreamItem, ...]:
    suites = ("yahpo-lcbench", "compilergym-cbench", "swebench-verified")
    result: list[ThreeArmStreamItem] = []
    for stream_index in range(24):
        block = stream_index // 3
        offset = block % 3
        suite = (suites[offset:] + suites[:offset])[stream_index % 3]
        task_id = f"task-{suite}-{block}"
        result.append(
            ThreeArmStreamItem(
                stream_index=stream_index,
                block_index=block,
                suite=suite,
                task_id=task_id,
                arm_order=(
                    THREE_ARMS[stream_index % 3 :]
                    + THREE_ARMS[: stream_index % 3]
                ),
                learning_mode="online" if block < 6 else "sealed",
            )
        )
    return tuple(result)


def _write_sealed_receipt(
    root: Path,
    *,
    directory_name: str,
    item: ThreeArmStreamItem,
    phase_id: str,
    staging_sha: str,
) -> Path:
    instance_root = root / "formal" / "instances" / directory_name
    task_binding = hashlib.sha256(item.instance_id.encode()).hexdigest()
    arm_hashes: dict[str, str] = {}
    for arm in THREE_ARMS:
        rounds = [
            {
                "version": f"v{index:03d}",
                "correct": True,
                "score": float(item.stream_index + index),
            }
            for index in range(1, 9)
        ]
        arm_payload = {
            "schema_version": 1,
            "staging_plan_sha256": staging_sha,
            "stream_index": item.stream_index,
            "instance_id": item.instance_id,
            "arm": arm,
            "cell_id": f"formal:{item.suite}:{item.task_id}:{arm}",
            "task_binding_sha256": task_binding,
            "builder_checkpoint_sha256": "1" * 64,
            "experience_bank_sha256": None if arm == "A" else "2" * 64,
            "cross_instance_record_ids": [],
            "round_event_ids": [f"event-{index}" for index in range(1, 9)],
            "round_sha256s": {
                f"v{index:03d}": f"{index}" * 64 for index in range(1, 9)
            },
            "curve": {"rounds": rounds},
            "sealed": True,
        }
        arm_hashes[arm] = _write(instance_root / "arms" / f"{arm}.json", arm_payload)
    receipt = {
        "schema_version": 2,
        "phase_id": phase_id,
        "staging_plan_sha256": staging_sha,
        "stream_item": item.to_dict(),
        "learning_mode": item.learning_mode,
        "first_encounter": True,
        "same_instance_rerun_policy": "replay_only_no_formal_update",
        "task_binding_sha256": task_binding,
        "input_online_checkpoint_sha256": "3" * 64,
        "input_online_bank_sha256": "4" * 64,
        "arm_order": list(item.arm_order),
        "arm_receipt_sha256s": arm_hashes,
        "trajectory_sha256": "5" * 64,
        "distillation_operation_id": (
            f"distill:{item.stream_index:03d}:{item.instance_id}:distillation_call"
            if item.learning_mode == "online"
            else None
        ),
        "output_online_bank_sha256": "6" * 64,
        "output_online_checkpoint_sha256": "7" * 64,
        "sealed": True,
        "no_next_phase": True,
    }
    _write(instance_root / "instance_receipt.json", receipt)
    return instance_root / "instance_receipt.json"


def _fixture(tmp_path: Path, *, pretty_source_staging: bool = False):
    source_root = tmp_path / "v1r8"
    successor_root = tmp_path / "v1r9"
    stream = _stream()
    if pretty_source_staging:
        source_staging_raw = (
            json.dumps({"phase_id": "v1r8-source"}, indent=2) + "\n"
        ).encode("utf-8")
        source_staging_path = source_root / "staging_plan.json"
        source_staging_path.parent.mkdir(parents=True, exist_ok=True)
        source_staging_path.write_bytes(source_staging_raw)
        source_staging_sha = hashlib.sha256(source_staging_raw).hexdigest()
    else:
        source_staging_sha = _write(
            source_root / "staging_plan.json", {"phase_id": "v1r8-source"}
        )
    successor_staging_sha = "9" * 64

    prefix: list[PrefixReceiptBinding] = []
    for index, item in enumerate(stream[:6]):
        # Directory names intentionally do not encode the stream index.
        path = _write_sealed_receipt(
            source_root,
            directory_name=f"prefix-node-{5 - index}",
            item=item,
            phase_id="v1r8-source",
            staging_sha=source_staging_sha,
        )
        prefix.append(
            PrefixReceiptBinding(
                relative_path=path.relative_to(source_root).as_posix(),
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                stream_index=index,
                instance_id=item.instance_id,
            )
        )

    successor_paths: dict[int, Path] = {}
    for item in reversed(stream[6:]):
        path = _write_sealed_receipt(
            successor_root,
            directory_name=f"opaque-node-{100 - item.stream_index}",
            item=item,
            phase_id="v1r9-successor",
            staging_sha=successor_staging_sha,
        )
        successor_paths[item.stream_index] = path

    tails = (
        ExcludedTailBinding(
            operation_id="formal-op:scikit:planner:v001",
            cell_id="formal:swebench-verified:scikit-learn-14983:A",
            operation_kind="planner_call",
            state="completed",
            start_event_sha256="a" * 64,
            charged_usage=ResourceVector(model_calls=1),
            operation_artifacts=(ArtifactBinding("tail/prompt.json", "b" * 64),),
            result_relative_path="tail/result.json",
            result_absent=False,
        ),
        ExcludedTailBinding(
            operation_id="formal-op:scikit:solution:v002",
            cell_id="formal:swebench-verified:scikit-learn-14983:A",
            operation_kind="solution_call",
            state="started",
            start_event_sha256="c" * 64,
            charged_usage=ResourceVector(model_calls=1),
            operation_artifacts=(ArtifactBinding("tail/schema.json", "d" * 64),),
            result_relative_path="tail/missing-result.json",
            result_absent=True,
        ),
    )
    snapshot = ThreeArmContinuationSourceSnapshot(
        source_manifest_sha256="e" * 64,
        source_staging_plan_sha256=source_staging_sha,
        source_code_revision="f" * 40,
        prefix_instance_receipts=tuple(prefix),
        operation_journal=OperationJournalBinding(
            relative_path="control/operation-ledger.jsonl",
            sha256="1" * 64,
            event_count=10,
            head_sha256="2" * 64,
        ),
        formal_ledger=ArtifactBinding("formal/ledger.jsonl", "3" * 64),
        online_checkpoint=ArtifactBinding("formal/checkpoint.json", "4" * 64),
        online_bank=ArtifactBinding("formal/bank.json", "5" * 64),
        rule_registry_sha256="6" * 64,
        learned_through_instance=stream[5].instance_id,
        record_source_instance_ids=tuple(item.instance_id for item in stream[:6]),
        source_committed_usage=ResourceVector(
            model_calls=10, evaluator_transactions=4, cpu_evaluator_seconds=12
        ),
        excluded_instance_id="swebench-verified:scikit-learn-14983",
        excluded_consumed_tail=tails,
    )
    contract = ThreeArmContinuationContract(
        staging_plan_sha256=successor_staging_sha,
        phase_id="v1r9-successor",
        model="model",
        execution_ready=True,
        blockers=(),
        stream=stream,
        execution_start_index=6,
        execution_stop_index=24,
        suffix_global_caps=ResourceCaps(),
        suffix_entitlement_totals=ResourceCaps(),
        cell_entitlements={},
        source_snapshot_sha256=snapshot.sha256,
        source_manifest_sha256=snapshot.source_manifest_sha256,
        source_staging_plan_sha256=snapshot.source_staging_plan_sha256,
        input_online_checkpoint_sha256=snapshot.online_checkpoint.sha256,
        input_online_bank_sha256=snapshot.online_bank.sha256,
        source_committed_usage=snapshot.source_committed_usage,
        composite_hard_caps=ResourceCaps(),
        qualification_transfer_sha256="7" * 64,
        excluded_consumed_tail_operation_ids=tuple(
            tail.operation_id for tail in snapshot.excluded_consumed_tail
        ),
    )
    return source_root, successor_root, snapshot, contract, successor_paths


def test_composition_is_cas_references_only_and_uses_nested_stream_indices(
    tmp_path: Path,
) -> None:
    source_root, successor_root, snapshot, contract, _paths = _fixture(tmp_path)
    outcome = prepare_verified_three_arm_composition_manifest(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=snapshot,
        successor_contract=contract,
        output_root=tmp_path / "output",
    )
    repeated = prepare_verified_three_arm_composition_manifest(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=snapshot,
        successor_contract=contract,
        output_root=tmp_path / "output",
    )

    assert repeated.manifest_path == outcome.manifest_path
    assert outcome.manifest_path.stem == outcome.manifest_sha256
    assert hashlib.sha256(outcome.manifest_path.read_bytes()).hexdigest() == (
        outcome.manifest_sha256
    )
    assert os.stat(outcome.manifest_path).st_mode & 0o777 == 0o444
    assert outcome.payload["segments"] == [
        {"segment_id": SOURCE_PREFIX_SEGMENT_ID, "role": "source_prefix"},
        {"segment_id": SUCCESSOR_SUFFIX_SEGMENT_ID, "role": "successor_suffix"},
    ]
    entries = outcome.payload["instances"]
    assert [entry["stream_index"] for entry in entries] == list(range(24))
    assert [entry["source_segment"] for entry in entries[:6]] == [
        SOURCE_PREFIX_SEGMENT_ID
    ] * 6
    assert [entry["source_segment"] for entry in entries[6:]] == [
        SUCCESSOR_SUFFIX_SEGMENT_ID
    ] * 18
    assert all(set(entry) == {"stream_index", "source_segment", "instance_receipt"} for entry in entries)
    assert not (tmp_path / "output" / "formal").exists()

    audits = outcome.payload["excluded_consumed_tail"]
    assert [item["operation_id"] for item in audits] == [
        tail.operation_id for tail in snapshot.excluded_consumed_tail
    ]
    assert [item["charged_usage"]["model_calls"] for item in audits] == [1, 1]
    assert all(item["learning_import"] is False for item in audits)
    assert all(item["performance_import"] is False for item in audits)
    summary = generate_three_arm_composite_report(
        composition_manifest_path=outcome.manifest_path,
        segment_roots=outcome.segment_roots,
        output_root=tmp_path / "report",
    )
    assert summary["task_count"] == 24
    assert len((tmp_path / "report" / "results.csv").read_text().splitlines()) == 73


def test_composition_accepts_exactly_bound_pretty_source_staging_plan(
    tmp_path: Path,
) -> None:
    source_root, successor_root, snapshot, contract, _paths = _fixture(
        tmp_path, pretty_source_staging=True
    )

    payload = build_three_arm_composition_payload(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=snapshot,
        successor_contract=contract,
    )

    assert len(payload["instances"]) == 24


@pytest.mark.parametrize("failure", ["missing", "duplicate", "unsealed", "arm-drift"])
def test_composition_fails_closed_on_incomplete_duplicate_or_drifted_suffix(
    tmp_path: Path, failure: str
) -> None:
    source_root, successor_root, snapshot, contract, paths = _fixture(tmp_path)
    target = paths[10]
    if failure == "missing":
        target.unlink()
    elif failure == "duplicate":
        shutil.copytree(target.parent, target.parent.parent / "duplicate-index-ten")
    elif failure == "unsealed":
        payload = json.loads(target.read_bytes())
        payload["sealed"] = False
        target.write_bytes(_canonical(payload))
    else:
        receipt = json.loads(target.read_bytes())
        arm_path = target.parent / "arms" / "A.json"
        arm = json.loads(arm_path.read_bytes())
        arm["curve"]["rounds"][0]["score"] = -1.0
        arm_path.write_bytes(_canonical(arm))
        assert receipt["arm_receipt_sha256s"]["A"] != hashlib.sha256(
            arm_path.read_bytes()
        ).hexdigest()

    with pytest.raises(ValueError):
        build_three_arm_composition_payload(
            source_root=source_root,
            successor_root=successor_root,
            source_snapshot=snapshot,
            successor_contract=contract,
        )


def test_composition_rejects_prefix_receipt_hash_drift(tmp_path: Path) -> None:
    source_root, successor_root, snapshot, contract, _paths = _fixture(tmp_path)
    target = source_root / snapshot.prefix_instance_receipts[0].relative_path
    payload = json.loads(target.read_bytes())
    payload["sealed"] = False
    target.write_bytes(_canonical(payload))

    with pytest.raises(ValueError, match="hash differs"):
        build_three_arm_composition_payload(
            source_root=source_root,
            successor_root=successor_root,
            source_snapshot=snapshot,
            successor_contract=contract,
        )


def test_composition_cas_refuses_existing_digest_rebinding(tmp_path: Path) -> None:
    source_root, successor_root, snapshot, contract, _paths = _fixture(tmp_path)
    outcome = prepare_verified_three_arm_composition_manifest(
        source_root=source_root,
        successor_root=successor_root,
        source_snapshot=snapshot,
        successor_contract=contract,
        output_root=tmp_path / "output",
    )
    outcome.manifest_path.chmod(0o644)
    outcome.manifest_path.write_bytes(b"{}\n")

    with pytest.raises(ValueError, match="already rebound"):
        prepare_verified_three_arm_composition_manifest(
            source_root=source_root,
            successor_root=successor_root,
            source_snapshot=snapshot,
            successor_contract=contract,
            output_root=tmp_path / "output",
        )
