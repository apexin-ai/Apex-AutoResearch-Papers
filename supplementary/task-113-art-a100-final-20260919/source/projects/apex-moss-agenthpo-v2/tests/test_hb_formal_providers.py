from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder import formal_providers
from optimization_lab.harness_builder.adapters.compilergym import (
    ADVERSARIAL_CANARY_IDS,
    frozen_contract,
)
from optimization_lab.harness_builder.events import (
    OperationJournal,
    ResourceCaps,
    ResourceGovernor,
    ResourceVector,
)
from optimization_lab.harness_builder.formal_providers import (
    CompilerGymFormalSuiteProvider,
    FormalProviderCompositionBlocked,
    FormalProviderCompositionConfig,
    StagingBoundFormalProviderFactory,
    compose_formal_provider_factory,
    compose_verified_suite_provider,
    preflight_formal_providers,
)
from optimization_lab.harness_builder.schema import PilotManifest
from optimization_lab.harness_builder.solutions import CompilerGymSolutionCodec
from optimization_lab.harness_builder.stream import ARMS, StreamItem, build_stream
from optimization_lab.harness_builder.sweperf_wrapper import (
    result_channel_capability_verdict,
)
from scripts.preflight_harness_builder_formal_providers import main as preflight_cli


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"
CODE_REVISION = "a" * 40
OLD_COMPILERGYM_REVISION = "edd202bb6bf4baadba70dfe745a9169f0a1dc597"


@pytest.fixture(autouse=True)
def _frozen_clean_code_revision(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        formal_providers,
        "_inspect_clean_code_revision",
        lambda _root: CODE_REVISION,
    )


