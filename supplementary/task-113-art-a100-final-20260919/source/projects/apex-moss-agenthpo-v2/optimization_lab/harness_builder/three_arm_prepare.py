from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping

from optimization_lab.registry import ExperimentRegistry

from .events import ResourceCaps
from .lcbench_canary import LCBENCH_SELECTED_INSTANCES
from .three_arm import THREE_ARMS, THREE_ARM_VALIDITY_POLICY
from .three_arm_providers import (
    COMPILERGYM_SELECTED_TASKS,
    SWEBENCH_VERIFIED_SELECTED_TASKS,
)


THREE_ARM_SUITES = (
    "yahpo-lcbench",
    "compilergym-cbench",
    "swebench-verified",
)
THREE_ARM_PHASE_ID = "hb-three-arm-live-v1"
FROZEN_MODEL_SIGNATURE = {
    "executor_model": "gpt-5.6-sol",
    "reasoning_effort": "high",
    "transport": "codex-exec-chatgpt-login",
    "client_version": "codex-cli-0.144.6",
}
SUITE_TASKS = {
    "yahpo-lcbench": LCBENCH_SELECTED_INSTANCES,
    "compilergym-cbench": COMPILERGYM_SELECTED_TASKS,
    "swebench-verified": SWEBENCH_VERIFIED_SELECTED_TASKS,
}
SUITE_CELL_CAPS = {
    "yahpo-lcbench": ResourceCaps(
        model_calls=16,
        evaluator_transactions=8,
        cpu_evaluator_seconds=2400.0,
    ),
    "compilergym-cbench": ResourceCaps(
        model_calls=16,
        evaluator_transactions=8,
        cpu_evaluator_seconds=2400.0,
    ),
    "swebench-verified": ResourceCaps(
        model_calls=16,
        evaluator_transactions=8,
        cpu_evaluator_seconds=28800.0,
    ),
}


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError(f"refusing to overwrite three-arm artifact: {path.name}")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".hb-three-arm")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def resolve_clean_revision(project_root: Path) -> str:
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    status = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    commit = revision.stdout.strip()
    if (
        revision.returncode != 0
        or len(commit) != 40
        or any(character not in "0123456789abcdef" for character in commit)
        or status.returncode != 0
        or status.stdout.strip()
    ):
        raise ValueError("three-arm prepare requires a clean full Git revision")
    return commit


def build_three_arm_stream() -> list[dict[str, object]]:
    stream: list[dict[str, object]] = []
    for block_index in range(8):
        offset = block_index % len(THREE_ARM_SUITES)
        suite_order = THREE_ARM_SUITES[offset:] + THREE_ARM_SUITES[:offset]
        for suite in suite_order:
            task_id = SUITE_TASKS[suite][block_index]
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


def build_three_arm_cell_caps(
    stream: list[dict[str, object]],
) -> dict[str, ResourceCaps]:
    cells: dict[str, ResourceCaps] = {}
    for item in stream:
        suite = str(item["suite"])
        task_id = str(item["task_id"])
        for arm in THREE_ARMS:
            cells[f"formal:{suite}:{task_id}:{arm}"] = SUITE_CELL_CAPS[suite]
        if item["learning_mode"] == "online":
            cells[
                f"distill:{int(item['stream_index']):03d}:{item['instance_id']}"
            ] = ResourceCaps(model_calls=1)
    return cells


def _sum_caps(cells: Mapping[str, ResourceCaps]) -> ResourceCaps:
    return ResourceCaps(
        model_calls=sum(cap.model_calls for cap in cells.values()),
        evaluator_transactions=sum(
            cap.evaluator_transactions for cap in cells.values()
        ),
        gpu_exclusive_seconds=sum(
            cap.gpu_exclusive_seconds for cap in cells.values()
        ),
        cpu_evaluator_seconds=sum(
            cap.cpu_evaluator_seconds for cap in cells.values()
        ),
    )


