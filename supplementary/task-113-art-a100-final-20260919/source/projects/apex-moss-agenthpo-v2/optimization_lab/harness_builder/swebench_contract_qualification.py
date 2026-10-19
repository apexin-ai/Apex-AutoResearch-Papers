from __future__ import annotations

import hashlib
import json
import os
import stat
import tempfile
from pathlib import Path
from typing import Any, Mapping

from optimization_lab.codex_generator import CodexExecGenerator

from .events import OperationJournal, ResourceCaps, ResourceGovernor
from .model_gateway import IsolatedModelGateway
from .operators import PublicAttempt, TrustedOperatorRegistry
from .runner import HarnessBuilderCellRunner
from .schema import BuilderVariant, RuleRegistry
from .three_arm import ThreeArmCampaignContract
from .three_arm_providers import SWEBenchVerifiedFormalSuiteProvider
from .three_arm_runtime import EXECUTABLE_RULES, _verify_runtime_sources


QUALIFICATION_TASK_ID = "sphinx-doc__sphinx-8459"
MINIMUM_VALID_ROUNDS = 4


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, payload: dict[str, Any]) -> None:
    encoded = (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    if path.exists():
        if path.read_bytes() != encoded:
            raise ValueError("qualification summary is already bound to other content")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        dir=path.parent, suffix=".qualification.tmp"
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def _load_signing_key(path: Path) -> bytes:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        try:
            os.write(descriptor, os.urandom(32))
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    if stat.S_IMODE(path.stat().st_mode) != 0o600:
        raise ValueError("qualification model capability key must be mode 0600")
    key = path.read_bytes()
    if len(key) != 32:
        raise ValueError("qualification model capability key must contain 32 bytes")
    return key


def build_qualification_summary(
    *,
    attempts: tuple[PublicAttempt, ...],
    staging_plan_sha256: str,
    code_revision: str,
    rule_registry_sha256: str,
    task_binding_sha256: str,
    cell_id: str,
) -> dict[str, Any]:
    if len(attempts) != 8:
        raise ValueError("SWE-bench contract qualification requires eight attempts")
    values = [
        float(attempt.score)
        for attempt in attempts
        if attempt.correct and attempt.score is not None
    ]
    sufficient = len(values) >= MINIMUM_VALID_ROUNDS
    return {
        "schema_version": 1,
        "purpose": "swebench_contract_compatibility_preformal_qualification",
        "staging_plan_sha256": staging_plan_sha256,
        "code_revision": code_revision,
        "rule_registry_sha256": rule_registry_sha256,
        "task_id": QUALIFICATION_TASK_ID,
        "task_binding_sha256": task_binding_sha256,
        "cell_id": cell_id,
        "attempted_rounds": len(attempts),
        "valid_rounds": len(values),
        "invalid_rounds": len(attempts) - len(values),
        "minimum_valid_rounds": MINIMUM_VALID_ROUNDS,
        "validity_status": (
            "sufficient_validity" if sufficient else "insufficient_validity"
        ),
        "valid_only_mean": sum(values) / len(values) if sufficient else None,
        "best_score": max(values) if sufficient else None,
        "round_outcomes": [attempt.outcome for attempt in attempts],
        "formal_score_reuse_forbidden": True,
        "may_start_formal_stream": sufficient,
        "sealed": True,
    }


def run_swebench_contract_qualification(
    *,
    project_root: Path,
    artifact_root: Path,
    staging_path: Path,
    rule_registry_path: Path,
    source_paths: Mapping[str, Path],
    canary_summary_path: Path,
    dataset_path: Path,
    selection_path: Path,
    image_lock_path: Path,
    host_alias: str,
    remote_python: str,
    remote_project_root: str,
    remote_swebench_source_root: str,
    remote_attempt_root: str,
    codex_executable: str = "codex",
) -> dict[str, Any]:
    project_root = project_root.resolve(strict=True)
    artifact_root = artifact_root.resolve()
    staging_path = staging_path.resolve(strict=True)
    staging = _verify_runtime_sources(
        staging_path=staging_path,
        project_root=project_root,
        source_paths=source_paths,
    )
    contract = ThreeArmCampaignContract.from_staging_path(staging_path)
    contract.require_executable()
    item = next(
        (
            candidate
            for candidate in contract.stream
            if candidate.suite == "swebench-verified"
            and candidate.task_id == QUALIFICATION_TASK_ID
        ),
        None,
    )
    if item is None:
        raise ValueError("qualification task is absent from the frozen staging stream")
    registry_path = rule_registry_path.resolve(strict=True)
    registry_sha = _sha(registry_path)
    if staging["source_hashes"].get("rule_registry") != registry_sha:
        raise ValueError("qualification Rule Registry differs from staging")
    registry = RuleRegistry.from_json(registry_path)
    if tuple(registry.executable_rule_ids) != EXECUTABLE_RULES:
        raise ValueError("qualification executable rule set differs")

    provider = SWEBenchVerifiedFormalSuiteProvider(
        staging_plan_sha256=contract.staging_plan_sha256,
        canary_summary_path=canary_summary_path,
        dataset_path=dataset_path,
        selection_path=selection_path,
        image_lock_path=image_lock_path,
        host_alias=host_alias,
        remote_python=remote_python,
        remote_project_root=remote_project_root,
        remote_swebench_source_root=remote_swebench_source_root,
        remote_attempt_root=remote_attempt_root,
    )
    binding = provider.bind(item)
    cell_id = (
        "qualification:swebench-verified:"
        + QUALIFICATION_TASK_ID
        + ":contract-compatibility"
    )
    caps = ResourceCaps(
        model_calls=16,
        evaluator_transactions=8,
        cpu_evaluator_seconds=28800.0,
    )
    governor = ResourceGovernor(
        journal=OperationJournal(
            artifact_root / "control" / "operations",
            anchor_path=artifact_root / "control" / "trusted-operation-head.json",
        ),
        global_caps=caps,
        cell_caps={cell_id: caps},
    )

    def transport_factory(work_root: Path, output_mode: str) -> CodexExecGenerator:
        return CodexExecGenerator(
            work_root=work_root,
            executable=codex_executable,
            reasoning_effort="high",
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
    variant = BuilderVariant(
        variant_id="contract-repair",
        description="preformal adaptive Harness contract qualification",
        freeze_after_initial=False,
        continual_update=False,
        rule_registry_sha256=registry_sha,
        allowed_rule_ids=EXECUTABLE_RULES,
        experience_sources=(),
        excluded_task_ids=(),
    )
    result = HarnessBuilderCellRunner(
        artifact_root=artifact_root / "cell",
        cell_id=cell_id,
        instance_id=item.instance_id,
        suite=item.suite,
        task_card=binding.task_card,
        reference_artifact=binding.reference_artifact,
        variant=variant,
        operator_registry=TrustedOperatorRegistry(
            rule_registry_sha256=registry_sha,
            rule_registry=registry,
        ),
        model_gateway=gateway,
        model=contract.model,
        solution_codec=binding.solution_codec,
        evaluator=binding.evaluator,
        rounds=8,
        operation_prefix="qualification-op:"
        + hashlib.sha256(cell_id.encode()).hexdigest(),
    ).run()
    if not result.sealed:
        raise RuntimeError("qualification cell did not seal eight attempts")
    summary = build_qualification_summary(
        attempts=result.attempts,
        staging_plan_sha256=contract.staging_plan_sha256,
        code_revision=str(staging["code_revision"]),
        rule_registry_sha256=registry_sha,
        task_binding_sha256=binding.task_binding_sha256,
        cell_id=cell_id,
    )
    _write_once(artifact_root / "qualification_summary.json", summary)
    return summary


__all__ = [
    "MINIMUM_VALID_ROUNDS",
    "QUALIFICATION_TASK_ID",
    "build_qualification_summary",
    "run_swebench_contract_qualification",
]
