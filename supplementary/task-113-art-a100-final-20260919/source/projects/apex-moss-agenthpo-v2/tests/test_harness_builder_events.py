from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.events import (
    JournalIntegrityError,
    OperationJournal,
    OperationStateError,
    ResourceCapExceeded,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
    UnsafeIdentifierError,
    verify_operation_journal,
)


def _caps(
    *,
    model_calls: int = 10,
    evaluator_transactions: int = 10,
    gpu: float = 1000.0,
    cpu: float = 1000.0,
) -> ResourceCaps:
    return ResourceCaps(
        model_calls=model_calls,
        evaluator_transactions=evaluator_transactions,
        gpu_exclusive_seconds=gpu,
        cpu_evaluator_seconds=cpu,
    )


def _governor(
    tmp_path: Path,
    *,
    global_caps: ResourceCaps | None = None,
    cell_caps: dict[str, ResourceCaps] | None = None,
    anchor: bool = True,
    pre_reserve_guard=None,
) -> ResourceGovernor:
    journal = OperationJournal(
        tmp_path / "events",
        anchor_path=(tmp_path / "trusted-head.json") if anchor else None,
    )
    return ResourceGovernor(
        journal=journal,
        global_caps=global_caps or _caps(),
        cell_caps=cell_caps or {"cell-a": _caps(), "cell-b": _caps()},
        pre_reserve_guard=pre_reserve_guard,
    )


def test_journal_is_hash_chained_append_only_idempotent_and_anchored(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)
    reservation = ResourceVector(model_calls=1)

    reserved = governor.reserve(
        operation_id="cell-a:model:001",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=reservation,
    )
    first_bytes = governor.journal.ledger_path.read_bytes()
    repeated = governor.reserve(
        operation_id="cell-a:model:001",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=reservation,
    )
    assert repeated == reserved
    assert governor.journal.ledger_path.read_bytes() == first_bytes

    governor.start("cell-a:model:001")
    assert governor.journal.ledger_path.read_bytes().startswith(first_bytes)
    governor.complete("cell-a:model:001", artifact_sha256="a" * 64)

    replay = verify_operation_journal(
        governor.journal.ledger_path,
        anchor_path=tmp_path / "trusted-head.json",
    )
    assert replay.event_count == 3
    assert replay.head_sha256 == replay.events[-1].event_sha256
    assert replay.events[0].prev_event_sha256 == "0" * 64
    assert replay.events[1].prev_event_sha256 == replay.events[0].event_sha256
    assert replay.operations["cell-a:model:001"].state == "completed"

    anchor = json.loads((tmp_path / "trusted-head.json").read_text(encoding="utf-8"))
    assert anchor == {
        "schema_version": 1,
        "event_count": 3,
        "head_sha256": replay.head_sha256,
    }


def test_pre_reserve_guard_fails_before_any_new_ledger_event(tmp_path: Path) -> None:
    valid = True
    checks = 0

    def guard() -> None:
        nonlocal checks
        checks += 1
        if not valid:
            raise RuntimeError("continuation source drift")

    governor = _governor(tmp_path, pre_reserve_guard=guard)
    governor.reserve(
        operation_id="cell-a:model:guarded",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=1),
    )
    before = governor.journal.ledger_path.read_bytes()
    valid = False

    with pytest.raises(RuntimeError, match="source drift"):
        governor.reserve(
            operation_id="cell-a:model:blocked",
            cell_id="cell-a",
            operation_kind="model_call",
            reservation=ResourceVector(model_calls=1),
        )

    assert checks == 2
    assert governor.journal.ledger_path.read_bytes() == before


def test_independent_replay_detects_content_tampering(tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    governor.reserve(
        operation_id="cell-a:eval:001",
        cell_id="cell-a",
        operation_kind="evaluator_transaction",
        reservation=ResourceVector(
            evaluator_transactions=1, gpu_exclusive_seconds=100.0
        ),
    )
    governor.start("cell-a:eval:001")

    lines = governor.journal.ledger_path.read_text(encoding="utf-8").splitlines()
    first = json.loads(lines[0])
    first["payload"]["reservation"]["gpu_exclusive_seconds"] = 1.0
    lines[0] = json.dumps(first, sort_keys=True)
    governor.journal.ledger_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with pytest.raises(JournalIntegrityError, match="hash"):
        verify_operation_journal(
            governor.journal.ledger_path,
            anchor_path=tmp_path / "trusted-head.json",
        )


def test_external_anchor_detects_a_valid_prefix_truncation(tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    governor.reserve(
        operation_id="cell-a:model:002",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=1),
    )
    one_event_prefix = governor.journal.ledger_path.read_bytes()
    governor.start("cell-a:model:002")
    governor.journal.ledger_path.write_bytes(one_event_prefix)

    # The remaining prefix is internally valid, but it cannot satisfy the independently
    # stored head commitment.
    replay = verify_operation_journal(governor.journal.ledger_path)
    assert replay.event_count == 1
    with pytest.raises(JournalIntegrityError, match="anchor"):
        verify_operation_journal(
            governor.journal.ledger_path,
            anchor_path=tmp_path / "trusted-head.json",
        )


@pytest.mark.parametrize(
    "operation_id",
    ["../escape", "bad\nline", " wildcard", "glob*operation", "", "x" * 257],
)
def test_operation_ids_are_safe(operation_id: str, tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    with pytest.raises(UnsafeIdentifierError):
        governor.reserve(
            operation_id=operation_id,
            cell_id="cell-a",
            operation_kind="model_call",
            reservation=ResourceVector(model_calls=1),
        )


def test_operation_state_machine_is_strict_and_terminal_calls_are_idempotent(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)

    with pytest.raises(OperationStateError, match="not reserved"):
        governor.start("cell-a:model:missing")

    governor.reserve(
        operation_id="cell-a:model:003",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=1),
    )
    with pytest.raises(OperationStateError, match="started"):
        governor.complete("cell-a:model:003")

    started = governor.start("cell-a:model:003")
    assert governor.start("cell-a:model:003") == started
    completed = governor.complete("cell-a:model:003", artifact_sha256="b" * 64)
    assert governor.complete(
        "cell-a:model:003", artifact_sha256="b" * 64
    ) == completed
    with pytest.raises(OperationStateError, match="terminal"):
        governor.fail("cell-a:model:003", reason_code="provider_error")
    with pytest.raises(OperationStateError, match="different terminal"):
        governor.complete("cell-a:model:003", artifact_sha256="c" * 64)


def test_per_cell_entitlements_cannot_be_borrowed(tmp_path: Path) -> None:
    governor = _governor(
        tmp_path,
        global_caps=_caps(model_calls=4),
        cell_caps={
            "cell-a": _caps(model_calls=3),
            "cell-b": _caps(model_calls=1),
        },
    )
    governor.reserve(
        operation_id="cell-b:model:001",
        cell_id="cell-b",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=1),
    )

    with pytest.raises(ResourceCapExceeded, match="cell-b.*model_calls"):
        governor.reserve(
            operation_id="cell-b:model:002",
            cell_id="cell-b",
            operation_kind="model_call",
            reservation=ResourceVector(model_calls=1),
        )

    # cell-a's unused allocation remains unavailable to cell-b, but cell-a can use it.
    governor.reserve(
        operation_id="cell-a:model:001",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=3),
    )
    with pytest.raises(ResourceCapExceeded, match="global.*model_calls"):
        governor.reserve(
            operation_id="cell-a:model:002",
            cell_id="cell-a",
            operation_kind="model_call",
            reservation=ResourceVector(model_calls=1),
        )


