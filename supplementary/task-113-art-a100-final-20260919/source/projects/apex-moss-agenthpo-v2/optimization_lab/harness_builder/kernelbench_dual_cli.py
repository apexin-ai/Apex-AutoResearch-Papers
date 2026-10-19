from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
from dataclasses import asdict, is_dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from optimization_lab.adapters.ssh_kernelbench import SSHKernelBenchAdapter
from optimization_lab.openai_generator import OpenAIResponsesGenerator
from optimization_lab.task_spec import TaskSpec

from .adapters.kernel_candidate_policy import (
    RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
    RESTRICTED_KERNEL_TASK_IDS,
)
from .dual_config import (
    DualHarnessModelConfig,
    create_dual_harness_generators,
    create_dual_harness_runtime,
)
from .dual_harness import HarnessWorkspace, TaskHarnessRuntime
from .kernelbench_dual_experiment import (
    KernelBenchPublicEvaluator,
    cross_test_frozen_harness,
    evolve_instance,
)

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}")
_SHA256 = re.compile(r"[0-9a-f]{64}")
_MIN_API_BUDGET_USD = 100.0


def _safe_id(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_ID.fullmatch(value) or ".." in value:
        raise ValueError(f"{label} is unsafe")
    return value


def _add_common_arguments(
    parser: argparse.ArgumentParser, *, require_contract_hash: bool
) -> None:
    parser.add_argument("--task-protocol", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, default=Path("results/kernelbench-dual"))
    parser.add_argument(
        "--execution-contract-sha256", required=require_contract_hash
    )
    parser.add_argument("--run-prefix", default="lineage")
    parser.add_argument("--rounds", type=int, default=8)
    parser.add_argument("--ssh-host", default="moss-h200")
    parser.add_argument("--remote-repository", default="/home/ec2-user/KernelBench")
    parser.add_argument("--remote-root", default="/home/ec2-user/moss-kernelbench-dual")
    parser.add_argument("--gpu-index", type=int, default=0)
    parser.add_argument("--expected-gpu-uuid", default="")
    parser.add_argument("--remote-uv", default="/home/ec2-user/.local/bin/uv")
    parser.add_argument("--private-log-root", type=Path)
    parser.add_argument("--api-budget-usd", type=float, default=100.0)
    parser.add_argument("--gpu-budget-seconds", type=float, default=3600.0)
    parser.set_defaults(execute=False)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the frozen KernelBench dual-Harness experiment")
    subparsers = parser.add_subparsers(dest="command", required=True)

    contract = subparsers.add_parser("contract")
    _add_common_arguments(contract, require_contract_hash=False)

    preflight_parser = subparsers.add_parser("preflight")
    _add_common_arguments(preflight_parser, require_contract_hash=True)

    evolve = subparsers.add_parser("evolve")
    _add_common_arguments(evolve, require_contract_hash=True)
    evolve.add_argument("--execute", action="store_true")

    cross = subparsers.add_parser("cross-test")
    _add_common_arguments(cross, require_contract_hash=True)
    cross.add_argument("--harness-sha256", required=True)
    cross.add_argument("--harness-workspace", type=Path)
    cross.add_argument("--cross-test-id", required=True)
    cross.add_argument("--execute", action="store_true")

    return parser


def load_task(path: Path) -> TaskSpec:
    task = TaskSpec.from_json(path.resolve())
    if task.target_gpu != "H200" or task.gpu_arch != "Hopper":
        raise ValueError("KernelBench dual experiment requires the frozen H200/Hopper protocol")
    return task


def _task_artifact_id(task_id: str) -> str:
    if not isinstance(task_id, str) or not task_id:
        raise ValueError("task id is unsafe")
    relative = PurePosixPath(task_id)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("task id is unsafe")
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", task_id).strip("._-")
    slug = (slug or "task")[:96]
    digest = hashlib.sha256(task_id.encode("utf-8")).hexdigest()[:16]
    return _safe_id(f"{slug}-{digest}", "task artifact id")


def instance_root(artifact_root: Path, task: TaskSpec, run_prefix: str) -> Path:
    run_prefix = _safe_id(run_prefix, "run prefix")
    task_id = _task_artifact_id(task.task_id)
    root = artifact_root.resolve()
    result = (root / task_id / run_prefix).resolve()
    if root not in result.parents:
        raise ValueError("instance workspace escapes artifact root")
    return result


def make_openai_client() -> Any:
    api_key = [REDACTED]"LLM_API_KEY", "").strip()
    base_url = os.environ.get("LLM_BASE_URL", "").strip()
    if not api_key or not base_url:
        raise RuntimeError("LLM_API_KEY and LLM_BASE_URL are required")
    from openai import OpenAI

    return OpenAI(api_key=[REDACTED], base_url=base_url)


