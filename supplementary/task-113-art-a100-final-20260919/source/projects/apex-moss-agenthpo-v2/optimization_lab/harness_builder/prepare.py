from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from optimization_lab.registry import ExperimentRegistry

from .events import ResourceCaps
from .schema import BuilderVariant, PilotManifest, RuleRegistry
from .stream import ARMS, build_stream


_DATA = Path("optimization_lab/harness_builder/data")
_COMMIT = re.compile(r"[0-9a-f]{40}")
_SOURCES = {
    "experiment_plan": Path(
        "docs/plans/2026-08-02-harness-builder-cross-benchmark-generalization.md"
    ),
    "manifest": _DATA / "hb_gen1_candidates.json",
    "rule_registry": _DATA / "rule_registry_v2.json",
    "builder_variants": _DATA / "builder_variants_v2.json",
    "experience_bank": _DATA / "experience_bank_v1.json",
    "kernelbenchx_replacement": _DATA / "kernelbenchx_replacement_v1.json",
}

_HISTORICAL_META_TRAIN = {
    "level1/40_LayerNorm.py",
    "level2/56_Matmul_Sigmoid_Sum.py",
}
_EXPECTED_ENTITLEMENT_TOTALS = {
    "model_calls": 1666,
    "evaluator_transactions": 1138,
    "gpu_exclusive_seconds": 246600.0,
    "cpu_evaluator_seconds": 1416000.0,
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def _write_once(path: Path, content: bytes) -> None:
    if path.exists():
        if path.read_bytes() != content:
            raise ValueError(f"refusing to overwrite different staging artifact: {path.name}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, suffix=".hb-gen1.tmp")
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(name).replace(path)
    except Exception:
        Path(name).unlink(missing_ok=True)
        raise


def build_hb_gen1_cell_caps(
    manifest: PilotManifest,
    experience_bank: dict[str, Any],
) -> dict[str, ResourceCaps]:
    """Build non-transferable resource envelopes for every formal operation cell."""

    suite_caps = {
        "kernelbenchx": ResourceCaps(
            model_calls=16,
            evaluator_transactions=11,
            gpu_exclusive_seconds=6600.0,
        ),
        "compilergym-cbench": ResourceCaps(
            model_calls=16,
            evaluator_transactions=11,
            cpu_evaluator_seconds=3300.0,
        ),
        "swe-perf": ResourceCaps(
            model_calls=16,
            evaluator_transactions=11,
            cpu_evaluator_seconds=39600.0,
        ),
    }
    if set(suite_caps) != {pool.suite for pool in manifest.benchmarks}:
        raise ValueError("HB-GEN-1 suite entitlement table differs from the manifest")

    cells: dict[str, ResourceCaps] = {}
    for pool in manifest.benchmarks:
        for task_id in pool.selected_heldout:
            for arm in ARMS:
                cells[f"formal:{pool.suite}:{task_id}:{arm}"] = suite_caps[pool.suite]

    source_instances = experience_bank.get("source_instances")
    if not isinstance(source_instances, list) or len(source_instances) != 8:
        raise ValueError("meta-train Experience Bank must bind exactly eight source instances")
    new_meta_train = [
        task_id for task_id in source_instances if task_id not in _HISTORICAL_META_TRAIN
    ]
    if len(new_meta_train) != 6:
        raise ValueError("meta-train must contain exactly six new KernelBench instances")
    for task_id in new_meta_train:
        cells[f"meta:kernelbench:{task_id}"] = ResourceCaps(
            model_calls=16,
            evaluator_transactions=8,
            gpu_exclusive_seconds=4800.0,
        )
    cells["meta:distillation"] = ResourceCaps(model_calls=8)

    for item in build_stream(manifest):
        cells[f"distill:{item.stream_index:03d}:{item.instance_id}"] = ResourceCaps(
            model_calls=1
        )

    cells["canary:kernelbenchx"] = ResourceCaps(
        evaluator_transactions=11,
        gpu_exclusive_seconds=6600.0,
    )
    cells["canary:compilergym-cbench"] = ResourceCaps(
        evaluator_transactions=12,
        cpu_evaluator_seconds=3600.0,
    )
    cells["canary:swe-perf"] = ResourceCaps(
        evaluator_transactions=11,
        cpu_evaluator_seconds=39600.0,
    )
    cells["canary:model-route"] = ResourceCaps(model_calls=2)
    return cells


def resolve_clean_code_revision(project_root: Path) -> str:
    project_root = project_root.resolve()
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if revision.returncode != 0 or not _COMMIT.fullmatch(revision.stdout.strip()):
        raise ValueError("HB-GEN-1 requires a pinned Git code revision")
    tracked = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=project_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if tracked.returncode != 0 or tracked.stdout.strip():
        raise ValueError("HB-GEN-1 tracked worktree must be clean before prepare")
    return revision.stdout.strip()


def resolve_model_client_version(executable: str = "codex") -> str:
    observed = subprocess.run(
        [executable, "--version"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
        check=False,
    )
    match = re.fullmatch(r"codex-cli (\d+\.\d+\.\d+)\s*", observed.stdout)
    if observed.returncode != 0 or match is None:
        raise ValueError("cannot verify the frozen Codex CLI version")
    return f"codex-cli-{match.group(1)}"


def prepare_hb_gen1(
    *,
    project_root: Path,
    artifact_root: Path,
    code_revision: str,
    observed_client_version: str,
) -> dict[str, Any]:
    project_root = project_root.resolve()
    artifact_root = artifact_root.resolve()
    if not isinstance(code_revision, str) or not _COMMIT.fullmatch(code_revision):
        raise ValueError("HB-GEN-1 code revision must be a full Git commit")
    paths = {name: project_root / relative for name, relative in _SOURCES.items()}
    for name, path in paths.items():
        if not path.is_file():
            raise FileNotFoundError(f"missing HB-GEN-1 {name}: {path}")

    manifest = PilotManifest.from_json(paths["manifest"])
    if observed_client_version != manifest.client_version:
        raise ValueError("installed Codex CLI differs from the frozen client version")
    registry = RuleRegistry.from_json(paths["rule_registry"])
    variants = BuilderVariant.list_from_json(paths["builder_variants"])
    registry_sha = _sha256(paths["rule_registry"])
    if any(variant.rule_registry_sha256 != registry_sha for variant in variants):
        raise ValueError("Builder variant does not bind the current Rule Registry")
    if {variant.variant_id for variant in variants} != {"A", "B0", "B*", "B-online"}:
        raise ValueError("HB-GEN-1 requires the frozen four-arm comparison")
    if "cross_instance_distillation" not in registry.rule_ids:
        raise ValueError("Rule Registry lacks the continual-learning skill")

    experience_bank = json.loads(paths["experience_bank"].read_text(encoding="utf-8"))
    if not isinstance(experience_bank, dict):
        raise ValueError("Experience Bank manifest must be an object")
    cell_caps = build_hb_gen1_cell_caps(manifest, experience_bank)
    entitlement_totals = {
        field: sum(getattr(value, field) for value in cell_caps.values())
        for field in (
            "model_calls",
            "evaluator_transactions",
            "gpu_exclusive_seconds",
            "cpu_evaluator_seconds",
        )
    }
    if entitlement_totals != _EXPECTED_ENTITLEMENT_TOTALS:
        raise ValueError("HB-GEN-1 resource entitlement arithmetic changed")
    if (
        entitlement_totals["model_calls"] > manifest.model_call_cap
        or entitlement_totals["evaluator_transactions"]
        > manifest.evaluator_transaction_cap
        or entitlement_totals["gpu_exclusive_seconds"]
        > manifest.gpu_exclusive_seconds_cap
        or entitlement_totals["cpu_evaluator_seconds"]
        > manifest.cpu_evaluator_seconds_cap
    ):
        raise ValueError("HB-GEN-1 cell entitlements exceed the global hard caps")

    source_hashes = {name: _sha256(path) for name, path in paths.items()}
    stream = [item.to_dict() for item in build_stream(manifest)]
    payload: dict[str, Any] = {
        "schema_version": 1,
        "phase_id": manifest.phase_id,
        "code_revision": code_revision,
        "model_signature": {
            "executor_model": manifest.executor_model,
            "reasoning_effort": manifest.reasoning_effort,
            "transport": manifest.model_transport,
            "client_version": manifest.client_version,
        },
        "execution_ready": False,
        "blockers": [
            "model_runtime_canary_pending",
            "meta_train_pending",
            "evaluator_canaries_pending",
        ],
        "source_hashes": source_hashes,
        "budgets": {
            "model_calls": manifest.model_call_cap,
            "evaluator_transactions": manifest.evaluator_transaction_cap,
            "gpu_exclusive_seconds": manifest.gpu_exclusive_seconds_cap,
            "cpu_evaluator_seconds": manifest.cpu_evaluator_seconds_cap,
        },
        "resource_entitlement_totals": entitlement_totals,
        "cell_entitlements": {
            cell_id: caps.to_dict() for cell_id, caps in sorted(cell_caps.items())
        },
        "rule_ids": list(registry.rule_ids),
        "variant_ids": [variant.variant_id for variant in variants],
        "stream": stream,
        "no_next_phase": True,
        "no_paid_provider_fallback": True,
    }
    encoded = _canonical_bytes(payload)
    _write_once(artifact_root / "staging_plan.json", encoded)
    plan_sha = hashlib.sha256(encoded).hexdigest()
    ExperimentRegistry(artifact_root).append(
        "hb_gen1_staging_prepared",
        {
            "phase_id": manifest.phase_id,
            "staging_plan_sha256": plan_sha,
            "source_hashes": source_hashes,
            "execution_ready": False,
            "blockers": payload["blockers"],
        },
        event_id=f"hb-gen1-staging-prepared:{plan_sha}",
    )
    return payload
