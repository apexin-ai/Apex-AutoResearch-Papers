"""Prepare the immutable schema-v6 successor staging plan.

The logical stream remains 24 instances long, while the new segment owns
entitlements only for global indices 6 through 23.  The historical prefix is
referenced through a verified continuation source snapshot and is never copied
or rewritten here.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from optimization_lab.registry import ExperimentRegistry

from .events import ResourceCaps, ResourceVector
from .lcbench_canary import LCBENCH_SELECTED_INSTANCES
from .three_arm import THREE_ARMS, THREE_ARM_VALIDITY_POLICY
from .three_arm_continuation import (
    ThreeArmContinuationSourceSnapshot,
    verify_three_arm_continuation_source,
)
from .three_arm_prepare import (
    FROZEN_MODEL_SIGNATURE,
    SUITE_CELL_CAPS,
    THREE_ARM_SUITES,
    resolve_clean_revision,
)
from .three_arm_providers import (
    COMPILERGYM_SELECTED_TASKS,
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS,
)
from .swebench_qualification_transfer import (
    verify_swebench_qualification_transfer,
)
from .swebench_remote_deployment import (
    verify_swebench_remote_deployment_receipt,
)


V1R9_PHASE_ID = "hb-three-arm-live-v1r9"
V1R9_EXECUTION_START_INDEX = 6
V1R9_EXECUTION_STOP_INDEX = 24
V1R9_COMPOSITE_HARD_CAPS = ResourceCaps(
    model_calls=1170,
    evaluator_transactions=576,
    cpu_evaluator_seconds=806400.0,
)
V1R9_SUFFIX_ENTITLEMENT_TOTALS = ResourceCaps(
    model_calls=876,
    evaluator_transactions=432,
    cpu_evaluator_seconds=604800.0,
)
V1R9_SUITE_TASKS = {
    "yahpo-lcbench": LCBENCH_SELECTED_INSTANCES,
    "compilergym-cbench": COMPILERGYM_SELECTED_TASKS,
    "swebench-verified": SWEBENCH_VERIFIED_V1R9_SELECTED_TASKS,
}
_REQUIRED_RULES = {
    "contract_compatibility",
    "discipline",
    "dream",
    "law_inversion",
    "recombination",
    "correctness_recovery",
    "cross_instance_distillation",
}
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_CODEX_EXECUTABLE_SOURCE_PREFIX = "runtime:codex-executable:"


@dataclass(frozen=True)
class V1R9CodexExecutableBinding:
    """The exact executable that is permitted to back formal model calls."""

    resolved_path: Path
    sha256: str
    client_version: str

    @property
    def source_hash_key(self) -> str:
        return f"{_CODEX_EXECUTABLE_SOURCE_PREFIX}{self.resolved_path}"


def resolve_v1r9_codex_executable(
    executable: str | Path = "codex",
) -> V1R9CodexExecutableBinding:
    """Resolve, hash, and execute the frozen Codex CLI without PATH ambiguity."""

    raw = os.fspath(executable)
    if not raw or "\x00" in raw:
        raise ValueError("v1r9 Codex executable is invalid")
    if os.sep in raw:
        candidate = Path(raw).expanduser().absolute()
    else:
        discovered = shutil.which(raw)
        if discovered is None:
            raise ValueError("v1r9 Codex executable cannot be resolved")
        candidate = Path(discovered).absolute()
    try:
        resolved = candidate.resolve(strict=True)
    except OSError as exc:
        raise ValueError("v1r9 Codex executable cannot be resolved") from exc
    if not resolved.is_file() or not os.access(resolved, os.X_OK):
        raise ValueError("v1r9 Codex executable is not an executable regular file")
    before = _sha(resolved)
    try:
        observed = subprocess.run(
            [str(resolved), "--version"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ValueError("v1r9 Codex CLI version cannot be verified") from exc
    after = _sha(resolved)
    if before != after:
        raise ValueError("v1r9 Codex executable changed during verification")
    expected = FROZEN_MODEL_SIGNATURE["client_version"]
    observed_version = observed.stdout.strip()
    normalized_version = observed_version.replace("codex-cli ", "codex-cli-", 1)
    if observed.returncode != 0 or normalized_version != expected:
        raise ValueError("installed Codex CLI differs from the frozen client")
    return V1R9CodexExecutableBinding(
        resolved_path=resolved,
        sha256=before,
        client_version=normalized_version,
    )


def _canonical_bytes(payload: object) -> bytes:
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


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError(f"refusing to overwrite v1r9 artifact: {path.name}")
        return
    descriptor, name = tempfile.mkstemp(dir=path.parent, suffix=".v1r9.tmp")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def _sum_caps(cells: Mapping[str, ResourceCaps]) -> ResourceCaps:
    return ResourceCaps(
        model_calls=sum(value.model_calls for value in cells.values()),
        evaluator_transactions=sum(
            value.evaluator_transactions for value in cells.values()
        ),
        gpu_exclusive_seconds=sum(
            value.gpu_exclusive_seconds for value in cells.values()
        ),
        cpu_evaluator_seconds=sum(
            value.cpu_evaluator_seconds for value in cells.values()
        ),
    )


def _assert_within(value: ResourceVector, cap: ResourceCaps) -> None:
    for field in (
        "model_calls",
        "evaluator_transactions",
        "gpu_exclusive_seconds",
        "cpu_evaluator_seconds",
    ):
        if getattr(value, field) > getattr(cap, field):
            raise ValueError(f"v1r9 composite {field} exceeds the original hard cap")


def build_three_arm_v1r9_stream() -> list[dict[str, object]]:
    """Return the full logical stream with the accepted v1r8 prefix intact."""

    if set(V1R9_SUITE_TASKS) != set(THREE_ARM_SUITES) or any(
        len(tasks) != 8 for tasks in V1R9_SUITE_TASKS.values()
    ):
        raise ValueError("v1r9 suite task matrix differs")
    stream: list[dict[str, object]] = []
    for block_index in range(8):
        offset = block_index % len(THREE_ARM_SUITES)
        suite_order = THREE_ARM_SUITES[offset:] + THREE_ARM_SUITES[:offset]
        for suite in suite_order:
            task_id = V1R9_SUITE_TASKS[suite][block_index]
            stream_index = len(stream)
            arm_order = THREE_ARMS[stream_index % 3 :] + THREE_ARMS[: stream_index % 3]
            stream.append(
                {
                    "stream_index": stream_index,
                    "block_index": block_index,
                    "suite": suite,
                    "task_id": task_id,
                    "instance_id": f"{suite}:{task_id}",
                    "arm_order": list(arm_order),
                    "learning_mode": "online" if block_index < 6 else "sealed",
                }
            )
    return stream


def build_three_arm_v1r9_cell_caps(
    stream: Sequence[Mapping[str, object]],
) -> dict[str, ResourceCaps]:
    if len(stream) != V1R9_EXECUTION_STOP_INDEX:
        raise ValueError("v1r9 cell caps require the full logical stream")
    cells: dict[str, ResourceCaps] = {}
    for item in stream[V1R9_EXECUTION_START_INDEX:V1R9_EXECUTION_STOP_INDEX]:
        suite = str(item["suite"])
        task_id = str(item["task_id"])
        if suite not in SUITE_CELL_CAPS:
            raise ValueError("v1r9 stream contains an unknown suite")
        for arm in THREE_ARMS:
            cells[f"formal:{suite}:{task_id}:{arm}"] = SUITE_CELL_CAPS[suite]
        if item["learning_mode"] == "online":
            cells[
                f"distill:{int(item['stream_index']):03d}:{item['instance_id']}"
            ] = ResourceCaps(model_calls=1)
    totals = _sum_caps(cells)
    if totals != V1R9_SUFFIX_ENTITLEMENT_TOTALS:
        raise ValueError("v1r9 suffix entitlement arithmetic differs")
    return cells


def build_three_arm_v1r9_staging_payload(
    *,
    source_snapshot: ThreeArmContinuationSourceSnapshot,
    code_revision: str,
    rule_ids: Sequence[str],
    source_hashes: Mapping[str, str],
    codex_executable_path: str,
    codex_executable_sha256: str,
    qualification_transfer_sha256: str,
    execution_ready: bool = True,
    blockers: Sequence[str] = (),
) -> dict[str, object]:
    if not isinstance(code_revision, str) or not _COMMIT.fullmatch(code_revision):
        raise ValueError("v1r9 staging requires a full code revision")
    if (
        not isinstance(execution_ready, bool)
        or (execution_ready and blockers)
        or any(not isinstance(value, str) or not value for value in blockers)
    ):
        raise ValueError("v1r9 execution gate differs")
    if len(rule_ids) != len(set(rule_ids)) or not _REQUIRED_RULES <= set(rule_ids):
        raise ValueError("v1r9 Rule Registry lacks required rules")
    if not source_hashes or any(
        not isinstance(name, str)
        or not name
        or not isinstance(digest, str)
        or not _SHA256.fullmatch(digest)
        for name, digest in source_hashes.items()
    ):
        raise ValueError("v1r9 source hashes differ")
    if any(name.startswith(_CODEX_EXECUTABLE_SOURCE_PREFIX) for name in source_hashes):
        raise ValueError("v1r9 Codex executable source binding is duplicated")
    codex_path = Path(codex_executable_path)
    if (
        not codex_path.is_absolute()
        or str(codex_path) != codex_executable_path
        or not isinstance(codex_executable_sha256, str)
        or not _SHA256.fullmatch(codex_executable_sha256)
    ):
        raise ValueError("v1r9 Codex executable binding differs")
    if not isinstance(qualification_transfer_sha256, str) or not _SHA256.fullmatch(
        qualification_transfer_sha256
    ):
        raise ValueError("v1r9 qualification transfer SHA-256 differs")
    stream = build_three_arm_v1r9_stream()
    prefix_ids = tuple(str(item["instance_id"]) for item in stream[:6])
    snapshot_prefix = tuple(
        item.instance_id for item in source_snapshot.prefix_instance_receipts
    )
    if prefix_ids != snapshot_prefix:
        raise ValueError("v1r9 logical prefix differs from its source snapshot")
    cells = build_three_arm_v1r9_cell_caps(stream)
    totals = _sum_caps(cells)
    combined = source_snapshot.source_committed_usage + totals
    _assert_within(combined, V1R9_COMPOSITE_HARD_CAPS)
    frozen_source_hashes = dict(source_hashes)
    frozen_source_hashes[
        f"{_CODEX_EXECUTABLE_SOURCE_PREFIX}{codex_executable_path}"
    ] = codex_executable_sha256
    return {
        "schema_version": 6,
        "phase_id": V1R9_PHASE_ID,
        "code_revision": code_revision,
        "model_signature": dict(FROZEN_MODEL_SIGNATURE),
        "execution_ready": execution_ready,
        "blockers": list(blockers),
        "source_hashes": dict(sorted(frozen_source_hashes.items())),
        "budgets": totals.to_dict(),
        "resource_entitlement_totals": totals.to_dict(),
        "cell_entitlements": {
            cell_id: cap.to_dict() for cell_id, cap in sorted(cells.items())
        },
        "rule_ids": list(rule_ids),
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "stream": stream,
        "experience_initialization": "successor_continuation",
        "online_instances_per_suite": 6,
        "sealed_instances_per_suite": 2,
        "validity_policy": dict(THREE_ARM_VALIDITY_POLICY),
        "continuation": {
            "source_manifest_sha256": source_snapshot.source_manifest_sha256,
            "source_snapshot_sha256": source_snapshot.sha256,
            "source_staging_plan_sha256": (
                source_snapshot.source_staging_plan_sha256
            ),
            "prefix_length": 6,
            "execution_window": {
                "start_index": V1R9_EXECUTION_START_INDEX,
                "stop_index": V1R9_EXECUTION_STOP_INDEX,
            },
            "input_online_checkpoint_sha256": (
                source_snapshot.online_checkpoint.sha256
            ),
            "input_online_bank_sha256": source_snapshot.online_bank.sha256,
            "source_committed_usage": (
                source_snapshot.source_committed_usage.to_dict()
            ),
            "composite_hard_caps": V1R9_COMPOSITE_HARD_CAPS.to_dict(),
            "excluded_consumed_tail_operation_ids": [
                item.operation_id
                for item in source_snapshot.excluded_consumed_tail
            ],
        },
        "qualification_transfer": {
            "receipt_sha256": qualification_transfer_sha256,
            "passed": True,
            "model_calls_started": 0,
            "evaluator_transactions_started": 0,
            "formal_score_reuse": False,
        },
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }


def prepare_three_arm_v1r9_campaign(
    *,
    project_root: Path,
    artifact_root: Path,
    code_revision: str,
    source_root: Path,
    source_manifest_path: Path,
    source_snapshot_path: Path,
    rule_registry_path: Path,
    suite_gate_summaries: Mapping[str, Path],
    source_paths: Mapping[str, Path],
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
    codex_executable: str | Path = "codex",
) -> dict[str, object]:
    """Verify all immutable inputs and write one schema-v6 staging plan."""

    project_root = project_root.resolve(strict=True)
    artifact_root = artifact_root.resolve()
    source_root = source_root.resolve(strict=True)
    if artifact_root == source_root or artifact_root.is_relative_to(source_root):
        raise ValueError("v1r9 artifact root must not overlap the frozen v1r8 source")
    if code_revision != resolve_clean_revision(project_root):
        raise ValueError("observed code revision differs from the clean worktree")
    codex_binding = resolve_v1r9_codex_executable(codex_executable)

    snapshot = verify_three_arm_continuation_source(
        source_root=source_root,
        manifest_path=source_manifest_path,
        snapshot_path=source_snapshot_path,
    )
    transfer_path = qualification_transfer_receipt_path.resolve(strict=True)
    verify_swebench_qualification_transfer(
        transfer_path,
        project_root=project_root,
        expected_new_code_revision=code_revision,
        selection_path=swebench_selection_path,
        task_lock_path=swebench_task_lock_path,
        image_lock_path=swebench_image_lock_path,
        gold_canary_summary_path=swebench_gold_canary_summary_path,
    )
    transfer_sha = _sha(transfer_path)
    deployment_path = remote_deployment_receipt_path.resolve(strict=True)
    deployment = verify_swebench_remote_deployment_receipt(
        deployment_path,
        project_root=project_root,
        expected_code_revision=code_revision,
        host_alias=swebench_host_alias,
        remote_project_root=swebench_remote_project_root,
        remote_python=swebench_remote_python,
        remote_swebench_source_root=swebench_remote_source_root,
        reprobe=True,
    )
    deployment_sha = _sha(deployment_path)
    if set(suite_gate_summaries) != set(THREE_ARM_SUITES):
        raise ValueError("v1r9 prepare requires one gate summary per suite")
    gate_hashes: dict[str, str] = {}
    for suite, raw_path in suite_gate_summaries.items():
        path = raw_path.resolve(strict=True)
        summary = json.loads(path.read_text(encoding="utf-8"))
        if (
            not isinstance(summary, dict)
            or summary.get("suite") != suite
            or summary.get("passed") is not True
        ):
            raise ValueError(f"v1r9 suite gate has not passed: {suite}")
        if suite == "swebench-verified" and (
            summary.get("selection_mode")
            != SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE
            or tuple(summary.get("selected_instances", ()))
            != SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
            or summary.get("remote_execution_contract")
            != {
                "host_alias": swebench_host_alias,
                "remote_python": swebench_remote_python.rstrip("/"),
                "remote_project_root": swebench_remote_project_root.rstrip("/"),
                "remote_swebench_source_root": (
                    swebench_remote_source_root.rstrip("/")
                ),
            }
        ):
            raise ValueError("v1r9 SWE-bench active canary binding differs")
        gate_hashes[f"gate:{suite}"] = _sha(path)

    registry_path = rule_registry_path.resolve(strict=True)
    registry_sha = _sha(registry_path)
    if registry_sha != snapshot.rule_registry_sha256:
        raise ValueError("v1r9 Rule Registry differs from the imported checkpoint")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    if not isinstance(registry, dict) or not isinstance(registry.get("rules"), list):
        raise ValueError("v1r9 Rule Registry is invalid")
    rule_ids = [item["rule_id"] for item in registry["rules"]]
    source_hashes = {
        "rule_registry": registry_sha,
        "continuation_source_manifest": snapshot.source_manifest_sha256,
        "continuation_source_snapshot": snapshot.sha256,
        "swebench_qualification_transfer": transfer_sha,
        "swebench_remote_deployment": deployment_sha,
        **gate_hashes,
    }
    for name, raw_path in sorted(source_paths.items()):
        source_hashes[f"source:{name}"] = _sha(raw_path.resolve(strict=True))
    payload = build_three_arm_v1r9_staging_payload(
        source_snapshot=snapshot,
        code_revision=code_revision,
        rule_ids=rule_ids,
        source_hashes=source_hashes,
        codex_executable_path=str(codex_binding.resolved_path),
        codex_executable_sha256=codex_binding.sha256,
        qualification_transfer_sha256=transfer_sha,
    )
    encoded = _canonical_bytes(payload)
    staging_path = artifact_root / "staging_plan.json"
    _write_once(staging_path, encoded)
    staging_sha = hashlib.sha256(encoded).hexdigest()
    ExperimentRegistry(artifact_root).append(
        "hb_three_arm_v1r9_staging_prepared",
        {
            "phase_id": V1R9_PHASE_ID,
            "staging_plan_sha256": staging_sha,
            "source_manifest_sha256": snapshot.source_manifest_sha256,
            "source_snapshot_sha256": snapshot.sha256,
            "execution_start_index": V1R9_EXECUTION_START_INDEX,
            "execution_ready": True,
            "codex_executable_path": str(codex_binding.resolved_path),
            "codex_executable_sha256": codex_binding.sha256,
            "swebench_remote_deployment_sha256": deployment_sha,
            "swebench_remote_hostname": deployment["observed_remote_hostname"],
        },
        event_id=f"hb-three-arm-v1r9-staging:{staging_sha}",
    )
    return payload


__all__ = [
    "V1R9_COMPOSITE_HARD_CAPS",
    "V1R9CodexExecutableBinding",
    "V1R9_EXECUTION_START_INDEX",
    "V1R9_EXECUTION_STOP_INDEX",
    "V1R9_PHASE_ID",
    "V1R9_SUFFIX_ENTITLEMENT_TOTALS",
    "V1R9_SUITE_TASKS",
    "build_three_arm_v1r9_cell_caps",
    "build_three_arm_v1r9_staging_payload",
    "build_three_arm_v1r9_stream",
    "prepare_three_arm_v1r9_campaign",
    "resolve_v1r9_codex_executable",
]
