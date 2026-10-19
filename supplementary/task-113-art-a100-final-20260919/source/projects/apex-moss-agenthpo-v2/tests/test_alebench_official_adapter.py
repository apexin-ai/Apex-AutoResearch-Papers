from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from optimization_lab.harness_builder.dual_runtime import EvaluationResult
from optimization_lab.harness_builder.official_solutions import ALEBenchCodeCodec
from optimization_lab.harness_builder.experiment_one import FreezeReceipt
from optimization_lab.harness_builder.adapters import alebench_official as ale_module
from optimization_lab.harness_builder.adapters.alebench_official import (
    ALE_BENCH_DATASET_REVISION,
    ALE_BENCH_SOURCE_COMMIT,
    ALEBenchContract,
    ALEBenchOfficialAdapter,
    FreezeAuthorization,
    ObservedALEBenchIdentity,
)

ALE_DIGEST = "sha256:e0ec0e015b3e11fda1ecdd0df270f83cee12136b37bbac438e8c861b4dfd420e"
ALE_ZIP_SHA = "b4f02d3cbcea3200d3e7d29dcf27b1e0bcce1fb566ed249541683114f7986585"


def _artifact():
    return ALEBenchCodeCodec().parse(
        "```cpp23\n#include <iostream>\nint main() { return 0; }\n```"
    )