def _canonical(payload: dict[str, object]) -> bytes:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _ready_staging(path: Path, *, marker: str | None = None) -> bytes:
    manifest = PilotManifest.from_json(MANIFEST_PATH)
    stream = build_stream(manifest)
    cells: dict[str, dict[str, int | float]] = {}
    for item in stream:
        for arm in ARMS:
            cells[f"formal:{item.suite}:{item.task_id}:{arm}"] = ResourceCaps(
                model_calls=16,
                evaluator_transactions=11,
            ).to_dict()
        cells[f"distill:{item.stream_index:03d}:{item.instance_id}"] = (
            ResourceCaps(model_calls=1).to_dict()
        )
    totals = ResourceCaps(
        model_calls=sum(value["model_calls"] for value in cells.values()),
        evaluator_transactions=sum(
            value["evaluator_transactions"] for value in cells.values()
        ),
    ).to_dict()
    source_hashes = {
        "manifest": hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()
    }
    if marker is not None:
        source_hashes["test_marker"] = hashlib.sha256(marker.encode()).hexdigest()
    payload = {
        "schema_version": 1,
        "phase_id": manifest.phase_id,
        "code_revision": CODE_REVISION,
        "model_signature": {
            "executor_model": manifest.executor_model,
            "reasoning_effort": manifest.reasoning_effort,
            "transport": manifest.model_transport,
            "client_version": manifest.client_version,
        },
        "execution_ready": True,
        "blockers": [],
        "source_hashes": source_hashes,
        "budgets": totals,
        "resource_entitlement_totals": totals,
        "cell_entitlements": cells,
        "rule_ids": ["discipline", "cross_instance_distillation"],
        "variant_ids": list(ARMS),
        "stream": [item.to_dict() for item in stream],
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    raw = _canonical(payload) + b"\n"
    path.write_bytes(raw)
    return raw


def _block_staging(path: Path, *, reason: str) -> None:
    payload = json.loads(path.read_text())
    payload["execution_ready"] = False
    payload["blockers"] = [reason]
    path.write_bytes(_canonical(payload) + b"\n")


def _blocked_swe_receipt(path: Path) -> None:
    core: dict[str, object] = {
        "schema_version": 1,
        "artifact_kind": "hb-gen1-sweperf-source-lock-prepare",
        "status": "blocked",
        "runnable_wrapper_source_lock": False,
        "blockers": [
            {
                "code": "in_process_candidate_outcome_unattestable",
                "scope": "wrapper_result_channel",
            }
        ],
        "command_trust": {
            "status": "blocked",
            "reason_code": "in_process_candidate_outcome_unattestable",
            "report_writer": "candidate_worker_uid_65534",
            "report_consumer": "root_supervisor",
            "capability_verdict": result_channel_capability_verdict().to_dict(),
        },
    }
    payload = {
        **core,
        "content_id": hashlib.sha256(_canonical(core)).hexdigest(),
    }
    path.write_bytes(_canonical(payload) + b"\n")


def _compilergym_result(name: str) -> tuple[dict[str, object], str]:
    if name.startswith("reference-"):
        task_id = name.removeprefix("reference-")
        uri = f"benchmark://cbench-v1/{task_id}"
        contract = frozen_contract(uri)
        status = "valid"
        correct = True
        result: dict[str, object] = {
            "status": status,
            "correct": correct,
            "replay_verified": True,
            "reward_validated": True,
            "semantics_validated": True,
            "contract": contract,
            "contract_sha256": hashlib.sha256(_canonical(contract)).hexdigest(),
        }
    else:
        status = {
            "empty-actions": "policy_rejected",
            "unknown-action": "policy_rejected",
            "no-effect": "no_effect",
            "forged-stdout": "policy_rejected",
        }[name]
        result = {"status": status, "correct": name == "no-effect"}
    return result, status


def _compilergym_gate(root: Path, *, code_revision: str = CODE_REVISION) -> None:
    manifest = PilotManifest.from_json(MANIFEST_PATH)
    pool = next(pool for pool in manifest.benchmarks if pool.suite == "compilergym-cbench")
    names = [f"reference-{task_id}" for task_id in pool.selected_heldout]
    names.extend(ADVERSARIAL_CANARY_IDS)
    result_hashes: list[str] = []
    cases = []
    for name in names:
        payload, status = _compilergym_result(name)
        raw = _canonical(payload) + b"\n"
        result_path = root / "private" / f"{name}.supervisor.json"
        result_path.parent.mkdir(parents=True, exist_ok=True)
        result_path.write_bytes(raw)
        digest = hashlib.sha256(raw).hexdigest()
        result_hashes.append(digest)
        cases.append({"name": name, "result_sha256": digest, "status": status})

    caps = ResourceCaps(
        evaluator_transactions=len(names),
        cpu_evaluator_seconds=300.0 * len(names),
    )
    journal = OperationJournal(
        root / "journal", anchor_path=root / "trusted-head.json"
    )
    governor = ResourceGovernor(
        journal=journal,
        global_caps=caps,
        cell_caps={"canary:compilergym-cbench": caps},
    )
    reservation = ResourceVector(
        evaluator_transactions=1, cpu_evaluator_seconds=300.0
    )
    for name, digest in zip(names, result_hashes, strict=True):
        operation_id = f"canary:compilergym-cbench:{name}"
        governor.reserve(
            operation_id=operation_id,
            cell_id="canary:compilergym-cbench",
            operation_kind="evaluator_canary",
            reservation=reservation,
        )
        governor.start(operation_id)
        governor.complete(operation_id, artifact_sha256=digest)
    replay = journal.replay()
    summary = {
        "schema_version": 1,
        "status": "passed",
        "suite": "compilergym-cbench",
        "code_revision": code_revision,
        "cases": cases,
        "committed_usage": caps.to_dict(),
        "operation_event_count": replay.event_count,
        "operation_journal_head_sha256": replay.head_sha256,
    }
    (root / "summary.json").write_bytes(_canonical(summary) + b"\n")


def _config(tmp_path: Path, staging: Path) -> FormalProviderCompositionConfig:
    swe = tmp_path / "swe-source-lock.json"
    _blocked_swe_receipt(swe)
    return FormalProviderCompositionConfig(
        project_root=ROOT,
        staging_plan_path=staging,
        manifest_path=MANIFEST_PATH,
        kernelbenchx_repository=tmp_path / "private-home-kernelbenchx",
        kernelbenchx_supervisor=tmp_path / "private-home-supervisor.py",
        kernelbenchx_scratch_root=tmp_path / "private-home-scratch",
        kernelbenchx_gpu="4",
        kernelbenchx_canary_root=tmp_path / "private-home-kbx-canary",
        compilergym_canary_root=tmp_path / "private-home-cg-canary",
        sweperf_source_lock_receipt=swe,
        component_rebind_root=tmp_path / "private-home-rebinds",
    )


def test_preflight_is_hash_only_and_current_swe_trust_boundary_blocks_factory(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)

    report = preflight_formal_providers(config)
    public = report.to_dict()

    assert report.provider_factory_ready is False
    assert report.model_calls_started == 0
    assert report.evaluator_transactions_started == 0
    swe = next(value for value in report.suites if value.suite == "swe-perf")
    assert swe.blocker_codes == (
        "sweperf_in_process_candidate_outcome_unattestable",
    )
    encoded = json.dumps(public, sort_keys=True)
    assert str(tmp_path) not in encoded
    assert "/home/" not in encoded
    assert public["external_actions"] == {
        "model_invoked": False,
        "evaluator_invoked": False,
        "gpu_used": False,
        "docker_invoked": False,
        "ssh_invoked": False,
        "network_used": False,
    }
    with pytest.raises(FormalProviderCompositionBlocked):
        compose_formal_provider_factory(config)
    with pytest.raises(TypeError, match="composition authority"):
        StagingBoundFormalProviderFactory(  # type: ignore[arg-type]
            object(), staging_plan_sha256="0" * 64, providers={}
        )


def test_compilergym_suite_gate_replays_anchor_and_binds_codec_task_and_staging(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)
    _compilergym_gate(config.compilergym_canary_root)

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "compilergym-cbench")
    assert suite.ready is True
    assert suite.gate_receipt_sha256 is not None
    assert len(suite.task_binding_core_sha256s) == 8

    provider = compose_verified_suite_provider(config, "compilergym-cbench")
    assert isinstance(provider, CompilerGymFormalSuiteProvider)
    item = next(
        value
        for value in build_stream(PilotManifest.from_json(MANIFEST_PATH))
        if value.suite == "compilergym-cbench"
    )
    binding = provider.bind(item)
    binding.validate_for(item)
    assert isinstance(binding.solution_codec, CompilerGymSolutionCodec)
    assert binding.task_binding_sha256 == suite.task_binding_core_sha256s[item.task_id]
    assert str(tmp_path) not in binding.task_card
    assert str(tmp_path) not in binding.reference_artifact
    with pytest.raises(ValueError, match="rebound"):
        binding.validate_for(
            StreamItem(
                stream_index=item.stream_index,
                block_index=item.block_index,
                suite=item.suite,
                task_id="qsort" if item.task_id != "qsort" else "bitcount",
                arm_order=item.arm_order,
            )
        )

    second_staging = tmp_path / "staging-second.json"
    _ready_staging(second_staging, marker="another-staging-segment")
    rebound = compose_verified_suite_provider(
        FormalProviderCompositionConfig(
            **{
                **config.__dict__,
                "staging_plan_path": second_staging,
            }
        ),
        "compilergym-cbench",
    ).bind(item)
    assert rebound.task_binding_sha256 != binding.task_binding_sha256


