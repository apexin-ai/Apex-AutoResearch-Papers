"""Zero-call, fail-closed transfer of the v1r8 SWE contract qualification.

The historical qualification is evidence about the candidate/codec/scoring
path, not a score that may be copied into v1r9.  A transfer is therefore
allowed only when the exact old evidence is present, the semantic code
projection is unchanged, the only worker delta is the locked-image acquisition
boundary, and the six newly selected gold canaries all pass.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence

from .three_arm_providers import (
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
    SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    _validate_swebench_image_lock,
)


V1R8_QUALIFICATION_SUMMARY_SHA256 = (
    "cc7e8c71afdd161f62c628e715a2127d890547b443bd1c1f861f6c234d71cd8d"
)
V1R8_STAGING_PLAN_SHA256 = (
    "0d98c1d733711f1f56649bb6d0547d902e1603ebf57af5fddaff34c41fd4092e"
)
V1R8_CODE_REVISION = "a9c049a2dcb7e8194181ba7f7d726451ab2959cd"
V1R8_RULE_REGISTRY_SHA256 = (
    "dc3cd72887cdb5d28a7b273d64047f6f3eda45dc0a51dee4157a8a3d91e091b3"
)
V1R8_QUALIFICATION_TASK_ID = "sphinx-doc__sphinx-8459"
V1R8_QUALIFICATION_TASK_BINDING_SHA256 = (
    "e07d729b2f1c42db70656127e9cd23b3a0c880d856fccb6b825dd8c1b8d6d72c"
)
_COMMIT = re.compile(r"[0-9a-f]{40}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SEMANTIC_FILES = (
    "optimization_lab/harness_builder/contract_compatibility.py",
    "optimization_lab/harness_builder/evaluation.py",
    "optimization_lab/harness_builder/solutions.py",
    "optimization_lab/harness_builder/adapters/sweperf.py",
    "optimization_lab/harness_builder/adapters/swebench_verified.py",
)
_WORKER_PATH = (
    "optimization_lab/harness_builder/adapters/swebench_verified_worker.py"
)
_SUMMARY_FIELDS = {
    "schema_version",
    "purpose",
    "staging_plan_sha256",
    "code_revision",
    "rule_registry_sha256",
    "task_id",
    "task_binding_sha256",
    "cell_id",
    "attempted_rounds",
    "valid_rounds",
    "invalid_rounds",
    "minimum_valid_rounds",
    "validity_status",
    "valid_only_mean",
    "best_score",
    "round_outcomes",
    "formal_score_reuse_forbidden",
    "may_start_formal_stream",
    "sealed",
}
_RECEIPT_FIELDS = {
    "schema_version",
    "kind",
    "historical_qualification",
    "semantic_transfer",
    "v1r9_inputs",
    "transfer_usage",
    "formal_score_reuse",
    "passed",
    "may_start_formal_stream",
}
_HISTORICAL_FIELDS = {
    "summary_sha256",
    "source_staging_plan_sha256",
    "source_code_revision",
    "rule_registry_sha256",
    "task_id",
    "task_binding_sha256",
    "attempted_rounds",
    "valid_rounds",
    "minimum_valid_rounds",
    "validity_status",
    "round_sha256s",
    "cell_ledger_sha256",
    "cell_state_sha256",
    "sealed",
}
_SEMANTIC_TRANSFER_FIELDS = {
    "old_code_revision",
    "new_code_revision",
    "policy",
    "components",
    "image_acquisition_delta_tests",
    "passed",
}
_SEMANTIC_COMPONENT_FIELDS = {
    "old_sha256",
    "new_sha256",
    "semantic_unchanged",
}
_WORKER_COMPONENT_FIELDS = {
    "old_sha256",
    "new_sha256",
    "semantic_projection_old_sha256",
    "semantic_projection_new_sha256",
    "semantic_unchanged",
    "allowed_delta",
}
_IMAGE_ACQUISITION_TEST_FIELDS = {
    "test_policy",
    "cases",
    "passed_cases",
    "passed",
}
_V1R9_INPUT_FIELDS = {
    "selection_mode",
    "active_instance_ids",
    "dataset_sha256",
    "selection_sha256",
    "task_lock_sha256",
    "image_lock_sha256",
    "gold_canary_summary_sha256",
    "gold_canary_passed_instances",
    "gold_canary_passed",
    "remote_execution_contract",
}
_REMOTE_EXECUTION_FIELDS = {
    "host_alias",
    "remote_python",
    "remote_project_root",
    "remote_swebench_source_root",
}
_TRANSFER_USAGE_FIELDS = {
    "model_calls_started",
    "evaluator_transactions_started",
}
_SEMANTIC_POLICY = (
    "candidate_normalization_codec_evaluator_scoring_unchanged;"
    "locked_image_acquisition_fail_closed_delta_only"
)
_IMAGE_ACQUISITION_TEST_CASES = [
    "exact_locked_digest_available",
    "locked_digest_missing_rejected_without_fallback",
    "repo_digest_mismatch_rejected",
]


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


def _sha_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sha(path: Path) -> str:
    return _sha_bytes(path.read_bytes())


def _strict_json(path: Path, *, fields: set[str], label: str) -> tuple[dict[str, Any], bytes]:
    path = path.resolve(strict=True)
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"{label} is not a regular file")
    raw = path.read_bytes()
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is invalid JSON") from exc
    if not isinstance(payload, dict) or set(payload) != fields:
        raise ValueError(f"{label} schema differs")
    if _canonical_bytes(payload) != raw:
        raise ValueError(f"{label} is not canonical")
    return payload, raw


def _exact_object(
    value: object, *, fields: set[str], label: str
) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"{label} schema differs")
    return value


def _verify_clean_successor_project_root(
    project_root: Path, *, expected_revision: str
) -> Path:
    root = project_root.resolve(strict=True)
    if not isinstance(expected_revision, str) or not _COMMIT.fullmatch(expected_revision):
        raise ValueError("qualification transfer successor revision differs")
    commands = {
        "top_level": ["git", "rev-parse", "--show-toplevel"],
        "revision": ["git", "rev-parse", "HEAD"],
        "status": ["git", "status", "--porcelain", "--untracked-files=no"],
    }
    results = {
        name: subprocess.run(
            command,
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        for name, command in commands.items()
    }
    if any(result.returncode != 0 for result in results.values()):
        raise ValueError("qualification transfer successor project root is not Git-bound")
    try:
        observed_top_level = Path(results["top_level"].stdout.strip()).resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise ValueError(
            "qualification transfer successor project root is invalid"
        ) from exc
    if observed_top_level != root:
        raise ValueError("qualification transfer successor project root is not the Git root")
    if results["revision"].stdout.strip() != expected_revision:
        raise ValueError("qualification transfer successor project revision differs")
    if results["status"].stdout.strip():
        raise ValueError("qualification transfer successor project root is not clean")
    ancestry = subprocess.run(
        [
            "git",
            "merge-base",
            "--is-ancestor",
            V1R8_CODE_REVISION,
            expected_revision,
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if expected_revision == V1R8_CODE_REVISION or ancestry.returncode != 0:
        raise ValueError("qualification transfer revision is not a v1r8 successor")
    return root


def _git_bytes(project_root: Path, revision: str, relative_path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{revision}:{relative_path}"],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(f"qualification transfer source is absent: {relative_path}")
    return result.stdout


def _worker_semantic_projection(raw: bytes) -> bytes:
    """Strip only the reviewed locked-image acquisition implementation delta."""

    try:
        tree = ast.parse(raw.decode("utf-8"))
    except (UnicodeDecodeError, SyntaxError) as exc:
        raise ValueError("SWE worker source is invalid") from exc
    tree.body = [
        node
        for node in tree.body
        if not (isinstance(node, ast.FunctionDef) and node.name == "_load_locked_local_image")
    ]
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "__all__"
            for target in node.targets
        ) and isinstance(node.value, (ast.List, ast.Tuple)):
            node.value.elts = [
                item
                for item in node.value.elts
                if not (
                    isinstance(item, ast.Constant)
                    and item.value == "_load_locked_local_image"
                )
            ]
        if not isinstance(node, ast.FunctionDef) or node.name != "run_worker":
            continue
        outer_try = next((item for item in node.body if isinstance(item, ast.Try)), None)
        if outer_try is None:
            raise ValueError("SWE worker acquisition boundary is absent")
        start = next(
            (
                index
                for index, item in enumerate(outer_try.body)
                if isinstance(item, ast.Assign)
                and any(
                    isinstance(target, ast.Name) and target.id == "client"
                    for target in item.targets
                )
            ),
            None,
        )
        stop = next(
            (
                index
                for index, item in enumerate(outer_try.body)
                if isinstance(item, ast.Assign)
                and any(
                    isinstance(target, (ast.Tuple, ast.List))
                    and any(
                        isinstance(element, ast.Name)
                        and element.id == "mutable_repository"
                        for element in target.elts
                    )
                    for target in item.targets
                )
            ),
            None,
        )
        if start is None or stop is None or stop <= start:
            raise ValueError("SWE worker acquisition boundary changed")
        outer_try.body[start + 1 : stop] = [
            ast.Expr(value=ast.Constant(value="QUALIFIED_LOCKED_IMAGE_ACQUISITION"))
        ]
    return ast.dump(tree, annotate_fields=True, include_attributes=False).encode("utf-8")


def _exercise_image_acquisition() -> dict[str, object]:
    from .adapters.swebench_verified_worker import _load_locked_local_image

    digest = "a" * 64
    locked = "example.invalid/swebench@sha256:" + digest

    class Missing(Exception):
        pass

    class Images:
        def __init__(self, outcome: object) -> None:
            self.outcome = outcome

        def get(self, reference: str) -> object:
            if reference != locked:
                raise AssertionError("mutable image lookup attempted")
            if isinstance(self.outcome, BaseException):
                raise self.outcome
            return self.outcome

    class Client:
        def __init__(self, outcome: object) -> None:
            self.images = Images(outcome)

    good = type("Image", (), {"attrs": {"RepoDigests": [locked]}})()
    wrong = type(
        "Image",
        (),
        {"attrs": {"RepoDigests": ["example.invalid/swebench@sha256:" + "b" * 64]}},
    )()
    if _load_locked_local_image(Client(good), locked, image_not_found_error=Missing) is not good:
        raise ValueError("locked-image positive test failed")
    failures = 0
    for outcome in (Missing(), wrong):
        try:
            _load_locked_local_image(Client(outcome), locked, image_not_found_error=Missing)
        except RuntimeError:
            failures += 1
    if failures != 2:
        raise ValueError("locked-image fail-closed tests failed")
    return {
        "test_policy": "in_process_fake_docker_no_network_v1",
        "cases": list(_IMAGE_ACQUISITION_TEST_CASES),
        "passed_cases": 3,
        "passed": True,
    }


def _semantic_components(
    *, project_root: Path, new_code_revision: str
) -> dict[str, dict[str, object]]:
    components: dict[str, dict[str, object]] = {}
    for relative in _SEMANTIC_FILES:
        old_raw = _git_bytes(project_root, V1R8_CODE_REVISION, relative)
        new_raw = _git_bytes(project_root, new_code_revision, relative)
        if old_raw != new_raw:
            raise ValueError(f"SWE qualification semantic component changed: {relative}")
        components[relative] = {
            "old_sha256": _sha_bytes(old_raw),
            "new_sha256": _sha_bytes(new_raw),
            "semantic_unchanged": True,
        }
    old_worker = _git_bytes(project_root, V1R8_CODE_REVISION, _WORKER_PATH)
    new_worker = _git_bytes(project_root, new_code_revision, _WORKER_PATH)
    old_projection = _sha_bytes(_worker_semantic_projection(old_worker))
    new_projection = _sha_bytes(_worker_semantic_projection(new_worker))
    if old_projection != new_projection:
        raise ValueError("SWE worker candidate/scoring semantic projection changed")
    components[_WORKER_PATH] = {
        "old_sha256": _sha_bytes(old_worker),
        "new_sha256": _sha_bytes(new_worker),
        "semantic_projection_old_sha256": old_projection,
        "semantic_projection_new_sha256": new_projection,
        "semantic_unchanged": True,
        "allowed_delta": "locked_image_acquisition_fail_closed_only",
    }
    return components


def _verify_old_evidence(
    *, qualification_root: Path, old_staging_path: Path
) -> dict[str, object]:
    root = qualification_root.resolve(strict=True)
    summary, summary_raw = _strict_json(
        root / "qualification_summary.json",
        fields=_SUMMARY_FIELDS,
        label="v1r8 qualification summary",
    )
    if _sha_bytes(summary_raw) != V1R8_QUALIFICATION_SUMMARY_SHA256:
        raise ValueError("v1r8 qualification summary hash differs")
    expected = {
        "schema_version": 1,
        "purpose": "swebench_contract_compatibility_preformal_qualification",
        "staging_plan_sha256": V1R8_STAGING_PLAN_SHA256,
        "code_revision": V1R8_CODE_REVISION,
        "rule_registry_sha256": V1R8_RULE_REGISTRY_SHA256,
        "task_id": V1R8_QUALIFICATION_TASK_ID,
        "task_binding_sha256": V1R8_QUALIFICATION_TASK_BINDING_SHA256,
        "cell_id": (
            "qualification:swebench-verified:"
            + V1R8_QUALIFICATION_TASK_ID
            + ":contract-compatibility"
        ),
        "attempted_rounds": 8,
        "valid_rounds": 5,
        "invalid_rounds": 3,
        "minimum_valid_rounds": 4,
        "validity_status": "sufficient_validity",
        "valid_only_mean": 1.0,
        "best_score": 1.0,
        "round_outcomes": [
            "valid",
            "valid",
            "valid",
            "valid",
            "contract_rejected",
            "contract_rejected",
            "contract_rejected",
            "valid",
        ],
        "formal_score_reuse_forbidden": True,
        "may_start_formal_stream": True,
        "sealed": True,
    }
    if summary != expected:
        raise ValueError("v1r8 qualification summary contents differ")
    staging_path = old_staging_path.resolve(strict=True)
    staging_raw = staging_path.read_bytes()
    if _sha_bytes(staging_raw) != V1R8_STAGING_PLAN_SHA256:
        raise ValueError("v1r8 qualification source staging hash differs")
    staging = json.loads(staging_raw)
    if (
        not isinstance(staging, dict)
        or staging.get("schema_version") != 5
        or staging.get("code_revision") != V1R8_CODE_REVISION
        or staging.get("source_hashes", {}).get("rule_registry")
        != V1R8_RULE_REGISTRY_SHA256
        or not any(
            isinstance(item, dict)
            and item.get("suite") == "swebench-verified"
            and item.get("task_id") == V1R8_QUALIFICATION_TASK_ID
            for item in staging.get("stream", ())
        )
    ):
        raise ValueError("v1r8 qualification staging binding differs")

    round_hashes: dict[str, str] = {}
    observed_outcomes: list[str] = []
    for index in range(1, 9):
        version = f"v{index:03d}"
        path = root / "cell" / "rounds" / f"{version}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        attempt = payload.get("attempt") if isinstance(payload, dict) else None
        if (
            not isinstance(attempt, dict)
            or payload.get("schema_version") != 1
            or payload.get("version") != version
            or payload.get("suite") != "swebench-verified"
            or payload.get("instance_id")
            != "swebench-verified:" + V1R8_QUALIFICATION_TASK_ID
            or payload.get("cell_id") != expected["cell_id"]
            or attempt.get("outcome") != expected["round_outcomes"][index - 1]
        ):
            raise ValueError("v1r8 qualification round evidence differs")
        observed_outcomes.append(str(attempt["outcome"]))
        round_hashes[version] = _sha(path)
    if observed_outcomes != summary["round_outcomes"]:
        raise ValueError("v1r8 qualification evidence disagrees with summary")
    state = json.loads((root / "cell" / "state.json").read_text(encoding="utf-8"))
    if state.get("event_count") != 8:
        raise ValueError("v1r8 qualification state is not sealed at eight rounds")
    return {
        "summary_sha256": V1R8_QUALIFICATION_SUMMARY_SHA256,
        "source_staging_plan_sha256": V1R8_STAGING_PLAN_SHA256,
        "source_code_revision": V1R8_CODE_REVISION,
        "rule_registry_sha256": V1R8_RULE_REGISTRY_SHA256,
        "task_id": V1R8_QUALIFICATION_TASK_ID,
        "task_binding_sha256": V1R8_QUALIFICATION_TASK_BINDING_SHA256,
        "attempted_rounds": 8,
        "valid_rounds": 5,
        "minimum_valid_rounds": 4,
        "validity_status": "sufficient_validity",
        "round_sha256s": round_hashes,
        "cell_ledger_sha256": _sha(root / "cell" / "ledger.jsonl"),
        "cell_state_sha256": _sha(root / "cell" / "state.json"),
        "sealed": True,
    }


def _verify_new_inputs(
    *,
    selection_path: Path,
    task_lock_path: Path,
    image_lock_path: Path,
    gold_canary_summary_path: Path,
) -> dict[str, object]:
    selection_path = selection_path.resolve(strict=True)
    task_lock_path = task_lock_path.resolve(strict=True)
    image_lock_path = image_lock_path.resolve(strict=True)
    canary_path = gold_canary_summary_path.resolve(strict=True)
    selection = json.loads(selection_path.read_text(encoding="utf-8"))
    selected = tuple(
        item.get("instance_id") if isinstance(item, dict) else None
        for item in selection.get("selected", ())
    ) if isinstance(selection, dict) else ()
    if selected != SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS:
        raise ValueError("v1r9 qualification selection differs")
    task_lock = json.loads(task_lock_path.read_text(encoding="utf-8"))
    task_ids = tuple(
        item.get("instance_id") if isinstance(item, dict) else None
        for item in task_lock.get("tasks", ())
    ) if isinstance(task_lock, dict) else ()
    if (
        task_lock.get("schema") != "swebench_verified_active_task_lock.v2"
        or task_lock.get("selection_mode")
        != SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE
        or task_lock.get("selection_sha256") != _sha(selection_path)
        or task_ids != SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
    ):
        raise ValueError("v1r9 qualification task lock differs")
    image_lock = json.loads(image_lock_path.read_text(encoding="utf-8"))
    images = _validate_swebench_image_lock(
        image_lock,
        selection_mode=SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        expected_task_ids=SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS,
    )
    canary = json.loads(canary_path.read_text(encoding="utf-8"))
    expected_canary_fields = {
        "schema_version",
        "suite",
        "dataset_sha256",
        "selection_sha256",
        "image_lock_sha256",
        "selected_instances",
        "candidate_policy",
        "gold_patch_normalization",
        "trust_grade",
        "results",
        "passed",
        "selection_mode",
        "remote_execution_contract",
    }
    if (
        not isinstance(canary, dict)
        or set(canary) != expected_canary_fields
        or canary.get("schema_version") != 2
        or canary.get("suite") != "swebench-verified"
        or canary.get("selection_mode")
        != SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE
        or tuple(canary.get("selected_instances", ()))
        != SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS
        or canary.get("selection_sha256") != _sha(selection_path)
        or canary.get("image_lock_sha256") != _sha(image_lock_path)
        or canary.get("dataset_sha256") != task_lock.get("dataset_sha256")
        or canary.get("candidate_policy")
        != "official_gold_patch_canonicalized_no_model"
        or canary.get("gold_patch_normalization")
        != "deterministic_nonsemantic_index_metadata_v1"
        or canary.get("trust_grade")
        != "official_standard_candidate_visible_test_process"
        or canary.get("passed") is not True
    ):
        raise ValueError("v1r9 six-task gold canary summary differs")
    results = canary.get("results")
    remote_execution = canary.get("remote_execution_contract")
    if (
        not isinstance(remote_execution, dict)
        or set(remote_execution)
        != {
            "host_alias",
            "remote_python",
            "remote_project_root",
            "remote_swebench_source_root",
        }
        or not isinstance(remote_execution.get("host_alias"), str)
        or re.fullmatch(r"[A-Za-z0-9_.-]+", remote_execution["host_alias"]) is None
        or any(
            not isinstance(remote_execution.get(field), str)
            or not remote_execution[field].startswith("/")
            or any(character.isspace() for character in remote_execution[field])
            for field in (
                "remote_python",
                "remote_project_root",
                "remote_swebench_source_root",
            )
        )
    ):
        raise ValueError("v1r9 gold canary remote execution contract differs")
    tasks = {item["instance_id"]: item for item in task_lock["tasks"]}
    if not isinstance(results, list) or len(results) != 6:
        raise ValueError("v1r9 gold canary result count differs")
    for result, instance_id in zip(results, SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS, strict=True):
        if not isinstance(result, dict):
            raise ValueError("v1r9 gold canary result differs")
        hashes = (
            result.get("task_sha256"),
            result.get("image_manifest_sha256"),
            result.get("official_gold_patch_sha256"),
            result.get("candidate_sha256"),
            result.get("private_result_sha256"),
        )
        if (
            result.get("instance_id") != instance_id
            or result.get("resolved") is not True
            or result.get("score") != 1.0
            or result.get("gold_patch_normalization")
            != "deterministic_nonsemantic_index_metadata_v1"
            or result.get("trust_grade")
            != "official_standard_candidate_visible_test_process"
            or result.get("task_sha256") != tasks[instance_id].get("task_sha256")
            or result.get("image_manifest_sha256")
            != images[instance_id][0].rsplit("@sha256:", 1)[1]
            or any(not isinstance(value, str) or not _SHA256.fullmatch(value) for value in hashes)
        ):
            raise ValueError("v1r9 gold canary result binding differs")
    return {
        "selection_mode": SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        "active_instance_ids": list(SWEBENCH_VERIFIED_V1R9_ACTIVE_TASKS),
        "dataset_sha256": canary["dataset_sha256"],
        "selection_sha256": _sha(selection_path),
        "task_lock_sha256": _sha(task_lock_path),
        "image_lock_sha256": _sha(image_lock_path),
        "gold_canary_summary_sha256": _sha(canary_path),
        "gold_canary_passed_instances": 6,
        "gold_canary_passed": True,
        "remote_execution_contract": remote_execution,
    }


def _verify_receipt_shape(payload: Mapping[str, object]) -> None:
    historical = _exact_object(
        payload.get("historical_qualification"),
        fields=_HISTORICAL_FIELDS,
        label="SWE qualification transfer historical qualification",
    )
    expected_historical = {
        "summary_sha256": V1R8_QUALIFICATION_SUMMARY_SHA256,
        "source_staging_plan_sha256": V1R8_STAGING_PLAN_SHA256,
        "source_code_revision": V1R8_CODE_REVISION,
        "rule_registry_sha256": V1R8_RULE_REGISTRY_SHA256,
        "task_id": V1R8_QUALIFICATION_TASK_ID,
        "task_binding_sha256": V1R8_QUALIFICATION_TASK_BINDING_SHA256,
        "attempted_rounds": 8,
        "valid_rounds": 5,
        "minimum_valid_rounds": 4,
        "validity_status": "sufficient_validity",
        "sealed": True,
    }
    if any(historical.get(key) != value for key, value in expected_historical.items()):
        raise ValueError("SWE qualification transfer historical qualification differs")
    round_hashes = _exact_object(
        historical.get("round_sha256s"),
        fields={f"v{index:03d}" for index in range(1, 9)},
        label="SWE qualification transfer historical round hashes",
    )
    if any(
        not isinstance(value, str) or not _SHA256.fullmatch(value)
        for value in round_hashes.values()
    ) or any(
        not isinstance(historical.get(field), str)
        or not _SHA256.fullmatch(str(historical[field]))
        for field in ("cell_ledger_sha256", "cell_state_sha256")
    ):
        raise ValueError("SWE qualification transfer historical hashes differ")

    semantic = _exact_object(
        payload.get("semantic_transfer"),
        fields=_SEMANTIC_TRANSFER_FIELDS,
        label="SWE qualification transfer semantic transfer",
    )
    components = _exact_object(
        semantic.get("components"),
        fields=set(_SEMANTIC_FILES) | {_WORKER_PATH},
        label="SWE qualification transfer semantic components",
    )
    for relative in _SEMANTIC_FILES:
        _exact_object(
            components.get(relative),
            fields=_SEMANTIC_COMPONENT_FIELDS,
            label=f"SWE qualification transfer semantic component {relative}",
        )
    _exact_object(
        components.get(_WORKER_PATH),
        fields=_WORKER_COMPONENT_FIELDS,
        label="SWE qualification transfer worker component",
    )
    acquisition = _exact_object(
        semantic.get("image_acquisition_delta_tests"),
        fields=_IMAGE_ACQUISITION_TEST_FIELDS,
        label="SWE qualification transfer image acquisition tests",
    )
    if (
        acquisition.get("test_policy") != "in_process_fake_docker_no_network_v1"
        or acquisition.get("cases") != _IMAGE_ACQUISITION_TEST_CASES
        or acquisition.get("passed_cases") != len(_IMAGE_ACQUISITION_TEST_CASES)
        or acquisition.get("passed") is not True
    ):
        raise ValueError("SWE qualification transfer image acquisition tests differ")

    inputs = _exact_object(
        payload.get("v1r9_inputs"),
        fields=_V1R9_INPUT_FIELDS,
        label="SWE qualification transfer v1r9 inputs",
    )
    _exact_object(
        inputs.get("remote_execution_contract"),
        fields=_REMOTE_EXECUTION_FIELDS,
        label="SWE qualification transfer remote execution contract",
    )
    _exact_object(
        payload.get("transfer_usage"),
        fields=_TRANSFER_USAGE_FIELDS,
        label="SWE qualification transfer usage",
    )


def _write_cas(directory: Path, raw: bytes) -> Path:
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    digest = _sha_bytes(raw)
    path = directory / f"{digest}.json"
    if path.exists() or path.is_symlink():
        if path.is_symlink() or path.read_bytes() != raw:
            raise ValueError("qualification transfer CAS is already rebound")
        return path
    descriptor, name = tempfile.mkstemp(dir=directory, suffix=".qualification-transfer.tmp")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, 0o444)
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return path


def prepare_swebench_qualification_transfer(
    *,
    project_root: Path,
    output_root: Path,
    new_code_revision: str,
    old_qualification_root: Path,
    old_staging_path: Path,
    selection_path: Path,
    task_lock_path: Path,
    image_lock_path: Path,
    gold_canary_summary_path: Path,
) -> Path:
    if not isinstance(new_code_revision, str) or not _COMMIT.fullmatch(new_code_revision):
        raise ValueError("qualification transfer requires a full new revision")
    project_root = _verify_clean_successor_project_root(
        project_root,
        expected_revision=new_code_revision,
    )
    historical = _verify_old_evidence(
        qualification_root=old_qualification_root,
        old_staging_path=old_staging_path,
    )
    components = _semantic_components(
        project_root=project_root,
        new_code_revision=new_code_revision,
    )
    new_inputs = _verify_new_inputs(
        selection_path=selection_path,
        task_lock_path=task_lock_path,
        image_lock_path=image_lock_path,
        gold_canary_summary_path=gold_canary_summary_path,
    )
    payload = {
        "schema_version": 1,
        "kind": "swebench_contract_qualification_transfer_v1r8_to_v1r9",
        "historical_qualification": historical,
        "semantic_transfer": {
            "old_code_revision": V1R8_CODE_REVISION,
            "new_code_revision": new_code_revision,
            "policy": _SEMANTIC_POLICY,
            "components": components,
            "image_acquisition_delta_tests": _exercise_image_acquisition(),
            "passed": True,
        },
        "v1r9_inputs": new_inputs,
        "transfer_usage": {
            "model_calls_started": 0,
            "evaluator_transactions_started": 0,
        },
        "formal_score_reuse": False,
        "passed": True,
        "may_start_formal_stream": True,
    }
    raw = _canonical_bytes(payload)
    return _write_cas(output_root.resolve() / "swebench-qualification-transfer", raw)


def verify_swebench_qualification_transfer(
    path: Path,
    *,
    project_root: Path,
    expected_new_code_revision: str,
    selection_path: Path,
    task_lock_path: Path,
    image_lock_path: Path,
    gold_canary_summary_path: Path,
) -> dict[str, Any]:
    payload, raw = _strict_json(
        path, fields=_RECEIPT_FIELDS, label="SWE qualification transfer receipt"
    )
    digest = _sha_bytes(raw)
    if path.name != f"{digest}.json":
        raise ValueError("SWE qualification transfer receipt is not content addressed")
    _verify_receipt_shape(payload)
    historical = payload["historical_qualification"]
    semantic = payload["semantic_transfer"]
    usage = payload["transfer_usage"]
    assert isinstance(historical, dict)
    assert isinstance(semantic, dict)
    if (
        payload.get("schema_version") != 1
        or payload.get("kind")
        != "swebench_contract_qualification_transfer_v1r8_to_v1r9"
        or historical.get("summary_sha256") != V1R8_QUALIFICATION_SUMMARY_SHA256
        or historical.get("source_staging_plan_sha256") != V1R8_STAGING_PLAN_SHA256
        or historical.get("source_code_revision") != V1R8_CODE_REVISION
        or historical.get("rule_registry_sha256") != V1R8_RULE_REGISTRY_SHA256
        or historical.get("task_binding_sha256")
        != V1R8_QUALIFICATION_TASK_BINDING_SHA256
        or historical.get("valid_rounds") != 5
        or historical.get("minimum_valid_rounds") != 4
        or historical.get("validity_status") != "sufficient_validity"
        or historical.get("sealed") is not True
        or semantic.get("old_code_revision") != V1R8_CODE_REVISION
        or semantic.get("new_code_revision") != expected_new_code_revision
        or semantic.get("policy") != _SEMANTIC_POLICY
        or semantic.get("passed") is not True
        or usage != {"model_calls_started": 0, "evaluator_transactions_started": 0}
        or payload.get("formal_score_reuse") is not False
        or payload.get("passed") is not True
        or payload.get("may_start_formal_stream") is not True
    ):
        raise ValueError("SWE qualification transfer receipt gate differs")
    clean_root = _verify_clean_successor_project_root(
        project_root,
        expected_revision=expected_new_code_revision,
    )
    observed_components = _semantic_components(
        project_root=clean_root,
        new_code_revision=expected_new_code_revision,
    )
    if semantic.get("components") != observed_components:
        raise ValueError("SWE qualification transfer semantic components drifted")
    observed_acquisition_tests = _exercise_image_acquisition()
    if semantic.get("image_acquisition_delta_tests") != observed_acquisition_tests:
        raise ValueError("SWE qualification transfer image acquisition tests drifted")
    observed_inputs = _verify_new_inputs(
        selection_path=selection_path,
        task_lock_path=task_lock_path,
        image_lock_path=image_lock_path,
        gold_canary_summary_path=gold_canary_summary_path,
    )
    if payload.get("v1r9_inputs") != observed_inputs:
        raise ValueError("SWE qualification transfer v1r9 inputs drifted")
    return payload


__all__ = [
    "V1R8_CODE_REVISION",
    "V1R8_QUALIFICATION_SUMMARY_SHA256",
    "V1R8_STAGING_PLAN_SHA256",
    "prepare_swebench_qualification_transfer",
    "verify_swebench_qualification_transfer",
]