def _contract(tmp_path: Path) -> ALEBenchContract:
    return ALEBenchContract(
        source_root=tmp_path / "ale-source",
        dataset_root=tmp_path / "ale-data",
        python_executable=tmp_path / "ale-venv" / "bin" / "python",
        source_commit=ALE_BENCH_SOURCE_COMMIT,
        dataset_revision=ALE_BENCH_DATASET_REVISION,
        task_id="ahc024",
        docker_image_reference="ale-bench:cpp23-202301",
        docker_image_digest=ALE_DIGEST,
        judge_version="202301",
        time_limit_seconds=2,
        memory_limit_bytes=1 << 30,
        score_direction="maximize",
        public_evaluator_command=("ale_bench.Session", "public_eval"),
        private_evaluator_command=("ale_bench.Session", "private_eval"),
    )


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _authorization(tmp_path: Path, contract: ALEBenchContract, artifact, *, target_id: str | None = None) -> FreezeAuthorization:
    evaluator = tmp_path / "evaluator.json"
    evidence = tmp_path / "public-evidence.json"
    evaluator.write_bytes(b"evaluator receipt\n")
    evidence.write_bytes(b"public evidence\n")
    adapter = ALEBenchOfficialAdapter(contract=contract, private_evidence_root=tmp_path / "private", session_factory=lambda **_: None, identity_probe=lambda _: _observed(contract))
    harness_sha = "12" * 32
    receipt = FreezeReceipt(
        schema_version=1, manifest_sha256="01" * 32, benchmark="alebench", seed_id="S1", position="A",
        task_id=target_id or contract.task_id, target_binding_sha256="02" * 32, selected_round=1,
        harness_sha256=harness_sha, ancestry_sha256s=(harness_sha,), candidate_sha256=artifact.sha256,
        official_score=5.0, evaluator_receipt_sha256=_sha(evaluator), private_evidence_sha256=_sha(evidence),
        audit_ledger_sha256="03" * 32, operation_journal_head_sha256="04" * 32,
        builder_model_configuration_sha256="05" * 32, solver_model_configuration_sha256="06" * 32,
        evaluator_contract_sha256=adapter.execution_contract_sha256, moss_revision_sha256="07" * 32,
        tracked_tree_sha256="08" * 32, source_revision_sha256="09" * 32,
        task_data_revision_sha256="0a" * 32, image_digest_sha256="0b" * 32, api_base_host_sha256="0c" * 32, valid=True,
    )
    payload = receipt.to_dict()
    payload_hash = hashlib.sha256(json.dumps(payload, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    receipt_path = tmp_path / f"freeze-{target_id or contract.task_id}.json"
    receipt_path.write_text(json.dumps({"schema_version": 1, "payload": payload, "payload_sha256": payload_hash}, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    return FreezeAuthorization(
        freeze_receipt_path=receipt_path, freeze_receipt_bytes_sha256=_sha(receipt_path), freeze_receipt_sha256=receipt.sha256,
        evaluator_receipt_path=evaluator, private_evidence_path=evidence,
        execution_contract_sha256=adapter.execution_contract_sha256, harness_sha256=harness_sha,
        ancestry_sha256s=(harness_sha,), candidate_sha256=artifact.sha256, benchmark="alebench",
        target_id=target_id or contract.task_id, official_public_score=5.0,
    )


def _observed(contract: ALEBenchContract) -> ObservedALEBenchIdentity:
    return ObservedALEBenchIdentity(
        source_commit=contract.source_commit,
        dataset_revision=contract.dataset_revision,
        task_id=contract.task_id,
        docker_image_digest=contract.docker_image_digest,
        judge_version=contract.judge_version,
        time_limit_seconds=contract.time_limit_seconds,
        memory_limit_bytes=contract.memory_limit_bytes,
        score_direction=contract.score_direction,
        public_evaluator_command=contract.public_evaluator_command,
        private_evaluator_command=contract.private_evaluator_command,
        task_zip_sha256=ALE_ZIP_SHA,
        ale_module_path=(contract.source_root / "src" / "ale_bench" / "__init__.py").resolve().as_posix(),
        direct_url_source=contract.source_root.as_uri(),
    )


class FakeResult:
    def __init__(self, *, judge: str, score: int, phase: str) -> None:
        self.overall_judge_result = judge
        self.overall_absolute_score = score
        self.resource_usage = SimpleNamespace(
            num_call_public_eval=1 if phase == "public" else 0,
            num_call_private_eval=1 if phase == "private" else 0,
        )
        self._payload = {
            "overall_judge_result": judge,
            "overall_absolute_score": score,
            "resource_usage": {
                "num_call_public_eval": self.resource_usage.num_call_public_eval,
                "num_call_private_eval": self.resource_usage.num_call_private_eval,
            },
            "case_results": [
                {
                    "input_str": "PRIVATE_SEED_INPUT",
                    "output_str": "PRIVATE_OUTPUT",
                    "judge_result": judge,
                    "absolute_score": score,
                }
            ],
        }

    def model_dump(self, *, mode: str) -> dict[str, object]:
        assert mode == "json"
        return self._payload


class FakeSession:
    def __init__(self, contract: ALEBenchContract, *, judge: str, score: int) -> None:
        self.problem_id = contract.task_id
        self.problem = SimpleNamespace(
            constraints=SimpleNamespace(
                time_limit=contract.time_limit_seconds,
                memory_limit=contract.memory_limit_bytes,
            )
        )
        self.num_public_cases = 50
        self.public_calls: list[dict[str, object]] = []
        self.private_calls: list[dict[str, object]] = []
        self.judge = judge
        self.score = score

    def public_eval(self, **kwargs: object) -> FakeResult:
        self.public_calls.append(kwargs)
        return FakeResult(judge=self.judge, score=self.score, phase="public")

    def private_eval(self, **kwargs: object) -> tuple[FakeResult, int, int]:
        self.private_calls.append(kwargs)
        return FakeResult(judge=self.judge, score=self.score, phase="private"), 7, 123


@pytest.mark.parametrize("judge", ["COMPILATION_ERROR", "WRONG_ANSWER"])
def test_ale_public_eval_preserves_valid_zero_and_hides_case_data(
    tmp_path: Path, judge: str
) -> None:
    contract = _contract(tmp_path)
    sessions: list[FakeSession] = []
    factory_calls: list[dict[str, object]] = []

    def session_factory(**kwargs: object) -> FakeSession:
        factory_calls.append(kwargs)
        session = FakeSession(contract, judge=judge, score=0)
        sessions.append(session)
        return session

    adapter = ALEBenchOfficialAdapter(
        contract=contract,
        private_evidence_root=tmp_path / "private",
        session_factory=session_factory,
        identity_probe=lambda _: _observed(contract),
    )

    result = adapter.evaluate_public(_artifact(), operation_id=f"public-{judge}")

    assert isinstance(result, EvaluationResult)
    assert result.public.score == 0.0
    feedback = json.loads(result.public.feedback)
    assert set(feedback) == {"status", "reason", "aggregate_score", "validity"}
    assert feedback == {
        "status": judge,
        "reason": "official_public_eval_completed",
        "aggregate_score": 0.0,
        "validity": True,
    }
    assert "PRIVATE" not in result.public.feedback
    assert factory_calls == [
        {
            "problem_id": contract.task_id,
            "lite_version": False,
            "maximum_num_call_public_eval": 1,
            "num_workers": 1,
            "run_visualization_server": False,
        }
    ]
    assert sessions[0].public_calls == [
        {
            "code": _artifact().text,
            "code_language": "cpp23",
            "judge_version": "202301",
            "skip_local_visualization": True,
            "reuse_containers": False,
        }
    ]
    assert sessions[0].private_calls == []
    evidence = Path(result.private["evidence_path"]).read_text(encoding="utf-8")
    assert "PRIVATE_SEED_INPUT" in evidence
    assert "PRIVATE_OUTPUT" in evidence


def test_ale_private_eval_requires_strict_freeze_authorization(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    session = FakeSession(contract, judge="ACCEPTED", score=42)
    adapter = ALEBenchOfficialAdapter(
        contract=contract,
        private_evidence_root=tmp_path / "private",
        session_factory=lambda **_: session,
        identity_probe=lambda _: _observed(contract),
    )
    artifact = _artifact()

    with pytest.raises(TypeError, match="FreezeAuthorization"):
        adapter.evaluate_private(
            artifact,
            operation_id="private-no-auth",
            authorization=[REDACTED]"valid": True},
        )
    assert session.private_calls == []

    wrong_target = _authorization(tmp_path, contract, artifact, target_id="ahc026")
    with pytest.raises(ValueError, match="authorization binding differs"):
        adapter.evaluate_private(
            artifact,
            operation_id="private-wrong-target",
            authorization=[REDACTED],
        )
    assert session.private_calls == []


def test_ale_private_result_is_withheld_and_written_only_to_private_evidence(
    tmp_path: Path,
) -> None:
    contract = _contract(tmp_path)
    session = FakeSession(contract, judge="ACCEPTED", score=42)
    artifact = _artifact()
    authorization = [REDACTED], contract, artifact)
    result = ALEBenchOfficialAdapter(
        contract=contract,
        private_evidence_root=tmp_path / "private",
        session_factory=lambda **_: session,
        identity_probe=lambda _: _observed(contract),
    ).evaluate_private(
        artifact,
        operation_id="private-authorized",
        authorization=[REDACTED],
    )

    assert isinstance(result, EvaluationResult)
    assert result.public.score is None
    feedback = json.loads(result.public.feedback)
    assert set(feedback) == {"status", "reason", "aggregate_score", "validity"}
    assert feedback["aggregate_score"] is None
    assert "42" not in result.public.feedback
    assert "123" not in result.public.feedback
    assert session.public_calls == []
    assert session.private_calls[0]["judge_version"] == "202301"
    evidence = Path(result.private["evidence_path"]).read_text(encoding="utf-8")
    assert '"rank":7' in evidence
    assert '"performance":123' in evidence
    assert '"overall_absolute_score":42' in evidence


def test_ale_identity_mismatch_fails_before_session_creation(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    factory_calls = 0

    def session_factory(**_: object) -> FakeSession:
        nonlocal factory_calls
        factory_calls += 1
        return FakeSession(contract, judge="ACCEPTED", score=1)

    observed = _observed(contract)
    wrong = ObservedALEBenchIdentity(
        **{**observed.__dict__, "judge_version": "202510"}
    )
    adapter = ALEBenchOfficialAdapter(
        contract=contract,
        private_evidence_root=tmp_path / "private",
        session_factory=session_factory,
        identity_probe=lambda _: wrong,
    )

    with pytest.raises(RuntimeError, match="identity differs"):
        adapter.evaluate_public(_artifact(), operation_id="public-wrong-identity")
    assert factory_calls == 0


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_commit", "0" * 40),
        ("dataset_revision", "0" * 40),
        ("task_id", "ahc027"),
        ("docker_image_reference", "ale-bench:cpp23-202510"),
        ("docker_image_digest", "not-a-digest"),
        ("judge_version", "202510"),
        ("time_limit_seconds", 3),
        ("memory_limit_bytes", 2 << 30),
        ("score_direction", "minimize"),
        ("public_evaluator_command", ("Session", "case_eval")),
        ("private_evaluator_command", ("Session", "case_eval")),
    ],
)
def test_ale_contract_fails_closed_on_unpinned_identity(
    tmp_path: Path, field: str, value: object
) -> None:
    values = _contract(tmp_path).__dict__.copy()
    values[field] = value
    with pytest.raises(ValueError):
        ALEBenchContract(**values)


def test_ale_fake_hash_only_authorization_is_rejected(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    artifact = _artifact()
    with pytest.raises((TypeError, ValueError)):
        FreezeAuthorization(freeze_receipt_path=tmp_path / "missing", freeze_receipt_bytes_sha256="a" * 64, freeze_receipt_sha256="a" * 64, evaluator_receipt_path=tmp_path / "missing-e", private_evidence_path=tmp_path / "missing-p", execution_contract_sha256="b" * 64, harness_sha256="c" * 64, ancestry_sha256s=("c" * 64,), candidate_sha256=artifact.sha256, benchmark="alebench", target_id=contract.task_id, official_public_score=5.0)


def test_ale_default_probe_reads_refs_snapshot_and_binds_import(monkeypatch, tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    contract.source_root.mkdir(parents=True)
    python = contract.python_executable
    python.parent.mkdir(parents=True)
    python.write_text("", encoding="utf-8")
    (contract.dataset_root / "refs").mkdir(parents=True)
    (contract.dataset_root / "refs" / "main").write_text(ALE_BENCH_DATASET_REVISION + "\n", encoding="utf-8")
    snapshot = contract.dataset_root / "snapshots" / ALE_BENCH_DATASET_REVISION
    snapshot.mkdir(parents=True)
    (snapshot / f"{contract.task_id}.zip").write_bytes(b"zip")
    monkeypatch.setattr(ale_module, "_sha256_file", lambda _: ALE_ZIP_SHA)
    package_json = json.dumps({"module": (contract.source_root / "src" / "ale_bench" / "__init__.py").as_posix(), "direct_url": contract.source_root.as_uri()})
    monkeypatch.setattr(ale_module, "_run_identity_command", lambda command, **_: ALE_BENCH_SOURCE_COMMIT if command[:2] == ("git", "rev-parse") else "" if command[:2] == ("git", "status") else package_json if "import ale_bench" in " ".join(command) else ALE_DIGEST)
    observed = ale_module._probe_identity(contract)
    assert observed.task_zip_sha256 == ALE_ZIP_SHA
    assert observed.dataset_revision == ALE_BENCH_DATASET_REVISION
    assert observed.ale_module_path.startswith(contract.source_root.as_posix())


def test_ale_contract_preserves_virtualenv_python_symlink(tmp_path: Path) -> None:
    target = tmp_path / "python3"
    target.write_text("", encoding="utf-8")
    entrypoint = tmp_path / "venv" / "bin" / "python"
    entrypoint.parent.mkdir(parents=True)
    try:
        entrypoint.symlink_to(target)
    except OSError as exc:
        pytest.skip(f"symlink creation is unavailable: {exc}")
    contract = _contract(tmp_path)
    values = contract.__dict__.copy()
    values["python_executable"] = entrypoint
    rebuilt = ALEBenchContract(**values)
    assert rebuilt.python_executable == entrypoint.absolute()
    assert rebuilt.python_executable != target.resolve()


def test_ale_session_is_bound_to_frozen_cache(tmp_path: Path) -> None:
    contract = _contract(tmp_path)
    seen = {}
    def factory(**_: object):
        seen["cache"] = os.environ.get("ALE_BENCH_CACHE")
        seen["offline"] = os.environ.get("HF_HUB_OFFLINE")
        return FakeSession(contract, judge="ACCEPTED", score=1)
    ALEBenchOfficialAdapter(contract=contract, private_evidence_root=tmp_path / "private", session_factory=factory, identity_probe=lambda _: _observed(contract)).evaluate_public(_artifact(), operation_id="cache-bound")
    assert Path(seen["cache"]).resolve() == contract.dataset_root.parent
    assert seen["offline"] == "1"


def test_ale_evaluator_uses_contract_python_environment_for_session_import(
    monkeypatch, tmp_path: Path
) -> None:
    """The official package must be importable from the contract's Python env."""

    target_site = tmp_path / "official-site-packages"
    package = target_site / "ale_bench"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text(
        """
from types import SimpleNamespace

class _Result:
    overall_judge_result = "ACCEPTED"
    overall_absolute_score = 7.0
    resource_usage = SimpleNamespace(num_call_public_eval=1, num_call_private_eval=0)

    def model_dump(self, *, mode):
        assert mode == "json"
        return {
            "overall_judge_result": self.overall_judge_result,
            "overall_absolute_score": self.overall_absolute_score,
            "resource_usage": {
                "num_call_public_eval": 1,
                "num_call_private_eval": 0,
            },
        }

class _Session:
    problem_id = "ahc024"
    problem = SimpleNamespace(
        constraints=SimpleNamespace(time_limit=2, memory_limit=1 << 30)
    )

    def public_eval(self, **kwargs):
        return _Result()

def start(**kwargs):
    return _Session()
""",
        encoding="utf-8",
    )

    # The target interpreter's site-packages are supplied by the production
    # helper.  The current interpreter deliberately cannot find this package.
    monkeypatch.setattr(
        ale_module,
        "_target_python_sys_path",
        lambda _: [str(target_site)],
        raising=False,
    )
    monkeypatch.delitem(sys.modules, "ale_bench", raising=False)
    contract = _contract(tmp_path)
    adapter = ALEBenchOfficialAdapter(
        contract=contract,
        private_evidence_root=tmp_path / "private",
        identity_probe=lambda _: _observed(contract),
    )

    result = adapter.evaluate_public(_artifact(), operation_id="target-env-import")

    assert result.public.score == 7.0
    assert json.loads(result.public.feedback)["status"] == "ACCEPTED"
