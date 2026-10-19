"""Runtime composition for the schema-v6 three-arm successor segment."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Mapping

from optimization_lab.codex_generator import CodexExecGenerator

from .events import OperationJournal, ResourceGovernor
from .experience import ExperienceRecord
from .learning import BuilderCheckpoint, ExperienceBankSnapshot
from .model_gateway import IsolatedModelGateway
from .operators import TrustedOperatorRegistry
from .schema import BuilderVariant, RuleRegistry
from .three_arm import ThreeArmCampaignRunner
from .three_arm_continuation import (
    ThreeArmContinuationContract,
    ThreeArmContinuationSourceGuard,
    ThreeArmContinuationSourceSnapshot,
    verify_three_arm_continuation_source,
)
from .three_arm_prepare import FROZEN_MODEL_SIGNATURE, THREE_ARM_SUITES
from .three_arm_providers import (
    CompilerGymFormalSuiteProviderV2,
    LCBenchFormalSuiteProvider,
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    SWEBenchVerifiedFormalSuiteProvider,
    ThreeArmProviderFactory,
)
from .three_arm_runtime import (
    EXECUTABLE_RULES,
    _load_signing_key,
    _verify_runtime_sources,
)
from .three_arm_v1r9_prepare import (
    _CODEX_EXECUTABLE_SOURCE_PREFIX,
    V1R9_COMPOSITE_HARD_CAPS,
    V1R9_EXECUTION_START_INDEX,
    V1R9_EXECUTION_STOP_INDEX,
    V1R9_PHASE_ID,
    V1R9_SUFFIX_ENTITLEMENT_TOTALS,
    build_three_arm_v1r9_cell_caps,
    build_three_arm_v1r9_stream,
    resolve_v1r9_codex_executable,
)
from .swebench_qualification_transfer import (
    verify_swebench_qualification_transfer,
)
from .swebench_remote_deployment import (
    verify_swebench_remote_deployment_receipt,
)


@dataclass(frozen=True)
class V1R9InitialState:
    empty_bank: ExperienceBankSnapshot
    empty_checkpoint: BuilderCheckpoint
    task_conditioned_checkpoint_sha256: str
    online_bank: ExperienceBankSnapshot
    online_checkpoint: BuilderCheckpoint


@dataclass(frozen=True)
class V1R9RuntimePreflight:
    contract: ThreeArmContinuationContract
    source_snapshot: ThreeArmContinuationSourceSnapshot
    source_guard: Callable[[], None]
    initial_state: V1R9InitialState
    qualification_transfer: Mapping[str, Any]
    remote_deployment: Mapping[str, Any]
    codex_executable_path: Path
    codex_executable_guard: Callable[[], Path]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _read_bound_source(
    source_root: Path, *, relative_path: str, expected_sha256: str
) -> bytes:
    root = source_root.resolve(strict=True)
    relative = PurePosixPath(relative_path)
    if relative.is_absolute() or ".." in relative.parts or "." in relative.parts:
        raise ValueError("v1r9 imported source path is unsafe")
    path = root.joinpath(*relative.parts)
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError) as exc:
        raise ValueError("v1r9 imported source artifact is unavailable") from exc
    current = path
    while current != root:
        if current.is_symlink():
            raise ValueError("v1r9 imported source artifact uses a symlink")
        current = current.parent
    if not resolved.is_file():
        raise ValueError("v1r9 imported source artifact is not a file")
    raw = resolved.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("v1r9 imported source artifact hash differs")
    return raw


def _load_checkpoint(raw: bytes) -> BuilderCheckpoint:
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("v1r9 imported checkpoint is invalid") from exc
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "parent_checkpoint_sha256",
        "experience_bank_sha256",
        "rule_registry_sha256",
        "learned_through_instance",
        "stream_index",
    } or payload["schema_version"] != 1:
        raise ValueError("v1r9 imported checkpoint schema differs")
    checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=payload["parent_checkpoint_sha256"],
        experience_bank_sha256=payload["experience_bank_sha256"],
        rule_registry_sha256=payload["rule_registry_sha256"],
        learned_through_instance=payload["learned_through_instance"],
        stream_index=payload["stream_index"],
    )
    if checkpoint.canonical_bytes != raw:
        raise ValueError("v1r9 imported checkpoint is not canonical")
    return checkpoint


def _load_bank(raw: bytes) -> ExperienceBankSnapshot:
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("v1r9 imported Experience Bank is invalid") from exc
    if not isinstance(payload, dict) or set(payload) != {
        "schema_version",
        "bank_id",
        "parent_sha256",
        "records",
    } or payload["schema_version"] != 1 or not isinstance(payload["records"], list):
        raise ValueError("v1r9 imported Experience Bank schema differs")
    bank = ExperienceBankSnapshot.create(
        bank_id=payload["bank_id"],
        parent_sha256=payload["parent_sha256"],
        records=tuple(ExperienceRecord.from_dict(item) for item in payload["records"]),
    )
    if bank.canonical_bytes != raw:
        raise ValueError("v1r9 imported Experience Bank is not canonical")
    return bank


def build_v1r9_initial_state(
    *,
    source_root: Path,
    source_snapshot: ThreeArmContinuationSourceSnapshot,
    rule_registry_sha256: str,
) -> V1R9InitialState:
    if rule_registry_sha256 != source_snapshot.rule_registry_sha256:
        raise ValueError("v1r9 runtime Rule Registry differs from its source")
    checkpoint = _load_checkpoint(
        _read_bound_source(
            source_root,
            relative_path=source_snapshot.online_checkpoint.relative_path,
            expected_sha256=source_snapshot.online_checkpoint.sha256,
        )
    )
    bank = _load_bank(
        _read_bound_source(
            source_root,
            relative_path=source_snapshot.online_bank.relative_path,
            expected_sha256=source_snapshot.online_bank.sha256,
        )
    )
    prefix_ids = tuple(
        item.instance_id for item in source_snapshot.prefix_instance_receipts
    )
    if (
        checkpoint.sha256 != source_snapshot.online_checkpoint.sha256
        or bank.sha256 != source_snapshot.online_bank.sha256
        or checkpoint.experience_bank_sha256 != bank.sha256
        or checkpoint.rule_registry_sha256 != rule_registry_sha256
        or checkpoint.stream_index != V1R9_EXECUTION_START_INDEX - 1
        or checkpoint.learned_through_instance != prefix_ids[-1]
        or tuple(record.source_instance_id for record in bank.records) != prefix_ids
    ):
        raise ValueError("v1r9 imported online state semantic binding differs")

    empty_bank = ExperienceBankSnapshot.create(
        bank_id="hb-three-arm-empty-v1", parent_sha256=None, records=()
    )
    task_conditioned = hashlib.sha256(
        b'{"kind":"empty-task-conditioned-builder","schema_version":1}\n'
    ).hexdigest()
    empty_checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=task_conditioned,
        experience_bank_sha256=empty_bank.sha256,
        rule_registry_sha256=rule_registry_sha256,
        learned_through_instance="initial-empty",
        stream_index=0,
    )
    return V1R9InitialState(
        empty_bank=empty_bank,
        empty_checkpoint=empty_checkpoint,
        task_conditioned_checkpoint_sha256=task_conditioned,
        online_bank=bank,
        online_checkpoint=checkpoint,
    )


def _validate_v1r9_budget(contract: ThreeArmContinuationContract) -> None:
    expected_stream = build_three_arm_v1r9_stream()
    if (
        contract.phase_id != V1R9_PHASE_ID
        or contract.model != FROZEN_MODEL_SIGNATURE["executor_model"]
    ):
        raise ValueError("v1r9 continuation identity differs")
    if [item.to_dict() for item in contract.stream] != expected_stream:
        raise ValueError("v1r9 continuation stream differs")
    expected_cells = build_three_arm_v1r9_cell_caps(expected_stream)
    if contract.cell_entitlements != expected_cells:
        raise ValueError("v1r9 continuation cell entitlements differ")
    if (
        contract.execution_start_index != V1R9_EXECUTION_START_INDEX
        or contract.execution_stop_index != V1R9_EXECUTION_STOP_INDEX
        or contract.suffix_entitlement_totals != V1R9_SUFFIX_ENTITLEMENT_TOTALS
        or contract.suffix_global_caps != V1R9_SUFFIX_ENTITLEMENT_TOTALS
        or contract.composite_hard_caps != V1R9_COMPOSITE_HARD_CAPS
    ):
        raise ValueError("v1r9 continuation execution window or budget differs")
    combined = contract.source_committed_usage + contract.suffix_entitlement_totals
    for field in (
        "model_calls",
        "evaluator_transactions",
        "gpu_exclusive_seconds",
        "cpu_evaluator_seconds",
    ):
        if getattr(combined, field) > getattr(V1R9_COMPOSITE_HARD_CAPS, field):
            raise ValueError(f"v1r9 composite {field} exceeds the original hard cap")


def _verify_swebench_remote_deployment_alignment(
    *,
    qualification_transfer: Mapping[str, Any],
    remote_deployment: Mapping[str, Any],
) -> None:
    inputs = qualification_transfer.get("v1r9_inputs")
    python_identity = remote_deployment.get("remote_python")
    if not isinstance(inputs, dict) or not isinstance(python_identity, dict):
        raise ValueError("v1r9 SWE-bench remote deployment alignment is missing")
    expected = {
        "host_alias": remote_deployment.get("host_alias"),
        "remote_python": python_identity.get("requested_path"),
        "remote_project_root": remote_deployment.get("remote_project_root"),
        "remote_swebench_source_root": remote_deployment.get(
            "remote_swebench_source_root"
        ),
    }
    if inputs.get("remote_execution_contract") != expected:
        raise ValueError(
            "v1r9 SWE-bench canary and remote deployment contracts differ"
        )


def _verify_v1r9_suite_gates(
    *,
    staging: Mapping[str, Any],
    suite_gate_paths: Mapping[str, Path],
) -> None:
    if set(suite_gate_paths) != set(THREE_ARM_SUITES):
        raise ValueError("v1r9 runtime suite gate set differs")
    source_hashes = staging.get("source_hashes")
    if not isinstance(source_hashes, dict):
        raise ValueError("v1r9 staging source hashes are missing")
    frozen_gate_keys = {key for key in source_hashes if key.startswith("gate:")}
    expected_gate_keys = {f"gate:{suite}" for suite in THREE_ARM_SUITES}
    if frozen_gate_keys != expected_gate_keys:
        raise ValueError("v1r9 staging suite gate set differs")
    for suite, raw_path in suite_gate_paths.items():
        path = raw_path.absolute()
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"v1r9 runtime suite gate is unsafe: {suite}")
        if _sha(path) != source_hashes[f"gate:{suite}"]:
            raise ValueError(f"v1r9 runtime suite gate hash differs: {suite}")


def _verify_v1r9_codex_executable(
    *, staging: Mapping[str, Any], executable: str | Path
) -> Path:
    """Fail closed unless the invoked CLI is the exact staged executable."""

    source_hashes = staging.get("source_hashes")
    signature = staging.get("model_signature")
    if not isinstance(source_hashes, dict) or signature != dict(FROZEN_MODEL_SIGNATURE):
        raise ValueError("v1r9 Codex executable staging binding is missing")
    keys = tuple(
        key
        for key in source_hashes
        if isinstance(key, str) and key.startswith(_CODEX_EXECUTABLE_SOURCE_PREFIX)
    )
    if len(keys) != 1:
        raise ValueError("v1r9 Codex executable staging binding differs")
    frozen_key = keys[0]
    frozen_path_text = frozen_key.removeprefix(_CODEX_EXECUTABLE_SOURCE_PREFIX)
    frozen_path = Path(frozen_path_text)
    frozen_sha = source_hashes[frozen_key]
    if (
        not frozen_path.is_absolute()
        or str(frozen_path) != frozen_path_text
        or not isinstance(frozen_sha, str)
        or len(frozen_sha) != 64
        or any(character not in "0123456789abcdef" for character in frozen_sha)
    ):
        raise ValueError("v1r9 Codex executable staging binding differs")
    observed = resolve_v1r9_codex_executable(executable)
    if observed.client_version != signature["client_version"]:
        raise ValueError("v1r9 Codex executable version differs")
    if observed.resolved_path != frozen_path:
        raise ValueError("v1r9 Codex executable path differs")
    if observed.sha256 != frozen_sha:
        raise ValueError("v1r9 Codex executable hash differs")
    return observed.resolved_path


def make_v1r9_resource_governor(
    *,
    artifact_root: Path,
    contract: ThreeArmContinuationContract,
    source_guard: Callable[[], None],
) -> ResourceGovernor:
    _validate_v1r9_budget(contract)
    return ResourceGovernor(
        journal=OperationJournal(
            artifact_root / "control" / "operations",
            anchor_path=artifact_root / "control" / "trusted-operation-head.json",
        ),
        global_caps=contract.suffix_global_caps,
        cell_caps=contract.cell_entitlements,
        pre_reserve_guard=source_guard,
    )


def preflight_three_arm_v1r9(
    *,
    source_root: Path,
    source_manifest_path: Path,
    source_snapshot_path: Path,
    staging_path: Path,
    expected_source_snapshot_sha256: str,
    rule_registry_path: Path,
    lcbench_gate_summary_path: Path,
    compilergym_gate_summary_path: Path,
    qualification_transfer_receipt_path: Path,
    remote_deployment_receipt_path: Path,
    swebench_task_lock_path: Path,
    swebench_selection_path: Path,
    swebench_image_lock_path: Path,
    swebench_gold_canary_summary_path: Path,
    swebench_host_alias: str,
    swebench_remote_python: str,
    swebench_remote_project_root: str,
    swebench_remote_source_root: str,
    project_root: Path,
    source_paths: Mapping[str, Path] | None = None,
    codex_executable: str | Path = "codex",
) -> V1R9RuntimePreflight:
    source_root = source_root.resolve(strict=True)
    snapshot = verify_three_arm_continuation_source(
        source_root=source_root,
        manifest_path=source_manifest_path,
        snapshot_path=source_snapshot_path,
    )
    if snapshot.sha256 != expected_source_snapshot_sha256:
        raise ValueError("v1r9 expected source snapshot binding differs")
    continuation_guard = ThreeArmContinuationSourceGuard(
        source_root=source_root,
        manifest_path=source_manifest_path,
        snapshot_path=source_snapshot_path,
        expected_snapshot_sha256=expected_source_snapshot_sha256,
    )
    continuation_guard()
    staging_path = staging_path.resolve(strict=True)
    contract = ThreeArmContinuationContract.from_staging_path(
        staging_path, source_snapshot=snapshot
    )
    contract.require_executable()
    _validate_v1r9_budget(contract)
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    if (
        staging.get("phase_id") != V1R9_PHASE_ID
        or staging.get("model_signature") != dict(FROZEN_MODEL_SIGNATURE)
        or staging.get("stream") != build_three_arm_v1r9_stream()
    ):
        raise ValueError("v1r9 staging identity differs")
    codex_path = _verify_v1r9_codex_executable(
        staging=staging,
        executable=codex_executable,
    )

    def codex_guard() -> Path:
        return _verify_v1r9_codex_executable(
            staging=staging,
            executable=codex_path,
        )
    if (
        staging["source_hashes"].get("continuation_source_manifest")
        != snapshot.source_manifest_sha256
        or staging["source_hashes"].get("continuation_source_snapshot")
        != snapshot.sha256
    ):
        raise ValueError("v1r9 staging source CAS bindings differ")
    suite_gate_paths = {
        "yahpo-lcbench": lcbench_gate_summary_path,
        "compilergym-cbench": compilergym_gate_summary_path,
        "swebench-verified": swebench_gold_canary_summary_path,
    }
    _verify_v1r9_suite_gates(
        staging=staging,
        suite_gate_paths=suite_gate_paths,
    )
    transfer_path = qualification_transfer_receipt_path.resolve(strict=True)
    transfer = verify_swebench_qualification_transfer(
        transfer_path,
        project_root=project_root,
        expected_new_code_revision=str(staging["code_revision"]),
        selection_path=swebench_selection_path,
        task_lock_path=swebench_task_lock_path,
        image_lock_path=swebench_image_lock_path,
        gold_canary_summary_path=swebench_gold_canary_summary_path,
    )
    transfer_sha = _sha(transfer_path)
    if (
        contract.qualification_transfer_sha256 != transfer_sha
        or staging["source_hashes"].get("swebench_qualification_transfer")
        != transfer_sha
    ):
        raise ValueError("v1r9 qualification transfer staging binding differs")
    deployment_path = remote_deployment_receipt_path.resolve(strict=True)
    deployment = verify_swebench_remote_deployment_receipt(
        deployment_path,
        project_root=project_root,
        expected_code_revision=str(staging["code_revision"]),
        host_alias=swebench_host_alias,
        remote_project_root=swebench_remote_project_root,
        remote_python=swebench_remote_python,
        remote_swebench_source_root=swebench_remote_source_root,
        reprobe=True,
    )
    _verify_swebench_remote_deployment_alignment(
        qualification_transfer=transfer,
        remote_deployment=deployment,
    )
    deployment_sha = _sha(deployment_path)
    if (
        staging["source_hashes"].get("swebench_remote_deployment")
        != deployment_sha
    ):
        raise ValueError("v1r9 remote deployment staging binding differs")

    if source_paths is not None:
        _verify_runtime_sources(
            staging_path=staging_path,
            project_root=project_root.resolve(strict=True),
            source_paths=source_paths,
        )
    registry_path = rule_registry_path.resolve(strict=True)
    registry_sha = _sha(registry_path)
    if (
        staging["source_hashes"].get("rule_registry") != registry_sha
        or registry_sha != snapshot.rule_registry_sha256
    ):
        raise ValueError("v1r9 runtime Rule Registry hash differs")
    staging_rule_ids = staging.get("rule_ids")
    registry_payload = json.loads(registry_path.read_text(encoding="utf-8"))
    registry_rule_ids = [item["rule_id"] for item in registry_payload["rules"]]
    if staging_rule_ids != registry_rule_ids:
        raise ValueError("v1r9 runtime Rule Registry rule list differs")

    def guard() -> None:
        continuation_guard()
        codex_guard()
        verified_transfer = verify_swebench_qualification_transfer(
            transfer_path,
            project_root=project_root,
            expected_new_code_revision=str(staging["code_revision"]),
            selection_path=swebench_selection_path,
            task_lock_path=swebench_task_lock_path,
            image_lock_path=swebench_image_lock_path,
            gold_canary_summary_path=swebench_gold_canary_summary_path,
        )
        if verified_transfer != transfer or _sha(transfer_path) != transfer_sha:
            raise ValueError("v1r9 qualification transfer changed after preflight")
        verified_deployment = verify_swebench_remote_deployment_receipt(
            deployment_path,
            project_root=project_root,
            expected_code_revision=str(staging["code_revision"]),
            host_alias=swebench_host_alias,
            remote_project_root=swebench_remote_project_root,
            remote_python=swebench_remote_python,
            remote_swebench_source_root=swebench_remote_source_root,
            reprobe=True,
        )
        _verify_swebench_remote_deployment_alignment(
            qualification_transfer=verified_transfer,
            remote_deployment=verified_deployment,
        )
        if (
            verified_deployment != deployment
            or _sha(deployment_path) != deployment_sha
        ):
            raise ValueError("v1r9 remote deployment changed after preflight")
        _verify_v1r9_suite_gates(
            staging=staging,
            suite_gate_paths=suite_gate_paths,
        )
        if _sha(registry_path) != registry_sha:
            raise ValueError("v1r9 Rule Registry changed after preflight")
        if source_paths is not None:
            _verify_runtime_sources(
                staging_path=staging_path,
                project_root=project_root.resolve(strict=True),
                source_paths=source_paths,
            )
    initial_state = build_v1r9_initial_state(
        source_root=source_root,
        source_snapshot=snapshot,
        rule_registry_sha256=registry_sha,
    )
    return V1R9RuntimePreflight(
        contract=contract,
        source_snapshot=snapshot,
        source_guard=guard,
        initial_state=initial_state,
        qualification_transfer=transfer,
        remote_deployment=deployment,
        codex_executable_path=codex_path,
        codex_executable_guard=codex_guard,
    )


def v1r9_dry_run_payload(
    *,
    contract: ThreeArmContinuationContract,
    source_snapshot: ThreeArmContinuationSourceSnapshot,
) -> dict[str, object]:
    _validate_v1r9_budget(contract)
    if contract.source_snapshot_sha256 != source_snapshot.sha256:
        raise ValueError("v1r9 dry-run source snapshot differs")
    return {
        "schema_version": 1,
        "phase": contract.phase_id,
        "execution_ready": contract.execution_ready,
        "staging_plan_sha256": contract.staging_plan_sha256,
        "source_snapshot_sha256": source_snapshot.sha256,
        "qualification_transfer_sha256": contract.qualification_transfer_sha256,
        "qualification_transfer_passed": True,
        "formal_score_reuse": False,
        "logical_stream_instances": len(contract.stream),
        "execution_start_index": contract.execution_start_index,
        "active_stream_instances": len(contract.active_stream),
        "arms": list(contract.arms),
        "suffix_entitlements": contract.suffix_entitlement_totals.to_dict(),
        "source_committed_usage": contract.source_committed_usage.to_dict(),
        "composite_hard_caps": contract.composite_hard_caps.to_dict(),
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
        "no_next_phase": True,
    }


def build_three_arm_v1r9_runner(
    *,
    artifact_root: Path,
    staging_path: Path,
    project_root: Path,
    source_root: Path,
    source_manifest_path: Path,
    source_snapshot_path: Path,
    expected_source_snapshot_sha256: str,
    rule_registry_path: Path,
    source_paths: Mapping[str, Path],
    qualification_transfer_receipt_path: Path,
    remote_deployment_receipt_path: Path,
    swebench_task_lock_path: Path,
    lcbench_canary_summary: Path,
    lcbench_data_root: Path,
    lcbench_settings: Path,
    lcbench_python: Path,
    compilergym_canary_summary: Path,
    compilergym_python: Path,
    compilergym_site_data_root: Path,
    compilergym_cache_root: Path,
    compilergym_compatibility_library_root: Path,
    swebench_canary_summary: Path,
    swebench_dataset: Path,
    swebench_selection: Path,
    swebench_image_lock: Path,
    swebench_host_alias: str,
    swebench_remote_python: str,
    swebench_remote_project_root: str,
    swebench_remote_source_root: str,
    swebench_remote_attempt_root: str,
    codex_executable: str = "codex",
) -> ThreeArmCampaignRunner:
    artifact_root = artifact_root.resolve()
    staging_path = staging_path.resolve(strict=True)
    if artifact_root != staging_path.parent:
        raise ValueError("v1r9 artifact root must equal the staging plan parent")
    source_root = source_root.resolve(strict=True)
    if artifact_root == source_root or artifact_root.is_relative_to(source_root):
        raise ValueError("v1r9 runtime artifact root overlaps its frozen source")
    preflight = preflight_three_arm_v1r9(
        source_root=source_root,
        source_manifest_path=source_manifest_path,
        source_snapshot_path=source_snapshot_path,
        staging_path=staging_path,
        expected_source_snapshot_sha256=expected_source_snapshot_sha256,
        rule_registry_path=rule_registry_path,
        lcbench_gate_summary_path=lcbench_canary_summary,
        compilergym_gate_summary_path=compilergym_canary_summary,
        project_root=project_root,
        source_paths=source_paths,
        qualification_transfer_receipt_path=qualification_transfer_receipt_path,
        remote_deployment_receipt_path=remote_deployment_receipt_path,
        swebench_task_lock_path=swebench_task_lock_path,
        swebench_selection_path=swebench_selection,
        swebench_image_lock_path=swebench_image_lock,
        swebench_gold_canary_summary_path=swebench_canary_summary,
        swebench_host_alias=swebench_host_alias,
        swebench_remote_python=swebench_remote_python,
        swebench_remote_project_root=swebench_remote_project_root,
        swebench_remote_source_root=swebench_remote_source_root,
        codex_executable=codex_executable,
    )
    contract = preflight.contract
    registry = RuleRegistry.from_json(rule_registry_path.resolve(strict=True))
    if not set(EXECUTABLE_RULES) <= set(registry.executable_rule_ids):
        raise ValueError("v1r9 Rule Registry lacks frozen executable rules")
    operator_registry = TrustedOperatorRegistry(
        rule_registry_sha256=preflight.source_snapshot.rule_registry_sha256,
        rule_registry=registry,
    )

    heldout = tuple(item.instance_id for item in contract.stream)
    common = {
        "rule_registry_sha256": preflight.source_snapshot.rule_registry_sha256,
        "allowed_rule_ids": EXECUTABLE_RULES,
        "experience_sources": (),
    }
    variants = (
        BuilderVariant(
            variant_id="A",
            description="one task-conditioned Harness frozen after v001",
            freeze_after_initial=True,
            continual_update=False,
            excluded_task_ids=(),
            **common,
        ),
        BuilderVariant(
            variant_id="B-frozen",
            description="adaptive within-task Builder without cross-task memory",
            freeze_after_initial=False,
            continual_update=False,
            excluded_task_ids=heldout,
            **common,
        ),
        BuilderVariant(
            variant_id="B-online",
            description="adaptive Builder with post-seal test-then-learn memory",
            freeze_after_initial=False,
            continual_update=True,
            excluded_task_ids=heldout,
            **common,
        ),
    )
    governor = make_v1r9_resource_governor(
        artifact_root=artifact_root,
        contract=contract,
        source_guard=preflight.source_guard,
    )

    def transport_factory(work_root: Path, output_mode: str) -> CodexExecGenerator:
        executable_path = preflight.codex_executable_guard()
        return CodexExecGenerator(
            work_root=work_root,
            executable=str(executable_path),
            reasoning_effort="high",
            timeout_seconds=900,
            output_mode=output_mode,
        )

    gateway = IsolatedModelGateway(
        artifact_root=artifact_root / "model-gateway",
        governor=governor,
        transport_factory=transport_factory,
        signing_key=_load_signing_key(
            artifact_root / "private-controller" / "model-capability.key"
        ),
    )
    providers = {
        THREE_ARM_SUITES[0]: LCBenchFormalSuiteProvider(
            staging_plan_sha256=contract.staging_plan_sha256,
            canary_summary_path=lcbench_canary_summary,
            data_root=lcbench_data_root,
            settings_path=lcbench_settings,
            python_executable=lcbench_python,
        ),
        THREE_ARM_SUITES[1]: CompilerGymFormalSuiteProviderV2(
            staging_plan_sha256=contract.staging_plan_sha256,
            canary_summary_path=compilergym_canary_summary,
            python_executable=compilergym_python,
            project_root=project_root,
            site_data_root=compilergym_site_data_root,
            cache_root=compilergym_cache_root,
            compatibility_library_root=compilergym_compatibility_library_root,
        ),
        THREE_ARM_SUITES[2]: SWEBenchVerifiedFormalSuiteProvider(
            staging_plan_sha256=contract.staging_plan_sha256,
            canary_summary_path=swebench_canary_summary,
            dataset_path=swebench_dataset,
            selection_path=swebench_selection,
            image_lock_path=swebench_image_lock,
            host_alias=swebench_host_alias,
            remote_python=swebench_remote_python,
            remote_project_root=swebench_remote_project_root,
            remote_swebench_source_root=swebench_remote_source_root,
            remote_attempt_root=swebench_remote_attempt_root,
            selection_mode=SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
            expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
        ),
    }
    factory = ThreeArmProviderFactory(
        staging_plan_sha256=contract.staging_plan_sha256,
        providers=providers,
    )
    initial = preflight.initial_state
    return ThreeArmCampaignRunner(
        artifact_root=artifact_root,
        contract=contract,  # type: ignore[arg-type]
        variants=variants,
        operator_registry=operator_registry,
        model_gateway=gateway,
        provider_factory=factory,
        initial_empty_bank=initial.empty_bank,
        initial_empty_checkpoint=initial.empty_checkpoint,
        task_conditioned_checkpoint_sha256=(
            initial.task_conditioned_checkpoint_sha256
        ),
        execution_start_index=V1R9_EXECUTION_START_INDEX,
        initial_online_bank=initial.online_bank,
        initial_online_checkpoint=initial.online_checkpoint,
    )


__all__ = [
    "V1R9InitialState",
    "V1R9RuntimePreflight",
    "build_three_arm_v1r9_runner",
    "build_v1r9_initial_state",
    "make_v1r9_resource_governor",
    "preflight_three_arm_v1r9",
    "v1r9_dry_run_payload",
]