def experiment_model_config() -> DualHarnessModelConfig:
    return DualHarnessModelConfig(
        builder_model="gpt-5.6-sol",
        solver_model="gpt-5.6-sol",
        builder_transport="openai_responses",
        solver_transport="openai_responses",
        tool_protocol="controller_json",
        reasoning_effort="high",
    )


def make_adapter(args: argparse.Namespace) -> SSHKernelBenchAdapter:
    return SSHKernelBenchAdapter(
        host=args.ssh_host,
        remote_repository=args.remote_repository,
        remote_root=args.remote_root,
        gpu_index=args.gpu_index,
        remote_uv=args.remote_uv,
    )


def canonical_json(payload: object) -> str:
    return json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def execution_contract_manifest(
    args: argparse.Namespace, task: TaskSpec
) -> dict[str, object]:
    manifest: dict[str, object] = {
        "schema_version": 1,
        "task": task.to_dict(),
        "models": {
            "builder": "gpt-5.6-sol",
            "solver": "gpt-5.6-sol",
            "reasoning_effort": "high",
            "transport": "openai_responses",
            "stream": True,
            "max_attempts": 3,
            "builder_max_output_tokens": 16_384,
            "solver_max_output_tokens": 32_768,
            "native_tools": False,
        },
        "evaluator": {
            "kind": "ssh_kernelbench",
            "host": args.ssh_host,
            "remote_repository": args.remote_repository,
            "remote_root": args.remote_root,
            "remote_uv": args.remote_uv,
            "gpu_index": args.gpu_index,
            "gpu_uuid": args.expected_gpu_uuid,
            "candidate_policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
        },
        "budget": {
            "rounds": args.rounds,
            "api_usd": args.api_budget_usd,
            "gpu_seconds": args.gpu_budget_seconds,
        },
    }
    harness_sha256 = getattr(args, "harness_sha256", None)
    cross_test_id = getattr(args, "cross_test_id", None)
    if harness_sha256 is not None or cross_test_id is not None:
        manifest["cross_test"] = {
            "harness_sha256": harness_sha256,
            "cross_test_id": cross_test_id,
        }
    return manifest


def write_execution_contract(path: Path, manifest: object) -> Path:
    encoded = (canonical_json(manifest) + "\n").encode("utf-8")
    path = path.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
    try:
        descriptor = os.open(path, flags, 0o600)
    except FileExistsError:
        if path.read_bytes() != encoded:
            raise ValueError("execution contract differs from durable evidence")
        return path
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return path

def execution_contract_sha256(manifest: object) -> str:
    return hashlib.sha256(canonical_json(manifest).encode("utf-8")).hexdigest()


