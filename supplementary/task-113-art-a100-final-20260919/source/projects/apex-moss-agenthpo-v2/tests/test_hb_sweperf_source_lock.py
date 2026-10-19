from __future__ import annotations

import hashlib
import json
import socket
import subprocess
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from optimization_lab.harness_builder.adapters.sweperf import (
    DATASET_COMMIT,
    EVALUATOR_COMMIT,
    FROZEN_TASKS,
)
from optimization_lab.harness_builder.sweperf_wrapper import source_lock_prepare


ROOT = Path(__file__).resolve().parents[1]
PILOT_MANIFEST = (
    ROOT / "optimization_lab/harness_builder/data/hb_gen1_candidates.json"
)
GOLD_PATCH = "GOLD_PATCH_MUST_NEVER_BE_LOADED_OR_WRITTEN"
GOLD_TEST_PATCH = "GOLD_TEST_PATCH_MUST_NEVER_BE_LOADED_OR_WRITTEN"
GOLD_HEAD = "GOLD_HEAD_COMMIT_MUST_NEVER_BE_LOADED_OR_WRITTEN"
GOLD_HUMAN = "GOLD_HUMAN_PATCH_MUST_NEVER_BE_LOADED_OR_WRITTEN"


def _detached_repo(path: Path, commit: str) -> Path:
    (path / ".git").mkdir(parents=True)
    (path / ".git/HEAD").write_text(f"{commit}\n", encoding="ascii")
    return path


def _dataset_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index, task in enumerate(FROZEN_TASKS.values()):
        rows.append(
            {
                "repo": task.repository,
                "instance_id": task.instance_id,
                "patch": f"{GOLD_PATCH}:{index}",
                "test_patch": f"{GOLD_TEST_PATCH}:{index}",
                "base_commit": task.base_commit,
                "head_commit": f"{GOLD_HEAD}:{index}",
                "version": f"v{index}",
                "efficiency_test": [f"tests/test_{index}.py::test_speed"],
                "test_functions": json.dumps(
                    {
                        f"pkg/module_{index}.py": [
                            f"public_function_{index}",
                            f"PublicClass{index}.method",
                        ]
                    },
                    separators=(",", ":"),
                    sort_keys=True,
                ),
                "problem_statement_realistic": f"public realistic problem {index}",
                "human_performance": f"{GOLD_HUMAN}:{index}",
            }
        )
    return rows


def _sources(tmp_path: Path, monkeypatch) -> tuple[Path, Path, Path, Path]:
    evaluator = _detached_repo(tmp_path / "evaluator", EVALUATOR_COMMIT)
    dataset = _detached_repo(tmp_path / "dataset", DATASET_COMMIT)
    parquet = dataset / "data/test.parquet"
    parquet.parent.mkdir()
    pq.write_table(pa.Table.from_pylist(_dataset_rows()), parquet)
    observed = hashlib.sha256(parquet.read_bytes()).hexdigest()
    monkeypatch.setattr(source_lock_prepare, "DATASET_PARQUET_SHA256", observed)
    output = tmp_path / "out"
    return evaluator, dataset, parquet, output


def _prepare(
    evaluator: Path,
    dataset: Path,
    parquet: Path,
    output: Path,
    *,
    pilot_manifest: Path = PILOT_MANIFEST,
):
    return source_lock_prepare.prepare_sweperf_source_lock(
        evaluator_repo=evaluator,
        dataset_repo=dataset,
        parquet_path=parquet,
        pilot_manifest_path=pilot_manifest,
        output_root=output,
    )


def test_prepare_extracts_only_public_fields_and_fails_closed(
    tmp_path: Path, monkeypatch
) -> None:
    evaluator, dataset, parquet, output = _sources(tmp_path, monkeypatch)

    def no_subprocess(*args, **kwargs):
        raise AssertionError("source-lock prepare must not spawn a process")

    def no_socket(*args, **kwargs):
        raise AssertionError("source-lock prepare must not use a network socket")

    monkeypatch.setattr(subprocess, "run", no_subprocess)
    monkeypatch.setattr(subprocess, "Popen", no_subprocess)
    monkeypatch.setattr(socket, "socket", no_socket)
    prepared = _prepare(evaluator, dataset, parquet, output)

    assert prepared.status == "blocked"
    assert prepared.runnable_wrapper_source_lock is False
    payload = json.loads(prepared.report_path.read_text(encoding="ascii"))
    assert payload["content_id"] == prepared.content_id
    assert payload["status"] == "blocked"
    assert payload["runnable_wrapper_source_lock"] is False
    assert payload["loaded_dataset_columns"] == [
        "repo",
        "instance_id",
        "base_commit",
        "version",
        "efficiency_test",
        "test_functions",
        "problem_statement_realistic",
    ]
    assert [item["instance_id"] for item in payload["tasks"]] == list(FROZEN_TASKS)
    first = payload["tasks"][0]
    assert first["allowed_patch_paths"] == ["pkg/module_0.py"]
    assert first["test_functions"] == {
        "pkg/module_0.py": ["public_function_0", "PublicClass0.method"]
    }
    assert first["realistic_problem_sha256"] == hashlib.sha256(
        b"public realistic problem 0"
    ).hexdigest()
    assert first["task_sha256"] == next(iter(FROZEN_TASKS.values())).task_sha256
    assert {item["code"] for item in payload["blockers"]} == {
        "local_repo_digest_unverified",
        "in_process_candidate_outcome_unattestable",
    }
    assert payload["external_actions"] == {
        "docker_invoked": False,
        "evaluator_invoked": False,
        "gpu_used": False,
        "model_invoked": False,
        "network_used": False,
    }

    raw = prepared.report_path.read_bytes()
    for secret in (GOLD_PATCH, GOLD_TEST_PATCH, GOLD_HEAD, GOLD_HUMAN):
        assert secret.encode("ascii") not in raw
    assert not (output / "wrapper-source-lock.json").exists()


