from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from types import SimpleNamespace

import pytest

from optimization_lab.harness_builder import kernelbench_dual_cli as cli


HASH = "a" * 64
COMMIT = "b" * 40


def write_protocol(
    path: Path,
    task_id: str = "level1/92_cumsum_exclusive.py",
    *,
    task_path: str | None = None,
) -> None:
    path.write_text(
        json.dumps(
            {
                "backend": "triton",
                "correctness_trials": 5,
                "display_name": "Cumsum Exclusive",
                "gpu_arch": "Hopper",
                "level": 1,
                "performance_trials": 100,
                "precision": "fp32",
                "problem_id": 92,
                "repository_commit": COMMIT,
                "target_gpu": "H200",
                "task_id": task_id,
                "task_path": task_path or f"KernelBench/{task_id}",
                "task_sha256": HASH,
                "timeout_seconds": 300,
            }
        ),
        encoding="utf-8",
    )


def test_parser_requires_pinned_execution_contract_hash() -> None:
    parser = cli.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["evolve", "--task-protocol", "task.json"])


def test_instance_workspace_is_separate_and_safe(tmp_path: Path) -> None:
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    args = cli.build_parser().parse_args(
        [
            "evolve",
            "--task-protocol",
            str(protocol),
            "--artifact-root",
            str(tmp_path / "artifacts"),
            "--execution-contract-sha256",
            HASH,
            "--run-prefix",
            "lineage-a",
        ]
    )
    first = cli.instance_root(args.artifact_root, cli.load_task(args.task_protocol), args.run_prefix)
    args.run_prefix = "lineage-b"
    second = cli.instance_root(args.artifact_root, cli.load_task(args.task_protocol), args.run_prefix)
    assert first != second
    assert first.parent == second.parent
    assert ".." not in first.parts


def test_instance_workspace_maps_official_task_id_without_changing_identity(
    tmp_path: Path,
) -> None:
    protocol = tmp_path / "task.json"
    task_id = "level2/56_Matmul_Sigmoid_Sum.py"
    write_protocol(protocol, task_id)
    task = cli.load_task(protocol)

    result = cli.instance_root(tmp_path / "artifacts", task, "lineage-a")

    expected_digest = hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:16]
    assert result.parent.name.endswith(expected_digest)
    assert "/" not in result.parent.name
    assert "\\" not in result.parent.name
    assert (tmp_path / "artifacts").resolve() in result.parents
    assert cli.execution_contract_manifest(_formal_args(tmp_path), task)["task"]["task_id"] == task_id


def test_instance_workspace_mapping_is_collision_resistant(tmp_path: Path) -> None:
    common = {
        "display_name": "task",
        "level": 1,
        "problem_id": 1,
        "task_path": "KernelBench/level1/task.py",
        "task_sha256": HASH,
        "repository_commit": COMMIT,
        "target_gpu": "H200",
        "gpu_arch": "Hopper",
    }
    slash = cli.TaskSpec(task_id="level1/a/b.py", **common)
    punctuation = cli.TaskSpec(task_id="level1-a-b.py", **common)

    first = cli.instance_root(tmp_path / "artifacts", slash, "lineage")
    second = cli.instance_root(tmp_path / "artifacts", punctuation, "lineage")

    assert first != second
    assert first.parent != second.parent


@pytest.mark.parametrize(
    ("protocol_name", "expected_task_id"),
    (
        ("kernelbench_h200_cumsum_exclusive.json", "level1/92_cumsum_exclusive.py"),
        ("kernelbench_h200_matmul_sigmoid_sum.json", "level2/56_Matmul_Sigmoid_Sum.py"),
    ),
)
def test_production_protocols_use_official_frozen_task_ids(
    protocol_name: str, expected_task_id: str
) -> None:
    protocol = (
        Path(__file__).resolve().parents[1] / "optimization_lab" / "protocols" / protocol_name
    )

    task = cli.load_task(protocol)

    assert task.task_id == expected_task_id
    assert task.task_path == f"KernelBench/{expected_task_id}"


