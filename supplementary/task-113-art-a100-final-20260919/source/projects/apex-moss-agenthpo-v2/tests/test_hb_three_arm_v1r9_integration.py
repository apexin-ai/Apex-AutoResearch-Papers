from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import pytest

from optimization_lab.harness_builder.events import ResourceVector
from optimization_lab.harness_builder.experience import ExperienceRecord
from optimization_lab.harness_builder.learning import (
    BuilderCheckpoint,
    ExperienceBankSnapshot,
)
from optimization_lab.harness_builder.three_arm import THREE_ARMS
from optimization_lab.harness_builder.three_arm_continuation import (
    ArtifactBinding,
    ExcludedTailBinding,
    OperationJournalBinding,
    PrefixReceiptBinding,
    ThreeArmContinuationContract,
    ThreeArmContinuationSourceSnapshot,
)
from optimization_lab.harness_builder.three_arm_providers import (
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
)
from optimization_lab.harness_builder.three_arm_v1r9_prepare import (
    V1R9_COMPOSITE_HARD_CAPS,
    V1R9_SUFFIX_ENTITLEMENT_TOTALS,
    build_three_arm_v1r9_staging_payload,
    build_three_arm_v1r9_stream,
    resolve_v1r9_codex_executable,
)
from optimization_lab.harness_builder.three_arm_v1r9_runtime import (
    _verify_swebench_remote_deployment_alignment,
    _verify_v1r9_codex_executable,
    _verify_v1r9_suite_gates,
    build_v1r9_initial_state,
    make_v1r9_resource_governor,
    v1r9_dry_run_payload,
)


RULE_SHA = "a" * 64
SOURCE_REVISION = "b" * 40
SUCCESSOR_REVISION = "c" * 40
CODEX_SHA = "0" * 64
CODEX_PATH = "/opt/moss/bin/codex-0.144.6"
PREFIX_IDS = (
    "yahpo-lcbench:167168",
    "compilergym-cbench:dijkstra",
    "swebench-verified:sphinx-doc__sphinx-8459",
    "compilergym-cbench:crc32",
    "swebench-verified:django__django-14500",
    "yahpo-lcbench:168331",
)


def test_runtime_cross_checks_canary_and_remote_deployment_contracts() -> None:
    remote_contract = {
        "host_alias": "a100jump",
        "remote_python": "/remote/venv/bin/python",
        "remote_project_root": "/remote/runtime/Moss-commit",
        "remote_swebench_source_root": "/remote/SWE-bench",
    }
    qualification = {
        "v1r9_inputs": {"remote_execution_contract": remote_contract}
    }
    deployment = {
        "host_alias": remote_contract["host_alias"],
        "remote_python": {"requested_path": remote_contract["remote_python"]},
        "remote_project_root": remote_contract["remote_project_root"],
        "remote_swebench_source_root": remote_contract[
            "remote_swebench_source_root"
        ],
    }

    _verify_swebench_remote_deployment_alignment(
        qualification_transfer=qualification,
        remote_deployment=deployment,
    )
    deployment["remote_project_root"] = "/remote/runtime/other"
    with pytest.raises(ValueError, match="canary and remote deployment"):
        _verify_swebench_remote_deployment_alignment(
            qualification_transfer=qualification,
            remote_deployment=deployment,
        )


def _record(index: int, source: str) -> ExperienceRecord:
    return ExperienceRecord.from_dict(
        {
            "record_id": f"record-{index}",
            "source_instance_id": source,
            "builder_version": "builder-v001",
            "instance_descriptor": ["fixture"],
            "initial_harness_structure": ["analyze", "generate", "verify"],
            "evolution_rule": "discipline",
            "trigger_evidence": ["sealed trajectory"],
            "outcome_delta": 0.1,
            "correctness": True,
            "resource_cost": {"model_calls": 1.0},
            "counterexamples": ["fixture only"],
            "scope": "single_instance_observation",
            "provenance_event_ids": [f"event-{index}"],
            "sealed": True,
        }
    )


