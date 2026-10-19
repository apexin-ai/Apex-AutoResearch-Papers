from __future__ import annotations

from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.factorial_coverage import (
    ExactFactorialAttemptMatrix,
)
from optimization_lab.harness_builder.factorial_operation_schedule import (
    ExactFactorialOperationSchedule,
)
from optimization_lab.harness_builder.factorial_stage_disposition import (
    BLOCKERS,
    CLAIM_SCOPE,
    FactorialSemanticDispositionVerifier,
    FactorialStageDispositionError,
    JOURNAL_STORAGE_STATUS,
    STANDALONE_VIEW_STATUS,
    SemanticJournalOperationReceipt,
    SemanticSkippedByParentReceipt,
    ExactSemanticDispositionSeal,
    derive_exact_semantic_artifact,
    verify_serialized_exact_semantic_artifact,
)
from optimization_lab.harness_builder.factorial_task_authority import (
    FactorialTaskArtifactAuthority,
)


_AGENT = Path(
    os.environ.get(
        "MOSS_TEST_AGENTHPO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/agenthpobench",
    )
)
_GDP = Path(
    os.environ.get(
        "MOSS_TEST_GDPEVO_CHECKOUT",
        "/tmp/moss-bench-qual.rYRM8Q/gdpevo",
    )
)
_ZERO = "0" * 64


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def _sha(payload: object) -> str:
    return hashlib.sha256(_canonical(payload).rstrip(b"\n")).hexdigest()


@pytest.fixture(scope="module")
def exact():
    if not _AGENT.is_dir() or not _GDP.is_dir():
        pytest.skip("pinned factorial benchmark checkouts are unavailable")
    authority = FactorialTaskArtifactAuthority(
        agenthpo_checkout=_AGENT,
        gdpevo_checkout=_GDP,
    )
    bundle = authority.rederive_exact_bundle()
    plan = authority.build_formal_zero_call_plan(authority.derived_contexts())
    matrix = ExactFactorialAttemptMatrix.from_verified_sources(
        plan=plan,
        bundle=bundle,
        task_authority=authority,
    )
    schedule = ExactFactorialOperationSchedule.from_verified_sources(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=authority,
    )
    return authority, bundle, plan, matrix, schedule


def _write_terminal_journal(
    root: Path,
    operations,
    *,
    state_for=None,
    extra=None,
) -> tuple[Path, Path]:
    ledger = root / "operation_ledger.jsonl"
    anchor = root / "trusted-head.json"
    root.mkdir(parents=True, exist_ok=True)
    events: list[bytes] = []
    sequence = 0
    previous = _ZERO
    selected = list(operations)
    if extra is not None:
        selected.append(extra)
    for operation in selected:
        state = "failed" if state_for is None else state_for(operation)
        for event_type in (
            "operation_reserved",
            "operation_started",
            "operation_completed" if state == "completed" else "operation_failed",
        ):
            sequence += 1
            if event_type == "operation_reserved":
                payload = {
                    "reservation": operation.full_path_reservation.to_dict()
                }
            elif event_type == "operation_started":
                payload = {}
            else:
                payload = {
                    "actual_usage": operation.full_path_reservation.to_dict(),
                    "artifact_sha256": hashlib.sha256(
                        (operation.logical_operation_id + ":artifact").encode()
                    ).hexdigest(),
                    "usage_known": True,
                }
                if event_type == "operation_failed":
                    payload["reason_code"] = "fixture_terminal_failure"
            core = {
                "cell_id": operation.cell_id,
                "event_id": "evt:"
                + hashlib.sha256(
                    f"{operation.logical_operation_id}|{event_type}".encode()
                ).hexdigest(),
                "event_type": event_type,
                "operation_id": operation.logical_operation_id,
                "operation_kind": operation.journal_operation_kind,
                "payload": payload,
                "prev_event_sha256": previous,
                "recorded_at": datetime(2026, 8, 13, tzinfo=timezone.utc).isoformat(),
                "schema_version": 1,
                "sequence": sequence,
            }
            previous = _sha(core)
            events.append(_canonical({**core, "event_sha256": previous}))
    ledger.write_bytes(b"".join(events))
    anchor.write_bytes(
        _canonical(
            {
                "event_count": sequence,
                "head_sha256": previous,
                "schema_version": 1,
            }
        )
    )
    return ledger, anchor


