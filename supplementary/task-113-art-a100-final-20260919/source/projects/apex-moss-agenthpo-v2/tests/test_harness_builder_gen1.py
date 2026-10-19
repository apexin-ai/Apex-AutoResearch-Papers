from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.schema import (
    BuilderVariant,
    HarnessDecision,
    PilotManifest,
    RuleRegistry,
)


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "optimization_lab/harness_builder/data"


def test_pilot_manifest_freezes_three_unseen_suites_and_24_instances() -> None:
    manifest = PilotManifest.from_json(DATA / "hb_gen1_candidates.json")

    assert manifest.phase_id == "hb-gen1-formal"
    assert manifest.executor_model == "gpt-5.6-sol"
    assert manifest.reasoning_effort == "high"
    assert manifest.model_transport == "codex-exec-chatgpt-login"
    assert manifest.client_version == "codex-cli-0.144.6"
    assert len(manifest.benchmarks) == 3
    assert {item.suite for item in manifest.benchmarks} == {
        "kernelbenchx",
        "compilergym-cbench",
        "swe-perf",
    }
    assert all(len(item.candidates) == 8 for item in manifest.benchmarks)
    assert all(len(item.selected_heldout) == 8 for item in manifest.benchmarks)
    assert len(manifest.heldout_ids) == 24

    compiler_gym = next(
        item for item in manifest.benchmarks if item.suite == "compilergym-cbench"
    )
    kernelbenchx = next(
        item for item in manifest.benchmarks if item.suite == "kernelbenchx"
    )
    assert "Fusion/fused_relu_max_pool2d_conv2d.py" in kernelbenchx.selected_heldout
    assert "Activation/gelu_bf16.py" not in kernelbenchx.selected_heldout
    assert "stringsearch2" in compiler_gym.selected_heldout
    assert "rijndael" not in compiler_gym.selected_heldout
    assert "blowfish" in compiler_gym.selected_heldout
    assert "sha" not in compiler_gym.selected_heldout

    for benchmark in manifest.benchmarks:
        expected = tuple(item.task_id for item in benchmark.candidates if item.eligible)
        assert benchmark.selected_heldout == expected


def test_kernelbenchx_replacement_audit_is_frozen_before_formal_scores() -> None:
    payload = json.loads(
        (DATA / "kernelbenchx_replacement_v1.json").read_text(encoding="utf-8")
    )
    assert payload["kernelbenchx_commit"] == (
        "fd4192293bf9a8c645327a9d46aa1e807f1f9cf2"
    )
    assert payload["tritonbench_commit"] == (
        "603e28a5050e8c268f6883a69709d477a272d49a"
    )
    assert payload["failed_task_id"] == "Activation/gelu_bf16.py"
    assert payload["selected"]["task_id"] == (
        "Fusion/fused_relu_max_pool2d_conv2d.py"
    )
    assert payload["selected"]["selection_digest"] == (
        "619f5a9da305b50b33ab1736d0d86ea24ec0ff8800b63ae7c323b16a1b17f3ca"
    )
    assert payload["selected"]["source_sha256"] == (
        "99fddc19b0e1987f7e64ef4e8711590696f9f15f469a3b887f1cf7bcda638177"
    )
    assert [item["task_id"] for item in payload["rejected_predecessors"]] == [
        "Fusion/fused_gelu_min.py",
        "Math/add.py",
        "LinearAlgebra/solve_and_add_scaled_vector.py",
        "LinearAlgebra/invert_matrix_lu.py",
        "Math/rad2deg_sqrt.py",
    ]
    scanned = [*payload["rejected_predecessors"], payload["selected"]]
    for item in scanned:
        assert item["selection_digest"] == hashlib.sha256(
            f"{payload['selection_seed']}|kernelbenchx|{item['task_id']}".encode()
        ).hexdigest()
    assert [item["selection_digest"] for item in scanned] == sorted(
        item["selection_digest"] for item in scanned
    )