def test_verified_suite_can_be_inspected_while_campaign_staging_remains_blocked(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    _block_staging(staging, reason="another_suite_gate_pending")
    config = _config(tmp_path, staging)
    _compilergym_gate(config.compilergym_canary_root)

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "compilergym-cbench")
    assert report.staging_execution_ready is False
    assert report.provider_factory_ready is False
    assert suite.ready is True
    assert isinstance(
        compose_verified_suite_provider(config, "compilergym-cbench"),
        CompilerGymFormalSuiteProvider,
    )
    with pytest.raises(FormalProviderCompositionBlocked):
        compose_formal_provider_factory(config)


def test_canary_revision_and_independent_anchor_replay_fail_closed(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)
    _compilergym_gate(
        config.compilergym_canary_root,
        code_revision="b" * 40,
    )

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "compilergym-cbench")
    assert suite.ready is False
    with pytest.raises(FormalProviderCompositionBlocked):
        compose_verified_suite_provider(config, "compilergym-cbench")

    # Rebuild a valid summary, then mutate only the independently stored head.
    root = tmp_path / "fresh-gate"
    rebound_config = FormalProviderCompositionConfig(
        **{**config.__dict__, "compilergym_canary_root": root}
    )
    _compilergym_gate(root)
    anchor = json.loads((root / "trusted-head.json").read_text())
    anchor["head_sha256"] = "f" * 64
    (root / "trusted-head.json").write_text(json.dumps(anchor))

    report = preflight_formal_providers(rebound_config)
    suite = next(value for value in report.suites if value.suite == "compilergym-cbench")
    assert suite.ready is False
    assert suite.blocker_codes == (
        "compilergym-cbench_gate_invalid_or_incomplete",
    )