def _source_snapshot(
    tmp_path: Path,
) -> tuple[Path, ThreeArmContinuationSourceSnapshot, ExperienceBankSnapshot, BuilderCheckpoint]:
    source_root = tmp_path / "v1r8"
    bank = ExperienceBankSnapshot.create(
        bank_id="online-through-005",
        parent_sha256="d" * 64,
        records=tuple(_record(index, source) for index, source in enumerate(PREFIX_IDS)),
    )
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256="e" * 64,
        experience_bank_sha256=bank.sha256,
        rule_registry_sha256=RULE_SHA,
        learned_through_instance=PREFIX_IDS[-1],
        stream_index=5,
    )
    bank_path = source_root / f"formal/experience_banks/{bank.sha256}.json"
    checkpoint_path = (
        source_root / f"formal/builder_checkpoints/{checkpoint.sha256}.json"
    )
    bank_path.parent.mkdir(parents=True)
    checkpoint_path.parent.mkdir(parents=True)
    bank_path.write_bytes(bank.canonical_bytes)
    checkpoint_path.write_bytes(checkpoint.canonical_bytes)
    snapshot = ThreeArmContinuationSourceSnapshot(
        source_manifest_sha256="1" * 64,
        source_staging_plan_sha256="2" * 64,
        source_code_revision=SOURCE_REVISION,
        prefix_instance_receipts=tuple(
            PrefixReceiptBinding(
                relative_path=f"formal/instances/{index:03d}/instance_receipt.json",
                sha256=f"{index + 1:x}" * 64,
                stream_index=index,
                instance_id=instance_id,
            )
            for index, instance_id in enumerate(PREFIX_IDS)
        ),
        operation_journal=OperationJournalBinding(
            relative_path="control/operations/operation_ledger.jsonl",
            sha256="8" * 64,
            event_count=1244,
            head_sha256="9" * 64,
        ),
        formal_ledger=ArtifactBinding(
            relative_path="formal/ledger.jsonl", sha256="3" * 64
        ),
        online_checkpoint=ArtifactBinding(
            relative_path=checkpoint_path.relative_to(source_root).as_posix(),
            sha256=checkpoint.sha256,
        ),
        online_bank=ArtifactBinding(
            relative_path=bank_path.relative_to(source_root).as_posix(),
            sha256=bank.sha256,
        ),
        rule_registry_sha256=RULE_SHA,
        learned_through_instance=PREFIX_IDS[-1],
        record_source_instance_ids=PREFIX_IDS,
        source_committed_usage=ResourceVector(
            model_calls=286,
            evaluator_transactions=129,
            cpu_evaluator_seconds=1695.3563624848612,
        ),
        excluded_instance_id=(
            "swebench-verified:scikit-learn__scikit-learn-14983"
        ),
        excluded_consumed_tail=(
            ExcludedTailBinding(
                operation_id="formal:discarded:sham_planner_call:v002",
                cell_id=(
                    "formal:swebench-verified:"
                    "scikit-learn__scikit-learn-14983:A"
                ),
                operation_kind="sham_planner_call",
                state="started",
                start_event_sha256="4" * 64,
                charged_usage=ResourceVector(model_calls=1),
                operation_artifacts=(
                    ArtifactBinding(
                        relative_path="model-gateway/operations/discarded/prompt.txt",
                        sha256="5" * 64,
                    ),
                ),
                result_relative_path=(
                    "model-gateway/operations/discarded/result.json"
                ),
                result_absent=True,
            ),
        ),
    )
    return source_root, snapshot, bank, checkpoint