def prepare_three_arm_campaign(
    *,
    project_root: Path,
    artifact_root: Path,
    code_revision: str,
    rule_registry_path: Path,
    suite_gate_summaries: Mapping[str, Path],
    source_paths: Mapping[str, Path],
) -> dict[str, Any]:
    project_root = project_root.resolve(strict=True)
    artifact_root = artifact_root.resolve()
    if code_revision != resolve_clean_revision(project_root):
        raise ValueError("observed code revision differs from the clean worktree")
    observed_version = subprocess.run(
        ["codex", "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if (
        observed_version.returncode != 0
        or observed_version.stdout.strip() != "codex-cli 0.144.6"
    ):
        raise ValueError("installed Codex CLI differs from the frozen client")
    if set(suite_gate_summaries) != set(THREE_ARM_SUITES):
        raise ValueError("three-arm prepare requires one gate summary per suite")
    gate_hashes: dict[str, str] = {}
    for suite, raw_path in suite_gate_summaries.items():
        path = raw_path.resolve(strict=True)
        summary = json.loads(path.read_text(encoding="utf-8"))
        if (
            not isinstance(summary, dict)
            or summary.get("suite") != suite
            or summary.get("passed") is not True
        ):
            raise ValueError(f"three-arm suite gate has not passed: {suite}")
        gate_hashes[f"gate:{suite}"] = _sha(path)
    registry_path = rule_registry_path.resolve(strict=True)
    source_hashes = {
        "rule_registry": _sha(registry_path),
        **gate_hashes,
    }
    for name, raw_path in sorted(source_paths.items()):
        path = raw_path.resolve(strict=True)
        source_hashes[f"source:{name}"] = _sha(path)
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    rule_ids = [item["rule_id"] for item in registry["rules"]]
    required_rules = {
        "contract_compatibility",
        "discipline",
        "dream",
        "law_inversion",
        "recombination",
        "correctness_recovery",
        "cross_instance_distillation",
    }
    if not required_rules <= set(rule_ids):
        raise ValueError("three-arm Rule Registry lacks required rules")
    stream = build_three_arm_stream()
    cells = build_three_arm_cell_caps(stream)
    totals = _sum_caps(cells)
    expected_totals = ResourceCaps(
        model_calls=1170,
        evaluator_transactions=576,
        cpu_evaluator_seconds=806400.0,
    )
    if totals != expected_totals:
        raise ValueError("three-arm entitlement arithmetic differs")
    payload = {
        "schema_version": 5,
        "phase_id": THREE_ARM_PHASE_ID,
        "code_revision": code_revision,
        "model_signature": FROZEN_MODEL_SIGNATURE,
        "execution_ready": True,
        "blockers": [],
        "source_hashes": source_hashes,
        "budgets": totals.to_dict(),
        "resource_entitlement_totals": totals.to_dict(),
        "cell_entitlements": {
            cell_id: caps.to_dict() for cell_id, caps in sorted(cells.items())
        },
        "rule_ids": rule_ids,
        "variant_ids": list(THREE_ARMS),
        "stream_policy": "balanced_interleaved",
        "stream": stream,
        "experience_initialization": "empty",
        "online_instances_per_suite": 6,
        "sealed_instances_per_suite": 2,
        "validity_policy": THREE_ARM_VALIDITY_POLICY,
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    encoded = _canonical_bytes(payload)
    staging_path = artifact_root / "staging_plan.json"
    _write_once(staging_path, encoded)
    staging_sha = hashlib.sha256(encoded).hexdigest()
    ExperimentRegistry(artifact_root).append(
        "hb_three_arm_staging_prepared",
        {
            "phase_id": THREE_ARM_PHASE_ID,
            "staging_plan_sha256": staging_sha,
            "source_hashes": source_hashes,
            "execution_ready": True,
        },
        event_id=f"hb-three-arm-staging:{staging_sha}",
    )
    return payload


__all__ = [
    "FROZEN_MODEL_SIGNATURE",
    "SUITE_CELL_CAPS",
    "SUITE_TASKS",
    "THREE_ARM_PHASE_ID",
    "THREE_ARM_SUITES",
    "build_three_arm_cell_caps",
    "build_three_arm_stream",
    "prepare_three_arm_campaign",
    "resolve_clean_revision",
]
