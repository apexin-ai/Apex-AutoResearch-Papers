from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest

from optimization_lab.harness_builder.agenthpo_qualification import (
    DEFAULT_AGENTHPO_QUALIFICATION_MANIFEST,
    AgentHPOQualificationError,
    adapt_agenthpo_result,
    canonical_agenthpo_qualification_bytes,
    verify_agenthpo_qualification,
    verify_agenthpo_source_checkout,
    verify_future_canary_results,
    verify_result_artifact,
)


def _payload() -> dict[str, object]:
    return json.loads(
        DEFAULT_AGENTHPO_QUALIFICATION_MANIFEST.read_text(encoding="utf-8")
    )


def _write(tmp_path: Path, payload: object, *, canonical: bool = True) -> Path:
    path = tmp_path / "agenthpo-contract.json"
    if canonical:
        path.write_bytes(canonical_agenthpo_qualification_bytes(payload))
    else:
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def _valid_result(task_id: str, final_metric: float) -> dict[str, object]:
    return {
        "decisions": [{"index": index} for index in range(1, 6)],
        "fallback_decision_count": 0,
        "history": [
            {"kind": "baseline", "metric_value": 0.0},
            *[
                {
                    "kind": f"intervention_{index}",
                    "metric_value": final_metric,
                }
                for index in range(1, 6)
            ],
        ],
        "model": "frozen-test-model",
        "raw_responses": [f"response {index}" for index in range(1, 6)],
        "replicate_seed": 42,
        "task_id": task_id,
    }


def test_checked_in_contract_is_q7_source_locked_and_zero_authority() -> None:
    payload = verify_agenthpo_qualification()
    assert payload["execution_authority"] == "NOT_GRANTED"
    assert payload["execution_entitlement"] == {
        "cpu_evaluator_seconds": 0,
        "evaluator_transactions": 0,
        "gpu_exclusive_seconds": 0,
        "max_parallel": 0,
        "model_calls": 0,
    }
    assert payload["source_lock"]["git_commit"] == (
        "6d8d90071cdb16b06f0db866480ecaae48880fba"
    )
    assert payload["source_lock"]["root_tree"] == (
        "1acedca0a63252deea57a51878b4ddfd002aa507"
    )
    assert payload["source_lock"]["git_index_sha256"] == (
        "89164675d5ad2aa1decda95881091bd71d598d5adda688f265e255eed8b24f7c"
    )
    tasks = payload["qualification_tasks"]
    assert [task["task_id"] for task in tasks] == [
        "modernbert_mnli_accuracy",
        "cifar10_airbench94",
        "sparsetsf_ettm1_96_mse",
        "noisygl_cora_uniform30_gcn",
        "art_2048_win_rate",
        "simple_rl_reason_qwen25_05b_math500",
        "vbll_yacht_rmse",
    ]
    assert {task["category"] for task in tasks} == {
        "NLP",
        "CV",
        "TS",
        "Graph",
        "RL",
        "LLM",
        "SL",
    }
    assert sum(len(task["files"]) for task in tasks) == 20


def test_exact_q7_files_revisions_and_scoring_anchors_are_frozen() -> None:
    payload = verify_agenthpo_qualification()
    tasks = {task["task_id"]: task for task in payload["qualification_tasks"]}
    assert tasks["modernbert_mnli_accuracy"] == {
        "anchor": 90.4,
        "baseline": 38.960774325,
        "category": "NLP",
        "direction": "higher",
        "files": {
            "tasks/main/modernbert_mnli_accuracy/baseline.json": "4b3b1254a0897b96ce804b076843ebe799c0b406b44047be154f71ae0fe0feea",
            "tasks/main/modernbert_mnli_accuracy/eval_modernbert_mnli.py": "8c43f867d1b8b64f7d890a8f8de6570286f9d4a8e02ce4d99897f4671b23bfba",
            "tasks/main/modernbert_mnli_accuracy/run_formal_modernbert_mnli_agent.py": "57ee526cd4d62a236b80149ef2bbe288c5c00317260bfe1cf55d15cfe9a4b404",
        },
        "task_id": "modernbert_mnli_accuracy",
        "upstream_revision": "c6d942312f1b0b24d423628b8e477a3e97c7038f",
    }
    assert tasks["simple_rl_reason_qwen25_05b_math500"]["files"] == {
        "tasks/main/simple_rl_reason_qwen25_05b_math500/baseline.json": "6ed136e35620fdbbda04317821970050b2b5f4b347aa3fc19095b750ecee785d",
        "tasks/main/simple_rl_reason_qwen25_05b_math500/run_formal_simple_rl_reason_qwen25_05b_math500_agent.py": "1555218bae01c7e66d42bf92d88a3353da951218e9edc0e17dbffe8198a8a855",
    }
    assert tasks["simple_rl_reason_qwen25_05b_math500"]["patch_sha256"] == (
        "4dab81c185aa9a2e0f46012f956ac55b3243840e53ce51a1c33db8806eaf2767"
    )
    assert tasks["vbll_yacht_rmse"]["direction"] == "lower"
    assert tasks["sparsetsf_ettm1_96_mse"]["direction"] == "lower"
    assert tasks["art_2048_win_rate"]["baseline"] == 0.0