def _staging(
    snapshot: ThreeArmContinuationSourceSnapshot,
) -> tuple[dict[str, object], ThreeArmContinuationContract]:
    payload = build_three_arm_v1r9_staging_payload(
        source_snapshot=snapshot,
        code_revision=SUCCESSOR_REVISION,
        rule_ids=(
            "contract_compatibility",
            "discipline",
            "dream",
            "law_inversion",
            "recombination",
            "correctness_recovery",
            "cross_instance_distillation",
        ),
        source_hashes={"rule_registry": RULE_SHA},
        codex_executable_path=CODEX_PATH,
        codex_executable_sha256=CODEX_SHA,
        qualification_transfer_sha256="f" * 64,
    )
    encoded = (
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode()
    return payload, ThreeArmContinuationContract.from_staging_bytes(
        encoded, source_snapshot=snapshot
    )


def test_v1r9_stream_keeps_exact_prefix_new_swe_suffix_and_global_rotation(
    tmp_path: Path,
) -> None:
    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    payload, contract = _staging(snapshot)
    stream = build_three_arm_v1r9_stream()

    assert tuple(item["instance_id"] for item in stream[:6]) == PREFIX_IDS
    assert tuple(
        item["task_id"] for item in stream if item["suite"] == "swebench-verified"
    )[2:] == SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    assert stream[6]["instance_id"] == "swebench-verified:pytest-dev__pytest-7205"
    assert tuple(stream[6]["arm_order"]) == THREE_ARMS
    assert tuple(stream[7]["arm_order"]) == THREE_ARMS[1:] + THREE_ARMS[:1]
    assert tuple(stream[8]["arm_order"]) == THREE_ARMS[2:] + THREE_ARMS[:2]
    assert contract.active_stream == contract.stream[6:24]
    assert len(contract.active_stream) == 18
    assert payload["experience_initialization"] == "successor_continuation"
    assert payload["source_hashes"][f"runtime:codex-executable:{CODEX_PATH}"] == (
        CODEX_SHA
    )


def _fake_codex(path: Path, *, version: str = "codex-cli 0.144.6") -> Path:
    path.write_text(f"#!/bin/sh\nprintf '%s\\n' '{version}'\n", encoding="utf-8")
    path.chmod(0o755)
    return path


def test_v1r9_codex_executable_binding_resolves_path_version_and_content(
    tmp_path: Path,
) -> None:
    target = _fake_codex(tmp_path / "codex-real")
    launcher = tmp_path / "codex"
    launcher.symlink_to(target.name)

    binding = resolve_v1r9_codex_executable(str(launcher))

    assert binding.resolved_path == target.resolve()
    assert binding.sha256 == hashlib.sha256(target.read_bytes()).hexdigest()
    assert binding.client_version == "codex-cli-0.144.6"

    wrong_version = _fake_codex(
        tmp_path / "codex-wrong-version", version="codex-cli 0.145.0"
    )
    with pytest.raises(ValueError, match="frozen client"):
        resolve_v1r9_codex_executable(wrong_version)


def test_v1r9_runtime_rejects_an_arbitrary_or_replaced_codex_cli(
    tmp_path: Path,
) -> None:
    frozen = _fake_codex(tmp_path / "codex-frozen")
    frozen_sha = hashlib.sha256(frozen.read_bytes()).hexdigest()
    staging = {
        "model_signature": {
            "executor_model": "gpt-5.6-sol",
            "reasoning_effort": "high",
            "transport": "codex-exec-chatgpt-login",
            "client_version": "codex-cli-0.144.6",
        },
        "source_hashes": {
            f"runtime:codex-executable:{frozen.resolve()}": frozen_sha,
        },
    }
    alternate = _fake_codex(tmp_path / "codex-alternate")

    with pytest.raises(ValueError, match="path differs"):
        _verify_v1r9_codex_executable(staging=staging, executable=alternate)

    _verify_v1r9_codex_executable(staging=staging, executable=frozen)
    frozen.write_text("#!/bin/sh\nprintf '%s\\n' 'codex-cli 0.144.6'\n# drift\n")
    frozen.chmod(0o755)
    with pytest.raises(ValueError, match="hash differs"):
        _verify_v1r9_codex_executable(staging=staging, executable=frozen)


def test_v1r9_suffix_entitlements_and_composite_budget_are_exact(
    tmp_path: Path,
) -> None:
    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    payload, contract = _staging(snapshot)

    assert len(payload["cell_entitlements"]) == 66
    assert contract.suffix_entitlement_totals == V1R9_SUFFIX_ENTITLEMENT_TOTALS
    assert contract.suffix_entitlement_totals.to_dict() == {
        "model_calls": 876,
        "evaluator_transactions": 432,
        "gpu_exclusive_seconds": 0.0,
        "cpu_evaluator_seconds": 604800.0,
    }
    assert contract.composite_hard_caps == V1R9_COMPOSITE_HARD_CAPS
    combined = snapshot.source_committed_usage + contract.suffix_entitlement_totals
    assert combined.model_calls == 1162
    assert combined.evaluator_transactions == 561
    assert combined.cpu_evaluator_seconds == pytest.approx(606495.3563624849)
    assert not any(PREFIX_IDS[0] in cell for cell in contract.cell_entitlements)


def test_v1r9_runtime_rejects_phase_model_stream_or_cell_cap_rebinding(
    tmp_path: Path,
) -> None:
    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    _payload, contract = _staging(snapshot)

    wrong_phase = replace(contract, phase_id="hb-three-arm-live-v1r9-rebound")
    with pytest.raises(ValueError, match="identity"):
        make_v1r9_resource_governor(
            artifact_root=tmp_path / "wrong-phase",
            contract=wrong_phase,
            source_guard=lambda: None,
        )

    wrong_model = replace(contract, model="another-model")
    with pytest.raises(ValueError, match="identity"):
        make_v1r9_resource_governor(
            artifact_root=tmp_path / "wrong-model",
            contract=wrong_model,
            source_guard=lambda: None,
        )

    stream = list(contract.stream)
    first_lc = next(i for i, item in enumerate(stream[6:], 6) if item.suite == "yahpo-lcbench")
    second_lc = next(
        i
        for i, item in enumerate(stream[first_lc + 1 :], first_lc + 1)
        if item.suite == "yahpo-lcbench" and item.learning_mode == stream[first_lc].learning_mode
    )
    first_task, second_task = stream[first_lc].task_id, stream[second_lc].task_id
    stream[first_lc] = replace(
        stream[first_lc],
        task_id=second_task,
    )
    stream[second_lc] = replace(
        stream[second_lc],
        task_id=first_task,
    )
    with pytest.raises(ValueError, match="stream"):
        make_v1r9_resource_governor(
            artifact_root=tmp_path / "wrong-stream",
            contract=replace(contract, stream=tuple(stream)),
            source_guard=lambda: None,
        )

    cells = dict(contract.cell_entitlements)
    cell_ids = [cell_id for cell_id in cells if cell_id.startswith("formal:")]
    donor, receiver = cell_ids[:2]
    cells[donor] = replace(
        cells[donor],
        cpu_evaluator_seconds=cells[donor].cpu_evaluator_seconds - 1.0,
    )
    cells[receiver] = replace(
        cells[receiver],
        cpu_evaluator_seconds=cells[receiver].cpu_evaluator_seconds + 1.0,
    )
    with pytest.raises(ValueError, match="cell entitlements"):
        make_v1r9_resource_governor(
            artifact_root=tmp_path / "wrong-cells",
            contract=replace(contract, cell_entitlements=cells),
            source_guard=lambda: None,
        )


def test_v1r9_suite_gate_hashes_are_exact_and_rechecked(tmp_path: Path) -> None:
    gates = {}
    source_hashes = {}
    for suite in ("yahpo-lcbench", "compilergym-cbench", "swebench-verified"):
        path = tmp_path / f"{suite}.json"
        path.write_text(f"{suite}\n", encoding="utf-8")
        gates[suite] = path
        source_hashes[f"gate:{suite}"] = hashlib.sha256(path.read_bytes()).hexdigest()
    staging = {"source_hashes": source_hashes}

    _verify_v1r9_suite_gates(staging=staging, suite_gate_paths=gates)
    gates["yahpo-lcbench"].write_text("drift\n", encoding="utf-8")
    with pytest.raises(ValueError, match="gate hash"):
        _verify_v1r9_suite_gates(staging=staging, suite_gate_paths=gates)


def test_v1r9_imports_online_state_but_keeps_control_state_empty(
    tmp_path: Path,
) -> None:
    source_root, snapshot, bank, checkpoint = _source_snapshot(tmp_path)

    state = build_v1r9_initial_state(
        source_root=source_root,
        source_snapshot=snapshot,
        rule_registry_sha256=RULE_SHA,
    )

    assert state.online_bank == bank
    assert state.online_checkpoint == checkpoint
    assert tuple(record.source_instance_id for record in state.online_bank.records) == (
        PREFIX_IDS
    )
    assert state.empty_bank.records == ()
    assert state.empty_checkpoint.experience_bank_sha256 == state.empty_bank.sha256
    assert state.empty_checkpoint.sha256 != state.online_checkpoint.sha256
    assert state.task_conditioned_checkpoint_sha256 not in {
        state.online_checkpoint.sha256,
        state.online_bank.sha256,
    }


def test_v1r9_resource_governor_invokes_source_guard_before_reserve(
    tmp_path: Path,
) -> None:
    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    _payload, contract = _staging(snapshot)
    calls: list[str] = []

    def guard() -> None:
        calls.append("verified")

    governor = make_v1r9_resource_governor(
        artifact_root=tmp_path / "v1r9",
        contract=contract,
        source_guard=guard,
    )
    first_cell = next(iter(contract.cell_entitlements))
    governor.reserve(
        operation_id="fixture:planner_call:v001",
        cell_id=first_cell,
        operation_kind="planner_call",
        reservation=ResourceVector(model_calls=1),
    )

    assert calls == ["verified"]
    assert governor.pre_reserve_guard is guard
    assert governor.global_caps == V1R9_SUFFIX_ENTITLEMENT_TOTALS


def test_v1r9_dry_run_reports_zero_calls_without_creating_artifact_root(
    tmp_path: Path,
) -> None:
    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    _payload, contract = _staging(snapshot)
    artifact_root = tmp_path / "must-not-exist"

    result = v1r9_dry_run_payload(contract=contract, source_snapshot=snapshot)

    assert result["execution_start_index"] == 6
    assert result["active_stream_instances"] == 18
    assert result["model_calls_started"] == 0
    assert result["evaluator_transactions_started"] == 0
    assert result["source_snapshot_sha256"] == snapshot.sha256
    assert not artifact_root.exists()


def test_v1r9_runner_rejects_artifact_root_outside_staging_parent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from optimization_lab.harness_builder import three_arm_v1r9_runtime as runtime

    source_root = tmp_path / "v1r8-source"
    source_root.mkdir()
    staging_root = tmp_path / "frozen-v1r9"
    staging_root.mkdir()
    staging_path = staging_root / "staging_plan.json"
    staging_path.write_text("{}\n", encoding="utf-8")

    def preflight_must_not_run(**_kwargs: object) -> object:
        raise AssertionError("preflight reached before artifact-root binding")

    monkeypatch.setattr(
        runtime,
        "preflight_three_arm_v1r9",
        preflight_must_not_run,
    )
    with pytest.raises(ValueError, match="staging plan parent"):
        runtime.build_three_arm_v1r9_runner(
            artifact_root=tmp_path / "duplicate-segment",
            staging_path=staging_path,
            project_root=tmp_path,
            source_root=source_root,
            source_manifest_path=tmp_path / "manifest.json",
            source_snapshot_path=tmp_path / "snapshot.json",
            expected_source_snapshot_sha256="1" * 64,
            rule_registry_path=tmp_path / "registry.json",
            source_paths={},
            qualification_transfer_receipt_path=tmp_path / "qualification.json",
            remote_deployment_receipt_path=tmp_path / "deployment.json",
            swebench_task_lock_path=tmp_path / "tasks.json",
            lcbench_canary_summary=tmp_path / "lcbench.json",
            lcbench_data_root=tmp_path / "lcbench-data",
            lcbench_settings=tmp_path / "lcbench.yaml",
            lcbench_python=tmp_path / "lcbench-python",
            compilergym_canary_summary=tmp_path / "compilergym.json",
            compilergym_python=tmp_path / "compilergym-python",
            compilergym_site_data_root=tmp_path / "site-data",
            compilergym_cache_root=tmp_path / "cache",
            compilergym_compatibility_library_root=tmp_path / "compat",
            swebench_canary_summary=tmp_path / "swebench.json",
            swebench_dataset=tmp_path / "dataset.parquet",
            swebench_selection=tmp_path / "selection.json",
            swebench_image_lock=tmp_path / "images.json",
            swebench_host_alias="a100jump",
            swebench_remote_python="/remote/venv/bin/python",
            swebench_remote_project_root="/remote/runtime/Moss-revision",
            swebench_remote_source_root="/remote/SWE-bench",
            swebench_remote_attempt_root="/remote/attempts",
            codex_executable="/opt/moss/bin/codex-0.144.6",
        )


def test_v1r9_dry_run_cli_calls_full_source_preflight_before_reporting(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import run_hb_three_arm_v1r9 as cli

    _source_root, snapshot, _bank, _checkpoint = _source_snapshot(tmp_path)
    _payload, contract = _staging(snapshot)
    observed: dict[str, object] = {}

    def fake_preflight(**kwargs: object) -> object:
        observed.update(kwargs)
        return SimpleNamespace(contract=contract, source_snapshot=snapshot)

    monkeypatch.setattr(cli, "preflight_three_arm_v1r9", fake_preflight)
    artifact_root = tmp_path / "dry-artifacts"
    result = cli.main(
        [
            "--project-root",
            str(tmp_path),
            "--artifact-root",
            str(artifact_root),
            "--staging-plan",
            str(tmp_path / "staging.json"),
            "--source-root",
            str(tmp_path / "v1r8"),
            "--source-manifest",
            str(tmp_path / "manifest.json"),
            "--source-snapshot",
            str(tmp_path / "snapshot.json"),
            "--expected-source-snapshot-sha256",
            snapshot.sha256,
            "--rule-registry",
            str(tmp_path / "registry.json"),
            "--lcbench-canary",
            str(tmp_path / "lcbench-canary.json"),
            "--compilergym-canary",
            str(tmp_path / "compilergym-canary.json"),
            "--qualification-transfer",
            str(tmp_path / "qualification.json"),
            "--remote-deployment-receipt",
            str(tmp_path / "remote-deployment.json"),
            "--swebench-task-lock",
            str(tmp_path / "tasks.json"),
            "--swebench-canary",
            str(tmp_path / "canary.json"),
            "--swebench-selection",
            str(tmp_path / "selection.json"),
            "--swebench-image-lock",
            str(tmp_path / "images.json"),
            "--swebench-remote-python",
            "/remote/venv/bin/python",
            "--swebench-remote-project-root",
            "/remote/runtime/Moss-commit",
            "--swebench-remote-source-root",
            "/remote/SWE-bench",
            "--codex-executable",
            str(tmp_path / "pinned-codex"),
        ]
    )

    assert result == 0
    assert observed["source_root"] == tmp_path / "v1r8"
    assert observed["expected_source_snapshot_sha256"] == snapshot.sha256
    assert observed["codex_executable"] == str(tmp_path / "pinned-codex")
    assert observed["remote_deployment_receipt_path"] == (
        tmp_path / "remote-deployment.json"
    )
    output = json.loads(capsys.readouterr().out)
    assert output["model_calls_started"] == 0
    assert output["evaluator_transactions_started"] == 0
    assert not artifact_root.exists()


def test_v1r9_prepare_cli_passes_the_selected_codex_executable_to_staging(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import prepare_hb_three_arm_v1r9 as cli

    observed: dict[str, object] = {}

    def fake_run(*args: object, **kwargs: object) -> object:
        return SimpleNamespace(stdout=SUCCESSOR_REVISION + "\n")

    def fake_prepare(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        return {"schema_version": 6, "execution_ready": True}

    monkeypatch.setattr(cli.subprocess, "run", fake_run)
    monkeypatch.setattr(cli, "prepare_three_arm_v1r9_campaign", fake_prepare)
    pinned = tmp_path / "pinned-codex"
    result = cli.main(
        [
            "prepare-staging",
            "--project-root",
            str(tmp_path),
            "--artifact-root",
            str(tmp_path / "artifacts"),
            "--source-root",
            str(tmp_path / "v1r8"),
            "--source-manifest",
            str(tmp_path / "manifest.json"),
            "--source-snapshot",
            str(tmp_path / "snapshot.json"),
            "--rule-registry",
            str(tmp_path / "registry.json"),
            "--qualification-transfer",
            str(tmp_path / "qualification.json"),
            "--remote-deployment-receipt",
            str(tmp_path / "remote-deployment.json"),
            "--swebench-task-lock",
            str(tmp_path / "tasks.json"),
            "--swebench-selection",
            str(tmp_path / "selection.json"),
            "--swebench-image-lock",
            str(tmp_path / "images.json"),
            "--swebench-gold-canary",
            str(tmp_path / "canary.json"),
            "--swebench-remote-python",
            "/remote/venv/bin/python",
            "--swebench-remote-project-root",
            "/remote/runtime/Moss-commit",
            "--swebench-remote-source-root",
            "/remote/SWE-bench",
            "--codex-executable",
            str(pinned),
            "--execute",
        ]
    )

    assert result == 0
    assert observed["codex_executable"] == str(pinned)
    assert observed["remote_deployment_receipt_path"] == (
        tmp_path / "remote-deployment.json"
    )
    assert json.loads(capsys.readouterr().out)["execution_ready"] is True
