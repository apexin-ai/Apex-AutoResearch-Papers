#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import subprocess
from pathlib import Path

from optimization_lab.adapters.ssh_kernelbench import SSHKernelBenchAdapter
from optimization_lab.adapters.ssh_profiler import SSHTierAProfiler
from optimization_lab.codex_generator import CodexExecGenerator
from optimization_lab.p2b_dashboard import P2bDashboard
from optimization_lab.p2b_plan import P2bPlan
from optimization_lab.p2b_runner import P2bCampaignRunner
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOLS = PROJECT_ROOT / "optimization_lab/protocols"
TASK_CARDS = PROJECT_ROOT / "optimization_lab/task_cards"


def _task(task_id: str) -> TaskSpec:
    return TaskSpec.from_json(PROTOCOLS / f"{task_id}.json")


def _remote_reference(host: str, repository: str, task: TaskSpec) -> str:
    path = f"{repository.rstrip('/')}/{task.task_path}"
    result = subprocess.run(
        ["ssh", "-o", "BatchMode=yes", host, "cat", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode(errors="replace")[-1000:])
    if hashlib.sha256(result.stdout).hexdigest() != task.task_sha256:
        raise RuntimeError(f"remote reference hash changed for {task.task_id}")
    return result.stdout.decode("utf-8")


def _require_preflight(
    adapter: SSHKernelBenchAdapter,
    tasks: dict[str, TaskSpec],
) -> dict[str, list[dict[str, str]]]:
    results = {
        task_id: [
            {"name": check.name, "status": check.status, "detail": check.detail}
            for check in adapter.preflight(task)
        ]
        for task_id, task in tasks.items()
    }
    blocked = [
        f"{task_id}:{check['name']}"
        for task_id, checks in results.items()
        for check in checks
        if check["status"] != "ready"
    ]
    if blocked:
        raise RuntimeError(f"P2b scorer preflight blocked: {', '.join(blocked)}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run only the frozen KernelBench P2b Harness search"
    )
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--ssh-host", default="a100jump")
    parser.add_argument(
        "--remote-repository",
        default="/data3/chenzhuofan/moss-kernelbench-pilot/KernelBench",
    )
    parser.add_argument(
        "--remote-root", default="/data3/chenzhuofan/moss-kernelbench-pilot"
    )
    parser.add_argument("--gpu-index", type=int, default=4)
    parser.add_argument(
        "--remote-uv",
        default="/data3/chenzhuofan/moss-kernelbench-pilot/uv-pkg/bin/uv",
    )
    args = parser.parse_args()

    artifact_root = args.artifact_root.resolve()
    plan = P2bPlan.read(artifact_root / "p2b_plan.json")
    registry = ExperimentRegistry(artifact_root)
    dashboard = P2bDashboard(artifact_root / "dashboard.html")
    lock_path = artifact_root / ".p2b-runner.lock"
    with lock_path.open("a+", encoding="utf-8") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("another P2b runner already holds the artifact lock") from exc

        tasks = {task_id: _task(task_id) for task_id in {lane.task_id for lane in plan.lanes}}
        task_cards = {
            task_id: (TASK_CARDS / f"{task_id}.md").read_text(encoding="utf-8")
            for task_id in tasks
        }
        references = {
            task_id: _remote_reference(args.ssh_host, args.remote_repository, task)
            for task_id, task in tasks.items()
        }
        adapter = SSHKernelBenchAdapter(
            host=args.ssh_host,
            remote_repository=args.remote_repository,
            remote_root=args.remote_root,
            gpu_index=args.gpu_index,
            remote_uv=args.remote_uv,
        )
        profiler = SSHTierAProfiler(
            host=args.ssh_host,
            remote_repository=args.remote_repository,
            remote_root=args.remote_root,
            gpu_index=args.gpu_index,
            remote_uv=args.remote_uv,
        )
        try:
            preflight = _require_preflight(adapter, tasks)
            registry.append(
                "p2b_scorer_preflight",
                {
                    "status": "ready",
                    "tasks": preflight,
                    "profiler": profiler.capabilities().to_dict(),
                },
                event_id="p2b-scorer-preflight:ready",
            )
            candidate_generator = CodexExecGenerator(
                work_root=artifact_root / "private_codex_executor/candidates",
                reasoning_effort="high",
            )
            policy_generator = CodexExecGenerator(
                work_root=artifact_root / "private_codex_executor/policies",
                reasoning_effort="high",
                output_mode="plain_text",
            )
            summary = P2bCampaignRunner(
                plan=plan,
                registry=registry,
                dashboard=dashboard,
                candidate_generator=candidate_generator,
                policy_generator=policy_generator,
                adapter=adapter,
                profiler=profiler,
                tasks=tasks,
                task_cards=task_cards,
                reference_sources=references,
            ).run()
        except Exception as exc:
            registry.append(
                "p2b_blocked",
                {
                    "status": "blocked",
                    "detail": f"{type(exc).__name__}: {str(exc)[:1000]}",
                },
                event_id=(
                    f"p2b-blocked:{type(exc).__name__}:"
                    f"{hashlib.sha256(str(exc).encode()).hexdigest()[:16]}"
                ),
            )
            dashboard.render(registry)
            raise
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