def test_exact_old_compilergym_segment_gets_content_addressed_rebind(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)
    _compilergym_gate(
        config.compilergym_canary_root,
        code_revision=OLD_COMPILERGYM_REVISION,
    )

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "compilergym-cbench")

    assert suite.ready is True
    evidence = tuple(
        (config.component_rebind_root / "compilergym-cbench").glob("*.json")
    )
    assert len(evidence) == 1
    payload = json.loads(evidence[0].read_text())
    assert evidence[0].stem == payload["content_id"]
    assert payload["old_code_revision"] == OLD_COMPILERGYM_REVISION
    assert payload["current_code_revision"] == CODE_REVISION
    assert payload["scope"] == "exact_compilergym_canary_36_event_segment_only"
    assert payload["journal_compatibility"]["event_count"] == 36
    assert payload["journal_compatibility"]["accepted_cell_ids"] == [
        "canary:compilergym-cbench"
    ]
    guard_proof = payload["journal_compatibility"][
        "current_only_pre_reserve_guard"
    ]
    assert guard_proof["affects_frozen_replay"] is False
    assert guard_proof["remains_active_for_future_reservations"] is True
    assert len(guard_proof["resource_governor_ast_sha256"]) == 64
    assert payload["external_actions"]["evaluator_invoked"] is False
    first_bytes = evidence[0].read_bytes()

    repeated = preflight_formal_providers(config)
    repeated_suite = next(
        value for value in repeated.suites if value.suite == "compilergym-cbench"
    )
    assert repeated_suite.gate_receipt_sha256 == suite.gate_receipt_sha256
    assert evidence[0].read_bytes() == first_bytes


def test_compilergym_rebind_rejects_modified_pre_reserve_guard_shape() -> None:
    source = (ROOT / "optimization_lab/harness_builder/events.py").read_bytes()
    modified = source.replace(
        b"            self.pre_reserve_guard()\n",
        b"            self.pre_reserve_guard(operation_id)\n",
        1,
    )
    assert modified != source

    with pytest.raises(ValueError, match="guard invocation differs"):
        formal_providers._normalized_events_ast(modified, current=True)


def test_obsolete_worker_authored_swe_receipt_is_never_upgraded(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)
    core: dict[str, object] = {
        "schema_version": 1,
        "artifact_kind": "hb-gen1-sweperf-source-lock-prepare",
        "status": "blocked",
        "runnable_wrapper_source_lock": False,
        "blockers": [
            {
                "code": "worker_authored_report_untrusted",
                "scope": "wrapper_result_channel",
            }
        ],
    }
    payload = {
        **core,
        "content_id": hashlib.sha256(_canonical(core)).hexdigest(),
    }
    config.sweperf_source_lock_receipt.write_bytes(_canonical(payload) + b"\n")

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "swe-perf")
    assert suite.ready is False
    assert suite.blocker_codes == (
        "sweperf_source_lock_receipt_obsolete_or_blocked",
    )


def test_swe_capability_verdict_must_match_the_current_trusted_analysis(
    tmp_path: Path,
) -> None:
    staging = tmp_path / "staging.json"
    _ready_staging(staging)
    config = _config(tmp_path, staging)
    payload = json.loads(config.sweperf_source_lock_receipt.read_text())
    payload["command_trust"]["capability_verdict"]["reason_code"] = "forged"
    core = {key: value for key, value in payload.items() if key != "content_id"}
    payload["content_id"] = hashlib.sha256(_canonical(core)).hexdigest()
    config.sweperf_source_lock_receipt.write_bytes(_canonical(payload) + b"\n")

    report = preflight_formal_providers(config)
    suite = next(value for value in report.suites if value.suite == "swe-perf")
    assert suite.ready is False
    assert suite.blocker_codes == (
        "sweperf_source_lock_receipt_obsolete_or_blocked",
    )


def test_cli_is_preflight_only_and_prints_no_operator_paths(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    artifact_root = tmp_path / "operator-private-artifacts"
    artifact_root.mkdir()
    _ready_staging(artifact_root / "staging_plan.json")
    swe = tmp_path / "operator-private-swe.json"
    _blocked_swe_receipt(swe)

    assert (
        preflight_cli(
            [
                "--artifact-root",
                str(artifact_root),
                "--project-root",
                str(ROOT),
                "--manifest",
                str(MANIFEST_PATH),
                "--kernelbenchx-repository",
                str(tmp_path / "operator-private-kbx"),
                "--kernelbenchx-supervisor",
                str(tmp_path / "operator-private-supervisor.py"),
                "--kernelbenchx-scratch-root",
                str(tmp_path / "operator-private-scratch"),
                "--sweperf-source-lock-receipt",
                str(swe),
            ]
        )
        == 0
    )
    payload = json.loads(capsys.readouterr().out)
    assert payload["provider_factory_ready"] is False
    assert payload["model_calls_started"] == 0
    assert payload["evaluator_transactions_started"] == 0
    assert str(tmp_path) not in json.dumps(payload, sort_keys=True)