def load_task_source(adapter: SSHKernelBenchAdapter, task: TaskSpec) -> str:
    relative = PurePosixPath(task.task_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("task path is unsafe")
    path = adapter.remote_repository / relative
    result = adapter._run_remote(["cat", str(path)], timeout=60)
    if result.returncode != 0:
        raise RuntimeError("failed to load pinned task source")
    source = result.stdout
    actual = hashlib.sha256(source.encode("utf-8")).hexdigest()
    if actual != task.task_sha256:
        raise RuntimeError(
            f"task source hash mismatch: actual={actual} expected={task.task_sha256}"
        )
    return source


def remote_gpu_snapshot(
    adapter: SSHKernelBenchAdapter, gpu_index: int
) -> dict[str, object]:
    query = adapter._run_remote(
        [
            "nvidia-smi",
            f"--id={gpu_index}",
            "--query-gpu=uuid,name,memory.total,memory.free,utilization.gpu",
            "--format=csv,noheader,nounits",
        ],
        timeout=30,
    )
    if query.returncode != 0 or not query.stdout.strip():
        raise RuntimeError("failed to query remote GPU")
    rows = [part.strip() for part in query.stdout.strip().splitlines()[0].split(",")]
    if len(rows) != 5:
        raise RuntimeError("remote GPU query returned an invalid record")
    processes_query = adapter._run_remote(
        [
            "nvidia-smi",
            f"--id={gpu_index}",
            "--query-compute-apps=pid,used_memory",
            "--format=csv,noheader,nounits",
        ],
        timeout=30,
    )
    processes: list[dict[str, int]] = []
    if processes_query.returncode == 0:
        for line in processes_query.stdout.splitlines():
            if not line.strip() or "No running" in line:
                continue
            fields = [part.strip() for part in line.split(",")]
            if len(fields) != 2:
                raise RuntimeError("remote GPU process query returned an invalid record")
            processes.append(
                {"pid": int(fields[0]), "used_memory_mib": int(fields[1])}
            )
    return {
        "uuid": rows[0],
        "name": rows[1],
        "memory_total_mib": int(rows[2]),
        "memory_free_mib": int(rows[3]),
        "utilization_percent": int(rows[4]),
        "compute_processes": processes,
    }


def _check(name: str, ready: bool, detail: object) -> dict[str, object]:
    return {
        "name": name,
        "status": "ready" if ready else "blocked",
        "detail": detail,
    }


def preflight(args: argparse.Namespace) -> dict[str, object]:
    task = load_task(args.task_protocol)
    checks: list[dict[str, object]] = []
    credentials_ready = bool(
        os.environ.get("LLM_API_KEY", "").strip()
        and os.environ.get("LLM_BASE_URL", "").strip()
    )
    checks.append(
        _check(
            "api_credentials",
            credentials_ready,
            "LLM_API_KEY and LLM_BASE_URL are set"
            if credentials_ready
            else "LLM_API_KEY and LLM_BASE_URL are required",
        )
    )

    manifest = execution_contract_manifest(args, task)
    actual_contract = execution_contract_sha256(manifest)
    checks.append(
        _check(
            "execution_contract",
            actual_contract == args.execution_contract_sha256,
            {"actual": actual_contract, "expected": args.execution_contract_sha256},
        )
    )
    checks.append(
        _check(
            "candidate_capability",
            task.task_id in RESTRICTED_KERNEL_TASK_IDS,
            {
                "task_id": task.task_id,
                "policy_sha256": RESTRICTED_KERNEL_CANDIDATE_POLICY_SHA256,
            },
        )
    )

    adapter = None
    adapter_error: Exception | None = None
    try:
        adapter = make_adapter(args)
    except Exception as exc:
        adapter_error = exc

    rounds_ready = (
        isinstance(args.rounds, int)
        and not isinstance(args.rounds, bool)
        and args.rounds > 0
    )
    api_budget_ready = (
        isinstance(args.api_budget_usd, (int, float))
        and not isinstance(args.api_budget_usd, bool)
        and math.isfinite(float(args.api_budget_usd))
        and float(args.api_budget_usd) >= _MIN_API_BUDGET_USD
    )
    estimated_gpu_seconds_per_round: float | None = None
    required_gpu_seconds: float | None = None
    if adapter is not None and rounds_ready:
        estimated_gpu_seconds_per_round = float(adapter.estimated_gpu_seconds(task))
        if (
            math.isfinite(estimated_gpu_seconds_per_round)
            and estimated_gpu_seconds_per_round > 0
        ):
            required_gpu_seconds = estimated_gpu_seconds_per_round * args.rounds
    gpu_budget_ready = (
        required_gpu_seconds is not None
        and isinstance(args.gpu_budget_seconds, (int, float))
        and not isinstance(args.gpu_budget_seconds, bool)
        and math.isfinite(float(args.gpu_budget_seconds))
        and float(args.gpu_budget_seconds) >= required_gpu_seconds
    )
    budget_ready = rounds_ready and api_budget_ready and gpu_budget_ready
    checks.append(
        _check(
            "budget_entitlement",
            budget_ready,
            {
                "rounds": args.rounds,
                "api_usd": args.api_budget_usd,
                "required_api_usd": _MIN_API_BUDGET_USD,
                "api_shortfall_usd": max(
                    0.0, _MIN_API_BUDGET_USD - float(args.api_budget_usd)
                )
                if isinstance(args.api_budget_usd, (int, float))
                and not isinstance(args.api_budget_usd, bool)
                and math.isfinite(float(args.api_budget_usd))
                else None,
                "gpu_seconds": args.gpu_budget_seconds,
                "estimated_gpu_seconds_per_round": estimated_gpu_seconds_per_round,
                "required_gpu_seconds": required_gpu_seconds,
                "gpu_shortfall_seconds": max(
                    0.0, required_gpu_seconds - float(args.gpu_budget_seconds)
                )
                if required_gpu_seconds is not None
                and isinstance(args.gpu_budget_seconds, (int, float))
                and not isinstance(args.gpu_budget_seconds, bool)
                and math.isfinite(float(args.gpu_budget_seconds))
                else None,
            },
        )
    )

    try:
        if adapter is None:
            assert adapter_error is not None
            raise adapter_error
        for item in adapter.preflight(task):
            checks.append(
                _check(
                    str(item.name),
                    str(item.status) == "ready",
                    str(item.detail),
                )
            )
        snapshot = remote_gpu_snapshot(adapter, args.gpu_index)
        identity_ready = (
            snapshot.get("uuid") == args.expected_gpu_uuid
            and task.target_gpu in str(snapshot.get("name", ""))
        )
        checks.append(
            _check(
                "gpu_identity",
                identity_ready,
                {
                    "actual_uuid": snapshot.get("uuid"),
                    "expected_uuid": args.expected_gpu_uuid,
                    "name": snapshot.get("name"),
                },
            )
        )
        processes = snapshot.get("compute_processes")
        gpu_idle = (
            isinstance(processes, list)
            and not processes
            and snapshot.get("utilization_percent") == 0
        )
        checks.append(_check("gpu_idle", gpu_idle, snapshot))
    except Exception as exc:
        checks.append(_check("remote_environment", False, str(exc)))

    return {
        "status": (
            "ready"
            if checks and all(item["status"] == "ready" for item in checks)
            else "blocked"
        ),
        "task_id": task.task_id,
        "execution_contract_sha256": actual_contract,
        "checks": checks,
    }


def _require_ready_preflight(args: argparse.Namespace) -> dict[str, object]:
    report = preflight(args)
    if report.get("status") != "ready":
        blockers = [
            str(check.get("name", "unknown"))
            for check in report.get("checks", [])
            if isinstance(check, dict) and check.get("status") != "ready"
        ]
        raise RuntimeError(
            "KernelBench dual experiment preflight blocked: "
            + ", ".join(blockers or ["unknown"])
        )
    return report


def run_evolve(args: argparse.Namespace) -> object:
    if not getattr(args, "execute", False):
        raise RuntimeError("evolve requires explicit --execute")
    _require_ready_preflight(args)
    task = load_task(args.task_protocol)
    root = instance_root(args.artifact_root, task, args.run_prefix)
    manifest = execution_contract_manifest(args, task)
    actual_contract = execution_contract_sha256(manifest)
    if actual_contract != args.execution_contract_sha256:
        raise RuntimeError("execution contract changed after preflight")
    write_execution_contract(root / "execution_contract.json", manifest)

    adapter = make_adapter(args)
    task_source = load_task_source(adapter, task)
    client = make_openai_client()
    workspace = HarnessWorkspace(root / "harness_workspace")
    runtime = create_dual_harness_runtime(
        experiment_model_config(),
        workspace=workspace,
        operation_root=root / "private_model_operations",
        openai_client=client,
    )
    private_log_root = (
        args.private_log_root.resolve()
        if args.private_log_root is not None
        else root / "private_evaluator"
    )
    evaluator = KernelBenchPublicEvaluator(
        task=task,
        adapter=adapter,
        archive_root=root / "solution_archive",
        cell_id=_safe_id(args.run_prefix, "run prefix"),
        private_log_root=private_log_root,
        gpu_uuid=args.expected_gpu_uuid,
    )
    return evolve_instance(
        runtime=runtime,
        workspace=workspace,
        task=task,
        task_source=task_source,
        evaluator=evaluator,
        rounds=args.rounds,
        execution_contract_sha256=args.execution_contract_sha256,
        run_prefix=args.run_prefix,
    )


def run_cross_test(args: argparse.Namespace) -> object:
    if not getattr(args, "execute", False):
        raise RuntimeError("cross-test requires explicit --execute")
    if _SHA256.fullmatch(args.harness_sha256) is None:
        raise ValueError("Harness hash is invalid")
    _require_ready_preflight(args)
    task = load_task(args.task_protocol)
    lineage_root = instance_root(args.artifact_root, task, args.run_prefix)
    cross_test_id = _safe_id(args.cross_test_id, "cross-test id")
    cross_root = lineage_root / "cross_tests" / cross_test_id
    manifest = execution_contract_manifest(args, task)
    actual_contract = execution_contract_sha256(manifest)
    if actual_contract != args.execution_contract_sha256:
        raise RuntimeError("execution contract changed after preflight")
    write_execution_contract(cross_root / "execution_contract.json", manifest)

    adapter = make_adapter(args)
    task_source = load_task_source(adapter, task)
    client = make_openai_client()
    solver_generator = OpenAIResponsesGenerator(
        client=client,
        max_output_tokens=32_768,
        reasoning_effort="high",
        max_attempts=3,
        stream=True,
        audit_root=cross_root / "private_model_operations" / "solver",
    )
    task_runtime = TaskHarnessRuntime(generator=solver_generator)
    workspace_value = getattr(args, "harness_workspace", None)
    workspace = HarnessWorkspace(
        workspace_value
        if workspace_value is not None
        else lineage_root / "harness_workspace"
    )
    private_log_root = (
        args.private_log_root.resolve()
        if args.private_log_root is not None
        else cross_root / "private_evaluator"
    )
    evaluator = KernelBenchPublicEvaluator(
        task=task,
        adapter=adapter,
        archive_root=cross_root / "solution_archive",
        cell_id=cross_test_id,
        private_log_root=private_log_root,
        gpu_uuid=args.expected_gpu_uuid,
    )
    return cross_test_frozen_harness(
        workspace=workspace,
        task_runtime=task_runtime,
        task=task,
        task_source=task_source,
        solver_model="gpt-5.6-sol",
        harness_sha256=args.harness_sha256,
        evaluator=evaluator,
        cross_test_id=cross_test_id,
        receipt_root=cross_root / "receipts",
    )


def _jsonable(value: object) -> object:
    if is_dataclass(value) and not isinstance(value, type):
        return _jsonable(asdict(value))
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    return value


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "contract":
        task = load_task(args.task_protocol)
        manifest = execution_contract_manifest(args, task)
        payload = {
            "manifest": manifest,
            "execution_contract_sha256": execution_contract_sha256(manifest),
        }
        print(canonical_json(payload))
        return 0

    if _SHA256.fullmatch(args.execution_contract_sha256) is None:
        raise ValueError("execution contract hash is invalid")
    if args.command == "preflight":
        result = preflight(args)
    elif args.command == "evolve":
        result = run_evolve(args)
    else:
        result = run_cross_test(args)
    print(canonical_json(_jsonable(result)))
    return 0


__all__ = [
    "TaskSpec",
    "TaskHarnessRuntime",
    "build_parser",
    "canonical_json",
    "create_dual_harness_runtime",
    "experiment_model_config",
    "execution_contract_manifest",
    "execution_contract_sha256",
    "instance_root",
    "load_task",
    "load_task_source",
    "make_adapter",
    "make_openai_client",
    "preflight",
    "remote_gpu_snapshot",
    "run_cross_test",
    "run_evolve",
    "write_execution_contract",
]