def test_openai_client_uses_environment_only(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[dict[str, str]] = []

    class OpenAI:
        def __init__(self, **kwargs: str) -> None:
            calls.append(kwargs)

    monkeypatch.setitem(__import__("sys").modules, "openai", type("M", (), {"OpenAI": OpenAI}))
    monkeypatch.setenv("LLM_API_KEY", "secret")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")
    client = cli.make_openai_client()
    assert isinstance(client, OpenAI)
    assert calls == [{"api_key": "[REDACTED]", "base_url": "https://llm.example/v1"}]


def test_exact_experiment_config_uses_responses_and_high() -> None:
    config = cli.experiment_model_config()
    assert config.builder_model == config.solver_model == "gpt-5.6-sol"
    assert config.builder_transport == config.solver_transport == "openai_responses"
    assert config.reasoning_effort == "high"


def test_cross_test_dispatch_does_not_construct_builder(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    class FakeRuntime:
        def __init__(self, **kwargs: object) -> None:
            calls.append("task-runtime")

    monkeypatch.setattr(cli, "TaskHarnessRuntime", FakeRuntime)
    monkeypatch.setattr(cli, "create_dual_harness_runtime", lambda *a, **k: (_ for _ in ()).throw(AssertionError("builder")))
    monkeypatch.setattr(cli, "make_openai_client", lambda: object())
    monkeypatch.setattr(cli, "make_adapter", lambda args: object())
    monkeypatch.setattr(cli, "load_task_source", lambda adapter, task: "public task")
    monkeypatch.setattr(cli, "KernelBenchPublicEvaluator", lambda **kwargs: lambda candidate, candidate_id: None)
    monkeypatch.setattr(
        cli,
        "cross_test_frozen_harness",
        lambda **kwargs: type("Result", (), {"cross_test_id": "x", "task_id": "t", "harness_sha256": HASH, "candidate": "c", "score": 1.0, "feedback": "ok", "receipt_path": Path("receipt")})(),
    )
    protocol = Path("tests") / "fixtures" / "missing-protocol.json"
    # The test only verifies the construction branch; dispatch is exercised with
    # a direct namespace so no network or filesystem protocol is needed.
    args = type(
        "Args",
        (),
        {
            "artifact_root": Path("artifacts"),
            "task_protocol": protocol,
            "run_prefix": "x",
            "rounds": 1,
            "execution_contract_sha256": HASH,
            "harness_sha256": HASH,
            "cross_test_id": "x",
            "private_log_root": None,
            "ssh_host": "host",
            "remote_repository": "/repo",
            "remote_root": "/root",
            "gpu_index": 0,
            "remote_uv": "/uv",
        },
    )
    task = cli.TaskSpec(
        task_id="t",
        display_name="t",
        level=1,
        problem_id=1,
        task_path="KernelBench/t.py",
        task_sha256=HASH,
        repository_commit=COMMIT,
        target_gpu="H200",
        gpu_arch="Hopper",
    )
    monkeypatch.setattr(cli, "load_task", lambda _: task)
    monkeypatch.setattr(cli, "run_cross_test", lambda parsed: calls.append("cross"))
    cli.run_cross_test(args)
    assert calls == ["cross"]


def _formal_args(tmp_path: Path) -> SimpleNamespace:
    return SimpleNamespace(
        artifact_root=tmp_path / "artifacts",
        task_protocol=tmp_path / "task.json",
        run_prefix="lineage-a",
        rounds=8,
        execution_contract_sha256=HASH,
        harness_sha256=HASH,
        cross_test_id="cross-a",
        private_log_root=None,
        ssh_host="moss-h200",
        remote_repository="/srv/KernelBench",
        remote_root="/srv/moss-kernelbench-dual",
        gpu_index=2,
        remote_uv="/srv/uv/bin/uv",
        expected_gpu_uuid="GPU-expected",
        api_budget_usd=100.0,
        gpu_budget_seconds=3600.0,
        execute=False,
    )


def test_contract_manifest_binds_frozen_runtime_settings(tmp_path: Path) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)

    manifest = cli.execution_contract_manifest(args, task)

    assert manifest["models"] == {
        "builder": "gpt-5.6-sol",
        "solver": "gpt-5.6-sol",
        "reasoning_effort": "high",
        "transport": "openai_responses",
        "stream": True,
        "max_attempts": 3,
        "builder_max_output_tokens": 16_384,
        "solver_max_output_tokens": 32_768,
        "native_tools": False,
    }
    assert manifest["task"] == task.to_dict()
    assert manifest["evaluator"]["gpu_uuid"] == "GPU-expected"
    assert manifest["evaluator"]["candidate_policy_sha256"] == (
        cli.RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
    )
    assert manifest["budget"] == {
        "rounds": 8,
        "api_usd": 100.0,
        "gpu_seconds": 3600.0,
    }
    digest = cli.execution_contract_sha256(manifest)
    assert len(digest) == 64
    assert digest == hashlib.sha256(cli.canonical_json(manifest).encode()).hexdigest()


def test_load_task_source_verifies_pinned_hash(tmp_path: Path) -> None:
    source = "import torch\nclass Model: pass\n"
    task = cli.TaskSpec(
        task_id="kernelbench_test",
        display_name="test",
        level=1,
        problem_id=1,
        task_path="KernelBench/level1/1_test.py",
        task_sha256=hashlib.sha256(source.encode()).hexdigest(),
        repository_commit=COMMIT,
        target_gpu="H200",
        gpu_arch="Hopper",
    )

    class Adapter:
        remote_repository = PurePosixPath("/srv/KernelBench")

        def _run_remote(self, command, *, timeout):
            assert command == ["cat", "/srv/KernelBench/KernelBench/level1/1_test.py"]
            assert timeout == 60
            return SimpleNamespace(returncode=0, stdout=source)

    assert cli.load_task_source(Adapter(), task) == source

    bad = task.__class__(**{**task.to_dict(), "task_sha256": "0" * 64})
    with pytest.raises(RuntimeError, match="hash"):
        cli.load_task_source(Adapter(), bad)


def test_preflight_blocks_busy_gpu_and_reports_all_gates(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    monkeypatch.setenv("LLM_API_KEY", "set")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")
    monkeypatch.setattr(
        cli,
        "make_adapter",
        lambda parsed: SimpleNamespace(
            estimated_gpu_seconds=lambda frozen_task: 420.0,
            preflight=lambda frozen_task: [
                SimpleNamespace(name="repository_commit", status="ready", detail="ok")
            ],
        ),
    )
    monkeypatch.setattr(
        cli,
        "remote_gpu_snapshot",
        lambda adapter, gpu_index: {
            "uuid": "GPU-expected",
            "name": "NVIDIA H200",
            "memory_total_mib": 143771,
            "memory_free_mib": 59000,
            "utilization_percent": 100,
            "compute_processes": [{"pid": 123, "used_memory_mib": 84000}],
        },
    )

    report = cli.preflight(args)

    assert report["status"] == "blocked"
    by_name = {check["name"]: check for check in report["checks"]}
    assert by_name["api_credentials"]["status"] == "ready"
    assert by_name["execution_contract"]["status"] == "ready"
    assert by_name["budget_entitlement"]["status"] == "ready"
    assert by_name["gpu_identity"]["status"] == "ready"
    assert by_name["gpu_idle"]["status"] == "blocked"


def test_preflight_blocks_task_without_frozen_candidate_capability(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(
        protocol,
        "kernelbench_cumsum_exclusive",
        task_path="KernelBench/level1/92_cumsum_exclusive.py",
    )
    task = cli.load_task(protocol)
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    monkeypatch.setenv("LLM_API_KEY", "set")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")
    adapter = SimpleNamespace(
        estimated_gpu_seconds=lambda frozen_task: 420.0,
        preflight=lambda frozen_task: [
            SimpleNamespace(name="repository_commit", status="ready", detail="ok")
        ],
    )
    monkeypatch.setattr(cli, "make_adapter", lambda parsed: adapter)
    monkeypatch.setattr(
        cli,
        "remote_gpu_snapshot",
        lambda actual, gpu_index: {
            "uuid": "GPU-expected",
            "name": "NVIDIA H200",
            "memory_total_mib": 143771,
            "memory_free_mib": 143158,
            "utilization_percent": 0,
            "compute_processes": [],
        },
    )

    report = cli.preflight(args)

    capability = {check["name"]: check for check in report["checks"]}[
        "candidate_capability"
    ]
    assert report["status"] == "blocked"
    assert capability["status"] == "blocked"
    assert capability["detail"]["task_id"] == "kernelbench_cumsum_exclusive"
    assert capability["detail"]["policy_sha256"] == (
        cli.RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256
    )


def test_preflight_requires_frozen_api_and_estimated_gpu_budget(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.api_budget_usd = 99.99
    args.gpu_budget_seconds = 3359.0
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    monkeypatch.setenv("LLM_API_KEY", "set")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")

    class Adapter:
        def estimated_gpu_seconds(self, frozen_task):
            assert frozen_task == task
            return 420.0

        def preflight(self, frozen_task):
            return [SimpleNamespace(name="repository_commit", status="ready", detail="ok")]

    monkeypatch.setattr(cli, "make_adapter", lambda parsed: Adapter())
    monkeypatch.setattr(
        cli,
        "remote_gpu_snapshot",
        lambda adapter, gpu_index: {
            "uuid": "GPU-expected",
            "name": "NVIDIA H200",
            "memory_total_mib": 143771,
            "memory_free_mib": 143158,
            "utilization_percent": 0,
            "compute_processes": [],
        },
    )

    report = cli.preflight(args)

    assert report["status"] == "blocked"
    budget = {check["name"]: check for check in report["checks"]}["budget_entitlement"]
    assert budget["status"] == "blocked"
    assert budget["detail"]["required_api_usd"] == 100.0
    assert budget["detail"]["required_gpu_seconds"] == 3360.0
    assert budget["detail"]["api_shortfall_usd"] == pytest.approx(0.01)
    assert budget["detail"]["gpu_shortfall_seconds"] == 1.0


def test_preflight_accepts_budget_at_frozen_minimum(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.api_budget_usd = 100.0
    args.gpu_budget_seconds = 3360.0
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    monkeypatch.setenv("LLM_API_KEY", "set")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")

    adapter = SimpleNamespace(
        estimated_gpu_seconds=lambda frozen_task: 420.0,
        preflight=lambda frozen_task: [
            SimpleNamespace(name="repository_commit", status="ready", detail="ok")
        ],
    )
    monkeypatch.setattr(cli, "make_adapter", lambda parsed: adapter)
    monkeypatch.setattr(
        cli,
        "remote_gpu_snapshot",
        lambda actual, gpu_index: {
            "uuid": "GPU-expected",
            "name": "NVIDIA H200",
            "memory_total_mib": 143771,
            "memory_free_mib": 143158,
            "utilization_percent": 0,
            "compute_processes": [],
        },
    )

    report = cli.preflight(args)

    assert report["status"] == "ready"
    budget = {check["name"]: check for check in report["checks"]}["budget_entitlement"]
    assert budget["status"] == "ready"


def test_evolve_requires_execute_before_constructing_clients(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    monkeypatch.setattr(
        cli,
        "make_openai_client",
        lambda: (_ for _ in ()).throw(AssertionError("client must not be created")),
    )
    with pytest.raises(RuntimeError, match="--execute"):
        cli.run_evolve(args)


def test_parser_exposes_nonexecuting_contract_and_preflight_commands() -> None:
    parser = cli.build_parser()
    common = [
        "--task-protocol",
        "task.json",
        "--expected-gpu-uuid",
        "GPU-fixed",
    ]
    contract = parser.parse_args(["contract", *common])
    assert contract.command == "contract"
    assert contract.execute is False
    assert contract.api_budget_usd == 100.0
    assert contract.gpu_budget_seconds == 3600.0

    preflight = parser.parse_args(
        ["preflight", *common, "--execution-contract-sha256", HASH]
    )
    assert preflight.command == "preflight"
    assert preflight.execute is False


def test_evolve_parser_requires_explicit_execute_to_arm_writes() -> None:
    parser = cli.build_parser()
    args = parser.parse_args(
        [
            "evolve",
            "--task-protocol",
            "task.json",
            "--expected-gpu-uuid",
            "GPU-fixed",
            "--execution-contract-sha256",
            HASH,
            "--execute",
        ]
    )
    assert args.execute is True


def test_remote_gpu_snapshot_parses_identity_and_processes() -> None:
    calls: list[list[str]] = []

    class Adapter:
        def _run_remote(self, command, *, timeout):
            calls.append(command)
            assert timeout == 30
            if "--query-gpu=uuid,name,memory.total,memory.free,utilization.gpu" in command:
                return SimpleNamespace(
                    returncode=0,
                    stdout="GPU-fixed, NVIDIA H200, 143771, 59000, 100\n",
                )
            return SimpleNamespace(returncode=0, stdout="123, 84000\n")

    snapshot = cli.remote_gpu_snapshot(Adapter(), 2)
    assert snapshot == {
        "uuid": "GPU-fixed",
        "name": "NVIDIA H200",
        "memory_total_mib": 143771,
        "memory_free_mib": 59000,
        "utilization_percent": 100,
        "compute_processes": [{"pid": 123, "used_memory_mib": 84000}],
    }
    assert all("--id=2" in command for command in calls)


def test_preflight_fails_closed_when_remote_probe_raises(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    monkeypatch.setenv("LLM_API_KEY", "set")
    monkeypatch.setenv("LLM_BASE_URL", "https://llm.example/v1")
    monkeypatch.setattr(
        cli,
        "make_adapter",
        lambda parsed: (_ for _ in ()).throw(RuntimeError("ssh unavailable")),
    )

    report = cli.preflight(args)

    assert report["status"] == "blocked"
    assert any(
        check["name"] == "remote_environment"
        and check["status"] == "blocked"
        and "ssh unavailable" in check["detail"]
        for check in report["checks"]
    )


def test_evolve_blocks_on_preflight_before_constructing_client(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    args.execute = True
    monkeypatch.setattr(
        cli,
        "preflight",
        lambda parsed: {
            "status": "blocked",
            "checks": [
                {"name": "gpu_idle", "status": "blocked", "detail": "busy"}
            ],
        },
    )
    monkeypatch.setattr(
        cli,
        "make_openai_client",
        lambda: (_ for _ in ()).throw(AssertionError("client must not be created")),
    )

    with pytest.raises(RuntimeError, match="gpu_idle"):
        cli.run_evolve(args)


def test_cross_test_requires_execute_before_constructing_client(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    monkeypatch.setattr(
        cli,
        "make_openai_client",
        lambda: (_ for _ in ()).throw(AssertionError("client must not be created")),
    )
    with pytest.raises(RuntimeError, match="--execute"):
        cli.run_cross_test(args)


def test_execution_contract_is_write_once_and_content_verified(tmp_path: Path) -> None:
    path = tmp_path / "execution_contract.json"
    manifest = {"schema_version": 1, "value": "fixed"}
    cli.write_execution_contract(path, manifest)
    cli.write_execution_contract(path, manifest)
    assert json.loads(path.read_text(encoding="utf-8")) == manifest
    with pytest.raises(ValueError, match="execution contract"):
        cli.write_execution_contract(path, {"schema_version": 1, "value": "changed"})


def test_run_evolve_wires_production_runtime_only_after_ready_preflight(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    args.execute = True
    adapter = object()
    client = object()
    runtime = object()
    captured: dict[str, object] = {}

    monkeypatch.setattr(cli, "preflight", lambda parsed: {"status": "ready", "checks": []})
    monkeypatch.setattr(cli, "make_adapter", lambda parsed: adapter)
    monkeypatch.setattr(cli, "load_task_source", lambda actual, frozen: "public source")
    monkeypatch.setattr(cli, "make_openai_client", lambda: client)

    def fake_create(config, *, workspace, operation_root, openai_client):
        captured["config"] = config
        captured["workspace"] = workspace
        captured["operation_root"] = operation_root
        captured["client"] = openai_client
        return runtime

    monkeypatch.setattr(cli, "create_dual_harness_runtime", fake_create)
    evaluator = object()

    def fake_evaluator(**kwargs):
        captured["evaluator_kwargs"] = kwargs
        return evaluator

    monkeypatch.setattr(cli, "KernelBenchPublicEvaluator", fake_evaluator)

    expected = ("round-result",)

    def fake_evolve(**kwargs):
        captured["evolve"] = kwargs
        return expected

    monkeypatch.setattr(cli, "evolve_instance", fake_evolve)

    result = cli.run_evolve(args)

    root = cli.instance_root(args.artifact_root, task, args.run_prefix)
    assert result == expected
    assert captured["client"] is client
    assert captured["evolve"]["runtime"] is runtime
    assert captured["evolve"]["task_source"] == "public source"
    assert captured["evolve"]["execution_contract_sha256"] == args.execution_contract_sha256
    assert captured["evaluator_kwargs"]["gpu_uuid"] == "GPU-expected"
    assert (root / "execution_contract.json").is_file()


def test_run_cross_test_builds_solver_only_and_uses_explicit_harness_sha(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    args = _formal_args(tmp_path)
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    task = cli.load_task(protocol)
    args.execution_contract_sha256 = cli.execution_contract_sha256(
        cli.execution_contract_manifest(args, task)
    )
    args.execute = True
    adapter = object()
    client = object()
    solver_generator = object()
    evaluator = object()
    captured: dict[str, object] = {}

    monkeypatch.setattr(cli, "preflight", lambda parsed: {"status": "ready", "checks": []})
    monkeypatch.setattr(cli, "make_adapter", lambda parsed: adapter)
    monkeypatch.setattr(cli, "load_task_source", lambda actual, frozen: "public source")
    monkeypatch.setattr(cli, "make_openai_client", lambda: client)
    monkeypatch.setattr(
        cli,
        "create_dual_harness_runtime",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("Builder runtime forbidden")),
    )

    def fake_generator(**kwargs):
        captured["generator_kwargs"] = kwargs
        return solver_generator

    class FakeTaskRuntime:
        def __init__(self, *, generator):
            assert generator is solver_generator

    monkeypatch.setattr(cli, "OpenAIResponsesGenerator", fake_generator)
    monkeypatch.setattr(cli, "TaskHarnessRuntime", FakeTaskRuntime)
    def fake_cross_evaluator(**kwargs):
        captured["evaluator_kwargs"] = kwargs
        return evaluator

    monkeypatch.setattr(cli, "KernelBenchPublicEvaluator", fake_cross_evaluator)
    expected = object()

    def fake_cross(**kwargs):
        captured["cross"] = kwargs
        return expected

    monkeypatch.setattr(cli, "cross_test_frozen_harness", fake_cross)

    result = cli.run_cross_test(args)

    assert result is expected
    assert captured["generator_kwargs"] == {
        "client": client,
        "max_output_tokens": 32_768,
        "reasoning_effort": "high",
        "max_attempts": 3,
        "stream": True,
        "audit_root": (
            cli.instance_root(args.artifact_root, task, args.run_prefix)
            / "cross_tests"
            / args.cross_test_id
            / "private_model_operations"
            / "solver"
        ),
    }
    assert captured["evaluator_kwargs"]["gpu_uuid"] == "GPU-expected"
    assert captured["cross"]["harness_sha256"] == HASH
    assert captured["cross"]["task_source"] == "public source"


def test_main_contract_prints_canonical_manifest_and_hash(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    assert cli.main(
        [
            "contract",
            "--task-protocol",
            str(protocol),
            "--expected-gpu-uuid",
            "GPU-fixed",
        ]
    ) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["execution_contract_sha256"] == cli.execution_contract_sha256(
        payload["manifest"]
    )
    assert payload["manifest"]["models"]["solver_max_output_tokens"] == 32_768


def test_main_preflight_dispatches_without_constructing_models(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    protocol = tmp_path / "task.json"
    write_protocol(protocol)
    expected = {"status": "blocked", "checks": []}
    monkeypatch.setattr(cli, "preflight", lambda args: expected)
    monkeypatch.setattr(
        cli,
        "make_openai_client",
        lambda: (_ for _ in ()).throw(AssertionError("model client forbidden")),
    )
    assert cli.main(
        [
            "preflight",
            "--task-protocol",
            str(protocol),
            "--execution-contract-sha256",
            HASH,
        ]
    ) == 0
    assert json.loads(capsys.readouterr().out) == expected