def _verifier(exact, ledger: Path, anchor: Path):
    authority, bundle, plan, matrix, _schedule = exact
    return FactorialSemanticDispositionVerifier.from_verified_sources(
        matrix=matrix,
        plan=plan,
        bundle=bundle,
        task_authority=authority,
        ledger_path=ledger,
        anchor_path=anchor,
    )


def test_small_semantic_chain_accepts_completed_then_failed_then_skip(
    exact, tmp_path: Path
) -> None:
    schedule = exact[4]
    attempt = schedule.operations[0].attempt_id
    chain = tuple(item for item in schedule.operations if item.attempt_id == attempt)
    assert [item.stage for item in chain] == ["update", "solution", "evaluator"]
    ledger, anchor = _write_terminal_journal(
        tmp_path,
        chain[:2],
        state_for=lambda item: (
            "completed" if item.stage == "update" else "failed"
        ),
    )
    verifier = _verifier(exact, ledger, anchor)

    update = verifier.executed(chain[0].logical_operation_id)
    solution = verifier.executed(chain[1].logical_operation_id)
    evaluator = verifier.skipped_by_parent(
        chain[2].logical_operation_id,
        parent=solution,
    )

    assert update.journal_state == "completed"
    assert solution.journal_state == "failed"
    assert evaluator.proof_kind == "PARENT_OPERATION_FAILED"
    assert update.execution_authority == "NOT_GRANTED"
    assert update.formal_readiness == "NOT_READY"
    assert update.claim_scope == CLAIM_SCOPE
    assert update.journal_storage_status == JOURNAL_STORAGE_STATUS


