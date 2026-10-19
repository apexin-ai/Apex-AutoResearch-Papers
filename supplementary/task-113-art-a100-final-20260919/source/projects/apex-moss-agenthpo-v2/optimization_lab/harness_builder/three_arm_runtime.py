from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
from dataclasses import asdict
from pathlib import Path
from typing import Mapping

from optimization_lab.codex_generator import CodexExecGenerator

from .events import OperationJournal, ResourceGovernor
from .learning import BuilderCheckpoint, ExperienceBankSnapshot
from .model_gateway import IsolatedModelGateway
from .operators import TrustedOperatorRegistry
from .schema import BuilderVariant, RuleRegistry
from .three_arm import ThreeArmCampaignContract, ThreeArmCampaignRunner
from .three_arm_providers import (
    CompilerGymFormalSuiteProviderV2,
    LCBenchFormalSuiteProvider,
    SWEBenchVerifiedFormalSuiteProvider,
    ThreeArmProviderFactory,
)


EXECUTABLE_RULES = (
    "contract_compatibility",
    "discipline",
    "dream",
    "law_inversion",
    "recombination",
    "correctness_recovery",
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_signing_key(path: Path) -> bytes:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        try:
            key = os.urandom(32)
            os.write(descriptor, key)
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    mode = stat.S_IMODE(path.stat().st_mode)
    if mode != 0o600:
        raise ValueError("model capability key must be mode 0600")
    key = path.read_bytes()
    if len(key) != 32:
        raise ValueError("model capability key must contain exactly 32 bytes")
    return key


def _verify_runtime_sources(
    *, staging_path: Path, project_root: Path, source_paths: Mapping[str, Path]
) -> dict[str, object]:
    staging = json.loads(staging_path.read_text(encoding="utf-8"))
    if not isinstance(staging, dict):
        raise ValueError("three-arm staging plan must be an object")
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    ).stdout.strip()
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    ).stdout.strip()
    if revision != staging.get("code_revision") or status:
        raise ValueError("runtime worktree differs from the frozen clean revision")
    frozen = staging.get("source_hashes")
    if not isinstance(frozen, dict):
        raise ValueError("staging source hashes are missing")
    expected_keys = {key for key in frozen if key.startswith("source:")}
    observed_keys = {f"source:{name}" for name in source_paths}
    if observed_keys != expected_keys:
        raise ValueError("runtime source path set differs from staging")
    for name, raw_path in source_paths.items():
        path = raw_path.resolve(strict=True)
        if _sha(path) != frozen[f"source:{name}"]:
            raise ValueError(f"runtime source hash differs: {name}")
    return staging


def build_three_arm_runner(
    *,
    artifact_root: Path,
    staging_path: Path,
    project_root: Path,
    rule_registry_path: Path,
    source_paths: Mapping[str, Path],
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
    project_root = project_root.resolve(strict=True)
    staging = _verify_runtime_sources(
        staging_path=staging_path,
        project_root=project_root,
        source_paths=source_paths,
    )
    contract = ThreeArmCampaignContract.from_staging_path(staging_path)
    contract.require_executable()
    registry_path = rule_registry_path.resolve(strict=True)
    registry_sha = _sha(registry_path)
    if staging["source_hashes"].get("rule_registry") != registry_sha:
        raise ValueError("runtime Rule Registry hash differs from staging")
    registry = RuleRegistry.from_json(registry_path)
    if not set(EXECUTABLE_RULES) <= set(registry.executable_rule_ids):
        raise ValueError("runtime Rule Registry lacks the frozen executable rules")
    operator_registry = TrustedOperatorRegistry(
        rule_registry_sha256=registry_sha,
        rule_registry=registry,
    )

    heldout = tuple(item.instance_id for item in contract.stream)
    common = {
        "rule_registry_sha256": registry_sha,
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
    empty_bank = ExperienceBankSnapshot.create(
        bank_id="hb-three-arm-empty-v1", parent_sha256=None, records=()
    )
    empty_parent = hashlib.sha256(
        b'{"kind":"empty-task-conditioned-builder","schema_version":1}\n'
    ).hexdigest()
    empty_checkpoint = BuilderCheckpoint(
        parent_checkpoint_sha256=empty_parent,
        experience_bank_sha256=empty_bank.sha256,
        rule_registry_sha256=registry_sha,
        learned_through_instance="initial-empty",
        stream_index=0,
    )
    governor = ResourceGovernor(
        journal=OperationJournal(
            artifact_root / "control" / "operations",
            anchor_path=artifact_root / "control" / "trusted-operation-head.json",
        ),
        global_caps=contract.global_caps,
        cell_caps=contract.cell_entitlements,
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
    providers = {
        "yahpo-lcbench": LCBenchFormalSuiteProvider(
            staging_plan_sha256=contract.staging_plan_sha256,
            canary_summary_path=lcbench_canary_summary,
            data_root=lcbench_data_root,
            settings_path=lcbench_settings,
            python_executable=lcbench_python,
        ),
        "compilergym-cbench": CompilerGymFormalSuiteProviderV2(
            staging_plan_sha256=contract.staging_plan_sha256,
            canary_summary_path=compilergym_canary_summary,
            python_executable=compilergym_python,
            project_root=project_root,
            site_data_root=compilergym_site_data_root,
            cache_root=compilergym_cache_root,
            compatibility_library_root=compilergym_compatibility_library_root,
        ),
        "swebench-verified": SWEBenchVerifiedFormalSuiteProvider(
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
        ),
    }
    factory = ThreeArmProviderFactory(
        staging_plan_sha256=contract.staging_plan_sha256,
        providers=providers,
    )
    return ThreeArmCampaignRunner(
        artifact_root=artifact_root,
        contract=contract,
        variants=variants,
        operator_registry=operator_registry,
        model_gateway=gateway,
        provider_factory=factory,
        initial_empty_bank=empty_bank,
        initial_empty_checkpoint=empty_checkpoint,
        task_conditioned_checkpoint_sha256=empty_parent,
    )


def result_payload(result) -> dict[str, object]:
    return asdict(result)


__all__ = ["EXECUTABLE_RULES", "build_three_arm_runner", "result_payload"]