def test_prepare_is_content_addressed_and_idempotent(
    tmp_path: Path, monkeypatch
) -> None:
    evaluator, dataset, parquet, output = _sources(tmp_path, monkeypatch)
    first = _prepare(evaluator, dataset, parquet, output)
    before = first.report_path.read_bytes()
    second = _prepare(evaluator, dataset, parquet, output)

    assert first == second
    assert first.report_path.name == f"{first.content_id}.json"
    assert first.report_path.read_bytes() == before
    assert len(tuple(output.glob("*.json"))) == 1
    core = json.loads(before)
    content_id = core.pop("content_id")
    assert content_id == hashlib.sha256(
        json.dumps(core, ensure_ascii=True, separators=(",", ":"), sort_keys=True).encode(
            "ascii"
        )
    ).hexdigest()


def test_parquet_hash_mismatch_never_reads_rows_and_writes_blocked_report(
    tmp_path: Path, monkeypatch
) -> None:
    evaluator, dataset, parquet, output = _sources(tmp_path, monkeypatch)
    expected = source_lock_prepare.DATASET_PARQUET_SHA256
    parquet.write_bytes(parquet.read_bytes() + b"tampered")

    prepared = _prepare(evaluator, dataset, parquet, output)
    payload = json.loads(prepared.report_path.read_text(encoding="ascii"))
    assert payload["status"] == "blocked"
    assert payload["tasks"] == []
    assert payload["dataset_rows_loaded"] is False
    assert payload["source_observations"]["dataset_parquet_sha256"] != expected
    assert "dataset_parquet_sha256_mismatch" in {
        item["code"] for item in payload["blockers"]
    }


def test_manifest_task_hash_mismatch_blocks_before_dataset_rows_are_accepted(
    tmp_path: Path, monkeypatch
) -> None:
    evaluator, dataset, parquet, output = _sources(tmp_path, monkeypatch)
    manifest = json.loads(PILOT_MANIFEST.read_text(encoding="utf-8"))
    sweperf = next(item for item in manifest["benchmarks"] if item["suite"] == "swe-perf")
    sweperf["candidates"][0]["source_sha256"] = "0" * 64
    changed = tmp_path / "changed-manifest.json"
    changed.write_text(json.dumps(manifest), encoding="utf-8")

    prepared = _prepare(
        evaluator,
        dataset,
        parquet,
        output,
        pilot_manifest=changed,
    )
    payload = json.loads(prepared.report_path.read_text(encoding="ascii"))
    assert payload["tasks"] == []
    assert payload["dataset_rows_loaded"] is False
    assert "frozen_task_hash_mismatch" in {
        item["code"] for item in payload["blockers"]
    }


def test_missing_image_digest_and_unattestable_outcome_are_hard_blockers(
    tmp_path: Path, monkeypatch
) -> None:
    evaluator, dataset, parquet, output = _sources(tmp_path, monkeypatch)
    prepared = _prepare(evaluator, dataset, parquet, output)
    payload = json.loads(prepared.report_path.read_text(encoding="ascii"))

    blockers = {item["code"]: item for item in payload["blockers"]}
    assert blockers["local_repo_digest_unverified"]["scope"] == "all_frozen_tasks"
    assert blockers["in_process_candidate_outcome_unattestable"]["scope"] == (
        "wrapper_result_channel"
    )
    assert payload["command_trust"]["status"] == "blocked"
    assert payload["command_trust"]["report_writer"] == "candidate_worker_uid_65534"
    assert payload["command_trust"]["report_consumer"] == "root_supervisor"
    verdict = payload["command_trust"]["capability_verdict"]
    assert verdict["reason_code"] == "in_process_candidate_outcome_unattestable"
    assert verdict["semantics_preserving_channel_implemented"] is False
    assert verdict["frozen_topology"][
        "candidate_and_pytest_reporter_share_process"
    ] is True
    assert payload["upstream_images"]["status"] == "unverified"
    assert payload["upstream_images"]["repo_digests"] == {}