def test_recovery_conservatively_charges_abandoned_operations(tmp_path: Path) -> None:
    governor = _governor(tmp_path)
    governor.reserve(
        operation_id="cell-a:model:abandoned",
        cell_id="cell-a",
        operation_kind="model_call",
        reservation=ResourceVector(model_calls=1),
    )
    governor.start("cell-a:model:abandoned")
    governor.reserve(
        operation_id="cell-a:eval:abandoned",
        cell_id="cell-a",
        operation_kind="evaluator_transaction",
        reservation=ResourceVector(
            evaluator_transactions=1,
            gpu_exclusive_seconds=420.0,
            cpu_evaluator_seconds=30.0,
        ),
    )
    governor.start("cell-a:eval:abandoned")
    governor.reserve(
        operation_id="cell-a:eval:complete",
        cell_id="cell-a",
        operation_kind="evaluator_transaction",
        reservation=ResourceVector(
            evaluator_transactions=1,
            gpu_exclusive_seconds=100.0,
            cpu_evaluator_seconds=100.0,
        ),
    )
    governor.start("cell-a:eval:complete")
    governor.complete(
        "cell-a:eval:complete",
        actual_usage=ResourceVector(
            evaluator_transactions=1,
            gpu_exclusive_seconds=25.0,
            cpu_evaluator_seconds=40.0,
        ),
        artifact_sha256="d" * 64,
    )
    governor.reserve(
        operation_id="cell-a:eval:reserved-only",
        cell_id="cell-a",
        operation_kind="evaluator_transaction",
        reservation=ResourceVector(
            evaluator_transactions=1,
            cpu_evaluator_seconds=50.0,
        ),
    )

    recovered = ResourceGovernor(
        journal=OperationJournal(
            tmp_path / "events", anchor_path=tmp_path / "trusted-head.json"
        ),
        global_caps=_caps(),
        cell_caps={"cell-a": _caps(), "cell-b": _caps()},
    )
    snapshot = recovered.snapshot()

    assert snapshot.abandoned_operation_ids == (
        "cell-a:eval:abandoned",
        "cell-a:model:abandoned",
    )
    assert snapshot.reserved_operation_ids == ("cell-a:eval:reserved-only",)
    assert snapshot.global_committed == ResourceVector(
        model_calls=1,
        evaluator_transactions=3,
        gpu_exclusive_seconds=445.0,
        cpu_evaluator_seconds=120.0,
    )
    assert snapshot.cell_committed["cell-a"] == snapshot.global_committed


def test_failed_operation_without_usage_charges_the_full_reservation(
    tmp_path: Path,
) -> None:
    governor = _governor(tmp_path)
    reservation = ResourceVector(
        evaluator_transactions=1,
        gpu_exclusive_seconds=420.0,
        cpu_evaluator_seconds=300.0,
    )
    governor.reserve(
        operation_id="cell-a:eval:failed",
        cell_id="cell-a",
        operation_kind="evaluator_transaction",
        reservation=reservation,
    )
    governor.start("cell-a:eval:failed")
    failed = governor.fail("cell-a:eval:failed", reason_code="lease_lost")

    assert failed.payload["usage_known"] is False
    assert governor.snapshot().global_committed == reservation


@pytest.mark.parametrize(
    "kwargs",
    [
        {"model_calls": -1},
        {"evaluator_transactions": True},
        {"gpu_exclusive_seconds": float("inf")},
        {"cpu_evaluator_seconds": float("nan")},
    ],
)
def test_resource_vectors_reject_invalid_values(kwargs: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        ResourceVector(**kwargs)  # type: ignore[arg-type]