def test_completed_operation_without_artifact_cannot_advance(
    exact, tmp_path: Path
) -> None:
    operation = exact[4].operations[0]
    ledger, anchor = _write_terminal_journal(
        tmp_path,
        (operation,),
        state_for=lambda _item: "completed",
    )
    lines = ledger.read_text(encoding="utf-8").splitlines()
    terminal = json.loads(lines[-1])
    terminal["payload"]["artifact_sha256"] = None
    terminal_core = {
        key: value for key, value in terminal.items() if key != "event_sha256"
    }
    terminal["event_sha256"] = _sha(terminal_core)
    lines[-1] = json.dumps(
        terminal,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    anchor.write_bytes(
        _canonical(
            {
                "event_count": 3,
                "head_sha256": terminal["event_sha256"],
                "schema_version": 1,
            }
        )
    )
    verifier = _verifier(exact, ledger, anchor)
    with pytest.raises(FactorialStageDispositionError, match="without an artifact"):
        verifier.executed(operation.logical_operation_id)


def test_failed_root_cascades_only_through_immediate_parents(
    exact, tmp_path: Path
) -> None:
    schedule = exact[4]
    attempt = schedule.operations[0].attempt_id
    chain = tuple(item for item in schedule.operations if item.attempt_id == attempt)
    ledger, anchor = _write_terminal_journal(tmp_path, chain[:1])
    verifier = _verifier(exact, ledger, anchor)
    update = verifier.executed(chain[0].logical_operation_id)
    solution = verifier.skipped_by_parent(
        chain[1].logical_operation_id,
        parent=update,
    )
    evaluator = verifier.skipped_by_parent(
        chain[2].logical_operation_id,
        parent=solution,
    )
    assert solution.proof_kind == "PARENT_OPERATION_FAILED"
    assert evaluator.proof_kind == "PARENT_SKIPPED_BY_PARENT"

    with pytest.raises(FactorialStageDispositionError, match="immediate"):
        verifier.skipped_by_parent(
            chain[2].logical_operation_id,
            parent=update,
        )


def test_root_cannot_skip_and_completed_parent_needs_typed_gate_receipt(
    exact, tmp_path: Path
) -> None:
    schedule = exact[4]
    first_attempt = schedule.operations[0].attempt_id
    chain = tuple(
        item for item in schedule.operations if item.attempt_id == first_attempt
    )
    ledger, anchor = _write_terminal_journal(
        tmp_path,
        chain[:1],
        state_for=lambda _item: "completed",
    )
    verifier = _verifier(exact, ledger, anchor)
    update = verifier.executed(chain[0].logical_operation_id)

    with pytest.raises(FactorialStageDispositionError, match="typed gate"):
        verifier.skipped_by_parent(
            chain[1].logical_operation_id,
            parent=update,
        )

    fixed = next(
        item
        for item in schedule.operations
        if item.arm_id == "A-fixed-feedback" and item.stage == "solution"
    )
    forged_parent = replace(
        update,
        potential_operation_sha256=fixed.sha256,
        logical_operation_id=fixed.logical_operation_id,
        observed_journal_operation_id=fixed.logical_operation_id,
        stage=fixed.stage,
    )
    with pytest.raises(FactorialStageDispositionError, match="not issued"):
        verifier.skipped_by_parent(
            fixed.logical_operation_id,
            parent=forged_parent,
        )


def test_semantic_receipts_reject_started_reserved_rebound_and_extra_operations(
    exact, tmp_path: Path
) -> None:
    operation = exact[4].operations[0]

    # A started-only prefix is not an abandoned-operation proof.
    terminal_ledger, terminal_anchor = _write_terminal_journal(
        tmp_path / "started-source", (operation,)
    )
    lines = terminal_ledger.read_bytes().splitlines(keepends=True)
    terminal_ledger.write_bytes(b"".join(lines[:2]))
    started = [json.loads(line) for line in lines[:2]]
    terminal_anchor.write_bytes(
        _canonical(
            {
                "event_count": 2,
                "head_sha256": started[-1]["event_sha256"],
                "schema_version": 1,
            }
        )
    )
    verifier = _verifier(exact, terminal_ledger, terminal_anchor)
    with pytest.raises(FactorialStageDispositionError, match="reserved/started"):
        verifier.executed(operation.logical_operation_id)

    # A caller cannot turn the same logical record into a physical retry.
    ledger, anchor = _write_terminal_journal(tmp_path / "retry", (operation,))
    verifier = _verifier(exact, ledger, anchor)
    receipt = verifier.executed(operation.logical_operation_id)
    with pytest.raises(FactorialStageDispositionError, match="logical/physical"):
        replace(
            receipt,
            observed_journal_operation_id=receipt.logical_operation_id
            + ":attempt-0002",
        )

    class Extra:
        logical_operation_id = "factorial-extra:operation"
        cell_id = operation.cell_id
        journal_operation_kind = operation.journal_operation_kind
        full_path_reservation = ResourceVector(model_calls=1)

    extra_ledger, extra_anchor = _write_terminal_journal(
        tmp_path / "extra", (operation,), extra=Extra()
    )
    with pytest.raises(FactorialStageDispositionError, match="outside"):
        _verifier(exact, extra_ledger, extra_anchor)


def test_full_4338_semantic_exact_set_uses_single_replay_and_stays_not_ready(
    exact, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import optimization_lab.harness_builder.factorial_stage_disposition as module

    schedule = exact[4]
    by_attempt: dict[str, list[object]] = {}
    for operation in schedule.operations:
        by_attempt.setdefault(operation.attempt_id, []).append(operation)
    roots = tuple(items[0] for items in by_attempt.values())
    assert len(roots) == 1566
    ledger, anchor = _write_terminal_journal(tmp_path, roots)
    calls = 0
    real_verify = module.verify_operation_journal

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return real_verify(*args, **kwargs)

    monkeypatch.setattr(module, "verify_operation_journal", counted)
    verifier = _verifier(exact, ledger, anchor)
    dispositions = []
    current: dict[str, object] = {}
    for operation in verifier.potential_operations:
        if operation.stage == by_attempt[operation.attempt_id][0].stage:
            receipt = verifier.executed(operation.logical_operation_id)
        else:
            receipt = verifier.skipped_by_parent(
                operation.logical_operation_id,
                parent=current[operation.attempt_id],
            )
        current[operation.attempt_id] = receipt
        dispositions.append(receipt)
    seal = verifier.seal(dispositions)

    assert calls == 1
    assert seal.potential_stage_count == 4338
    assert seal.executed_count == seal.terminal_failed_count == 1566
    assert seal.terminal_completed_count == 0
    assert seal.skipped_by_parent_count == 2772
    assert seal.exact_disposition_set_complete is True
    assert seal.semantic_journal_operation_set_exact is True
    assert seal.formal_execution_ready is False
    assert seal.formal_readiness == "NOT_READY"
    assert seal.execution_authority == "NOT_GRANTED"
    assert seal.standalone_view_status == STANDALONE_VIEW_STATUS
    assert seal.blockers == BLOCKERS
    assert seal.model_call_entitlement == 0
    assert seal.evaluator_transaction_entitlement == 0

    with pytest.raises(TypeError):
        verifier._replay.operations["forged"] = object()  # type: ignore[index]


def test_full_exact_set_accepts_one_complete_success_chain_among_failed_roots(
    exact, tmp_path: Path
) -> None:
    schedule = exact[4]
    by_attempt: dict[str, list[object]] = {}
    for operation in schedule.operations:
        by_attempt.setdefault(operation.attempt_id, []).append(operation)
    first_attempt = schedule.operations[0].attempt_id
    selected = []
    for attempt_id, chain in by_attempt.items():
        selected.extend(chain if attempt_id == first_attempt else chain[:1])
    ledger, anchor = _write_terminal_journal(
        tmp_path,
        selected,
        state_for=lambda item: (
            "completed" if item.attempt_id == first_attempt else "failed"
        ),
    )
    artifact = _verifier(exact, ledger, anchor).derive_exact_artifact()
    assert artifact.seal.terminal_completed_count == 3
    assert artifact.seal.terminal_failed_count == 1565
    assert artifact.seal.skipped_by_parent_count == 2770
    first_receipts = tuple(
        receipt
        for operation, receipt in zip(schedule.operations, artifact.receipts)
        if operation.attempt_id == first_attempt
    )
    assert len(first_receipts) == 3
    assert all(
        isinstance(receipt, SemanticJournalOperationReceipt)
        and receipt.journal_state == "completed"
        for receipt in first_receipts
    )


def test_full_seal_rejects_missing_duplicate_rehash_and_executed_after_failed(
    exact, tmp_path: Path
) -> None:
    schedule = exact[4]
    by_attempt: dict[str, list[object]] = {}
    for operation in schedule.operations:
        by_attempt.setdefault(operation.attempt_id, []).append(operation)
    roots = tuple(items[0] for items in by_attempt.values())
    ledger, anchor = _write_terminal_journal(tmp_path / "valid", roots)
    verifier = _verifier(exact, ledger, anchor)
    dispositions = []
    current: dict[str, object] = {}
    for operation in verifier.potential_operations:
        if operation.logical_operation_id == (
            by_attempt[operation.attempt_id][0].logical_operation_id
        ):
            receipt = verifier.executed(operation.logical_operation_id)
        else:
            receipt = verifier.skipped_by_parent(
                operation.logical_operation_id,
                parent=current[operation.attempt_id],
            )
        current[operation.attempt_id] = receipt
        dispositions.append(receipt)

    with pytest.raises(FactorialStageDispositionError, match="4,338"):
        verifier.seal(dispositions[:-1])
    with pytest.raises(FactorialStageDispositionError, match="repeat"):
        verifier.seal(dispositions[:-1] + [dispositions[0]])

    forged = replace(
        dispositions[0],
        terminal_artifact_sha256="f" * 64,
    )
    with pytest.raises(FactorialStageDispositionError, match="not issued"):
        verifier.seal([forged, *dispositions[1:]])

    with pytest.raises(FactorialStageDispositionError, match="not issued"):
        verifier.seal(
            [replace(dispositions[0]), *dispositions[1:]]
        )

    seal = verifier.seal(dispositions)
    with pytest.raises(FactorialStageDispositionError, match="pinned replay"):
        ExactSemanticDispositionSeal(
            **{
                name: getattr(seal, name)
                for name in seal.__dataclass_fields__
            }
        )

    with pytest.raises((FactorialStageDispositionError, TypeError)):
        replace(seal, schedule_sha256="f" * 64)

    # A failed parent may not coexist with an executed child, even before a
    # complete 4,338-row seal is attempted.
    first_chain = by_attempt[schedule.operations[0].attempt_id]
    rebound_ledger, rebound_anchor = _write_terminal_journal(
        tmp_path / "failed-parent-child", first_chain[:2]
    )
    rebound = _verifier(exact, rebound_ledger, rebound_anchor)
    failed_parent = rebound.executed(first_chain[0].logical_operation_id)
    assert failed_parent.journal_state == "failed"
    with pytest.raises(FactorialStageDispositionError, match="failed|nonterminal"):
        rebound.executed(first_chain[1].logical_operation_id)


def test_replay_payload_is_deep_frozen_and_preexisting_mutation_is_rejected(
    exact, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import optimization_lab.harness_builder.factorial_stage_disposition as module

    operation = exact[4].operations[0]
    ledger, anchor = _write_terminal_journal(
        tmp_path / "frozen", (operation,), state_for=lambda _item: "completed"
    )
    captured = None
    real_verify = module.verify_operation_journal

    def capture(*args, **kwargs):
        nonlocal captured
        captured = real_verify(*args, **kwargs)
        return captured

    monkeypatch.setattr(module, "verify_operation_journal", capture)
    verifier = _verifier(exact, ledger, anchor)
    original = verifier.executed(operation.logical_operation_id)
    assert captured is not None
    captured.operations[operation.logical_operation_id].events[-1].payload[
        "artifact_sha256"
    ] = "f" * 64
    captured.operations[operation.logical_operation_id].events[-1].payload[
        "usage_known"
    ] = False
    repeated = verifier.executed(operation.logical_operation_id)
    assert repeated is original
    assert repeated.terminal_artifact_sha256 == original.terminal_artifact_sha256
    assert repeated.usage_known is True

    raw_replay = real_verify(ledger, anchor_path=anchor)
    raw_replay.operations[operation.logical_operation_id].events[-1].payload[
        "artifact_sha256"
    ] = "e" * 64
    with pytest.raises(FactorialStageDispositionError, match="changed"):
        module.FactorialSemanticDispositionVerifier(
            schedule=exact[4],
            replay=raw_replay,
            _trusted_source_replay=module._TRUSTED_SOURCE_REPLAY,
        )


def _interleaved_completed_chain(
    exact,
    root: Path,
    *,
    start_child_before_parent_terminal: bool,
):
    schedule = exact[4]
    attempt = schedule.operations[0].attempt_id
    parent, child = tuple(
        item for item in schedule.operations if item.attempt_id == attempt
    )[:2]
    journal = OperationJournal(
        root,
        anchor_path=root.parent / (root.name + "-head.json"),
    )
    total = parent.full_path_reservation + child.full_path_reservation
    governor = ResourceGovernor(
        journal=journal,
        global_caps=ResourceCaps(**total.to_dict()),
        cell_caps={parent.cell_id: ResourceCaps(**total.to_dict())},
    )
    governor.reserve(
        operation_id=parent.logical_operation_id,
        cell_id=parent.cell_id,
        operation_kind=parent.journal_operation_kind,
        reservation=parent.full_path_reservation,
    )
    governor.start(parent.logical_operation_id)
    governor.reserve(
        operation_id=child.logical_operation_id,
        cell_id=child.cell_id,
        operation_kind=child.journal_operation_kind,
        reservation=child.full_path_reservation,
    )
    if start_child_before_parent_terminal:
        governor.start(child.logical_operation_id)
    governor.complete(
        parent.logical_operation_id,
        actual_usage=parent.full_path_reservation,
        artifact_sha256="a" * 64,
    )
    if not start_child_before_parent_terminal:
        governor.start(child.logical_operation_id)
    governor.complete(
        child.logical_operation_id,
        actual_usage=child.full_path_reservation,
        artifact_sha256="c" * 64,
    )
    return parent, child, journal


def test_completed_child_may_reserve_early_but_cannot_start_before_parent_terminal(
    exact, tmp_path: Path
) -> None:
    parent, child, valid_journal = _interleaved_completed_chain(
        exact,
        tmp_path / "reserved-early",
        start_child_before_parent_terminal=False,
    )
    valid = _verifier(
        exact,
        valid_journal.ledger_path,
        valid_journal.anchor_path,
    )
    valid.executed(parent.logical_operation_id)
    assert valid.executed(child.logical_operation_id).journal_state == "completed"

    parent, child, invalid_journal = _interleaved_completed_chain(
        exact,
        tmp_path / "started-early",
        start_child_before_parent_terminal=True,
    )
    verifier = _verifier(
        exact,
        invalid_journal.ledger_path,
        invalid_journal.anchor_path,
    )
    verifier.executed(parent.logical_operation_id)
    with pytest.raises(FactorialStageDispositionError, match="started before parent"):
        verifier.executed(child.logical_operation_id)


def test_serialized_exact_artifact_requires_fresh_pinned_replay(
    exact, tmp_path: Path
) -> None:
    authority, bundle, plan, matrix, schedule = exact
    by_attempt: dict[str, list[object]] = {}
    for operation in schedule.operations:
        by_attempt.setdefault(operation.attempt_id, []).append(operation)
    roots = tuple(items[0] for items in by_attempt.values())
    ledger, anchor = _write_terminal_journal(tmp_path / "artifact", roots)
    kwargs = {
        "matrix": matrix,
        "plan": plan,
        "bundle": bundle,
        "task_authority": authority,
        "ledger_path": ledger,
        "anchor_path": anchor,
    }
    artifact = derive_exact_semantic_artifact(**kwargs)
    verified = verify_serialized_exact_semantic_artifact(
        artifact.canonical_bytes,
        expected_sha256=artifact.sha256,
        **kwargs,
    )
    assert verified.canonical_bytes == artifact.canonical_bytes
    assert verified.seal.formal_execution_ready is False

    payload = artifact.to_dict()
    payload["seal"]["schedule_sha256"] = "f" * 64
    with pytest.raises(FactorialStageDispositionError, match="differs"):
        verify_serialized_exact_semantic_artifact(_canonical(payload), **kwargs)
    with pytest.raises(FactorialStageDispositionError, match="size"):
        verify_serialized_exact_semantic_artifact(
            b"x" * (32 * 1024 * 1024 + 1), **kwargs
        )

    # A formerly valid artifact is not provenance for a later journal head.
    lines = ledger.read_text(encoding="utf-8").splitlines()
    terminal = json.loads(lines[-1])
    terminal["payload"]["artifact_sha256"] = "d" * 64
    terminal_core = {
        key: value for key, value in terminal.items() if key != "event_sha256"
    }
    terminal["event_sha256"] = _sha(terminal_core)
    lines[-1] = json.dumps(
        terminal,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    ledger.write_text("\n".join(lines) + "\n", encoding="utf-8")
    anchor.write_bytes(
        _canonical(
            {
                "event_count": len(lines),
                "head_sha256": terminal["event_sha256"],
                "schema_version": 1,
            }
        )
    )
    with pytest.raises(FactorialStageDispositionError, match="differs"):
        verify_serialized_exact_semantic_artifact(
            artifact.canonical_bytes,
            **kwargs,
        )
