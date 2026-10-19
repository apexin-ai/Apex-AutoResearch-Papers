from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Sequence

from .adapters.swebench_verified import (
    SWEBENCH_VERIFIED_DATASET_SHA256,
    SWEBenchVerifiedRemoteAdapter,
    SWEBenchVerifiedResult,
    SWEBenchVerifiedTask,
)
from .adapters.sweperf import validate_unified_diff
from .contract_compatibility import normalize_swebench_verified_response
from .three_arm_providers import (
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R8,
    SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
    _resolve_swebench_selection_contract,
    _swebench_remote_execution_contract,
    _validate_swebench_image_lock,
    validate_swebench_verified_selection,
)


GOLD_PATCH_NORMALIZATION = "deterministic_nonsemantic_index_metadata_v1"


def _canonical_bytes(payload: object) -> bytes:
    return (
        json.dumps(
            payload,
            ensure_ascii=True,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_once(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != content:
            raise RuntimeError(f"refusing to overwrite SWE-bench canary artifact: {path.name}")
        return
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, suffix=".swebench-canary")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary).replace(path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def _canonicalize_official_gold_patch(patch: str) -> str:
    """Use the same safe, deterministic compatibility policy as formal candidates."""

    result = normalize_swebench_verified_response(patch).text
    validate_unified_diff(result)
    return result


def _gold_canary_result_passed(result: SWEBenchVerifiedResult) -> bool:
    return (
        result.status == "valid"
        and result.valid_scored is True
        and result.resolved is True
        and result.score == 1.0
        and result.fail_to_pass_passed == result.fail_to_pass_total
        and result.pass_to_pass_passed == result.pass_to_pass_total
    )


def run_swebench_verified_canary(
    *,
    artifact_root: Path,
    dataset_path: Path,
    selection_path: Path,
    image_lock_path: Path,
    host_alias: str,
    remote_python: str,
    remote_project_root: str,
    remote_swebench_source_root: str,
    remote_attempt_root: str,
    selection_mode: str = SWEBENCH_VERIFIED_SELECTION_MODE_V1R8,
    expected_instances: Sequence[str] | None = None,
) -> Path:
    dataset_path = dataset_path.resolve(strict=True)
    selection_path = selection_path.resolve(strict=True)
    image_lock_path = image_lock_path.resolve(strict=True)
    if _sha(dataset_path) != SWEBENCH_VERIFIED_DATASET_SHA256:
        raise RuntimeError("SWE-bench canary dataset digest differs")
    selected, _online_ids = _resolve_swebench_selection_contract(
        selection_mode=selection_mode,
        expected_task_ids=expected_instances,
    )
    try:
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover - production dependency gate.
        raise RuntimeError("pyarrow is required for the SWE-bench canary") from exc
    selection_columns = (
        ["instance_id"]
        if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R8
        else ["instance_id", "repo", "FAIL_TO_PASS", "PASS_TO_PASS"]
    )
    selection_rows = pq.read_table(
        dataset_path, columns=selection_columns
    ).to_pylist()
    selection = json.loads(selection_path.read_text(encoding="utf-8"))
    try:
        validate_swebench_verified_selection(
            selection,
            selection_rows,
            selection_mode=selection_mode,
            expected_task_ids=selected,
        )
    except ValueError as exc:
        raise RuntimeError("SWE-bench canary selection differs") from exc
    image_lock = json.loads(image_lock_path.read_text(encoding="utf-8"))
    try:
        images = _validate_swebench_image_lock(
            image_lock,
            selection_mode=selection_mode,
            expected_task_ids=selected,
        )
    except ValueError as exc:
        raise RuntimeError("SWE-bench canary image lock differs") from exc
    rows = {
        row["instance_id"]: row
        for row in pq.read_table(dataset_path).to_pylist()
        if row["instance_id"] in selected
    }
    if set(rows) != set(selected):
        raise RuntimeError("SWE-bench canary selected rows are missing")

    evidence: list[dict[str, object]] = []
    for instance_id in selected:
        row = dict(rows[instance_id])
        locked, mutable = images[instance_id]
        task_sha = hashlib.sha256(_canonical_bytes(row)).hexdigest()
        task = SWEBenchVerifiedTask(
            instance=row,
            task_sha256=task_sha,
            locked_image_ref=locked,
            mutable_image_ref=mutable,
        )
        instance_root = artifact_root.resolve() / "instances" / instance_id
        candidate_path = instance_root / "gold.patch"
        private_result_path = instance_root / "private-result.json"
        official_patch = str(row["patch"]).rstrip("\n") + "\n"
        patch = _canonicalize_official_gold_patch(official_patch)
        _write_once(candidate_path, patch.encode("utf-8"))
        adapter = SWEBenchVerifiedRemoteAdapter(
            task=task,
            host_alias=host_alias,
            remote_python=remote_python,
            remote_project_root=remote_project_root,
            remote_swebench_source_root=remote_swebench_source_root,
            remote_attempt_root=remote_attempt_root,
        )
        if private_result_path.is_file():
            candidate_sha = _sha(candidate_path)
            result = adapter._parse_result(
                private_result_path.read_bytes(),
                expected_attempt_id=adapter._attempt_id(
                    instance_id=instance_id,
                    candidate_sha256=candidate_sha,
                    private_result_path=private_result_path,
                ),
                expected_candidate_sha256=candidate_sha,
            )
        else:
            result = adapter.evaluate(candidate_path, private_result_path)
        if not _gold_canary_result_passed(result):
            raise RuntimeError(f"SWE-bench gold canary failed for {instance_id}")
        evidence.append(
            {
                "instance_id": instance_id,
                "task_sha256": task_sha,
                "image_manifest_sha256": locked.rsplit("@sha256:", 1)[1],
                "official_gold_patch_sha256": hashlib.sha256(
                    official_patch.encode("utf-8")
                ).hexdigest(),
                "gold_patch_normalization": GOLD_PATCH_NORMALIZATION,
                "candidate_sha256": result.candidate_sha256,
                "private_result_sha256": _sha(private_result_path),
                "resolved": result.resolved,
                "score": result.score,
                "trust_grade": result.trust_grade,
            }
        )
    summary = {
        "schema_version": (
            1
            if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R8
            else 2
        ),
        "suite": "swebench-verified",
        "dataset_sha256": SWEBENCH_VERIFIED_DATASET_SHA256,
        "selection_sha256": _sha(selection_path),
        "image_lock_sha256": _sha(image_lock_path),
        "selected_instances": list(selected),
        "candidate_policy": "official_gold_patch_canonicalized_no_model",
        "gold_patch_normalization": GOLD_PATCH_NORMALIZATION,
        "trust_grade": "official_standard_candidate_visible_test_process",
        "results": evidence,
        "passed": True,
    }
    if selection_mode == SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE:
        summary["selection_mode"] = selection_mode
        summary["remote_execution_contract"] = _swebench_remote_execution_contract(
            host_alias=host_alias,
            remote_python=remote_python,
            remote_project_root=remote_project_root,
            remote_swebench_source_root=remote_swebench_source_root,
        )
    summary_path = artifact_root.resolve() / "summary.json"
    _write_once(summary_path, _canonical_bytes(summary))
    return summary_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the pinned SWE-bench Verified canary")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--selection", type=Path, required=True)
    parser.add_argument("--image-lock", type=Path, required=True)
    parser.add_argument("--host-alias", default="a100jump")
    parser.add_argument("--remote-python", required=True)
    parser.add_argument("--remote-project-root", required=True)
    parser.add_argument("--remote-swebench-source-root", required=True)
    parser.add_argument("--remote-attempt-root", required=True)
    parser.add_argument(
        "--selection-mode",
        choices=(
            SWEBENCH_VERIFIED_SELECTION_MODE_V1R8,
            SWEBENCH_VERIFIED_SELECTION_MODE_V1R9_ACTIVE,
        ),
        default=SWEBENCH_VERIFIED_SELECTION_MODE_V1R8,
    )
    parser.add_argument(
        "--expected-instance",
        action="append",
        dest="expected_instances",
    )
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args(argv)
    if not args.execute:
        parser.error("SWE-bench canary requires explicit --execute")
    path = run_swebench_verified_canary(
        artifact_root=args.artifact_root,
        dataset_path=args.dataset,
        selection_path=args.selection,
        image_lock_path=args.image_lock,
        host_alias=args.host_alias,
        remote_python=args.remote_python,
        remote_project_root=args.remote_project_root,
        remote_swebench_source_root=args.remote_swebench_source_root,
        remote_attempt_root=args.remote_attempt_root,
        selection_mode=args.selection_mode,
        expected_instances=args.expected_instances,
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