def test_explicit_blockers_explain_why_formal_execution_is_impossible() -> None:
    payload = verify_agenthpo_qualification()
    assert payload["capability"] == {
        "blockers": [
            "agenthpobench_free_form_prompt_codec_or_fresh_split_required",
            "agenthpobench_formal_intervention_dispatch_integration_missing",
            "agenthpobench_trusted_transport_ledger_missing",
            "agenthpobench_upstream_repositories_absent",
            "agenthpobench_datasets_checkpoints_and_models_absent",
            "agenthpobench_target_gpu_environment_unverified",
            "agenthpobench_reference_negative_isolation_canary_pending",
        ],
        "execution_ready": False,
        "status": "BLOCKED_CAPABILITY",
    }
    assert payload["canary_plan"] == {
        "q7_baseline_replay": {
            "planned_evaluator_transactions": 14,
            "repeat_count": 2,
            "task_count": 7,
        },
        "future_gate_only": True,
        "negative_candidates": {
            "kinds": [
                "unknown_key",
                "out_of_range_value",
                "no_operational_change",
            ],
            "required_disposition": "strict_codec_reject_before_evaluator",
        },
        "total_planned_evaluator_transactions": 14,
    }


def test_manifest_drift_noncanonical_duplicate_and_execute_fail_closed(
    tmp_path: Path,
) -> None:
    payload = _payload()
    payload["unexpected"] = True
    with pytest.raises(AgentHPOQualificationError, match="fields or source"):
        verify_agenthpo_qualification(_write(tmp_path, payload))

    payload = _payload()
    payload["source_lock"]["root_tree"] = "0" * 40
    with pytest.raises(AgentHPOQualificationError, match="fields or source"):
        verify_agenthpo_qualification(_write(tmp_path, payload))

    with pytest.raises(AgentHPOQualificationError, match="not canonically"):
        verify_agenthpo_qualification(_write(tmp_path, _payload(), canonical=False))

    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"schema_version":1,"schema_version":1}\n')
    with pytest.raises(AgentHPOQualificationError, match="repeats"):
        verify_agenthpo_qualification(duplicate)

    with pytest.raises(AgentHPOQualificationError, match="no execution authority"):
        verify_agenthpo_qualification(request_execution=True)


def test_separately_observed_source_lock_drift_is_rejected() -> None:
    payload = verify_agenthpo_qualification()
    observed = copy.deepcopy(payload["source_lock"])
    verify_agenthpo_qualification(observed_source_lock=observed)
    observed["control_file_sha256"]["configs/tasks.json"] = "0" * 64
    with pytest.raises(AgentHPOQualificationError, match="source lock drifted"):
        verify_agenthpo_qualification(observed_source_lock=observed)


def test_source_checkout_hash_and_symlink_drift_fail_closed(tmp_path: Path) -> None:
    payload = verify_agenthpo_qualification()
    root = tmp_path.resolve() / "source"
    root.mkdir()
    required = dict(payload["source_lock"]["control_file_sha256"])
    for task in payload["qualification_tasks"]:
        required.update(task["files"])
    for relative, digest in required.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(bytes.fromhex(digest))

    # Synthetic bytes do not match their names' frozen hashes: fail on first file.
    with pytest.raises(AgentHPOQualificationError, match="hash drifted"):
        verify_agenthpo_source_checkout(
            root,
            observed_git_commit=payload["source_lock"]["git_commit"],
            observed_root_tree=payload["source_lock"]["root_tree"],
        )

    with pytest.raises(AgentHPOQualificationError, match="commit drifted"):
        verify_agenthpo_source_checkout(
            root,
            observed_git_commit="0" * 40,
            observed_root_tree=payload["source_lock"]["root_tree"],
        )

    link = tmp_path.resolve() / "source-link"
    link.symlink_to(root, target_is_directory=True)
    with pytest.raises(AgentHPOQualificationError, match="symlinks"):
        verify_agenthpo_source_checkout(
            link,
            observed_git_commit=payload["source_lock"]["git_commit"],
            observed_root_tree=payload["source_lock"]["root_tree"],
        )


