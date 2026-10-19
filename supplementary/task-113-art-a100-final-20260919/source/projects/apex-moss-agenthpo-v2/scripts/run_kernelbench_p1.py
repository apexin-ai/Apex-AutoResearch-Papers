#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from optimization_lab.adapters.ssh_kernelbench import SSHKernelBenchAdapter
from optimization_lab.campaign import ACTIVE_TASK_IDS, CampaignPlan
from optimization_lab.codex_generator import CodexExecGenerator
from optimization_lab.dashboard import Dashboard
from optimization_lab.p1_runner import P1CampaignRunner
from optimization_lab.registry import ExperimentRegistry
from optimization_lab.task_spec import TaskSpec


PROTOCOLS = Path(__file__).resolve().parents[1] / "optimization_lab/protocols"
TASK_CARDS = Path(__file__).resolve().parents[1] / "optimization_lab/task_cards"


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


def main() -> int:
    parser = argparse.ArgumentParser(description="Run only the frozen KernelBench P1 matrix")
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, required=True)
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
    project_root = args.project_root.resolve()
    plan = CampaignPlan.read(artifact_root / "campaign_plan.json")
    registry = ExperimentRegistry(artifact_root)
    dashboard = Dashboard(artifact_root / "dashboard.html")
    tasks = {task_id: _task(task_id) for task_id in ACTIVE_TASK_IDS}
    task_cards = {
        task_id: (TASK_CARDS / f"{task_id}.md").read_text(encoding="utf-8")
        for task_id in ACTIVE_TASK_IDS
    }
    references = {
        task_id: _remote_reference(args.ssh_host, args.remote_repository, task)
        for task_id, task in tasks.items()
    }
    generator = CodexExecGenerator(
        work_root=artifact_root / "private_codex_executor",
    )
    adapter = SSHKernelBenchAdapter(
        host=args.ssh_host,
        remote_repository=args.remote_repository,
        remote_root=args.remote_root,
        gpu_index=args.gpu_index,
        remote_uv=args.remote_uv,
    )
    runner = P1CampaignRunner(
        plan=plan,
        project_root=project_root,
        registry=registry,
        dashboard=dashboard,
        generator=generator,
        adapter=adapter,
        tasks=tasks,
        task_cards=task_cards,
        reference_sources=references,
    )
    try:
        summary = runner.run()
    except Exception as exc:
        registry.append(
            "p1_blocked",
            {"status": "blocked", "detail": f"{type(exc).__name__}: {str(exc)[:800]}"},
            event_id=f"p1-blocked:{type(exc).__name__}:{hashlib.sha256(str(exc).encode()).hexdigest()[:16]}",
        )
        dashboard.render(registry)
        raise
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
