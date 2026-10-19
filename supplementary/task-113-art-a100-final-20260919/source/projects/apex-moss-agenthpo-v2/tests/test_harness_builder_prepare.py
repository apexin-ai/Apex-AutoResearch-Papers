from __future__ import annotations

import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.prepare import (
    build_hb_gen1_cell_caps,
    prepare_hb_gen1,
)
from optimization_lab.harness_builder.schema import PilotManifest


ROOT = Path(__file__).resolve().parents[1]


def test_prepare_writes_content_addressed_blocked_staging_plan(tmp_path: Path) -> None:
    artifact_root = tmp_path / "hb-gen1"
    result = prepare_hb_gen1(
        project_root=ROOT,
        artifact_root=artifact_root,
        code_revision="a" * 40,
        observed_client_version="codex-cli-0.144.6",
    )

    assert result["phase_id"] == "hb-gen1-formal"
    assert result["code_revision"] == "a" * 40
    assert result["model_signature"] == {
        "executor_model": "gpt-5.6-sol",
        "reasoning_effort": "high",
        "transport": "codex-exec-chatgpt-login",
        "client_version": "codex-cli-0.144.6",
    }
    assert result["execution_ready"] is False
    assert set(result["blockers"]) == {
        "model_runtime_canary_pending",
        "meta_train_pending",
        "evaluator_canaries_pending",
    }
    assert len(result["stream"]) == 24
    assert set(result["source_hashes"]) == {
        "experiment_plan",
        "manifest",
        "rule_registry",
        "builder_variants",
        "experience_bank",
        "kernelbenchx_replacement",
    }
    assert result["resource_entitlement_totals"] == {
        "model_calls": 1666,
        "evaluator_transactions": 1138,
        "gpu_exclusive_seconds": 246600.0,
        "cpu_evaluator_seconds": 1416000.0,
    }
    assert len(result["cell_entitlements"]) == 131
    assert (artifact_root / "staging_plan.json").is_file()
    assert (artifact_root / "ledger.jsonl").is_file()

    repeated = prepare_hb_gen1(
        project_root=ROOT,
        artifact_root=artifact_root,
        code_revision="a" * 40,
        observed_client_version="codex-cli-0.144.6",
    )
    assert repeated == result
    assert len((artifact_root / "ledger.jsonl").read_text(encoding="utf-8").splitlines()) == 1


def test_prepare_refuses_to_overwrite_a_different_staging_plan(tmp_path: Path) -> None:
    artifact_root = tmp_path / "hb-gen1"
    prepare_hb_gen1(
        project_root=ROOT,
        artifact_root=artifact_root,
        code_revision="a" * 40,
        observed_client_version="codex-cli-0.144.6",
    )
    path = artifact_root / "staging_plan.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["execution_ready"] = True
    path.write_text(json.dumps(payload), encoding="utf-8")

    with pytest.raises(ValueError, match="overwrite"):
        prepare_hb_gen1(
            project_root=ROOT,
            artifact_root=artifact_root,
            code_revision="a" * 40,
            observed_client_version="codex-cli-0.144.6",
        )


def test_prepare_rejects_a_different_model_client(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Codex CLI"):
        prepare_hb_gen1(
            project_root=ROOT,
            artifact_root=tmp_path / "hb-gen1",
            code_revision="a" * 40,
            observed_client_version="codex-cli-0.145.0",
        )


def test_cell_entitlements_are_nontransferable_and_close_under_global_caps() -> None:
    manifest = PilotManifest.from_json(
        ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"
    )
    experience_bank = json.loads(
        (ROOT / "optimization_lab/harness_builder/data/experience_bank_v1.json").read_text(
            encoding="utf-8"
        )
    )
    caps = build_hb_gen1_cell_caps(manifest, experience_bank)

    formal = {key: value for key, value in caps.items() if key.startswith("formal:")}
    assert len(formal) == 24 * 4
    assert all(value.model_calls == 16 for value in formal.values())
    assert all(value.evaluator_transactions == 11 for value in formal.values())

    totals = {
        field: sum(getattr(value, field) for value in caps.values())
        for field in (
            "model_calls",
            "evaluator_transactions",
            "gpu_exclusive_seconds",
            "cpu_evaluator_seconds",
        )
    }
    assert totals == {
        "model_calls": 1666,
        "evaluator_transactions": 1138,
        "gpu_exclusive_seconds": 246600.0,
        "cpu_evaluator_seconds": 1416000.0,
    }
    assert totals["model_calls"] <= manifest.model_call_cap
    assert totals["evaluator_transactions"] <= manifest.evaluator_transaction_cap
    assert totals["gpu_exclusive_seconds"] <= manifest.gpu_exclusive_seconds_cap
    assert totals["cpu_evaluator_seconds"] <= manifest.cpu_evaluator_seconds_cap

    assert caps["canary:kernelbenchx"].evaluator_transactions == 11
    assert caps["canary:model-route"].model_calls == 2
    assert caps["canary:compilergym-cbench"].evaluator_transactions == 12
    assert caps["canary:swe-perf"].evaluator_transactions == 11