def test_result_artifact_path_symlink_and_hash_binding(tmp_path: Path) -> None:
    allowed = tmp_path.resolve() / "results"
    allowed.mkdir()
    result = allowed / "result.json"
    result.write_text('{"ok":true}\n')
    digest = hashlib.sha256(result.read_bytes()).hexdigest()
    assert verify_result_artifact(
        result,
        expected_sha256=digest,
        allowed_root=allowed,
    ) == {
        "result_realpath": str(result),
        "result_sha256": digest,
        "size_bytes": result.stat().st_size,
    }

    with pytest.raises(AgentHPOQualificationError, match="content hash drifted"):
        verify_result_artifact(
            result,
            expected_sha256="0" * 64,
            allowed_root=allowed,
        )
    outside = tmp_path.resolve() / "outside.json"
    outside.write_text("{}\n")
    outside_digest = hashlib.sha256(outside.read_bytes()).hexdigest()
    with pytest.raises(AgentHPOQualificationError, match="outside"):
        verify_result_artifact(
            outside,
            expected_sha256=outside_digest,
            allowed_root=allowed,
        )
    link = allowed / "linked.json"
    link.symlink_to(result)
    with pytest.raises(AgentHPOQualificationError, match="symlinks"):
        verify_result_artifact(
            link,
            expected_sha256=digest,
            allowed_root=allowed,
        )


def test_adapter_clips_normalized_score_and_keeps_raw_result_private() -> None:
    payload = _valid_result("modernbert_mnli_accuracy", 90.4)
    payload["history"][0]["private_log"] = "do not expose"
    result = adapt_agenthpo_result(
        "modernbert_mnli_accuracy", json.dumps(payload)
    )
    assert result.public_projection == {
        "bounded_normalized_score": 1.0,
        "validity": "valid",
        "coarse_reason_codes": [],
    }
    assert set(result.public_projection) == {
        "bounded_normalized_score",
        "validity",
        "coarse_reason_codes",
    }
    assert "private_log" not in result.public_projection
    assert result.private_evidence["result_json"]["history"][0][
        "private_log"
    ] == "do not expose"

    low = adapt_agenthpo_result(
        "vbll_yacht_rmse",
        json.dumps(_valid_result("vbll_yacht_rmse", 2.5)),
    )
    assert low.public_projection["bounded_normalized_score"] == -1.0


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        (lambda value: value.update({"history": value["history"][:-1]}), "trace_contract_invalid"),
        (lambda value: value.update({"decisions": value["decisions"][:-1]}), "decision_contract_invalid"),
        (lambda value: value.update({"raw_responses": [""] * 5}), "raw_response_contract_invalid"),
        (lambda value: value.update({"fallback_decision_count": 1}), "fallback_decision_present"),
        (lambda value: value.pop("replicate_seed"), "seed_provenance_missing"),
        (lambda value: value.pop("model"), "model_provenance_missing"),
        (lambda value: value.update({"task_error": "boom"}), "task_execution_error"),
    ],
)
def test_adapter_returns_only_coarse_invalidity_reasons(mutation, reason: str) -> None:
    payload = _valid_result("art_2048_win_rate", 0.3)
    mutation(payload)
    result = adapt_agenthpo_result("art_2048_win_rate", json.dumps(payload))
    assert result.public_projection["validity"] == "invalid"
    assert reason in result.public_projection["coarse_reason_codes"]
    assert set(result.public_projection) == {
        "bounded_normalized_score",
        "validity",
        "coarse_reason_codes",
    }


def test_adapter_rejects_unknown_duplicate_nonfinite_or_trailing_result() -> None:
    with pytest.raises(AgentHPOQualificationError, match="outside the frozen Q7"):
        adapt_agenthpo_result("future_task", "{}")
    with pytest.raises(AgentHPOQualificationError, match="repeats"):
        adapt_agenthpo_result("art_2048_win_rate", '{"history":[],"history":[]}')
    with pytest.raises(AgentHPOQualificationError, match="contains NaN"):
        adapt_agenthpo_result("art_2048_win_rate", '{"metric":NaN}')
    with pytest.raises(AgentHPOQualificationError, match="contains data after"):
        adapt_agenthpo_result("art_2048_win_rate", "{} trailing")


def test_future_canary_gate_validates_plan_but_never_executes() -> None:
    payload = verify_agenthpo_qualification()
    tasks = payload["qualification_tasks"]
    baseline = {task["task_id"]: [task["baseline"]] * 2 for task in tasks}
    negative = {
        kind: ["strict_codec_reject_before_evaluator"] * 7
        for kind in ("unknown_key", "out_of_range_value", "no_operational_change")
    }
    assert verify_future_canary_results(
        baseline_replay=baseline,
        negative_dispositions=negative,
    ) == {
        "baseline_evaluator_transactions": 14,
        "negative_evaluator_transactions": 0,
        "passed": True,
        "total_evaluator_transactions": 14,
    }
    baseline["art_2048_win_rate"] = [0.0, 0.5]
    with pytest.raises(AgentHPOQualificationError, match="nondeterministic"):
        verify_future_canary_results(
            baseline_replay=baseline,
            negative_dispositions=negative,
        )