def test_builder_variants_isolate_cross_instance_experience() -> None:
    manifest = PilotManifest.from_json(DATA / "hb_gen1_candidates.json")
    registry = RuleRegistry.from_json(DATA / "rule_registry_v2.json")
    variants = {
        item.variant_id: item
        for item in BuilderVariant.list_from_json(DATA / "builder_variants_v2.json")
    }

    assert set(variants) == {"A", "B0", "B*", "B-online"}
    assert variants["A"].freeze_after_initial is True
    assert variants["B0"].freeze_after_initial is False
    assert variants["B*"].freeze_after_initial is False
    assert variants["B*"].continual_update is False
    assert variants["B-online"].continual_update is True
    assert variants["B0"].rule_registry_sha256 == variants["B*"].rule_registry_sha256
    assert variants["B*"] .rule_registry_sha256 == variants["B-online"].rule_registry_sha256
    assert variants["B0"].experience_sources == ()
    assert variants["B*"].experience_sources
    assert variants["B-online"].experience_sources == variants["B*"].experience_sources
    assert set(variants["B*"].excluded_task_ids) >= set(manifest.heldout_ids)
    assert set(variants["B-online"].excluded_task_ids) >= set(manifest.heldout_ids)
    assert "compilergym-cbench:stringsearch2" in variants["B*"].excluded_task_ids
    assert "compilergym-cbench:rijndael" not in variants["B*"].excluded_task_ids
    assert "compilergym-cbench:blowfish" in variants["B*"].excluded_task_ids
    assert "compilergym-cbench:sha" not in variants["B*"].excluded_task_ids
    decision_rules = set(registry.executable_rule_ids)
    assert set(variants["B0"].allowed_rule_ids) == decision_rules
    assert set(variants["B*"].allowed_rule_ids) == decision_rules
    assert set(variants["B-online"].allowed_rule_ids) == decision_rules


def test_harness_decision_requires_operational_system_change_after_plateau() -> None:
    payload = {
        "schema_version": 1,
        "rule_id": "discipline",
        "role_graph": ["analyst", "generator"],
        "memory_views": ["current", "best"],
        "tools": ["score"],
        "parent_strategy": "incumbent",
        "workflow": ["diagnose", "generate"],
        "scheduler_mode": "single_candidate",
        "recovery_mode": "repair_then_reset",
        "kernel_directive": "Change only the measured bottleneck.",
    }
    decision = HarnessDecision.from_dict(payload)
    assert decision.operational_fingerprint

    prompt_only = dict(payload)
    prompt_only["kernel_directive"] = "Use different wording but keep the same plan."
    rewritten = HarnessDecision.from_dict(prompt_only)
    with pytest.raises(ValueError, match="operational"):
        rewritten.require_operational_change_from(decision)

    changed = dict(payload)
    changed["rule_id"] = "law_inversion"
    changed["parent_strategy"] = "restart"
    changed_decision = HarnessDecision.from_dict(changed)
    changed_decision.require_operational_change_from(decision)


def test_data_files_are_strict_json_without_heldout_experience_leakage() -> None:
    manifest = PilotManifest.from_json(DATA / "hb_gen1_candidates.json")
    payload = json.loads((DATA / "experience_bank_v1.json").read_text(encoding="utf-8"))
    serialized = json.dumps(payload, sort_keys=True)
    for task_id in manifest.heldout_ids:
        assert task_id not in serialized


def test_meta_train_sources_bind_the_pinned_kernelbench_snapshot() -> None:
    payload = json.loads((DATA / "experience_bank_v1.json").read_text(encoding="utf-8"))
    assert payload["repository_commit"] == "423217d9fda91e0c2d67e4a43bf62f96f6d104f1"
    bindings = payload["source_bindings"]
    assert [item["task_id"] for item in bindings] == payload["source_instances"]
    assert len(bindings) == 8
    assert all(item["source_path"] == f"KernelBench/{item['task_id']}" for item in bindings)
    assert all(len(item["source_sha256"]) == 64 for item in bindings)
    assert bindings[2]["source_sha256"] == (
        "8f3ae78284ddd70b5c2fff66e066e967780245dee262fbf8cd2432498833796a"
    )
