from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pytest

from optimization_lab.harness_builder.swebench_qualification_transfer import (
    V1R8_CODE_REVISION,
    V1R8_QUALIFICATION_SUMMARY_SHA256,
    V1R8_QUALIFICATION_TASK_BINDING_SHA256,
    V1R8_RULE_REGISTRY_SHA256,
    V1R8_STAGING_PLAN_SHA256,
    _exercise_image_acquisition,
    _worker_semantic_projection,
    verify_swebench_qualification_transfer,
)
from optimization_lab.harness_builder.three_arm_providers import (
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORKER = "optimization_lab/harness_builder/adapters/swebench_verified_worker.py"
SEMANTIC_FILES = (
    "optimization_lab/harness_builder/contract_compatibility.py",
    "optimization_lab/harness_builder/evaluation.py",
    "optimization_lab/harness_builder/solutions.py",
    "optimization_lab/harness_builder/adapters/sweperf.py",
    "optimization_lab/harness_builder/adapters/swebench_verified.py",
)


def _canonical(payload: object) -> bytes:
    return (
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode()


def _inputs(tmp_path: Path) -> tuple[Path, Path, Path, Path, dict[str, object]]:
    selection = {
        "selected": [
            {"instance_id": instance_id}
            for instance_id in SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
        ]
    }
    selection_path = tmp_path / "selection.json"
    selection_path.write_bytes(_canonical(selection))
    selection_sha = hashlib.sha256(selection_path.read_bytes()).hexdigest()
    tasks = [
        {"instance_id": instance_id, "task_sha256": f"{index + 1:x}" * 64}
        for index, instance_id in enumerate(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS)
    ]
    task_lock = {
        "schema": "swebench_verified_active_task_lock.v2",
        "selection_mode": SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        "selection_sha256": selection_sha,
        "dataset_sha256": "d" * 64,
        "tasks": tasks,
    }
    task_path = tmp_path / "tasks.json"
    task_path.write_bytes(_canonical(task_lock))
    images = [
        {
            "instance_id": instance_id,
            "locked_reference": "example.invalid/" + str(index) + "@sha256:" + f"{index + 7:x}" * 64,
            "mutable_reference": "example.invalid/" + str(index) + ":latest",
            "manifest_sha256": f"{index + 7:x}" * 64,
        }
        for index, instance_id in enumerate(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS)
    ]
    image_path = tmp_path / "images.json"
    image_path.write_bytes(
        _canonical({"schema": "swebench_verified_image_lock.v2", "images": images})
    )
    results = []
    for index, instance_id in enumerate(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS):
        results.append(
            {
                "instance_id": instance_id,
                "task_sha256": tasks[index]["task_sha256"],
                "image_manifest_sha256": images[index]["manifest_sha256"],
                "official_gold_patch_sha256": "a" * 64,
                "gold_patch_normalization": "deterministic_nonsemantic_index_metadata_v1",
                "candidate_sha256": "b" * 64,
                "private_result_sha256": "c" * 64,
                "resolved": True,
                "score": 1.0,
                "trust_grade": "official_standard_candidate_visible_test_process",
            }
        )
    canary = {
        "schema_version": 2,
        "suite": "swebench-verified",
        "dataset_sha256": "d" * 64,
        "selection_sha256": selection_sha,
        "image_lock_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
        "selected_instances": list(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS),
        "candidate_policy": "official_gold_patch_canonicalized_no_model",
        "gold_patch_normalization": "deterministic_nonsemantic_index_metadata_v1",
        "trust_grade": "official_standard_candidate_visible_test_process",
        "results": results,
        "passed": True,
        "selection_mode": SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        "remote_execution_contract": {
            "host_alias": "a100jump",
            "remote_python": "/remote/venv/bin/python",
            "remote_project_root": "/remote/runtime/Moss-commit",
            "remote_swebench_source_root": "/remote/SWE-bench",
        },
    }
    canary_path = tmp_path / "canary.json"
    canary_path.write_bytes(_canonical(canary))
    inputs = {
        "selection_mode": SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        "active_instance_ids": list(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS),
        "dataset_sha256": "d" * 64,
        "selection_sha256": selection_sha,
        "task_lock_sha256": hashlib.sha256(task_path.read_bytes()).hexdigest(),
        "image_lock_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
        "gold_canary_summary_sha256": hashlib.sha256(canary_path.read_bytes()).hexdigest(),
        "gold_canary_passed_instances": 6,
        "gold_canary_passed": True,
        "remote_execution_contract": canary["remote_execution_contract"],
    }
    return selection_path, task_path, image_path, canary_path, inputs


def _git_bytes(project_root: Path, revision: str, relative_path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{relative_path}"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout


def _semantic_components(
    project_root: Path, new_revision: str
) -> dict[str, dict[str, object]]:
    components: dict[str, dict[str, object]] = {}
    for relative_path in SEMANTIC_FILES:
        old = _git_bytes(project_root, V1R8_CODE_REVISION, relative_path)
        new = _git_bytes(project_root, new_revision, relative_path)
        components[relative_path] = {
            "old_sha256": hashlib.sha256(old).hexdigest(),
            "new_sha256": hashlib.sha256(new).hexdigest(),
            "semantic_unchanged": True,
        }
    old_worker = _git_bytes(project_root, V1R8_CODE_REVISION, WORKER)
    new_worker = _git_bytes(project_root, new_revision, WORKER)
    old_projection = hashlib.sha256(_worker_semantic_projection(old_worker)).hexdigest()
    new_projection = hashlib.sha256(_worker_semantic_projection(new_worker)).hexdigest()
    components[WORKER] = {
        "old_sha256": hashlib.sha256(old_worker).hexdigest(),
        "new_sha256": hashlib.sha256(new_worker).hexdigest(),
        "semantic_projection_old_sha256": old_projection,
        "semantic_projection_new_sha256": new_projection,
        "semantic_unchanged": True,
        "allowed_delta": "locked_image_acquisition_fail_closed_only",
    }
    return components


def _clean_successor_checkout(tmp_path: Path) -> tuple[Path, str]:
    checkout = tmp_path / "clean-project"
    subprocess.run(
        ["git", "clone", "--quiet", "--no-checkout", str(PROJECT_ROOT), str(checkout)],
        check=True,
    )
    subprocess.run(
        ["git", "checkout", "--quiet", "--detach", V1R8_CODE_REVISION],
        cwd=checkout,
        check=True,
    )
    (checkout / WORKER).write_bytes((PROJECT_ROOT / WORKER).read_bytes())
    subprocess.run(["git", "add", WORKER], cwd=checkout, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=qualification-test",
            "-c",
            "user.email=qualification-test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "test locked image acquisition successor",
        ],
        cwd=checkout,
        check=True,
    )
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=checkout,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    return checkout, revision


def _receipt(
    tmp_path: Path,
    *,
    project_root: Path | None = None,
    new_revision: str = V1R8_CODE_REVISION,
    simplified: bool = False,
) -> tuple[Path, tuple[Path, Path, Path, Path]]:
    selection, tasks, images, canary, inputs = _inputs(tmp_path)
    if simplified:
        historical: dict[str, object] = {
            "summary_sha256": V1R8_QUALIFICATION_SUMMARY_SHA256,
            "source_staging_plan_sha256": V1R8_STAGING_PLAN_SHA256,
            "source_code_revision": V1R8_CODE_REVISION,
            "rule_registry_sha256": V1R8_RULE_REGISTRY_SHA256,
            "task_binding_sha256": V1R8_QUALIFICATION_TASK_BINDING_SHA256,
            "valid_rounds": 5,
            "minimum_valid_rounds": 4,
            "validity_status": "sufficient_validity",
            "sealed": True,
        }
        semantic: dict[str, object] = {
            "old_code_revision": V1R8_CODE_REVISION,
            "new_code_revision": new_revision,
            "passed": True,
            "image_acquisition_delta_tests": {"passed": True},
        }
    else:
        assert project_root is not None
        historical = {
            "summary_sha256": V1R8_QUALIFICATION_SUMMARY_SHA256,
            "source_staging_plan_sha256": V1R8_STAGING_PLAN_SHA256,
            "source_code_revision": V1R8_CODE_REVISION,
            "rule_registry_sha256": V1R8_RULE_REGISTRY_SHA256,
            "task_id": "sphinx-doc__sphinx-8459",
            "task_binding_sha256": V1R8_QUALIFICATION_TASK_BINDING_SHA256,
            "attempted_rounds": 8,
            "valid_rounds": 5,
            "minimum_valid_rounds": 4,
            "validity_status": "sufficient_validity",
            "round_sha256s": {
                f"v{index:03d}": f"{index:x}" * 64 for index in range(1, 9)
            },
            "cell_ledger_sha256": "9" * 64,
            "cell_state_sha256": "a" * 64,
            "sealed": True,
        }
        semantic = {
            "old_code_revision": V1R8_CODE_REVISION,
            "new_code_revision": new_revision,
            "policy": (
                "candidate_normalization_codec_evaluator_scoring_unchanged;"
                "locked_image_acquisition_fail_closed_delta_only"
            ),
            "components": _semantic_components(project_root, new_revision),
            "image_acquisition_delta_tests": _exercise_image_acquisition(),
            "passed": True,
        }
    payload = {
        "schema_version": 1,
        "kind": "swebench_contract_qualification_transfer_v1r8_to_v1r9",
        "historical_qualification": historical,
        "semantic_transfer": semantic,
        "v1r9_inputs": inputs,
        "transfer_usage": {
            "model_calls_started": 0,
            "evaluator_transactions_started": 0,
        },
        "formal_score_reuse": False,
        "passed": True,
        "may_start_formal_stream": True,
    }
    raw = _canonical(payload)
    receipt = tmp_path / f"{hashlib.sha256(raw).hexdigest()}.json"
    receipt.write_bytes(raw)
    return receipt, (selection, tasks, images, canary)


def test_worker_semantic_projection_allows_only_locked_image_acquisition_delta() -> None:
    old = subprocess.run(
        ["git", "show", f"{V1R8_CODE_REVISION}:{WORKER}"],
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout
    current = (PROJECT_ROOT / WORKER).read_bytes()

    assert _worker_semantic_projection(old) == _worker_semantic_projection(current)
    changed = current.replace(b"passed + 1.0", b"passed + 2.0")
    assert _worker_semantic_projection(old) != _worker_semantic_projection(changed)


def test_locked_image_acquisition_delta_tests_fail_closed() -> None:
    result = _exercise_image_acquisition()

    assert result["passed"] is True
    assert result["passed_cases"] == 3


def test_transfer_receipt_is_cas_zero_call_and_rechecks_new_inputs(tmp_path: Path) -> None:
    project_root, revision = _clean_successor_checkout(tmp_path)
    receipt, paths = _receipt(
        tmp_path,
        project_root=project_root,
        new_revision=revision,
    )

    payload = verify_swebench_qualification_transfer(
        receipt,
        project_root=project_root,
        expected_new_code_revision=revision,
        selection_path=paths[0],
        task_lock_path=paths[1],
        image_lock_path=paths[2],
        gold_canary_summary_path=paths[3],
    )

    assert payload["transfer_usage"] == {
        "model_calls_started": 0,
        "evaluator_transactions_started": 0,
    }
    assert payload["formal_score_reuse"] is False
    paths[3].write_text("{}\n", encoding="utf-8")
    with pytest.raises(ValueError, match="canary"):
        verify_swebench_qualification_transfer(
            receipt,
            project_root=project_root,
            expected_new_code_revision=revision,
            selection_path=paths[0],
            task_lock_path=paths[1],
            image_lock_path=paths[2],
            gold_canary_summary_path=paths[3],
        )


def test_transfer_rejects_forged_simplified_nested_receipt(tmp_path: Path) -> None:
    receipt, paths = _receipt(
        tmp_path,
        new_revision="e" * 40,
        simplified=True,
    )

    with pytest.raises(ValueError, match="schema"):
        verify_swebench_qualification_transfer(
            receipt,
            project_root=PROJECT_ROOT,
            expected_new_code_revision="e" * 40,
            selection_path=paths[0],
            task_lock_path=paths[1],
            image_lock_path=paths[2],
            gold_canary_summary_path=paths[3],
        )


def test_transfer_recomputes_components_and_binds_clean_successor_root(
    tmp_path: Path,
) -> None:
    project_root, revision = _clean_successor_checkout(tmp_path)
    receipt, paths = _receipt(
        tmp_path,
        project_root=project_root,
        new_revision=revision,
    )
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    payload["semantic_transfer"]["components"][SEMANTIC_FILES[1]][
        "new_sha256"
    ] = "f" * 64
    forged_raw = _canonical(payload)
    forged = tmp_path / f"{hashlib.sha256(forged_raw).hexdigest()}.json"
    forged.write_bytes(forged_raw)

    with pytest.raises(ValueError, match="semantic components drifted"):
        verify_swebench_qualification_transfer(
            forged,
            project_root=project_root,
            expected_new_code_revision=revision,
            selection_path=paths[0],
            task_lock_path=paths[1],
            image_lock_path=paths[2],
            gold_canary_summary_path=paths[3],
        )

    tracked = project_root / SEMANTIC_FILES[1]
    tracked.write_bytes(tracked.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="not clean"):
        verify_swebench_qualification_transfer(
            receipt,
            project_root=project_root,
            expected_new_code_revision=revision,
            selection_path=paths[0],
            task_lock_path=paths[1],
            image_lock_path=paths[2],
            gold_canary_summary_path=paths[3],
        )
